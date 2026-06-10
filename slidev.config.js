import process from 'node:process';

if (process.platform === 'win32') {
    const cwd = process.cwd();
    const normalized = cwd.replace(/^[a-z]:/i, m => m.toUpperCase());
    if (cwd !== normalized) {
        process.chdir(normalized);
    }
}

export default {
    fonts: {
        sans: 'Noto Sans Hebrew',
        mono: 'Fira Code',
    },
    vite: {
        build: {
            emptyOutDir: false,
        },
        optimizeDeps: {
            include: ['d3', 'katex'],
        },
    },
}



