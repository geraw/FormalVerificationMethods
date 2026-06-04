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
<div dir="ltr" class="mt-4 text-center text-[28px]"><KatexInline math="init\;U\;ready" /></div>
</div>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[17px] leading-relaxed">
<span class="font-bold">מקרא אופרטורים:</span>
<span dir="ltr" class="mr-3"><KatexInline math="\Box" /></span> תמיד,
<span dir="ltr" class="mr-3"><KatexInline math="\bigcirc" /></span> בצעד הבא,
<span dir="ltr" class="mr-3"><KatexInline math="U" /></span> עד ש־.
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
<KatexInline display math="\varphi ::= true \mid a \mid \varphi_1\land\varphi_2 \mid \neg\varphi \mid \bigcirc\varphi \mid \varphi_1\,U\,\varphi_2" />
</div>

<div class="mt-7 grid grid-cols-2 gap-4 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<span dir="ltr"><KatexInline math="\bigcirc\varphi" /></span> אומר: <span class="font-bold">בצעד הבא</span> תתקיים <span dir="ltr"><KatexInline math="\varphi" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<span dir="ltr"><KatexInline math="\varphi_1 U \varphi_2" /></span> אומר: <span dir="ltr"><KatexInline math="\varphi_1" /></span> תתקיים עד ש־<span dir="ltr"><KatexInline math="\varphi_2" /></span> תתקיים.
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
<div dir="ltr" class="text-[20px]"><KatexInline math="\{\sigma:\underset{\infty}{\exists} i.\;crit_1\in\sigma[i]\;\land\;\underset{\infty}{\exists} i.\;crit_2\in\sigma[i]\}" /></div>
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
<div dir="ltr" class="text-center text-[25px]"><KatexInline math="\Box\neg output\lor(\neg output\;U\;input)" /></div>
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
\sigma\models\varphi\mathbin{\mathrm{U}}\psi &\iff \left(\exists j\;\left(\sigma[j..]\models\psi\land\forall i<j\;\sigma[i..]\models\varphi\right)\right)
\end{aligned}" />
</div>

---

# סמנטיקה של Until

<div class="mt-6 text-center text-[29px]" dir="ltr">
<KatexInline display math="\sigma\models\varphi\mathbin{\mathrm{U}}\psi \iff \left(\exists j\ge 0\;\left(\sigma[j..]\models\psi\;\land\;\forall i<j\;\sigma[i..]\models\varphi\right)\right)" />
</div>

<div class="mt-3 text-center text-[20px]">
בכל אינדקס <span dir="ltr"><KatexInline math="k" /></span> בודקים את הנוסחה על הזנב <span dir="ltr"><KatexInline math="\sigma[k..]" /></span> בלבד.
</div>

<div class="mt-5 bg-slate-50 border border-slate-200 rounded p-4" dir="ltr">
  <svg viewBox="0 0 760 305" class="w-full h-[305px]">
    <defs>
      <pattern id="cellsGray" width="18" height="20" patternUnits="userSpaceOnUse">
        <rect width="18" height="20" fill="#d1d5db" />
        <line x1="18" y1="0" x2="18" y2="20" stroke="#6b7280" stroke-width="1" />
      </pattern>
      <pattern id="cellsRed" width="18" height="20" patternUnits="userSpaceOnUse">
        <rect width="18" height="20" fill="#fca5a5" />
        <line x1="18" y1="0" x2="18" y2="20" stroke="#ef4444" stroke-width="1" />
      </pattern>
      <pattern id="cellsBlue" width="18" height="20" patternUnits="userSpaceOnUse">
        <rect width="18" height="20" fill="#93c5fd" />
        <line x1="18" y1="0" x2="18" y2="20" stroke="#2563eb" stroke-width="1" />
      </pattern>
      <marker id="redArrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
        <polygon points="0 0, 7 3.5, 0 7" fill="#dc2626" />
      </marker>
      <marker id="blueArrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
        <polygon points="0 0, 7 3.5, 0 7" fill="#2563eb" />
      </marker>
    </defs>

    <text x="12" y="18" font-size="22" fill="#111827">σ |= φ₁ U ψ₂</text>
    <rect x="12" y="28" width="736" height="20" fill="url(#cellsGray)" stroke="#4b5563" />

    <text x="118" y="77" font-size="18" fill="#111827">σ[4..] |= </text>
    <text x="198" y="77" font-size="18" fill="#1d4ed8">ψ₂</text>
    <rect x="92" y="84" width="656" height="20" fill="url(#cellsBlue)" stroke="#2563eb" />
    <line x1="98" y1="50" x2="98" y2="82" stroke="#2563eb" stroke-width="3" marker-end="url(#blueArrow)" />

    <text x="98" y="125" font-size="18" fill="#111827">σ[3..] |= </text>
    <text x="178" y="125" font-size="18" fill="#dc2626">φ₁</text>
    <rect x="74" y="132" width="674" height="20" fill="url(#cellsRed)" stroke="#ef4444" />
    <line x1="80" y1="50" x2="80" y2="130" stroke="#dc2626" stroke-width="3" marker-end="url(#redArrow)" />

    <text x="74" y="173" font-size="18" fill="#111827">σ[2..] |= </text>
    <text x="154" y="173" font-size="18" fill="#dc2626">φ₁</text>
    <rect x="56" y="180" width="692" height="20" fill="url(#cellsRed)" stroke="#ef4444" />
    <line x1="62" y1="50" x2="62" y2="178" stroke="#dc2626" stroke-width="3" marker-end="url(#redArrow)" />

    <text x="50" y="221" font-size="18" fill="#111827">σ[1..] |= </text>
    <text x="130" y="221" font-size="18" fill="#dc2626">φ₁</text>
    <rect x="38" y="228" width="710" height="20" fill="url(#cellsRed)" stroke="#ef4444" />
    <line x1="44" y1="50" x2="44" y2="226" stroke="#dc2626" stroke-width="3" marker-end="url(#redArrow)" />

    <text x="30" y="269" font-size="18" fill="#111827">σ[0..] |= </text>
    <text x="110" y="269" font-size="18" fill="#dc2626">φ₁</text>
    <rect x="12" y="276" width="736" height="20" fill="url(#cellsRed)" stroke="#ef4444" />
    <line x1="26" y1="50" x2="26" y2="274" stroke="#dc2626" stroke-width="3" marker-end="url(#redArrow)" />
  </svg>
