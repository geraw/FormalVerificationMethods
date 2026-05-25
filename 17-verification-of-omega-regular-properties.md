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
  lang: heb
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

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# ראשי פרקים

<div class="grid grid-cols-2 gap-5 mt-8 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold text-slate-700 mb-2">תזכורת</div>
בדיקת תכונות בטיחות רגולריות, שפות <KatexInline math="\omega" />-רגולריות, ואוטומטי Büchi.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">הרעיון המרכזי</div>
ייצוג העקבות הרעות באמצעות <span dir="ltr">NBA</span>, ובדיקת חיתוך עם עקבות המערכת.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">תכונות התמדה</div>
רדוקציה מאימות <KatexInline math="\omega" />-רגולרי לבדיקת “בסופו של דבר תמיד”.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2"><span dir="ltr">Nested DFS</span></div>
זיהוי מעגל נגיש המכיל מצב מפר, ובניית דוגמה נגדית.
</div>
</div>

---

# תזכורת: בטיחות רגולרית

<div class="mt-7 text-right text-[22px] leading-relaxed">
עבור תכונת בטיחות רגולרית <KatexInline math="P_{\mathrm{safe}}" />, נתון אוטומט סופי
<KatexInline math="\mathcal{A}" /> שמקבל את הרֵישׁוֹת הרעות:
</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline display math="L(\mathcal{A})=\mathit{BadPref}(P_{\mathrm{safe}})" />
</div>

<div class="mt-8 grid grid-cols-[1fr_auto_1fr] gap-4 items-center text-[21px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
מחפשים רישא שמערכת המעברים יכולה לייצר
</div>
<div class="text-[34px] text-slate-500">⇔</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
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
<div class="bg-blue-50 border border-blue-200 rounded p-4">
אפשר לתאר אותה באמצעות ביטוי <KatexInline math="\omega" />-רגולרי.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
אפשר לתאר אותה באמצעות אוטומט Büchi.
</div>
</div>

<div class="mt-8 text-right text-[22px] leading-relaxed">
המטרה בהרצאה: לבדוק אלגוריתמית אם <KatexInline math="TS\models P" />.
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

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-[20px] leading-snug">
אם קיימת עקבה של המערכת שמתקבלת על ידי <KatexInline math="\mathcal{A}" />, מצאנו ריצה שמפרה את התכונה.
</div>

---

# למה לא להשתמש באוטומט של <KatexInline math="P" />?

<div class="mt-5 text-right text-[21px] leading-snug">
אנחנו רוצים לעבוד עם המכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>.
כל ריצה שלה היא שילוב של ריצה של המערכת עם ריצה אחת של האוטומט על העקבה שלה.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[19px] leading-snug">
<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">אם משתמשים באוטומט של <KatexInline math="P" /></div>
לאותה ריצה של המערכת יכולות להיות כמה ריצות של האוטומט.
לכן ריצה אחת לא-מקבלת במכפלה לא מוכיחה שהעקבה אינה ב־<KatexInline math="P" />.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מה כן ניתן לבדוק ריצה־ריצה?</div>
אפשר לבדוק קיום של ריצה מקבלת במכפלה. לכן נשתמש באוטומט שמקבל את העקבות הרעות.
</div>
</div>

<div class="mt-6 text-center text-[26px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-5 bg-red-50 border border-red-200 rounded p-3 text-[20px] leading-snug">
אז ריצה מקבלת אחת של <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>
היא בדיוק ריצה של המערכת שמפרה את <KatexInline math="P" />.
</div>

---

# הרעיון האלגוריתמי

