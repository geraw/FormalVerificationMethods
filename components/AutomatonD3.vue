<template>
  <div class="automaton-container flex justify-center items-center" dir="ltr"
       @mousedown.stop @touchstart.stop @pointerdown.stop @wheel.stop>
    <svg :width="width" :height="height" class="overflow-visible">
      <defs>
        <filter :id="shadowId" x="-30%" y="-30%" width="160%" height="160%">
          <feDropShadow dx="4" dy="4" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.22" />
        </filter>
        <marker v-for="color in uniqueColors" :key="color"
                :id="getMarkerId(color)"
                :markerWidth="arrowSize * 1.9" :markerHeight="arrowSize * 1.9"
                viewBox="0 -5 10 10"
                refX="9" refY="0" orient="auto">
          <path d="M 0 -4 L 9 0 L 0 4 z" :fill="color" />
        </marker>
      </defs>

      <g class="transitions">
        <g v-for="transition in renderedTransitions" :key="transition.id">
          <path :d="transition.path"
                fill="none"
                :stroke="transition.stroke"
                :stroke-width="transition.strokeWidth"
                :stroke-dasharray="transition.dasharray"
                stroke-linecap="round"
                :marker-end="`url(#${getMarkerId(transition.stroke)})`" />
        </g>
      </g>

      <g class="initial-arrows">
        <g v-for="state in initialStates" :key="`initial-${state.id}`">
          <path :d="initialArrowPath(state)"
                fill="none"
                :stroke="state.initialStroke || defaultStroke"
                :stroke-width="state.initialStrokeWidth || 2.4"
                stroke-linecap="round"
                :marker-end="`url(#${getMarkerId(state.initialStroke || defaultStroke)})`" />
          <foreignObject v-if="state.initialLabel"
                         :x="initialLabelPosition(state).x"
                         :y="initialLabelPosition(state).y"
                         :width="state.initialLabelWidth || 52"
                         :height="state.initialLabelHeight || 28"
                         class="overflow-visible pointer-events-none">
            <div class="automaton-label"
                 :style="{ color: state.initialStroke || defaultStroke, fontSize: `${state.initialLabelFontSize || 18}px` }"
                 v-html="renderMath(state.initialLabel)" />
          </foreignObject>
        </g>
      </g>

      <g class="states">
        <g v-for="state in normalizedStates" :key="state.id">
          <circle :cx="state.x" :cy="state.y" :r="state.r"
                  :fill="state.fill"
                  :stroke="state.stroke"
                  :stroke-width="state.strokeWidth"
                  :filter="state.shadow ? `url(#${shadowId})` : undefined" />
          <circle v-if="state.accepting"
                  :cx="state.x" :cy="state.y" :r="state.r - 6"
                  fill="none"
                  :stroke="state.innerStroke"
                  :stroke-width="Math.max(1.6, state.strokeWidth - 0.4)" />
          <foreignObject :x="state.x - state.labelWidth / 2"
                         :y="state.y - state.labelHeight / 2"
                         :width="state.labelWidth"
                         :height="state.labelHeight"
                         class="overflow-visible pointer-events-none">
            <div class="automaton-state-label"
                 :style="{ color: state.textColor, fontSize: `${state.labelFontSize}px` }"
                 v-html="renderMath(state.label || state.id)" />
          </foreignObject>
        </g>
      </g>

      <g class="transition-labels">
        <g v-for="transition in renderedTransitions" :key="`label-${transition.id}`">
          <foreignObject v-if="transition.label"
                         :x="transition.labelX - transition.labelWidth / 2"
                         :y="transition.labelY - transition.labelHeight / 2"
                         :width="transition.labelWidth"
                         :height="transition.labelHeight"
                         class="overflow-visible">
            <div class="automaton-label automaton-transition-label"
                 :style="{ color: transition.labelColor, fontSize: `${transition.labelFontSize}px` }">
              <span v-html="renderMath(transition.label)" />
              <span v-if="transition.tooltip"
                    class="automaton-tooltip"
                    dir="rtl">{{ transition.tooltip }}</span>
            </div>
          </foreignObject>
        </g>
      </g>
    </svg>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import katex from 'katex';
