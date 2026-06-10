---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 14-model-checking-regular-safety-properties
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## בדיקת תכונות בטיחות רגולריות
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# בדיקת תכונות בטיחות רגולריות

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">נחזור לתכונות בטיחות רגולריות</div>

- נגדיר תכונת בטיחות רגולרית דרך רישות רעות.
- נראה למה מספיק להסתכל על רישות רעות מינימליות.
- נבדיל בין תכונות בטיחות רגולריות ולא רגולריות.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">נבנה אלגוריתם בדיקה</div>

- נתרגם בדיקת תכונת בטיחות רגולרית לבדיקת שְׁמוּרָה.
- נבנה מכפלה של מערכת מעברים עם אוטומט סופי.
- נשתמש בהפרת הַשְׁמוּרָה כדי להפיק דוגמה נגדית סופית.
</div>
</div>

---

# תזכורת: רישות רעות

<div class="mt-8 text-right text-[24px] leading-relaxed">
תכונת בטיחות <KatexInline math="P_{\mathrm{safe}}" /> היא תכונה שבה כל הפרה נחשפת אחרי מספר סופי של צעדים.
</div>

<div class="mt-8 text-center text-[24px]" dir="ltr">
<KatexInline display math="\begin{array}{rcl}
\mathit{BadPref}(P_{\mathrm{safe}}) &amp;=&amp; \{\rho\in(2^{AP})^* \mid \forall\sigma\in(2^{AP})^\omega\ (\rho\sigma\notin P_{\mathrm{safe}})\}\\[4pt]
&amp;=&amp; (2^{AP})^* \setminus \mathit{pref}(P_{\mathrm{safe}})
\end{array}" />
</div>

<div class="mt-8 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold text-red-700 mb-2">רישא רעה</div>
מרגע שראינו אותה, שום המשך אינסופי כבר לא יכול לתקן את ההפרה.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-2">דוגמה נגדית סופית</div>
לכן בדיקת בטיחות מחזירה עדות סופית: מסלול שמגיע לרישא רעה.
</div>
</div>

---

# תכונת בטיחות רגולרית

<div class="mt-8 text-right text-[24px] leading-relaxed w-full">
תכונת בטיחות <KatexInline math="P_{\mathrm{safe}}" /> היא <span class="font-bold">רגולרית</span> אם קבוצת הרישות הרעות שלה היא שפה רגולרית:
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-5 text-[23px] leading-relaxed w-full">
קבוצת הרישות הרעות
<span dir="ltr"><KatexInline math="\mathit{BadPref}(P_{\mathrm{safe}})\subseteq (2^{AP})^*" /></span>
היא שפה רגולרית.
</div>

<div class="mt-8 grid grid-cols-[1fr_25%] gap-5 items-center">
<div class="bg-blue-50 border border-blue-200 rounded p-5 text-[22px] leading-relaxed">
קיים אוטומט סופי <KatexInline math="\mathcal{A}" /> מעל האלפבית <KatexInline math="2^{AP}" /> כך ש־
<span dir="ltr"><KatexInline math="\mathcal{L}(\mathcal{A})=\mathit{BadPref}(P_{\mathrm{safe}})" /></span>.
</div>

<img src="./public/security_automaton_guard.png" class="w-full rounded shadow-lg border-2 border-slate-200" />
</div>

---

# רישות רעות מינימליות

<div class="mt-7 text-right text-[23px] leading-relaxed">
רישא רעה <KatexInline math="\rho" /> היא <span class="font-bold">מינימלית</span> אם אף רישא ממש שלה אינה רעה.
</div>

<div class="mt-7 text-center text-[24px]" dir="ltr">
<KatexInline display math="\mathit{MinBadPref}(P_{\mathrm{safe}})=\{\rho\in\mathit{BadPref}(P_{\mathrm{safe}})\mid \forall\rho'\prec\rho\ \left(\rho'\notin\mathit{BadPref}(P_{\mathrm{safe}})\right)\}" />
</div>

<div class="grid grid-cols-2 gap-6 mt-7 text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">למה זה שימושי?</div>
אוטומט עבור רישות מינימליות עוצר בדיוק בנקודת ההפרה הראשונה, ולכן הדוגמה הנגדית שהוא מייצר בדרך כלל קצרה וברורה יותר.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold mb-3">משפט</div>
<KatexInline math="P_{\mathrm{safe}}" /> רגולרית אם ורק אם
<KatexInline math="\mathit{MinBadPref}(P_{\mathrm{safe}})" /> רגולרית.
<div class="mt-3 text-emerald-700 font-bold">נסו להוכיח בעצמכם 💪</div>
</div>
</div>

---

# למה המינימליות שומרת רגולריות?

<div class="grid grid-cols-2 gap-5 mt-5 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">ממינימליות לכל הרישות הרעות</div>
אם יש אוטומט שמקבל את הרישות הרעות המינימליות, מוסיפים לכל מצב מקבל לולאות על כל אות באלפבית.
מרגע שהגענו להפרה, כל המשך נשאר רישא רעה.

<div class="mt-3 bg-white rounded-lg shadow border-2 border-blue-200">
<AutomatonD3 variant="classic" :width="360" :height="170" :arrowSize="4" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { id: 'q0', x: 90, y: 85, label: '$q_0$', initial: true, initialDirection: 'top', r: 20, labelWidth: 60 },
    { id: 'qf', x: 245, y: 85, label: '$q_f$', accepting: true, r: 20, labelWidth: 60 }
  ]"
  :transitions="[
    { source: 'q0', target: 'qf', label: '$u$', labelY: -10, labelWidth: 45 },
    { source: 'qf', target: 'qf', label: '$\\Sigma$', loopDirection: '0deg', labelX: 24, labelWidth: 55 }
  ]"
