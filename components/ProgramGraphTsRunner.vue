<template>
  <div class="pg-ts-runner" dir="ltr">
    <div class="runner-grid">
      <div class="runner-panel">
        <div class="runner-header">pg_to_ts(...)</div>
        <textarea
          v-model="expression"
          class="runner-textarea"
          rows="14"
          spellcheck="false"
        />
        <div class="runner-controls">
          <button class="runner-button" @click="run" :disabled="loading || running || !helperReady">
            {{ loading ? 'Loading Pyodide...' : running ? 'Running...' : 'Run' }}
          </button>
          <div class="runner-summary" v-if="summaryText">{{ summaryText }}</div>
        </div>
        <pre v-if="errorText" class="runner-error">{{ errorText }}</pre>
      </div>

      <div class="runner-panel">
        <div class="runner-header">TS(PG)</div>
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
            The transition system will appear here after running <code>pg_to_ts(...)</code>.
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
  color?: string
  stroke?: string
  strokeWidth?: number
}

type GraphTransition = {
  source: string
  target: string
  action?: string
  actionWidth?: number
  actionFontSize?: number
  actionY?: number
  loopDirection?: string
  curve?: number
  stroke?: string
  strokeWidth?: number
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
  width: 470,
  height: 360,
  initialExpression: `pg_to_ts(
  var_domains={
    'x': [0, 1, 2],
  },
  locations=['l0', 'l1'],
  initial_locations=['l0'],
  initial_guard=lambda eta: eta['x'] == 0,
  transitions=[
    ('l0', lambda eta: eta['x'] < 2, 'inc', lambda eta: update(eta, x=eta['x'] + 1), 'l1'),
    ('l1', lambda eta: True, 'reset', lambda eta: update(eta, x=0), 'l0'),
  ],
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
    pyodide.globals.set('__pg_expr__', expression.value)

    const jsonText = await pyodide.runPythonAsync(`
import json
__pg_ts_result = eval(__pg_expr__)
json.dumps(pg_ts_to_slidev_data(__pg_ts_result))
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
.pg-ts-runner {
  direction: ltr;
  text-align: left;
  max-width: 100%;
  max-height: 78vh;
  overflow: auto;
}

.runner-grid {
  display: grid;
  grid-template-columns: minmax(340px, 1fr) minmax(380px, 1.15fr);
  gap: 14px;
  align-items: start;
  min-width: 860px;
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
  min-height: 330px;
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
  overflow: auto;
  white-space: pre;
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
  min-height: 392px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border: 1px dashed #cbd5e1;
  border-radius: 10px;
  overflow: auto;
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
