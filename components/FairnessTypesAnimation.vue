<template>
  <div class="fairness-animation border border-slate-200/80 rounded-2xl bg-white/95 p-5 shadow-xl text-right font-sans my-4" dir="rtl">
    <!-- Header -->
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 mb-4 border-b border-slate-100 pb-3">
      <div>
        <h3 class="text-base font-bold text-slate-800">הדמיה אינטראקטיבית: אילוצי הוגנות והרעבה</h3>
        <p class="text-xs text-slate-500 mt-1">אנימציה מחזורית המדגימה שיבוצים שונים. ניתן ללחוץ ידנית כדי להקפיא.</p>
      </div>
      <!-- Mode selectors and autoplay -->
      <div class="flex items-center gap-3 flex-wrap">
        <label class="flex items-center gap-1.5 cursor-pointer select-none text-slate-500 hover:text-slate-700 transition-colors">
          <input type="checkbox" v-model="isAutoplay" class="rounded border-slate-300 text-indigo-600 focus:ring-indigo-500 w-3.5 h-3.5" />
          <span class="text-[11px] font-medium">ניגון מחזורי (כמו GIF)</span>
        </label>
        <div class="flex gap-1">
          <button 
            v-for="mode in modes" 
            :key="mode.id"
            @click="selectModeManually(mode.id)"
            type="button"
            class="px-2.5 py-1 rounded-full text-xs font-bold transition-all duration-200"
            :class="currentMode === mode.id ? 'bg-indigo-600 text-white shadow-sm font-semibold' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
          >
            {{ mode.name }}
          </button>
        </div>
      </div>
    </div>

    <!-- Description -->
    <div class="text-xs bg-slate-50 border border-slate-100 rounded-lg p-3 mb-4 text-slate-700 leading-relaxed">
      <strong>תיאור השיבוץ:</strong> {{ currentModeDescription }}
    </div>

    <!-- Timeline Grid -->
    <div class="space-y-4">
      <div v-for="actor in actors" :key="actor.id" class="bg-white border border-slate-100 rounded-xl p-3 shadow-sm hover:shadow transition-shadow duration-200">
        <!-- Actor Info -->
        <div class="flex justify-between items-baseline mb-2.5">
          <span class="font-bold text-xs" :class="actor.colorClass">{{ actor.name }}</span>
          <span class="text-[10px] text-slate-500">{{ actor.constraintText }}</span>
        </div>

        <!-- Time Steps Grid -->
        <div class="grid grid-cols-11 gap-1 text-center font-mono select-none">
          <!-- Step Labels -->
          <div class="col-span-1 text-[10px] font-bold text-slate-400 self-center text-right">שלב (t):</div>
          <div v-for="t in 10" :key="t" class="text-[10px] font-bold text-slate-400 flex items-center justify-center">{{ t - 1 }}</div>

          <!-- Enabled Row -->
          <div class="col-span-1 text-[10px] text-slate-500 self-center text-right">בקשה:</div>
          <div v-for="t in 10" :key="t" class="flex justify-center items-center h-7">
            <span v-if="isEnabled(actor.id, t - 1)" class="text-sm transform transition-all duration-300 hover:scale-125" title="מבקש שירות (Enabled)">🙋</span>
            <span v-else class="text-xs text-slate-300" title="לא מבקש (Disabled)">🙅</span>
          </div>

          <!-- Taken Row -->
          <div class="col-span-1 text-[10px] text-slate-500 self-center text-right">שירות:</div>
          <div v-for="t in 10" :key="t" class="flex justify-center items-center h-7">
            <span v-if="isTaken(actor.id, t - 1)" class="w-4.5 h-4.5 rounded-full bg-emerald-500 text-white text-[9px] flex items-center justify-center font-bold shadow-sm" title="קיבל שירות (Taken)">✓</span>
            <span v-else class="w-1.5 h-1.5 rounded-full bg-slate-200"></span>
          </div>
        </div>
        
        <!-- Status Message -->
        <div class="mt-2.5 text-[10.5px] flex items-center gap-1.5 border-t border-slate-50 pt-2" :class="actorStatus(actor.id).colorClass">
          <span class="text-xs">{{ actorStatus(actor.id).icon }}</span>
          <span class="font-medium">{{ actorStatus(actor.id).text }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

const currentMode = ref<'unfair' | 'weak_fair' | 'strong_fair'>('unfair')
const isAutoplay = ref(true)
let intervalId: any = null

const modes = [
  { id: 'unfair', name: 'שיבוץ לא הוגן' },
  { id: 'weak_fair', name: 'שיבוץ הוגן חלש' },
  { id: 'strong_fair', name: 'שיבוץ הוגן חזק' }
] as const

function cycleMode() {
  if (currentMode.value === 'unfair') currentMode.value = 'weak_fair'
  else if (currentMode.value === 'weak_fair') currentMode.value = 'strong_fair'
  else currentMode.value = 'unfair'
}

function selectModeManually(modeId: 'unfair' | 'weak_fair' | 'strong_fair') {
  currentMode.value = modeId
  isAutoplay.value = false // Pause autoplay when manually clicked
}

onMounted(() => {
  intervalId = setInterval(() => {
    if (isAutoplay.value) {
      cycleMode()
    }
  }, 4500) // Cycle every 4.5 seconds
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})

const currentModeDescription = computed(() => {
  if (currentMode.value === 'unfair') {
    return 'המשבץ מתעלם מכל הבקשות. דמות א\' (שמבקשת תמיד) לא מקבלת שירות לעולם. דמויות ב\' וג\' מבקשות לסירוגין או ברצף אך אינן מקבלות מענה. זהו שיבוץ שאינו מקיים אף תנאי הוגנות.'
  } else if (currentMode.value === 'weak_fair') {
    return 'המשבץ נותן מענה לדמות ג\' (שמבקשת ברצף מ-t=3) בשלבים 5 ו-9. דמות א\' מקבלת מענה ב-t=2. אך דמות ב\' שמבקשת לסירוגין (לא ברצף) לא נבחרת לעולם! זהו שיבוץ הוגן חלש, אך הוא אינו הוגן חזק (דמות ב\' מורעבת!).'
  } else {
    return 'המשבץ משרת את כולם: דמות א\' מקבלת שירות ב-t=1; דמות ב\' (המבקשת לסירוגין) מלווה בשירות ב-t=3,7; ודמות ג\' (המבקשת ברצף) מקבלת שירות ב-t=5,9. כל אילוצי ההוגנות מתקיימים.'
  }
})

const actors = [
  {
    id: 'uncond',
    name: 'דמות א\' (בלתי מותנית)',
    constraintText: 'דרישה: חייבת להיבחר אינסוף פעמים ללא תלות בבקשה',
    colorClass: 'text-blue-700 bg-blue-50 px-2 py-0.5 rounded'
  },
  {
    id: 'strong',
    name: 'דמות ב\' (בקשה לסירוגין)',
    constraintText: 'דרישה: אם מבקשת אינסוף פעמים (גם לסירוגין), חייבת לקבל שירות',
    colorClass: 'text-amber-700 bg-amber-50 px-2 py-0.5 rounded'
  },
  {
    id: 'weak',
    name: 'דמות ג\' (בקשה רציפה)',
    constraintText: 'דרישה: אם מבקשת ברצף מנקודה מסוימת, חייבת לקבל שירות',
    colorClass: 'text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded'
  }
] as const

function isEnabled(actorId: string, t: number): boolean {
  if (actorId === 'uncond') return true
  if (actorId === 'strong') return t % 2 === 1 // 1, 3, 5, 7, 9 (infinitely often but not continuously)
  if (actorId === 'weak') return t >= 3 // continuously from t=3 onwards
  return false
}

function isTaken(actorId: string, t: number): boolean {
  if (currentMode.value === 'unfair') {
    return false
  }
  
  if (currentMode.value === 'weak_fair') {
    if (actorId === 'uncond' && t === 2) return true
    if (actorId === 'weak' && (t === 5 || t === 9)) return true
    return false
  }

  if (currentMode.value === 'strong_fair') {
    if (actorId === 'uncond' && t === 1) return true
    if (actorId === 'strong' && (t === 3 || t === 7)) return true
    if (actorId === 'weak' && (t === 5 || t === 9)) return true
    return false
  }

  return false
}

interface ActorStatus {
  text: string
  icon: string
  colorClass: string
}

function actorStatus(actorId: string): ActorStatus {
  if (currentMode.value === 'unfair') {
    return {
      text: 'לא הוגן! מורעב לנצח (מפר את הדרישה).',
      icon: '❌',
      colorClass: 'text-red-600 bg-red-50/50 rounded px-2'
    }
  }

  if (currentMode.value === 'weak_fair') {
    if (actorId === 'uncond') {
      return {
        text: 'הוגן בלתי מותנה (קיבל שירות).',
        icon: '✅',
        colorClass: 'text-emerald-700 bg-emerald-50/50 rounded px-2'
      }
    }
    if (actorId === 'weak') {
      return {
        text: 'הוגן חלש! הבקשה הרציפה נענתה.',
        icon: '✅',
        colorClass: 'text-emerald-700 bg-emerald-50/50 rounded px-2'
      }
    }
    // actorId === 'strong'
    return {
      text: 'לא הוגן חזק! בקשה לסירוגין מורעבת לנצח (מפר אילוץ הוגנות חזקה).',
      icon: '❌',
      colorClass: 'text-red-600 bg-red-50/50 rounded px-2'
    }
  }

  // strong_fair
  return {
    text: 'הוגן! הדרישה התקבלה במלואה.',
    icon: '✅',
    colorClass: 'text-emerald-700 bg-emerald-50/50 rounded px-2'
  }
}
</script>

<style scoped>
.fairness-animation {
  user-select: none;
}
</style>
