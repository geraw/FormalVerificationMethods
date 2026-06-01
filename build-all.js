import { execSync } from "child_process";
import fs from "fs";
import path from "path";
import crypto from "crypto";

const REPO = "FormalVerificationMethods";
const MIN_VALID_PDF_SIZE_BYTES = 10 * 1024;
const PDF_EXPORT_ARGS = [
    "--wait-until", "networkidle",
    "--wait", "1000",
    "--timeout", "120000",
];
const GLOBAL_DEPENDENCY_PATHS = [
    "build-all.js",
    "package.json",
    "package-lock.json",
    "slidev.config.js",
    "styles.css",
    "components",
    "setup",
];
const ASSET_ROOTS = ["public", "images"];
const FORCE_REBUILD = process.env.FORCE_REBUILD === "1" || process.env.FORCE_REBUILD === "true";
const SKIP_PDF_EXPORT = process.env.SKIP_PDF_EXPORT === "1" || process.env.SKIP_PDF_EXPORT === "true";
const TARGET_DECK = (process.env.TARGET_DECK || "").trim();

/**
 * Calculates a content hash for the file.
 * We use content-only hashing to ensure robustness against flaky timestamps.
 */
function getFileHash(filePath) {
    const content = fs.readFileSync(filePath);
    return crypto.createHash('sha1').update(content).digest('hex');
}

function listFilesRecursive(targetPath) {
    if (!fs.existsSync(targetPath)) return [];

    const stat = fs.statSync(targetPath);
    if (stat.isFile()) return [targetPath];
    if (!stat.isDirectory()) return [];

    return fs
        .readdirSync(targetPath, { withFileTypes: true })
        .flatMap(entry => listFilesRecursive(path.join(targetPath, entry.name)))
        .sort();
}

function addIfExists(files, filePath) {
    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
        files.push(filePath);
    }
}

function getReferencedAssets(sourceFile) {
    const content = fs.readFileSync(sourceFile, "utf8");
    const files = [];
    const patterns = [
        /(?:src|href)=["']\/([^"']+)["']/g,
        /!\[[^\]]*]\(([^)]+)\)/g,
        /\[[^\]]*]\(([^)]+)\)/g,
    ];

    for (const pattern of patterns) {
        for (const match of content.matchAll(pattern)) {
            const rawRef = match[1].split(/[?#]/)[0];
            if (!rawRef || /^[a-z]+:/i.test(rawRef)) continue;

            const normalized = rawRef.replace(/\\/g, "/").replace(/^\/+/, "");
            const candidates = [];

            if (ASSET_ROOTS.some(root => normalized === root || normalized.startsWith(`${root}/`))) {
                candidates.push(normalized);
            } else {
                candidates.push(path.join(path.dirname(sourceFile), normalized));
                candidates.push(path.join("public", normalized));
                candidates.push(path.join("images", normalized));
            }

            for (const candidate of candidates) {
                addIfExists(files, candidate);
            }
        }
    }

    return files;
}

function getBuildHash(sourceFile) {
    const files = [
        sourceFile,
        ...GLOBAL_DEPENDENCY_PATHS.flatMap(listFilesRecursive),
        ...getReferencedAssets(sourceFile),
    ];

    const hash = crypto.createHash("sha1");
    for (const file of [...new Set(files)].sort()) {
        hash.update(path.relative(process.cwd(), file));
        hash.update("\0");
        hash.update(fs.readFileSync(file));
        hash.update("\0");
    }

    return hash.digest("hex");
}

function quote(value) {
    return `"${String(value).replace(/"/g, '\\"')}"`;
}

function runSlidev(command, args) {
    const quotedArgs = args.map(quote).join(" ");
    execSync(`npx slidev ${command} ${quotedArgs}`, { stdio: "inherit" });
}

function getBuildArgs(sourceFile, basePath, outputDir) {
    const args = [sourceFile, "--base", basePath, "-o", outputDir];
    if (SKIP_PDF_EXPORT) {
        // Frontmatter sets download: true on decks; disable it in CI to avoid Playwright.
        args.push("--download", "false");
    }
    return args;
}

function exportPdfWithRetry(sourceFile, outputFile, maxAttempts = 2) {
    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
        runSlidev("export", [sourceFile, "--output", outputFile, ...PDF_EXPORT_ARGS]);

        if (fs.existsSync(outputFile) && fs.statSync(outputFile).size >= MIN_VALID_PDF_SIZE_BYTES) {
            return;
        }

        console.warn(`\n[WARN] PDF export for ${sourceFile} looks incomplete after attempt ${attempt}/${maxAttempts}.`);
    }

    throw new Error(`Failed to export a valid PDF for ${sourceFile}`);
}

/**
 * Checks if a file needs to be rebuilt by comparing its hash with a stored one.
 */
function needsRebuild(sourceFile, outputDir, targetFiles = []) {
    const signatureFile = path.join(outputDir, ".build_hash");
    const actualTargets = targetFiles.length > 0
        ? targetFiles
        : [path.join(outputDir, "index.html")];

    if (FORCE_REBUILD) return { rebuild: true, reason: "Forced rebuild" };
    if (!fs.existsSync(signatureFile)) return { rebuild: true, reason: "Missing signature file" };
    const missingTarget = actualTargets.find(target => !fs.existsSync(target));
    if (missingTarget) {
        return { rebuild: true, reason: `Missing output file (${path.basename(missingTarget)})` };
    }

    const currentHash = getBuildHash(sourceFile);
    const savedHash = fs.readFileSync(signatureFile, 'utf8').trim();
    
    if (currentHash !== savedHash) {
        return { rebuild: true, reason: "Content changed" };
    }
    
    return { rebuild: false };
}