<div class="mt-6 text-center text-[24px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr_auto_1fr] gap-3 items-center text-[20px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
בונים מכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4">
מחפשים ריצה של <KatexInline math="TS" /> ש־<KatexInline math="\mathcal{A}" /> מקבל את העקבה שלה
<span class="block mt-1 text-[13px] leading-tight text-blue-700">(בוחנים כל ריצה של <KatexInline math="TS\times\mathcal{A}" /> בנפרד)</span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
כלומר ריצה עם אינסוף מצבים שהתיוג שלהם מכיל מצב מקבל של <KatexInline math="\mathcal{A}" />
<span class="block mt-1 text-[13px] leading-tight text-red-700">(כי התיוג ב־<KatexInline math="TS\times\mathcal{A}" />  הוא המצב של <KatexInline math="\mathcal{A}" />)</span>
</div>
</div>

<div class="mt-9 text-center text-[21px]" dir="ltr">
<KatexInline display math="\begin{array}{rcl}
TS\not\models P &amp;\iff&amp; \mathit{Traces}(TS)\cap L_\omega(\mathcal{A})\neq\emptyset\\[6pt]
&amp;\iff&amp; TS\times \mathcal{A}\not\models \text{Eventually Always}\bigwedge_{q_f\in F} \neg q_f
\end{array}" />
</div>

---

# מכפלה של מערכת מעברים ואוטומט Büchi

<div class="mt-5 text-right text-[20px] leading-relaxed">
עבור <KatexInline math="TS=(S,Act,\to,I,AP,L)" /> ללא מצבים סופיים, ו־
<KatexInline math="\mathcal{A}=(Q,2^{AP},\delta,Q_0,F)" /> בלתי חוסם:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="TS\times\mathcal{A}=(S\times Q,Act,\to_\times,I_\times,Q,L_\times)" />
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מעברים</div>
<div dir="ltr"><KatexInline display math="\frac{s\xrightarrow{\alpha}t\ \land\ p\in\delta(q,L(t))}{(s,q)\xrightarrow{\alpha}_\times(t,p)}" /></div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מצבים התחלתיים</div>
<div dir="ltr"><KatexInline display math="I_\times=\{(s_0,q)\mid s_0\in I,\ \exists q_0\in Q_0\ \left(q\in\delta(q_0,L(s_0))\right)\}" /></div>
</div>
</div>

<div class="mt-5 text-right text-[20px] leading-relaxed">
התיוג במכפלה הוא מצב האוטומט: <span dir="ltr"><KatexInline math="L_\times(s,q)=\{q\}" /></span>.
</div>

---

# מה מייצגת ריצה במכפלה?

<div class="mt-6 grid grid-cols-3 gap-4 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">ריצת מערכת</div>
<div dir="ltr"><KatexInline math="s_0s_1s_2\cdots" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">עקבה</div>
<div dir="ltr"><KatexInline math="L(s_0)L(s_1)L(s_2)\cdots" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">ריצת אוטומט</div>
<div dir="ltr"><KatexInline math="q_0q_1q_2\cdots" /></div>
</div>
</div>

<div class="mt-9 text-center text-[28px]" dir="ltr">
<KatexInline display math="(s_0,q_1)(s_1,q_2)(s_2,q_3)\cdots" />
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[21px] leading-relaxed">
אם לאורך ריצה במכפלה מבקרים במצבים מהצורה <KatexInline math="(s,q)" /> עם
<KatexInline math="q\in F" /> אינסוף פעמים, אז העקבה של ריצת המערכת מתקבלת על ידי האוטומט.
</div>

---

# תכונת התמדה

<div class="mt-8 text-right text-[23px] leading-relaxed">
תכונת התמדה היא תכונה מהצורה:
</div>

<div class="mt-5 text-center text-[32px]" dir="ltr">
<KatexInline display math="\text{eventually forever }\Phi" />
</div>

<div class="mt-6 text-center text-[29px]" dir="ltr">
<KatexInline display math="P_{\mathrm{pers}}(\Phi)=\{\sigma=A_0A_1A_2\cdots\mid \exists i\ge 0\ \left(\forall j\ge i\ \left(A_j\models\Phi\right)\right)\}" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
אחרי רישא סופית כל המצבים מקיימים <KatexInline math="\Phi" />.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
ההפרה היא ביקור אינסופי במצבים שמקיימים <KatexInline math="\neg\Phi" />.
</div>
</div>

