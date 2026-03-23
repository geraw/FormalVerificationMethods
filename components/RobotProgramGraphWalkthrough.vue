<template>
  <div class="robot-walkthrough" dir="rtl">
    <div class="walkthrough-grid">
      <section class="panel">
        <div class="panel-title">גרף התוכנית</div>
        <div class="program-graph-shell">
          <TransitionSystemD3
            :width="360"
            :height="228"
            :auto="false"
            :states="graphStates"
            :transitions="graphTransitions"
          />
        </div>

        <div class="panel-note">{{ current.note }}</div>
      </section>

      <section class="panel">
        <div class="panel-title">הרצת הרובוט</div>
        <div class="world-layout">
          <div class="board-wrap">
            <div class="board">
              <div
                v-for="cell in boardCells"
                :key="cell.id"
                class="board-cell"
              />

              <div class="charger-ring" :style="chargerStyle">CH</div>
              <div class="robot-token" :style="robotStyle">R</div>
            </div>
          </div>

          <div class="telemetry">
            <div class="status-line">
              <span class="status-badge">{{ current.shortLabel }}</span>
              <span class="status-mode">mode: {{ current.location }}</span>
            </div>

            <div class="vars-grid">
              <div class="var-card">
                <span class="var-name">x</span>
                <span class="var-value">{{ current.x }}</span>
              </div>
              <div class="var-card">
                <span class="var-name">y</span>
                <span class="var-value">{{ current.y }}</span>
              </div>
              <div class="var-card">
                <span class="var-name">bat</span>
                <span class="var-value">{{ current.bat }}</span>
              </div>
              <div class="var-card">
                <span class="var-name">action</span>
                <span class="var-value">{{ current.action }}</span>
              </div>
            </div>

            <div class="effect-box">
              <div class="effect-title">עדכון משתנים</div>
              <div class="effect-text">{{ current.effect }}</div>
            </div>

            <div class="battery">
              <div class="battery-label">
                <span>סוללה</span>
                <span>{{ current.bat }}%</span>
              </div>
              <div class="battery-track">
                <div class="battery-fill" :style="{ width: `${current.bat}%` }" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <div class="timeline">
      <button
        v-for="(frame, index) in frames"
        :key="frame.id"
        type="button"
        class="timeline-step"
        :class="{ active: index === currentIndex }"
        @click="goTo(index)"
      >
        <span class="timeline-index">{{ index + 1 }}</span>
        <span class="timeline-label">{{ frame.shortLabel }}</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import TransitionSystemD3 from './TransitionSystemD3.vue'

type LocationId = 'load' | 'cart' | 'diag'
type EdgeId =
  | 'load-cart'
  | 'load-diag'
  | 'cart-load'
  | 'diag-load'
  | 'cart-loop'
  | 'diag-loop'
  | 'cart-diag'
  | 'diag-cart'
  | null

type Frame = {
  id: string
  shortLabel: string
  location: LocationId
  activeEdge: EdgeId
  action: string
  x: number
  y: number
  bat: number
  effect: string
  note: string
}

