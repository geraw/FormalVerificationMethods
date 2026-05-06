<template>
  <div class="deadlock-stepper" dir="rtl">
    <div class="control-panel">
      <div class="control-copy">
        <div class="eyebrow">הרצת האירועים</div>
        <div class="event-line">
          <span class="event-pill" :dir="current.dir ?? 'rtl'">{{ current.title }}</span>
          <span class="event-note">{{ current.note }}</span>
        </div>
      </div>

      <div class="control-actions">
        <button type="button" class="primary-button" @click="advance">
          {{ isFinalStep ? 'התחל מחדש' : 'השלב הבא' }}
        </button>
        <button type="button" class="secondary-button" @click="reset" :disabled="currentIndex === 0">
          איפוס
        </button>
      </div>
    </div>

    <div class="timeline">
      <button
        v-for="(frame, index) in frames"
        :key="frame.id"
        type="button"
        class="timeline-step"
        :class="{ active: index === currentIndex, done: index < currentIndex, terminal: frame.deadlock }"
        @click="goTo(index)"
      >
        <span class="timeline-index">{{ index + 1 }}</span>
        <span class="timeline-label" :dir="frame.dir ?? 'rtl'">{{ frame.shortLabel }}</span>
      </button>
    </div>

    <section class="systems-section">
      <div class="section-label">פילוסופים</div>
      <div class="systems-grid">
        <article
          v-for="phil in ids"
          :key="`phil-${phil}`"
          class="system-card"
          :class="{ active: current.activePhilosopher === phil }"
        >
          <div class="card-head">
            <div class="card-title" dir="ltr">Phil_{{ phil }}</div>
            <div class="card-state" dir="ltr">{{ philosopherStateId(current, phil) }}</div>
          </div>

          <div class="diagram-shell phil-diagram">
            <TransitionSystemD3
              :width="360"
              :height="260"
              :auto="false"
              :states="philosopherStates"
              :transitions="philosopherTransitions(phil)"
              :highlighted-transition-ids="activePhilosopherTransitionIds(phil)"
              :markers="philosopherMarkers(phil)"
              :pulse-highlights="true"
              :highlight-fill="'#fff7ed'"
            />
          </div>

          <div class="card-caption">
            {{ philosopherStatus(current, phil) }}
          </div>
        </article>
      </div>
    </section>

    <section class="systems-section sticks-section">
      <div class="section-label">מקלות</div>
      <div class="systems-grid">
        <article
          v-for="stick in ids"
          :key="`stick-${stick}`"
          class="system-card"
          :class="{ active: current.activePhilosopher === stick }"
        >
          <div class="card-head">
            <div class="card-title" dir="ltr">Stick_{{ stick }}</div>
            <div class="card-state" dir="ltr">{{ stickStateId(current, stick) }}</div>
          </div>

          <div class="diagram-shell stick-diagram">
            <TransitionSystemD3
              :width="360"
              :height="260"
              :auto="false"
              :states="stickStates"
              :transitions="stickTransitions(stick)"
              :highlighted-transition-ids="activeStickTransitionIds(stick)"
              :markers="stickMarkers(stick)"
              :pulse-highlights="true"
              :highlight-fill="'#fff7ed'"
            />
          </div>

          <div class="card-caption">
            {{ stickStatus(current, stick) }}
          </div>
        </article>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import TransitionSystemD3 from './TransitionSystemD3.vue'

type Frame = {
  id: string
  shortLabel: string
  title: string
  note: string
  completed: Set<number>
  activePhilosopher: number | null
  deadlock?: boolean
  dir?: 'rtl' | 'ltr'
}

interface Props {
  count?: number
  run?: number[]
}

const props = withDefaults(defineProps<Props>(), {
  count: 4,
})

const count = computed(() => Math.max(2, props.count))

function mod(index: number) {
  return ((index % count.value) + count.value) % count.value
}

const ids = computed(() => Array.from({ length: count.value }, (_, index) => index))

const run = computed(() => {
  if (props.run && props.run.length > 0) {
    return props.run.map((index) => mod(Math.trunc(index))).slice(0, count.value)
  }
  return Array.from({ length: count.value }, (_, index) => count.value - 1 - index)
})

