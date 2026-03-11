import { execSync } from "child_process";
import fs from "fs";
import path from "path";
import crypto from "crypto";

const REPO = "FormalVerificationMethods";

/**
 * Calculates a content hash for the file.
 * We use content-only hashing to ensure robustness against flaky timestamps.
 */
function getFileHash(filePath) {
    const content = fs.readFileSync(filePath);
    return crypto.createHash('sha1').update(content).digest('hex');
}

/**
 * Checks if a file needs to be rebuilt by comparing its hash with a stored one.
 */
function needsRebuild(sourceFile, outputDir, targetFile = null) {
    const signatureFile = path.join(outputDir, ".build_hash");
    const actualTarget = targetFile || path.join(outputDir, "index.html");

    if (!fs.existsSync(signatureFile)) return { rebuild: true, reason: "Missing signature file" };
    if (!fs.existsSync(actualTarget)) return { rebuild: true, reason: "Missing output file" };

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

// 0. Setup dist
if (!fs.existsSync("dist")) {
    fs.mkdirSync("dist");
}

// Get all .md files starting with 2 digits
const decks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && /^\d{2}-.*\.md$/.test(dirent.name))
    .map(dirent => dirent.name);

let builtCount = 0;
let skippedCount = 0;

console.log(`🔍 Checking for updates in ${decks.length + 1} files...`);

// 1. Build index.md as the main landing page
if (fs.existsSync("index.md")) {
    const result = needsRebuild("index.md", "dist", path.join("dist", "index.html"));
    
    if (result.rebuild) {
        console.log(`\n▶ [REBUILD] index.md (${result.reason})`);
        execSync(
            `npx slidev build index.md --base "/${REPO}/" -o dist`,
            { stdio: "inherit" }
        );
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
    const result = needsRebuild(file, outputDir);

    if (result.rebuild) {
        console.log(`\n▶ [REBUILD] ${file} (${result.reason})`);
        
        // Clean target directory to ensure fresh build
        if (fs.existsSync(outputDir)) {
            fs.rmSync(outputDir, { recursive: true, force: true });
        }
        fs.mkdirSync(outputDir, { recursive: true });

        execSync(
            `npx slidev build ${file} --base "/${REPO}/${base}/" -o ${outputDir}`,
            { stdio: "inherit" }
        );
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