const frames: Frame[] = [
  {
    id: 'start',
    shortLabel: 'התחלה',
    location: 'load',
    activeEdge: null,
    action: 'start',
    x: 0,
    y: 0,
    bat: 100,
    effect: 'bat = 100, x = 0, y = 0',
    note: 'המערכת מתחילה במיקום load, בעמדת הטעינה, עם סוללה מלאה.',
  },
  {
    id: 'load-cart',
    shortLabel: 'load→cart',
    location: 'cart',
    activeEdge: 'load-cart',
    action: 'τ',
    x: 0,
    y: 0,
    bat: 100,
    effect: 'אין שינוי בערכים, רק מעבר מיקום בגרף התוכנית.',
    note: 'יוצאים מ-load אל מצב התנועה בצירים.',
  },
  {
    id: 'cart-east',
    shortLabel: 'E',
    location: 'cart',
    activeEdge: 'cart-loop',
    action: 'E',
    x: -1,
    y: 0,
    bat: 99,
    effect: 'x ← x - 1, bat ← bat - 1',
    note: 'בלולאת cart בוחרים פעולה אופקית, והרובוט מתקדם מזרחה.',
  },
  {
    id: 'cart-north',
    shortLabel: 'N',
    location: 'cart',
    activeEdge: 'cart-loop',
    action: 'N',
    x: -1,
    y: -1,
    bat: 98,
    effect: 'y ← y - 1, bat ← bat - 1',
    note: 'צעד נוסף בצירים: N משנה את y ומקדם את הרובוט כלפי מעלה.',
  },
  {
    id: 'switch-diag',
    shortLabel: 'TR',
    location: 'diag',
    activeEdge: 'cart-diag',
    action: 'TR',
    x: -1,
    y: -1,
    bat: 88,
    effect: 'bat ← bat - 10',
    note: 'הפעולה TR מחליפה mode מ-cart ל-diag ומבזבזת 10 יחידות סוללה.',
  },
  {
    id: 'diag-southwest',
    shortLabel: 'SW',
    location: 'diag',
    activeEdge: 'diag-loop',
    action: 'SW',
    x: 0,
    y: 0,
    bat: 87,
    effect: 'x ← x + 1, y ← y + 1, bat ← bat - 1',
    note: 'במצב האלכסוני הרובוט חוזר ל-(0,0), ולכן שוב מתקיים תנאי החזרה ל-load.',
  },
  {
    id: 'back-load',
    shortLabel: 'חזרה',
    location: 'load',
    activeEdge: 'diag-load',
    action: 'τ',
    x: 0,
    y: 0,
    bat: 87,
    effect: 'אין שינוי נוסף במשתנים; תנאי הבקרה מחזיר ל-load.',
    note: 'כשהרובוט שוב בעמדת הטעינה, גרף התוכנית מחזיר אותו למיקום load.',
  },
]

const boardCells = Array.from({ length: 25 }, (_, index) => ({
  id: `cell-${index}`,
}))

const currentIndex = ref(0)
const current = computed(() => frames[currentIndex.value])

let timer: ReturnType<typeof setInterval> | null = null

const cellSize = 46
const tokenOffset = 8

function boardPosition(x: number, y: number) {
  const col = 2 - x
  const row = 2 + y
  return {
    top: '0px',
    left: '0px',
    transform: `translate(${col * cellSize + tokenOffset}px, ${row * cellSize + tokenOffset}px)`,
  }
}

const robotStyle = computed(() => boardPosition(current.value.x, current.value.y))
const chargerStyle = boardPosition(0, 0)

function graphEdgeStyle(edgeId: Exclude<EdgeId, null>) {
  if (current.value.activeEdge === edgeId) {
    return {
      stroke: '#ea580c',
      strokeWidth: 4,
    }
  }
  return {
    stroke: '#94a3b8',
    strokeWidth: 2.4,
  }
}

const graphStates = computed(() => {
  const activeLocation = current.value.location
  const styleFor = (location: LocationId) => ({
    color: activeLocation === location ? '#fef3c7' : '#e2e8f0',
    stroke: activeLocation === location ? '#d97706' : '#475569',
    strokeWidth: activeLocation === location ? 4 : 2.5,
  })

  return [
    {
      id: 'load',
      text: 'טעינה',
      x: 180,
      y: 34,
      width: 94,
      rx: 16,
      initial: true,
      initialDirection: 'top' as const,
      ...styleFor('load'),
    },
    {
      id: 'cart',
      text: 'צירים',
      x: 88,
      y: 152,
      width: 104,
      rx: 18,
      ...styleFor('cart'),
    },
    {
      id: 'diag',
      text: 'אלכסון',
      x: 272,
      y: 152,
      width: 114,
      rx: 18,
      ...styleFor('diag'),
    },
  ]
})

