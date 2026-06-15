---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 17-verification-of-omega-regular-properties
htmlAttrs:
  dir: rtl
  lang: he
drawings:
  enabled: true
info: |
  ## אימות תכונות ω-רגולריות
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# אימות תכונות <KatexInline math="\omega" />-רגולריות

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# ראשי פרקים

<div class="grid grid-cols-2 gap-5 mt-8 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold text-slate-700 mb-2">תזכורת</div>
בדיקת תכונות בטיחות רגולריות, שפות <KatexInline math="\omega" />-רגולריות, ואוטומטי Büchi.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">הרעיון המרכזי</div>
ייצוג העקבות הרעות באמצעות <span dir="ltr">NBA</span>, ובדיקת חיתוך עם עקבות המערכת.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">תכונות התמדה</div>
רדוקציה מאימות <KatexInline math="\omega" />-רגולרי לבדיקת “בסופו של דבר תמיד”.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2"><span dir="ltr">Nested DFS</span></div>
זיהוי מעגל נגיש המכיל מצב מפר, ובניית דוגמה נגדית.
</div>
</div>

---

# תזכורת: בטיחות רגולרית

<div class="mt-7 text-right text-[19px] leading-relaxed">
עבור תכונת בטיחות רגולרית <KatexInline math="P_{\mathrm{safe}}" />, נתון אוטומט סופי
<KatexInline math="\mathcal{A}" /> שמקבל את הרֵישׁוֹת הרעות:
</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline display math="L(\mathcal{A})=\mathit{BadPref}(P_{\mathrm{safe}})" />
</div>

<div class="mt-8 grid grid-cols-[1fr_auto_1fr] gap-4 items-center text-[21px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800">
מחפשים רישא שמערכת המעברים יכולה לייצר
</div>
<div class="text-[34px] text-slate-500">⇔</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
מחפשים מצב מקבל נגיש במכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline display math="TS\not\models P_{\mathrm{safe}}\iff \mathit{Reach}(TS\times\mathcal{A})\cap F\neq\emptyset" />
</div>

---

# תזכורת: תכונה <KatexInline math="\omega" />-רגולרית

<div class="mt-4 text-right text-[21px] leading-snug">
תכונת זמן ליניארי <KatexInline math="P\subseteq(2^{AP})^\omega" /> נקראת
<span class="font-bold"><KatexInline math="\omega" />-רגולרית</span> אם היא שפה
<KatexInline math="\omega" />-רגולרית.
</div>

<div class="mt-8 text-center text-[31px]" dir="ltr">
<KatexInline display math="P=L_\omega(\mathcal{A})" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
אפשר לתאר אותה באמצעות ביטוי <KatexInline math="\omega" />-רגולרי.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
אפשר לתאר אותה באמצעות אוטומט Büchi.
</div>
</div>

<div class="mt-8 text-right text-[22px] leading-relaxed">
המטרה בהרצאה: לבדוק אלגוריתמית אם <KatexInline math="TS\models P" />.
</div>

---

# תזכורת: מכפלה של מערכת מעברים ואוטומט

<div class="mt-2 grid grid-cols-[1.05fr_0.95fr] gap-4 items-start">

<div>
<div class="text-right text-[18px] leading-snug">
עבור <KatexInline math="TS=\langle S,Act,\to,I,AP,L\rangle" /> ללא מצבים סופניים, ו־
<KatexInline math="\mathcal{A}=\langle Q,2^{AP},\delta,Q_0,F\rangle" /> בלתי חוסם:
</div>

<div class="compact-display mt-2 text-center text-[23px]" dir="ltr">
<KatexInline display math="TS\times\mathcal{A}=\langle S\times Q,Act,\to_\times,I_\times,Q,L_\times\rangle" />
</div>

<div class="mt-2 grid grid-cols-1 gap-2 text-[17px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded px-3 py-2 text-slate-800">
<div class="font-bold mb-1">מעברים</div>
<div class="compact-display" dir="ltr"><KatexInline display math="\frac{s\xrightarrow{\alpha}t\ \land\ p\in\delta(q,L(t))}{\langle s,q\rangle\xrightarrow{\alpha}_\times\langle t,p\rangle}" /></div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded px-3 py-2 text-slate-800">
<div class="font-bold mb-1">מצבי התחלה</div>
<div class="compact-display" dir="ltr"><KatexInline display math="I_\times=\{\langle s_0,q\rangle\mid s_0\in I\ \land\ \exists q_0\in Q_0\ \left(q\in\delta(q_0,L(s_0))\right)\}" /></div>
</div>
</div>

<div class="mt-2 text-right text-[18px] leading-snug">
התיוג במכפלה הוא מצב האוטומט: <span dir="ltr"><KatexInline math="L_\times(\langle s,q\rangle)=\{q\}" /></span>.
</div>
</div>

<div class="relative h-[470px] overflow-hidden">
  <div class="absolute top-[92px] left-1/2 -translate-x-1/2 w-[220px] h-[186px] overflow-hidden">
    <img src="/slide-reference/l18/image36.gif" class="w-[220px] h-[220px] object-cover object-top" style="clip-path: inset(0 0 34px 0);" />
  </div>

  <div class="absolute top-[280px] left-1/2 -translate-x-1/2 text-[25px]" dir="ltr">
    <KatexInline math="TS\times\mathcal{A}" />
  </div>

  <div class="absolute top-[100px] right-[14px] text-[17px] text-blue-700 text-right leading-tight">
    מערכת המעברים<br>מייצרת עקבות
  </div>

  <div class="absolute top-[232px] left-[4px] text-[17px] text-red-700 text-right leading-tight">
    האוטומט עוקב<br>אחרי העקבות
  </div>

  <svg class="absolute left-[18px] top-[140px] w-[154px] h-[114px]" viewBox="0 0 154 114" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow-red-product-reminder" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth">
        <path d="M 0 0 L 8 4 L 0 8 z" fill="#dc2626" />
      </marker>
    </defs>
    <path d="M 20 96 C 42 66, 82 42, 132 26" stroke="#dc2626" stroke-width="5" stroke-linecap="round" marker-end="url(#arrow-red-product-reminder)" />
  </svg>

  <svg class="absolute right-[26px] top-[130px] w-[150px] h-[110px]" viewBox="0 0 150 110" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow-blue-product-reminder" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth">
        <path d="M 0 0 L 8 4 L 0 8 z" fill="#1d4ed8" />
      </marker>
    </defs>
    <path d="M 128 18 C 110 48, 82 76, 34 96" stroke="#1d4ed8" stroke-width="5" stroke-linecap="round" marker-end="url(#arrow-blue-product-reminder)" />
  </svg>

  <div class="absolute left-1/2 -translate-x-1/2 bottom-[72px] w-[90%] bg-[#0f4c81] text-white text-[14px] px-5 py-2 rounded shadow-md text-center leading-tight">
    בכל צעד מתקדמים גם במערכת המעברים וגם באוטומט שקורא את התיוג של המצב החדש.
  </div>
</div>
</div>

<style>
.compact-display :deep(.katex-display) {
  margin: 0.15em 0;
}
</style>

---

# דוגמה: בניית המכפלה

