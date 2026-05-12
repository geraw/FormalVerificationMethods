<template>
  <div class="automaton-container flex justify-center items-center" dir="ltr"
       @mousedown.stop @touchstart.stop @pointerdown.stop @wheel.stop>
    <svg :width="width" :height="height" class="overflow-visible">
      <defs>
        <marker v-for="color in uniqueColors" :key="color"
                :id="getMarkerId(color)"
                markerWidth="7" markerHeight="7" refX="6.5" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 z" :fill="color" />
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

          <foreignObject v-if="transition.label"
                         :x="transition.labelX - transition.labelWidth / 2"
                         :y="transition.labelY - transition.labelHeight / 2"
                         :width="transition.labelWidth"
                         :height="transition.labelHeight"
                         class="overflow-visible pointer-events-none">
            <div class="automaton-label"
                 :style="{ color: transition.labelColor, fontSize: `${transition.labelFontSize}px` }"
                 v-html="renderMath(transition.label)" />
          </foreignObject>
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
                  :stroke-width="state.strokeWidth" />
          <circle v-if="state.accepting"
                  :cx="state.x" :cy="state.y" :r="state.r - 6"
                  fill="none"
                  :stroke="state.stroke"
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
  strokeWidth?: number;
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
  labelX?: number;
  labelY?: number;
  labelWidth?: number;
  labelHeight?: number;
  labelFontSize?: number;
  labelColor?: string;
  curve?: number;
  loopDirection?: string;
  loopRadius?: number;
  stroke?: string;
  strokeWidth?: number;
  dasharray?: string;
}

interface Props {
  states: AutomatonState[];
  transitions: AutomatonTransition[];
  width?: number;
  height?: number;
  defaultStateFill?: string;
  defaultStroke?: string;
}

const props = withDefaults(defineProps<Props>(), {
  width: 520,
  height: 260,
  defaultStateFill: '#fef9c3',
  defaultStroke: '#111827',
});

const defaultStroke = computed(() => props.defaultStroke);
const markerIdBase = `arrowhead-automaton-${Math.random().toString(36).slice(2, 11)}`;

const normalizedStates = computed(() => props.states.map((state) => ({
  ...state,
  r: state.r ?? 34,
  fill: state.fill ?? props.defaultStateFill,
  stroke: state.stroke ?? props.defaultStroke,
  strokeWidth: state.strokeWidth ?? 2.2,
  textColor: state.textColor ?? '#111827',
  labelWidth: state.labelWidth ?? 90,
  labelHeight: state.labelHeight ?? 44,
  labelFontSize: state.labelFontSize ?? 22,
})));

const statesById = computed(() => {
  const map = new Map<string, ReturnType<typeof normalizedStates.value[number]>>();
  normalizedStates.value.forEach((state) => map.set(state.id, state));
  return map;
});

const initialStates = computed(() => normalizedStates.value.filter((state) => state.initial));

const uniqueColors = computed(() => {
  const colors = new Set<string>([props.defaultStroke]);
  props.states.forEach((state) => {
    if (state.stroke) colors.add(state.stroke);
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

  const stroke = transition.stroke ?? props.defaultStroke;
  const strokeWidth = transition.strokeWidth ?? 2.4;
  const labelWidth = transition.labelWidth ?? 72;
  const labelHeight = transition.labelHeight ?? 34;
  const labelFontSize = transition.labelFontSize ?? 20;
  const labelColor = transition.labelColor ?? stroke;

  if (source.id === target.id) {
    const direction = parseAngle(transition.loopDirection ?? '-90deg');
    const radius = transition.loopRadius ?? source.r * 1.35;
    const anchorX = source.x + Math.cos(direction) * source.r * 0.55;
    const anchorY = source.y + Math.sin(direction) * source.r * 0.55;
    const c1x = source.x + Math.cos(direction - 0.9) * radius;
    const c1y = source.y + Math.sin(direction - 0.9) * radius;
    const c2x = source.x + Math.cos(direction + 0.9) * radius;
    const c2y = source.y + Math.sin(direction + 0.9) * radius;
    const endX = source.x + Math.cos(direction + 0.52) * source.r;
    const endY = source.y + Math.sin(direction + 0.52) * source.r;
    const labelX = transition.labelX ?? source.x + Math.cos(direction) * (radius + 16);
    const labelY = transition.labelY ?? source.y + Math.sin(direction) * (radius + 16);

    return [{
      id: transition.id ?? `${transition.source}-${transition.target}-${index}`,
      path: `M ${anchorX} ${anchorY} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${endX} ${endY}`,
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
    }];
  }

  const dx = target.x - source.x;
  const dy = target.y - source.y;
  const distance = Math.hypot(dx, dy) || 1;
  const ux = dx / distance;
  const uy = dy / distance;
  const startX = source.x + ux * source.r;
  const startY = source.y + uy * source.r;
  const endX = target.x - ux * target.r;
  const endY = target.y - uy * target.r;
  const curve = transition.curve ?? 0;
  const mx = (startX + endX) / 2;
  const my = (startY + endY) / 2;
  const normalX = -uy;
  const normalY = ux;
  const cx = mx + normalX * curve * distance;
  const cy = my + normalY * curve * distance;
  const path = Math.abs(curve) < 0.001
    ? `M ${startX} ${startY} L ${endX} ${endY}`
    : `M ${startX} ${startY} Q ${cx} ${cy} ${endX} ${endY}`;
  const labelX = transition.labelX ?? mx + normalX * curve * distance + normalX * 18;
  const labelY = transition.labelY ?? my + normalY * curve * distance + normalY * 18;

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
  }];
}));

function getMarkerId(color: string) {
  return `${markerIdBase}-${color.replace(/[^a-zA-Z0-9]/g, '')}`;
}

function parseAngle(value: string) {
  if (value.endsWith('deg')) return Number(value.slice(0, -3)) * Math.PI / 180;
  return Number(value) || 0;
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
  const length = state.r + 38;
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
</style>
