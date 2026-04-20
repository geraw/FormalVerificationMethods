<script setup lang="ts">
import { computed, onMounted, onUnmounted } from 'vue'
import { useSlideContext } from '@slidev/client'

const clickId = Symbol('modeling-language-stack')
const { $clicksContext, $clicks } = useSlideContext()
const clickInfo = $clicksContext.calculate(1)

onMounted(() => {
  $clicksContext.register(clickId, clickInfo)
})

onUnmounted(() => {
  $clicksContext.unregister(clickId)
})

const showNano = computed(() => clickInfo?.isActive.value ?? $clicks.value >= 1)
</script>

<template>
  <div class="text-[11px] leading-snug">
    <div class="bg-amber-50 px-4 py-2 rounded border border-amber-200 mt-1 text-right">
      <slot name="intro" />
    </div>
    <div class="relative mx-auto -mt-4 h-[380px] max-w-[800px] scale-80">
      <div
        class="absolute top-0 left-[35px] flex h-[82px] w-[750px] items-center justify-center rounded-2xl border px-6 text-center text-[34px] text-white shadow-[0_6px_18px_rgba(15,23,42,0.16)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#b3ada2' : '#af843f', borderColor: showNano ? '#a8a29e' : '#fcd34d' }"
      >
        <slot name="ts" />
      </div>
      <div
        class="absolute top-[102px] left-[35px] flex h-[82px] w-[430px] items-center justify-center rounded-2xl border px-6 text-center text-[31px] text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#a79b9f' : '#0f479b', borderColor: showNano ? '#a8a29e' : '#2563eb' }"
      >
        <slot name="pg" />
      </div>
      <div
        class="absolute top-[102px] left-[478px] flex h-[82px] w-[142px] items-center justify-center rounded-2xl border px-3 text-center text-[20px] leading-tight text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#a79b9f' : '#0f479b', borderColor: showNano ? '#a8a29e' : '#2563eb' }"
      >
        <slot name="ts-weave" />
      </div>
      <div
        class="absolute top-[102px] left-[633px] flex h-[82px] w-[152px] items-center justify-center rounded-2xl border px-3 text-center text-[22px] leading-tight text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#a79b9f' : '#0f479b', borderColor: showNano ? '#a8a29e' : '#2563eb' }"
      >
        <slot name="circuit" />
      </div>
      <div
        class="absolute top-[208px] left-[35px] flex h-[82px] w-[140px] items-center justify-center rounded-2xl border px-3 text-center text-[23px] leading-tight text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#b18689' : '#af2b41', borderColor: showNano ? '#fda4af' : '#be123c' }"
      >
        <slot name="channels" />
      </div>
      <div
        class="absolute top-[208px] left-[183px] flex h-[82px] w-[140px] items-center justify-center rounded-2xl border px-3 text-center text-[20px] leading-tight text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#b18689' : '#af2b41', borderColor: showNano ? '#fda4af' : '#be123c' }"
      >
        <slot name="sync" />
      </div>
      <div
        class="absolute top-[208px] left-[330px] flex h-[82px] w-[140px] items-center justify-center rounded-2xl border px-3 text-center text-[20px] leading-tight text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)] transition-colors duration-500"
        :style="{ backgroundColor: showNano ? '#b18689' : '#af2b41', borderColor: showNano ? '#fda4af' : '#be123c' }"
      >
        <slot name="async" />
      </div>
      <transition
        enter-active-class="transition-all duration-500"
        enter-from-class="opacity-0 translate-y-6"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition-all duration-300"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 translate-y-6"
      >
        <div
          v-if="showNano"
          class="absolute top-[314px] left-[35px] flex h-[82px] w-[138px] items-center justify-center rounded-2xl border px-3 text-center text-[22px] text-white shadow-[0_6px_16px_rgba(15,23,42,0.14)]"
          style="background-color: #dc4f14; border-color: #fdba74;"
        >
          <slot name="nano" />
        </div>
      </transition>
    </div>
    <div class="relative mt-2 h-[56px]">
      <div class="absolute inset-0 rounded border border-blue-200 bg-blue-50 px-4 py-2 text-right">
        <slot name="before-note" />
      </div>
      <transition
        enter-active-class="transition-opacity duration-500"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="transition-opacity duration-300"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <div v-if="showNano" class="absolute inset-0 rounded border border-blue-200 bg-blue-50 px-4 py-2 text-right">
          <slot name="after-note" />
        </div>
      </transition>
    </div>
  </div>
</template>