import 'katex/dist/katex.min.css';

type Direction = 'left' | 'right' | 'top' | 'bottom';

interface AutomatonState {
  id: string;
  x: number;
  y: number;
  r?: number;
  label?: string;
  accepting?: boolean;
  initial?: boolean;
  initialDirection?: Direction;
  initialLabel?: string;
  initialLabelWidth?: number;
  initialLabelHeight?: number;
  initialLabelFontSize?: number;
  initialStroke?: string;
  initialStrokeWidth?: number;
  fill?: string;
  stroke?: string;
  innerStroke?: string;
  strokeWidth?: number;
  shadow?: boolean;
  textColor?: string;
  labelWidth?: number;
  labelHeight?: number;
  labelFontSize?: number;
}

interface AutomatonTransition {
  id?: string;
  source: string;
  target: string;
  label?: string;
  labelX?: number; // Offset from the natural label position.
  labelY?: number; // Offset from the natural label position; 0 keeps it near the edge.
  labelWidth?: number;
  labelHeight?: number;
  labelFontSize?: number;
  labelColor?: string;
  curve?: number;
  sourceAngle?: string;
  targetAngle?: string;
  loopDirection?: string;
  loopRadius?: number;
  loopAngle?: number;
  loopSpread?: number;
  stroke?: string;
  strokeWidth?: number;
  dasharray?: string;
  tooltip?: string;
}

interface Props {
  states: AutomatonState[];
  transitions: AutomatonTransition[];
  width?: number;
  height?: number;
  defaultStateFill?: string;
  defaultStroke?: string;
  defaultStateShadow?: boolean;
  variant?: 'default' | 'classic';
  arrowSize?: number;
  stateLabelFontSize?: number;
  transitionLabelFontSize?: number;
}

const props = withDefaults(defineProps<Props>(), {
  width: 520,
  height: 260,
  defaultStateFill: '#fef9c3',
  defaultStroke: '#111827',
  defaultStateShadow: false,
  variant: 'default',
  arrowSize: 5,
  stateLabelFontSize: 22,
  transitionLabelFontSize: 20,
});

const defaultStroke = computed(() => (isClassic.value ? '#6b7280' : props.defaultStroke));
const markerIdBase = `arrowhead-automaton-${Math.random().toString(36).slice(2, 11)}`;
const shadowId = `automaton-shadow-${Math.random().toString(36).slice(2, 11)}`;
const isClassic = computed(() => props.variant === 'classic');
const arrowSize = computed(() => props.arrowSize);

const normalizedStates = computed(() => props.states.map((state) => ({
  ...state,
  r: state.r ?? 34,
  fill: state.fill ?? (isClassic.value ? '#fff9c4' : props.defaultStateFill),
  stroke: state.stroke ?? defaultStroke.value,
  innerStroke: state.innerStroke ?? state.stroke ?? defaultStroke.value,
  strokeWidth: state.strokeWidth ?? (isClassic.value ? 1.6 : 2.2),
  shadow: state.shadow ?? (isClassic.value || props.defaultStateShadow),
  textColor: state.textColor ?? '#111827',
  labelWidth: state.labelWidth ?? 90,
  labelHeight: state.labelHeight ?? 44,
  labelFontSize: state.labelFontSize ?? props.stateLabelFontSize,
})));

const statesById = computed(() => {
  const map = new Map<string, ReturnType<typeof normalizedStates.value[number]>>();
  normalizedStates.value.forEach((state) => map.set(state.id, state));
  return map;
});

const initialStates = computed(() => normalizedStates.value.filter((state) => state.initial));

const uniqueColors = computed(() => {
  const colors = new Set<string>([defaultStroke.value]);
  props.states.forEach((state) => {
    if (state.stroke) colors.add(state.stroke);
    if (state.innerStroke) colors.add(state.innerStroke);
    if (state.initialStroke) colors.add(state.initialStroke);
  });
  props.transitions.forEach((transition) => {
    if (transition.stroke) colors.add(transition.stroke);
  });
  return Array.from(colors);
});

