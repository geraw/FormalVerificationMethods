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
            if (normalizedId.includes('@slidev/client') && code.includes('createWebHashHistory(import.meta.env.BASE_URL)')) {
                return {
                    code: code.replace(
                        'createWebHashHistory(import.meta.env.BASE_URL)',
                        "createWebHashHistory('/')",
                    ),
                    map: null,
                }
            }
            return null
        },
    }
}

export default function vitePlugins() {
    return [disableRecordingDurationFix(), fixSlidevHashRouteBase()]
}