<div class="mt-1 flex flex-col items-center gap-3 text-[16px] leading-snug" dir="ltr">
  <!-- Top row: TS and Automaton -->
  <div class="flex items-center gap-4 justify-center w-full">
    <!-- TS -->
    <div class="bg-blue-50/50 border border-blue-200/60 rounded-xl p-3 w-[320px] h-[165px] flex flex-col justify-between shadow-sm">
      <div class="font-bold text-blue-700 text-sm text-right" dir="rtl">מערכת המעברים (TS)</div>
      <div class="flex-grow flex items-center justify-center -mt-6">
        <TransitionSystemD3 :width="290" :height="140" :auto="false"
          :states="[
            { id: 's0', text: '$s_0$', label: '$\\{a\\}$', initial: true, initialDirection: 'left', initialStroke: '#2563eb', x: 70, y: 70, width: 50, color: '#dbeafe', stroke: '#2563eb', labelX: -12, labelY: 18, textColor: '#1e40af' },
            { id: 's1', text: '$s_1$', label: '$\\{a\\}$', x: 200, y: 70, width: 50, color: '#dbeafe', stroke: '#2563eb', labelX: -12, labelY: 18, textColor: '#1e40af' }
          ]"
          :transitions="[
            { source: 's0', target: 's1', action: '$\\alpha$',  actionY: -12, actionWidth: 60, stroke: '#3b82f6', labelColor: '#1d4ed8' },
            { source: 's1', target: 's1', action: '$\\beta$', loopDirection: '0deg', loopRadius: 85, loopLabelRadius: 70, actionWidth: 52, stroke: '#3b82f6', labelColor: '#1d4ed8' }
          ]"
        />
      </div>
    </div>
    <!-- Operator -->
    <div class="text-[32px] text-slate-400 font-bold select-none">×</div>
    <!-- Automaton -->
    <div class="bg-emerald-50/50 border border-emerald-200/60 rounded-xl p-3 w-[320px] h-[165px] flex flex-col justify-between shadow-sm">
      <div class="font-bold text-emerald-700 text-sm text-right" dir="rtl">אוטומט Büchi (A)</div>
      <div class="flex-grow flex items-center justify-center -mt-6">
        <AutomatonD3 variant="classic" :width="290" :height="140" :arrowSize="4.2" :stateLabelFontSize="15" :transitionLabelFontSize="13"
          :states="[
            { id: 'q0', x: 70, y: 70, label: '$q_0$', initial: true, initialDirection: 'left', initialStroke: '#059669', r: 20, fill: '#d1fae5', stroke: '#059669', textColor: '#065f46' },
            { id: 'q1', x: 200, y: 70, label: '$q_1$', accepting: true, r: 20, fill: '#d1fae5', stroke: '#059669', textColor: '#065f46' }
          ]"
          :transitions="[
            { source: 'q0', target: 'q1', label: '$\\{a\\}$', labelY: -15, stroke: '#10b981', strokeWidth: 2.5, labelColor: '#047857' },
            { source: 'q1', target: 'q1', label: '$\\{a\\}$', loopDirection: '0deg', 
              loopRadius: 85, labelX: 15, stroke: '#10b981', strokeWidth: 2.5, labelColor: '#047857' },
          ]"
        />
      </div>
    </div>
  </div>


  <!-- Bottom row: Product -->
  <div class="bg-slate-50/50 border border-slate-200/60 rounded-xl p-3 w-[420px] h-[165px] flex flex-col justify-between shadow-sm">
    <div class="font-bold text-slate-700 text-sm text-right" dir="rtl">המכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span> הנגישה</div>
    <div class="flex-grow flex items-center justify-center -mt-6">
      <TransitionSystemD3 :width="390" :height="140" :auto="false"
        :states="[
          { id: 'p0', text: '$\\langle s_0,q_1\\rangle$', initial: true, initialDirection: 'left', initialStroke: '#64748b', x: 100, y: 70, width: 85, color: '#f8fafc', stroke: '#64748b', textColor: '#334155' },
          { id: 'p1', text: '$\\langle s_1,q_1\\rangle$', x: 270, y: 70, width: 85, color: '#fee2e2', stroke: '#ef4444', textColor: '#991b1b' }
        ]"
        :transitions="[
          { source: 'p0', target: 'p1', action: '$\\alpha$', actionY: -12, actionWidth: 60, stroke: '#64748b', labelColor: '#334155' },
          { source: 'p1', target: 'p1', action: '$\\beta$', loopDirection: '0deg', loopRadius: 95, loopLabelRadius: 80, actionWidth: 48, stroke: '#ef4444', labelColor: '#991b1b' }
        ]"
      />
    </div>
  </div>
</div>

<div class="mt-3 grid grid-cols-3 gap-3 text-[17px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-right text-blue-900">
המערכת עוברת מ־<span dir="ltr"><KatexInline math="s_0" /></span> אל <span dir="ltr"><KatexInline math="s_1" /></span>, ואז נשארת ב־<span dir="ltr"><KatexInline math="s_1" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-right text-emerald-900">
בכל מצב קוראים את התיוג <span dir="ltr"><KatexInline math="\{a\}" /></span>, ולכן האוטומט מגיע ל־<span dir="ltr"><KatexInline math="q_1" /></span> ונשאר בו.
</div>
<div class="bg-red-50 border border-red-200 rounded p-3 text-right text-red-900">
במכפלה מתקבל מעגל על <span dir="ltr"><KatexInline math="\langle s_1,q_1\rangle" /></span>; זהו ביקור חוזר במצב מקבל של האוטומט.
</div>
</div>

---

# מה מייצגת ריצה במכפלה?

<div class="mt-6 grid grid-cols-3 gap-4 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">ריצת מערכת</div>
<div dir="ltr"><KatexInline math="s_0s_1s_2\cdots" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">עקבה</div>
<div dir="ltr"><KatexInline math="L(s_0)L(s_1)L(s_2)\cdots" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2">ריצת אוטומט</div>
<div dir="ltr"><KatexInline math="q_0q_1q_2\cdots" /></div>
</div>
</div>

<div class="mt-9 text-center text-[28px]" dir="ltr">
<KatexInline display math="\langle s_0,q_1\rangle\langle s_1,q_2\rangle\langle s_2,q_3\rangle\cdots" />
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-slate-800 text-right text-[21px] leading-relaxed">
התיוג במכפלה הוא מצבי האוטומט:
<span dir="ltr"><KatexInline math="L_\times(\langle s,q\rangle)=\{q\}" /></span>.
לכן צופה בעקבה של המכפלה יכול לדעת אם המילה התקבלה או לא, לפי ביקורים במצבי
<span dir="ltr"><KatexInline math="F" /></span>.
</div>

---

# מה מחפשים כשבודקים <KatexInline math="TS\models P" />?

<div class="mt-8 text-right text-[23px] leading-relaxed">
במקום להוכיח ישירות שכל עקבה של <KatexInline math="TS" /> נמצאת ב־<KatexInline math="P" />,
נחפש דוגמה נגדית:
</div>

<div class="mt-3 text-center text-[26px]" dir="ltr">
<KatexInline display math="TS\not\models P\iff \mathit{Traces}(TS)\cap\left((2^{AP})^\omega\setminus P\right)\neq\emptyset" />
</div>

<div class="mt-4 text-right text-[21px] leading-snug">
לכן נשתמש באוטומט Büchi עבור <span class="font-bold">העקבות הרעות</span>:
</div>

<div class="mt-3 text-center text-[26px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-slate-800 text-[20px] leading-snug">
אם קיימת עקבה של המערכת שמתקבלת על ידי <KatexInline math="\mathcal{A}" />, מצאנו ריצה שמפרה את התכונה.
</div>

---

# למה לא להשתמש באוטומט של <KatexInline math="P" />?

