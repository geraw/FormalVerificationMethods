<template>
  <div class="nano-pg-runner" dir="ltr">
    <div class="runner-grid">
      <div class="runner-panel">
        <div class="runner-header">NanoPromela</div>
        <div class="editor-shell">
          <div class="runner-overlay" aria-hidden="true">
            <div class="runner-overlay-content" :style="overlayContentStyle">
              <span
                v-for="marker in visibleMarkerPositions"
                :key="marker.key"
                class="runner-inline-marker"
                :title="marker.title"
                :style="marker.style"
              ></span>
            </div>
          </div>

          <textarea
            ref="textareaRef"
            v-model="code"
            class="runner-textarea"
            rows="18"
            spellcheck="false"
            wrap="off"
            @scroll="syncOverlayScroll"
          />
        </div>

        <div class="runner-controls">
          <button class="runner-button" @click="run" :disabled="loading || running || !helperReady">
            {{ loading ? 'Loading Pyodide + Lark...' : running ? 'Running...' : 'Run' }}
          </button>

          <label class="runner-toggle">
            <input v-model="compactNames" type="checkbox">
            <span>Short location names</span>
          </label>

          <label class="runner-toggle">
            <input v-model="showCodeMarkers" type="checkbox">
            <span>Show code markers</span>
          </label>

          <div class="runner-summary" v-if="summaryText">{{ summaryText }}</div>
        </div>

        <pre v-if="errorText" class="runner-error">{{ errorText }}</pre>
      </div>

      <div class="runner-panel">
        <div class="runner-header">Program Graph</div>
        <div class="diagram-shell">
          <TransitionSystemD3
            v-if="diagramData"
            :width="width"
            :height="height"
            :auto="true"
            :zoomable="true"
            :show-zoom-controls="true"
            :states="diagramData.states"
            :transitions="diagramData.transitions"
          />
          <div v-else class="diagram-placeholder">
            The program graph will appear here after running the translation.
          </div>
        </div>
        <div v-if="diagramData" class="diagram-help-text">
          Zoom with the mouse wheel or trackpad pinch, and drag the background to pan.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import TransitionSystemD3 from './TransitionSystemD3.vue'

type RawState = {
  id: string
  shortText: string
  fullText: string
  shortWidth: number
  fullWidth: number
  anchorLine?: number | null
  anchorColumn?: number | null
  hasExactSourceMatch?: boolean
  initial?: boolean
  initialDirection?: 'left' | 'right' | 'top' | 'bottom'
  color?: string
  stroke?: string
  strokeWidth?: number
}

type RawTransition = {
  source: string
  target: string
  action?: string
  actionWidth?: number
  actionHeight?: number
  actionFontSize?: number
  loopDirection?: string
  loopRadius?: number
  loopLabelRadius?: number
  curve?: number
  stroke?: string
  strokeWidth?: number
}

type GraphData = {
  states: RawState[]
  transitions: RawTransition[]
  summary: {
    states: number
    transitions: number
    initial: number
  }
}

type DiagramState = {
  id: string
  text: string
  width: number
  initial?: boolean
  initialDirection?: 'left' | 'right' | 'top' | 'bottom'
  color?: string
  stroke?: string
  strokeWidth?: number
}

const props = withDefaults(defineProps<{
  src: string
  initialCode?: string
  width?: number
  height?: number
  initialCompactNames?: boolean
}>(), {
  width: 520,
  height: 380,
  initialCompactNames: true,
  initialCode: `if
:: x > 1 -> y := x + y
:: true  -> x := 0; y := x
fi`,
})

const code = ref(props.initialCode)
const compactNames = ref(props.initialCompactNames)
const loading = ref(true)
const running = ref(false)
const helperReady = ref(false)
const errorText = ref('')
const graphData = ref<GraphData | null>(null)
const textareaRef = ref<HTMLTextAreaElement | null>(null)
const showCodeMarkers = ref(true)
const scrollTop = ref(0)
const scrollLeft = ref(0)

let pyodide: any = null
let measureCanvas: HTMLCanvasElement | null = null