const renderedTransitions = computed(() => props.transitions.flatMap((transition, index) => {
  const source = statesById.value.get(transition.source);
  const target = statesById.value.get(transition.target);
  if (!source || !target) return [];

  const stroke = transition.stroke ?? defaultStroke.value;
  const strokeWidth = transition.strokeWidth ?? (isClassic.value ? 1.6 : 2.4);
  const labelWidth = transition.labelWidth ?? 72;
  const labelHeight = transition.labelHeight ?? 34;
  const labelFontSize = transition.labelFontSize ?? props.transitionLabelFontSize;
  const labelColor = transition.labelColor ?? stroke;

  if (source.id === target.id) {
    const direction = parseAngle(transition.loopDirection ?? '-90deg');
    const radius = transition.loopRadius ?? 76;
    const loopAngle = transition.loopAngle ?? 0.5;
    const spread = transition.loopSpread ?? 0.3;
    const start = pointOnCircle(source, direction - spread);
    const end = pointOnCircle(source, direction + spread);
    const c1x = source.x + Math.cos(direction - loopAngle) * radius;
    const c1y = source.y + Math.sin(direction - loopAngle) * radius;
    const c2x = source.x + Math.cos(direction + loopAngle) * radius;
    const c2y = source.y + Math.sin(direction + loopAngle) * radius;
    const loopLabelPoint = cubicPoint(
      start,
      { x: c1x, y: c1y },
      { x: c2x, y: c2y },
      end,
      0.5,
    );
    const naturalLabelX = loopLabelPoint.x;
    const naturalLabelY = loopLabelPoint.y;
    const labelX = naturalLabelX + (transition.labelX ?? 0);
    const labelY = naturalLabelY + (transition.labelY ?? 0);

    return [{
      id: transition.id ?? `${transition.source}-${transition.target}-${index}`,
      path: `M ${start.x} ${start.y} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${end.x} ${end.y}`,
      stroke,
      strokeWidth,
      dasharray: transition.dasharray,
      label: transition.label,
      labelX,
      labelY,
      labelWidth,
      labelHeight,
      labelFontSize,
      labelColor,
      tooltip: transition.tooltip,
    }];
  }

  const dx = target.x - source.x;
  const dy = target.y - source.y;
  const distance = Math.hypot(dx, dy) || 1;
  const ux = dx / distance;
  const uy = dy / distance;
  const curve = transition.curve ?? 0;
  const normalX = -uy;
  const normalY = ux;
  const centerMx = (source.x + target.x) / 2;
  const centerMy = (source.y + target.y) / 2;
  const cx = centerMx + normalX * curve * distance;
  const cy = centerMy + normalY * curve * distance;

  const naturalStartAngle = Math.abs(curve) < 0.001
    ? Math.atan2(dy, dx)
    : Math.atan2(cy - source.y, cx - source.x);
  const naturalEndAngle = Math.abs(curve) < 0.001
    ? Math.atan2(source.y - target.y, source.x - target.x)
    : Math.atan2(cy - target.y, cx - target.x);
  const startAngle = transition.sourceAngle ? parseAngle(transition.sourceAngle) : naturalStartAngle;
  const endAngle = transition.targetAngle ? parseAngle(transition.targetAngle) : naturalEndAngle;
  const start = pointOnCircle(source, startAngle);
  const end = pointOnCircle(target, endAngle);

  const path = Math.abs(curve) < 0.001
    ? `M ${start.x} ${start.y} L ${end.x} ${end.y}`
    : `M ${start.x} ${start.y} Q ${cx} ${cy} ${end.x} ${end.y}`;
  const labelPoint = Math.abs(curve) < 0.001
    ? { x: (start.x + end.x) / 2, y: (start.y + end.y) / 2 }
    : quadraticPoint(start, { x: cx, y: cy }, end, 0.5);
  const naturalLabelX = labelPoint.x;
  const naturalLabelY = labelPoint.y;
  const labelX = naturalLabelX + (transition.labelX ?? 0);
  const labelY = naturalLabelY + (transition.labelY ?? 0);

  return [{
    id: transition.id ?? `${transition.source}-${transition.target}-${index}`,
    path,
    stroke,
    strokeWidth,
    dasharray: transition.dasharray,
    label: transition.label,
    labelX,
    labelY,
    labelWidth,
    labelHeight,
    labelFontSize,
    labelColor,
    tooltip: transition.tooltip,
  }];
}));

