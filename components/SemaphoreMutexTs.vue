<template>
  <TransitionSystemD3
    :width="width"
    :height="height"
    :auto="false"
    :states="states"
    :transitions="transitions"
    :highlighted-state-ids="highlightStarvation ? starvationStateIds : []"
    :highlighted-transition-ids="highlightedTransitionIds"
    :fade-unhighlighted="false"
    :pulse-highlights="false"
    highlight-color="#dc2626"
    :highlight-fill="null"
  />
</template>

<script setup lang="ts">
import { computed } from 'vue';
import TransitionSystemD3 from './TransitionSystemD3.vue';

const props = withDefaults(defineProps<{
  width?: number;
  height?: number;
  highlightStarvation?: boolean;
  highlightEnter2Opportunity?: boolean;
  highlightProblematicRun?: boolean;
}>(), {
  width: 620,
  height: 430,
  highlightStarvation: false,
  highlightEnter2Opportunity: false,
  highlightProblematicRun: false,
});

const stateStyle = {
  width: 118,
  color: '#ffffff',
  stroke: '#111827',
  textFontSize: 13,
};

const starvationStateIds = ['free', 'n1w2', 'bothWait', 'c1w2'];
const starvationTransitionIds = new Set(['req2', 'req1FromW2', 'enter1FromBoth', 'rel1ToW2']);
const enter2OpportunityTransitionIds = new Set(['enter2FromW2', 'enter2FromBoth']);
const enter2OpportunityColor = '#2563eb';

// Dedicated stage-2 run: red problematic cycle + blue missed opportunities.
const problematicRunStateIds = ['free', 'w1n2', 'c1n2'];
const problematicRunRedTransitionIds = new Set([
  'req1',
  'enter1FromW1',
  'rel1',
]);
const problematicRunBlueTransitionIds = new Set([
  'req2',
  'req2FromW1',
  'req2InCrit1',
]);

const highlightedTransitionIds = computed(() => [
  ...(props.highlightProblematicRun
    ? [
        ...Array.from(problematicRunRedTransitionIds),
        ...Array.from(problematicRunBlueTransitionIds),
      ]
    : []),
  ...(props.highlightStarvation ? Array.from(starvationTransitionIds) : []),
  ...(props.highlightEnter2Opportunity ? Array.from(enter2OpportunityTransitionIds) : []),
]);

const baseStates = [
  { id: 'free', text: '$n_1,n_2,y=1$', initial: true, initialDirection: 'top' as const, x: 320, y: 50, ...stateStyle },
  { id: 'w1n2', text: '$w_1,n_2,y=1$', x: 205, y: 145, ...stateStyle },
  { id: 'n1w2', text: '$n_1,w_2,y=1$', x: 435, y: 145, ...stateStyle },
  { id: 'c1n2', text: '$c_1,n_2,y=0$', x: 78, y: 260, ...stateStyle },
  { id: 'bothWait', text: '$w_1,w_2,y=1$', x: 320, y: 260, ...stateStyle },
  { id: 'n1c2', text: '$n_1,c_2,y=0$', x: 565, y: 260, ...stateStyle },
  { id: 'c1w2', text: '$c_1,w_2,y=0$', x: 190, y: 352, ...stateStyle },
  { id: 'w1c2', text: '$w_1,c_2,y=0$', x: 470, y: 365, ...stateStyle },
];

