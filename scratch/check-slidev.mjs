import { chromium } from 'playwright-chromium';

const browser = await chromium.launch();
const page = await browser.newPage();
const errors = [];
page.on('console', msg => {
  if (msg.type() === 'error' || msg.type() === 'warning') errors.push(`[${msg.type()}] ` + msg.text());
});
page.on('pageerror', err => errors.push('pageerror: ' + err.message));

await page.goto('http://localhost:3721/overview/', { waitUntil: 'networkidle', timeout: 30000 });
await page.waitForTimeout(3000);

console.log('ERRORS_FOUND:', errors.length);
for (const e of errors) console.log(' -', e);

await browser.close();
