function disableRecordingDurationFix() {
    return {
        name: 'disable-recording-duration-fix',
        enforce: 'pre',
        transform(code: string, id: string) {
            const normalizedId = id.replace(/\\/g, '/');
            const targetImport = "import { fixWebmDuration } from '@fix-webm-duration/fix'"
            if (!normalizedId.includes('@slidev/client') || !code.includes(targetImport))
                return null

            return {
                code: code.replace(
                    targetImport,
                    'async function fixWebmDuration(blob: Blob) {\n    return blob\n}',
                ),
                map: null,
            }
        },
    }
}

function fixSlidevHashRouteBase() {
    return {
        name: 'fix-slidev-hash-route-base',
        enforce: 'pre',
        transform(code: string, id: string) {
            const normalizedId = id.replace(/\\/g, '/');
            if (normalizedId.includes('@slidev/client')) {
                let changed = false;
                let newCode = code;
                if (newCode.includes('createWebHashHistory(import.meta.env.BASE_URL)')) {
                    newCode = newCode.replace(
                        'createWebHashHistory(import.meta.env.BASE_URL)',
                        "createWebHashHistory('/')",
                    );
                    changed = true;
                }
                if (newCode.includes('return `${import.meta.env.BASE_URL}${path}`')) {
                    newCode = newCode.replace(
                        'return `${import.meta.env.BASE_URL}${path}`',
                        'return __SLIDEV_HASH_ROUTE__ ? `/${path}` : `${import.meta.env.BASE_URL}${path}`',
                    );
                    changed = true;
                }
                if (changed) {
                    return {
                        code: newCode,
                        map: null,
                    }
                }
            }
            return null
        },
    }
}

export default function vitePlugins() {
    return [disableRecordingDurationFix(), fixSlidevHashRouteBase()]
}