function saveSignature(sourceFile, outputDir) {
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }
    const signatureFile = path.join(outputDir, ".build_hash");
    const currentHash = getBuildHash(sourceFile);
    fs.writeFileSync(signatureFile, currentHash);
}

function replaceRootDistContents(tempDir, distDir, preservedDirs = new Set()) {
    for (const entry of fs.readdirSync(distDir, { withFileTypes: true })) {
        if (entry.isDirectory() && preservedDirs.has(entry.name)) continue;
        fs.rmSync(path.join(distDir, entry.name), { recursive: true, force: true });
    }

    fs.cpSync(tempDir, distDir, { recursive: true });
}

// 0. Setup dist
if (!fs.existsSync("dist")) {
    fs.mkdirSync("dist");
}

// Get all .md files starting with 2 digits
const allDecks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && /^\d{2}-.*\.md$/.test(dirent.name))
    .map(dirent => dirent.name);

let decks = allDecks;
if (TARGET_DECK) {
    const normalizedTarget = TARGET_DECK.endsWith(".md") ? TARGET_DECK : `${TARGET_DECK}.md`;
    decks = allDecks.filter(file => file === normalizedTarget || file.replace(/\.md$/, "") === TARGET_DECK);

    if (decks.length === 0) {
        throw new Error(`TARGET_DECK was set to '${TARGET_DECK}', but no matching deck was found.`);
    }
}

const deckBases = new Set(allDecks.map(file => file.replace(/\.md$/, "")));

let builtCount = 0;
let skippedCount = 0;
let removedCount = 0;

for (const entry of fs.readdirSync("dist", { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    if (!/^\d{2}-.*$/.test(entry.name)) continue;
    if (deckBases.has(entry.name)) continue;

    const staleDir = path.join("dist", entry.name);
    console.log(`\n[REMOVE] ${staleDir} (source deck no longer exists)`);
    fs.rmSync(staleDir, { recursive: true, force: true });
    removedCount++;
}

const totalCandidates = decks.length + (TARGET_DECK ? 0 : 1);
console.log(`🔍 Checking for updates in ${totalCandidates} files...`);
if (SKIP_PDF_EXPORT) {
    console.log(`📄 PDF export is disabled (SKIP_PDF_EXPORT=1)`);
}
if (TARGET_DECK) {
    console.log(`🎯 Building target deck only: ${decks[0]}`);
}

// 1. Build index.md as the main landing page
if (!TARGET_DECK && fs.existsSync("index.md")) {
    const result = needsRebuild("index.md", "dist", [path.join("dist", "index.html")]);
    
    if (result.rebuild) {
        console.log(`\n▶ [REBUILD] index.md (${result.reason})`);
        const tempIndexDir = path.join(".slidev-temp", "index");
        fs.rmSync(tempIndexDir, { recursive: true, force: true });
        fs.mkdirSync(path.dirname(tempIndexDir), { recursive: true });
        runSlidev("build", getBuildArgs("index.md", `/${REPO}/`, tempIndexDir));
        replaceRootDistContents(tempIndexDir, "dist", deckBases);
        fs.rmSync(".slidev-temp", { recursive: true, force: true });
        saveSignature("index.md", "dist");
        builtCount++;
    } else {
        console.log(`⏭️  [SKIP] index.md (up to date)`);
        skippedCount++;
    }
} else if (TARGET_DECK) {
    console.log(`⏭️  [SKIP] index.md (TARGET_DECK mode)`);
}

// 2. Build each deck into its own directory
for (const file of decks) {
    const base = file.replace(/\.md$/, "");
    const outputDir = path.join("dist", base);
    const pdfOutput = path.join(outputDir, `${base}.pdf`);
    const requiredTargets = [path.join(outputDir, "index.html")];
    if (!SKIP_PDF_EXPORT) {
        requiredTargets.push(pdfOutput);
    }
    const result = needsRebuild(file, outputDir, requiredTargets);

    if (result.rebuild) {
        console.log(`\n▶ [REBUILD] ${file} (${result.reason})`);
        
        // Clean target directory to ensure fresh build
        if (fs.existsSync(outputDir)) {
            fs.rmSync(outputDir, { recursive: true, force: true });
        }
        fs.mkdirSync(outputDir, { recursive: true });

        runSlidev("build", getBuildArgs(file, `/${REPO}/${base}/`, outputDir));
        if (!SKIP_PDF_EXPORT) {
            exportPdfWithRetry(file, pdfOutput);
        }
        saveSignature(file, outputDir);
        builtCount++;
    } else {
        console.log(`⏭️  [SKIP] ${file} (up to date)`);
        skippedCount++;
    }
}

console.log(`\n🎉 Build complete!`);
console.log(`Built:   ${builtCount}`);
console.log(`Skipped: ${skippedCount}`);
console.log(`Removed: ${removedCount}`);
