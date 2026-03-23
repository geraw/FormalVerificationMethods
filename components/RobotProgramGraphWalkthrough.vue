<template>
  <div class="robot-walkthrough" dir="rtl">
    <div class="walkthrough-grid">
      <section class="panel">
        <div class="panel-title">גרף התוכנית</div>
        <svg class="program-graph" viewBox="0 0 360 250" aria-label="Program graph animation">
          <defs>
            <marker id="robot-pg-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
              <polygon points="0 0, 8 3, 0 6" fill="#475569" />
            </marker>
          </defs>

          <path
            d="M 177 64 C 150 96, 118 120, 92 145"
            :class="edgeClasses('load-cart')"
            marker-end="url(#robot-pg-arrow)"
          />
          <path
            d="M 74 190 C 28 220, 12 134, 66 120"
            :class="edgeClasses('cart-loop')"
            marker-end="url(#robot-pg-arrow)"
          />
          <path
            d="M 104 160 L 256 160"
            :class="edgeClasses('cart-diag')"
            marker-end="url(#robot-pg-arrow)"
          />
          <path
            d="M 286 190 C 332 220, 348 134, 294 120"
            :class="edgeClasses('diag-loop')"
            marker-end="url(#robot-pg-arrow)"
          />
          <path
            d="M 268 145 C 240 103, 214 82, 184 64"
            :class="edgeClasses('diag-load')"
            marker-end="url(#robot-pg-arrow)"
          />

          <text x="126" y="98" class="edge-label">τ</text>
          <text x="22" y="148" class="edge-label">E / N / S / W</text>
          <text x="180" y="148" class="edge-label">TR</text>
          <text x="262" y="112" class="edge-label">NE / NW / SE / SW</text>
          <text x="219" y="93" class="edge-label">x=0 ∧ y=0</text>

          <g :class="nodeClasses('load')" transform="translate(180 42)">
            <rect x="-48" y="-22" width="96" height="44" rx="16" />
            <text y="7">טעינה</text>
          </g>

          <g :class="nodeClasses('cart')" transform="translate(80 160)">
            <rect x="-56" y="-24" width="112" height="48" rx="18" />
            <text y="7">צירים</text>
          </g>

          <g :class="nodeClasses('diag')" transform="translate(280 160)">
            <rect x="-62" y="-24" width="124" height="48" rx="18" />
            <text y="7">אלכסון</text>
          </g>
        </svg>

        <div class="panel-note">{{ current.note }}</div>
      </section>

      <section class="panel">
        <div class="panel-title">הרצת הרובוט</div>
        <div class="world-layout">
          <div class="board-wrap">
            <div class="direction north">N</div>
            <div class="direction south">S</div>
            <div class="direction west">W</div>
            <div class="direction east">E</div>

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

type LocationId = 'load' | 'cart' | 'diag'
type EdgeId = 'load-cart' | 'cart-loop' | 'cart-diag' | 'diag-loop' | 'diag-load' | null

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

function edgeClasses(edgeId: EdgeId) {
  return {
    'pg-edge': true,
    'is-active': current.value.activeEdge === edgeId,
  }
}

function nodeClasses(location: LocationId) {
  return {
    'pg-node': true,
    'is-active': current.value.location === location,
  }
}

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

.program-graph {
  width: 100%;
  height: 214px;
  overflow: visible;
}

.pg-edge {
  fill: none;
  stroke: #94a3b8;
  stroke-width: 3;
  stroke-linecap: round;
  transition: stroke 0.45s ease, stroke-width 0.45s ease, filter 0.45s ease;
}

.pg-edge.is-active {
  stroke: #ea580c;
  stroke-width: 5;
  filter: drop-shadow(0 0 10px rgba(234, 88, 12, 0.28));
  stroke-dasharray: 8 6;
  animation: edge-dash 1s linear infinite;
}

.edge-label {
  font-size: 10px;
  font-weight: 700;
  fill: #475569;
}

.pg-node rect {
  fill: #e2e8f0;
  stroke: #64748b;
  stroke-width: 2.5;
  transition: fill 0.4s ease, stroke 0.4s ease, transform 0.4s ease;
}

.pg-node text {
  text-anchor: middle;
  font-size: 13px;
  font-weight: 800;
  fill: #0f172a;
}

.pg-node.is-active rect {
  fill: #fef3c7;
  stroke: #d97706;
  transform: scale(1.04);
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

.direction {
  position: absolute;
  font-size: 10px;
  font-weight: 800;
  color: #0f766e;
  letter-spacing: 0.18em;
}

.north {
  top: 4px;
  left: 50%;
  transform: translateX(-50%);
}

.south {
  bottom: 4px;
  left: 50%;
  transform: translateX(-50%);
}

.west {
  left: 4px;
  top: 50%;
  transform: translateY(-50%);
}

.east {
  right: 4px;
  top: 50%;
  transform: translateY(-50%);
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

@keyframes edge-dash {
  to {
    stroke-dashoffset: -14;
  }
}
</style>