<div class="mt-5 text-right text-[21px] leading-snug">
אנחנו רוצים לעבוד עם המכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>.
כל ריצה שלה היא שילוב של ריצה של המערכת עם ריצה אחת של האוטומט על העקבה שלה.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[19px] leading-snug">
<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2">אם משתמשים באוטומט של <KatexInline math="P" /></div>
לאותה ריצה של המערכת יכולות להיות כמה ריצות של האוטומט.
לכן ריצה אחת לא-מקבלת במכפלה לא מוכיחה שהעקבה אינה ב־<KatexInline math="P" />.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">מה כן ניתן לבדוק ריצה־ריצה?</div>
אפשר לבדוק קיום של ריצה מקבלת במכפלה. לכן נשתמש באוטומט שמקבל את העקבות הרעות.
</div>
</div>

<div class="mt-6 text-center text-[26px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-5 bg-red-50 border border-red-200 rounded p-3 text-red-900 text-[20px] leading-snug">
אז ריצה מקבלת אחת של <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>
היא בדיוק ריצה של המערכת שמפרה את <KatexInline math="P" />.
</div>

---

# הרעיון האלגוריתמי

<div class="mt-6 text-center text-[24px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr_auto_1fr] gap-3 items-center text-[20px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800">
בונים מכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
מחפשים ריצה של <KatexInline math="TS" /> ש־<KatexInline math="\mathcal{A}" /> מקבל את העקבה שלה
<span class="block mt-1 text-[13px] leading-tight text-blue-800">(בוחנים כל ריצה של <KatexInline math="TS\times\mathcal{A}" /> בנפרד)</span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
כלומר ריצה עם אינסוף מצבים שהתיוג שלהם מכיל מצב מקבל של <KatexInline math="\mathcal{A}" />
<span class="block mt-1 text-[13px] leading-tight text-red-800">(כי התיוג ב־<KatexInline math="TS\times\mathcal{A}" />  הוא המצב של <KatexInline math="\mathcal{A}" />)</span>
</div>
</div>

<div class="mt-9 text-center text-[21px]" dir="ltr">
<KatexInline display math="\begin{array}{rcl}
TS\not\models P &amp;\iff&amp; \mathit{Traces}(TS)\cap L_\omega(\mathcal{A})\neq\emptyset\\[6pt]
&amp;\iff&amp; \exists \sigma\in\mathit{Traces}(TS\times\mathcal{A})\
\left(\underset{\infty}{\exists} i\ \left(\sigma[i]\subseteq F\right)\right)
\end{array}" />
</div>

---

# תכונת התמדה

<div class="absolute left-[24px] top-[58px] pointer-events-none">
<InclusionDiagramD3 :width="330" :height="145" :fontSize="12"
  :sets="[
    { label: 'תכונות זמן לינארי', fill: '#3b82f6', stroke: '#bfdbfe', textColor: '#ffffff', Y: -2 },
    { label: 'תכונות חַיּוּת', fill: '#10b981', stroke: '#a7f3d0', textColor: '#ffffff', Y: 0 },
    { label: 'תכונות התמדה', fill: '#f59e0b', stroke: '#fde68a', textColor: '#4a2c00', Y: -4 }
  ]"
/>
</div>

<div class="mt-8 text-right text-[23px] leading-relaxed">
תכונת התמדה היא תכונה מהצורה:
</div>

<div class="mt-5 text-center text-[32px]" dir="ltr">
<KatexInline display math="\text{Eventually Always }\Phi" />
</div>

