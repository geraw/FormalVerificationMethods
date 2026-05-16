<template>
  <span
    class="katex-inline"
    :class="{ 'katex-display-wrapper': display }"
    v-html="rendered"
  />
</template>

<script setup lang="ts">
import { computed } from 'vue';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const props = withDefaults(defineProps<{
  math: string;
  display?: boolean;
}>(), {
  display: false,
});

const rendered = computed(() => {
  try {
    return katex.renderToString(props.math, {
      throwOnError: false,
      displayMode: props.display,
    });
  } catch {
    return props.math;
  }
});
</script>

<style scoped>
.katex-inline {
  display: inline-block;
}

.katex-display-wrapper {
  width: 100%;
}
</style>
