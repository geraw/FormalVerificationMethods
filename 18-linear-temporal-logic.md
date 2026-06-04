---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 18-linear-temporal-logic
htmlAttrs:
  dir: rtl
  lang: he
drawings:
  enabled: true
info: |
  ## לוגיקת זמנים ליניארית
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# לוגיקת זמנים ליניארית

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# ראשי פרקים

<div class="grid grid-cols-3 gap-4 mt-8 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">תחביר</div>
נגדיר את נוסחאות <span dir="ltr">LTL</span>, את האופרטורים הבסיסיים, ואת הסוכר התחבירי השימושי.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">סמנטיקה</div>
נפרש נוסחאות מעל מילים אינסופיות, מסלולים ומערכות מעברים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">שקילות</div>
נראה דואליות, פריסה, אופרטורים נגזרים וצורות נורמליות.
</div>
</div>

---

# איפה LTL יושבת בתהליך בדיקת המודל?

<div class="mt-6 grid grid-cols-[1fr_auto_1fr] gap-5 items-center text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-2">דרישות</div>
תכונות זמן ליניארי שנרצה לבדוק על כל ההתנהגויות של המערכת.
</div>
<div class="text-[34px] text-slate-500">←</div>
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">לוגיקת זמנים</div>
שפה קומפקטית לכתיבת הדרישות כנוסחאות.
</div>
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr_auto_1fr] gap-3 items-center text-[18px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
תכונות פורמליות
</div>
<div class="text-[28px] text-slate-500">←</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
אוטומטי Büchi
</div>
<div class="text-[28px] text-slate-500">←</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
בדיקת מודל ודוגמה נגדית
</div>
</div>

<div class="mt-8 text-center text-[28px]" dir="ltr">
<KatexInline display math="\text{requirements}\;\longrightarrow\;\text{LTL formula}\;\longrightarrow\;\omega\text{-regular property}" />
</div>

---

# אמיר פנואלי ולוגיקת הזמן

<div class="mt-4 grid grid-cols-[1.25fr_0.95fr] gap-4 items-center text-right">
<div class="text-[18px] leading-snug">
אמיר פנואלי הציג בשנת 1977 את השימוש בלוגיקה טמפורלית לתיאור תוכניות.
הרעיון היה להחליף טענות על מצב יחיד בטענות על רצף של מצבים.
</div>

<div class="p-1 text-center">
<img src="./public/amir-pnueli.jpg" class="mx-auto rounded w-[132px] h-[142px] object-cover" alt="אמיר פנואלי" />
<div class="mt-1 text-[13px] text-slate-700">1941-2009</div>
<div class="mt-0.5 text-[9px] text-slate-500" dir="ltr">Dennis Hamilton, CC BY 2.0</div>
</div>
</div>

<div class="mt-4 grid grid-cols-2 gap-3 text-right text-[16px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-3">
<div class="font-bold text-blue-700 mb-0.5 text-[15px]">דוגמה 1</div>
תמיד אם יש בקשה להיכנס למקטע קריטי, אז בסופו של דבר תגיע כניסה למקטע הקריטי.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<div class="font-bold text-emerald-700 mb-0.5 text-[15px]">דוגמה 2</div>
בסופו של דבר תהליך האתחול יסתיים.
</div>
<div class="bg-white border border-slate-200 rounded p-3">
<div class="font-bold text-slate-700 mb-0.5 text-[15px]">דוגמה 3</div>
מהרגע שמצב מוכן הושג, הוא יישמר לתמיד.
</div>
<div class="bg-red-50 border border-red-200 rounded p-3">
<div class="font-bold text-red-700 mb-0.5 text-[15px]">דוגמה 4</div>
פעולת ניטור תתבצע שוב ושוב לאורך הריצה.
</div>
</div>

---

# תכונות זמן ליניארי כנוסחאות

<div class="mt-3 flex justify-center gap-3 text-[16px]" dir="ltr">
<div class="bg-slate-50 border border-slate-200 rounded px-4 py-2">
<KatexInline math="\Box" /> = Always
</div>
<div class="bg-slate-50 border border-slate-200 rounded px-4 py-2">
<KatexInline math="\Diamond" /> = Eventually
</div>
</div>

<div class="mt-4 grid grid-cols-[1fr_1.1fr] gap-5 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מניעה הדדית</div>
<div dir="ltr" class="text-center text-[26px]"><KatexInline math="\Box\neg(crit_1\land crit_2)" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">האתחול יסתיים</div>
<div dir="ltr" class="text-center text-[26px]"><KatexInline math="\Diamond\neg init" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">האתחול יסתיים ולא יחזור</div>
<div dir="ltr" class="text-center text-[26px]"><KatexInline math="\Diamond\Box\neg init" /></div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">מניעת הרעבה</div>
<div dir="ltr" class="text-center text-[25px]"><KatexInline math="\Box\Diamond crit_1 \lor \Box\Diamond crit_2" /></div>
</div>
</div>

<div class="mt-7 text-center text-[22px]">
האופרטורים הטמפורליים נותנים שמות קצרים לדפוסים על כל המילה האינסופית.
</div>

---

# עוד שני דפוסים בסיסיים

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">הצעד הבא</div>
אם הרמזור צהוב עכשיו, אז בצעד הבא הוא לא אדום:
<div dir="ltr" class="mt-4 text-center text-[28px]"><KatexInline math="\Box(yellow\Rightarrow \bigcirc\neg red)" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-2">עד ש...</div>
נהיה במצב אתחול עד שנגיע למצב מוכן:
<div dir="ltr" class="mt-4 text-center text-[28px]"><KatexInline math="init\mathbin{\mathrm{U}}ready" /></div>
</div>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[17px] leading-relaxed">
<span class="font-bold">מקרא אופרטורים:</span>
<span dir="ltr" class="mr-3"><KatexInline math="\Box" /></span> תמיד,
<span dir="ltr" class="mr-3"><KatexInline math="\bigcirc" /></span> בצעד הבא,
<span dir="ltr" class="mr-3"><KatexInline math="\mathrm{U}" /></span> עד ש־.
</div>

<div class="mt-8 grid grid-cols-[1fr_auto_1fr_auto_1fr] gap-3 items-center text-[18px]">
<div class="bg-slate-50 border border-slate-200 rounded p-3">עכשיו</div>
<div class="text-[28px] text-slate-500">←</div>
<div class="bg-slate-50 border border-slate-200 rounded p-3">הצעד הבא</div>
<div class="text-[28px] text-slate-500">←</div>
<div class="bg-slate-50 border border-slate-200 rounded p-3">המשך אינסופי</div>
</div>

---

# תחביר: נוסחה ב-LTL

<div class="mt-7 text-right text-[21px] leading-relaxed">
נגדיר <span dir="ltr">LTL</span> מעל קבוצת פסוקים אטומיים <span dir="ltr"><KatexInline math="AP" /></span>.
אם <span dir="ltr"><KatexInline math="a\in AP" /></span>, אז:
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="\varphi ::= true \mid a \mid \varphi_1\land\varphi_2 \mid \neg\varphi \mid \bigcirc\varphi \mid \varphi_1\mathbin{\mathrm{U}}\varphi_2" />
</div>

<div class="mt-7 grid grid-cols-2 gap-4 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<span dir="ltr"><KatexInline math="\bigcirc\varphi" /></span> אומר: <span class="font-bold">בצעד הבא</span> תתקיים <span dir="ltr"><KatexInline math="\varphi" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<span dir="ltr"><KatexInline math="\varphi_1\mathbin{\mathrm{U}}\varphi_2" /></span> אומר: <span dir="ltr"><KatexInline math="\varphi_1" /></span> תתקיים עד ש־<span dir="ltr"><KatexInline math="\varphi_2" /></span> תתקיים.
</div>
</div>

<div class="mt-4 text-center text-[17px] text-slate-600">
הערה: האופרטורים <span dir="ltr"><KatexInline math="\Diamond" /></span> (<span dir="ltr">Eventually</span>) ו־<span dir="ltr"><KatexInline math="\Box" /></span> (<span dir="ltr">Always</span>) יוגדרו בהמשך כסוכר תחבירי.
</div>

---

# אופרטורים נגזרים

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">לוגיקה פסוקית</div>
<div dir="ltr" class="text-[23px]"><KatexInline display math="\begin{aligned}
false &\equiv \neg true \\
\varphi\lor\psi &\equiv \neg(\neg\varphi\land\neg\psi) \\
\varphi\Rightarrow\psi &\equiv \neg\varphi\lor\psi
\end{aligned}" /></div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">אופרטורי זמן</div>
<div dir="ltr" class="text-[23px]"><KatexInline display math="\begin{aligned}
\Diamond\varphi &\equiv true\,\mathbin{\mathrm{U}}\,\varphi \\
\Box\varphi &\equiv \neg\Diamond\neg\varphi
\end{aligned}" /></div>
</div>
</div>

<div class="mt-7 text-center text-[21px]">
סדר קדימויות: אופרטורים אונריים קודם, אחר כך <span dir="ltr"><KatexInline math="\mathbin{\mathrm{U}}" /></span>, ואז הקשרים הבינאריים הפסוקיים.
</div>

---

# ארבע תבניות זמן שכדאי להכיר

<div class="mt-7 grid grid-cols-4 gap-3 text-center text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div dir="ltr" class="text-[34px] font-bold text-blue-700"><KatexInline math="\Diamond" /></div>
מתישהו בעתיד
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div dir="ltr" class="text-[34px] font-bold text-emerald-700"><KatexInline math="\Box" /></div>
עכשיו ולתמיד
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div dir="ltr" class="text-[34px] font-bold text-amber-700"><KatexInline math="\Box\Diamond" /></div>
חוזר ונשנה
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
<div dir="ltr" class="text-[34px] font-bold text-red-700"><KatexInline math="\Diamond\Box" /></div>
התמדה
</div>
</div>

<div class="mt-7 text-center text-[22px]">
גרירות לוגיות הנובעות מהתיאור למעלה
</div>

<div class="mt-4 text-center text-[26px]" dir="ltr">
<KatexInline display math="\Diamond\Box\varphi \Rightarrow \Diamond\varphi,\qquad \Box\varphi \Rightarrow \Box\Diamond\varphi" />
</div>


---

# שלוש דרכים לתאר אותה דרישה

<div class="mt-3 grid grid-cols-1 gap-2 text-center text-[17px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-2.5">
<div class="font-bold text-blue-700 mb-2">כשפה</div>
<div dir="ltr" class="text-[20px]"><KatexInline math="\{\sigma:\underset{\infty}{\exists}i\;(crit_1\in\sigma[i])\;\land\;\underset{\infty}{\exists}i\;(crit_2\in\sigma[i])\}" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-2.5">
<div class="font-bold text-emerald-700 mb-2">כנוסחת LTL</div>
<div dir="ltr" class="text-[24px]"><KatexInline math="\Box\Diamond crit_1\land\Box\Diamond crit_2" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-2.5">
<div class="font-bold text-amber-700 mb-1">כאוטומט GNBA</div>
<div class="mt-2 bg-white rounded border border-slate-200 shadow-sm p-2 flex justify-center">
<AutomatonD3 variant="classic" :width="390" :height="125" :arrowSize="3.7" :stateLabelFontSize="14" :transitionLabelFontSize="11"
:states="[
{ id: 'q0', x: 195, y: 60, label: '$q_0$', initial: true, initialDirection: 'top', r: 20, labelWidth: 56 },
{ id: 'q1', x: 68, y: 60, label: '$q_1$', accepting: true, r: 20, labelWidth: 56, stroke: '#2563eb' },
{ id: 'q2', x: 322, y: 60, label: '$q_2$', accepting: true, r: 20, labelWidth: 56, stroke: '#dc2626' }
]"
:transitions="[
{ source: 'q0', target: 'q0', label: '$true$', loopDirection: '90deg', labelY: 8, labelWidth: 50 },
{ source: 'q0', target: 'q1', label: '$crit_1$', labelY: 12, labelWidth: 70, curve: -0.18 },
{ source: 'q1', target: 'q0', label: '$true$', labelY: -12, labelWidth: 50, curve: -0.18 },
{ source: 'q0', target: 'q2', label: '$crit_2$', labelY: -12, labelWidth: 70, curve: -0.18 },
{ source: 'q2', target: 'q0', label: '$true$', labelY: 12, labelWidth: 50, curve: -0.18 }
]"
/>
</div>
</div>
</div>

