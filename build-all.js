import { execSync } from "child_process";
import crypto from "crypto";
import fs from "fs";
import path from "path";

// Normalize CWD drive letter to uppercase on Windows to prevent Vite path resolution errors
if (process.platform === "win32") {
    const cwd = process.cwd();
    const normalized = cwd.replace(/^[a-z]:/i, m => m.toUpperCase());
    if (cwd !== normalized) {
        process.chdir(normalized);
    }
}

const REPO = process.env.REPO_NAME || "FormalVerificationMethods";
const FORCE_REBUILD = process.env.FORCE_REBUILD === "1" || process.env.FORCE_REBUILD === "true";
const COPIED_PUBLIC_DIRS = [
    "slide-backgrounds",
    "slide-reference",
    "extracted",
    "__pycache__",
];


function quote(value) {
    return `"${String(value).replace(/"/g, '\\"')}"`;
}

function fileHash(filePath) {
    return crypto.createHash("sha1").update(fs.readFileSync(filePath)).digest("hex");
}

function buildSignature(sourceFile) {
    const hash = crypto.createHash("sha1");
    const signatureInputs = [
        sourceFile,
        "build-all.js",
        "slidev.config.js",
        "vite.config.js",
        "setup/vite-plugins.ts",
        "package-lock.json",
        "package.json",
    ];

    for (const file of signatureInputs) {
        if (!fs.existsSync(file)) continue;
        hash.update(file);
        hash.update("\0");
        hash.update(fs.readFileSync(file));
        hash.update("\0");
    }

    hash.update(JSON.stringify({
        repo: REPO,
        routerMode: "hash",
        download: false,
        copiedPublicDirs: COPIED_PUBLIC_DIRS,
    }));

    return hash.digest("hex");
}