const LINE_HEIGHT = 18
const CODE_PADDING_X = 10
const CODE_PADDING_Y = 10
const MARKER_OFFSET_X = 8
const MARKER_STACK_Y = 5

const summaryText = computed(() => {
  if (!graphData.value) return ''
  const { states, transitions, initial } = graphData.value.summary
  return `${states} states, ${transitions} transitions, ${initial} initial`
})

const overlayContentStyle = computed(() => ({
  transform: `translate(${-scrollLeft.value}px, ${-scrollTop.value}px)`,
}))

const diagramData = computed(() => {
  if (!graphData.value) return null

  const states: DiagramState[] = graphData.value.states.map((state) => ({
    id: state.id,
    text: compactNames.value ? state.shortText : state.fullText,
    width: compactNames.value ? state.shortWidth : state.fullWidth,
    initial: state.initial,
    initialDirection: state.initialDirection,
    color: state.color,
    stroke: state.stroke,
    strokeWidth: state.strokeWidth,
  }))

  return {
    states,
    transitions: graphData.value.transitions,
  }
})

const markerPositions = computed(() => {
  const lines = code.value.split(/\r?\n/)
  const states = [...(graphData.value?.states ?? [])]
    .filter((state) =>
      state.shortText !== 'exit'
      && state.anchorLine
      && state.anchorColumn
    )
    .sort((a, b) =>
      (a.anchorLine! - b.anchorLine!)
      || (a.anchorColumn! - b.anchorColumn!)
      || a.shortText.localeCompare(b.shortText, 'en'),
    )

  const anchorCounts = new Map<string, number>()

  return states.map((state) => {
    const anchorKey = `${state.anchorLine}:${state.anchorColumn}`
    const stackIndex = anchorCounts.get(anchorKey) ?? 0
    anchorCounts.set(anchorKey, stackIndex + 1)
    const lineText = lines[state.anchorLine! - 1] ?? ''
    const prefixText = lineText.slice(0, Math.max(0, state.anchorColumn! - 1))

    return {
      key: state.id,
      title: compactNames.value ? `${state.shortText}: ${state.fullText}` : state.fullText,
      style: {
        left: `${CODE_PADDING_X + measurePrefixWidth(prefixText) - MARKER_OFFSET_X}px`,
        top: `${CODE_PADDING_Y + (state.anchorLine! - 1) * LINE_HEIGHT + stackIndex * MARKER_STACK_Y}px`,
      },
    }
  })
})

const visibleMarkerPositions = computed(() =>
  showCodeMarkers.value ? [...markerPositions.value, endCodeMarker.value] : [],
)

function measurePrefixWidth(text: string) {
  if (!text) return 0
  if (typeof document === 'undefined') return text.length * 7

  measureCanvas ??= document.createElement('canvas')
  const context = measureCanvas.getContext('2d')
  if (!context) return text.length * 7

  const style = textareaRef.value ? window.getComputedStyle(textareaRef.value) : null
  if (style?.font) {
    context.font = style.font
  } else {
    context.font = `12px "Fira Code", "Consolas", monospace`
  }

  let width = context.measureText(text).width
  const letterSpacing = style?.letterSpacing && style.letterSpacing !== 'normal'
    ? Number.parseFloat(style.letterSpacing)
    : 0

  if (Number.isFinite(letterSpacing) && letterSpacing !== 0) {
    width += Math.max(0, text.length - 1) * letterSpacing
  }

  return width
}

const endCodeMarker = computed(() => {
  const lines = code.value.split(/\r?\n/)
  const lastLineIndex = Math.max(0, lines.length - 1)
  const lastLine = lines[lastLineIndex] ?? ''

  return {
    key: '__end__',
    title: 'End of code',
    style: {
      left: `${CODE_PADDING_X + measurePrefixWidth(lastLine) - MARKER_OFFSET_X}px`,
      top: `${CODE_PADDING_Y + lastLineIndex * LINE_HEIGHT}px`,
    },
  }
})

