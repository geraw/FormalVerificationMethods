<template>
  <div class="sub-tree-demo" dir="rtl">
    <pre class="program-text">{{ currentExample.program.join('\n') }}</pre>

    <div class="tree-card">
      <div
        class="tree-stage"
        :style="{ height: `${displayHeight}px` }"
      >
        <svg
          class="tree-edges"
          :viewBox="`0 0 ${currentExample.width} ${currentExample.height}`"
          preserveAspectRatio="none"
        >
          <line
            v-for="edge in currentExample.edges"
            :key="`${edge.from}-${edge.to}`"
            :x1="nodeMap[edge.from].x"
            :y1="nodeMap[edge.from].y"
            :x2="nodeMap[edge.to].x"
            :y2="nodeMap[edge.to].y"
            :class="edgeClass(edge.to)"
          />
        </svg>

        <div
          v-for="edge in currentExample.edges"
          :key="`${edge.from}-${edge.to}-label`"
          class="edge-label"
          :class="{ active: currentStep >= nodeMap[edge.to].step }"
          :style="edgeLabelStyle(edge)"
          dir="ltr"
        >
          {{ edge.label }}
        </div>

        <div
          v-for="node in currentExample.nodes"
          :key="`${node.id}-sub`"
          v-show="node.sub && currentStep >= node.step"
          class="sub-box"
          :class="subState(node)"
          :style="subStyle(node)"
          dir="ltr"
        >
          <div
            v-for="line in node.sub?.lines || []"
            :key="line"
            class="sub-line"
          >
            {{ line }}
          </div>
        </div>

        <div
          v-for="node in currentExample.nodes"
          :key="node.id"
          class="tree-node"
          :class="nodeState(node)"
          :style="nodeStyle(node)"
          dir="ltr"
        >
          <div
            v-for="line in node.lines"
            :key="line"
            class="tree-node-line"
          >
            {{ line }}
          </div>
        </div>
      </div>
    </div>

    <div class="note-card">
      <div class="note-text">{{ currentNote }}</div>

      <div class="rule-block">
        <div class="rule-title">{{ currentRule.title }}</div>
        <div
          v-for="line in currentRule.lines"
          :key="line"
          class="rule-line"
          dir="auto"
        >
          {{ line }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import {
  examples,
  type ExampleKey,
  type StepRule,
  type TreeEdge,
  type TreeNode,
} from './NanoPromelaSubTree.examples'

const props = defineProps<{
  example: ExampleKey
}>()

const { $clicks } = useSlideContext()

const currentExample = computed(() => examples[props.example])

const nodeMap = computed(() =>
  Object.fromEntries(currentExample.value.nodes.map(node => [node.id, node])),
) as unknown as Record<string, TreeNode>

const currentStep = computed(() => {
  const raw = Number($clicks.value || 0)
  return Math.min(raw, currentExample.value.maxSteps)
})

const displayHeight = computed(() =>
  Math.round(currentExample.value.height * 0.88),
)

const currentNote = computed(() =>
  currentExample.value.notes[currentStep.value] ?? '',
)

const currentRule = computed<StepRule>(() =>
  currentExample.value.rules[currentStep.value] ?? {
    title: '',
    lines: [],
  },
)

function nodeStyle(node: TreeNode) {
  return {
    left: `${(node.x / currentExample.value.width) * 100}%`,
    top: `${(node.y / currentExample.value.height) * 100}%`,
    width: `${node.width}px`,
  }
}

function subStyle(node: TreeNode) {
  const sub = node.sub!
  const placement = sub.placement ?? 'above-node'
  const leftValue = placement === 'absolute'
    ? sub.x
    : node.x
  const topValue = placement === 'absolute'
    ? sub.y
    : node.y - 18

  return {
    left: `${(leftValue / currentExample.value.width) * 100}%`,
    top: `${(topValue / currentExample.value.height) * 100}%`,
    width: `${sub.width}px`,
    '--sub-translate-y': placement === 'absolute'
      ? 'calc(-50% - 4px)'
      : 'calc(-100% - 6px)',
  }
}

function edgeLabelStyle(edge: TreeEdge) {
  return {
    left: `${(edge.labelX / currentExample.value.width) * 100}%`,
    top: `${(edge.labelY / currentExample.value.height) * 100}%`,
  }
}

function nodeState(node: TreeNode) {
  if (currentStep.value === 0)
    return 'pending'
  if (currentStep.value === node.step)
    return 'current'
  if (currentStep.value > node.step)
    return 'done'
  return 'pending'
}

function subState(node: TreeNode) {
  return currentStep.value === node.step
    ? 'current'
    : 'done'
}

function edgeClass(targetId: string) {
  return currentStep.value >= nodeMap.value[targetId].step
    ? 'tree-edge edge-done'
    : 'tree-edge edge-pending'
  }
</script>

<style scoped>
.sub-tree-demo {
  display: flex;
  flex-direction: column;
  gap: 6px;
  max-width: 900px;
  margin: 0 auto;
}

.program-text,
.tree-card,
.note-card {
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

.tree-card {
  position: relative;
  padding: 7px 7px 12px;
}

.tree-stage {
  position: relative;
  overflow: visible;
  border-radius: 14px;
  background:
    radial-gradient(circle at top left, rgba(125, 211, 252, 0.18), transparent 36%),
    radial-gradient(circle at bottom right, rgba(251, 191, 36, 0.16), transparent 32%),
    #f8fafc;
}

.tree-edges {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.tree-edge {
  fill: none;
  stroke-linecap: round;
  transition: stroke 220ms ease, stroke-width 220ms ease, opacity 220ms ease;
}

.edge-pending {
  stroke: #cbd5e1;
  stroke-width: 2.2;
  opacity: 0.8;
}

.edge-done {
  stroke: #0ea5e9;
  stroke-width: 3.4;
}

.edge-label {
  position: absolute;
  transform: translate(-50%, -50%);
  padding: 1px 5px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.94);
  border: 1px solid #cbd5e1;
  color: #475569;
  font-size: 9px;
  line-height: 1.2;
  transition: all 220ms ease;
}

.edge-label.active {
  border-color: #7dd3fc;
  color: #0369a1;
}

.tree-node {
  position: absolute;
  transform: translate(-50%, -50%);
  border-radius: 14px;
  border: 2px solid #cbd5e1;
  background: rgba(255, 255, 255, 0.96);
  color: #0f172a;
  padding: 6px 8px 4px;
  min-height: 36px;
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.08);
  text-align: center;
  transition: all 220ms ease;
}

.tree-node.pending {
  opacity: 0.45;
  transform: translate(-50%, -50%) scale(0.97);
}

.tree-node.current {
  opacity: 1;
  border-color: #f59e0b;
  background: #fef3c7;
  box-shadow: 0 16px 32px rgba(245, 158, 11, 0.22);
  transform: translate(-50%, -50%) scale(1.03);
}

.tree-node.done {
  opacity: 1;
  border-color: #10b981;
  background: #ecfdf5;
}

.tree-node-line {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 10.4px;
  line-height: 1.14;
  white-space: nowrap;
}

.sub-box {
  position: absolute;
  transform: translate(-50%, var(--sub-translate-y));
  z-index: 2;
  border-radius: 12px;
  border: 1px solid #cbd5e1;
  background: rgba(255, 255, 255, 0.96);
  padding: 5px 6px;
  box-shadow: 0 8px 16px rgba(15, 23, 42, 0.08);
  transition: all 220ms ease;
}

.sub-box.current {
  border-color: #f59e0b;
  background: #fff7ed;
  box-shadow: 0 14px 24px rgba(245, 158, 11, 0.18);
}

.sub-box.done {
  border-color: #93c5fd;
  background: #eff6ff;
}

.sub-line {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8.9px;
  line-height: 1.12;
  white-space: pre;
}

.note-card {
  padding: 7px 10px 8px;
  color: #334155;
}

.note-text {
  font-size: 10.1px;
  line-height: 1.26;
}

.rule-block {
  margin-top: 5px;
  padding-top: 5px;
  border-top: 1px dashed #cbd5e1;
}

.rule-title {
  display: inline-block;
  margin-bottom: 3px;
  padding: 1px 7px;
  border-radius: 999px;
  background: #ffedd5;
  border: 1px solid #fdba74;
  color: #9a3412;
  font-size: 8.8px;
  font-weight: 700;
}

.rule-line {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 8.7px;
  line-height: 1.14;
  color: #0f172a;
  white-space: pre;
  text-align: start;
}
</style>
