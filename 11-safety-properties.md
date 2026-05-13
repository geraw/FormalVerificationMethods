---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 11-safety-properties
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## תכונות בטיחות
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תכונות בטיחות

## הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

---

# מה מעבר לשמורות?

<div class="mt-8 text-right">

בהרצאה הקודמת הכרנו את ה**שמורות** (Invariants) כתכונות שתלויות רק ב*מצב הנוכחי* של המערכת. 

אך קיימות דרישות טבעיות למערכות שהן יותר מורכבות, ועדיין נחשבות לתכונות בטיחות:

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-6">
<div class="font-bold mb-2">דוגמה 1: כספומט (ATM)</div>

הדרישה: "ניתן למשוך כסף רק אם קודם לכן הוקלד קוד סודי (PIN) נכון".
זו אינה שמורה, כי המצב שבו יוצא כסף אינו "רע" בפני עצמו - הוא תלוי במה שקרה קודם. 
עם זאת, זו עדיין תכונת בטיחות: אם משכנו כסף בלי קוד, עשינו מעשה רע **בזמן סופי**.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-4">
<div class="font-bold mb-2">דוגמה 2: מכונת שתייה</div>
הדרישה: "מספר המטבעות שהוכנסו תמיד גדול או שווה למספר המשקאות שסופקו".
גם כאן, כדי לדעת אם מצב תקין, יש לספור את ההיסטוריה עד כה.
</div>

</div>

---

# תכונה של מצב / תכונה של ריצה

<div class="mt-6 text-right">

הפסוקים האטומיים והפונקציה $L$ המתאימה אותם למצבים מאפשרים לנו לדבר על **תכונות של מצבים**.

<div class="grid grid-cols-[1fr_1.1fr] gap-6 mt-6 items-center">

<div class="bg-slate-50 border border-slate-200 rounded p-4 text-[15px]">
<div class="font-bold mb-3">למשל:</div>

- "תהליך 1 נמצא בקטע הקריטי"

- "המצב $s$ מקיים את הפסוק $p \lor q$"  <br/> (מסומן ב-$s \models p \lor q$).   

</div>

<div class="text-[15px]">

אבל בתכונות בטיחות רבות אנו מתעניינים גם ב**תכונות של ריצות**:

<div class="mt-4 text-red-600 font-bold text-[16px] leading-snug">
"הרמזור לא יישאר אדום למשך יותר משלושה צעדים רצופים"
</div>

<div class="-mt-25 -mb-6 scale-80" dir="ltr">

<TransitionSystemD3 :width="430" :height="240" :auto="false"
  :states="[
    { id: 'green',  text: ' ', label: '$\\{\\}$', initial: true, x: 55, y: 118, width: 50, color: '#ffffff', stroke: '#111827' },
    { id: 'yellow', text: ' ', label: '$\\{\\}$', x: 150, y: 118, width: 50, color: '#ffffff', stroke: '#111827' },
    { id: 'red1',   text: ' ', label: '$\\{red\\}$', x: 245, y: 118, width: 52, color: '#fee2e2', stroke: '#dc2626' },
    { id: 'red2',   text: ' ', label: '$\\{red\\}$', x: 340, y: 118, width: 52, color: '#fee2e2', stroke: '#dc2626' },
    { id: 'red3',   text: ' ', label: '$\\{red\\}$', x: 340, y: 205, width: 52, color: '#fee2e2', stroke: '#dc2626' },
    { id: 'bad',    text: ' ', label: '$\\{red\\}$', x: 245, y: 205, width: 52, color: '#fecaca', stroke: '#b91c1c', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 'green', target: 'yellow' },
    { source: 'yellow', target: 'red1' },
    { source: 'red1', target: 'red2', stroke: '#dc2626' },
    { source: 'red2', target: 'red3', stroke: '#dc2626' },
    { source: 'red3', target: 'bad', stroke: '#dc2626', strokeWidth: 3 },
    // { source: 'bad', target: 'green', curve: 0.35, stroke: '#dc2626', strokeWidth: 3 },
    // { source: 'red2', target: 'green', curve: 0.35 },
    // { source: 'red3', target: 'green', curve: 0.45 }
  ]"
/>

</div>

</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-[18px] font-bold">
לא מספיק לבדוק מצבים לחוד כפי שבדקנו תכונות שמורה; צריך להסתכל על רישות סופיות של ריצות.
</div>

</div>

---

# תכונות בטיחות ורישות רעות

<div class="mt-8 text-right">

תכונת בטיחות כללית מוגדרת על ידי העובדה ש**כל הפרה שלה ניתן לזהות על ידי רצף סופי**.

<div class="bg-blue-50 border border-blue-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">הגדרה: תכונת בטיחות ורֵישָׁא רעה</div>

תכונת זמן לינארי $P$ מעל $AP$ נקראת **תכונת בטיחות** (Safety Property) אם לכל מילה אינסופית $\sigma \in (2^{AP})^\omega \setminus P$ שמפרה את התכונה, קיימת **רֵישָׁא סופית** (prefix) $\rho \prec \sigma$ כך ש:
$$ P \cap \{ \sigma' \in (2^{AP})^\omega \mid \rho \prec \sigma' \} = \emptyset $$
</div>

- רֵישָׁא סופית כזו $\rho$ נקראת **רֵישָׁא רעה** (Bad Prefix). ברגע שהיא מתרחשת, לא משנה מה יקרה בעתיד, העקבה כולה לעולם לא תקיים את התכונה.

- אוסף כל הרישות הרעות של תכונה מסומן ב-**$\operatorname{BadPref}(P)$**.

<div class="mt-4 text-sm font-bold text-blue-700">
כל שמורה (Invariant) היא מקרה פרטי של תכונת בטיחות! הָרֵישָׁא הרעה שלה מסתיימת במצב שמפר את תנאי השמורה.
</div>

</div>

---

# ניסוח שקול

<div class="mt-6 text-right text-[24px] leading-relaxed">

תכונת זמן לינארי $P \subseteq (2^{AP})^\omega$ היא <span class="text-red-600 font-bold">תכונת בטיחות</span> אם ורק אם:

</div>

<div class="mx-auto mt-6 w-4/5 bg-white border border-slate-200 rounded shadow-md p-5 text-[22px] leading-relaxed text-right">

לכל מילה שלא מקיימת את התכונה, $\sigma \notin P$, קיים $i \ge -1$ כך ש־

<div class="mt-4 text-center" dir="ltr">

$\sigma'[..i] = \sigma[..i] \;\Rightarrow\; \sigma' \notin P$

</div>

</div>

<div class="relative mx-auto mt-3 w-[40%]">
  <img src="/safety_equivalent_branching.png" class="w-full" />
  <svg class="absolute left-[47%] bottom-[2%] w-[12%] h-[30%] overflow-visible" viewBox="0 0 60 150" aria-hidden="true">
    <defs>
      <marker id="sigma-prefix-arrow" markerWidth="9" markerHeight="9" refX="4.5" refY="4.5" orient="auto">
        <path d="M 0 0 L 9 4.5 L 0 9 z" fill="#1e04e3" />
      </marker>
    </defs>
    <line x1="440" y1="10" x2="60" y2="15" stroke="#1e04e3" stroke-width="6" marker-end="url(#sigma-prefix-arrow)" />
  </svg>
  <div class="absolute bottom-[18%] -right-[35%] text-blue-800 text-[22px] font-bold" dir="ltr">

  $\sigma[..i]$
  </div>
</div>


---

# דוגמאות

<div class="mt-4 text-right text-[24px]">
מי מהבאות הן תכונות בטיחות? הוכיחו טענותיכם.
</div>

<div class="grid grid-cols-2 gap-6 mt-6 text-[23px]">
  <div class="bg-green-50 text-green-800 border border-green-100 rounded p-3 text-center">
    איך נוכיח שתכונה היא תכונת בטיחות?
  </div>
  <div class="bg-red-50 text-red-800 border border-red-100 rounded p-3 text-center">
    איך נוכיח שתכונה אינה תכונת בטיחות?
  </div>
</div>

<div class="mt-10 text-left text-[22px] leading-[4.2]" dir="ltr">

$P_1 = \{\sigma \in (2^{AP})^\omega \mid \forall i \geq 0 ( \sigma[i] \models p \to (q \lor \neg r))\}$
<br/><br/>

$P_2 = \{\sigma \in (2^{AP})^\omega \mid \forall i \geq 0(p \in \sigma[0] \to p \in \sigma[i])\}$
<br/><br/>

$P_3 = \{\sigma \in (2^{AP})^\omega \mid \forall i \geq 0(p \in \sigma[2i] \to p \in \sigma[i])\}$
<br/><br/>

$P_4 = \{\sigma \in (2^{AP})^\omega \mid \exists i \geq 0 (p \in \sigma[i])\}$

</div>

---

# איך מוכיחים שתכונה היא תכונת בטיחות?

<div class="grid grid-cols-[0.95fr_1.05fr] gap-6 mt-6 items-center">

<div class="text-right text-[20px] leading-relaxed">

תכונה היא <span class="text-red-600 font-bold">תכונת בטיחות</span> אם כל הפרה שלה משאירה אחריה
<span class="text-blue-700 font-bold">רישא רעה סופית</span>.

<div class="mt-6 bg-red-50 border border-red-200 rounded p-4 text-[18px] leading-relaxed">

אם עקבה אינסופית $\sigma$ אינה מקיימת את $P$, אז יש לה רֵישָׁא סופית $\rho$ כך שכל המשך של $\rho$ עדיין מפר את $P$.
</div>

<div class="mt-5 text-[18px]">

כלומר: ברגע שהגענו ל־$\rho$, כבר מאוחר מדי לתקן.
</div>

</div>

<div class="mx-auto w-[95%]">
<div class="mx-auto w-[98%] relative">
  <img src="/safety_property_basketball.png" class="w-full rounded-xl shadow-2xl border border-slate-800" />
  
  <!-- Opponent label -->
  <div class="absolute top-[1%] -left-[10%] w-[35%] bg-gradient-to-r from-amber-900/90 to-amber-800/80 text-white p-3 rounded-lg text-[16px] font-bold shadow-lg flex items-center gap-3 backdrop-blur-sm border border-amber-700/50">
    <div class="shrink-0 w-0 h-0 border-y-[12px] border-y-transparent border-r-[18px] border-r-amber-400"></div>
    <span class="leading-tight text-right">יריב המנסה להראות שההוכחה אינה נכונה</span>
  </div>

  <!-- Mathematician label -->
  <div class="absolute top-[1%] -right-[10%] w-[35%] bg-gradient-to-l from-amber-900/90 to-amber-800/80 text-white p-3 rounded-lg text-[16px] font-bold shadow-lg flex items-center justify-end gap-3 backdrop-blur-sm border border-amber-700/50 text-right">
    <div class="leading-tight">
    מתמטיקאי המנסה להוכיח ש-P היא תכונת בטיחות
    </div>
    <div class="shrink-0 w-0 h-0 border-y-[12px] border-y-transparent border-l-[18px] border-l-amber-400"></div>
  </div>

  <!-- Success condition label -->
  <div class="absolute bottom-[-2%] -left-[8%] w-[44%] bg-gradient-to-r from-emerald-900/90 to-emerald-800/80 text-white p-3 rounded-lg text-[16px] font-bold shadow-lg flex items-center gap-3 backdrop-blur-sm border border-emerald-700/50">
    <div class="shrink-0 w-0 h-0 border-y-[12px] border-y-transparent border-r-[18px] border-r-emerald-400"></div>
    <div class="leading-tight" dir="rtl">

ההוכחה נכונה אם   היריב לא יכול למצוא כזאת $\sigma'$
  </div>
  </div>
</div>

</div>

</div>

---

# דוגמה: הוכחת בטיחות


<div class="mt-6 text-right text-[18px]">

**טענה:** התכונה הבאה היא תכונת בטיחות:

<div class="mt-3 text-center" dir="ltr">

$P = \{\sigma \in (2^{AP})^\omega :  \forall i \geq 0 ((p \in \sigma[2i]) \to (p \in \sigma[i]))\}$
</div>

