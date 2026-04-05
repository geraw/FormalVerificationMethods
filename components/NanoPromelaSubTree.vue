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

type ExampleKey = 'if-basic' | 'do-basic' | 'nested-if-do'

type SubBox = {
  x: number
  y: number
  width: number
  lines: string[]
  placement?: 'absolute' | 'above-node'
}

type TreeNode = {
  id: string
  lines: string[]
  x: number
  y: number
  width: number
  step: number
  sub?: SubBox
}

type TreeEdge = {
  from: string
  to: string
  label: string
  labelX: number
  labelY: number
}

type StepRule = {
  title: string
  lines: string[]
}

type Example = {
  program: string[]
  width: number
  height: number
  maxSteps: number
  notes: Record<number, string>
  rules: Record<number, StepRule>
  nodes: TreeNode[]
  edges: TreeEdge[]
}

const props = defineProps<{
  example: ExampleKey
}>()

const { $clicks } = useSlideContext()

const examples: Record<ExampleKey, Example> = {
  'if-basic': {
    program: [
      'if',
      ':: x > 1 -> y := x + y',
      ':: true  -> x := 0; y := x',
      'fi',
    ],
    width: 700,
    height: 285,
    maxSteps: 5,
    notes: {
      0: 'מתחילים מן העלים. בכל צעד נחשף ה-sub של צומת אחד, והוא נשאר ליד הצומת גם בהמשך.',
      1: 'לעלה y := x + y מפעילים את מקרה הבסיס, ולכן ה-sub שלו הוא רק הוא עצמו יחד עם exit.',
      2: 'כעת גם לעלה x := 0 יש sub משלו, ועדיין ההרכבה מעליו טרם חושבה.',
      3: 'הבן השני של ההרכבה, y := x, מצטרף גם הוא עם sub בסיסי משלו.',
      4: 'עכשיו אפשר לטפס להורה עם כלל ההרכבה הסדרתית: sub של שני הבנים משולב ל-sub של x := 0 ; y := x.',
      5: 'לבסוף מפעילים את ההגדרה של if: מאחדים את שני הענפים ומוסיפים cond_cmd.',
    },
    rules: {
      0: {
        title: 'כיוון העבודה',
        lines: ['מתקדמים מן העלים כלפי מעלה.'],
      },
      1: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      2: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      3: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      4: {
        title: 'הרכבה סדרתית',
        lines: ['sub(stmt1 ; stmt2) = { stmt1 ; stmt2 } ∪ (sub(stmt1) \\ {exit}) ∪ sub(stmt2)'],
      },
      5: {
        title: 'כלל if',
        lines: ['sub(if ... fi) = { cond_cmd } ∪ ⋃_i sub(stmt_i)'],
      },
    },
    nodes: [
      {
        id: 'if-root',
        lines: ['if ... fi'],
        x: 350,
        y: 58,
        width: 148,
        step: 5,
        sub: {
          x: 224,
          y: 58,
          width: 100,
          placement: 'absolute',
          lines: [
            'sub = {',
            '  cond_cmd,',
            '  y := x + y,',
            '  x := 0 ; y := x,',
            '  y := x, exit',
            '}',
          ],
        },
      },
      {
        id: 'if-left',
        lines: ['y := x + y'],
        x: 180,
        y: 188,
        width: 138,
        step: 1,
        sub: {
          x: 104,
          y: 132,
          width: 170,
          lines: ['sub = {', '  y := x + y,', '  exit', '}'],
        },
      },
      {
        id: 'if-seq',
        lines: ['x := 0 ; y := x'],
        x: 520,
        y: 166,
        width: 172,
        step: 4,
        sub: {
          x: 590,
          y: 94,
          width: 190,
          lines: ['sub = {', '  x := 0 ; y := x,', '  y := x, exit', '}'],
        },
      },
      {
        id: 'if-x0',
        lines: ['x := 0'],
        x: 405,
        y: 258,
        width: 108,
        step: 2,
        sub: {
          x: 315,
          y: 236,
          width: 150,
          lines: ['sub = {', '  x := 0,', '  exit', '}'],
        },
      },
      {
        id: 'if-yx',
        lines: ['y := x'],
        x: 540,
        y: 258,
        width: 108,
        step: 3,
        sub: {
          x: 654,
          y: 236,
          width: 142,
          lines: ['sub = {', '  y := x,', '  exit', '}'],
        },
      },
    ],
    edges: [
      { from: 'if-root', to: 'if-left', label: 'x > 1', labelX: 246, labelY: 116 },
      { from: 'if-root', to: 'if-seq', label: 'true', labelX: 452, labelY: 104 },
      { from: 'if-seq', to: 'if-x0', label: 'stmt1', labelX: 445, labelY: 214 },
      { from: 'if-seq', to: 'if-yx', label: 'stmt2', labelX: 566, labelY: 214 },
    ],
  },
  'do-basic': {
    program: [
      'do',
      ':: x > 1 -> y := x + y',
      ':: y < x -> x := 0; y := x',
      'od',
    ],
    width: 700,
    height: 295,
    maxSteps: 5,
    notes: {
      0: 'עד שלב 4 העץ דומה לדוגמת if, אבל בצעד האחרון נראה שהאופרטור do מייצר sub שונה לגמרי.',
      1: 'העלה y := x + y תורם sub בסיסי משלו.',
      2: 'גם ל-x := 0 יש sub בסיסי, שעדיין לא הומר ל-loop.',
      3: 'גם ל-y := x יש sub בסיסי. שלושת ה-sub-ים של העלים נשארים גלויים על המסך.',
      4: 'כמו קודם, קודם בונים את sub של x := 0 ; y := x לפי כלל ההרכבה הסדרתית.',
      5: 'רק בשורש do מחברים לכל תת-פקודה לא-סופית את ; loop_cmd ומוסיפים loop_cmd, exit.',
    },
    rules: {
      0: {
        title: 'כיוון העבודה',
        lines: ['מתקדמים מן העלים כלפי מעלה.'],
      },
      1: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      2: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      3: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      4: {
        title: 'הרכבה סדרתית',
        lines: ['sub(stmt1 ; stmt2) = { stmt1 ; stmt2 } ∪ (sub(stmt1) \\ {exit}) ∪ sub(stmt2)'],
      },
      5: {
        title: 'כלל do',
        lines: [
          'sub(do ... od) = { loop_cmd, exit }',
          '                 ∪ ⋃_i { stmt ; loop_cmd | stmt ∈ sub(stmt_i) \\ {exit} }',
        ],
      },
    },
    nodes: [
      {
        id: 'do-root',
        lines: ['do ... od'],
        x: 350,
        y: 58,
        width: 148,
        step: 5,
        sub: {
          x: 176,
          y: 66,
          width: 224,
          placement: 'absolute',
          lines: [
            'sub = {',
            '  loop_cmd, exit,',
            '  y := x + y ; loop_cmd,',
            '  x := 0 ; y := x ; loop_cmd,',
            '  y := x ; loop_cmd',
            '}',
          ],
        },
      },
      {
        id: 'do-left',
        lines: ['y := x + y'],
        x: 180,
        y: 192,
        width: 138,
        step: 1,
        sub: {
          x: 102,
          y: 136,
          width: 170,
          lines: ['sub = {', '  y := x + y,', '  exit', '}'],
        },
      },
      {
        id: 'do-seq',
        lines: ['x := 0 ; y := x'],
        x: 520,
        y: 170,
        width: 172,
        step: 4,
        sub: {
          x: 592,
          y: 96,
          width: 190,
          lines: ['sub = {', '  x := 0 ; y := x,', '  y := x, exit', '}'],
        },
      },
      {
        id: 'do-x0',
        lines: ['x := 0'],
        x: 405,
        y: 266,
        width: 108,
        step: 2,
        sub: {
          x: 316,
          y: 242,
          width: 148,
          lines: ['sub = {', '  x := 0,', '  exit', '}'],
        },
      },
      {
        id: 'do-yx',
        lines: ['y := x'],
        x: 590,
        y: 266,
        width: 108,
        step: 3,
        sub: {
          x: 654,
          y: 242,
          width: 142,
          lines: ['sub = {', '  y := x,', '  exit', '}'],
        },
      },
    ],
    edges: [
      { from: 'do-root', to: 'do-left', label: 'x > 1', labelX: 246, labelY: 118 },
      { from: 'do-root', to: 'do-seq', label: 'y < x', labelX: 454, labelY: 108 },
      { from: 'do-seq', to: 'do-x0', label: 'stmt1', labelX: 446, labelY: 220 },
      { from: 'do-seq', to: 'do-yx', label: 'stmt2', labelX: 568, labelY: 220 },
    ],
  },
  'nested-if-do': {
    program: [
      'if',
      ':: y = 0 -> do',
      '             :: x < 3 -> x := x + 1',
      '           od',
      ':: true  -> skip',
      'fi',
    ],
    width: 700,
    height: 265,
    maxSteps: 4,
    notes: {
      0: 'בקינון, ה-sub של הילד do נבנה קודם ורק אחר כך עובר להורה if.',
      1: 'העלה x := x + 1 מקבל sub בסיסי, כמו כל פקודה אטומית.',
      2: 'כעת do בונה sub חדש מן הילד שלו: הוא מוסיף loop_cmd ויוצר x := x + 1 ; loop_cmd.',
      3: 'גם לענף השני של if, כלומר skip, יש sub בסיסי משלו.',
      4: 'לבסוף if מאחד את sub של do עם sub של skip, ומוסיף cond_cmd.',
    },
    rules: {
      0: {
        title: 'כיוון העבודה',
        lines: ['קודם מחשבים את sub של do, ורק אחר כך של if.'],
      },
      1: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      2: {
        title: 'כלל do',
        lines: [
          'sub(do ... od) = { loop_cmd, exit }',
          '                 ∪ ⋃_i { stmt ; loop_cmd | stmt ∈ sub(stmt_i) \\ {exit} }',
        ],
      },
      3: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      4: {
        title: 'כלל if',
        lines: ['sub(if ... fi) = { cond_cmd } ∪ ⋃_i sub(stmt_i)'],
      },
    },
    nodes: [
      {
        id: 'nested-root',
        lines: ['if ... fi'],
        x: 350,
        y: 54,
        width: 146,
        step: 4,
        sub: {
          x: 520,
          y: 60,
          width: 190,
          placement: 'absolute',
          lines: [
            'sub = {',
            '  cond_cmd,',
            '  loop_cmd,',
            '  x := x + 1 ; loop_cmd,',
            '  skip, exit',
            '}',
          ],
        },
      },
      {
        id: 'nested-do',
        lines: ['do ... od'],
        x: 220,
        y: 160,
        width: 146,
        step: 2,
        sub: {
          x: 96,
          y: 162,
          width: 162,
          lines: ['sub = { loop_cmd, exit,', '        x := x + 1 ; loop_cmd }'],
        },
      },
      {
        id: 'nested-assign',
        lines: ['x := x + 1'],
        x: 220,
        y: 248,
        width: 136,
        step: 1,
        sub: {
          x: 96,
          y: 244,
          width: 150,
          lines: ['sub = { x := x + 1, exit }'],
        },
      },
      {
        id: 'nested-skip',
        lines: ['skip'],
        x: 488,
        y: 192,
        width: 102,
        step: 3,
        sub: {
          x: 608,
          y: 190,
          width: 128,
          lines: ['sub = { skip, exit }'],
        },
      },
    ],
    edges: [
      { from: 'nested-root', to: 'nested-do', label: 'y = 0', labelX: 260, labelY: 98 },
      { from: 'nested-root', to: 'nested-skip', label: 'true', labelX: 444, labelY: 118 },
      { from: 'nested-do', to: 'nested-assign', label: 'x < 3', labelX: 266, labelY: 208 },
    ],
  },
}

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