---

# תכונת ההתמדה של האוטומט

<div class="mt-7 text-right text-[22px] leading-relaxed">
במכפלה <KatexInline math="TS\times\mathcal{A}" /> הפסוקים האטומיים הם מצבי האוטומט
<KatexInline math="Q" />.
</div>

<div class="mt-7 text-center text-[31px]" dir="ltr">
<KatexInline display math="P_{\mathrm{pers}}(\mathcal{A})=\text{eventually forever }\neg F" />
</div>

<div class="mt-7 text-center text-[29px]" dir="ltr">
<KatexInline display math="\neg F=\bigwedge_{q\in F}\neg q" />
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-5 text-[22px] leading-relaxed">
כלומר: החל מרגע מסוים, הריצה במכפלה אינה מבקרת יותר במצב מקבל של האוטומט.
</div>

---

# משפט: אימות תכונות <KatexInline math="\omega" />-רגולריות

<div class="mt-5 text-right text-[20px] leading-relaxed">
יהיו <KatexInline math="TS" /> מערכת מעברים סופית ללא מצבים סופיים,
<KatexInline math="P" /> תכונה <KatexInline math="\omega" />-רגולרית,
ו־<KatexInline math="\mathcal{A}" /> אוטומט Büchi בלתי חוסם כך ש־
</div>

<div class="mt-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" />
</div>

<div class="mt-5 text-right text-[21px] leading-relaxed">
אז התנאים הבאים שקולים:
</div>

<div class="mt-4 grid grid-cols-3 gap-4 text-[20px]">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4" dir="ltr">
<KatexInline math="TS\models P" />
</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4" dir="ltr">
<KatexInline math="\mathit{Traces}(TS)\cap L_\omega(\mathcal{A})=\emptyset" />
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4" dir="ltr">
<KatexInline math="TS\times\mathcal{A}\models P_{\mathrm{pers}}(\mathcal{A})" />
</div>
</div>

<div class="mt-8 text-right text-[21px] leading-relaxed">
זהו סעיף 4.4 בספר: אימות כללי של תכונה <KatexInline math="\omega" />-רגולרית מצטמצם לבדיקת התמדה במכפלה.
</div>

---

# הוכחת המשפט: הכיוון של דוגמה נגדית

<div class="mt-6 text-right text-[21px] leading-relaxed">
נניח ש־<KatexInline math="TS\times\mathcal{A}\not\models P_{\mathrm{pers}}(\mathcal{A})" />.
אז קיימת ריצה במכפלה שמבקרת במצבי <KatexInline math="F" /> אינסוף פעמים:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="(s_0,q_1)(s_1,q_2)(s_2,q_3)\cdots" />
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
ההטלה על הרכיב הראשון היא ריצה של <KatexInline math="TS" />.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
הרכיב השני הוא ריצת Büchi מקבלת על העקבה של אותה ריצה.
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathit{trace}(s_0s_1s_2\cdots)\in\mathit{Traces}(TS)\cap L_\omega(\mathcal{A})" />
</div>

---

# דוגמה: “אינסוף פעמים ירוק”

