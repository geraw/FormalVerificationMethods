<template>
  <div class="pg-derivation" dir="rtl">
    <pre class="program-text">{{ currentExample.program.join('\n') }}</pre>

    <div class="walkthrough-grid">
      <section class="graph-card">
        <div
          class="graph-shell"
          dir="ltr"
          :style="{ minHeight: `${graphHeight + 8}px` }"
        >
          <TransitionSystemD3
            :width="graphWidth"
            :height="graphHeight"
            :auto="false"
            :states="graphStates"
            :transitions="graphTransitions"
          />
        </div>

        <div class="graph-note">{{ currentNote }}</div>
      </section>

      <section class="details-column">
        <div class="locations-card">
          <div class="section-title">Loc = sub(stmt)</div>

          <div
            v-for="state in currentExample.states"
            :key="state.id"
            class="location-row"
            :class="{ active: focusStateIds.has(state.id) }"
          >
            <span class="loc-chip" dir="ltr">{{ state.shortLabel }}</span>
            <code class="location-code" dir="ltr">{{ state.locationText }}</code>
          </div>
        </div>

        <div class="rule-card">
          <div class="section-title">{{ currentRuleTitle }}</div>

          <div class="rule-subtitle">הכלל</div>
          <div
            v-if="showIntroRuleCopy"
            class="rule-copy"
          >
            <div
              v-for="(line, index) in currentRuleLines"
              :key="`intro-${index}`"
              class="rule-copy-line"
            >
              {{ line }}
            </div>
          </div>
          <div
            v-else-if="currentRuleLatex"
            class="derivation-display"
            dir="ltr"
            v-html="currentRuleLatex"
          />
          <div
            v-else
            class="formula-list"
            dir="ltr"
          >
            <div
              v-for="(line, index) in currentRuleLines"
              :key="`rule-${index}`"
              class="formula-line"
              v-html="renderFormulaLine(line)"
            />
          </div>

          <div
            v-if="currentInstanceLines.length > 0"
            class="rule-subtitle"
          >
            הצבה בדוגמה
          </div>
          <div
            v-if="currentInstanceLatex"
            class="derivation-display"
            dir="ltr"
            v-html="currentInstanceLatex"
          />
          <div
            v-else-if="currentInstanceLines.length > 0"
            class="formula-list"
            dir="ltr"
          >
            <div
              v-for="(line, index) in currentInstanceLines"
              :key="`instance-${index}`"
              class="formula-line"
              v-html="renderFormulaLine(line)"
            />
          </div>

        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import katex from 'katex'
import 'katex/dist/katex.min.css'
import TransitionSystemD3 from './TransitionSystemD3.vue'
import {
  pgExamples,
  type PgEdge,
  type PgExampleKey,
  type PgState,
  type PgStep,
} from './NanoPromelaGraphDerivation.examples'

type DiagramTransition = {
  source: string
  target: string
  action: string
  stroke: string
  strokeWidth: number
  actionFontSize?: number
  actionWidth?: number
  actionHeight?: number
  actionX?: number
  actionY?: number
  loopDirection?: string
  loopRadius?: number
  loopLabelRadius?: number
  curve?: number
}

const props = defineProps<{
  example: PgExampleKey
}>()

const GRAPH_SCALE = 0.82

const { $clicks } = useSlideContext()

const currentExample = computed(() => pgExamples[props.example])

const stateById = computed(() =>
  Object.fromEntries(currentExample.value.states.map(state => [state.id, state])),
) as unknown as Record<string, PgState>

const edgeById = computed(() =>
  Object.fromEntries(currentExample.value.edges.map(edge => [edge.id, edge])),
) as unknown as Record<string, PgEdge>

const currentStep = computed(() => {
  const raw = Number($clicks.value || 0)
  return Math.min(raw, currentExample.value.steps.length)
})

const activeStep = computed<PgStep | null>(() =>
  currentStep.value > 0
    ? currentExample.value.steps[currentStep.value - 1]
    : null,
)

