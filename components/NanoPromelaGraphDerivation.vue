<template>
  <div class="pg-derivation" dir="rtl">
    <pre class="program-text">{{ currentExample.program.join('\n') }}</pre>

    <div class="walkthrough-grid">
      <section class="graph-card">
        <div class="graph-shell" dir="ltr">
          <TransitionSystemD3
            :width="currentExample.width"
            :height="currentExample.height"
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
            <span
              class="reach-chip"
              :class="state.reachableFromStart ? 'reachable' : 'unreachable'"
            >
              {{ state.reachableFromStart ? 'נגיש' : 'לא נגיש' }}
            </span>
          </div>
        </div>

        <div class="rule-card">
          <div class="section-title">{{ currentRuleTitle }}</div>

          <div
            v-if="currentTransitionPreview"
            class="transition-preview"
            dir="ltr"
          >
            {{ currentTransitionPreview }}
          </div>

          <div class="rule-subtitle">הכלל</div>
          <pre class="rule-pre" dir="ltr">{{ currentRuleLines.join('\n') }}</pre>

          <div
            v-if="currentInstanceLines.length > 0"
            class="rule-subtitle"
          >
            הצבה בדוגמה
          </div>
          <pre
            v-if="currentInstanceLines.length > 0"
            class="rule-pre"
            dir="ltr"
          >{{ currentInstanceLines.join('\n') }}</pre>

          <div
            v-if="currentUnreachableNote"
            class="reach-note"
          >
            {{ currentUnreachableNote }}
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
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

const graphStates = computed(() =>
  currentExample.value.states.map((state) => {
    const isFocused = focusStateIds.value.has(state.id)
    const isInitial = !!state.initial

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
      x: state.x,
      y: state.y,
      width: state.width,
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
      actionWidth: edge.actionWidth,
      actionHeight: edge.actionHeight,
      actionX: edge.actionX,
      actionY: edge.actionY,
      loopDirection: edge.loopDirection,
      loopRadius: edge.loopRadius,
      loopLabelRadius: edge.loopLabelRadius,
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

const currentInstanceLines = computed(() =>
  activeStep.value?.instanceLines ?? [],
)

const currentTransitionPreview = computed(() => {
  if (!activeStep.value || !currentEdge.value) {
    return ''
  }

  return `${stateById.value[activeStep.value.source].shortLabel} ${currentEdge.value.previewLabel} ${stateById.value[activeStep.value.target].shortLabel}`
})

const currentUnreachableNote = computed(() => {
  if (!activeStep.value) {
    return ''
  }

  const source = stateById.value[activeStep.value.source]
  if (!source || source.reachableFromStart) {
    return ''
  }

  return `${source.shortLabel} אינו נגיש מהמקום ההתחלתי, אבל הוא שייך ל-Loc ולכן גם ממנו גוזרים מעברים.`
})
</script>

<style scoped>
.pg-derivation {
  display: flex;
  flex-direction: column;
  gap: 6px;
  max-width: 900px;
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
  padding: 8px 10px;
  background: #e2e8f0;
  color: #0f172a;
  font-size: 10.8px;
  line-height: 1.25;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
}

.walkthrough-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.95fr;
  gap: 8px;
  align-items: start;
}

.graph-card {
  padding: 6px 6px 8px;
}

.graph-shell {
  min-height: 334px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.graph-note {
  margin-top: 4px;
  padding: 0 6px;
  font-size: 10px;
  line-height: 1.28;
  color: #334155;
}

.details-column {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.locations-card,
.rule-card {
  padding: 8px 10px;
}

.section-title {
  margin-bottom: 6px;
  font-size: 10px;
  font-weight: 700;
  color: #334155;
}

.location-row {
  display: grid;
  grid-template-columns: 42px 1fr auto;
  gap: 6px;
  align-items: start;
  padding: 4px 6px;
  border-radius: 10px;
}

.location-row.active {
  background: #fff7ed;
}

.loc-chip {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 22px;
  padding: 1px 6px;
  border-radius: 999px;
  background: #e2e8f0;
  border: 1px solid #cbd5e1;
  color: #0f172a;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8.8px;
}

.location-code {
  white-space: normal;
  word-break: break-word;
  color: #0f172a;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8.9px;
  line-height: 1.18;
}

.reach-chip {
  display: inline-flex;
  align-items: center;
  min-height: 20px;
  padding: 0 6px;
  border-radius: 999px;
  font-size: 8.2px;
  font-weight: 700;
  white-space: nowrap;
}

.reach-chip.reachable {
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  color: #047857;
}

.reach-chip.unreachable {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  color: #475569;
}

.transition-preview {
  margin-bottom: 6px;
  padding: 5px 8px;
  border-radius: 12px;
  background: #fff7ed;
  border: 1px solid #fdba74;
  color: #9a3412;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8.9px;
  line-height: 1.2;
  text-align: center;
}

.rule-subtitle {
  margin: 5px 0 3px;
  font-size: 8.8px;
  font-weight: 700;
  color: #475569;
}

.rule-pre {
  margin: 0;
  padding: 5px 6px;
  border-radius: 10px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  color: #0f172a;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8.7px;
  line-height: 1.22;
  white-space: pre-wrap;
}

.reach-note {
  margin-top: 6px;
  padding: 6px 8px;
  border-radius: 12px;
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  color: #334155;
  font-size: 9px;
  line-height: 1.25;
}
</style>