<div class="grid grid-cols-[0.9fr_1.1fr] gap-5 mt-5 items-center">
<div class="bg-white border border-slate-200 rounded p-3">
<AutomatonD3 variant="classic" :width="430" :height="230" :arrowSize="4.2" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'q0', x: 70, y: 115, label: '$q_0$', initial: true, initialDirection: 'left', r: 24, labelWidth: 60 },
    { id: 'q1', x: 215, y: 115, label: '$q_1$', accepting: true, r: 24, labelWidth: 60 },
    { id: 'q2', x: 360, y: 115, label: '$q_2$', r: 24, labelWidth: 60 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$true$', loopDirection: '-90deg', labelY: -10, labelWidth: 60 },
    { source: 'q0', target: 'q1', label: '$\\neg green$', labelY: -10, labelWidth: 95 },
    { source: 'q1', target: 'q1', label: '$\\neg green$', loopDirection: '-90deg', labelY: -10, labelWidth: 95 },
    { source: 'q1', target: 'q2', label: '$green$', labelY: -10, labelWidth: 70 },
    { source: 'q2', target: 'q2', label: '$true$', loopDirection: '-90deg', labelY: -10, labelWidth: 60 }
  ]"
/>
</div>

<div class="text-right text-[21px] leading-relaxed">
<div class="font-bold mb-3">התכונה שרוצים לבדוק:</div>
<div class="text-center text-[28px] mb-5" dir="ltr"><KatexInline math="\Box\Diamond green" /></div>
<div class="font-bold mb-3">האוטומט מקבל את המשלים:</div>
<div class="text-center text-[28px]" dir="ltr"><KatexInline math="\Diamond\Box\neg green" /></div>
<div class="mt-5">
כלומר, החל מרגע מסוים אין יותר ירוק.
</div>
</div>
</div>

---

# דוגמה: מערכת שמקיימת את התכונה

<div class="mt-5 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-white border border-slate-200 rounded p-4">
<div class="font-bold mb-3">רמזור פשוט</div>
<div class="flex justify-center items-center gap-4 mt-6" dir="ltr">
  <div class="rounded-full bg-red-100 border-2 border-red-500 w-24 h-24 flex items-center justify-center font-bold">$red$</div>
  <div class="text-[34px]">⇄</div>
  <div class="rounded-full bg-green-100 border-2 border-green-500 w-24 h-24 flex items-center justify-center font-bold">$green$</div>
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-3">במכפלה</div>
אין מעגל נגיש שמבקר במצב מקבל של האוטומט עבור המשלים.
לכן לא קיימת עקבה רעה, ומתקיים:
<div class="mt-4 text-center text-[27px]" dir="ltr"><KatexInline math="TS\models\Box\Diamond green" /></div>
</div>
</div>

<div class="mt-8 text-right text-[21px] leading-relaxed">
המעבר בין אדום לירוק חוזר אינסוף פעמים, ולכן אי אפשר להישאר לנצח באזור <KatexInline math="\neg green" />.
</div>

---

# דוגמה: מערכת שמפרה את התכונה

<div class="mt-5 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-white border border-slate-200 rounded p-4">
<div class="font-bold mb-3">רמזור שיכול להיכבות</div>
<div class="flex justify-center items-center gap-3 mt-6" dir="ltr">
  <div class="rounded-full bg-red-100 border-2 border-red-500 w-20 h-20 flex items-center justify-center font-bold">$red$</div>
  <div class="text-[30px]">⇄</div>
  <div class="rounded-full bg-green-100 border-2 border-green-500 w-20 h-20 flex items-center justify-center font-bold">$green$</div>
  <div class="text-[30px]">←</div>
  <div class="rounded-full bg-slate-100 border-2 border-slate-500 w-20 h-20 flex items-center justify-center font-bold">$\emptyset$</div>
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-3">במכפלה</div>
יש מעגל נגיש שבו האוטומט נשאר במצב שמקבל את המשלים:
<div class="mt-4 text-center text-[26px]" dir="ltr"><KatexInline math="red,\emptyset,red,\emptyset,\ldots" /></div>
</div>
</div>

<div class="mt-8 text-center text-[28px]" dir="ltr">
<KatexInline display math="TS\not\models\Box\Diamond green" />
</div>

---

# בדיקת התמדה: מעבר לבעיית מעגל