<div class="mt-6 text-center text-[29px]" dir="ltr">
<KatexInline display math="P_{\mathrm{pers}}(\Phi)=\{\sigma\in(2^{AP})^\omega\mid \exists i\ge 0\ \left(\forall j\ge i\ \left(\sigma[j]\models\Phi\right)\right)\}" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[19px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
אחרי רישא סופית כל המצבים מקיימים <KatexInline math="\Phi" />.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
הפרה היא ביקור באינסוף מצבים שמקיימים <KatexInline math="\neg\Phi" />.
</div>
</div>

---

# היחס לתכונות שמורה

<div class="mt-2 text-right text-[18px] leading-snug">
נשווה בין שתי צורות של תכונות:
</div>

<div class="mt-2 grid grid-cols-2 gap-3 text-[18px]">
<div class="bg-blue-50 border border-blue-200 rounded px-3 py-1 text-center text-blue-900" dir="rtl">
<div class="font-bold text-blue-800" dir="ltr"><KatexInline math="P_{\mathrm{inv}}(\Phi)" /></div>
<div dir="ltr"><KatexInline display math="\{\sigma\mid \forall i\ge 0:\ \sigma[i]\models\Phi\}" /></div>
<div class="text-[14px] leading-tight text-blue-800">כלומר: <span dir="ltr"><KatexInline math="\text{Always }\Phi" /></span></div>
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded px-3 py-1 text-center text-emerald-900" dir="rtl">
<div class="font-bold text-emerald-800" dir="ltr"><KatexInline math="P_{\mathrm{per}}(\Phi)" /></div>
<div dir="ltr"><KatexInline display math="\{\sigma\mid \exists k\ge 0\ \forall i\ge k:\ \sigma[i]\models\Phi\}" /></div>
<div class="text-[14px] leading-tight text-emerald-800">כלומר: <span dir="ltr"><KatexInline math="\text{Eventually Always }\Phi" /></span></div>
</div>
</div>

<div class="mt-2 space-y-2 text-right text-[15px] leading-tight" dir="rtl">
<div v-click="1" class="bg-slate-50 border border-slate-200 rounded px-3 py-2" dir="rtl">
<div class="flex items-start gap-3">
<div class="font-bold">האם <span dir="ltr"><KatexInline math="P_{\mathrm{per}}(\Phi)=P_{\mathrm{inv}}(\Phi)" /></span>?</div>
<div v-click="2" class="text-red-800 font-bold">לא, אלא אם <KatexInline math="\Phi" /> טריוויאלית.</div>
</div>
<div v-click="3" class="mt-1">
הוכחה: אם <KatexInline math="\Phi" /> אינה תמיד אמת ואינה תמיד שקר, קיימות אותיות
<span dir="ltr"><KatexInline math="A\not\models\Phi" /></span> ו־
<span dir="ltr"><KatexInline math="B\models\Phi" /></span>.
אז <span dir="ltr"><KatexInline math="AB^\omega\in P_{\mathrm{per}}(\Phi)" /></span>
כי החל ממיקום 1 מתקיים <KatexInline math="\Phi" />, אבל
<span dir="ltr"><KatexInline math="AB^\omega\notin P_{\mathrm{inv}}(\Phi)" /></span>
כי האות הראשונה מפרה את <KatexInline math="\Phi" />.
</div>
</div>

<div v-click="4" class="bg-slate-50 border border-slate-200 rounded px-3 py-2" dir="rtl">
<div class="flex items-start gap-3">
<div class="font-bold">האם קיימות <span dir="ltr"><KatexInline math="\Phi_{\mathrm{inv}},\Phi_{\mathrm{per}}" /></span> כך ש־<span dir="ltr"><KatexInline math="P_{\mathrm{per}}(\Phi_{\mathrm{per}})=P_{\mathrm{inv}}(\Phi_{\mathrm{inv}})" /></span>?</div>
<div v-click="5" class="text-emerald-800 font-bold">כן, רק טריוויאליות.</div>
</div>
<div v-click="6" class="mt-1">
נסמן <span dir="ltr"><KatexInline math="\Sigma=2^{AP}" /></span>,
<span dir="ltr"><KatexInline math="X=\{A\mid A\models\Phi_{\mathrm{inv}}\}" /></span>,
<span dir="ltr"><KatexInline math="Y=\{A\mid A\models\Phi_{\mathrm{per}}\}" /></span>.
אז <span dir="ltr"><KatexInline math="P_{\mathrm{inv}}=X^\omega" /></span> ו־
<span dir="ltr"><KatexInline math="P_{\mathrm{per}}=\Sigma^*Y^\omega" /></span>.
אם <span dir="ltr"><KatexInline math="Y=\emptyset" /></span>, שוויון מחייב
<span dir="ltr"><KatexInline math="X=\emptyset" /></span>.
אחרת, לכל <span dir="ltr"><KatexInline math="A\in\Sigma" /></span> ולכל <span dir="ltr"><KatexInline math="B\in Y" /></span>,
<span dir="ltr"><KatexInline math="AB^\omega\in\Sigma^*Y^\omega=X^\omega" /></span>, ולכן
<span dir="ltr"><KatexInline math="A\in X" /></span>. מכאן <span dir="ltr"><KatexInline math="X=\Sigma" /></span>, ואז שוויון מחייב
<span dir="ltr"><KatexInline math="Y=\Sigma" /></span>.
</div>
</div>
</div>

---

# תכונת ההתמדה של האוטומט

<div class="mt-5 text-right text-[21px] leading-snug">
במכפלה <KatexInline math="TS\times\mathcal{A}" /> הפסוקים האטומיים הם מצבי האוטומט
<KatexInline math="Q" />.
נסמן ב־<KatexInline math="P_{\mathrm{pers}}(\mathcal{A})" /> את תכונת ההתמדה שמתקבלת מהצבת
<KatexInline math="\Phi=\neg F" />.
</div>

<div class="mt-5 text-center text-[29px]" dir="ltr">
<KatexInline display math="P_{\mathrm{pers}}(\mathcal{A})=\text{Eventually Always }\neg F" />
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="\neg F=\bigwedge_{q\in F}\neg q" />
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-4 text-slate-800 text-[21px] leading-snug">
כלומר: החל מרגע מסוים, הריצה במכפלה אינה מבקרת יותר במצבים מקבלים של האוטומט.
</div>

---

# משפט: אימות תכונות <KatexInline math="\omega" />-רגולריות

<div class="mt-5 text-right text-[20px] leading-relaxed">
יהיו <KatexInline math="TS" /> מערכת מעברים סופית ללא מצבים סופניים,
<KatexInline math="P" /> תכונה <KatexInline math="\omega" />-רגולרית,
ו־<KatexInline math="\mathcal{A}" /> אוטומט Büchi בלתי חוסם <span class="text-red-600 font-bold">למילים שאינן מקיימות את <KatexInline math="P" /></span>, כלומר
</div>

<div class="mt-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-5 text-right text-[21px] leading-relaxed">
אז התנאים הבאים שקולים:
</div>

<div class="mt-4 grid grid-cols-[0.8fr_1.35fr_1fr] gap-4 text-[19px]">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-center text-emerald-900" dir="ltr">
<KatexInline math="TS\models P" />
</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-center text-blue-900" dir="ltr">
<KatexInline math="\mathit{Traces}(TS)\cap L_\omega(\mathcal{A})=\emptyset" />
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4 text-center text-amber-900" dir="ltr">
<KatexInline math="TS\times\mathcal{A}\models P_{\mathrm{pers}}(\mathcal{A})" />
</div>
</div>

<div class="mt-8 text-right text-[21px] leading-relaxed">
אימות כללי של תכונה <KatexInline math="\omega" />-רגולרית מצטמצם לבדיקת התמדה במכפלה.
</div>

---

# הוכחת המשפט: הכיוון של דוגמה נגדית

<div class="mt-6 text-right text-[21px] leading-relaxed">
נניח ש־<KatexInline math="TS\times\mathcal{A}\not\models P_{\mathrm{pers}}(\mathcal{A})" />.
אז קיימת ריצה במכפלה שמבקרת במצבי <KatexInline math="F" /> אינסוף פעמים:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="\langle s_0,q_1\rangle\langle s_1,q_2\rangle\langle s_2,q_3\rangle\cdots" />
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
ההטלה על הרכיב הראשון היא ריצה של <KatexInline math="TS" />.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
הרכיב השני הוא ריצת Büchi מקבלת על העקבה של אותה ריצה.
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathit{trace}(s_0s_1s_2\cdots)\in\mathit{Traces}(TS)\cap L_\omega(\mathcal{A})" />
</div>

<div v-click>
<div class="absolute left-[50px] bottom-[100px] text-red-800 font-bold text-[27px] rotate-[0deg]">
האומנם?
</div>
<svg class="absolute left-[120px] bottom-[130px] w-[120px] h-[74px] pointer-events-none" viewBox="0 0 120 74">
  <defs>
    <marker id="proof-s0-arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
      <path d="M0,0 L9,4.5 L0,9 Z" fill="#dc2626" />
    </marker>
  </defs>
  <path d="M6 66 C34 28 66 20 112 7" fill="none" stroke="#dc2626" stroke-width="2" stroke-linecap="round" marker-end="url(#proof-s0-arrow)" />
</svg>
</div>

---

# הוכחת המשפט: הכיוון של אי קיום התכונה

<div class="mt-4 text-right text-[19px] leading-relaxed">
נניח ש־<KatexInline math="TS \not\models P" />. כלומר, קיימת עקבה של המערכת שאינה מקיימת את התכונה:
</div>

<div class="mt-2 text-center text-[25px]" dir="ltr">
<KatexInline display math="\mathit{trace}(s_0s_1s_2\cdots) \in (2^{AP})^\omega \setminus P = L_\omega(\mathcal{A})" />
</div>

<div class="mt-4 text-right text-[19px] leading-relaxed">
קיימת ריצה מקבלת של האוטומט <KatexInline math="q_0q_1q_2\cdots" /> על עקבה זו. נבנה ריצה במכפלה:
</div>

<div class="mt-4 grid grid-cols-2 gap-4 text-[17px] text-right leading-snug">
<div class="bg-blue-50/50 border border-blue-200 rounded-xl p-3 shadow-sm text-blue-900">
<div class="font-bold text-blue-800 mb-1">מצב ההתחלה של המכפלה</div>
מכיוון ש־<KatexInline math="s_0 \in I" /> ו־<KatexInline math="q_1 \in \delta(q_0, L(s_0))" />, מתקיים:
<div class="text-center mt-1" dir="ltr"><KatexInline math="\langle s_0, q_1\rangle \in I_\times" /></div>
</div>

<div class="bg-emerald-50/50 border border-emerald-200 rounded-xl p-3 shadow-sm text-emerald-900">
<div class="font-bold text-emerald-800 mb-1">מעברים במכפלה</div>
לכל <KatexInline math="i \ge 0" />, מכיוון ש־<KatexInline math="s_i \xrightarrow{\alpha_{i+1}} s_{i+1}" /> ו־<KatexInline math="q_{i+2} \in \delta(q_{i+1}, L(s_{i+1}))" />, יש מעבר:
<div class="text-center mt-1" dir="ltr"><KatexInline math="\langle s_i, q_{i+1}\rangle \xrightarrow{\alpha_{i+1}}_\times \langle s_{i+1}, q_{i+2}\rangle" /></div>
</div>
</div>

<div class="mt-4 bg-slate-50/50 border border-slate-200 rounded-xl p-3 text-slate-800 text-right text-[18px] leading-relaxed shadow-sm">
קיבלנו ריצה חוקית במכפלה <KatexInline math="\langle s_0,q_1\rangle\langle s_1,q_2\rangle\langle s_2,q_3\rangle\cdots" />.
<div class="mt-1">
מכיוון שריצת האוטומט מקבלת, הרכיב השני מבקר ב־<KatexInline math="F" /> אינסוף פעמים.
לכן הריצה במכפלה מבקרת אינסוף פעמים במצבי קבלה, ומכאן ש־<KatexInline math="TS\times\mathcal{A}\not\models P_{\mathrm{pers}}(\mathcal{A})" />.
</div>
</div>

---

# דוגמה: “אינסוף פעמים ירוק”

<div class="grid grid-cols-2 gap-x-10 gap-y-4 mt-6 justify-center w-fit mx-auto" dir="ltr">
  <!-- Top Row: Automata -->
  <!-- Automaton for Property P -->
  <div class="bg-emerald-50/50 border border-emerald-200/60 rounded-xl p-3 w-[420px] h-[200px] flex items-center justify-center shadow-sm">
    <AutomatonD3 variant="classic" :width="390" :height="180" :arrowSize="4.2" :stateLabelFontSize="15" :transitionLabelFontSize="13"
      :states="[
        { id: 'p0', x: 90, y: 90, label: '$p_0$', initial: true, initialDirection: 'left', initialStroke: '#047857', r: 22, fill: '#d1fae5', stroke: '#047857', textColor: '#065f46' },
        { id: 'p1', x: 260, y: 90, label: '$p_1$', accepting: true, r: 22, fill: '#d1fae5', stroke: '#047857', textColor: '#065f46' }
      ]"
      :transitions="[
        { source: 'p0', target: 'p0', label: '$\\neg green$', loopDirection: '-90deg', labelY: -10, labelWidth: 90, stroke: '#10b981', strokeWidth: 2.5, labelColor: '#047857' },
        { source: 'p0', target: 'p1', label: '$green$', curve: -0.22, labelY: -10, labelWidth: 70, stroke: '#10b981', strokeWidth: 2.5, labelColor: '#047857' },
        { source: 'p1', target: 'p0', label: '$\\neg green$', curve: -0.22, labelY: 10, labelWidth: 90, stroke: '#10b981', strokeWidth: 2.5, labelColor: '#047857' },
        { source: 'p1', target: 'p1', label: '$green$', loopDirection: '-90deg', labelY: -10, labelWidth: 70, stroke: '#10b981', strokeWidth: 2.5, labelColor: '#047857' }
      ]"
    />
  </div>

  <!-- Automaton for Complement A -->
  <div class="bg-red-50/50 border border-red-200/60 rounded-xl p-3 w-[420px] h-[200px] flex items-center justify-center shadow-sm">
    <AutomatonD3 variant="classic" :width="390" :height="180" :arrowSize="4.2" :stateLabelFontSize="15" :transitionLabelFontSize="13"
      :states="[
        { id: 'q0', x: 70, y: 90, label: '$q_0$', initial: true, initialDirection: 'left', initialStroke: '#dc2626', r: 20, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
        { id: 'q1', x: 195, y: 90, label: '$q_1$', accepting: true, r: 20, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
        { id: 'q2', x: 320, y: 90, label: '$q_2$', r: 20, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' }
      ]"
      :transitions="[
        { source: 'q0', target: 'q0', label: '$true$', loopDirection: '-90deg', labelY: -10, labelWidth: 60, stroke: '#ef4444', strokeWidth: 2.5, labelColor: '#991b1b' },
        { source: 'q0', target: 'q1', label: '$\\neg green$', labelY: -10, labelWidth: 95, stroke: '#ef4444', strokeWidth: 2.5, labelColor: '#991b1b' },
        { source: 'q1', target: 'q1', label: '$\\neg green$', loopDirection: '-90deg', labelY: -10, labelWidth: 95, stroke: '#ef4444', strokeWidth: 2.5, labelColor: '#991b1b' },
        { source: 'q1', target: 'q2', label: '$green$', labelY: -10, labelWidth: 70, stroke: '#ef4444', strokeWidth: 2.5, labelColor: '#991b1b' },
        { source: 'q2', target: 'q2', label: '$true$', loopDirection: '-90deg', labelY: -10, labelWidth: 60, stroke: '#ef4444', strokeWidth: 2.5, labelColor: '#991b1b' }
      ]"
    />
  </div>

  <!-- Bottom Row: Descriptions -->
  <!-- Description for P -->
  <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-4 w-[420px] text-emerald-950 text-right text-[16px] leading-relaxed shadow-sm" dir="rtl">
  <div class="font-bold text-emerald-800 text-[18px] mb-2">
    התכונה שרוצים לבדוק (<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A})=P" /></span>)
  </div>
  <div class="text-center text-[22px] mb-2 font-mono text-emerald-800" dir="ltr">
      <KatexInline math="\text{Always Eventually }green" />
    </div>
    <div class="text-[14px] text-emerald-900 leading-snug">
      השפה היא כל המילים שבהן הצבע ירוק מופיע אינסוף פעמים (תכונת חַיּוּת).
    </div>
  </div>

  <!-- Description for A -->
  <div class="bg-red-50 border border-red-200 rounded-xl p-4 w-[420px] text-red-950 text-right text-[16px] leading-relaxed shadow-sm" dir="rtl">
    <div class="font-bold text-red-800 text-[18px] mb-2">אוטומט המשלים 
    (<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A})=(2^{AP})^{\omega} \setminus P"/>
    </span>)
    </div>
    <div class="text-center text-[22px] mb-2 font-mono text-red-800" dir="ltr">
      <KatexInline math="\text{Eventually Always }\neg green" />
    </div>
    <div class="text-[14px] text-red-900 leading-snug">
      השפה המשלימה (העקבות הרעות) שבה החל מרגע מסוים אין יותר ירוק.
    </div>
  </div>