/>
</div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">מכל הרישות הרעות למינימליות</div>
אם יש אוטומט שמקבל את כל הרישות הרעות, מסירים את כל המעברים היוצאים ממצבים מקבלים.
כך מתקבלות רק מילים שבהן הקבלה מתרחשת לראשונה בסוף המילה.

<div class="mt-3 bg-white rounded-lg shadow border-2 border-amber-200">
<AutomatonD3 variant="classic" :width="360" :height="170" :arrowSize="4" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { id: 'q0', x: 90, y: 85, label: '$q_0$', initial: true, initialDirection: 'top', r: 20, labelWidth: 60 },
    { id: 'qf', x: 245, y: 85, label: '$q_f$', accepting: true, r: 20, labelWidth: 60 }
  ]"
  :transitions="[
    { source: 'q0', target: 'qf', label: '$u$', labelY: -10, labelWidth: 45 }
  ]"
/>
</div>
</div>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-[18px]">
האינטואיציה: רישא רעה היא “נקודת אַל־חזור”; רישא רעה מינימלית היא נקודת אַל־חזור הראשונה.
</div>

---

# הבעיה האלגוריתמית

<div class="mt-3 grid grid-cols-[1.1fr_0.9fr] gap-5 items-center">
<div class="text-right text-[18px] leading-snug">

<div class="bg-blue-50 border border-blue-200 rounded p-3">
<div class="font-bold text-blue-700 mb-1">קלט</div>
מערכת מעברים סופית <KatexInline math="TS" />, ואוטומט סופי <KatexInline math="\mathcal{A}" /> עבור הרישות הרעות של תכונת בטיחות רגולרית <KatexInline math="P_{\mathrm{safe}}" />:
<div class="mt-1 text-center" dir="ltr">
<KatexInline math="\mathcal{L}(\mathcal{A})=\mathit{BadPref}(P_{\mathrm{safe}})" />
</div>
</div>

<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3">
<div class="font-bold text-emerald-700 mb-1">פלט רצוי</div>
אלגוריתם שמכריע אם <KatexInline math="TS\models P_{\mathrm{safe}}" />.
אם לא, הוא מפיק דוגמה נגדית סופית: מסלול של <KatexInline math="TS" /> שהעקבה שלו מגיעה לרישא רעה.
</div>

</div>

<img src="./public/regular-safety-problem-comic-he.svg" class="w-full rounded border border-slate-200 shadow-md" />
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-center text-[18px] leading-snug">
פלט: ריצה סופית <span dir="ltr"><KatexInline math="s_0s_1\cdots s_n" /></span> כך ש־
<span dir="ltr"><KatexInline math="L(s_0)L(s_1)\cdots L(s_n)\in\mathit{BadPref}(P_{\mathrm{safe}})" /></span>,
<br>
או הודעה שלא קיימת ריצה כזאת.
</div>

---

# דוגמאות

<div class="grid grid-cols-3 gap-5 mt-7 text-right text-[18px] leading-relaxed">
<div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 min-h-[190px]">
<div class="font-bold text-emerald-700 mb-3">שְׁמוּרָה</div>
כל שְׁמוּרָה היא תכונת בטיחות רגולרית.

<div class="mt-4 text-center" dir="ltr">
<KatexInline math="\mathit{MinBadPref} = (2^{AP})^* \neg\Phi" />
</div>
</div>
<div v-click class="mt-5 h-[86px] bg-lime-400 px-4 pt-9 text-center text-[17px] leading-snug shadow-sm" style="clip-path: polygon(50% 0, 100% 28%, 100% 100%, 0 100%, 0 28%);">
ראינו אלגוריתמים<br>לבדיקת תכונות שְׁמוּרָה
</div>
</div>

<div>
<div class="bg-blue-50 border border-blue-200 rounded p-4 min-h-[190px]">
<div class="font-bold text-blue-700 mb-3">תכונת בטיחות רגולרית שאינה שְׁמוּרָה</div>
אור אדום נדלק רק אם בצעד הקודם דלק אור צהוב.
צריך לזכור צעד אחד אחורה.
</div>
<div v-click class="mt-5 h-[86px] bg-yellow-300 px-4 pt-9 text-center text-[17px] leading-snug shadow-sm" style="clip-path: polygon(50% 0, 100% 28%, 100% 100%, 0 100%, 0 28%);">
אין לנו <span class="font-bold">עדיין</span> אלגוריתם<br>לתכונות שאינן שְׁמוּרָה
</div>
</div>

<div>
<div class="bg-red-50 border border-red-200 rounded p-4 min-h-[190px]">
<div class="font-bold text-red-700 mb-3">בטיחות לא רגולרית</div>
בכל רישא סופית, מספר המטבעות שהוכנסו אינו קטן ממספר המשקאות שסופקו.
כאן צריך זיכרון לא חסום.
</div>
<div v-click class="mt-5 h-[86px] bg-red-700 text-white px-4 pt-9 text-center text-[17px] leading-snug shadow-sm" style="clip-path: polygon(50% 0, 100% 28%, 100% 100%, 0 100%, 0 28%);">
לא נתאר<br>אלגוריתם לתכונות שאינן רגולריות
</div>
</div>
</div>

---

# דוגמה: מניעה הדדית

<div class="mt-7 text-right text-[23px] leading-relaxed">
בתכונת מניעה הדדית דורשים ששני תהליכים לא יהיו באזור הקריטי בו־זמנית.
</div>

<div class="mt-7 text-center text-[31px]" dir="ltr">
<KatexInline display math="P_{\mathrm{mutex}}=\{\sigma\mid \forall i\ge 0\ (\sigma[i]\not\models (crit_1\land crit_2))\}" />
</div>