---

# דוגמאות שימושיות בתוכניות

<div class="mt-6 grid grid-cols-2 gap-4 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">עצירה</div>
<div dir="ltr" class="text-center text-[27px]"><KatexInline math="\Diamond terminated" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">שירות חי</div>
<div dir="ltr" class="text-center text-[27px]"><KatexInline math="\Box(requested\Rightarrow\Diamond served)" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">העברת הודעות הוגנת</div>
<div dir="ltr" class="text-center text-[27px]"><KatexInline math="\Box\Diamond sent\Rightarrow\Box\Diamond delivered" /></div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">אין פלט לפני קלט</div>
<div dir="ltr" class="text-center text-[25px]"><KatexInline math="\Box\neg output\lor(\neg output\mathbin{\mathrm{U}}input)" /></div>
</div>
</div>

---

# תכונות פרקטיות ב-LTL

<div class="mt-6 grid grid-cols-2 gap-5 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">נגישות</div>
<div dir="ltr" class="text-[25px]"><KatexInline math="\Diamond\varphi" /></div>
<div class="mt-2">מתישהו מגיעים למצב שמקיים את <span dir="ltr"><KatexInline math="\varphi" /></span>.</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">בטיחות / שמורה</div>
<div dir="ltr" class="text-[25px]"><KatexInline math="\Box\varphi" /></div>
<div class="mt-2">כל מצב לאורך המסלול מקיים את <span dir="ltr"><KatexInline math="\varphi" /></span>.</div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">חיות מותנית</div>
<div dir="ltr" class="text-[25px]"><KatexInline math="\Box(\varphi\Rightarrow\Diamond\psi)" /></div>
<div class="mt-2">כל בקשה שמתרחשת תיענה בעתיד.</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">הוגנות</div>
<div dir="ltr" class="text-[25px]"><KatexInline math="\Box\Diamond\varphi" /></div>
<div class="mt-2">האירוע אינו נעלם; הוא חוזר אינסוף פעמים.</div>
</div>
</div>