const graphTransitions = computed(() => [
  {
    source: 'load',
    target: 'cart',
    action: '$bat > 10$',
    actionFontSize: 9,
    actionWidth: 74,
    actionX: -18,
    actionY: -14,
    ...graphEdgeStyle('load-cart'),
  },
  {
    source: 'load',
    target: 'diag',
    action: '$bat > 10$',
    actionFontSize: 9,
    actionWidth: 74,
    actionX: 16,
    actionY: -14,
    ...graphEdgeStyle('load-diag'),
  },
  {
    source: 'cart',
    target: 'load',
    action: '$x=0 \\land y=0$',
    actionFontSize: 8,
    curve: -0.48,
    actionWidth: 112,
    actionX: -20,
    actionY: -2,
    ...graphEdgeStyle('cart-load'),
  },
  {
    source: 'diag',
    target: 'load',
    action: '$x=0 \\land y=0$',
    actionFontSize: 8,
    curve: 0.48,
    actionWidth: 112,
    actionX: 20,
    actionY: -2,
    ...graphEdgeStyle('diag-load'),
  },
  {
    source: 'cart',
    target: 'cart',
    action: '$E$ / $N$ / $S$ / $W$',
    actionFontSize: 8,
    loopDirection: '115deg',
    actionWidth: 118,
    actionHeight: 28,
    actionY: 24,
    ...graphEdgeStyle('cart-loop'),
  },
  {
    source: 'diag',
    target: 'diag',
    action: '$NE$ / $NW$ / $SE$ / $SW$',
    actionFontSize: 8,
    loopDirection: '65deg',
    actionWidth: 156,
    actionHeight: 28,
    actionY: 24,
    ...graphEdgeStyle('diag-loop'),
  },
  {
    source: 'cart',
    target: 'diag',
    action: '$TR$',
    actionFontSize: 9,
    actionWidth: 42,
    actionY: -10,
    ...graphEdgeStyle('cart-diag'),
  },
  {
    source: 'diag',
    target: 'cart',
    action: '$TR$',
    actionFontSize: 9,
    curve: 0.18,
    actionWidth: 42,
    actionY: 14,
    ...graphEdgeStyle('diag-cart'),
  },
])

function startCycle() {
  stopCycle()
  timer = setInterval(() => {
    currentIndex.value = (currentIndex.value + 1) % frames.length
  }, 1800)
}

function stopCycle() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

function goTo(index: number) {
  currentIndex.value = index
  startCycle()
}

onMounted(() => {
  startCycle()
})

onBeforeUnmount(() => {
  stopCycle()
})
</script>

<style scoped>
.robot-walkthrough {
  margin-top: 0;
  max-width: 100%;
  overflow: hidden;
}

.walkthrough-grid {
  display: grid;
  grid-template-columns: minmax(0, 0.92fr) minmax(0, 1.08fr);
  gap: 12px;
  align-items: stretch;
}

.panel {
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(241, 245, 249, 0.92));
  border: 1px solid rgba(148, 163, 184, 0.45);
  border-radius: 16px;
  box-shadow: 0 10px 22px rgba(15, 23, 42, 0.07);
  padding: 10px;
  min-width: 0;
}

.panel-title {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #0f766e;
  margin-bottom: 6px;
}

.program-graph-shell {
  height: 228px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 14px;
  background:
    radial-gradient(circle at top, rgba(255, 255, 255, 0.98), rgba(226, 232, 240, 0.88));
  border: 1px solid rgba(148, 163, 184, 0.28);
  overflow: hidden;
}

.panel-note {
  margin-top: 6px;
  padding: 8px 10px;
  border-radius: 12px;
  background: rgba(255, 247, 237, 0.9);
  border: 1px solid rgba(251, 191, 36, 0.38);
  color: #7c2d12;
  font-size: 11px;
  line-height: 1.45;
  min-height: 52px;
}

