<template>
  <div class="flex flex-col md:flex-row gap-4 items-center justify-between w-full h-full max-h-[385px]" dir="rtl">
    <!-- Explanations and Steps (Right Side in Hebrew) -->
    <div class="flex-1 flex flex-col gap-2 text-right min-w-[280px]">
      <div class="text-[13.5px] text-slate-600 leading-relaxed mb-1">
        התרגום של ביטוי רגולרי <KatexInline math="E" /> לשפה <KatexInline math="L(E)" /> נעשה מלמטה למעלה (מלמטה אל השורש):
      </div>

      <!-- Step items -->
      <div class="flex flex-col gap-1.5">
        <!-- Step 1 -->
        <div 
          class="p-2 border rounded-lg transition-all duration-300 flex items-start gap-2.5"
          :class="[
            clicks >= 1 
              ? 'bg-blue-50/70 border-blue-200 text-blue-900 shadow-sm' 
              : 'bg-slate-50/50 border-slate-100 text-slate-400'
          ]"
        >
          <div 
            class="w-5 h-5 rounded-full flex items-center justify-center text-[10.5px] font-bold mt-0.5 shrink-0"
            :class="clicks >= 1 ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500'"
          >
            1
          </div>
          <div>
            <div class="font-bold text-[13px]">בסיס האינדוקציה (עלי השלד)</div>
            <div class="text-[11.5px] mt-0.5 leading-snug" :class="clicks >= 1 ? 'text-blue-700' : 'text-slate-400'">
              מתרגמים את אותיות האלפבית לקבוצות בסיס: <KatexInline math="L(a) = \{a\}" />, <KatexInline math="L(b) = \{b\}" />, <KatexInline math="L(c) = \{c\}" />.
            </div>
          </div>
        </div>

        <!-- Step 2 -->
        <div 
          class="p-2 border rounded-lg transition-all duration-300 flex items-start gap-2.5"
          :class="[
            clicks >= 2 
              ? 'bg-blue-50/70 border-blue-200 text-blue-900 shadow-sm' 
              : 'bg-slate-50/50 border-slate-100 text-slate-400'
          ]"
        >
          <div 
            class="w-5 h-5 rounded-full flex items-center justify-center text-[10.5px] font-bold mt-0.5 shrink-0"
            :class="clicks >= 2 ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500'"
          >
            2
          </div>
          <div>
            <div class="font-bold text-[13px]">אופרטור כוכב (Kleene Star)</div>
            <div class="text-[11.5px] mt-0.5 leading-snug" :class="clicks >= 2 ? 'text-blue-700' : 'text-slate-400'">
              מחשבים את סגירת קלין של תת-העץ: <KatexInline math="L(b^*) = (L(b))^* = \{\epsilon, b, bb, bbb, \dots\}" />.
            </div>
          </div>
        </div>

        <!-- Step 3 -->
        <div 
          class="p-2 border rounded-lg transition-all duration-300 flex items-start gap-2.5"
          :class="[
            clicks >= 3 
              ? 'bg-blue-50/70 border-blue-200 text-blue-900 shadow-sm' 
              : 'bg-slate-50/50 border-slate-100 text-slate-400'
          ]"
        >
          <div 
            class="w-5 h-5 rounded-full flex items-center justify-center text-[10.5px] font-bold mt-0.5 shrink-0"
            :class="clicks >= 3 ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500'"
          >
            3
          </div>
          <div>
            <div class="font-bold text-[13px]">אופרטור שרשור (Concatenation)</div>
            <div class="text-[11.5px] mt-0.5 leading-snug" :class="clicks >= 3 ? 'text-blue-700' : 'text-slate-400'">
              משרשרים את השפה של <KatexInline math="L(a)" /> עם השפה של <KatexInline math="L(b^*)" />: <KatexInline math="L(a \cdot b^*) = L(a) \cdot L(b^*) = \{a, ab, abb, \dots\}" />.
            </div>
          </div>
        </div>

        <!-- Step 4 -->
        <div 
          class="p-2 border rounded-lg transition-all duration-300 flex items-start gap-2.5"
          :class="[
            clicks >= 4 
              ? 'bg-blue-50/70 border-blue-200 text-blue-900 shadow-sm' 
              : 'bg-slate-50/50 border-slate-100 text-slate-400'
          ]"
        >
          <div 
            class="w-5 h-5 rounded-full flex items-center justify-center text-[10.5px] font-bold mt-0.5 shrink-0"
            :class="clicks >= 4 ? 'bg-blue-600 text-white' : 'bg-slate-200 text-slate-500'"
          >
            4
          </div>
          <div>
            <div class="font-bold text-[13px]">אופרטור איחוד (Union)</div>
            <div class="text-[11.5px] mt-0.5 leading-snug" :class="clicks >= 4 ? 'text-blue-700' : 'text-slate-400'">
              מבצעים איחוד של שני צידי עץ השורש: <KatexInline math="L(E) = L(a \cdot b^*) \cup L(c) = \{c, a, ab, abb, \dots\}" />.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Parse Tree Visual (Left Side) -->
    <div class="flex-1 flex justify-center items-center bg-slate-50/30 border border-slate-100 rounded-xl p-3 min-w-[320px] relative">
      <!-- Title / Formula Badge -->
      <div class="absolute top-2 right-2 bg-slate-100 text-slate-700 text-xs font-semibold px-2 py-0.5 rounded border border-slate-200" dir="ltr">
        <KatexInline math="E = a \cdot b^* + c" />
      </div>

      <svg viewBox="0 0 500 425" class="w-full h-auto max-h-[295px]">
        <g transform="translate(0, 80)">
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
            <foreignObject x="228" y="28" width="44" height="44">
              <div class="flex items-center justify-center w-full h-full text-[16px] font-bold select-none" :style="{ color: clicks >= 4 ? '#e11d48' : '#475569' }">
                <KatexInline math="+" />
              </div>
            </foreignObject>
            <!-- Set Value label -->
            <g v-if="clicks >= 4" class="animate-fade-in">
              <foreignObject x="282" y="30" width="210" height="40">
                <div class="bg-rose-600/95 text-white text-[11px] font-bold px-2 py-1 rounded shadow border border-rose-500/30 flex items-center justify-center w-full h-full" dir="ltr">
                  <KatexInline math="L(E) = \{c, a, ab, abb, \dots\}" />
                </div>
              </foreignObject>
            </g>
          </g>

          <!-- Concat node (·) -->
          <g class="transition-all duration-500 transform origin-[150px_130px]" :class="{ 'scale-110': clicks >= 3 }">
            <circle cx="150" cy="130" r="20" 
                    :fill="clicks >= 3 ? '#dbeafe' : '#f8fafc'" 
                    :stroke="clicks >= 3 ? '#2563eb' : '#64748b'" 
                    stroke-width="2.5" />
            <foreignObject x="130" y="110" width="40" height="40">
              <div class="flex items-center justify-center w-full h-full text-[16px] font-bold select-none" :style="{ color: clicks >= 3 ? '#2563eb' : '#475569' }">
                <KatexInline math="\cdot" />
              </div>
            </foreignObject>
            <!-- Set Value label -->
            <g v-if="clicks >= 3" class="animate-fade-in">
              <foreignObject x="-20" y="110" width="165" height="40">
                <div class="bg-blue-600/95 text-white text-[11px] font-bold px-2 py-1 rounded shadow border border-blue-500/30 flex items-center justify-center w-full h-full" dir="ltr">
                  <KatexInline math="L(a \cdot b^*) = \{a, ab, \dots\}" />
                </div>
              </foreignObject>
            </g>
          </g>

          <!-- Node c -->
          <g class="transition-all duration-500 transform origin-[350px_130px]" :class="{ 'scale-110': clicks >= 1 }">
            <circle cx="350" cy="130" r="20" 
                    :fill="clicks >= 1 ? '#dcfce7' : '#f8fafc'" 
                    :stroke="clicks >= 1 ? '#16a34a' : '#64748b'" 
                    stroke-width="2.5" />
            <foreignObject x="330" y="110" width="40" height="40">
              <div class="flex items-center justify-center w-full h-full text-[14px] font-bold select-none" :style="{ color: clicks >= 1 ? '#16a34a' : '#475569' }">
                <KatexInline math="c" />
              </div>
            </foreignObject>
            <!-- Set Value label -->
            <g v-if="clicks >= 1" class="animate-fade-in">
              <foreignObject x="375" y="115" width="105" height="35">
                <div class="bg-emerald-600/95 text-white text-[11px] font-bold px-2 py-1 rounded shadow border border-emerald-500/30 flex items-center justify-center w-full h-full" dir="ltr">
                  <KatexInline math="L(c) = \{c\}" />
                </div>
              </foreignObject>
            </g>
          </g>

          <!-- Node a -->
          <g class="transition-all duration-500 transform origin-[80px_210px]" :class="{ 'scale-110': clicks >= 1 }">
            <circle cx="80" cy="210" r="20" 
                    :fill="clicks >= 1 ? '#dcfce7' : '#f8fafc'" 
                    :stroke="clicks >= 1 ? '#16a34a' : '#64748b'" 
                    stroke-width="2.5" />
            <foreignObject x="60" y="190" width="40" height="40">
              <div class="flex items-center justify-center w-full h-full text-[14px] font-bold select-none" :style="{ color: clicks >= 1 ? '#16a34a' : '#475569' }">
                <KatexInline math="a" />
              </div>
            </foreignObject>
            <!-- Set Value label -->
            <g v-if="clicks >= 1" class="animate-fade-in">
              <foreignObject x="0" y="228" width="105" height="35">
                <div class="bg-emerald-600/95 text-white text-[11px] font-bold px-2 py-1 rounded shadow border border-emerald-500/30 flex items-center justify-center w-full h-full" dir="ltr">
                  <KatexInline math="L(a) = \{a\}" />
                </div>
              </foreignObject>
            </g>
          </g>

          <!-- Star node (*) -->
          <g class="transition-all duration-500 transform origin-[220px_210px]" :class="{ 'scale-110': clicks >= 2 }">
            <circle cx="220" cy="210" r="20" 
                    :fill="clicks >= 2 ? '#f3e8ff' : '#f8fafc'" 
                    :stroke="clicks >= 2 ? '#7c3aed' : '#64748b'" 
                    stroke-width="2.5" />
            <foreignObject x="200" y="190" width="40" height="40">
              <div class="flex items-center justify-center w-full h-full text-[16px] font-bold select-none" :style="{ color: clicks >= 2 ? '#7c3aed' : '#475569' }">
                <KatexInline math="*" />
              </div>
            </foreignObject>
            <!-- Set Value label -->
            <g v-if="clicks >= 2" class="animate-fade-in">
              <foreignObject x="245" y="193" width="160" height="38">
                <div class="bg-purple-600/95 text-white text-[11px] font-bold px-2 py-1 rounded shadow border border-purple-500/30 flex items-center justify-center w-full h-full" dir="ltr">
                  <KatexInline math="L(b^*) = \{\epsilon, b, bb, \dots\}" />
                </div>
              </foreignObject>
            </g>
          </g>

          <!-- Node b -->
          <g class="transition-all duration-500 transform origin-[220px_290px]" :class="{ 'scale-110': clicks >= 1 }">
            <circle cx="220" cy="290" r="20" 
                    :fill="clicks >= 1 ? '#dcfce7' : '#f8fafc'" 
                    :stroke="clicks >= 1 ? '#16a34a' : '#64748b'" 
                    stroke-width="2.5" />
            <foreignObject x="200" y="270" width="40" height="40">
              <div class="flex items-center justify-center w-full h-full text-[14px] font-bold select-none" :style="{ color: clicks >= 1 ? '#16a34a' : '#475569' }">
                <KatexInline math="b" />
              </div>
            </foreignObject>
            <!-- Set Value label -->
            <g v-if="clicks >= 1" class="animate-fade-in">
              <foreignObject x="245" y="274" width="105" height="35">
                <div class="bg-emerald-600/95 text-white text-[11px] font-bold px-2 py-1 rounded shadow border border-emerald-500/30 flex items-center justify-center w-full h-full" dir="ltr">
                  <KatexInline math="L(b) = \{b\}" />
                </div>
              </foreignObject>
            </g>
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