const frames = computed<Frame[]>(() => {
  const sequence = run.value
  const result: Frame[] = [
    {
      id: 'start',
      shortLabel: 'התחלה',
      title: 'מצב התחלתי',
      note: 'כולם ב־think, כל המקלות פנויים.',
      completed: new Set<number>(),
      activePhilosopher: null,
    },
  ]

  sequence.forEach((phil, index) => {
    result.push({
      id: `request-${phil}`,
      shortLabel: `request_${phil}`,
      title: `request_${phil}`,
      note: `P_${phil} לוקח את S_${phil}.`,
      completed: new Set(sequence.slice(0, index + 1)),
      activePhilosopher: phil,
      dir: 'ltr',
    })
  })

  result.push({
    id: 'deadlock',
    shortLabel: 'deadlock',
    title: 'deadlock',
    note: 'כולם מחכים לשכן. אין אירוע נוסף.',
    completed: new Set(sequence),
    activePhilosopher: null,
    deadlock: true,
    dir: 'ltr',
  })

  return result
})

const philosopherStates = [
  {
    id: 'think',
    text: 'think',
    textFontSize: 12,
    initial: true,
    initialDirection: 'top' as const,
    x: 210,
    y: 18,
    width: 88,
    color: '#e0f2fe',
    stroke: '#2563eb',
  },
  {
    id: 'waitL',
    text: 'wait for<br>left stick',
    textFontSize: 11,
    x: 110,
    y: 112,
    width: 100,
    height: 52,
    color: '#f8fafc',
    stroke: '#94a3b8',
  },
  {
    id: 'waitR',
    text: 'wait for<br>right stick',
    textFontSize: 11,
    x: 270,
    y: 112,
    width: 100,
    height: 52,
    color: '#f8fafc',
    stroke: '#94a3b8',
  },
  {
    id: 'eat',
    text: 'eat',
    textFontSize: 12,
    x: 210,
    y: 196,
    width: 72,
    color: '#dcfce7',
    stroke: '#15803d',
  },
  {
    id: 'retL',
    text: 'return the<br>left stick',
    textFontSize: 10,
    x: 10,
    y: 196,
    width: 100,
    height: 52,
    color: '#f8fafc',
    stroke: '#94a3b8',
  },
  {
    id: 'retR',
    text: 'return the<br>right stick',
    textFontSize: 10,
    x: 400,
    y: 196,
    width: 100,
    height: 52,
    color: '#f8fafc',
    stroke: '#94a3b8',
  },
]

const stickStates = [
  {
    id: 'avail',
    text: 'available',
    textFontSize: 12,
    initial: true,
    initialDirection: 'top' as const,
    x: 180,
    y: 20,
    width: 120,
    color: '#dcfce7',
    stroke: '#15803d',
  },
  {
    id: 'occn',
    text: 'Occupied by the <br> left philosopher',
    textFontSize: 10,
    x: 65,
    y: 196,
    width: 180,
    color: '#f8fafc',
    stroke: '#94a3b8',
  },
  {
    id: 'occi',
    text: 'Occupied by the <br> right philosopher',
    textFontSize: 10,
    x: 295,
    y: 196,
    width: 180,
    color: '#f8fafc',
    stroke: '#94a3b8',
  },
]

const currentIndex = ref(0)
const current = computed(() => frames.value[currentIndex.value] ?? frames.value[0])
const isFinalStep = computed(() => currentIndex.value === frames.value.length - 1)

function requestPairLabel(stick: number, phil: number) {
  return `$request_{${stick},${phil}}$`
}

function releasePairLabel(stick: number, phil: number) {
  return `$release_{${stick},${phil}}$`
}