.world-layout {
  display: grid;
  grid-template-columns: 250px minmax(0, 1fr);
  gap: 10px;
  align-items: start;
}

.board-wrap {
  position: relative;
  padding: 12px;
  background:
    radial-gradient(circle at top, rgba(14, 165, 233, 0.12), transparent 55%),
    linear-gradient(180deg, #f8fafc, #e2e8f0);
  border-radius: 14px;
  border: 1px solid rgba(148, 163, 184, 0.4);
}

.board {
  position: relative;
  display: grid;
  grid-template-columns: repeat(5, 46px);
  grid-template-rows: repeat(5, 46px);
  gap: 0;
}

.board-cell {
  width: 46px;
  height: 46px;
  border: 1px dashed rgba(100, 116, 139, 0.35);
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.82), rgba(226, 232, 240, 0.75));
}

.charger-ring,
.robot-token {
  position: absolute;
  top: 0;
  left: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  font-weight: 800;
  font-size: 11px;
  transition:
    transform 0.7s cubic-bezier(0.22, 1, 0.36, 1),
    background-color 0.35s ease,
    box-shadow 0.35s ease;
}

.charger-ring {
  background: rgba(20, 184, 166, 0.16);
  border: 2px dashed #0f766e;
  color: #115e59;
  z-index: 1;
}

.robot-token {
  background: linear-gradient(135deg, #0ea5e9, #0284c7);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.88);
  box-shadow: 0 8px 16px rgba(2, 132, 199, 0.24);
  z-index: 2;
}

.telemetry {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 0;
}

.status-line {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.status-badge {
  background: #0f766e;
  color: white;
  border-radius: 999px;
  padding: 4px 8px;
  font-size: 10px;
  font-weight: 800;
}

.status-mode {
  font-size: 11px;
  color: #334155;
  font-weight: 700;
}

.vars-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 6px;
}

.var-card {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(148, 163, 184, 0.35);
  border-radius: 12px;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
}

.var-name {
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #64748b;
  font-weight: 700;
}

.var-value {
  font-size: 15px;
  font-weight: 800;
  color: #0f172a;
}

.effect-box {
  background: rgba(255, 247, 237, 0.9);
  border: 1px solid rgba(251, 191, 36, 0.38);
  border-radius: 13px;
  padding: 8px 10px;
}

.effect-title {
  font-size: 10px;
  font-weight: 800;
  color: #9a3412;
  margin-bottom: 3px;
}

.effect-text {
  font-size: 11px;
  color: #7c2d12;
  line-height: 1.4;
}

.battery {
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(148, 163, 184, 0.35);
  border-radius: 13px;
  padding: 8px 10px;
}

.battery-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  font-weight: 700;
  color: #334155;
  margin-bottom: 6px;
}

.battery-track {
  height: 10px;
  background: rgba(148, 163, 184, 0.18);
  border-radius: 999px;
  overflow: hidden;
}

.battery-fill {
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #f97316, #facc15, #22c55e);
  transition: width 0.7s cubic-bezier(0.22, 1, 0.36, 1);
}

.timeline {
  margin-top: 8px;
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  gap: 6px;
}

.timeline-step {
  border: 1px solid rgba(148, 163, 184, 0.32);
  background: rgba(255, 255, 255, 0.78);
  border-radius: 12px;
  padding: 6px 4px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  align-items: center;
  cursor: pointer;
  transition: transform 0.25s ease, border-color 0.25s ease, background-color 0.25s ease;
}

.timeline-step:hover {
  transform: translateY(-2px);
  border-color: rgba(14, 165, 233, 0.45);
}

.timeline-step.active {
  background: rgba(224, 242, 254, 0.92);
  border-color: rgba(14, 165, 233, 0.55);
}

.timeline-index {
  width: 20px;
  height: 20px;
  border-radius: 999px;
  background: #0f172a;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 800;
}

.timeline-label {
  font-size: 10px;
  font-weight: 700;
  color: #334155;
}

</style>