<div class="mt-7 text-right text-[22px] leading-relaxed">
כדי לבדוק <KatexInline math="TS\models\Diamond\Box\Phi" />, מספיק לשאול:
האם יש מצב נגיש שאינו מקיים <KatexInline math="\Phi" /> ונמצא על מעגל?
</div>

<div class="mt-7 text-center text-[29px]" dir="ltr">
<KatexInline display math="TS\not\models\Diamond\Box\Phi\iff \exists s\in Reach(TS)\ \left(s\not\models\Phi\ \land\ s\text{ is on a cycle}\right)" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
נגישות נותנת רישא שמגיעה אל <KatexInline math="s" />.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
המעגל מאפשר לחזור אל <KatexInline math="s" /> אינסוף פעמים.
</div>
</div>

---

# דוגמה נגדית לתכונת התמדה

<div class="mt-5 relative h-[300px] mx-auto max-w-[760px]" dir="ltr">
  <div class="absolute left-[40px] top-[120px] w-20 h-20 rounded-full border-2 border-slate-500 bg-slate-50 flex items-center justify-center">$s_0$</div>
  <div class="absolute left-[205px] top-[120px] w-20 h-20 rounded-full border-2 border-red-500 bg-red-50 flex items-center justify-center">$s$<br>$\neg\Phi$</div>
  <div class="absolute left-[370px] top-[120px] w-20 h-20 rounded-full border-2 border-slate-500 bg-slate-50 flex items-center justify-center">$t$</div>
  <div class="absolute left-[535px] top-[120px] w-20 h-20 rounded-full border-2 border-slate-500 bg-slate-50 flex items-center justify-center">$u$</div>

  <svg class="absolute inset-0 w-full h-full" viewBox="0 0 760 300">
    <defs>
      <marker id="arrow21" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
        <path d="M0,0 L0,6 L9,3 z" fill="#475569" />
      </marker>
    </defs>
    <path d="M120 160 L200 160" stroke="#475569" stroke-width="2.5" marker-end="url(#arrow21)" fill="none" />
    <path d="M285 160 L365 160" stroke="#475569" stroke-width="2.5" marker-end="url(#arrow21)" fill="none" />
    <path d="M450 160 L530 160" stroke="#475569" stroke-width="2.5" marker-end="url(#arrow21)" fill="none" />
    <path d="M575 118 C545 40 245 40 245 118" stroke="#475569" stroke-width="2.5" marker-end="url(#arrow21)" fill="none" />
  </svg>
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="s_0\cdots s\ t\ u\ s\ t\ u\ s\cdots" />
</div>

<div class="mt-4 text-right text-[21px] leading-relaxed">
המצב <KatexInline math="s" /> מפר את <KatexInline math="\Phi" /> ומופיע אינסוף פעמים, ולכן “לבסוף תמיד <KatexInline math="\Phi" />” מופר.
</div>

---

# זיהוי מעגלים: שתי דרכים

<div class="mt-8 grid grid-cols-2 gap-6 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold text-slate-700 mb-3">רכיבי קשירות חזקים</div>
מחשבים <span dir="ltr">SCC</span> בגרף המצבים הנגישים, ובודקים אם יש רכיב לא טריוויאלי המכיל מצב <KatexInline math="\neg\Phi" />.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3"><span dir="ltr">Nested DFS</span></div>
מבצעים חיפוש עומק חיצוני למציאת מצבי <KatexInline math="\neg\Phi" /> נגישים, ומתוכם חיפוש עומק פנימי למציאת חזרה.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-[21px] leading-relaxed">
<span dir="ltr">Nested DFS</span> מתאים במיוחד לאימות <span dir="ltr">on-the-fly</span>:
אין צורך לבנות מראש את כל גרף המכפלה.
</div>

---

# <span dir="ltr">DFS</span> דו-שלבי

<div class="mt-7 text-right text-[21px] leading-relaxed">
גישה פשוטה:
</div>

