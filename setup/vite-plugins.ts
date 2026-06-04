function disableRecordingDurationFix() {
    return {
        name: 'disable-recording-duration-fix',
        enforce: 'pre',
        transform(code: string, id: string) {
            const targetImport = "import { fixWebmDuration } from '@fix-webm-duration/fix'"
            if (!id.includes('@slidev/client') || !code.includes(targetImport))
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

export default function vitePlugins() {
    return [disableRecordingDurationFix()]
}
