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

restoreGitTimestamps();

const decks = fs
    .readdirSync(process.cwd(), { withFileTypes: true })
    .filter(dirent => dirent.isFile() && dirent.name.endsWith(".md") && !dirent.name.startsWith("_"))
    .map(dirent => dirent.name);

if (fs.existsSync("dist")) {
    fs.rmSync("dist", { recursive: true, force: true });
}
fs.mkdirSync("dist");

// 1. Build index.md as the main landing page (index.html)
if (fs.existsSync("index.md")) {
    console.log(`\n▶ Building index.md as the root landing page...`);
    execSync(
        `npx slidev build index.md --base "/${REPO}/" -o dist`,
        { stdio: "inherit" }
    );
}

// 2. Build each deck into its own isolated directory
// This provides clean URLs (e.g., /00-intro/) and avoids asset collisions
let builtCount = 0;
for (const file of decks) {
    const base = file.replace(/\.md$/, "");
    if (base === 'index') continue;

    const outputDir = path.join("dist", base);
    console.log(`\n▶ Building ${file} into ${outputDir}/ ...`);

    execSync(
        `npx slidev build ${file} --base "/${REPO}/${base}/" -o ${outputDir}`,
        { stdio: "inherit" }
    );
    builtCount++;
}

console.log(`\n🎉 Build complete!`);
console.log(`Built ${builtCount} decks + 1 index page.`);
