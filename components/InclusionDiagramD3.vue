<template>
  <div ref="containerRef" class="inclusion-diagram flex justify-center items-center" dir="rtl"></div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';
import * as d3 from 'd3';

interface InclusionSet {
  label: string;
  fill?: string;
  stroke?: string;
  textColor?: string;
  X?: number;
  Y?: number;
  x?: number;
  y?: number;
}

interface Props {
  sets: InclusionSet[];
  width?: number;
  height?: number;
  fontSize?: number;
  labelYOffset?: number;
}

const props = withDefaults(defineProps<Props>(), {
  width: 760,
  height: 300,
  fontSize: 24,
  labelYOffset: 0,
});

const containerRef = ref<HTMLDivElement | null>(null);

function draw() {
  if (!containerRef.value) return;

  const root = d3.select(containerRef.value);
  root.selectAll('*').remove();

  const svg = root
    .append('svg')
    .attr('width', props.width)
    .attr('height', props.height)
    .attr('viewBox', `0 0 ${props.width} ${props.height}`)
    .attr('class', 'overflow-visible');

  const count = Math.max(props.sets.length, 1);
  const cx = props.width / 2;
  const baseBottom = props.height - 14;
  const maxRx = props.width * 0.49;
  const maxRy = props.height * 0.43;
  const minRx = props.width * 0.24;
  const minRy = props.height * 0.12;
  const verticalStep = count > 1 ? (maxRy - minRy) / (count - 1) : 0;
  const horizontalStep = count > 1 ? (maxRx - minRx) / (count - 1) : 0;

  const palette = [
    { fill: '#b85f45', stroke: '#df927c', textColor: '#ffffff' },
    { fill: '#5ca5ab', stroke: '#b9eef0', textColor: '#ffffff' },
    { fill: '#ef8f8f', stroke: '#c45f5f', textColor: '#6b2f1f' },
    { fill: '#ead0cd', stroke: '#9b7777', textColor: '#6b2f1f' },
  ];

  const rendered = props.sets.map((set, index) => {
    const t = count === 1 ? 0 : index / (count - 1);
    const rx = maxRx - t * (maxRx - minRx);
    const ry = maxRy - t * (maxRy - minRy);
    const cy = baseBottom - ry - index * verticalStep * 0.18;
    return {
      ...set,
      rx,
      ry,
      cx,
      cy,
      fill: set.fill ?? palette[index % palette.length].fill,
      stroke: set.stroke ?? palette[index % palette.length].stroke,
      textColor: set.textColor ?? palette[index % palette.length].textColor,
      labelX: cx + (set.X ?? set.x ?? 0),
      labelY: cy - ry * 0.55 + props.labelYOffset + defaultLabelYOffset(index, count) + (set.Y ?? set.y ?? 0),
    };
  });

  const groups = svg.selectAll('g.inclusion-set')
    .data(rendered)
    .join('g')
    .attr('class', 'inclusion-set');

  groups.append('ellipse')
    .attr('cx', (d) => d.cx)
    .attr('cy', (d) => d.cy)
    .attr('rx', (d) => d.rx)
    .attr('ry', (d) => d.ry)
    .attr('fill', (d) => d.fill)
    .attr('fill-opacity', 0.92)
    .attr('stroke', (d) => d.stroke)
    .attr('stroke-width', 2)
    .attr('filter', 'drop-shadow(0 4px 4px rgb(0 0 0 / 0.28))');

  groups.append('text')
    .attr('x', (d) => d.labelX)
    .attr('y', (d) => d.labelY)
    .attr('fill', (d) => d.textColor)
    .attr('font-size', props.fontSize)
    .attr('font-weight', 700)
    .attr('text-anchor', 'middle')
    .attr('dominant-baseline', 'middle')
    .style('font-family', 'Arial, sans-serif')
    .text((d) => d.label);
}

function defaultLabelYOffset(index: number, count: number) {
  if (count === 4) return [-30, -20, -10, 0][index] ?? 0;
  return index * 8;
}

onMounted(draw);
watch(() => props, draw, { deep: true });
</script>