</div>

---

# דוגמה: מערכת שמקיימת את התכונה

<div class="mt-2 grid grid-cols-[1fr_0.78fr] gap-2 text-[13px] leading-snug">
<div class="bg-blue-50/50 border border-blue-200 rounded px-2 py-1 text-blue-950">
<div class="font-bold text-blue-800 mb-1">המערכת</div>
<div class="-mt-9 -mb-11" dir="ltr">
<TransitionSystemD3 :width="240" :height="160" :auto="false"
  :states="[
    { id: 'simple_ts_r', text: '$r$', label: '$\\{red\\}$', initial: true, initialDirection: 'left', initialStroke: '#dc2626', x: 20, y: 66, width: 50, color: '#fee2e2', stroke: '#dc2626', labelX: -12, labelY: 18, textColor: '#991b1b' },
    { id: 'simple_ts_g', text: '$g$', label: '$\\{green\\}$', x: 175, y: 66, width: 50, color: '#dcfce7', stroke: '#16a34a', labelX: -18, labelY: 18, textColor: '#14532d' }
  ]"
  :transitions="[
    { source: 'simple_ts_r', target: 'simple_ts_g', action: '$switch$', curve: -0.25, actionY: -14, actionWidth: 60 },
    { source: 'simple_ts_g', target: 'simple_ts_r', action: '$switch$', curve: -0.25, actionY: 16, actionWidth: 60 }
  ]"
/>
</div>
</div>