<div class="mt-4 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">שלב 1</div>
חיפוש <span dir="ltr">DFS</span> רגיל מוצא את כל מצבי <KatexInline math="\neg\Phi" /> הנגישים.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">שלב 2</div>
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
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">DFS חיצוני</div>
סורק את המצבים הנגישים. כאשר מצב <KatexInline math="\neg\Phi" /> נסגר במלואו, מתחיל חיפוש פנימי.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">DFS פנימי</div>
מתחיל מאותו מצב ומחפש קשת חזרה אליו. אם נמצאה, יש מעגל נגיש מפר.
</div>
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-[21px]">
הדוגמה הנגדית מתקבלת משרשור מחסנית החיפוש החיצוני עם מחסנית החיפוש הפנימי.
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
<KatexInline math="P_{\mathrm{pers}}=\Diamond\Box\Phi" />:
</div>

<div class="mt-7 text-center text-[28px]" dir="ltr">
<KatexInline display math="\text{Nested DFS returns no}\iff TS\not\models P_{\mathrm{pers}}" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-[20px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
אם האלגוריתם מוצא חזרה למצב <KatexInline math="\neg\Phi" /> נגיש, קיבלנו ריצה אינסופית שמפרה התמדה.
</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4">
אם קיימת הפרה, יש מצב <KatexInline math="\neg\Phi" /> נגיש על מעגל, והחיפוש יאתר חזרה אליו.
</div>
</div>

---

# סיבוכיות

<div class="mt-8 text-right text-[22px] leading-relaxed">
נסמן:
</div>

<div class="mt-5 grid grid-cols-3 gap-4 text-[21px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr"><KatexInline math="N=|Reach(TS)|" /></div>
<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr"><KatexInline math="M=|\to_{\mathrm{reachable}}|" /></div>
<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr"><KatexInline math="|\Phi|" /></div>
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
<div class="bg-slate-50 border border-slate-200 rounded p-4">
תכונה <KatexInline math="\omega" />-רגולרית <KatexInline math="P" />
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4">
אוטומט Büchi למשלים <span dir="ltr"><KatexInline math="\mathcal{A}_{\overline{P}}" /></span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
מכפלה <span dir="ltr"><KatexInline math="TS\times\mathcal{A}_{\overline{P}}" /></span>
</div>
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr] gap-3 items-center text-[19px] leading-relaxed">
<div class="bg-amber-50 border border-amber-200 rounded p-4">
בדיקת התמדה <span dir="ltr"><KatexInline math="\Diamond\Box\neg F" /></span>
</div>
<div class="text-[30px] text-slate-500">←</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
חיפוש מעגל נגיש עם מצב מקבל
</div>
</div>

<div class="mt-8 text-center text-[29px]" dir="ltr">
<KatexInline display math="TS\models P\iff \text{no reachable accepting cycle in }TS\times\mathcal{A}_{\overline{P}}" />
</div>

---

# סיכום תכונות רגולריות

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">בטיחות רגולרית</div>
רֵישׁוֹת רעות מתקבלות על ידי <span dir="ltr">NFA/DFA</span>; הבדיקה מצטמצמת לנגישות במכפלה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2"><KatexInline math="\omega" />-רגולריות</div>
עקבות רעות מתקבלות על ידי <span dir="ltr">NBA</span>; הבדיקה מצטמצמת למעגל מקבל נגיש.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">התמדה</div>
הכלי הטכני שמחליף כאן את תכונות השמורה.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2"><span dir="ltr">Nested DFS</span></div>
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
3. מחפשים מעגל נגיש שמכיל מצב מהצורה <KatexInline math="(s,q)" /> עם
<KatexInline math="q\in F" />.
</div>

<div class="mt-8 text-center text-[30px]" dir="ltr">
<KatexInline display math="\text{found accepting cycle}\Rightarrow\text{counterexample}" />
<KatexInline display math="\text{no accepting cycle}\Rightarrow TS\models P" />
</div>