function getMarkerId(color: string) {
  return `${markerIdBase}-${color.replace(/[^a-zA-Z0-9]/g, '')}`;
}

function parseAngle(value: string) {
  if (value.endsWith('deg')) return Number(value.slice(0, -3)) * Math.PI / 180;
  return Number(value) || 0;
}

function cubicPoint(
  p0: { x: number; y: number },
  p1: { x: number; y: number },
  p2: { x: number; y: number },
  p3: { x: number; y: number },
  t: number,
) {
  const mt = 1 - t;
  return {
    x: mt ** 3 * p0.x + 3 * mt ** 2 * t * p1.x + 3 * mt * t ** 2 * p2.x + t ** 3 * p3.x,
    y: mt ** 3 * p0.y + 3 * mt ** 2 * t * p1.y + 3 * mt * t ** 2 * p2.y + t ** 3 * p3.y,
  };
}

function quadraticPoint(
  p0: { x: number; y: number },
  p1: { x: number; y: number },
  p2: { x: number; y: number },
  t: number,
) {
  const mt = 1 - t;
  return {
    x: mt ** 2 * p0.x + 2 * mt * t * p1.x + t ** 2 * p2.x,
    y: mt ** 2 * p0.y + 2 * mt * t * p1.y + t ** 2 * p2.y,
  };
}

function pointOnCircle(state: ReturnType<typeof normalizedStates.value[number]>, angle: number) {
  return {
    x: state.x + Math.cos(angle) * state.r,
    y: state.y + Math.sin(angle) * state.r,
  };
}

function renderMath(value: string) {
  const trimmed = value.trim();
  const math = trimmed.startsWith('$') && trimmed.endsWith('$')
    ? trimmed.slice(1, -1)
    : trimmed;
  try {
    return katex.renderToString(math, { throwOnError: false, displayMode: false });
  } catch {
    return value;
  }
}

function initialArrowPath(state: ReturnType<typeof normalizedStates.value[number]>) {
  const direction = state.initialDirection ?? 'left';
  const length = state.r + (isClassic.value ? 34 : 38);
  if (direction === 'right') return `M ${state.x + length} ${state.y} L ${state.x + state.r} ${state.y}`;
  if (direction === 'top') return `M ${state.x} ${state.y - length} L ${state.x} ${state.y - state.r}`;
  if (direction === 'bottom') return `M ${state.x} ${state.y + length} L ${state.x} ${state.y + state.r}`;
  return `M ${state.x - length} ${state.y} L ${state.x - state.r} ${state.y}`;
}

function initialLabelPosition(state: ReturnType<typeof normalizedStates.value[number]>) {
  const direction = state.initialDirection ?? 'left';
  const width = state.initialLabelWidth || 52;
  const height = state.initialLabelHeight || 28;
  if (direction === 'right') return { x: state.x + state.r + 18, y: state.y - height - 8 };
  if (direction === 'top') return { x: state.x - width - 8, y: state.y - state.r - 42 };
  if (direction === 'bottom') return { x: state.x + 8, y: state.y + state.r + 14 };
  return { x: state.x - state.r - width - 18, y: state.y - height - 8 };
}
</script>

<style scoped>
.automaton-label,
.automaton-state-label {
  direction: ltr;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  white-space: nowrap;
}

.automaton-transition-label {
  position: relative;
  pointer-events: auto;
}

.automaton-tooltip {
  position: absolute;
  left: 50%;
  bottom: calc(100% + 6px);
  transform: translateX(-50%);
  z-index: 20;
  display: none;
  width: max-content;
  max-width: 260px;
  padding: 5px 8px;
  border: 1px solid #d1d5db;
  border-radius: 4px;
  background: #ffffff;
  color: #111827;
  box-shadow: 0 4px 12px rgb(0 0 0 / 18%);
  direction: rtl;
  unicode-bidi: plaintext;
  font-size: 13px;
  line-height: 1.35;
  text-align: right;
  white-space: normal;
}

.automaton-transition-label:hover .automaton-tooltip {
  display: block;
}
</style>