<div class="grid grid-cols-2 gap-6 mt-7 text-right text-[21px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold text-red-700 mb-3">רישא רעה מינימלית</div>
מסלול שמסתיים בפעם הראשונה במצב שבו <KatexInline math="crit_1\land crit_2" /> נכון.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">אוטומט הבדיקה</div>
מספיק אוטומט קטן: כל עוד לא ראינו הפרה נשארים במצב תקין; כשנראה <KatexInline math="crit_1\land crit_2" /> עוברים למצב מקבל.
</div>
</div>

---

# דוגמה: רמזור

<div class="mt-7 text-right text-[23px] leading-relaxed">
נדרוש שאור אדום לא יידלק אם לא דלק אור צהוב בדיוק בצעד הקודם.
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

<div class="mt-4 text-[20px] leading-relaxed">
האוטומט זוכר אם בצעד הקודם דלק צהוב; אם אדום מופיע בלי זיכרון כזה, עוברים למצב מקבל.
</div>

---

# רעיון האלגוריתם : רדוקציה לבדיקת שְׁמוּרָה

<img src="./public/bad-prefix-monitor-machine.png" class="absolute right-[-165px] top-[82px] w-[500px]" />

<div class="absolute left-[145px] top-[150px] w-[350px] h-[100px] bg-blue-700 text-white text-center text-[22px] leading-tight px-7 pt-3 shadow-lg border-2 border-blue-950" style="clip-path: polygon(0 0, 100% 0, 100% 78%, 50% 100%, 0 78%);">
נוסיף למערכת רכיב שיזהה שנצפתה
רישא רעה
</div>

<div class="absolute left-[145px] top-[270px] w-[350px] h-[100px] bg-blue-700 text-white text-center text-[21px] leading-tight px-7 pt-5 shadow-lg border-2 border-blue-950" style="clip-path: polygon(0 0, 50% 12%, 100% 0, 100% 100%, 0 100%);">
ונבדוק את תכונת הַשְׁמוּרָה
<br>
“אף פעם לא נצפית רישא רעה”
</div>

<svg class="absolute left-[450px] top-[126px] w-[315px] h-[92px] z-20 overflow-visible" viewBox="-8 -12 325 92" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="monitor-arrow-head" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth">
      <path d="M 0 0 L 8 4 L 0 8 z" fill="#1d4ed8" />
    </marker>
  </defs>
  <path d="M 0 42 C 78 42, 122 42, 138 24 S 210 18, 281 18" stroke="#1d4ed8" stroke-width="7" stroke-linecap="round" marker-end="url(#monitor-arrow-head)" />
</svg>

---

# דוגמה לצורך המחשת רעיון הרדוקציה: מונה פשוט

<div class="mt-7 text-right text-[23px] leading-relaxed">
נבדוק את התכונה: בכל שלושה צעדים רצופים, לפחות אחד מקיים <KatexInline math="\psi" />.
</div>

<div class="mt-6 text-center text-[28px]" dir="ltr">
<KatexInline display math="P=\{\sigma\mid \forall i\ (\sigma[i]\models\psi\ \lor\ \sigma[i+1]\models\psi\ \lor\ \sigma[i+2]\models\psi)\}" />
</div>

<div class="mt-5 grid grid-cols-[1fr_auto_1fr] gap-5 items-center text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-[19px] leading-relaxed">
<div class="font-bold mb-2">המערכת המקורית</div>
בכל צעד עוברת ממצב <KatexInline math="s" /> למצב <KatexInline math="t" /> ומייצרת תווית <KatexInline math="L(t)" />.
</div>

<div class="text-[34px] text-slate-500">+</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 text-[19px] leading-relaxed">
<div class="font-bold mb-2">מנגנון התראה</div>
שומר מונה <KatexInline math="c\in\{0,1,2,3\}" /> של מספר הצעדים הרצופים שבהם לא התקיים <KatexInline math="\psi" />.
</div>
</div>

<div class="mt-5 grid grid-cols-4 gap-3 text-center text-[18px]">
<div class="bg-emerald-50 border border-emerald-200 rounded p-2">
<div class="font-bold">מונה 0</div>
<div class="text-[14px] mt-0">ראינו <KatexInline math="\psi" /></div>
</div>
<div class="bg-sky-50 border border-sky-200 rounded p-2">
<div class="font-bold">מונה 1</div>
<div class="text-[14px] mt-0">צעד אחד בלי <KatexInline math="\psi" /></div>
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-3">
<div class="font-bold">מונה 2</div>
<div class="text-[15px] mt-1">שני צעדים בלי <KatexInline math="\psi" /></div>
</div>
<div class="bg-red-50 border border-red-200 rounded p-3">
<div class="font-bold text-red-700">התראה</div>
<div class="text-[15px] mt-1">שלושה צעדים בלי <KatexInline math="\psi" /></div>
</div>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-4 text-[19px] leading-relaxed">
במערכת המורחבת המצבים הם מהצורה <span dir="ltr"><KatexInline math="\langle s,c\rangle" /></span>.
אם <KatexInline math="L(t)\models\psi" /> מאפסים את המונה; אחרת מעלים אותו באחד. כאשר מגיעים ל־<KatexInline math="c=3" />, התווית של המצב כוללת <KatexInline math="bad" />.
</div>

---

# הרכבת המונה עם המערכת

<div class="-mt-3 text-right text-[18px] leading-snug">
נבנה מערכת מעברים חדשה כמכפלה סינכרונית של המערכת המקורית עם מונה דטרמיניסטי, כך שהמונה זוכר כמה צעדים רצופים עברו בלי <KatexInline math="\psi" />.
</div>

<div class="mt-3 text-center text-[19px]" dir="ltr">
<KatexInline display math="TS_{\#}=\langle S\times\{0,1,2,3\},Act,\to_{\#},I_{\#},AP\cup\{bad\},L_{\#}\rangle" />
</div>