const baseTransitions = [
  { id: 'req1', source: 'free', target: 'w1n2', action: '$req_1$', midPoints: [{ x: 205, y: 92 }], actionY: -14 },
  { id: 'req2', source: 'free', target: 'n1w2', action: '$req_2$', midPoints: [{ x: 435, y: 92 }], actionY: -14, highlightStroke: '#dc2626', highlightStrokeWidth: 3.2 },
  { id: 'enter1FromW1', source: 'w1n2', target: 'c1n2', action: '$enter_1$', midPoints: [{ x: 78, y: 145 }], actionX: -20, actionY: -18 },
  { id: 'enter2FromW2', source: 'n1w2', target: 'n1c2', action: '$enter_2$', midPoints: [{ x: 565, y: 145 }], actionX: 18, actionY: -18 },
  { id: 'req2FromW1', source: 'w1n2', target: 'bothWait', action: '$req_2$', midPoints: [{ x: 276, y: 145 }], actionY: -16 },
  { id: 'req1FromW2', source: 'n1w2', target: 'bothWait', action: '$req_1$', midPoints: [{ x: 364, y: 145 }], actionY: -16, highlightStroke: '#dc2626', highlightStrokeWidth: 3.2 },
  { id: 'rel1', source: 'c1n2', target: 'free', action: '$rel$', midPoints: [{ x: 18, y: 260 }, { x: 18, y: 32 }, { x: 252, y: 32 }], actionX: 170, actionY: -18 },
  { id: 'rel2', source: 'n1c2', target: 'free', action: '$rel$', midPoints: [{ x: 622, y: 260 }, { x: 622, y: 32 }, { x: 388, y: 32 }], actionX: -170, actionY: -18 },
  { id: 'req2InCrit1', source: 'c1n2', target: 'c1w2', action: '$req_2$', midPoints: [{ x: 78, y: 352 }], actionX: -26, actionY: -8 },
  { id: 'req1InCrit2', source: 'n1c2', target: 'w1c2', action: '$req_1$', midPoints: [{ x: 565, y: 365 }], actionX: 22, actionY: -8 },
  { id: 'enter1FromBoth', source: 'bothWait', target: 'c1w2', action: '$enter_1$', midPoints: [{ x: 190, y: 260 }], actionX: -12, actionY: 34, highlightStroke: '#dc2626', highlightStrokeWidth: 3.2 },
  { id: 'enter2FromBoth', source: 'bothWait', target: 'w1c2', action: '$enter_2$', midPoints: [{ x: 470, y: 260 }], actionX: 36, actionY: 46 },
  { id: 'rel1ToW2', source: 'c1w2', target: 'n1w2', action: '$rel_1$', midPoints: [{ x: 435, y: 352 }], curve: 1, actionX: -62, actionY: -52, highlightStroke: '#dc2626', highlightStrokeWidth: 3.2 },
  { id: 'rel2ToW1', source: 'w1c2', target: 'w1n2', action: '$rel_2$', midPoints: [{ x: 205, y: 365 }], curve: 1, actionX: 58, actionY: -56 },
];

const states = computed(() => baseStates.map(state => {
  if (props.highlightProblematicRun && problematicRunStateIds.includes(state.id)) {
    return {
      ...state,
      textColor: '#dc2626',
      highlightStroke: '#dc2626',
      highlightStrokeWidth: 3.2,
    };
  }

  if (!props.highlightStarvation || !starvationStateIds.includes(state.id)) {
    return state;
  }

  return {
    ...state,
    textColor: '#dc2626',
    highlightStroke: '#dc2626',
    highlightStrokeWidth: 3.2,
  };
}));

const transitions = computed(() => baseTransitions.map(transition => {
  if (props.highlightProblematicRun && problematicRunBlueTransitionIds.has(transition.id)) {
    return {
      ...transition,
      stroke: enter2OpportunityColor,
      strokeWidth: 3,
      labelColor: enter2OpportunityColor,
      highlightStroke: enter2OpportunityColor,
      highlightStrokeWidth: 3.2,
    };
  }

  if (props.highlightProblematicRun && problematicRunRedTransitionIds.has(transition.id)) {
    return {
      ...transition,
      stroke: '#dc2626',
      strokeWidth: 3,
      labelColor: '#dc2626',
      highlightStroke: '#dc2626',
      highlightStrokeWidth: 3.2,
    };
  }

  if (props.highlightEnter2Opportunity && enter2OpportunityTransitionIds.has(transition.id)) {
    return {
      ...transition,
      stroke: enter2OpportunityColor,
      strokeWidth: 3,
      labelColor: enter2OpportunityColor,
      highlightStroke: enter2OpportunityColor,
      highlightStrokeWidth: 3.2,
    };
  }

  if (!props.highlightStarvation || !starvationTransitionIds.has(transition.id)) {
    return transition;
  }

  return {
    ...transition,
    stroke: '#dc2626',
    strokeWidth: 3,
    labelColor: '#dc2626',
    highlightStroke: '#dc2626',
    highlightStrokeWidth: 3.2,
  };
}));
</script>