</div>

<div class="mt-7 text-center text-[21px]">
ה־<span dir="ltr"><KatexInline math="Until" /></span> הוא חזק: הוא דורש שבסוף אכן נגיע ל־<span dir="ltr"><KatexInline math="\psi" /></span>.
</div>

---

# סמנטיקה של האופרטורים הנגזרים

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div dir="ltr" class="text-[26px]"><KatexInline math="\sigma\models\Diamond\varphi \iff \exists j\ge0.\;\sigma[j..]\models\varphi" /></div>
<div class="mt-2">מתישהו בעתיד.</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div dir="ltr" class="text-[26px]"><KatexInline math="\sigma\models\Box\varphi \iff \forall j\ge0.\;\sigma[j..]\models\varphi" /></div>
<div class="mt-2">בכל נקודה מעכשיו והלאה.</div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div dir="ltr" class="text-[26px]"><KatexInline math="\sigma\models\Box\Diamond\varphi \iff \forall i\ge0.\exists j\ge i.\;\sigma[j..]\models\varphi" /></div>
<div class="mt-2">אינסוף פעמים.</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div dir="ltr" class="text-[26px]"><KatexInline math="\sigma\models\Diamond\Box\varphi \iff \exists i\ge0.\forall j\ge i.\;\sigma[j..]\models\varphi" /></div>
<div class="mt-2">בסופו של דבר תמיד.</div>
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
<div dir="ltr" class="text-[24px]"><KatexInline math="\pi\models\varphi \iff trace(\pi)\models\varphi" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">מצב</div>
<div dir="ltr" class="text-[24px]"><KatexInline math="s\models\varphi \iff \forall\pi\in Paths(s).\;\pi\models\varphi" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">מערכת</div>
<div dir="ltr" class="text-[24px]"><KatexInline math="TS\models\varphi \iff Traces(TS)\subseteq Words(\varphi)" /></div>
</div>
</div>

<div class="mt-7 text-center text-[24px]" dir="ltr">
<KatexInline display math="TS\models\varphi \iff \forall s_0\in I.\;s_0\models\varphi" />
</div>

---

# דוגמה: מערכת מעברים קטנה

<div class="mt-8 flex justify-center items-center gap-6" dir="ltr">
<div class="bg-blue-50 border border-blue-300 rounded-full w-20 h-20 flex flex-col items-center justify-center">
<div class="font-bold">s1</div><div>{a,b}</div>
</div>
<div class="text-[34px] text-slate-500">→</div>
<div class="bg-blue-50 border border-blue-300 rounded-full w-20 h-20 flex flex-col items-center justify-center">
<div class="font-bold">s2</div><div>{a,b}</div>
</div>
<div class="text-[34px] text-slate-500">→</div>
<div class="bg-blue-50 border border-blue-300 rounded-full w-20 h-20 flex flex-col items-center justify-center">
<div class="font-bold">s3</div><div>{a}</div>
</div>
<div class="text-[34px] text-slate-500">↺</div>
</div>