<div class="grid grid-cols-2 gap-3 -mt-0 text-right text-[14px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-3">
<div class="font-bold mb-2">מצבים התחלתיים</div>
מתחילים באותו מצב מערכת, והמונה נקבע לפי התווית הראשונה:
<div class="mt-1 text-center text-[13px]" dir="ltr">
<KatexInline math="I_{\#}=\{\langle s,0\rangle\mid s\in I,\ L(s)\models\psi\}\cup\{\langle s,1\rangle\mid s\in I,\ L(s)\not\models\psi\}" />
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-3">
<div class="font-bold mb-2">כלל גזירה: עדכון המונה והמעבר במכפלה</div>
המעברים במערכת <KatexInline math="TS_{\#}" /> מוגדרים על ידי הכלל:
<div class="mt-1 text-center text-[13px]" dir="ltr">
<KatexInline display math="\frac{s\xrightarrow{\alpha}t,\quad c'=\begin{cases}0 & L(t)\models\psi\\ \min(c+1,3) & L(t)\not\models\psi\end{cases}}{\langle s,c\rangle\xrightarrow{\alpha}_{\#}\langle t,c'\rangle}" />
</div>
</div>
</div>

<div class="mt-3 grid grid-cols-2 gap-3 text-[14px] leading-snug" dir="ltr">
<div class="bg-orange-50 border border-orange-200 rounded p-3 text-right" dir="rtl">
<div class="font-bold text-orange-800 mb-2">בדיקת שְׁמוּרָה על המערכת החדשה</div>
על המערכת שקיבלנו נוכל לבדוק את תכונת הַשְׁמוּרָה:
<div class="mt-1 text-center text-[13px]" dir="ltr">
<KatexInline math="P_{inv}=\{\sigma\mid \forall i\ge 0\ (\sigma[i]\models\neg bad)\}" />
</div>
<div class="mt-2 text-center text-[16px] text-red-700" dir="ltr">
<KatexInline math="TS\models P\iff TS_{\#}\models P_{inv}" />
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-3 text-right" dir="rtl">
<div class="font-bold text-red-700 mb-2">תוויות</div>
התווית המקורית נשמרת, ונוסיף התראה אם ראינו שלושה צעדים רצופים בלי <KatexInline math="\psi" />:
<div class="mt-1 text-center text-[13px]" dir="ltr">
<KatexInline math="L_{\#}(\langle s,c\rangle)=L(s)\cup\begin{cases}\{bad\} & c=3\\ \emptyset & c\neq 3\end{cases}" />
</div>
</div>
</div>

# ניסוח הבעיה

<div class="mt-8 text-right text-[23px] leading-relaxed">
נתונים:
</div>

<div class="mt-5 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
מערכת מעברים סופית ללא מצבים סופניים:
<div class="mt-3 text-center" dir="ltr">
<KatexInline math="TS=\langle S,Act,\to,I,AP,L\rangle" />
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
אוטומט סופי מעל <KatexInline math="2^{AP}" /> שמקבל את הרישות הרעות:
<div class="mt-3 text-center" dir="ltr">
<KatexInline math="\mathcal{L}(\mathcal{A})=\mathit{BadPref}(P_{\mathrm{safe}})" />
</div>
</div>
</div>

<div class="mt-8 bg-emerald-50 border border-emerald-200 rounded p-5 text-[24px] leading-relaxed">
המטרה: להכריע האם <KatexInline math="TS\models P_{\mathrm{safe}}" />.
</div>

---

# נפעיל את אותו הרעיון<br> לבדיקת תכונות בטיחות רגולרית באופן כללי

<div class="mt-8 text-right text-[24px] leading-relaxed">
נריץ את המערכת ואת אוטומט הרישות הרעות במקביל.
</div>

<div class="mt-7 grid grid-cols-[1fr_auto_1fr] gap-5 items-center text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
מערכת המעברים מייצרת עקבה:
<div class="mt-3 text-center" dir="ltr">
<KatexInline math="L(s_0)L(s_1)L(s_2)\cdots" />
</div>
</div>

<div class="text-[36px] text-slate-500">+</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
האוטומט קורא את התוויות ומזהה מתי נוצרה רישא רעה.
</div>
</div>

<div class="mt-8 bg-red-50 border border-red-200 rounded p-5 text-[23px] leading-relaxed">
אם מגיעים למצב מקבל של האוטומט, מצאנו רישא רעה ולכן מצאנו הפרה של תכונת הבטיחות.
</div>

---

# המכפלה עם אוטומט הרישות הרעות

<div class="mt-8 text-right text-[23px] leading-relaxed">
נשתמש באוטומט סופי:
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathcal{A}=\langle Q,2^{AP},\delta,Q_0,F\rangle" />
</div>

<div class="mt-7 text-right text-[23px] leading-relaxed">
נבנה מערכת מעברים חדשה שבה כל מצב שומר שני רכיבים:
</div>

<div class="mt-6 text-center text-[30px]" dir="ltr">
<KatexInline display math="TS\times\mathcal{A}=\langle S\times Q,Act,\to_\times,I_\times,Q,L_\times\rangle" />
</div>

<div class="mt-7 bg-slate-50 border border-slate-200 rounded p-5 text-[22px] leading-relaxed">
הרכיב הראשון הוא מצב המערכת; הרכיב השני הוא מצב האוטומט אחרי קריאת התוויות שראינו עד כה.
</div>

---

# הגדרת המכפלה

<div class="mt-4 text-right text-[19px] leading-relaxed">
המצבים ההתחלתיים:
</div>

<div class="mt-2 text-center text-[22px]" dir="ltr">
<KatexInline display math="I_\times=\{\langle s_0,q\rangle \mid s_0\in I \land \exists q_0\in Q_0\ (q\in\delta(q_0,L(s_0)))\}" />
</div>

<div class="mt-4 text-right text-[19px] leading-relaxed">
המעברים:
</div>