---

# סמנטיקה: נוסחה מגדירה קבוצת מילים

<div class="mt-4 text-right text-[21px] leading-snug">
תכונת הזמן הליניארי המוגדרת על ידי נוסחת <span dir="ltr"><KatexInline math="\psi" /></span> היא קבוצת כל המילים שמספקות אותה:
</div>

<div class="mt-3 text-center text-[20px]" dir="ltr">
<KatexInline display math="Words(\psi)=\{\sigma\in(2^{AP})^\omega : \sigma\models\psi\}" />
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[21px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models true &\iff true \\
\sigma\models a &\iff a\in\sigma[0] \\
\sigma\models\varphi_1\land\varphi_2 &\iff \left(\sigma\models\varphi_1\;\text{and}\;\sigma\models\varphi_2\right) \\
\sigma\models\neg\varphi &\iff \sigma\not\models\varphi \\
\sigma\models\bigcirc\varphi &\iff \sigma[1..]\models\varphi \\
\sigma\models\varphi\mathbin{\mathrm{U}}\psi &\iff \left(\exists j\;\left(\sigma[j..]\models\psi\land\forall i<j\;\left(\sigma[i..]\models\varphi\right)\right)\right)
\end{aligned}" />
</div>

---

# סמנטיקה של Until

<div class="mt-6 text-center text-[29px]" dir="ltr">
<KatexInline display math="\sigma\models\varphi\mathbin{\mathrm{U}}\psi \iff \left(\exists j\ge0\;\left(\sigma[j..]\models\psi\;\land\;\forall i<j\;\left(\sigma[i..]\models\varphi\right)\right)\right)" />
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-4 text-left" dir="ltr">
<div class="space-y-2 text-[18px] overflow-hidden">
<div v-click class="grid grid-cols-[42px_170px_1fr] gap-3 items-center">
<div class="text-emerald-600 font-bold text-[22px]">✓</div>
<div class="font-mono text-red-700">i=0 &lt; j</div>
<div class="relative h-8 bg-red-100 border border-red-300 flex items-center px-3 after:content-[''] after:absolute after:top-[-1px] after:left-full after:h-8 after:w-[280px] after:bg-red-100 after:border-y after:border-red-300 after:bg-[repeating-linear-gradient(90deg,#fee2e2_0,#fee2e2_18px,#fecaca_18px,#fecaca_20px)]"><KatexInline math="\sigma[0..]\models\varphi" /><span class="absolute left-[calc(100%+248px)] top-10 h-8 flex items-center text-red-500 text-[18px]">→</span></div>
</div>
<div v-click class="grid grid-cols-[42px_170px_1fr] gap-3 items-center">
<div class="text-emerald-600 font-bold text-[22px]">✓</div>
<div class="font-mono text-red-700">i=1 &lt; j</div>
<div class="relative h-8 bg-red-100 border border-red-300 flex items-center px-3 ml-8 after:content-[''] after:absolute after:top-[-1px] after:left-full after:h-8 after:w-[280px] after:bg-red-100 after:border-y after:border-red-300 after:bg-[repeating-linear-gradient(90deg,#fee2e2_0,#fee2e2_18px,#fecaca_18px,#fecaca_20px)]"><KatexInline math="\sigma[1..]\models\varphi" /><span class="absolute left-[calc(100%+248px)] top-0 h-8 flex items-center text-red-500 text-[18px]">→</span></div>
</div>
<div v-click class="grid grid-cols-[42px_170px_1fr] gap-3 items-center">
<div class="text-emerald-600 font-bold text-[22px]">✓</div>
<div class="font-mono text-red-700">i=2 &lt; j</div>
<div class="relative h-8 bg-red-100 border border-red-300 flex items-center px-3 ml-16 after:content-[''] after:absolute after:top-[-1px] after:left-full after:h-8 after:w-[280px] after:bg-red-100 after:border-y after:border-red-300 after:bg-[repeating-linear-gradient(90deg,#fee2e2_0,#fee2e2_18px,#fecaca_18px,#fecaca_20px)]"><KatexInline math="\sigma[2..]\models\varphi" /><span class="absolute left-[calc(100%+248px)] top-0 h-8 flex items-center text-red-500 text-[18px]">→</span></div>
</div>
<div v-click class="grid grid-cols-[42px_170px_1fr] gap-3 items-center">
<div class="text-emerald-600 font-bold text-[22px]">✓</div>
<div class="font-mono text-red-700">i=3 &lt; j</div>
<div class="relative h-8 bg-red-100 border border-red-300 flex items-center px-3 ml-24 after:content-[''] after:absolute after:top-[-1px] after:left-full after:h-8 after:w-[280px] after:bg-red-100 after:border-y after:border-red-300 after:bg-[repeating-linear-gradient(90deg,#fee2e2_0,#fee2e2_18px,#fecaca_18px,#fecaca_20px)]"><KatexInline math="\sigma[3..]\models\varphi" /><span class="absolute left-[calc(100%+248px)] top-0 h-8 flex items-center text-red-500 text-[18px]">→</span></div>
</div>
<div v-click class="grid grid-cols-[42px_170px_1fr] gap-3 items-center">
<div class="text-emerald-600 font-bold text-[22px]">✓</div>
<div class="font-mono text-blue-700">now j=4</div>
<div class="relative h-8 bg-blue-100 border-2 border-blue-500 flex items-center px-3 ml-32 after:content-[''] after:absolute after:top-[-2px] after:left-full after:h-8 after:w-[280px] after:bg-blue-100 after:border-y-2 after:border-blue-500 after:bg-[repeating-linear-gradient(90deg,#dbeafe_0,#dbeafe_18px,#bfdbfe_18px,#bfdbfe_20px)]"><KatexInline math="\sigma[4..]\models\psi" /><span class="absolute left-[calc(100%+248px)] top-0 h-8 flex items-center text-blue-500 text-[18px]">→</span></div>
</div>
</div>
</div>

<div v-click class="mt-7 text-center text-[21px]">
ה־<span dir="ltr"><KatexInline math="Until" /></span> הוא חזק: הוא דורש שבסוף אכן נגיע ל־<span dir="ltr"><KatexInline math="\psi" /></span>.
</div>

---

# סמנטיקה ישירה של האופרטורים הנגזרים

<div class="mt-5 grid grid-cols-1 gap-y-2 text-right text-[18px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-3 grid grid-cols-[170px_1fr] gap-8 items-center">
<div>מתישהו בעתיד.</div>
<div dir="ltr" class="grid grid-cols-[235px_64px_minmax(0,1fr)] gap-4 items-center text-[23px] leading-tight">
<div class="text-right"><KatexInline math="\sigma\models\Diamond\varphi" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left pl-3"><KatexInline math="\exists j\ge0\;\left(\sigma[j..]\models\varphi\right)" /></div>
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3 grid grid-cols-[170px_1fr] gap-8 items-center">
<div>בכל נקודה מעכשיו והלאה.</div>
<div dir="ltr" class="grid grid-cols-[235px_64px_minmax(0,1fr)] gap-4 items-center text-[23px] leading-tight">
<div class="text-right"><KatexInline math="\sigma\models\Box\varphi" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left pl-3"><KatexInline math="\forall j\ge0\;\left(\sigma[j..]\models\varphi\right)" /></div>
</div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3 grid grid-cols-[170px_1fr] gap-8 items-center">
<div>אינסוף פעמים.</div>
<div dir="ltr" class="grid grid-cols-[235px_64px_minmax(0,1fr)] gap-4 items-center text-[22px] leading-tight">
<div class="text-right"><KatexInline math="\sigma\models\Box\Diamond\varphi" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left pl-3"><KatexInline math="\forall i\ge0\;\left(\exists j\ge i\;\left(\sigma[j..]\models\varphi\right)\right)" /></div>
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-3 grid grid-cols-[170px_1fr] gap-8 items-center">
<div>בסופו של דבר תמיד.</div>
<div dir="ltr" class="grid grid-cols-[235px_64px_minmax(0,1fr)] gap-4 items-center text-[22px] leading-tight">
<div class="text-right"><KatexInline math="\sigma\models\Diamond\Box\varphi" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left pl-3"><KatexInline math="\exists i\ge0\;\left(\forall j\ge i\;\left(\sigma[j..]\models\varphi\right)\right)" /></div>
</div>
</div>
</div>

---

# סמנטיקה מעל מסלולים ומצבים

<div class="mt-6 text-right text-[21px] leading-relaxed">
תהי מערכת מעברים <span dir="ltr"><KatexInline math="TS=\langle S,Act,\to,I,AP,L\rangle" /></span> ללא מצבים סופיים, ו־<span dir="ltr"><KatexInline math="\varphi" /></span> נוסחת <span dir="ltr">LTL</span>.
</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מסלול</div>
<div dir="ltr" class="text-[19px] text-center leading-tight space-y-1">
<div><KatexInline math="\pi\models\varphi" /></div>
<div class="text-[17px]"><KatexInline math="\Updownarrow" /></div>
<div><KatexInline math="trace(\pi)\models\varphi" /></div>
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">מצב</div>
<div dir="ltr" class="text-[17px] text-center leading-tight space-y-1">
<div><KatexInline math="s\models\varphi" /></div>
<div class="text-[17px]"><KatexInline math="\Updownarrow" /></div>
<div class="whitespace-nowrap"><KatexInline math="\forall\pi\in Paths(s)\;\left(\pi\models\varphi\right)" /></div>
</div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">מערכת</div>
<div dir="ltr" class="text-[18px] text-center leading-tight space-y-1">
<div><KatexInline math="TS\models\varphi" /></div>
<div class="text-[17px]"><KatexInline math="\Updownarrow" /></div>
<div><KatexInline math="\forall s_0\in I\;\left(s_0\models\varphi\right)" /></div>
<div class="text-[17px]"><KatexInline math="\Updownarrow" /></div>
<div><KatexInline math="Traces(TS)\subseteq Words(\varphi)" /></div>
</div>
</div>
</div>

---

# דוגמה: מערכת מעברים קטנה

<TransitionSystemD3
  :width="520" :height="190" :auto="false"
  :states="[
    { id: 's1', text: '$s_1$', label: '\{a,b\}', x: 90, y: 95, width: 62, initial: true, initialDirection: 'left' },
    { id: 's2', text: '$s_2$', label: '\{a,b\}', x: 260, y: 95, width: 62 },
    { id: 's3', text: '$s_3$', label: '\{a\}', x: 430, y: 95, width: 62 }
  ]"
  :transitions="[
    { source: 's1', target: 's2', action: ' ' },
    { source: 's2', target: 's3', action: ' ' },
    { source: 's3', target: 's3', action: ' ', loopDirection: '90deg', loopRadius: 72, loopLabelRadius: 82 }
  ]"