async function loadPyodideFromCDN() {
  if ((window as any).loadPyodide) {
    return (window as any).loadPyodide
  }

  return new Promise<any>((resolve, reject) => {
    const script = document.createElement('script')
    script.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js'
    script.onload = () => resolve((window as any).loadPyodide)
    script.onerror = reject
    document.head.appendChild(script)
  })
}

async function ensureLarkInstalled() {
  if (!pyodide) return

  const hasLark = Boolean(pyodide.runPython(`
import importlib.util
importlib.util.find_spec("lark") is not None
`))

  if (hasLark) return

  await pyodide.loadPackage('micropip')
  await pyodide.runPythonAsync(`
import micropip
await micropip.install("lark")
`)
}

async function initialize() {
  try {
    const [helperResp, loadPyodide] = await Promise.all([
      fetch(props.src),
      loadPyodideFromCDN(),
    ])

    const helperSource = await helperResp.text()
    pyodide = await loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/',
    })

    await ensureLarkInstalled()
    await pyodide.runPythonAsync(helperSource)

    helperReady.value = true
    loading.value = false
    await run()
  } catch (error: any) {
    errorText.value = `Failed to initialize runner: ${error.message || String(error)}`
    loading.value = false
  }
}

async function run() {
  if (!pyodide || running.value || !helperReady.value) return

  running.value = true
  errorText.value = ''

  try {
    pyodide.globals.set('__nanopromela_code__', code.value)

    const jsonText = await pyodide.runPythonAsync(`
import json
json.dumps(nanopromela_to_pg_slidev_data(__nanopromela_code__))
`)

    graphData.value = JSON.parse(String(jsonText))
  } catch (error: any) {
    graphData.value = null
    errorText.value = String(error)
  } finally {
    running.value = false
  }
}

function syncOverlayScroll() {
  if (!textareaRef.value) return
  scrollTop.value = textareaRef.value.scrollTop
  scrollLeft.value = textareaRef.value.scrollLeft
}

onMounted(() => {
  void initialize()
})
</script>

<style scoped>
.nano-pg-runner {
  direction: ltr;
  text-align: left;
  max-width: 100%;
  max-height: 78vh;
  overflow: auto;
}

.runner-grid {
  display: grid;
  grid-template-columns: minmax(360px, 0.95fr) minmax(430px, 1.15fr);
  gap: 14px;
  align-items: start;
  min-width: 920px;
}

.runner-panel {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  padding: 10px;
}

.runner-header {
  color: #1d4ed8;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 8px;
}

.editor-shell {
  position: relative;
  border: 1px solid #334155;
  border-radius: 8px;
  overflow: hidden;
  background: #0f172a;
}

.runner-overlay {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 1;
}

.runner-overlay-content {
  position: absolute;
  inset: 0;
}

.runner-inline-marker {
  position: absolute;
  width: 0;
  height: 0;
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #facc15;
  filter: drop-shadow(0 0 0.5px #854d0e);
}

.runner-textarea {
  width: 100%;
  min-height: 360px;
  resize: vertical;
  border: none;
  background: #0f172a;
  color: #e2e8f0;
  padding: 10px;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 12px;
  line-height: 18px;
  tab-size: 2;
  white-space: pre;
}

.runner-textarea:focus {
  outline: none;
}

.runner-controls {
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.runner-button {
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 6px 16px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
}

.runner-button:disabled {
  opacity: 0.55;
  cursor: default;
}

.runner-toggle {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #334155;
}

.runner-summary {
  font-size: 12px;
  color: #334155;
}

.runner-error {
  margin-top: 8px;
  white-space: pre-wrap;
  background: #fff1f2;
  color: #be123c;
  border: 1px solid #fda4af;
  border-radius: 8px;
  padding: 8px;
  font-size: 11px;
  line-height: 1.45;
}

.diagram-shell {
  min-height: 412px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border: 1px dashed #cbd5e1;
  border-radius: 10px;
  overflow: hidden;
}

.diagram-placeholder {
  color: #64748b;
  font-size: 12px;
  padding: 20px;
  text-align: center;
}

.diagram-help-text {
  margin-top: 8px;
  font-size: 12px;
  color: #475569;
}
</style>