<div class="mt-2 text-center text-[22px]" dir="ltr">
<KatexInline display math="\frac{s\xrightarrow{\alpha}t \ \land\ p\in\delta(q,L(t))}{\langle s,q\rangle\xrightarrow{\alpha}_\times \langle t,p\rangle}" />
</div>

<div class="mt-4 text-right text-[19px] leading-relaxed">
התווית במכפלה משקפת את מצב האוטומט:
</div>

<div class="mt-2 text-center text-[22px]" dir="ltr">
<KatexInline display math="L_\times(\langle s,q\rangle)=\{q\}" />
</div>

---

# מה המכפלה מייצגת?

<div class="mt-8 text-right text-[22px] leading-relaxed">
מסלול סופי במכפלה:
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="\langle s_0,q_1\rangle\langle s_1,q_2\rangle\cdots\langle s_n,q_{n+1}\rangle" />
</div>

<div class="mt-6 text-right text-[22px] leading-relaxed">
קיים אם ורק אם <KatexInline math="s_0s_1\cdots s_n" /> הוא מסלול סופי התחלתי של <KatexInline math="TS" />, וקיימת ריצה של האוטומט:
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="q_0 \xrightarrow{L(s_0)} q_1 \xrightarrow{L(s_1)} q_2 \cdots \xrightarrow{L(s_n)} q_{n+1}" />
</div>

<div class="mt-7 bg-blue-50 border border-blue-200 rounded p-4 text-[22px]">
לכן מצב מקבל במכפלה פירושו: העקבה הסופית שנוצרה עד כה שייכת לשפת הרישות הרעות.
</div>

---

# הַשְׁמוּרָה שמחליפה את הבטיחות

<div class="mt-8 text-right text-[24px] leading-relaxed">
במכפלה כבר אין צורך לדבר על כל השפה הרגולרית. מספיק לבדוק שאף פעם לא מגיעים למצב אוטומט מקבל.
</div>

<div class="mt-8 text-center text-[30px]" dir="ltr">
<KatexInline display math="P_{\mathrm{inv}}=\{\sigma\in(2^Q)^\omega \mid \forall i\ge 0\ (\sigma[i]\cap F=\emptyset)\}" />
</div>

<div class="mt-8 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
אם הַשְׁמוּרָה מתקיימת, אין רישא רעה באף עקבה של המערכת.
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
אם הַשְׁמוּרָה מופרת, המסלול שמגיע ל־<KatexInline math="F" /> הוא דוגמה נגדית סופית.
</div>
</div>

---

# אינטואיציית הבניה

<div class="relative mt-2 mx-auto w-[96%] h-[560px] overflow-hidden">
  <div class="absolute top-[8px] left-1/2 -translate-x-1/2 w-[220px] h-[186px] overflow-hidden">
    <img src="./public/slide-reference/l18/image36.gif" class="w-[220px] h-[220px] object-cover object-top" style="clip-path: inset(0 0 34px 0);" />
  </div>

  <div class="absolute top-[206px] left-1/2 -translate-x-1/2 text-[27px]" dir="ltr">
    <KatexInline math="TS\times\mathcal{A}" />
  </div>

  <div class="absolute top-[184px] left-[98px] text-[20px] text-red-700 text-right leading-tight">
    האוטומט עוקב אחר<br>העקבות שנוצרות
  </div>

  <div class="absolute top-[-4px] right-[88px] text-[20px] text-blue-700 text-right leading-tight">
    מערכת המעברים<br>מייצרת עקבות
  </div>

  <svg class="absolute left-[184px] top-[42px] w-[212px] h-[148px]" viewBox="0 0 212 148" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow-red-build" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth">
        <path d="M 0 0 L 8 4 L 0 8 z" fill="#dc2626" />
      </marker>
    </defs>
    <path d="M 48 124 C 62 86, 98 58, 156 44" stroke="#dc2626" stroke-width="6" stroke-linecap="round" marker-end="url(#arrow-red-build)" />
  </svg>

  <svg class="absolute right-[176px] top-[26px] w-[204px] h-[148px]" viewBox="0 0 204 148" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow-blue-build" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth">
        <path d="M 0 0 L 8 4 L 0 8 z" fill="#1d4ed8" />
      </marker>
    </defs>
    <path d="M 170 34 C 150 64, 122 94, 70 126" stroke="#1d4ed8" stroke-width="6" stroke-linecap="round" marker-end="url(#arrow-blue-build)" />
  </svg>

  <div class="absolute left-[48.5%] -translate-x-1/2 bottom-[158px] w-[46%] bg-white/80 rounded px-4 py-2 text-center text-[25px]" dir="ltr">
    <KatexInline display math="\frac{s\xrightarrow{\alpha}{\color{blue}t}\ \land\ p\in\delta(q,L({\color{blue}t}))}{\langle s,q\rangle\xrightarrow{\alpha}_{\times}\langle {\color{blue}t},p\rangle}" />
  </div>

  <div class="absolute left-[56px] bottom-[228px] bg-[#0f4c81] text-white text-[16px] leading-tight px-4 py-2 shadow-md text-right" style="clip-path: polygon(0 0, 88% 0, 100% 50%, 88% 100%, 0 100%, 7% 50%);">
    קיים מעבר מערכת<br>המעברים המקורית
  </div>

  <div class="absolute right-[56px] bottom-[228px] bg-[#0f4c81] text-white text-[16px] leading-tight px-4 py-2 shadow-md text-right" style="clip-path: polygon(12% 0, 100% 0, 100% 100%, 12% 100%, 0 50%);">
    קיים מעבר באוטומט<br>הקורא את התווית של <span dir="ltr">t</span>
  </div>

  <div class="absolute left-1/2 -translate-x-1/2 bottom-[110px] w-[78%] bg-[#0f4c81] text-white text-[15px] px-8 py-3 rounded shadow-md text-center leading-tight">
    מערכת המעברים החדשה מתקדמת בשני הרכיבים,<br>זה שמייצג את מערכת המעברים המקורית וזה שעוקב אחר האוטומט
  </div>