<div class="bg-red-50/50 border border-red-200 rounded px-2 py-1 text-red-950">
<div class="font-bold text-red-800 mb-1">האוטומט למשלים</div>
<div class="-mt-3 -mb-5" dir="ltr">
<AutomatonD3 variant="classic" :width="280" :height="115" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="11"
  :states="[
    { id: 'sq0', x: 45, y: 82, label: '$q_0$', initial: true, initialDirection: 'left', initialStroke: '#dc2626', r: 19, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', labelWidth: 48 },
    { id: 'sq1', x: 140, y: 82, label: '$q_1$', accepting: true, r: 19, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', labelWidth: 48 },
    { id: 'sq2', x: 235, y: 82, label: '$q_2$', r: 19, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', labelWidth: 48 }
  ]"
  :transitions="[
    { source: 'sq0', target: 'sq0', label: '$true$', loopDirection: '-90deg', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 48 },
    { source: 'sq0', target: 'sq1', label: '$\\neg green$', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 72 },
    { source: 'sq1', target: 'sq1', label: '$\\neg green$', loopDirection: '-90deg', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 72 },
    { source: 'sq1', target: 'sq2', label: '$green$', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 54 },
    { source: 'sq2', target: 'sq2', label: '$true$', loopDirection: '-90deg', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 48 }
  ]"
/>
</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-2 col-span-2 text-slate-950">
<div class="font-bold text-slate-800 mb-1">המכפלה</div>
<div class="-mt-8 -mb-10" dir="ltr">
<TransitionSystemD3 :width="760" :height="205" :auto="false"
  :states="[
    { id: 'simple_r0', text: '$\\langle r,q_0\\rangle$', label: '$\\{q_0\\}$', initial: true, initialDirection: 'left', initialStroke: '#64748b', x: 145, y: 36, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: -18, labelY: 18, textColor: '#334155' },
    { id: 'simple_r1', text: '$\\langle r,q_1\\rangle$', label: '$\\{q_1\\}$', initial: true, initialDirection: 'left', initialStroke: '#e11d48', x: 145, y: 115, width: 82, color: '#fff1f2', stroke: '#e11d48', labelX: -18, labelY: 18, textColor: '#991b1b' },
    { id: 'simple_g0', text: '$\\langle g,q_0\\rangle$', label: '$\\{q_0\\}$', x: 325, y: 36, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: -18, labelY: 18, textColor: '#334155' },
    { id: 'simple_g2', text: '$\\langle g,q_2\\rangle$', label: '$\\{q_2\\}$', x: 325, y: 115, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: -18, labelY: 18, textColor: '#334155' },
    { id: 'simple_r2', text: '$\\langle r,q_2\\rangle$', label: '$\\{q_2\\}$', x: 505, y: 115, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: -18, labelY: 18, textColor: '#334155' }
  ]"
  :transitions="[
    { source: 'simple_r0', target: 'simple_g0', action: '', curve: -0.15, actionY: -10, actionWidth: 42 },
    { source: 'simple_g0', target: 'simple_r0', action: '', curve: -0.15, actionY: 14, actionWidth: 42 },
    { source: 'simple_g0', target: 'simple_r1', action: '', curve: 0, actionX: -8, actionY: 2, actionWidth: 42 },
    { source: 'simple_r1', target: 'simple_g2', action: '', curve: 0, actionY: -10, actionWidth: 42 },
    { source: 'simple_g2', target: 'simple_r2', action: '', curve: -0.15, actionY: -10, actionWidth: 42 },
    { source: 'simple_r2', target: 'simple_g2', action: '', curve: -0.15, actionY: 14, actionWidth: 42 }
  ]"
/>
</div>
</div>
</div>

<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900 text-[14px] leading-snug">
יש מצב מקבל נגיש, למשל <span dir="ltr"><KatexInline math="\langle r,q_1\rangle" /></span>, אבל אין ממנו מעגל שמבקר במצבי קבלה אינסוף פעמים. לכן אין ריצה בעייתית, ומתקיים
<span dir="ltr"><KatexInline math="TS\models\text{Always Eventually }green" /></span>.
</div>

---

# דוגמה: מערכת שמפרה את התכונה

<div class="mt-2 grid grid-cols-[1fr_0.78fr] gap-2 text-[13px] leading-snug">
<div class="bg-blue-50/50 border border-blue-200 rounded px-2 py-1 text-blue-950">
<div class="font-bold text-blue-800 mb-1">המערכת</div>
<div class="-mt-9 -mb-3" dir="ltr">
<TransitionSystemD3 :width="240" :height="118" :auto="false"
  :states="[
    { id: 'bad_ts_r', text: '$r$', label: '$\\{red\\}$', initial: true, initialDirection: 'left', initialStroke: '#dc2626', x: 15, y: 46, width: 50, color: '#fee2e2', stroke: '#dc2626', labelX: -12, labelY: 18, textColor: '#991b1b' },
    { id: 'bad_ts_g', text: '$g$', label: '$\\{green\\}$', x: 155, y: 46, width: 50, color: '#dcfce7', stroke: '#16a34a', labelX: -18, labelY: 18, textColor: '#14532d' },
    { id: 'bad_ts_off', text: '$off$', label: '$\\{\\}$', x: 285, y: 46, width: 54, color: '#f1f5f9', stroke: '#64748b', labelX: 24, labelY: 18, textColor: '#334155' }
  ]"
  :transitions="[
    { source: 'bad_ts_r', target: 'bad_ts_g', action: '$sw$', curve: -0.25, actionY: -12, actionWidth: 42 },
    { source: 'bad_ts_g', target: 'bad_ts_r', action: '$sw$', curve: -0.25, actionY: 14, actionWidth: 42 },
    { source: 'bad_ts_g', target: 'bad_ts_off', action: '$fail$', actionY: -10, actionWidth: 48 },
    { source: 'bad_ts_off', target: 'bad_ts_off', action: '$stay$', loopDirection: '90deg', loopRadius: 62, loopLabelRadius: 28, actionWidth: 48, actionY: 27}
  ]"
/>
</div>
</div>