<div class="-mt-0">
<span class="font-bold underline">הוכחה:</span>
</div>

- תהי $\sigma \notin P$ כלשהי.

- לפי הגדרת $P$, קיים $i$ כך ש־$p \in \sigma[2i]$ ו־$p \notin \sigma[i]$.
- תהי $\sigma'$ כך ש־$\sigma'[..2i] = \sigma[..2i]$.
- לפי הגדרת $P$, גם $\sigma' \notin P$.
- לכן ל־$\sigma$ יש רֵישָׁא רעה: $\sigma[..2i]$, וכל המשך שלה לא יקיים את התכונה.

</div>

<div class="relative mx-auto -mt-8 -ml-20 w-[78%] h-[120px] scale-60" dir="ltr">
  <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 900 120" aria-hidden="true">
    <defs>
      <marker id="bad-suffix-arrow" markerWidth="6" markerHeight="6" refX="5.5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 z" fill="#9a3412" />
      </marker>
    </defs>
    <path d="M 10 48 C 90 20, 170 36, 245 44 S 300 18, 360 38 S 430 50, 465 45"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" />
    <circle cx="465" cy="45" r="7" fill="#9a3412" />
    <path d="M 465 45 C 525 5, 610 38, 680 28 S 800 25, 890 12"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-suffix-arrow)" />
    <path d="M 465 45 C 525 38, 560 78, 635 74 S 800 70, 885 78"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-suffix-arrow)" />
    <path d="M 465 45 C 520 78, 540 120, 625 100 S 785 92, 890 150"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-suffix-arrow)" />
    <path d="M 430 102 C 440 82, 452 68, 462 55"
          fill="none" stroke="#dc2626" stroke-width="5" marker-end="url(#bad-suffix-arrow)" />
  </svg>
  <div class="absolute left-[24%] -top-[5%] text-[#5f1f1a] text-[22px] font-bold">

  $\sigma[..2i]$
  </div>
  <div class="absolute left-[24%] top-[82%] text-red-600 text-[15px] leading-tight text-center" dir="rtl">
    רֵישָׁא רעה שכל המשך שלה לא<br/>
    מקיים את התכונה
  </div>
</div>

---

# דוגמה: הוכחת אי־בטיחות


<div class="mt-6 text-right text-[16px]">

**טענה:** התכונה הבאה אינה תכונת בטיחות:

<div class="mt-3 text-center" dir="ltr">

$P = \{\sigma \in (2^{AP})^\omega \mid \exists i \geq 0 (p \in \sigma[i])\}$
</div>

<div class="mt-5">
<span class="font-bold underline">הוכחה:</span>
</div>

- ניקח את המילה $\sigma = \{\}^{\omega}$ שאינה שייכת ל־$P$.

- לכל $i$ נבנה את המילה $\sigma' = \{\}^{i}\{p\}^{\omega}$.
- על פי הגדרת $P$, מתקיים $\sigma' \in P$.
- קיבלנו שלכל $i$ קיימת $\sigma'$ כך ש־$\sigma'[..i] = \sigma[..i]$ וגם $\sigma' \in P$.
- לכן אין ל־$\sigma$ רֵישָׁא רעה, ולכן $P$ אינה תכונת בטיחות.

</div>

<div class="relative mx-auto -mt-5 w-[82%] h-[125px] scale-60" dir="ltr">
  <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 900 135" aria-hidden="true">
    <defs>
      <marker id="good-suffix-arrow" markerWidth="6" markerHeight="6" refX="5.5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 z" fill="#2f6b08" />
      </marker>
      <marker id="bad-base-arrow" markerWidth="6" markerHeight="6" refX="5.5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 z" fill="#9a3412" />
      </marker>
    </defs>
    <path d="M 20 52 C 115 74, 220 72, 330 70 S 535 66, 655 72 S 790 46, 880 62"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-base-arrow)" />
    <circle cx="135" cy="64" r="7" fill="#2f6b08" />
    <circle cx="225" cy="68" r="7" fill="#2f6b08" />
    <circle cx="355" cy="69" r="7" fill="#2f6b08" />
    <circle cx="585" cy="70" r="7" fill="#2f6b08" />
    <circle cx="635" cy="70" r="7" fill="#2f6b08" />
    <path d="M 135 64 C 210 120, 280 106, 360 110 S 510 180, 880 170"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 225 68 C 305 18, 390 45, 465 30 S 610 8, 880 -10"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 355 69 C 430 100, 500 90, 570 110 S 735 140, 880 140"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 585 70 C 650 100, 705 112, 790 104 S 845 98, 880 100"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 635 70 C 675 28, 725 42, 765 30 S 835 24, 880 28"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
  </svg>
  <div class="absolute left-[0%] top-[2%] text-[#5f1f1a] text-[22px] font-bold">

  $\sigma \notin P$


  </div>

  <div class="absolute -left-[10%] top-[48%] text-[#5f1f1a] text-[22px] font-bold" dir="rtl">
  מילה רעה<br/> בלי רישא רעה
  </div>


</div>

---

# היחס בין תכונות בטיחות ותכונות שמורה?

<div class="mt-5 text-center text-[30px] leading-relaxed">
משפט: כל <span class="text-blue-700 font-bold">תכונת שמורה</span> היא גם <span class="text-red-600 font-bold">תכונת בטיחות</span>
</div>

<InclusionDiagramD3 :width="760" :height="300" :fontSize="20"
  :sets="[
    { label: 'תכונות זמן לינארי', fill: '#4285F4', stroke: '#AECBFA', textColor: '#ffffff' },
    { label: 'תכונות בטיחות', fill: '#DB4437', stroke: '#F4B7B2', textColor: '#ffffff' },
    { label: 'תכונות שמורה', fill: '#0F9D58', stroke: '#A8DAB5', textColor: '#ffffff' }
  ]"
/>

<div class="mt-1 text-center text-[30px]">
הוכחה?
</div>

---

# הגדרה: תכונות בטיחות רגולריות

<div class="mt-5 text-right text-[15px]">
תכונה שקבוצת הרישות הרעות שלה היא שפה רגולרית
</div>