<div class="mt-8 grid grid-cols-2 gap-4 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div dir="ltr"><KatexInline math="TS\models\Box a" /></div>
<div dir="ltr"><KatexInline math="TS\models \Box(\neg b\Rightarrow\Box(a\land\neg b))" /></div>
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
<div dir="ltr"><KatexInline math="TS\not\models \bigcirc(a\land b)" /></div>
<div dir="ltr"><KatexInline math="TS\not\models b\,U\,(a\land\neg b)" /></div>
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

# דוגמה: הוגנות אינה מובטחת בלי הנחות

<div class="mt-7 text-right text-[21px] leading-relaxed">
במערכת סמפורים אפשר להוכיח מניעה הדדית, אבל לא בהכרח התקדמות הוגנת של שני התהליכים.
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">נכון</div>
<div dir="ltr" class="text-[27px]"><KatexInline math="TS_{sem}\models\Box(\neg crit_1\lor\neg crit_2)" /></div>
<div dir="ltr" class="text-[27px]"><KatexInline math="TS_{sem}\models\Box\Diamond crit_1\lor\Box\Diamond crit_2" /></div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">לא נובע בלי הוגנות</div>
<div dir="ltr" class="text-[27px]"><KatexInline math="TS_{sem}\not\models\Box\Diamond crit_1\land\Box\Diamond crit_2" /></div>
<div dir="ltr" class="text-[27px]"><KatexInline math="TS_{sem}\not\models\Box\Diamond wait_1\Rightarrow\Box\Diamond crit_1" /></div>
</div>
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
<div dir="ltr"><KatexInline math="\neg\Box\varphi\equiv\Diamond\neg\varphi" /></div>
<div dir="ltr"><KatexInline math="\neg\Diamond\varphi\equiv\Box\neg\varphi" /></div>
<div dir="ltr"><KatexInline math="\neg\bigcirc\varphi\equiv\bigcirc\neg\varphi" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">אידמפוטנטיות</div>
<div dir="ltr"><KatexInline math="\Box\Box\varphi\equiv\Box\varphi" /></div>
<div dir="ltr"><KatexInline math="\Diamond\Diamond\varphi\equiv\Diamond\varphi" /></div>
<div dir="ltr"><KatexInline math="\varphi U(\varphi U\psi)\equiv\varphi U\psi" /></div>
</div>
</div>

<div class="mt-7 text-center text-[22px]">
הוכחות השקילות נעשות ישירות מהסמנטיקה של <span dir="ltr"><KatexInline math="\models" /></span>.
</div>

---

# דוגמה: הוכחת דואליות

<div class="mt-6 text-right text-[22px] leading-relaxed">
נוכיח:
</div>

<div class="text-center text-[31px]" dir="ltr">
<KatexInline display math="\neg\Diamond\varphi\equiv\Box\neg\varphi" />
</div>

<div class="mt-5 bg-slate-50 border border-slate-200 rounded p-5 text-[22px]" dir="ltr">
<div><KatexInline math="\sigma\models\neg\Diamond\varphi" /></div>
<div><KatexInline math="\iff \sigma\not\models\Diamond\varphi" /></div>
<div><KatexInline math="\iff \nexists j\ge0.\;\sigma[j..]\models\varphi" /></div>
<div><KatexInline math="\iff \forall j\ge0.\;\sigma[j..]\models\neg\varphi" /></div>
<div><KatexInline math="\iff \sigma\models\Box\neg\varphi" /></div>
</div>

---

# כללי ספיגה ופילוג

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">ספיגה</div>
<div dir="ltr"><KatexInline math="\Diamond\Box\Diamond\varphi\equiv\Box\Diamond\varphi" /></div>
<div dir="ltr"><KatexInline math="\Box\Diamond\Box\varphi\equiv\Diamond\Box\varphi" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">פילוג שמתקיים</div>
<div dir="ltr"><KatexInline math="\bigcirc(\varphi U\psi)\equiv(\bigcirc\varphi)U(\bigcirc\psi)" /></div>
<div dir="ltr"><KatexInline math="\Diamond(\varphi\lor\psi)\equiv\Diamond\varphi\lor\Diamond\psi" /></div>
<div dir="ltr"><KatexInline math="\Box(\varphi\land\psi)\equiv\Box\varphi\land\Box\psi" /></div>
</div>
</div>

<div class="mt-7 bg-red-50 border border-red-200 rounded p-4 text-right text-[20px] leading-relaxed">
אבל בדרך כלל: <span dir="ltr"><KatexInline math="\Diamond(\varphi\land\psi)\not\equiv\Diamond\varphi\land\Diamond\psi" /></span>.
</div>

---

# כללי הפריסה

