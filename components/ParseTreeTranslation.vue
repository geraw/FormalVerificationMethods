<template>
  <div class="flex flex-col md:flex-row gap-6 items-center justify-between w-full h-full max-h-[460px]" dir="rtl">
    <!-- Explanations and Steps (Right Side in Hebrew) -->
    <div class="flex-1 flex flex-col gap-4 text-right min-w-[280px]">
      <div class="text-[20px] font-bold text-slate-800">
        תרגום אינדוקטיבי מביטוי לשפה
      </div>
      
      <div class="text-[16px] text-slate-600 leading-relaxed">
        התרגום של ביטוי רגולרי $E$ לשפה $L(E)$ נעשה מלמטה למעלה (מלמטה אל השורש):
      </div>

      <!-- Step items -->
      <div class="flex flex-col gap-2.5">
        <div 
          v-for="(step, idx) in steps" 
          :key="idx"
          class="p-2.5 border rounded-lg transition-all duration-300 flex items-start gap-3"
          :class="[
            clicks >= idx + 1 
              ? 'bg-blue-50/70 border-blue-200 text-blue-900 shadow-sm' 
              : 'bg-slate-50/50 border-slate-100 text-slate-400'
          ]"
        >
          <div 
            class="w-6 h-6 rounded-full flex items-center justify-center text-[12px] font-bold mt-0.5 shrink-0"
            :class="clicks >= idx + 1 ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500'"
          >
            {{ idx + 1 }}
          </div>
          <div>
            <div class="font-bold text-[15px]">{{ step.title }}</div>
            <div class="text-[13px] mt-0.5 leading-snug" :class="clicks >= idx + 1 ? 'text-blue-700' : 'text-slate-400'">
              {{ step.desc }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Parse Tree Visual (Left Side) -->
    <div class="flex-1 flex justify-center items-center bg-slate-50/30 border border-slate-100 rounded-xl p-4 min-w-[320px] relative">
      <!-- Title / Formula Badge -->
      <div class="absolute top-3 right-3 bg-slate-100 text-slate-700 text-xs font-semibold px-2 py-0.5 rounded border border-slate-200" dir="ltr">
        E = a · b* + c
      </div>

      <svg viewBox="0 0 500 360" class="w-full h-auto max-h-[340px]">
        <!-- Edges (Paths) -->
        <g stroke-linecap="round">
          <!-- Root to Concat -->
          <line x1="250" y1="50" x2="150" y2="130" 
                :stroke="clicks >= 4 ? '#e11d48' : (clicks >= 3 ? '#3b82f6' : '#cbd5e1')" 
                :stroke-width="clicks >= 3 ? '4' : '2.5'" class="transition-all duration-500" />
          <!-- Root to C -->
          <line x1="250" y1="50" x2="350" y2="130" 
                :stroke="clicks >= 4 ? '#e11d48' : '#cbd5e1'" 
                :stroke-width="clicks >= 4 ? '4' : '2.5'" class="transition-all duration-500" />
          <!-- Concat to A -->
          <line x1="150" y1="130" x2="80" y2="210" 
                :stroke="clicks >= 3 ? '#3b82f6' : '#cbd5e1'" 
                :stroke-width="clicks >= 3 ? '4' : '2.5'" class="transition-all duration-500" />
          <!-- Concat to Star -->
          <line x1="150" y1="130" x2="220" y2="210" 
                :stroke="clicks >= 3 ? '#3b82f6' : '#cbd5e1'" 
                :stroke-width="clicks >= 3 ? '4' : '2.5'" class="transition-all duration-500" />
          <!-- Star to B -->
          <line x1="220" y1="210" x2="220" y2="290" 
                :stroke="clicks >= 2 ? '#8b5cf6' : '#cbd5e1'" 
                :stroke-width="clicks >= 2 ? '4' : '2.5'" class="transition-all duration-500" />
        </g>

        <!-- Nodes -->
        <!-- Root node (+) -->
        <g class="transition-all duration-500 transform origin-[250px_50px]" :class="{ 'scale-110': clicks >= 4 }">
          <circle cx="250" cy="50" r="22" 
                  :fill="clicks >= 4 ? '#ffe4e6' : '#f8fafc'" 
                  :stroke="clicks >= 4 ? '#e11d48' : '#64748b'" 
                  stroke-width="3" />
          <text x="250" y="56" text-anchor="middle" font-weight="bold" font-size="20" :fill="clicks >= 4 ? '#e11d48' : '#475569'">+</text>
          <!-- Set Value label -->
          <g v-if="clicks >= 4" class="animate-fade-in">
            <rect x="282" y="32" width="180" height="34" rx="4" fill="#e11d48" opacity="0.9" />
            <text x="292" y="53" fill="white" font-weight="bold" font-size="13" font-family="monospace">L(E) = {c, a, ab, abb, ...}</text>
          </g>
        </g>

        <!-- Concat node (·) -->
        <g class="transition-all duration-500 transform origin-[150px_130px]" :class="{ 'scale-110': clicks >= 3 }">
          <circle cx="150" cy="130" r="20" 
                  :fill="clicks >= 3 ? '#dbeafe' : '#f8fafc'" 
                  :stroke="clicks >= 3 ? '#2563eb' : '#64748b'" 
                  stroke-width="2.5" />
          <text x="150" y="136" text-anchor="middle" font-weight="bold" font-size="20" :fill="clicks >= 3 ? '#2563eb' : '#475569'">·</text>
          <!-- Set Value label -->
          <g v-if="clicks >= 3" class="animate-fade-in">
            <rect x="5" y="112" width="115" height="30" rx="4" fill="#2563eb" opacity="0.9" />
            <text x="12" y="131" fill="white" font-size="12" font-family="monospace">L(a·b*) = {a, ab, ...}</text>
          </g>
        </g>

        <!-- Node c -->
        <g class="transition-all duration-500 transform origin-[350px_130px]" :class="{ 'scale-110': clicks >= 1 }">
          <circle cx="350" cy="130" r="20" 
                  :fill="clicks >= 1 ? '#dcfce7' : '#f8fafc'" 
                  :stroke="clicks >= 1 ? '#16a34a' : '#64748b'" 
                  stroke-width="2.5" />
          <text x="350" y="136" text-anchor="middle" font-weight="bold" font-size="16" :fill="clicks >= 1 ? '#16a34a' : '#475569'">c</text>
          <!-- Set Value label -->
          <g v-if="clicks >= 1" class="animate-fade-in">
            <rect x="380" y="115" width="85" height="26" rx="4" fill="#16a34a" opacity="0.9" />
            <text x="388" y="132" fill="white" font-size="12" font-family="monospace">L(c) = {c}</text>
          </g>
        </g>

        <!-- Node a -->
        <g class="transition-all duration-500 transform origin-[80px_210px]" :class="{ 'scale-110': clicks >= 1 }">
          <circle cx="80" cy="210" r="20" 
                  :fill="clicks >= 1 ? '#dcfce7' : '#f8fafc'" 
                  :stroke="clicks >= 1 ? '#16a34a' : '#64748b'" 
                  stroke-width="2.5" />
          <text x="80" y="216" text-anchor="middle" font-weight="bold" font-size="16" :fill="clicks >= 1 ? '#16a34a' : '#475569'">a</text>
          <!-- Set Value label -->
          <g v-if="clicks >= 1" class="animate-fade-in">
            <rect x="5" y="228" width="85" height="26" rx="4" fill="#16a34a" opacity="0.9" />
            <text x="13" y="245" fill="white" font-size="12" font-family="monospace">L(a) = {a}</text>
          </g>
        </g>

        <!-- Star node (*) -->
        <g class="transition-all duration-500 transform origin-[220px_210px]" :class="{ 'scale-110': clicks >= 2 }">
          <circle cx="220" cy="210" r="20" 
                  :fill="clicks >= 2 ? '#f3e8ff' : '#f8fafc'" 
                  :stroke="clicks >= 2 ? '#7c3aed' : '#64748b'" 
                  stroke-width="2.5" />
          <text x="220" y="218" text-anchor="middle" font-weight="bold" font-size="22" :fill="clicks >= 2 ? '#7c3aed' : '#475569'">*</text>
          <!-- Set Value label -->
          <g v-if="clicks >= 2" class="animate-fade-in">
            <rect x="250" y="196" width="130" height="30" rx="4" fill="#7c3aed" opacity="0.9" />
            <text x="258" y="215" fill="white" font-size="11" font-family="monospace">L(b*) = {ε, b, bb, ...}</text>
          </g>
        </g>

        <!-- Node b -->
        <g class="transition-all duration-500 transform origin-[220px_290px]" :class="{ 'scale-110': clicks >= 1 }">
          <circle cx="220" cy="290" r="20" 
                  :fill="clicks >= 1 ? '#dcfce7' : '#f8fafc'" 
                  :stroke="clicks >= 1 ? '#16a34a' : '#64748b'" 
                  stroke-width="2.5" />
          <text x="220" y="296" text-anchor="middle" font-weight="bold" font-size="16" :fill="clicks >= 1 ? '#16a34a' : '#475569'">b</text>
          <!-- Set Value label -->
          <g v-if="clicks >= 1" class="animate-fade-in">
            <rect x="250" y="277" width="85" height="26" rx="4" fill="#16a34a" opacity="0.9" />
            <text x="258" y="294" fill="white" font-size="12" font-family="monospace">L(b) = {b}</text>
          </g>
        </g>
      </svg>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  clicks: {
    type: Number,
    default: 0
  }
});

const steps = [
  {
    title: "בסיס האינדוקציה (עלי השלד)",
    desc: "מתרגמים את אותיות האלפבית לקבוצות בסיס: L(a) = {a}, L(b) = {b}, L(c) = {c}."
  },
  {
    title: "אופרטור כוכב (Kleene Star)",
    desc: "מחשבים את סגירת קלין של תת-העץ: L(b*) = {ε, b, bb, bbb, ...}."
  },
  {
    title: "אופרטור שרשור (Concatenation)",
    desc: "משרשרים את השפה של L(a) עם השפה של L(b*): L(a·b*) = {a, ab, abb, ...}."
  },
  {
    title: "אופרטור איחוד (Union)",
    desc: "מבצעים איחוד של שני צידי עץ השורש (+): L(E) = L(a·b*) ∪ L(c) = {c, a, ab, ...}."
  }
];
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.4s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