function philosopherTransitions(phil: number) {
  return [
    {
      id: 'take-right',
      source: 'think',
      target: 'waitL',
      action: requestPairLabel(mod(phil - 1), phil),
      curve: 0.18,
      actionX: -20,
      actionY: -2,
      actionFontSize: 8,
      stroke: '#94a3b8',
    },
    {
      id: 'take-left-after-right',
      source: 'waitL',
      target: 'eat',
      action: requestPairLabel(phil, phil),
      curve: 0.12,
      actionX: -8,
      actionY: -8,
      actionFontSize: 8,
      stroke: '#94a3b8',
    },
    {
      id: 'take-left',
      source: 'think',
      target: 'waitR',
      action: requestPairLabel(phil, phil),
      curve: -0.18,
      actionX: 20,
      actionY: -2,
      actionFontSize: 8,
      stroke: '#94a3b8',
      dashed: true,
    },
    {
      id: 'take-right-after-left',
      source: 'waitR',
      target: 'eat',
      action: requestPairLabel(mod(phil - 1), phil),
      curve: -0.12,
      actionX: 8,
      actionY: -8,
      actionFontSize: 8,
      stroke: '#94a3b8',
      dashed: true,
    },
    {
      id: 'release-left-first',
      source: 'eat',
      target: 'retL',
      action: releasePairLabel(phil, phil),
      curve: -0.12,
      actionX: -10,
      actionY: 8,
      actionFontSize: 7,
      stroke: '#cbd5e1',
    },
    {
      id: 'release-right-first',
      source: 'eat',
      target: 'retR',
      action: releasePairLabel(mod(phil - 1), phil),
      curve: 0.12,
      actionX: 10,
      actionY: 8,
      actionFontSize: 7,
      stroke: '#cbd5e1',
      dashed: true,
    },
    {
      id: 'finish-left-return',
      source: 'retL',
      target: 'think',
      action: releasePairLabel(mod(phil - 1), phil),
      curve: -0.5,
      actionX: -46,
      actionY: -4,
      actionFontSize: 7,
      stroke: '#cbd5e1',
    },
    {
      id: 'finish-right-return',
      source: 'retR',
      target: 'think',
      action: releasePairLabel(phil, phil),
      curve: 0.5,
      actionX: 46,
      actionY: -4,
      actionFontSize: 7,
      stroke: '#cbd5e1',
      dashed: true,
    },
  ]
}

function stickTransitions(stick: number) {
  return [
    {
      id: 'take-by-right',
      source: 'avail',
      target: 'occi',
      action: requestPairLabel(stick, stick),
      curve: 0.22,
      actionFontSize: 8,
      actionY: -8,
      stroke: '#94a3b8',
    },
    {
      id: 'take-by-left',
      source: 'avail',
      target: 'occn',
      action: requestPairLabel(stick, mod(stick + 1)),
      curve: -0.22,
      actionFontSize: 8,
      actionY: -8,
      stroke: '#94a3b8',
    },
    {
      id: 'release-right',
      source: 'occi',
      target: 'avail',
      action: releasePairLabel(stick, stick),
      curve: 0.38,
      actionFontSize: 7,
      actionY: 0,
      stroke: '#cbd5e1',
    },
    {
      id: 'release-left',
      source: 'occn',
      target: 'avail',
      action: releasePairLabel(stick, mod(stick + 1)),
      curve: -0.38,
      actionFontSize: 7,
      actionY: 0,
      stroke: '#cbd5e1',
    },
  ]
}

function philosopherStateId(frame: Frame, phil: number) {
  return frame.completed.has(phil) ? 'waitR' : 'think'
}

function stickStateId(frame: Frame, stick: number) {
  return frame.completed.has(stick) ? 'occi' : 'avail'
}

function philosopherMarkers(phil: number) {
  return [
    {
      stateId: philosopherStateId(current.value, phil),
      color: current.value.activePhilosopher === phil ? '#f97316' : '#0f766e',
    },
  ]
}

function stickMarkers(stick: number) {
  return [
    {
      stateId: stickStateId(current.value, stick),
      color: current.value.activePhilosopher === stick ? '#f97316' : '#0f766e',
    },
  ]
}

function activePhilosopherTransitionIds(phil: number) {
  if (current.value.activePhilosopher !== phil) {
    return []
  }
  return ['take-left']
}

function activeStickTransitionIds(stick: number) {
  if (current.value.activePhilosopher !== stick) {
    return []
  }
  return ['take-by-right']
}

function philosopherStatus(frame: Frame, phil: number) {
  if (philosopherStateId(frame, phil) === 'think') {
    return 'עוד לא ביקש'
  }
  return `מחזיק S_${phil}, ממתין ל־S_${mod(phil - 1)}`
}

function stickStatus(frame: Frame, stick: number) {
  if (!frame.completed.has(stick)) {
    return 'פנוי'
  }
  return `בידי P_${stick}`
}

function advance() {
  if (isFinalStep.value) {
    currentIndex.value = 0
    return
  }
  currentIndex.value += 1
}

function reset() {
  currentIndex.value = 0
}

