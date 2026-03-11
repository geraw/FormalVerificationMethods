import { execSync } from "child_process";
import fs from "fs";
import path from "path";
import crypto from "crypto";

const REPO = "FormalVerificationMethods";

/**
 * Restores file modification times from git history.
 * Only touches files that are not modified in the working directory.
 */
function restoreGitTimestamps() {
    try {
        // Get list of files modified in working directory/staging
        const status = execSync('git status --porcelain', { encoding: 'utf8' });
        const modifiedFiles = new Set(
            status.split('\n')
                .map(line => line.slice(3).trim())
                .filter(f => f)
        );

        const files = execSync('git ls-files -z', { encoding: 'utf8' })
            .split('\0')
            .filter(f => f && !modifiedFiles.has(f));

        for (const file of files) {
            if (!fs.existsSync(file)) continue;

            const timestamp = execSync(
                `git log -1 --format=%ct -- "${file}"`,
                { encoding: 'utf8' }
            ).trim();

            if (timestamp) {
                const date = new Date(parseInt(timestamp) * 1000);
                fs.utimesSync(file, date, date);
            }
        }
        console.log('✓ Restored file timestamps from git history (excluding local modifications)\n');
    } catch (err) {
        console.warn('⚠ Could not restore git timestamps:', err.message);
    }
}

/**
 * Calculates a signature for the file based on its content hash and modification time.
 */
function getFileSignature(filePath) {
    const stats = fs.statSync(filePath);
    const content = fs.readFileSync(filePath);
    const hash = crypto.createHash('md5').update(content).digest('hex');
    return `${hash}_${stats.mtimeMs}`;
}

/**
 * Checks if a file needs to be rebuilt by comparing its signature with a stored one.
 */
function needsRebuild(sourceFile, outputDir) {
    const signatureFile = path.join(outputDir, ".build_signature");
    if (!fs.existsSync(signatureFile)) return true;
    
    const targetMain = path.join(outputDir, "index.html");
    if (!fs.existsSync(targetMain)) return true;

    const currentSignature = getFileSignature(sourceFile);
    const savedSignature = fs.readFileSync(signatureFile, 'utf8').trim();
    
    return currentSignature !== savedSignature;
}

function saveSignature(sourceFile, outputDir) {
    const signatureFile = path.join(outputDir, ".build_signature");
    const currentSignature = getFileSignature(sourceFile);
    fs.writeFileSync(signatureFile, currentSignature);
}

restoreGitTimestamps();

// Only include files starting with two digits + .md
const decks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && /^\d{2}-.*\.md$/.test(dirent.name))
    .map(dirent => dirent.name);

// Create dist directory if it doesn't exist
if (!fs.existsSync("dist")) {
    fs.mkdirSync("dist");
}

let builtCount = 0;
let skippedCount = 0;

// 1. Build index.md as the main landing page
if (fs.existsSync("index.md")) {
    // For root index, we check against a hidden folder to avoid collisions
    const rootIndexSigDir = path.join("dist", ".root_index_sig");
    if (!fs.existsSync(rootIndexSigDir)) fs.mkdirSync(rootIndexSigDir);
    
    if (needsRebuild("index.md", rootIndexSigDir) || !fs.existsSync("dist/index.html")) {
        console.log(`\n▶ Building index.md as the root landing page...`);
        execSync(
            `npx slidev build index.md --base "/${REPO}/" -o dist`,
            { stdio: "inherit" }
        );
        saveSignature("index.md", rootIndexSigDir);
        builtCount++;
    } else {
        console.log(`⏭️  Skipping index.md (up to date)`);
        skippedCount++;
    }
}

// 2. Build each deck only if changed
for (const file of decks) {
    const base = file.replace(/\.md$/, "");
    const outputDir = path.join("dist", base);

    if (needsRebuild(file, outputDir)) {
        console.log(`\n▶ Building ${file} into ${outputDir}/ ...`);
        
        // Ensure outputDir exists
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        execSync(
            `npx slidev build ${file} --base "/${REPO}/${base}/" -o ${outputDir}`,
            { stdio: "inherit" }
        );
        saveSignature(file, outputDir);
        builtCount++;
    } else {
        console.log(`⏭️  Skipping ${file} (up to date)`);
        skippedCount++;
    }
}

console.log(`\n🎉 Build summary:`);
console.log(`Built:   ${builtCount}`);
console.log(`Skipped: ${skippedCount}`);