</div>

---

# דוגמה: מערכת בת 3 מצבים

<div class="grid grid-cols-[1.15fr_0.85fr] gap-3 mt-1 items-start">
<div class="space-y-1.5">
<div class="bg-white border border-slate-200 rounded p-1 shadow-sm text-center">
<div class="text-[11px] font-bold text-blue-800 mb-0.5">מערכת המעברים <KatexInline math="TS" /></div>
<TransitionSystemD3
:width="440" :height="95" :auto="false"
:states="[
{ id: 't0', text: '$0$', label: '$\\{\\}$', initial: true, initialDirection: 'left', x: 60, y: 48, width: 44 },
{ id: 't1', text: '$1$', label: '$\\{\\}$', x: 190, y: 48, width: 44 },
{ id: 't2', text: '$2$', label: '$\\{X\\}$', x: 320, y: 48, width: 44 }
]"
:transitions="[
{ source: 't0', target: 't1', action: '$tick$', actionY: -10, actionWidth: 40 },
{ source: 't1', target: 't2', action: '$tick$', actionY: -10, actionWidth: 40 },
{ source: 't2', target: 't0', action: '$tick$', curve: 0.25, actionY: -14, actionWidth: 40 }
]"
/>
</div>

<div class="bg-white border border-slate-200 rounded p-1 shadow-sm text-center">
<div class="text-[11px] font-bold text-amber-800 mb-0.5">אוטומט הרישות הרעות <KatexInline math="\mathcal{A}" /></div>
<AutomatonD3 variant="classic" :width="440" :height="120" :arrowSize="3.5" :stateLabelFontSize="10" :transitionLabelFontSize="10"
:states="[
{ id: 'q0', x: 70, y: 58, label: '$q_0$', initial: true, initialDirection: 'top', r: 18 },
{ id: 'q1', x: 165, y: 58, label: '$q_1$',                  r: 18 },
{ id: 'q2', x: 260, y: 58, label: '$q_2$',                  r: 18 },
{ id: 'q3', x: 355, y: 58, label: '$q_3$', accepting: true, r: 18}
]"
:transitions="[
{ source: 'q0', target: 'q1', label: '$\\{\\}$', labelY: -10 },
{ source: 'q1', target: 'q2', label: '$\\{\\}$', labelY: -10 },
{ source: 'q2', target: 'q3', label: '$\\{\\}$', labelY: -10 },
{ source: 'q3', target: 'q3', label: '$\\{\\}$', loopDirection: '0deg', labelX: 20, loopRadius: 48 },
{ source: 'q0', target: 'q0', label: '$\\{X\\}$',    loopDirection: '180deg', labelX: -18, loopRadius: 48 },
{ source: 'q1', target: 'q0', label: '$\\{X\\}$', curve: -0.30, labelY: 15 },
{ source: 'q2', target: 'q0', label: '$\\{X\\}$', curve: 0.30, labelY: -10 },
{ source: 'q3', target: 'q1', label: '$\\{X\\}$', curve: -0.22, labelY: 15 }
]"
/>
</div>
</div>

<div class="space-y-1.5">
<div class="bg-white border border-slate-200 rounded p-1 shadow-sm text-center">
<div class="text-[12px] font-bold text-emerald-800 mb-0.5"><KatexInline math="TS \times \mathcal{A}" /></div>
<TransitionSystemD3
:width="340" :height="190" :auto="false"
:states="[
{ id: 'p0', text: '$\\langle 0, q_1 \\rangle$', label: '$\\{\\}$', labelY: 12, initial: true, initialDirection: 'top', x: 170, y: 45, width: 80, color: '#DCFCE7', stroke: '#15803D' },
{ id: 'p1', text: '$\\langle 1, q_2 \\rangle$', label: '$\\{\\}$', labelY: 12, x: 255, y: 140, width: 80, color: '#DCFCE7', stroke: '#15803D' },
{ id: 'p2', text: '$\\langle 2, q_0 \\rangle$', label: '$\\{X\\}$', labelY: 12, x: 85, y: 140, width: 80, color: '#DCFCE7', stroke: '#15803D' }
]"
:transitions="[
{ source: 'p0', target: 'p1', action: '$tick$', actionX: 10, actionY: -5 },
{ source: 'p1', target: 'p2', action: '$tick$', actionY: 12 },
{ source: 'p2', target: 'p0', action: '$tick$', actionX: -10, actionY: -5 }
]"
/>
</div>

<div class="bg-emerald-50/70 border border-emerald-200/80 rounded p-2 text-right text-[13px] leading-snug">
<div class="font-bold text-emerald-900 mb-0.5">התוצאה: התכונה מתקיימת!</div>
אף מצב נגיש במערכת המכפלה אינו מכיל את המצב המקבל <KatexInline math="q_3" />, לכן <KatexInline math="TS \models P_{\text{safe}}" />.
</div>
</div>
</div>

---

# דוגמה: מערכת בת 4 מצבים

<div class="grid grid-cols-[1.15fr_0.85fr] gap-3 mt-1 items-start">
<div class="space-y-1.5">
<div class="bg-white border border-slate-200 rounded p-1 shadow-sm text-center">
<div class="text-[11px] font-bold text-blue-800 mb-0.5">מערכת המעברים <KatexInline math="TS" /></div>
<TransitionSystemD3
:width="440" :height="95" :auto="false"
:states="[
{ id: 't0', text: '$0$', label: '$\\{\\}$', initial: true, initialDirection: 'left', x: 70, y: 48, width: 44 },
{ id: 't1', text: '$1$', label: '$\\{\\}$', x: 165, y: 48, width: 44 },
{ id: 't2', text: '$2$', label: '$\\{\\}$', x: 260, y: 48, width: 44 },
{ id: 't3', text: '$3$', label: '$\\{X\\}$', x: 355, y: 48, width: 44 }
]"
:transitions="[
{ source: 't0', target: 't1', action: '$tick$', actionY: -10, actionWidth: 40 },
{ source: 't1', target: 't2', action: '$tick$', actionY: -10, actionWidth: 40 },
{ source: 't2', target: 't3', action: '$tick$', actionY: -10, actionWidth: 40 },
{ source: 't3', target: 't0', action: '$tick$', curve: 0.25, actionY: -14, actionWidth: 40 }
]"
/>
</div>