<div class="bg-red-50/50 border border-red-200 rounded px-2 py-1 text-red-950">
<div class="font-bold text-red-800 mb-1">האוטומט למשלים</div>
<div class="-mt-3 -mb-2" dir="ltr">
<AutomatonD3 variant="classic" :width="280" :height="118" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="11"
  :states="[
    { id: 'bq0', x: 45, y: 82, label: '$q_0$', initial: true, initialDirection: 'left', initialStroke: '#dc2626', r: 19, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', labelWidth: 48 },
    { id: 'bq1', x: 140, y: 82, label: '$q_1$', accepting: true, r: 19, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', labelWidth: 48 },
    { id: 'bq2', x: 235, y: 82, label: '$q_2$', r: 19, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', labelWidth: 48 }
  ]"
  :transitions="[
    { source: 'bq0', target: 'bq0', label: '$true$', loopDirection: '-90deg', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 48 },
    { source: 'bq0', target: 'bq1', label: '$\\neg green$', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 72 },
    { source: 'bq1', target: 'bq1', label: '$\\neg green$', loopDirection: '-90deg', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 72 },
    { source: 'bq1', target: 'bq2', label: '$green$', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 54 },
    { source: 'bq2', target: 'bq2', label: '$true$', loopDirection: '-90deg', labelY: -8, stroke: '#ef4444', labelColor: '#991b1b', labelWidth: 48 }
  ]"
/>
</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded px-2 py-1 col-span-2 text-slate-950">
<div class="font-bold text-slate-800 mb-1">המכפלה</div>
<div class="-mt-10 -mb-10 h-[270px] scale-[.9] origin-top mx-auto w-fit" dir="ltr">
<TransitionSystemD3 :width="760" :height="300" :auto="false"
  :highlightedStateIds="['bad_r0', 'bad_g0', 'bad_o1']"
  :highlightedTransitionIds="['bad_r0_g0', 'bad_g0_o1', 'bad_o1_loop']"
  highlightColor="#dc2626"
  :highlightArrowheadScale="0.65"
  :states="[
    { id: 'bad_r0', text: '$\\langle r,q_0\\rangle$', label: '$\\{q_0\\}$', initial: true, initialDirection: 'left', initialStroke: '#64748b', x: 95, y: 46, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: 20, labelY: 18, textColor: '#334155' },
    { id: 'bad_g0', text: '$\\langle g,q_0\\rangle$', label: '$\\{q_0\\}$', x: 275, y: 46, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: 20, labelY: 18, textColor: '#334155' },
    { id: 'bad_o0', text: '$\\langle off,q_0\\rangle$', label: '$\\{q_0\\}$', x: 530, y: 46, width: 98, color: '#f8fafc', stroke: '#64748b', labelX: 30, labelY: 18, textColor: '#334155' },
    { id: 'bad_r1', text: '$\\langle r,q_1\\rangle$', label: '$\\{q_1\\}$', initial: true, initialDirection: 'left', initialStroke: '#e11d48', x: 95, y: 126, width: 82, color: '#fff1f2', stroke: '#e11d48', labelX: 20, labelY: 18, textColor: '#991b1b' },
    { id: 'bad_o1', text: '$\\langle off,q_1\\rangle$', label: '$\\{q_1\\}$', x: 530, y: 126, width: 98, color: '#fff1f2', stroke: '#e11d48', labelX: 30, labelY: 18, highlightFill: '#fee2e2', textColor: '#991b1b' },
    { id: 'bad_r2', text: '$\\langle r,q_2\\rangle$', label: '$\\{q_2\\}$', x: 95, y: 206, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: 20, labelY: 18, textColor: '#334155' },
    { id: 'bad_g2', text: '$\\langle g,q_2\\rangle$', label: '$\\{q_2\\}$', x: 275, y: 206, width: 82, color: '#f8fafc', stroke: '#64748b', labelX: 20, labelY: 18, textColor: '#334155' },
    { id: 'bad_o2', text: '$\\langle off,q_2\\rangle$', label: '$\\{q_2\\}$', x: 530, y: 206, width: 98, color: '#f8fafc', stroke: '#64748b', labelX: 30, labelY: 18, textColor: '#334155' }
  ]"
  :transitions="[
    { id: 'bad_r0_g0', source: 'bad_r0', target: 'bad_g0', action: '', curve: -0.18, actionY: -12, actionWidth: 42 },
    { source: 'bad_g0', target: 'bad_r0', action: '', curve: -0.18, actionY: 16, actionWidth: 42 },
    { source: 'bad_g0', target: 'bad_r1', action: '', curve: 0, actionX: -10, actionY: 2, actionWidth: 42 },
    { source: 'bad_g0', target: 'bad_o0', action: '', curve: -0.12, actionY: -10, actionWidth: 42 },
    { id: 'bad_g0_o1', source: 'bad_g0', target: 'bad_o1', action: '', curve: 0.12, actionY: 10, actionWidth: 42 },
    { source: 'bad_o0', target: 'bad_o0', action: '', loopDirection: '-90deg', loopRadius: 74, loopLabelRadius: 34, actionWidth: 42 },
    { source: 'bad_o0', target: 'bad_o1', action: '', curve: 0.1, actionX: 14, actionY: 0, actionWidth: 42 },
    { source: 'bad_r1', target: 'bad_g2', action: '', curve: -0.18, actionY: -8, actionWidth: 42 },
    { source: 'bad_g2', target: 'bad_r2', action: '', curve: -0.18, actionY: -10, actionWidth: 42 },
    { source: 'bad_r2', target: 'bad_g2', action: '', curve: -0.18, actionY: 14, actionWidth: 42 },
    { source: 'bad_g2', target: 'bad_o2', action: '', curve: -0.12, actionY: -10, actionWidth: 42 },
    { id: 'bad_o1_loop', source: 'bad_o1', target: 'bad_o1', action: '', loopDirection: '90deg', loopRadius: 74, loopLabelRadius: 34, actionWidth: 42, actionY: 22 },
    { source: 'bad_o2', target: 'bad_o2', action: '', loopDirection: '90deg', loopRadius: 74, loopLabelRadius: 34, actionWidth: 42, actionY: 22 }
  ]"
/>
</div>
</div>
</div>

<div class="mt-1 bg-red-50 border border-red-200 rounded px-3 py-1 text-red-900 text-[13px] leading-tight">
הריצה הבעייתית מסומנת באדום: מגיעים אל <span dir="ltr"><KatexInline math="\langle off,q_1\rangle" /></span> וחוזרים אליו אינסוף פעמים. זהו מעגל מקבל נגיש במכפלה, ולכן
<span dir="ltr"><KatexInline math="TS\not\models\text{Always Eventually }green" /></span>.
</div>

---

# בדיקת התמדה: מעבר לבעיית מעגל

<div class="mt-7 text-right text-[19px] leading-relaxed">
כדי לבדוק <KatexInline math="TS\models\text{Eventually Always }\Phi" />, מספיק לשאול:
האם יש מצב נגיש שאינו מקיים <KatexInline math="\Phi" /> ונמצא על מעגל?
</div>

<div class="mt-6 flex flex-col items-center gap-1 text-center" dir="ltr">
<div class="text-[24px]">
<KatexInline display math="TS\not\models\text{Eventually Always }\Phi" />
</div>
<div class="text-[30px] leading-none">⇕</div>
<div class="text-[22px]">
<KatexInline display math="\exists s\in Reach(TS)\ \left(s\not\models\Phi\ \land\ s\text{ is on a cycle}\right)" />
</div>
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
נגישות נותנת רישא שמגיעה אל <KatexInline math="s" />.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
המעגל מאפשר לחזור אל <KatexInline math="s" /> אינסוף פעמים.
</div>
</div>

<div class="absolute right-[54px] top-[262px] w-[245px] h-[110px] pointer-events-none scale-85" dir="ltr">
<svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 245 110">
  <defs>
    <marker id="persistence-arrow" markerWidth="9" markerHeight="7" viewBox="0 0 9 7" refX="8" refY="3.5" orient="auto">
      <path d="M0,0 L9,3.5 L0,7 z" fill="#dc2626" />
    </marker>
    <marker id="persistence-red-arrow" markerWidth="9" markerHeight="7" viewBox="0 0 9 7" refX="8" refY="3.5" orient="auto">
      <path d="M0,0 L9,3.5 L0,7 z" fill="#dc2626" />
    </marker>
  </defs>
  <path d="M8 54 C20 42 32 66 44 54 C56 42 68 66 80 54 C88 46 96 54 103 54"
        stroke="#dc2626" stroke-width="3" fill="none" stroke-linecap="round"
        marker-end="url(#persistence-arrow)" />
  <path d="M135 42
           C139 18 151 32 164 20
           C177 8 187 40 200 30
           C213 20 228 43 234 58
           C240 73 226 91 211 98
           C196 105 187 84 174 98
           C161 112 145 84 135 73"
        stroke="#dc2626" stroke-width="3" fill="none" stroke-linecap="round"
        marker-end="url(#persistence-red-arrow)" />
</svg>
<div class="absolute left-[105px] top-[38px] w-[50px] h-[32px] rounded border-[3px] border-red-600 bg-red-50 flex items-center justify-center text-[22px] text-red-800">
<KatexInline math="s" />
</div>
</div>

---

# זיהוי מעגלים: שתי דרכים

<div class="mt-8 grid grid-cols-2 gap-6 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5 text-slate-800">
<div class="font-bold text-slate-800 mb-3">רכיבי קשירות חזקים</div>
מחשבים <span dir="ltr">SCC</span> בגרף המצבים הנגישים, ובודקים אם יש רכיב לא טריוויאלי המכיל מצב <KatexInline math="\neg\Phi" />.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-blue-900">
<div class="font-bold text-blue-800 mb-3"><span dir="ltr">Nested DFS</span></div>
מבצעים חיפוש עומק חיצוני למציאת מצבי <KatexInline math="\neg\Phi" /> נגישים, ומתוכם חיפוש עומק פנימי למציאת חזרה.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-amber-900 text-[21px] leading-relaxed">
<span dir="ltr">Nested DFS</span> מתאים במיוחד לאימות <span dir="ltr">on-the-fly</span>:
אין צורך לבנות מראש את כל גרף המכפלה.
</div>