<div class="mt-7 text-right text-[15px]">
כל תכונת שמורה היא תכונת בטיחות רגולרית:
</div>

<div class="grid grid-cols-[0.9fr_1.5fr] gap-8 mt-6 items-center">

<AutomatonD3 :width="260" :height="50" :stateLabelFontSize="18" :transitionLabelFontSize="16"
  :states="[
    { id: 'ok', x: 90,   y: 35, label: ' ', initial: true, r: 16 },
    { id: 'bad', x: 198, y: 35, label: ' ', r: 16, accepting: true }
  ]"
  :transitions="[
    { source: 'ok', target: 'ok', label: '$\\Phi$', loopDirection: '-90deg', loopRadius: 86, labelY: -10 },
    { source: 'ok', target: 'bad', label: '$\\neg\\Phi$', labelY: -10 },
    { source: 'bad', target: 'bad', label: '$True$', loopDirection: '-90deg', loopRadius: 86, labelY: -10 },
  ]"
/>

<div class="text-right text-[15px] leading-relaxed">

אם $\Phi$ היא תנאי השמורה, האוטומט שקורא את הרישא עובר למצב כישלון ברגע הראשון שבו מתקיים $\neg\Phi$.
</div>

</div>

<div class="-mt-5">
<InclusionDiagramD3 :width="760" :height="300" :fontSize="21"
  :sets="[
    { label: 'תכונות זמן לינארי', fill: '#d98a8a', stroke: '#9f4f4f', textColor: '#6b2f1f' },
    { label: 'תכונות בטיחות', fill: '#f28f8f', stroke: '#b95f5f', textColor: '#6b2f1f' },
    { label: 'תכונות בטיחות רגולריות', fill: '#f7aaaa', stroke: '#bf6666', textColor: '#6b2f1f', Y: 5 },
    { label: 'תכונות שמורה', fill: '#f2c7c4', stroke: '#9b7777', textColor: '#6b2f1f', Y: 10 }
  ]"
/>
</div>

---

# דוגמה: רמזור (סדר מופעים)

<div class="mt-8 text-right">

נניח שקבוצת הפסוקים האטומיים היא $AP = \{red, yellow, green\}$.
נדרוש את התכונה הבאה: **"מופע של אור אדום חייב לבוא מיד אחרי מופע של אור צהוב"**.

התכונה הפורמלית:
$$ P_{traffic} = \{ \sigma \in (2^{AP})^\omega \mid \forall i \ge 0 (red \in \sigma[i] \implies i > 0 \land yellow \in \sigma[i-1]) \} $$

### דוגמאות לרישות רעות:
1. **$\emptyset \{red\}$**: הרמזור התחיל כבוי (או לא מוגדר) ועבר לאדום.
2. **$\{green\} \{red\}$**: הרמזור עבר מירוק ישר לאדום.

<div class="mt-6 text-[15px]">

כל ריצה שמתחילה באחת הרישות האלו כבר הפרה את התכונה; שום המשך עתידי לא יכול לתקן את ההפרה.
גם רישות ארוכות יותר שממשיכות אחת מהרישות האלו הן רישות רעות.
</div>

</div>

---

# דוגמה: רמזור כאוטומט

<div class="mt-4 text-right text-[15px] leading-relaxed">

נתאר את קבוצת הרישות הרעות של התכונה באמצעות אוטומט סופי.
האוטומט זוכר רק האם האות הקודמת היתה צהובה; אם מופיע $red$ כאשר הקודמת לא היתה צהובה, עוברים למצב מקבל.
</div>

<div class="mt-6">
<AutomatonD3 variant="classic" :width="760" :height="235" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 's1', x: 135, y: 130, label: '$s_1$', r: 22, labelWidth: 70 },
    { id: 's0', x: 380, y: 130, label: '$s_0$', initial: true, initialDirection: 'top', r: 22, labelWidth: 70 },
    { id: 's2', x: 610, y: 130, label: '$s_2$', r: 22, accepting: true, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', label: '$yellow \\land \\neg red$', curve: 0.36, labelY: -12, labelWidth: 145, tooltip: 'האותיות המקיימות: {yellow}' },
    { source: 's1', target: 's0', label: '$\\neg yellow$', curve: 0.30, labelY: 12, labelWidth: 105, tooltip: 'האותיות המקיימות: ∅, {red}' },
    { source: 's1', target: 's1', label: '$yellow$', loopDirection: '180deg', labelX: -32, labelY: 0, labelWidth: 85, tooltip: 'האותיות המקיימות: {yellow}, {red, yellow}' },
    { source: 's0', target: 's0', label: '$\\neg(yellow \\lor red)$', loopDirection: '90deg',  labelY: 10, labelWidth: 145, tooltip: 'האותיות המקיימות: ∅' },
    { source: 's0', target: 's2', label: '$red$', labelY: -10, labelWidth: 70, tooltip: 'האותיות המקיימות: {red}, {red, yellow}' },
    { source: 's2', target: 's2', label: '$True$', loopDirection: '0deg', labelX: 32, labelY: 0, labelWidth: 70, tooltip: 'כל האותיות' }
  ]"
/>
</div>

<div class="mt-2 text-right text-[14px] leading-relaxed">

למשל, אחרי $\emptyset$ האוטומט נשאר ב-$s_0$, ואז קריאת $\{red\}$ מעבירה אותו ל-$s_2$.
לעומת זאת, אחרי $\{yellow\}$ האוטומט נמצא ב-$s_1$, ולכן מותר לקרוא $\{red\}$.
</div>

---

# תכונות בטיחות למכונת משקאות

<div class="mt-5 text-right text-[18px]">

- דרישה טבעית:

<div class="mx-auto my-4 w-[88%] bg-green-100 shadow-md p-3 text-center text-green-600 text-[18px]">
"מספר המטבעות שהוכנסו הוא לפחות מספר המשקאות שניתנו"
</div>


לכל $i \ge 0$:

$$|\{0 \le j \le i : drink \in A_j\}| \le |\{0 \le j \le i : pay \in A_j\}|$$

- רישות רעות:

