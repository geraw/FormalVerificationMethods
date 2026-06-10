import { defineConfig } from 'vite';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.log('--- LOADING VITE.CONFIG.JS ---');

export default defineConfig({
    plugins: [
        {
            name: 'resolve-public-assets',
            enforce: 'pre',
            resolveId(id) {
                if (id.startsWith('/') && !id.startsWith('/@') && !id.includes('__slidev_') && !id.startsWith('/node_modules') && !id.startsWith('/index.html')) {
                    const publicPath = path.resolve(__dirname, 'public', id.slice(1));
                    if (fs.existsSync(publicPath) && fs.statSync(publicPath).isFile()) {
                        return publicPath;
                    }
                }
                return null;
            }
        }
    ]
});