<div class="mt-7 text-right text-[21px] leading-relaxed">
כללי הפריסה מציגים את אופרטורי הזמן באופן רקורסיבי:
</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-center text-[22px]" dir="ltr">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<KatexInline math="\varphi U\psi \equiv \psi\lor(\varphi\land\bigcirc(\varphi U\psi))" />
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<KatexInline math="\Diamond\varphi\equiv\varphi\lor\bigcirc\Diamond\varphi" />
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
<KatexInline math="\Box\varphi\equiv\varphi\land\bigcirc\Box\varphi" />
</div>
</div>

<div class="mt-8 text-center text-[22px]">
אלה הכללים שמאפשרים לחשוב על נוסחת <span dir="ltr">LTL</span> כמו על מצב נוכחי והמשך.
</div>

---

# Weak Until

<div class="mt-7 text-right text-[21px] leading-relaxed">
הקשר <span dir="ltr"><KatexInline math="W" /></span>, הנקרא לפעמים <span dir="ltr">unless</span>, הוא גרסה חלשה של <span dir="ltr"><KatexInline math="U" /></span>:
</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline display math="\varphi W\psi \equiv (\varphi U\psi)\lor\Box\varphi" />
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
ב־<span dir="ltr"><KatexInline math="\varphi U\psi" /></span> חייבים להגיע בסוף ל־<span dir="ltr"><KatexInline math="\psi" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
ב־<span dir="ltr"><KatexInline math="\varphi W\psi" /></span> מותר לא להגיע ל־<span dir="ltr"><KatexInline math="\psi" /></span>, אם <span dir="ltr"><KatexInline math="\varphi" /></span> ממשיכה להתקיים לנצח.
</div>
</div>

---

# Release

<div class="mt-7 text-right text-[21px] leading-relaxed">
הקשר <span dir="ltr"><KatexInline math="R" /></span> הוא הדואלי של <span dir="ltr"><KatexInline math="U" /></span>:
</div>

<div class="mt-5 text-center text-[29px]" dir="ltr">
<KatexInline display math="\varphi R\psi \equiv \neg(\neg\varphi U\neg\psi)" />
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-5 text-right text-[21px] leading-relaxed">
האינטואיציה: <span dir="ltr"><KatexInline math="\psi" /></span> חייבת להתקיים עד וכולל הזמן שבו <span dir="ltr"><KatexInline math="\varphi" /></span> מתקיימת בפעם הראשונה.
אם <span dir="ltr"><KatexInline math="\varphi" /></span> לא מתקיימת אף פעם, אז <span dir="ltr"><KatexInline math="\psi" /></span> חייבת להתקיים לנצח.
</div>

<div class="mt-6 text-center text-[26px]" dir="ltr">
<KatexInline display math="\Box\psi\equiv false\,R\,\psi" />
</div>

---

# צורה חיובית נורמלית

<div class="mt-7 text-right text-[21px] leading-relaxed">
ב־<span dir="ltr">Positive Normal Form</span> שלילה מופיעה רק ליד פסוקים אטומיים.
</div>

<div class="mt-5 text-center text-[27px]" dir="ltr">
<KatexInline display math="\varphi ::= true \mid false \mid a \mid \neg a \mid \varphi_1\land\varphi_2 \mid \varphi_1\lor\varphi_2 \mid \bigcirc\varphi \mid \varphi_1 U\varphi_2 \mid \varphi_1 R\varphi_2" />
</div>

<div class="mt-7 grid grid-cols-2 gap-4 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
עם <span dir="ltr"><KatexInline math="W" /></span> בלבד עלול להיווצר ניפוח אקספוננציאלי.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
עם <span dir="ltr"><KatexInline math="R" /></span> אפשר להכניס שלילה פנימה בגודל ליניארי.
</div>
</div>

---

# התמרות ל-PNF

<div class="mt-6 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div dir="ltr"><KatexInline math="\neg true \rightsquigarrow false" /></div>
<div dir="ltr"><KatexInline math="\neg\neg\varphi \rightsquigarrow \varphi" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1\land\varphi_2)\rightsquigarrow\neg\varphi_1\lor\neg\varphi_2" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1\lor\varphi_2)\rightsquigarrow\neg\varphi_1\land\neg\varphi_2" /></div>
</div>
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div dir="ltr"><KatexInline math="\neg\bigcirc\varphi\rightsquigarrow\bigcirc\neg\varphi" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1 U\varphi_2)\rightsquigarrow\neg\varphi_1 R\neg\varphi_2" /></div>
<div dir="ltr"><KatexInline math="\neg(\varphi_1 R\varphi_2)\rightsquigarrow\neg\varphi_1 U\neg\varphi_2" /></div>
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline display math="\forall\varphi\;\exists\psi\in PNF.\quad \varphi\equiv\psi\;\land\;|\psi|=O(|\varphi|)" />
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