<div class="mt-3 text-left text-[15px] leading-[2.2]" dir="ltr">

$\emptyset\ \{pay\}\ \{drink\}\ \{drink\}$

$\emptyset\ \{pay\}\ \{drink\}\ \emptyset\ \{pay\}\ \{drink\}\ \{drink\}$
</div>

</div>

<div class="text-red-600 mt-10">

זאת דוגמה לתכונת בטיחות
 שלא ניתן לבטא את הרישות הרעות שלה כשפה רגולרית.
 <br/>
  ז"א תכונת בטיחות שאינה תכונת בטיחות רגולרית.
</div>



---

<div class="transform scale-90 origin-top-right">

# אימות תכונות בטיחות

<div class="mt-5 text-right text-[14px] leading-snug">


<div class="bg-green-50 border border-green-200 p-2">

עבור מערכת מעברים $TS$ ללא מצבים סופניים, ותכונת בטיחות $P_{safe}$:
$$ TS \models P_{safe} \iff Traces_{fin}(TS) \cap \operatorname{BadPref}(P_{safe}) = \emptyset $$
</div>


**($\implies$)** נניח ש-$TS \models P_{safe}$. נוכיח שהחיתוך ריק.
- נניח בשלילה שקיימת $\rho \in Traces_{fin}(TS) \cap \operatorname{BadPref}(P_{safe})$.
- כיוון ש-$\rho \in Traces_{fin}(TS)$ ו-$TS$ ללא מצבים סופניים, ניתן להאריך את המסלול שיצר את $\rho$ לריצה אינסופית. לכן קיימת עקבה אינסופית $\sigma \in Traces(TS)$ כך ש-$\rho \prec \sigma$.
- כיוון ש-$\rho$ היא רֵישָׁא רעה של $P_{safe}$, כל עקבה אינסופית שממשיכה את $\rho$ אינה שייכת ל-$P_{safe}$. בפרט, $\sigma \notin P_{safe}$.
- קיבלנו $\sigma \in Traces(TS)$ אבל $\sigma \notin P_{safe}$, בסתירה ל-$TS \models P_{safe}$.

**($\impliedby$)** נניח ש-$Traces_{fin}(TS) \cap \operatorname{BadPref}(P_{safe}) = \emptyset$. נוכיח ש-$TS \models P_{safe}$.
- נניח בשלילה ש-$TS \not\models P_{safe}$. לכן קיימת עקבה אינסופית $\sigma \in Traces(TS)$ כך ש-$\sigma \notin P_{safe}$.
- מכיוון ש-$P_{safe}$ היא תכונת בטיחות, קיימת ל-$\sigma$ רֵישָׁא רעה $\rho \prec \sigma$.
- מאחר ש-$\rho$ היא רֵישָׁא של עקבה שמיוצרת על ידי $TS$, מתקיים $\rho \in Traces_{fin}(TS)$.
- מצד שני, $\rho \in \operatorname{BadPref}(P_{safe})$. לכן $\rho$ שייכת לחיתוך, בסתירה לכך שהחיתוך ריק.
- מכאן $TS \models P_{safe}$.

</div>

</div>

---

# הכלת עקבות סופיות (Finite Trace Inclusion)

<div class="mt-8 text-right">

כאשר מתכננים מערכת בגישה של עידון הדרגתי (Stepwise Refinement), לרוב אנו מעוניינים להוכיח שאם המודל האבסטרקטי מקיים תכונה, כך גם המודל המפורט (המעודן).

ראינו קודם ש**הכלת עקבות אינסופיות** שומרת על *כל* תכונות הזמן הלינארי. תכונות בטיחות דורשות פחות מזה:

<div class="bg-slate-50 border border-slate-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">משפט: בטיחות והכלת עקבות סופיות</div>

