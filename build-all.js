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

/**
 * Calculates a content hash for the file.
 * We use content-only hashing to ensure robustness against flaky timestamps.
 */
function getFileHash(filePath) {
    const content = fs.readFileSync(filePath);
    return crypto.createHash('sha1').update(content).digest('hex');
}

function quote(value) {
    return `"${String(value).replace(/"/g, '\\"')}"`;
}

function runSlidev(command, args) {
    const quotedArgs = args.map(quote).join(" ");
    execSync(`npx slidev ${command} ${quotedArgs}`, { stdio: "inherit" });
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

    if (!fs.existsSync(signatureFile)) return { rebuild: true, reason: "Missing signature file" };
    const missingTarget = actualTargets.find(target => !fs.existsSync(target));
    if (missingTarget) {
        return { rebuild: true, reason: `Missing output file (${path.basename(missingTarget)})` };
    }

    const currentHash = getFileHash(sourceFile);
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
    const currentHash = getFileHash(sourceFile);
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
const decks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && /^\d{2}-.*\.md$/.test(dirent.name))
    .map(dirent => dirent.name);

const deckBases = new Set(decks.map(file => file.replace(/\.md$/, "")));

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

console.log(`🔍 Checking for updates in ${decks.length + 1} files...`);

// 1. Build index.md as the main landing page
if (fs.existsSync("index.md")) {
    const result = needsRebuild("index.md", "dist", [path.join("dist", "index.html")]);
    
    if (result.rebuild) {
        console.log(`\n▶ [REBUILD] index.md (${result.reason})`);
        const tempIndexDir = path.join(".slidev-temp", "index");
        fs.rmSync(tempIndexDir, { recursive: true, force: true });
        fs.mkdirSync(path.dirname(tempIndexDir), { recursive: true });
        runSlidev("build", ["index.md", "--base", `/${REPO}/`, "-o", tempIndexDir]);
        replaceRootDistContents(tempIndexDir, "dist", deckBases);
        fs.rmSync(".slidev-temp", { recursive: true, force: true });
        saveSignature("index.md", "dist");
        builtCount++;
    } else {
        console.log(`⏭️  [SKIP] index.md (up to date)`);
        skippedCount++;
    }
}

// 2. Build each deck into its own directory
for (const file of decks) {
    const base = file.replace(/\.md$/, "");
    const outputDir = path.join("dist", base);
    const pdfOutput = path.join(outputDir, `${base}.pdf`);
    const result = needsRebuild(file, outputDir, [
        path.join(outputDir, "index.html"),
        pdfOutput,
    ]);

    if (result.rebuild) {
        console.log(`\n▶ [REBUILD] ${file} (${result.reason})`);
        
        // Clean target directory to ensure fresh build
        if (fs.existsSync(outputDir)) {
            fs.rmSync(outputDir, { recursive: true, force: true });
        }
        fs.mkdirSync(outputDir, { recursive: true });

        runSlidev("build", [file, "--base", `/${REPO}/${base}/`, "-o", outputDir]);
        exportPdfWithRetry(file, pdfOutput);
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