function resolveAbsoluteAssetRef(rawRef) {
    if (!rawRef.startsWith("/") || rawRef.startsWith("//")) return rawRef;

    const match = rawRef.match(/^\/([^?#]+)(.*)$/);
    if (!match) return rawRef;

    const relativePath = match[1];
    const suffix = match[2] || "";
    const candidates = [
        path.join("public", relativePath),
        relativePath,
        path.join("images", relativePath),
    ];

    for (const candidate of candidates) {
        if (fs.existsSync(candidate) && fs.statSync(candidate).isFile()) {
            return `./${candidate.replace(/\\/g, "/")}${suffix}`;
        }
    }

    return rawRef;
}

function prepareBuildSource(sourceFile) {
    const original = fs.readFileSync(sourceFile, "utf8");
    let updated = original;

    if (/^---\r?\n/.test(updated)) {
        if (/^routerMode:/m.test(updated)) {
            updated = updated.replace(/^routerMode:.*$/m, "routerMode: hash");
        } else {
            updated = updated.replace(/^---(\r?\n)/, "---$1routerMode: hash$1");
        }

        if (/^download:/m.test(updated)) {
            updated = updated.replace(/^download:.*$/m, "download: false");
        } else {
            updated = updated.replace(/^---(\r?\n)/, "---$1download: false$1");
        }
    }

    // Rewrite absolute image refs (e.g. ![](/logo.png)) to concrete local files.
    updated = updated.replace(/!\[([^\]]*)\]\((\/[^)]+)\)/g, (_m, altText, rawRef) => {
        const resolved = resolveAbsoluteAssetRef(rawRef);
        return `![${altText}](${resolved})`;
    });

    // Rewrite html src="/..." image refs.
    updated = updated.replace(/src=["']\/(.+?)["']/g, (_m, rawRef) => {
        const resolved = resolveAbsoluteAssetRef(`/${rawRef}`);
        return `src="${resolved}"`;
    });

    if (updated === original) {
        return { buildFile: sourceFile, cleanup: () => {} };
    }

    const tempFile = path.join(process.cwd(), `.slidev-build-${path.basename(sourceFile)}`);
    fs.writeFileSync(tempFile, updated);

    return {
        buildFile: tempFile,
        cleanup: () => {
            fs.rmSync(tempFile, { force: true });
        },
    };
}

function runSlidevBuild(sourceFile, basePath, outputDir) {
    const prepared = prepareBuildSource(sourceFile);
    const args = [
        prepared.buildFile,
        "--base", basePath,
        "-o", outputDir,
        "--download", "false",
    ];
    try {
        execSync(`npx slidev build ${args.map(quote).join(" ")}`, { stdio: "inherit" });
    } finally {
        prepared.cleanup();
    }
}

function signaturePath(outputDir) {
    return path.join(outputDir, ".md_hash");
}

function removeCopiedPublicDirs(outputDir) {
    for (const dirname of COPIED_PUBLIC_DIRS) {
        fs.rmSync(path.join(outputDir, dirname), { recursive: true, force: true });
    }
}

function needsBuild(sourceFile, outputDir) {
    if (FORCE_REBUILD) return { rebuild: true, reason: "forced rebuild" };
    const sigPath = signaturePath(outputDir);
    const indexPath = path.join(outputDir, "index.html");
    if (!fs.existsSync(sigPath)) return { rebuild: true, reason: "missing signature" };
    if (!fs.existsSync(indexPath)) return { rebuild: true, reason: "missing index.html" };

    const current = buildSignature(sourceFile);
    const previous = fs.readFileSync(sigPath, "utf8").trim();
    return current === previous
        ? { rebuild: false }
        : { rebuild: true, reason: "source or build config changed" };
}

function writeSignature(sourceFile, outputDir) {
    fs.mkdirSync(outputDir, { recursive: true });
    fs.writeFileSync(signaturePath(outputDir), buildSignature(sourceFile));
}

function discoverDecks() {
    return fs
        .readdirSync(process.cwd(), { withFileTypes: true })
        .filter((entry) => entry.isFile() && /^\d{2}-.*\.md$/.test(entry.name))
        .map((entry) => entry.name)
        .sort();
}

function removeDeletedDeckOutputs(deckBases) {
    if (!fs.existsSync("dist")) return 0;
    let removed = 0;
    for (const entry of fs.readdirSync("dist", { withFileTypes: true })) {
        if (!entry.isDirectory()) continue;
        if (!/^\d{2}-/.test(entry.name)) continue;
        if (deckBases.has(entry.name)) continue;
        fs.rmSync(path.join("dist", entry.name), { recursive: true, force: true });
        removed++;
    }
    return removed;
}

if (!fs.existsSync("dist")) {
    fs.mkdirSync("dist", { recursive: true });
}

const allDecks = discoverDecks();
const decks = allDecks.filter((file) => file === "00-intro.md");
const deckBases = new Set(allDecks.map((file) => file.replace(/\.md$/, "")));
const removedCount = removeDeletedDeckOutputs(deckBases);

let builtCount = 0;
let skippedCount = 0;

console.log(`Checking ${decks.length + 1} markdown files for changes...`);

if (fs.existsSync("index.md")) {
    const indexResult = needsBuild("index.md", "dist");
    if (indexResult.rebuild) {
        console.log(`[BUILD] index.md (${indexResult.reason})`);
        runSlidevBuild("index.md", `/${REPO}/`, "dist");
        writeSignature("index.md", "dist");
        builtCount++;
    } else {
        console.log(`[SKIP] index.md`);
        skippedCount++;
    }
}

for (const file of decks) {
    const base = file.replace(/\.md$/, "");
    const outputDir = path.join("dist", base);
    const result = needsBuild(file, outputDir);

    if (!result.rebuild) {
        console.log(`[SKIP] ${file}`);
        removeCopiedPublicDirs(outputDir);
        skippedCount++;
        continue;
    }

    console.log(`[BUILD] ${file} (${result.reason})`);
    fs.rmSync(outputDir, { recursive: true, force: true });
    fs.mkdirSync(outputDir, { recursive: true });
    runSlidevBuild(file, `/${REPO}/${base}/`, outputDir);
    removeCopiedPublicDirs(outputDir);
    writeSignature(file, outputDir);
    builtCount++;
}

console.log("Build complete.");
console.log(`Built:   ${builtCount}`);
console.log(`Skipped: ${skippedCount}`);
console.log(`Removed: ${removedCount}`);