יהיו $TS$ ו-$TS'$ שתי מערכות מעברים ללא מצבים סופניים, מעל אותה קבוצת פסוקים אטומיים $AP$. התנאים הבאים שקולים:
1. $Traces_{fin}(TS) \subseteq Traces_{fin}(TS')$
2. לכל תכונת בטיחות $P_{safe}$: אם $TS' \models P_{safe}$ אזי $TS \models P_{safe}$
</div>

המשמעות: כדי לשמר תכונות בטיחות, מספיק להראות שהמערכת המפורטת $TS$ לא יכולה לייצר אף עקבה **סופית** שלא הייתה אפשרית במערכת האבסטרקטית $TS'$.

</div>

---

<script setup>
const traceExStates = [
  // TS (Left)
  { id: 'ts_label', x: 100, y: 5, text: 'TS', color: 'transparent', stroke: 'none', textFontSize: 24 },
  { id: 'ts_s', text: ' ', x: 100, y: 145, label: '{}', labelFontSize: 20, color: '#fee2e2', stroke: '#dc2626', rx: 0, width: 50, initial: true, initialDirection: 'left' },

  // TS' (Right)
  { id: 'tsp_label', x: 550, y: 5, text: 'TS\'', color: 'transparent', stroke: 'none', textFontSize: 24 },
  { id: 'tsp_init', text: ' ', x: 550, y: 145, initial: true, initialDirection: 'left', color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  
  // Branch 1
  { id: 'b1', text: ' ', x: 670, y: 40, label: '{b}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  
  // Branch 2
  { id: 'e2_1', text: ' ', x: 670, y: 110, label: '{}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  { id: 'b2', text: ' ', x: 770, y: 110, label: '{b}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  
  // Branch 3
  { id: 'e3_1', text: ' ', x: 670, y: 180, label: '{}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  { id: 'e3_2', text: ' ', x: 770, y: 180, label: '{}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  { id: 'b3', text: ' ', x: 870, y: 180, label: '{b}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },

  // Branch 4
  { id: 'e4_1', text: ' ', x: 670, y: 250, label: '{}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  { id: 'e4_2', text: ' ', x: 770, y: 250, label: '{}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  { id: 'e4_3', text: ' ', x: 870, y: 250, label: '{}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },
  { id: 'b4', text: ' ', x: 970, y: 250, label: '{b}', labelFontSize: 20, color: '#e0f2fe', stroke: '#0284c7', rx: 0, width: 50 },

  // Dots
  { id: 'dots', x: 670, y: 320, text: '$\\vdots$', color: 'transparent', stroke: 'none', textFontSize: 26 }
];

const traceExTransitions = [
  { source: 'ts_s', target: 'ts_s', loopDirection: '-90deg', loopRadius: 70, loopSpread: 0.15 },
  { source: 'tsp_init', target: 'b1' },
  { source: 'tsp_init', target: 'e2_1' },
  { source: 'e2_1', target: 'b2' },
  { source: 'tsp_init', target: 'e3_1' },
  { source: 'e3_1', target: 'e3_2' },
  { source: 'e3_2', target: 'b3' },
  { source: 'tsp_init', target: 'e4_1' },
  { source: 'e4_1', target: 'e4_2' },
  { source: 'e4_2', target: 'e4_3' },
  { source: 'e4_3', target: 'b4' },
  { source: 'tsp_init', target: 'dots' },
  { source: 'b1', target: 'b1', loopDirection: '0deg', loopRadius: 70, loopSpread: 0.15 },
  { source: 'b2', target: 'b2', loopDirection: '0deg', loopRadius: 70, loopSpread: 0.15 },
  { source: 'b3', target: 'b3', loopDirection: '0deg', loopRadius: 70, loopSpread: 0.15 },
  { source: 'b4', target: 'b4', loopDirection: '0deg', loopRadius: 70, loopSpread: 0.15 }
];
</script>

# דוגמה: הכלת עקבות $\neq$ הכלת עקבות סופיים

<div class="text-right leading-relaxed text-[15px] mt-2">

נשים לב שהתנאי להכלת תכונות בטיחות הוא **הכלת עקבות סופיות**, וזהו תנאי חלש יותר מהכלת עקבות אינסופיות.
</div>

<div class="grid grid-cols-2 gap-4 mt-3">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-[14px]">
    
<div class="font-bold mb-1 text-blue-800">הכלת עקבות אינסופיות:</div>

- המערכת $TS$ מייצרת את $\emptyset^\omega$.
- המערכת $TS'$ **לא** מייצרת את $\emptyset^\omega$.
- לכן: $Traces(TS) \not\subseteq Traces(TS')$.

</div>

<div class="bg-green-50 border border-green-200 rounded p-3 text-[14px]">
    
<div class="font-bold mb-1 text-green-800">הכלת עקבות סופיות:</div>

- כל רֵישָׁא סופית של $\emptyset^\omega$ היא $\emptyset^n$.
- לכל $n$, קיימת עקבה ב-$TS'$ שמתחילה ב-$\emptyset^n$.
- לכן: $Traces_{fin}(TS) \subset Traces_{fin}(TS')$.

</div>
</div>

<div class="flex justify-center mt-1 h-[270px] w-full">
  <div class="relative bg-white border border-slate-200 rounded-xl shadow-lg p-2" dir="ltr" style="transform: scale(0.68); transform-origin: top center; width: 1100px; height: 390px;">
    <TransitionSystemD3 :width="1100" :height="380" :auto="false" 
      :states="traceExStates" 
      :transitions="traceExTransitions" 
    />
    
</div>
</div>


---

# משפט: עקבות סופיים מול אינסופיים

<div class="mt-8 text-right text-[18px] leading-relaxed">

עבור $TS$ **ללא מצבים סופניים** ו-$TS'$ בעלת מספר **סופי** של מצבים:

<div class="flex justify-center my-10" v-click>
<div class="bg-blue-50 border border-blue-300 rounded-lg p-6 shadow-sm text-center text-[22px] w-3/4">

$Traces(TS) \subseteq Traces(TS')$<br>
<div class="my-3 font-bold text-blue-700 text-[18px]">אם ורק אם</div>

$Traces_{fin}(TS) \subseteq Traces_{fin}(TS')$
</div>
</div>

<div v-click class="bg-amber-50 border border-amber-300 rounded p-0 -mt-6 shadow-sm text-[17px]">
<div class="font-bold -mb-2 text-amber-800">💡 הוכיחו או הפריכו:</div>

קיימת תכונת זמן לינארי שמערכת $TS'$ מקיימת ומערכת $TS$ לא מקיימת, אם ורק אם קיימת תכונת בטיחות שמערכת $TS'$ מקיימת ומערכת $TS$ לא מקיימת.
</div>

</div>

---

# הוכחת המשפט

<div class="mt-6 text-right leading-relaxed text-[17px]">

<div class="font-bold text-blue-700 text-lg mb-2">

כיוון ראשון ($\implies$):
</div>

אם $Traces(TS) \subseteq Traces(TS')$ אזי $Traces_{fin}(TS) \subseteq Traces_{fin}(TS')$

<ul class="list-disc list-inside mb-8 mt-2">
  <li>תרגיל קל (נובע ישירות מהגדרת רישות של עקבה).</li>
</ul>

<div v-click>
<div class="font-bold text-blue-700 text-lg mb-2">

כיוון שני ($\impliedby$):
</div>

נניח $Traces_{fin}(TS) \subseteq Traces_{fin}(TS')$ ונוכיח $Traces(TS) \subseteq Traces(TS')$.
</div>

<v-clicks>

- תהי $\sigma \in Traces(TS)$. עלינו למצוא מסלול $s_0 s_1 \dots$ של $TS'$ שאלו עקבותיו.
- ע"פ ההנחה: לכל $m$ קיים מסלול $\pi_m$ של $TS'$ כך ש- $trace(\pi_m) = \sigma[..m]$.
- למרות ש-$\sigma[..m]$ היא רֵישָׁא של $\sigma[..m+1]$, **לא ברור** ש-$\pi_m$ הוא רֵישָׁא של $\pi_{m+1}$.
- בזכות **הסופיות** של $TS'$, קיימת תת-סדרה $\pi_{s_1}, \pi_{s_2}, \dots$ של $\pi_1, \pi_2, \dots$ כך ש-$\pi_{s_i}$ ו-$\pi_{s_{i+1}}$ **מסכימות על $i$ האינדקסים הראשונים**.
- ניקח את המסלול שבו המצב במקום ה-$i$ הוא המצב ה-$i$ של $\pi_{s_i}$. (ראו דוגמה נגדית בשקף הקודם למערכת ללא סופיות!)

</v-clicks>

</div>

---

# המחשה גרפית: בניית המסלול ב- $TS'$


<div class="mt-4 flex justify-center w-full" dir="ltr">
  <table class="text-center border-collapse text-[16px] w-full max-w-4xl bg-white shadow-sm rounded">
    <thead>
      <tr class="border-b-2 border-slate-300 font-bold bg-slate-50">
        <th class="p-2 w-32 border-r border-slate-200 text-right" dir="rtl">&rarr; ריצה של <i class="font-serif">TS</i></th>
        <th class="p-2 w-16"><i class="font-serif">q</i><sub>1</sub></th>
        <th class="p-2 w-16"><i class="font-serif">q</i><sub>2</sub></th>
        <th class="p-2 w-16"><i class="font-serif">q</i><sub>3</sub></th>
        <th class="p-2 w-16"><i class="font-serif">q</i><sub>4</sub></th>
        <th class="p-2 w-16"><i class="font-serif">q</i><sub>5</sub></th>
        <th class="p-2">&hellip;</th>
      </tr>
      <tr class="border-b-4 border-slate-400 font-bold bg-blue-50 text-blue-800">
        <th class="p-2 border-r border-slate-200 text-right" dir="rtl">&rarr; תיוגים</th>
        <th class="p-2"><i class="font-serif">L</i>(<i class="font-serif">q</i><sub>1</sub>)</th>
        <th class="p-2"><i class="font-serif">L</i>(<i class="font-serif">q</i><sub>2</sub>)</th>
        <th class="p-2"><i class="font-serif">L</i>(<i class="font-serif">q</i><sub>3</sub>)</th>
        <th class="p-2"><i class="font-serif">L</i>(<i class="font-serif">q</i><sub>4</sub>)</th>
        <th class="p-2"><i class="font-serif">L</i>(<i class="font-serif">q</i><sub>5</sub>)</th>
        <th class="p-2">&hellip;</th>
      </tr>
    </thead>
    <tbody class="font-mono text-[14px]">
      <tr class="border-b border-slate-100 transition-opacity duration-500" :class="{ 'opacity-20': $slidev.nav.clicks >= 1 }">
        <td class="p-2 border-r border-slate-200 font-sans text-right bg-slate-50" dir="rtl">&rarr; ריצה לרישא 1</td>
        <td class="p-2 bg-red-100 text-red-800"><i class="font-serif">q</i><sub>1,1</sub></td>
        <td class="p-2"></td><td class="p-2"></td><td class="p-2"></td><td class="p-2"></td><td class="p-2"></td>
      </tr>
      <tr class="border-b border-slate-100 transition-opacity duration-500" :class="{ 'opacity-20': $slidev.nav.clicks >= 2 }">
        <td class="p-2 border-r border-slate-200 font-sans text-right bg-slate-50" dir="rtl">&rarr; ריצה לרישא 2</td>
        <td class="p-2 bg-green-100 text-green-900 border-2" :class="$slidev.nav.clicks >= 1 ? 'border-green-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>2,1</sub></td>
        <td class="p-2 bg-yellow-100 text-yellow-800"><i class="font-serif">q</i><sub>2,2</sub></td>
        <td class="p-2"></td><td class="p-2"></td><td class="p-2"></td><td class="p-2"></td>
      </tr>
      <tr class="border-b border-slate-100 transition-opacity duration-500" :class="{ 'opacity-20': $slidev.nav.clicks >= 1 }">
        <td class="p-2 border-r border-slate-200 font-sans text-right bg-slate-50" dir="rtl">&rarr; ריצה לרישא 3</td>
        <td class="p-2 bg-red-100 text-red-800"><i class="font-serif">q</i><sub>3,1</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>3,2</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>3,3</sub></td>
        <td class="p-2"></td><td class="p-2"></td><td class="p-2"></td>
      </tr>
      <tr class="border-b border-slate-100 transition-opacity duration-500">
        <td class="p-2 border-r border-slate-200 font-sans text-right bg-slate-50" dir="rtl">&rarr; ריצה לרישא 4</td>
        <td class="p-2 bg-green-100 text-green-900 border-2" :class="$slidev.nav.clicks >= 1 ? 'border-green-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>4,1</sub></td>
        <td class="p-2 bg-purple-100 text-purple-900 border-2" :class="$slidev.nav.clicks >= 2 ? 'border-purple-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>4,2</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>4,3</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>4,4</sub></td>
        <td class="p-2"></td><td class="p-2"></td>
      </tr>
      <tr class="border-b border-slate-100 transition-opacity duration-500" :class="{ 'opacity-20': $slidev.nav.clicks >= 2 }">
        <td class="p-2 border-r border-slate-200 font-sans text-right bg-slate-50" dir="rtl">&rarr; ריצה לרישא 5</td>
        <td class="p-2 bg-green-100 text-green-900 border-2" :class="$slidev.nav.clicks >= 1 ? 'border-green-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>5,1</sub></td>
        <td class="p-2 bg-yellow-100 text-yellow-800"><i class="font-serif">q</i><sub>5,2</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>5,3</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>5,4</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>5,5</sub></td>
        <td class="p-2"></td>
      </tr>
      <tr class="border-b border-slate-100 transition-opacity duration-500">
        <td class="p-2 border-r border-slate-200 font-sans text-right bg-slate-50" dir="rtl">&rarr; ריצה לרישא 6</td>
        <td class="p-2 bg-green-100 text-green-900 border-2" :class="$slidev.nav.clicks >= 1 ? 'border-green-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>6,1</sub></td>
        <td class="p-2 bg-purple-100 text-purple-900 border-2" :class="$slidev.nav.clicks >= 2 ? 'border-purple-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>6,2</sub></td>
        <td class="p-2 bg-blue-100 text-blue-900 border-2" :class="$slidev.nav.clicks >= 3 ? 'border-blue-500 font-bold' : 'border-transparent'"><i class="font-serif">q</i><sub>6,3</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>6,4</sub></td>
        <td class="p-2 bg-slate-100"><i class="font-serif">q</i><sub>6,5</sub></td>
        <td class="p-2 font-bold">&hellip;</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="mt-6 text-right text-[16px] font-bold text-slate-700 bg-slate-50 p-4 rounded-lg border border-slate-200 min-h-[90px] shadow-sm flex items-center justify-center transition-all duration-500">
  <div v-if="$slidev.nav.clicks === 0">שלב 0: נתונות כל הריצות ב-$TS'$ שיוצרות רישות סופיות של התיוגים.</div>
  <div v-else-if="$slidev.nav.clicks === 1" class="text-green-700">שלב 1: ע"פ שובך היונים ($TS'$ סופית), קיים מצב בעמודה 1 החוזר אינסוף פעמים. נשמור רק את השורות האלו!</div>
  <div v-else-if="$slidev.nav.clicks === 2" class="text-purple-700">שלב 2: מתוך השורות שנותרו, מצב כלשהו חייב לחזור אינסוף פעמים גם בעמודה 2. נסנן שוב!</div>
  <div v-else class="text-blue-700">שלב 3: וכך הלאה... באלכסון המודגש נבנית ריצה אינסופית חוקית ב-$TS'$ שתיוגיה הם בדיוק תיוגי $\sigma$!</div>
</div>

<v-clicks>
  <div class="hidden">Click 1</div>
  <div class="hidden">Click 2</div>
  <div class="hidden">Click 3</div>
</v-clicks>


---

# סגור (Closure)


<div class="mt-8 text-right">

דרך מתמטית אלגנטית נוספת לאפיין תכונות בטיחות היא דרך המושג "סגור" (Closure).
עבור עקבה $\sigma$, נסמן ב-$\operatorname{pref}(\sigma)$ את קבוצת כל הרישות הסופיות שלה. באופן דומה עבור תכונה $P$, נסמן את אוסף הרישות שלה ב-$\operatorname{pref}(P)$.

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-6">
<div class="font-bold mb-2">הגדרה: סגור של תכונה</div>

הסגור של תכונה $P$ הוא קבוצת כל העקבות האינסופיות ש**כל הרישות שלהן** שייכים לקבוצת הרישות של $P$:
$$ \operatorname{closure}(P) = \{ \sigma \in (2^{AP})^\omega \mid \operatorname{pref}(\sigma) \subseteq \operatorname{pref}(P) \} $$
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 mt-6">
<div class="font-bold mb-2">משפט: אפיון אלטרנטיבי לתכונות בטיחות</div>

תכונת זמן לינארי $P$ היא תכונת בטיחות **אם ורק אם** היא שווה לסגור שלה: 
$P = \operatorname{closure}(P)$
</div>

</div>

---

# הוכחת משפט הסגור

<div class="mt-8 text-right text-[15px]">

**כיוון ראשון ($\implies$):** נניח ש-$P$ היא תכונת בטיחות. עלינו להראות ש-$P = \operatorname{closure}(P)$.
- ההכלה $P \subseteq \operatorname{closure}(P)$ נובעת ישירות מההגדרה (כל רֵישָׁא של $\sigma \in P$ שייך ל-$\operatorname{pref}(P)$).
- עבור ההכלה השנייה: יהי $\sigma \in \operatorname{closure}(P)$. נניח בשלילה ש-$\sigma \notin P$. 
- כיוון ש-$P$ תכונת בטיחות, קיים ל-$\sigma$ **רֵישָׁא רעה** $\rho \prec \sigma$. 
- מצד שני, כיוון ש-$\sigma \in \operatorname{closure}(P)$, כל הרישות שלו שייכים ל-$\operatorname{pref}(P)$, ולכן $\rho \in \operatorname{pref}(P)$. 
- משמעות הדבר היא שקיים $\sigma' \in P$ כך ש-$\rho \prec \sigma'$, בסתירה לכך ש-$\rho$ היא רֵישָׁא רעה. לכן $\sigma \in P$.

**כיוון שני ($\impliedby$):** נניח ש-$P = \operatorname{closure}(P)$. נראה ש-$P$ תכונת בטיחות.
- יהי $\sigma \notin P$. כיוון ש-$P = \operatorname{closure}(P)$, הרי ש-$\sigma \notin \operatorname{closure}(P)$.
- לפי הגדרת הסגור, קיים ל-$\sigma$ רֵישָׁא סופית $\rho \prec \sigma$ כך ש-$\rho \notin \operatorname{pref}(P)$.
- המשמעות היא שלא קיימת אף מילה $\sigma'$ המקיימת $\rho \prec \sigma'$ ושייכת ל-$P$.
- לכן $\rho$ היא **רֵישָׁא רעה** עבור $\sigma$, ומכאן ש-$P$ היא תכונת בטיחות.

</div>

---

# סיכום

<div class="grid grid-cols-2 gap-8 mt-10 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">מהות הבטיחות (Safety)</div>

- **אינטואיציה:** "משהו רע לעולם לא יקרה". הפרה מזוהה ב**זמן סופי** ע"י **רֵישָׁא רעה**.
- **אפיון מתמטי:** $P$ היא תכונת בטיחות אם ורק אם $P = \operatorname{closure}(P)$.
- **סוגים:** 
  - **רגולריות:** ניתן לזהות רֵישָׁא רעה ע"י אוטומט סופי (למשל: רמזור).
  - **לא רגולריות:** דורשות זיכרון אינסופי (למשל: מכונת משקאות).
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">אימות ושימור</div>

- **סיפוק התכונה:** $TS \models P_{safe}$ אם ורק אם אף עקבה סופית של המערכת אינה רֵישָׁא רעה.
- **שימור בעידון:** הכלת עקבות סופיות ($Traces_{fin} \subseteq Traces'_{fin}$) מספיקה כדי לשמר את כל תכונות הבטיחות.
- **סופיות המערכת:** במערכות סופיות, הכלת עקבות סופיות שקולה להכלת עקבות אינסופיות.
- **המשך:** בהרצאה הבאה נכיר תכונות **חַיּוּת** (Liveness).
</div>
</div>