const currentEdge = computed<PgEdge | null>(() =>
  activeStep.value
    ? edgeById.value[activeStep.value.edgeId]
    : null,
)

const visibleEdgeIds = computed(() =>
  new Set(currentExample.value.steps.slice(0, currentStep.value).map(step => step.edgeId)),
)

const focusStateIds = computed(() => {
  if (activeStep.value) {
    return new Set([activeStep.value.source, activeStep.value.target])
  }

  return new Set(
    currentExample.value.states
      .filter(state => state.initial)
      .map(state => state.id),
  )
})

const scaleSize = (value?: number) =>
  value === undefined ? undefined : Math.round(value * GRAPH_SCALE)

const graphWidth = computed(() =>
  Math.round(currentExample.value.width * GRAPH_SCALE),
)

const graphHeight = computed(() =>
  Math.round(currentExample.value.height * GRAPH_SCALE),
)

const graphStates = computed(() =>
  currentExample.value.states.map((state) => {
    const isFocused = focusStateIds.value.has(state.id)
    const isInitial = !!state.initial && activeStep.value === null

    let color = '#ffffff'
    let stroke = '#64748b'
    let strokeWidth = 2.4

    if (!state.reachableFromStart) {
      color = '#f8fafc'
      stroke = '#94a3b8'
    }

    if (isInitial) {
      color = '#fef3c7'
      stroke = '#d97706'
      strokeWidth = 3.2
    }

    if (isFocused) {
      color = state.id === activeStep.value?.source
        ? '#fff7ed'
        : '#eff6ff'
      stroke = state.id === activeStep.value?.source
        ? '#f59e0b'
        : '#0ea5e9'
      strokeWidth = 4
    }

    return {
      id: state.id,
      text: `$${state.shortLabel}$`,
      x: Math.round(state.x * GRAPH_SCALE),
      y: Math.round(state.y * GRAPH_SCALE),
      width: scaleSize(state.width),
      initial: state.initial,
      initialDirection: state.initialDirection,
      color,
      stroke,
      strokeWidth,
    }
  }),
)

const graphTransitions = computed<DiagramTransition[]>(() =>
  currentExample.value.edges
    .filter(edge => visibleEdgeIds.value.has(edge.id))
    .map((edge) => ({
      source: edge.source,
      target: edge.target,
      action: edge.graphLabel,
      stroke: edge.id === currentEdge.value?.id ? '#f59e0b' : '#0ea5e9',
      strokeWidth: edge.id === currentEdge.value?.id ? 4.2 : 2.7,
      actionFontSize: 10,
      actionWidth: scaleSize(edge.actionWidth),
      actionHeight: scaleSize(edge.actionHeight),
      actionX: scaleSize(edge.actionX),
      actionY: scaleSize(edge.actionY),
      loopDirection: edge.loopDirection,
      loopRadius: scaleSize(edge.loopRadius),
      loopLabelRadius: scaleSize(edge.loopLabelRadius),
      curve: edge.curve,
    })),
)

const currentNote = computed(() =>
  activeStep.value?.note ?? currentExample.value.introNote,
)

const currentRuleTitle = computed(() =>
  activeStep.value?.ruleTitle ?? 'מה בונים עכשיו?'
)

const currentRuleLines = computed(() =>
  activeStep.value?.ruleLines ?? currentExample.value.introRuleLines,
)

const currentRuleLatex = computed(() =>
  activeStep.value?.ruleLatex
    ? renderLatex(activeStep.value.ruleLatex, true)
    : '',
)

const currentInstanceLines = computed(() =>
  activeStep.value?.instanceLines ?? [],
)

const currentInstanceLatex = computed(() =>
  activeStep.value?.instanceLatex
    ? renderLatex(activeStep.value.instanceLatex, true)
    : currentInstanceLines.value.length > 0
      ? renderLatex(buildInferenceLatex(currentInstanceLines.value), true)
      : '',
)

const showIntroRuleCopy = computed(() =>
  activeStep.value === null,
)

const escapeHtml = (value: string) =>
  value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;')