<div class="bg-white border border-slate-200 rounded p-1 shadow-sm text-center">
<div class="text-[11px] font-bold text-amber-800 mb-0.5">אוטומט הרישות הרעות <KatexInline math="\mathcal{A}" /></div>
<AutomatonD3 variant="classic" :width="440" :height="120" :arrowSize="3.5" :stateLabelFontSize="10" :transitionLabelFontSize="10"
:states="[
{ id: 'q0', x: 70, y: 58, label: '$q_0$', initial: true, initialDirection: 'top', r: 18 },
{ id: 'q1', x: 165, y: 58, label: '$q_1$',                  r: 18 },
{ id: 'q2', x: 260, y: 58, label: '$q_2$',                  r: 18 },
{ id: 'q3', x: 355, y: 58, label: '$q_3$', accepting: true, r: 18}
]"
:transitions="[
{ source: 'q0', target: 'q1', label: '$\\{\\}$', labelY: -10 },
{ source: 'q1', target: 'q2', label: '$\\{\\}$', labelY: -10 },
{ source: 'q2', target: 'q3', label: '$\\{\\}$', labelY: -10 },
{ source: 'q3', target: 'q3', label: '$\\{\\}$', loopDirection: '0deg', labelX: 20, loopRadius: 48 },
{ source: 'q0', target: 'q0', label: '$\\{X\\}$',    loopDirection: '180deg', labelX: -18, loopRadius: 48 },
{ source: 'q1', target: 'q0', label: '$\\{X\\}$', curve: -0.30, labelY: 15 },
{ source: 'q2', target: 'q0', label: '$\\{X\\}$', curve: 0.30, labelY: -10 },
{ source: 'q3', target: 'q1', label: '$\\{X\\}$', curve: -0.22, labelY: 15 }
]"
/>
</div>
</div>

<div class="space-y-1.5">
<div class="bg-white border border-slate-200 rounded p-1 shadow-sm text-center">
<div class="text-[12px] font-bold text-red-800 mb-0.5"><KatexInline math="TS \times \mathcal{A}" /></div>
<TransitionSystemD3
:width="340" :height="190" :auto="false"
:states="[
{ id: 'p0', text: '$\\langle 0, q_1 \\rangle$', label: '$\\{\\}$', labelY: 12, initial: true, initialDirection: 'top', x: 55, y: 45, width: 80, color: '#DCFCE7', stroke: '#15803D' },
{ id: 'p1', text: '$\\langle 1, q_2 \\rangle$', label: '$\\{\\}$', labelY: 12, x: 55, y: 140, width: 80, color: '#DCFCE7', stroke: '#15803D' },
{ id: 'p2', text: '$\\langle 2, q_3 \\rangle$', label: '$\\{\\}$', labelY: 12, x: 170, y: 140, width: 80, color: '#FEE2E2', stroke: '#991B1B' },
{ id: 'p3', text: '$\\langle 3, q_3 \\rangle$', label: '$\\{X\\}$', labelY: 12, x: 285, y: 140, width: 80, color: '#FEE2E2', stroke: '#991B1B' },
{ id: 'p4', text: '$\\langle 0, q_3 \\rangle$', label: '$\\{\\}$', labelY: 12, x: 285, y: 45, width: 80, color: '#FEE2E2', stroke: '#991B1B' },
{ id: 'p5', text: '$\\langle 1, q_3 \\rangle$', label: '$\\{\\}$', labelY: 12, x: 170, y: 45, width: 80, color: '#FEE2E2', stroke: '#991B1B' }
]"
:transitions="[
{ source: 'p0', target: 'p1', action: '$tick$', actionX: -18 },
{ source: 'p1', target: 'p2', action: '$tick$', actionY: 10 },
{ source: 'p2', target: 'p3', action: '$tick$', actionY: 10 },
{ source: 'p3', target: 'p4', action: '$tick$', actionX: 18 },
{ source: 'p4', target: 'p5', action: '$tick$', actionY: -10 },
{ source: 'p5', target: 'p2', action: '$tick$', actionX: -18 }
]"
/>
</div>

<div class="bg-red-50/70 border border-red-200/80 rounded p-2 text-right text-[13px] leading-snug">
<div class="font-bold text-red-900 mb-0.5">התוצאה: התכונה מופרת!</div>
מערכת המכפלה מגיעה למצבים אדומים (המכילים את המצב המקבל <KatexInline math="q_3" />). לכן <KatexInline math="TS \not\models P_{\text{safe}}" />.
</div>
</div>
</div>

---

# המשפט המרכזי

<div class="mt-7 text-right text-[22px] leading-relaxed">
נניח ש־<KatexInline math="TS" /> סופית וללא מצבים סופניים, וש־<KatexInline math="\mathcal{A}" /> מקבלת את
<KatexInline math="\mathit{BadPref}(P_{\mathrm{safe}})" />.
אז התנאים הבאים שקולים:
</div>

<div class="mt-6 text-right text-[22px] leading-relaxed">
<ol class="space-y-4">
<li><span dir="ltr"><KatexInline math="TS\models P_{\mathrm{safe}}" /></span>.</li>
<li><span dir="ltr"><KatexInline math="\mathit{Traces}_{fin}(TS)\cap\mathcal{L}(\mathcal{A})=\emptyset" /></span>.</li>
<li><span dir="ltr"><KatexInline math="TS\times\mathcal{A}\models P_{\mathrm{inv}}" /></span>.</li>
</ol>
</div>