function goTo(index: number) {
  currentIndex.value = index
}
</script>

<style scoped>
.deadlock-stepper {
  margin-top: 4px;
}

.control-panel,
.systems-section {
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(241, 245, 249, 0.94));
  border: 1px solid rgba(148, 163, 184, 0.34);
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
}

.control-panel {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 8px;
  align-items: center;
  padding: 6px 8px;
}

.eyebrow,
.section-label {
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #0f766e;
}

.event-line {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 3px;
}

.event-pill {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  background: rgba(255, 247, 237, 0.96);
  color: #9a3412;
  border: 1px solid rgba(251, 146, 60, 0.32);
  padding: 2px 7px;
  font-size: 10px;
  font-weight: 800;
}

.event-note {
  font-size: 10px;
  line-height: 1.1;
  color: #475569;
}

.control-actions {
  display: flex;
  gap: 6px;
}

.primary-button,
.secondary-button,
.timeline-step {
  transition:
    transform 160ms ease,
    background-color 160ms ease,
    border-color 160ms ease,
    color 160ms ease,
    box-shadow 160ms ease;
}

.primary-button,
.secondary-button {
  border-radius: 999px;
  padding: 6px 10px;
  font-size: 10px;
  font-weight: 800;
}

.primary-button {
  background: linear-gradient(135deg, #f97316, #ea580c);
  color: white;
  border: 0;
  box-shadow: 0 8px 16px rgba(234, 88, 12, 0.18);
}

.primary-button:hover,
.secondary-button:hover,
.timeline-step:hover {
  transform: translateY(-1px);
}

.secondary-button {
  background: #f8fafc;
  color: #0f172a;
  border: 1px solid #cbd5e1;
}

.secondary-button:disabled {
  opacity: 0.45;
  cursor: default;
  transform: none;
}

.timeline {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-top: 5px;
}

.timeline-step {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border: 1px solid rgba(148, 163, 184, 0.42);
  background: rgba(248, 250, 252, 0.95);
  color: #334155;
  border-radius: 999px;
  padding: 2px 7px;
  font-size: 9px;
  font-weight: 700;
}

.timeline-step.done {
  background: rgba(254, 243, 199, 0.88);
  color: #9a3412;
  border-color: rgba(217, 119, 6, 0.4);
}

.timeline-step.active {
  background: linear-gradient(135deg, #f97316, #ea580c);
  color: white;
  border-color: transparent;
}

.timeline-step.terminal.active {
  background: linear-gradient(135deg, #dc2626, #b91c1c);
}

.timeline-index {
  width: 14px;
  height: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.18);
  font-size: 8px;
}

.systems-section {
  margin-top: 6px;
  padding: 5px 6px 6px;
}

.sticks-section {
  margin-top: 5px;
}

.section-label {
  margin: 0 2px 4px 0;
}

.systems-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 5px;
}

.system-card {
  padding: 4px;
  border-radius: 10px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(255, 255, 255, 0.76);
}

.system-card.active {
  border-color: rgba(234, 88, 12, 0.48);
  box-shadow: 0 8px 18px rgba(234, 88, 12, 0.08);
}

.card-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 4px;
}

.card-title {
  font-size: 10px;
  font-weight: 800;
  color: #0f172a;
}

.card-state {
  font-size: 9px;
  font-weight: 700;
  color: #0f766e;
}

.diagram-shell {
  margin-top: 2px;
  overflow: hidden;
  border-radius: 8px;
  border: 1px solid rgba(148, 163, 184, 0.24);
  background:
    radial-gradient(circle at top, rgba(255, 255, 255, 0.98), rgba(226, 232, 240, 0.78));
}

.phil-diagram {
  height: 126px;
}

.stick-diagram {
  height: 110px;
}

.card-caption {
  min-height: 14px;
  margin-top: 2px;
  font-size: 8.5px;
  line-height: 1.1;
  color: #475569;
}

.diagram-shell :deep(.transition-system-container) {
  margin-top: 0 !important;
}

.phil-diagram :deep(.transition-system-container svg) {
  transform: translate(-14px, 17px) scale(0.42);
  transform-origin: top center;
}

.stick-diagram :deep(.transition-system-container svg) {
  transform: translate(0, 8px) scale(0.42);
  transform-origin: top center;
}
</style>