/>

<div class="mt-8 grid grid-cols-2 gap-4 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div dir="ltr" class="text-left"><KatexInline math="TS\models\Box a" /></div>
<div dir="ltr" class="text-left"><KatexInline math="TS\models \Box(\neg b\Rightarrow\Box(a\land\neg b))" /></div>
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
<div dir="ltr" class="text-left"><KatexInline math="TS\not\models \bigcirc(a\land b)" /></div>
<div dir="ltr" class="text-left"><KatexInline math="TS\not\models b\mathbin{\mathrm{U}}(a\land\neg b)" /></div>
</div>
</div>

---

# נקודה מבלבלת: שלילה של מערכת

<div class="mt-7 text-right text-[21px] leading-relaxed">
עבור מילה או מסלול יחיד, <span dir="ltr"><KatexInline math="\pi\models\varphi" /></span> שקול לכך ש־<span dir="ltr"><KatexInline math="\pi\not\models\neg\varphi" /></span>.
אבל עבור מערכת מעברים, הכמת על כל המסלולים משנה את התמונה.
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr] gap-4 items-center text-[20px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">לא מקיימת את <span dir="ltr"><KatexInline math="\varphi" /></span></div>
יש מסלול אחד שמפר את <span dir="ltr"><KatexInline math="\varphi" /></span>.
</div>
<div class="text-[34px] text-slate-500">≠</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מקיימת את <span dir="ltr"><KatexInline math="\neg\varphi" /></span></div>
כל המסלולים מקיימים את השלילה.
</div>
</div>

<div class="mt-7 text-center text-[27px]" dir="ltr">
<KatexInline display math="TS\not\models\varphi\;\not\Rightarrow\;TS\models\neg\varphi" />
</div>

---

# שקילות של נוסחאות LTL

<div class="mt-7 text-right text-[22px] leading-relaxed">
נוסחאות <span dir="ltr"><KatexInline math="\varphi" /></span> ו־<span dir="ltr"><KatexInline math="\psi" /></span> שקולות, מסומן <span dir="ltr"><KatexInline math="\varphi\equiv\psi" /></span>, אם הן מגדירות אותה קבוצת מילים.
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="\varphi\equiv\psi \iff Words(\varphi)=Words(\psi)" />
</div>

<div class="mt-7 bg-amber-50 border border-amber-200 rounded p-5 text-right text-[21px] leading-relaxed">
תרגיל: האם שקילות של נוסחאות שקולה לכך שכל מערכת שמקיימת אחת מהן מקיימת גם את השנייה?
</div>

---

# דואליות ואידמפוטנטיות

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">דואליות</div>
<div dir="ltr" class="grid grid-cols-[150px_44px_1fr] gap-2 items-center text-[20px] leading-snug">
<div class="text-right"><KatexInline math="\neg\Box\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Diamond\neg\varphi" /></div>
<div class="text-right"><KatexInline math="\neg\Diamond\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Box\neg\varphi" /></div>
<div class="text-right"><KatexInline math="\neg\bigcirc\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\bigcirc\neg\varphi" /></div>
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">אידמפוטנטיות</div>
<div dir="ltr" class="grid grid-cols-[150px_44px_1fr] gap-2 items-center text-[20px] leading-snug">
<div class="text-right"><KatexInline math="\Box\Box\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Box\varphi" /></div>
<div class="text-right"><KatexInline math="\Diamond\Diamond\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Diamond\varphi" /></div>
<div class="text-right"><KatexInline math="\varphi\mathbin{\mathrm{U}}(\varphi\mathbin{\mathrm{U}}\psi)" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\varphi\mathbin{\mathrm{U}}\psi" /></div>
</div>
</div>
</div>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="mt-4 min-h-[150px]">
<div v-show="$slidev.nav.clicks === 0" class="pt-10 text-center text-[22px]">
הוכחות השקילות נעשות ישירות מהסמנטיקה של <span dir="ltr"><KatexInline math="\models" /></span>.
</div>

<div v-show="$slidev.nav.clicks === 1" class="bg-slate-50 border border-slate-200 rounded p-2 text-[15px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\neg\Box\varphi
&\iff \sigma\not\models\Box\varphi\\
&\iff \exists j\ge0\;\left(\sigma[j..]\models\neg\varphi\right)\\
&\iff \sigma\models\Diamond\neg\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 2" class="bg-slate-50 border border-slate-200 rounded p-2 text-[15px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\neg\Diamond\varphi
&\iff \sigma\not\models\Diamond\varphi\\
&\iff \nexists j\ge0\;\left(\sigma[j..]\models\varphi\right)\\
&\iff \forall j\ge0\;\left(\sigma[j..]\models\neg\varphi\right)\\
&\iff \sigma\models\Box\neg\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 3" class="bg-slate-50 border border-slate-200 rounded p-2 text-[15px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\neg\bigcirc\varphi
&\iff \sigma[1..]\not\models\varphi\\
&\iff \sigma[1..]\models\neg\varphi\\
&\iff \sigma\models\bigcirc\neg\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 4" class="bg-slate-50 border border-slate-200 rounded p-2 text-[15px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\Box\Box\varphi
&\iff \forall i\ge0\;\left(\sigma[i..]\models\Box\varphi\right)\\
&\iff \forall i\ge0\;\forall j\ge i\;\left(\sigma[j..]\models\varphi\right)\\
&\iff \forall j\ge0\;\left(\sigma[j..]\models\varphi\right)\\
&\iff \sigma\models\Box\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 5" class="bg-slate-50 border border-slate-200 rounded p-2 text-[15px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\Diamond\Diamond\varphi
&\iff \exists i\ge0\;\left(\sigma[i..]\models\Diamond\varphi\right)\\
&\iff \exists i\ge0\;\exists j\ge i\;\left(\sigma[j..]\models\varphi\right)\\
&\iff \exists j\ge0\;\left(\sigma[j..]\models\varphi\right)\\
&\iff \sigma\models\Diamond\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 6" class="bg-slate-50 border border-slate-200 rounded p-2 text-[15px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\varphi\mathbin{\mathrm{U}}(\varphi\mathbin{\mathrm{U}}\psi)
&\iff \exists k\ge0\;\left(\sigma[k..]\models\varphi\mathbin{\mathrm{U}}\psi\land\forall i<k\;\left(\sigma[i..]\models\varphi\right)\right)\\
&\iff \exists j\ge0\;\left(\sigma[j..]\models\psi\land\forall i<j\;\left(\sigma[i..]\models\varphi\right)\right)\\
&\iff \sigma\models\varphi\mathbin{\mathrm{U}}\psi
\end{aligned}" />
</div>
</div>

---

# כללי ספיגה ופילוג

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">ספיגה</div>
<div dir="ltr" class="grid grid-cols-[160px_44px_1fr] gap-2 items-center text-[19px] leading-snug">
<div class="text-right"><KatexInline math="\Diamond\Box\Diamond\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Box\Diamond\varphi" /></div>
<div class="text-right"><KatexInline math="\Box\Diamond\Box\varphi" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Diamond\Box\varphi" /></div>
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">פילוג שמתקיים</div>
<div dir="ltr" class="grid grid-cols-[160px_44px_1fr] gap-2 items-center text-[17px] leading-snug">
<div class="text-right"><KatexInline math="\bigcirc(\varphi\mathbin{\mathrm{U}}\psi)" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="(\bigcirc\varphi)\mathbin{\mathrm{U}}(\bigcirc\psi)" /></div>
<div class="text-right"><KatexInline math="\Diamond(\varphi\lor\psi)" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Diamond\varphi\lor\Diamond\psi" /></div>
<div class="text-right"><KatexInline math="\Box(\varphi\land\psi)" /></div>
<div class="text-center"><KatexInline math="\equiv" /></div>
<div class="text-left"><KatexInline math="\Box\varphi\land\Box\psi" /></div>
</div>
</div>
</div>

<div class="mt-4 bg-red-50 border border-red-200 rounded p-3 text-right text-[20px] leading-relaxed">
<div class="font-bold text-red-700 mb-1">אבל בדרך כלל</div>
<div dir="ltr" class="grid grid-cols-[250px_70px_250px] justify-center gap-2 items-center text-[19px] leading-snug">
<div class="text-right"><KatexInline math="\Diamond(\varphi\land\psi)" /></div>
<div class="text-center"><KatexInline math="\not\equiv" /></div>
<div class="text-left"><KatexInline math="\Diamond\varphi\land\Diamond\psi" /></div>
</div>
</div>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="mt-3 min-h-[136px]">
<div v-show="$slidev.nav.clicks === 0" class="pt-8 text-center text-[21px]">
גם כאן ההוכחות הן פריסה ישירה של הסמנטיקה מעל כל מיקום במסלול.
</div>

<div v-show="$slidev.nav.clicks === 1" class="bg-slate-50 border border-slate-200 rounded p-2 text-[14px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\Diamond\Box\Diamond\varphi
&\iff \exists i\ge0\;\left(\forall j\ge i\;\exists k\ge j\;\left(\sigma[k..]\models\varphi\right)\right)\\
&\iff \forall j\ge0\;\exists k\ge j\;\left(\sigma[k..]\models\varphi\right)\\
&\iff \sigma\models\Box\Diamond\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 2" class="bg-slate-50 border border-slate-200 rounded p-2 text-[14px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\Box\Diamond\Box\varphi
&\iff \forall i\ge0\;\exists j\ge i\;\forall k\ge j\;\left(\sigma[k..]\models\varphi\right)\\
&\iff \exists j\ge0\;\forall k\ge j\;\left(\sigma[k..]\models\varphi\right)\\
&\iff \sigma\models\Diamond\Box\varphi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 3" class="bg-slate-50 border border-slate-200 rounded p-2 text-[14px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\bigcirc(\varphi\mathbin{\mathrm{U}}\psi)
&\iff \sigma[1..]\models\varphi\mathbin{\mathrm{U}}\psi\\
&\iff \sigma\models(\bigcirc\varphi)\mathbin{\mathrm{U}}(\bigcirc\psi)
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 4" class="bg-slate-50 border border-slate-200 rounded p-2 text-[14px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\Diamond(\varphi\lor\psi)
&\iff \exists j\ge0\;\left(\sigma[j..]\models\varphi\lor\psi\right)\\
&\iff \sigma\models\Diamond\varphi\lor\Diamond\psi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 5" class="bg-slate-50 border border-slate-200 rounded p-2 text-[14px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\sigma\models\Box(\varphi\land\psi)
&\iff \forall j\ge0\;\left(\sigma[j..]\models\varphi\land\psi\right)\\
&\iff \sigma\models\Box\varphi\land\Box\psi
\end{aligned}" />
</div>

<div v-show="$slidev.nav.clicks === 6" class="bg-red-50 border border-red-200 rounded p-2 text-[14px]" dir="ltr">
<KatexInline display math="\begin{aligned}
\varphi&=a,\quad \psi=b\\
\sigma[0]&=\{a\},\quad \sigma[1]=\{b\},\quad \sigma[i]=\emptyset\ (i\ge2)\\
\sigma&\models\Diamond a\land\Diamond b\\
\sigma&\not\models\Diamond(a\land b)
\end{aligned}" />
</div>
</div>

---

# כללי הפריסה

<div class="mt-7 text-right text-[21px] leading-relaxed">
כללי הפריסה מציגים את אופרטורי הזמן באופן רקורסיבי:
</div>

<div class="mt-5 grid grid-cols-1 gap-3 text-center text-[28px]" dir="ltr">
<div class="bg-blue-50 border border-blue-200 rounded p-3 whitespace-nowrap">
<KatexInline math="\varphi\mathbin{\mathrm{U}}\psi \equiv \psi\lor(\varphi\land\bigcirc(\varphi\mathbin{\mathrm{U}}\psi))" />
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 whitespace-nowrap">
<KatexInline math="\Diamond\varphi\equiv\varphi\lor\bigcirc\Diamond\varphi" />
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-3 whitespace-nowrap">
<KatexInline math="\Box\varphi\equiv\varphi\land\bigcirc\Box\varphi" />
</div>
</div>

<div class="mt-6 text-center text-[22px]">
אלה הכללים שמאפשרים לחשוב על נוסחת <span dir="ltr">LTL</span> כמו על מצב נוכחי והמשך.
</div>

---

# ניסיון ראשון: Weak Until

<div class="mt-7 text-right text-[21px] leading-relaxed">
כדי לדחוף שלילות פנימה נרצה, לכל קשר, קשר דואלי. עבור <span dir="ltr"><KatexInline math="\mathrm{U}" /></span> אפשר להגדיר תחילה את <span dir="ltr"><KatexInline math="\mathrm{W}" /></span>, הנקרא לפעמים <span dir="ltr">unless</span>:
</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline display math="\varphi\mathbin{\mathrm{W}}\psi \equiv (\varphi\mathbin{\mathrm{U}}\psi)\lor\Box\varphi" />
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
ב־<span dir="ltr"><KatexInline math="\varphi\mathbin{\mathrm{U}}\psi" /></span> חייבים להגיע בסוף ל־<span dir="ltr"><KatexInline math="\psi" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
ב־<span dir="ltr"><KatexInline math="\varphi\mathbin{\mathrm{W}}\psi" /></span> מותר לא להגיע ל־<span dir="ltr"><KatexInline math="\psi" /></span>, אם <span dir="ltr"><KatexInline math="\varphi" /></span> ממשיכה להתקיים לנצח.
</div>
</div>

<div class="mt-6 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[20px] leading-relaxed">
זה מספיק אקספרסיבית, אבל לא תמיד מספיק טוב אלגוריתמית: המרה דרך <span dir="ltr"><KatexInline math="\mathrm{W}" /></span> עלולה לנפח נוסחאות באופן אקספוננציאלי.
</div>

---

# Release

<div class="mt-7 text-right text-[21px] leading-relaxed">
הפתרון הוא להשתמש בדואלי הישיר של <span dir="ltr"><KatexInline math="\mathrm{U}" /></span>: הקשר <span dir="ltr"><KatexInline math="\mathrm{R}" /></span>, הנקרא <span dir="ltr">Release</span>.
</div>

<div class="mt-5 text-center text-[29px]" dir="ltr">
<KatexInline display math="\varphi\mathbin{\mathrm{R}}\psi \equiv \neg(\neg\varphi\mathbin{\mathrm{U}}\neg\psi)" />
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-5 text-right text-[21px] leading-relaxed">
האינטואיציה: <span dir="ltr"><KatexInline math="\psi" /></span> חייבת להתקיים עד וכולל הזמן שבו <span dir="ltr"><KatexInline math="\varphi" /></span> מתקיימת בפעם הראשונה.
אם <span dir="ltr"><KatexInline math="\varphi" /></span> לא מתקיימת אף פעם, אז <span dir="ltr"><KatexInline math="\psi" /></span> חייבת להתקיים לנצח.
</div>

<div class="mt-6 text-center text-[26px]" dir="ltr">
<KatexInline display math="\Box\psi\equiv false\mathbin{\mathrm{R}}\psi" />
</div>

<div class="mt-5 bg-emerald-50 border border-emerald-200 rounded p-4 text-right text-[20px] leading-relaxed">
עכשיו אפשר להחליף שלילה של <span dir="ltr"><KatexInline math="\mathrm{U}" /></span> ב־<span dir="ltr"><KatexInline math="\mathrm{R}" /></span> בלי לשכפל את תת־הנוסחאות.
</div>

---

# צורה חיובית נורמלית בלי ניפוח

<div class="mt-7 text-right text-[21px] leading-relaxed">
בזכות הדואלים של הקשרים אפשר להגיע ל־<span dir="ltr">Positive Normal Form</span>: שלילה מופיעה רק ליד פסוקים אטומיים.
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="\varphi ::= true \mid false \mid a \mid \neg a \mid \varphi_1\land\varphi_2 \mid \varphi_1\lor\varphi_2 \mid \bigcirc\varphi \mid \varphi_1\mathbin{\mathrm{U}}\varphi_2 \mid \varphi_1\mathbin{\mathrm{R}}\varphi_2" />
</div>

<div class="mt-7 grid grid-cols-2 gap-4 text-right text-[20px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">ניסיון עם <span dir="ltr"><KatexInline math="\mathrm{W}" /></span></div>
אפשר לדחוף שלילות פנימה, אבל במקרים מסוימים מתקבל ניפוח אקספוננציאלי.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">עם <span dir="ltr"><KatexInline math="\mathrm{R}" /></span></div>
מקבלים אותה צורה נורמלית, אבל ההמרה שומרת על גודל ליניארי.
</div>
</div>

---

# התמרות ל-PNF

<div class="mt-5 text-right text-[20px] leading-relaxed">
כל כלל מחליף קשר בקשר הדואלי שלו, וכך השלילה “יורדת” שלב אחד פנימה:
</div>

<div class="mt-4 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div dir="ltr"><KatexInline math="\neg true \rightsquigarrow false" /></div>
<div dir="ltr"><KatexInline math="\neg\neg\varphi \rightsquigarrow \varphi" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1\land\varphi_2)\rightsquigarrow\neg\varphi_1\lor\neg\varphi_2" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1\lor\varphi_2)\rightsquigarrow\neg\varphi_1\land\neg\varphi_2" /></div>
</div>
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div dir="ltr"><KatexInline math="\neg\bigcirc\varphi\rightsquigarrow\bigcirc\neg\varphi" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1\mathbin{\mathrm{U}}\varphi_2)\rightsquigarrow\neg\varphi_1\mathbin{\mathrm{R}}\neg\varphi_2" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1\mathbin{\mathrm{R}}\varphi_2)\rightsquigarrow\neg\varphi_1\mathbin{\mathrm{U}}\neg\varphi_2" /></div>
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline display math="\forall\varphi\;\left(\exists\psi\in PNF\;\left(\varphi\equiv\psi\;\land\;|\psi|=O(|\varphi|)\right)\right)" />
</div>

---

# סיכום

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">LTL היא שפה לתכונות עקבות</div>
נוסחה מגדירה קבוצת מילים אינסופיות מעל <span dir="ltr"><KatexInline math="2^{AP}" /></span>.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">הסמנטיקה היא אוניברסלית על מסלולי TS</div>
מערכת מקיימת נוסחה אם כל העקבות שלה נמצאות בשפה שהנוסחה מגדירה.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">השקילויות הן כלי עבודה</div>
דואליות, פריסה, ספיגה ופילוג מאפשרים לפשט ולהמיר נוסחאות.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">לקראת האימות</div>
בהמשך נתרגם נוסחאות <span dir="ltr">LTL</span> לאוטומטי Büchi ונשתמש במנגנון של אימות <span dir="ltr"><KatexInline math="\omega" /></span>-רגולרי.
</div>
</div>