<div class="mt-7 bg-slate-50 border border-slate-200 rounded p-4 text-[21px]">
זו הרדוקציה: בדיקת תכונת בטיחות רגולרית מצטמצמת לבדיקת שְׁמוּרָה על מערכת מכפלה.
</div>

---

# דוגמה נגדית

<div class="mt-8 text-right text-[23px] leading-relaxed">
אם בדיקת הַשְׁמוּרָה נכשלת, נקבל מסלול התחלתי במכפלה:
</div>

<div class="mt-5 text-center text-[26px]" dir="ltr">
<KatexInline display math="\langle s_0,q_1\rangle\langle s_1,q_2\rangle\cdots\langle s_n,q_{n+1}\rangle" />
</div>

<div class="mt-7 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-5">
אם <KatexInline math="q_{n+1}\in F" />, אז
<span dir="ltr"><KatexInline math="L(s_0)L(s_1)\cdots L(s_n)\in\mathit{BadPref}(P_{\mathrm{safe}})" /></span>.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
ההיטל על רכיב המערכת, <KatexInline math="s_0s_1\cdots s_n" />, הוא מסלול אמיתי של <KatexInline math="TS" /> שמסביר את ההפרה.
</div>
</div>

---

# מצבים סופניים ומעברים חסרים

<div class="mt-8 text-right text-[23px] leading-relaxed">
אם באוטומט יש מעברים חסרים, המכפלה עלולה ליצור מצבים סופניים שאינם קיימים במערכת המקורית.
</div>

<div class="mt-7 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-amber-50 border border-amber-200 rounded p-5">
<div class="font-bold text-amber-700 mb-3">הבעיה</div>
מסלול במערכת יכול להמשיך, אבל רכיב האוטומט “נתקע” כי אין מעבר מתאים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">הפתרון</div>
משלימים את האוטומט באמצעות מצב מלכודת לא מקבל, ומוסיפים אליו את כל המעברים החסרים.
</div>
</div>

<div class="mt-7 bg-slate-50 border border-slate-200 rounded p-4 text-[21px]">
אחרי השלמה, האוטומט יודע להמשיך לקרוא כל מילה מעל <KatexInline math="2^{AP}" />.
</div>

---

# האלגוריתם

<div class="mt-7 text-right text-[21px] leading-relaxed">
קלט: מערכת מעברים סופית <KatexInline math="TS" /> ותכונת בטיחות רגולרית <KatexInline math="P_{\mathrm{safe}}" />.
</div>

<div class="mt-6 text-right text-[21px] leading-relaxed bg-slate-50 border border-slate-200 rounded p-5">
<ol class="space-y-3">
<li>בונים אוטומט סופי <KatexInline math="\mathcal{A}" /> עבור <KatexInline math="\mathit{BadPref}(P_{\mathrm{safe}})" /> או עבור <KatexInline math="\mathit{MinBadPref}(P_{\mathrm{safe}})" />.</li>
<li>משלימים את האוטומט אם צריך.</li>
<li>בונים את מערכת המכפלה <KatexInline math="TS\times\mathcal{A}" />.</li>
<li>בודקים את הַשְׁמוּרָה: לא מגיעים למצב שבו רכיב האוטומט שייך ל־<KatexInline math="F" />.</li>
<li>אם הַשְׁמוּרָה מופרת, מחזירים את המסלול הסופי כדוגמה נגדית.</li>
</ol>
</div>

---

# שיפור מעשי

<div class="mt-8 text-right text-[24px] leading-relaxed">
כאשר אפשר, עדיף לבנות אוטומט עבור הרישות הרעות המינימליות.
</div>

<div class="mt-8 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3">פחות חיפוש מיותר</div>
האוטומט מקבל בדיוק ברגע שבו ההפרה מתגלה לראשונה.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">דוגמאות נגדיות קצרות</div>
המסלול המוחזר מסתיים בנקודת ההפרה הראשונה, ולא אחרי המשכים לא רלוונטיים.
</div>
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-[22px]">
מבחינה תיאורטית זה שקול; מבחינה אלגוריתמית זה בדרך כלל נוח יותר.
</div>

---

# סיבוכיות

<div class="mt-8 text-right text-[24px] leading-relaxed">
גודל מערכת המכפלה הוא מכפלת הגדלים של המערכת ושל האוטומט.
</div>

<div class="mt-8 text-center text-[34px]" dir="ltr">
<KatexInline display math="O(|TS|\cdot|\mathcal{A}|)" />
</div>

<div class="mt-8 grid grid-cols-2 gap-6 text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
הזיכרון הדרוש הוא ליניארי בגודל המכפלה.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5">
הזמן הדרוש לבדיקת הַשְׁמוּרָה הוא ליניארי בגודל המכפלה.
</div>
</div>

---

# מה לקחת מכאן?

<div class="grid grid-cols-2 gap-6 mt-8 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">תכונת בטיחות רגולרית</div>
הפרות מזוהות על ידי אוטומט סופי שקורא רישות סופיות של עקבות.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3">בדיקה על ידי מכפלה</div>
מכפילים את המערכת באוטומט הרישות הרעות, ובודקים שְׁמוּרָה פשוטה.
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold text-red-700 mb-3">דוגמה נגדית</div>
הגעה למצב מקבל באוטומט נותנת רישא רעה ומסלול סופי שמסביר אותה.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-5">
<div class="font-bold text-amber-700 mb-3">העלות</div>
המחיר הוא גודל המכפלה: <span dir="ltr"><KatexInline math="O(|TS|\cdot|\mathcal{A}|)" /></span>.
</div>
</div>