---

# <span dir="ltr">DFS</span> דו-שלבי

<div class="mt-7 text-right text-[21px] leading-relaxed">
גישה פשוטה:
</div>

<div class="mt-4 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">שלב 1</div>
חיפוש <span dir="ltr">DFS</span> רגיל מוצא את כל מצבי <KatexInline math="\neg\Phi" /> הנגישים.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
<div class="font-bold text-red-800 mb-2">שלב 2</div>
עבור כל מצב כזה <KatexInline math="s" />, מריצים <span dir="ltr">DFS</span> נוסף כדי לבדוק אם אפשר לחזור אל <KatexInline math="s" />.
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline display math="O(N_\Phi\cdot(N+M))" />
</div>

<div class="mt-5 text-right text-[21px] leading-relaxed">
זה נכון אבל עלול לסרוק אותם אזורים פעמים רבות.
</div>

---

# חיפוש <span dir="ltr">DFS</span> מקונן

<div class="mt-7 text-right text-[21px] leading-relaxed">
הרעיון: לשזור את שני החיפושים.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">DFS חיצוני</div>
סורק את המצבים הנגישים. כאשר מצב <KatexInline math="\neg\Phi" /> נסגר במלואו, מתחיל חיפוש פנימי.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">DFS פנימי</div>
מתחיל מאותו מצב ומחפש קשת חזרה אליו. אם נמצאה, יש מעגל נגיש מפר.
</div>
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-slate-800 text-[21px]">
הדוגמה הנגדית מתקבלת משרשור מחסנית החיפוש החיצוני עם מחסנית החיפוש פנימי.
</div>

---

# פסאודו־קוד: החיפוש החיצוני

<div class="mt-5 text-left" dir="ltr">

```txt
reachable-cycle(s):
    add s to R
    push s onto U

    for each t in Post(s):
        if t not in R:
            if reachable-cycle(t):
                return true

    if s does not satisfy Phi:
        clear V
        if cycle-check(s, s):
            return true

    pop s from U
    return false
```

</div>

<div class="mt-4 text-right text-[20px] leading-relaxed">
המחסנית <KatexInline math="U" /> שומרת מסלול התחלתי עד המצב הנבדק.
</div>

---

# פסאודו־קוד: החיפוש הפנימי

<div class="mt-5 text-left" dir="ltr">

```txt
cycle-check(root, s):
    add s to V

    for each t in Post(s):
        if t == root:
            return true
        if t not in V:
            if cycle-check(root, t):
                return true

    return false
```

</div>

<div class="mt-6 text-right text-[20px] leading-relaxed">
אם נמצאת קשת חזרה ל־<KatexInline math="root" />, אז <KatexInline math="root" /> נמצא על מעגל.
אם <KatexInline math="root\not\models\Phi" />, זו הפרה של תכונת ההתמדה.
</div>

---

# נכונות <span dir="ltr">Nested DFS</span>

<div class="mt-7 text-right text-[21px] leading-relaxed">
עבור מערכת מעברים סופית ללא מצבים ללא מוצא ותכונת התמדה
<KatexInline math="P_{\mathrm{pers}}=\text{Eventually Always }\Phi" />:
</div>

<div class="mt-7 text-center text-[28px]" dir="ltr">
<KatexInline display math="\text{Nested DFS returns no}\iff TS\not\models P_{\mathrm{pers}}" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
אם האלגוריתם מוצא חזרה למצב <KatexInline math="\neg\Phi" /> נגיש, קיבלנו ריצה אינסופית שמפרה התמדה.
</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
אם קיימת הפרה, יש מצב <KatexInline math="\neg\Phi" /> נגיש על מעגל, והחיפוש יאתר חזרה אליו.
</div>
</div>

---

# סיבוכיות

<div class="mt-8 text-right text-[22px] leading-relaxed">
נסמן:
</div>

<div class="mt-5 grid grid-cols-3 gap-4 text-[21px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800" dir="ltr"><KatexInline math="N=|Reach(TS)|" /></div>
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800" dir="ltr"><KatexInline math="M=|\to_{\mathrm{reachable}}|" /></div>
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800" dir="ltr"><KatexInline math="|\Phi|" /></div>
</div>

<div class="mt-8 text-center text-[31px]" dir="ltr">
<KatexInline display math="O\left(N\cdot|\Phi|+(N+M)\right)" />
</div>

<div class="mt-8 text-right text-[21px] leading-relaxed">
כל מצב וכל מעבר נסרקים מספר קבוע של פעמים; בדיקת תנאי המצב מוסיפה את עלות הערכת <KatexInline math="\Phi" />.
</div>

---

# התמונה המלאה

<div class="mt-6 grid grid-cols-[1fr_auto_1fr_auto_1fr] gap-3 items-center text-[19px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800">
תכונה <KatexInline math="\omega" />-רגולרית <KatexInline math="P" />
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
אוטומט Büchi למשלים <span dir="ltr"><KatexInline math="\mathcal{A}_{\overline{P}}" /></span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
מכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}_{\overline{P}}" /></span>
</div>
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr] gap-3 items-center text-[19px] leading-relaxed">
<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
בדיקת התמדה <span dir="ltr"><KatexInline math="\text{Eventually Always }\neg F" /></span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
חיפוש מעגל נגיש עם מצב מקבל
</div>
</div>

<div class="mt-8 text-center text-[29px]" dir="ltr">
<KatexInline display math="TS\models P\iff \text{no reachable accepting cycle in }TS\times\mathcal{A}_{\overline{P}}" />
</div>

---

# סיכום תכונות רגולריות

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-slate-800">
<div class="font-bold text-slate-800 mb-2">בטיחות רגולרית</div>
רֵישׁוֹת רעות מתקבלות על ידי <span dir="ltr">NFA/DFA</span>; הבדיקה מצטמצמת לנגישות במכפלה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2"><KatexInline math="\omega" />-רגולריות</div>
עקבות רעות מתקבלות על ידי <span dir="ltr">NBA</span>; הבדיקה מצטמצמת למעגל מקבל נגיש.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">התמדה</div>
הכלי הטכני שמחליף כאן את תכונות השמורה.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2"><span dir="ltr">Nested DFS</span></div>
בדיקה ליניארית שמייצרת דוגמה נגדית בצורת רישא ומעגל.
</div>
</div>

---

# סיכום האלגוריתם

<div class="mt-7 text-right text-[22px] leading-relaxed">
כדי לבדוק תכונה <KatexInline math="\omega" />-רגולרית <KatexInline math="P" />:
</div>

<div class="mt-5 text-right text-[21px] leading-relaxed">
1. בונים או מקבלים אוטומט Büchi בלתי חוסם <KatexInline math="\mathcal{A}" /> עבור
<KatexInline math="\overline{P}" />.
</div>
<div class="mt-3 text-right text-[21px] leading-relaxed">
2. בונים באופן מפורש או <span dir="ltr">on-the-fly</span> את המכפלה
<KatexInline math="TS\times\mathcal{A}" />.
</div>
<div class="mt-3 text-right text-[21px] leading-relaxed">
3. מחפשים מעגל נגיש שמכיל מצב מהצורה <KatexInline math="\langle s,q\rangle" /> עם
<KatexInline math="q\in F" />.
</div>

<div class="mt-8 text-center text-[30px]" dir="ltr">
<KatexInline display math="\text{found accepting cycle}\Rightarrow\text{counterexample}" />
<KatexInline display math="\text{no accepting cycle}\Rightarrow TS\models P" />
</div>
