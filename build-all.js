import { execSync } from "child_process";
import fs from "fs";
import path from "path";

const REPO = "FormalVerificationMethods";

// Restore file timestamps from git to avoid unnecessary rebuilds
function restoreGitTimestamps() {
    try {
        const files = execSync('git ls-files -z', { encoding: 'utf8' })
            .split('\0')
            .filter(f => f);

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
        console.log('✓ Restored file timestamps from git history\n');
    } catch (err) {
        console.warn('⚠ Could not restore git timestamps:', err.message);
    }
}

function needsRebuild(sourceFile, targetFile) {
    if (!fs.existsSync(targetFile)) return true;
    
    const sourceStats = fs.statSync(sourceFile);
    const targetStats = fs.statSync(targetFile);
    
    return sourceStats.mtime > targetStats.mtime;
}

restoreGitTimestamps();

// Only include files starting with two digits + .md
const decks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && /^\d{2}-.*\.md$/.test(dirent.name))
    .map(dirent => dirent.name);

// Create dist directory if it doesn't exist, but DON'T delete it to keep incremental results
if (!fs.existsSync("dist")) {
    fs.mkdirSync("dist");
}

let builtCount = 0;
let skippedCount = 0;

// 1. Build index.md if changed
if (fs.existsSync("index.md")) {
    const target = path.join("dist", "index.html");
    if (needsRebuild("index.md", target)) {
        console.log(`\n▶ Building index.md as the root landing page...`);
        execSync(
            `npx slidev build index.md --base "/${REPO}/" -o dist`,
            { stdio: "inherit" }
        );
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
    const target = path.join(outputDir, "index.html");

    if (needsRebuild(file, target)) {
        console.log(`\n▶ Building ${file} into ${outputDir}/ ...`);
        
        // Remove old output for this specific deck to ensure clean build
        if (fs.existsSync(outputDir)) {
            fs.rmSync(outputDir, { recursive: true, force: true });
        }

        execSync(
            `npx slidev build ${file} --base "/${REPO}/${base}/" -o ${outputDir}`,
            { stdio: "inherit" }
        );
        builtCount++;
    } else {
        console.log(`⏭️  Skipping ${file} (up to date)`);
        skippedCount++;
    }
}

console.log(`\n🎉 Build summary:`);
console.log(`Built:   ${builtCount}`);
console.log(`Skipped: ${skippedCount}`);
