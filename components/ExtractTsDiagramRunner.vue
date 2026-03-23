<template>
  <div class="extract-ts-runner" dir="ltr">
    <div class="runner-grid">
      <div class="runner-panel">
        <div class="runner-header">extract_ts(...)</div>
        <textarea
          v-model="expression"
          class="runner-textarea"
          rows="10"
          spellcheck="false"
        />
        <div class="runner-controls">
          <button class="runner-button" @click="run" :disabled="loading || running || !helperReady">
            {{ loading ? 'Loading Pyodide...' : running ? 'Running...' : 'Run' }}
          </button>
          <div class="runner-summary" v-if="summaryText">{{ summaryText }}</div>
        </div>
        <pre v-if="errorText" class="runner-error">{{ errorText }}</pre>
        <div v-else class="runner-help">
          Edit the call to <code>extract_ts</code>, then click <code>Run</code>.
        </div>
      </div>

      <div class="runner-panel">
        <div class="runner-header">Transition System</div>
        <div class="diagram-shell">
          <TransitionSystemD3
            v-if="graphData"
            :width="width"
            :height="height"
            :auto="true"
            :zoomable="true"
            :show-zoom-controls="true"
            :states="graphData.states"
            :transitions="graphData.transitions"
          />
          <div v-else class="diagram-placeholder">
            The graph will appear here after running <code>extract_ts(...)</code>.
          </div>
        </div>
        <div v-if="graphData" class="diagram-help-text">
          Zoom with the mouse wheel or trackpad pinch, and drag the background to pan.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import TransitionSystemD3 from './TransitionSystemD3.vue'

type GraphState = {
  id: string
  text?: string
  label?: string
  width?: number
  initial?: boolean
  initialDirection?: 'left' | 'right' | 'top' | 'bottom'
}

type GraphTransition = {
  source: string
  target: string
  action?: string
  loopDirection?: string
  actionWidth?: number
  actionY?: number
}

type GraphData = {
  states: GraphState[]
  transitions: GraphTransition[]
}

const props = withDefaults(defineProps<{
  src: string
  width?: number
  height?: number
  initialExpression?: string
}>(), {
  width: 430,
  height: 300,
  initialExpression: `extract_ts(
  1,
  [0],
  lambda x, r: [x[0] | r[0]],
  lambda x, r: not (x[0] ^ r[0]),
)`,
})

const expression = ref(props.initialExpression)
const loading = ref(true)
const running = ref(false)
const helperReady = ref(false)
const errorText = ref('')
const summaryText = ref('')
const graphData = ref<GraphData | null>(null)

let pyodide: any = null

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
    pyodide.globals.set('__extract_expr__', expression.value)

    const jsonText = await pyodide.runPythonAsync(`
import json
__ts_result = eval(__extract_expr__)
json.dumps(ts_to_slidev_data(__ts_result))
`)

    const parsed = JSON.parse(String(jsonText))
    graphData.value = {
      states: parsed.states,
      transitions: parsed.transitions,
    }
    summaryText.value = `${parsed.summary.states} states, ${parsed.summary.transitions} transitions, ${parsed.summary.initial} initial`
  } catch (error: any) {
    graphData.value = null
    summaryText.value = ''
    errorText.value = String(error)
  } finally {
    running.value = false
  }
}

onMounted(() => {
  void initialize()
})
</script>

<style scoped>
.extract-ts-runner {
  direction: ltr;
  text-align: left;
}

.runner-grid {
  display: grid;
  grid-template-columns: minmax(320px, 1fr) minmax(360px, 1.1fr);
  gap: 14px;
  align-items: start;
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

.runner-textarea {
  width: 100%;
  min-height: 220px;
  resize: vertical;
  border: 1px solid #334155;
  border-radius: 8px;
  background: #0f172a;
  color: #e2e8f0;
  padding: 10px;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 12px;
  line-height: 1.5;
  tab-size: 2;
}

.runner-controls {
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 10px;
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

.runner-summary {
  font-size: 12px;
  color: #334155;
}

.runner-help {
  margin-top: 8px;
  font-size: 12px;
  color: #475569;
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
  min-height: 335px;
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