const escapeLatexText = (value: string) =>
  value
    .replaceAll('\\', '\\textbackslash ')
    .replace(/([{}#$%&_])/g, '\\$1')

const stripMathDelimiters = (value: string) => {
  const trimmed = value.trim()
  if (trimmed.startsWith('$') && trimmed.endsWith('$')) {
    return trimmed.slice(1, -1).trim()
  }
  return trimmed
}

const formatGuard = (value: string) =>
  stripMathDelimiters(value)
    .replace(/\.\.\./g, '\\cdots')
    .replace(/&&/g, '\\land')
    .replace(/!\s*\(([^)]+)\)/g, '\\neg($1)')
    .replace(/!\s*([A-Za-z][A-Za-z0-9_]*)/g, '\\neg $1')
    .replace(/\btrue\b/g, '\\mathrm{true}')
    .replace(/\bid\b/g, '\\mathrm{id}')
    .replace(/\balpha\b/g, '\\alpha')

const formatAction = (value: string) => {
  const trimmed = stripMathDelimiters(value)
  if (trimmed === 'id') {
    return '\\mathrm{id}'
  }

  return `\\texttt{${escapeLatexText(trimmed)}}`
}

const formatTerm = (value: string) => {
  const trimmed = value.trim()
  const locationMatch = trimmed.match(/^l_(\d+)$/)
  if (locationMatch) {
    return `\\ell_${locationMatch[1]}`
  }

  if (trimmed === 'exit' || trimmed === 'skip') {
    return `\\texttt{${trimmed}}`
  }

  if (trimmed === 'h' || trimmed === 'expr') {
    return trimmed
  }

  if (/^(stmt|g)_[A-Za-z0-9]+('?)+$/.test(trimmed) || /^(stmt|g)_[A-Za-z0-9]+$/.test(trimmed)) {
    return trimmed.replace(/\balpha\b/g, '\\alpha')
  }

  if (trimmed === 'cond_cmd' || trimmed === 'loop_cmd') {
    return `\\texttt{${escapeLatexText(trimmed)}}`
  }

  if (trimmed.includes(':=') || trimmed.includes(';') || trimmed.includes(' ') || trimmed.includes('do') || trimmed.includes('if')) {
    return `\\texttt{${escapeLatexText(trimmed)}}`
  }

  return formatGuard(trimmed)
}

const formatLabel = (value: string) => {
  const trimmed = stripMathDelimiters(value)
  const colonIndex = trimmed.indexOf(':')
  if (colonIndex === -1) {
    return formatGuard(trimmed)
  }

  const guard = trimmed.slice(0, colonIndex).trim()
  const action = trimmed.slice(colonIndex + 1).trim()
  return `${formatGuard(guard)} : ${formatAction(action)}`
}

const formatTransitionLatex = (value: string) => {
  const match = value.trim().match(/^(.*?)\s+--\s+(.*?)\s+-->\s+(.*)$/)
  if (!match) {
    return `\\texttt{${escapeLatexText(value.trim())}}`
  }

  const [, source, label, target] = match
  return `${formatTerm(source)} \\xrightarrow{${formatLabel(label)}} ${formatTerm(target)}`
}

const normalizeDisplayFractions = (value: string) =>
  value.replaceAll('\\frac', '\\dfrac')

const renderLatex = (value: string, displayMode = false) =>
  katex.renderToString(displayMode ? normalizeDisplayFractions(value) : value, {
    throwOnError: false,
    displayMode,
    strict: 'ignore',
  })

const buildInferenceLatex = (lines: string[]) => {
  const normalizedLines = lines
    .map(line => line.trim())
    .filter(Boolean)
    .map(line => formatTransitionLatex(line))

  if (normalizedLines.length === 0) {
    return ''
  }

  if (normalizedLines.length === 1) {
    return String.raw`\frac{}{${normalizedLines[0]}}`
  }

  const numerator = normalizedLines.slice(0, -1).join(String.raw` \\ `)
  const denominator = normalizedLines[normalizedLines.length - 1]
  return String.raw`\frac{${numerator}}{${denominator}}`
}

const renderFormulaLine = (value: string) => {
  const trimmed = value.trim()
  if (!trimmed) {
    return ''
  }

  let prefix = ''
  let body = trimmed

  if (trimmed.startsWith('אם ')) {
    prefix = 'אם'
    body = trimmed.slice(3)
  } else if (trimmed.startsWith('אז ')) {
    prefix = 'אז'
    body = trimmed.slice(3)
  }

  const mathHtml = renderLatex(formatTransitionLatex(body))
  if (!prefix) {
    return mathHtml
  }

  return `<span class="formula-prefix">${escapeHtml(prefix)}</span>${mathHtml}`
}

</script>

<style scoped>
.pg-derivation {
  display: flex;
  flex-direction: column;
  gap: 4px;
  max-width: 930px;
  margin: 0 auto;
}

.program-text,
.graph-card,
.locations-card,
.rule-card {
  border: 1px solid #cbd5e1;
  border-radius: 16px;
  background: linear-gradient(180deg, #ffffff, #f8fafc);
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.07);
}

.program-text {
  margin: 0;
  padding: 6px 8px;
  background: #e2e8f0;
  color: #0f172a;
  font-size: 9.6px;
  line-height: 1.18;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
}

.walkthrough-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 1.02fr);
  gap: 6px;
  align-items: start;
}

.graph-card {
  padding: 4px 4px 6px;
}

.graph-shell {
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.graph-shell :deep(.transition-system-container),
.graph-shell :deep(svg),
.graph-shell :deep(.node-group),
.graph-shell :deep(.links),
.graph-shell :deep(.nodes),
.graph-shell :deep(foreignObject) {
  pointer-events: none !important;
}

.graph-note {
  margin-top: 2px;
  padding: 0 4px;
  font-size: 9px;
  line-height: 1.18;
  color: #334155;
}

.details-column {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.locations-card,
.rule-card {
  padding: 6px 8px;
}

.section-title {
  margin-bottom: 4px;
  font-size: 9px;
  font-weight: 700;
  color: #334155;
}

.location-row {
  display: grid;
  grid-template-columns: 36px 1fr;
  gap: 4px;
  align-items: start;
  padding: 3px 4px;
  border-radius: 10px;
}

.location-row.active {
  background: #fff7ed;
}

.loc-chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 18px;
  padding: 1px 6px;
  border-radius: 999px;
  background: #e2e8f0;
  border: 1px solid #cbd5e1;
  color: #0f172a;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8px;
}

.location-code {
  white-space: normal;
  word-break: break-word;
  color: #0f172a;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 7.7px;
  line-height: 1.1;
}

.rule-subtitle {
  margin: 4px 0 2px;
  font-size: 8px;
  font-weight: 700;
  color: #475569;
}

.rule-copy,
.formula-list {
  margin: 0;
  padding: 4px 5px;
  border-radius: 10px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}

.rule-copy {
  color: #0f172a;
  font-size: 8px;
  line-height: 1.18;
}

.rule-copy-line + .rule-copy-line {
  margin-top: 2px;
}

.formula-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.formula-line {
  display: flex;
  align-items: center;
  gap: 4px;
  min-height: 18px;
  color: #0f172a;
  overflow: hidden;
}

.formula-line + .formula-line {
  margin-top: 2px;
  padding-top: 4px;
  border-top: 1px solid #cbd5e1;
}

.formula-line :deep(.katex) {
  font-size: 0.74em;
}

.formula-line :deep(.katex-display) {
  margin: 0;
}

.formula-prefix {
  font-size: 8px;
  font-weight: 700;
  color: #475569;
}

.derivation-display {
  margin: 0;
  padding: 4px 5px;
  border-radius: 10px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  overflow-x: auto;
  overflow-y: hidden;
}

.derivation-display :deep(.katex-display) {
  margin: 0;
}

.derivation-display :deep(.katex) {
  font-size: 0.7em;
}

</style>
