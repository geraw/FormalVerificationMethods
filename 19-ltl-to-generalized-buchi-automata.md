---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 19-ltl-to-generalized-buchi-automata
htmlAttrs:
  dir: rtl
  lang: he
drawings:
  enabled: true
info: |
  ## תרגום LTL לאוטומטי Büchi מוכללים
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תרגום LTL לאוטומטי Büchi מוכללים

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# ראשי פרקים

<div class="grid grid-cols-3 gap-4 mt-8 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">רדוקציה</div>
נראה איך בדיקת <span dir="ltr">LTL</span> הופכת לחיפוש ריצה מקבלת במכפלה עם אוטומט.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">בניית האוטומט</div>
נבנה <span dir="ltr">GNBA</span> שמקבל בדיוק את המילים שמקיימות נוסחת <span dir="ltr">LTL</span>.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">הבטחות Until</div>
נבין למה תנאי הקבלה נועד לוודא שכל הבטחת <span dir="ltr">Until</span> אכן מתממשת.
</div>
</div>

---

# היעד: בדיקת תכונת LTL

<div class="mt-7 text-right text-[22px] leading-relaxed">
בהינתן מערכת מעברים <span dir="ltr"><KatexInline math="TS" /></span> ונוסחת <span dir="ltr"><KatexInline math="\varphi" /></span>, נרצה להחליט:
</div>

<div class="mt-6 text-center text-[34px]" dir="ltr">
<KatexInline display math="TS\models\varphi" />
</div>

<div class="mt-8 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">כן</div>
כל עקבה של המערכת מקיימת את הנוסחה.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">לא</div>
יש עקבה של המערכת שמפרה את הנוסחה, והיא תהיה הדוגמה הנגדית.
</div>
</div>

---

# מאימות LTL לאי־ריקות

<div class="mt-7 text-right text-[21px] leading-relaxed">
הרעיון האוטומטי: במקום לבדוק את <span dir="ltr"><KatexInline math="\varphi" /></span> ישירות, מחפשים עקבה שמקיימת את <span dir="ltr"><KatexInline math="\neg\varphi" /></span>.
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="TS\models\varphi \iff Traces(TS)\cap Words(\neg\varphi)=\emptyset" />
</div>

<div class="mt-6 grid grid-cols-[1fr_auto_1fr] gap-4 items-center text-center text-[20px]">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
מערכת המעברים<br />
<span dir="ltr"><KatexInline math="TS" /></span>
</div>
<div class="text-[34px]">×</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
אוטומט עבור ההפרה<br />
<span dir="ltr"><KatexInline math="\mathcal{A}_{\neg\varphi}" /></span>
</div>
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[20px] leading-relaxed">
אם במכפלה יש ריצה מקבלת, היא מתארת בדיוק עקבה מפרה של המערכת. אם אין ריצה כזאת, המערכת מקיימת את הנוסחה.
</div>

---

# מה נבנה היום?

<div class="absolute top-[30px] left-[72px] flex gap-5 items-start">
<div class="text-center">
<img src="./public/moshe-vardi.png" class="h-[108px] mx-auto object-contain" />
<div class="mt-1 text-[16px]">משה ורדי</div>
</div>
<div class="text-center">
<img src="./public/pierre-wolper.png" class="h-[108px] mx-auto object-contain" />
<div class="mt-1 text-[16px]">פייר וולפר</div>
</div>
</div>

<div class="mt-5 text-right text-[22px] leading-relaxed max-w-[720px]">
לכל נוסחת <span dir="ltr">LTL</span> <span dir="ltr"><KatexInline math="\varphi" /></span> נבנה אוטומט Büchi מוכלל:
</div>

<div class="mt-4 text-center text-[32px]" dir="ltr">
<KatexInline display math="\mathcal{G}_{\varphi}=\langle Q,2^{AP},\delta,Q_0,\mathcal{F}\rangle" />
</div>

<div class="mt-5 text-right text-[21px] leading-relaxed">
נרצה לבנות את האוטומט כדי שיתקיים:
</div>

<div class="mt-5 bg-emerald-50 border border-emerald-200 rounded p-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="\mathcal{L}_{\omega}(\mathcal{G}_{\varphi})=Words(\varphi)" />
</div>

---

# תזכורת: GNBA

<div class="grid grid-cols-[0.82fr_1.18fr] gap-5 mt-2 items-start">
<div>
<div class="bg-white rounded border border-slate-200 shadow-sm ">
<div class="scale-90">
<AutomatonD3 variant="classic" :width="430" :height="235" :arrowSize="3.8" :stateLabelFontSize="14" :transitionLabelFontSize="12"
  :states="[
    { id: 'q0', x: 72, y: 122, label: '$q_0$', initial: true, initialDirection: 'bottom', r: 22, labelWidth: 66 },
    { id: 'qa', x: 215, y: 62, label: '$q_a$', accepting: true, stroke: '#2563eb', innerStroke: '#2563eb', r: 25, labelWidth: 66 },
    { id: 'qb', x: 358, y: 122, label: '$q_b$', accepting: true, stroke: '#059669', innerStroke: '#059669', r: 25, labelWidth: 66 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$\\neg a\\land\\neg b$', loopDirection: '180deg', labelY: -25, labelWidth: 120 },
    { source: 'q0', target: 'qa', label: '$a$', labelY: -12, labelWidth: 45, curve: -0.18 },
    { source: 'q0', target: 'qb', label: '$b$', labelY: 16, labelWidth: 45, curve: 0.18 },
    { source: 'qa', target: 'qa', label: '$a$', loopDirection: '-90deg', labelY: -10, labelWidth: 45 },
    { source: 'qb', target: 'qb', label: '$b$', loopDirection: '90deg', labelY: 10, labelWidth: 45 },
    { source: 'qa', target: 'qb', label: '$b$', labelY: 18, labelWidth: 45, curve: 0.28 },
    { source: 'qb', target: 'qa', label: '$a$', labelY: -18, labelWidth: 45, curve: 0.28 }
  ]"
/>
</div>
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[16px] leading-snug">
<div class="font-bold mb-1">הוכחה ששפת האוטומט היא <span dir="ltr"><KatexInline math="\Box\Diamond a\land\Box\Diamond b" /></span></div>
אם ריצה מתקבלת, היא מבקרת ב־<span dir="ltr"><KatexInline math="q_a" /></span> וב־<span dir="ltr"><KatexInline math="q_b" /></span> אינסוף פעמים; לכן נקראו אותיות עם <span dir="ltr"><KatexInline math="a" /></span> ועם <span dir="ltr"><KatexInline math="b" /></span> אינסוף פעמים.
להפך, אם במילה יש אינסוף מופעים של <span dir="ltr"><KatexInline math="a" /></span> ואינסוף מופעים של <span dir="ltr"><KatexInline math="b" /></span>, אפשר לבחור בכל מופע כזה מעבר אל <span dir="ltr"><KatexInline math="q_a" /></span> או <span dir="ltr"><KatexInline math="q_b" /></span>, ולכן הריצה מבקרת בשתי קבוצות הקבלה אינסוף פעמים.
</div>
</div>

<div class="text-right text-[19px] leading-relaxed -mt-4">
<div class="bg-slate-50 border border-slate-200 rounded p-3 mb-3 w-full">
ב־<span dir="ltr">GNBA</span> ריצה מתקבלת אם ורק אם היא מבקרת בכל אחת מקבוצות הקבלה אינסוף פעמים.
</div>

<div class="grid grid-cols-1 gap-3">
<div class="bg-blue-50 border border-blue-200 rounded p-3 w-full">
<span dir="ltr"><KatexInline math="F_a=\{q_a\}" /></span>: צריך לראות <span dir="ltr"><KatexInline math="a" /></span> אינסוף פעמים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3 w-full">
<span dir="ltr"><KatexInline math="F_b=\{q_b\}" /></span>: צריך לראות <span dir="ltr"><KatexInline math="b" /></span> אינסוף פעמים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3 text-center w-full">
<div class="text-right mb-1">לכן הדוגמה מקבלת את השפה:</div>
<div class="text-[24px]" dir="ltr">
<KatexInline display math="\Box\Diamond a\;\land\;\Box\Diamond b" />
</div>
</div>
</div>
</div>
</div>

---

# האינטואיציה של הבנייה

<div class="mt-7 grid grid-cols-3 gap-4 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מצב</div>
השמה עקבית לתת־נוסחאות של <span dir="ltr"><KatexInline math="\varphi" /></span>: מה נכון עכשיו לגבי הסיפה הנוכחית של המילה.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">מעבר</div>
בדיקה שהניחוש במצב הבא מתאים ל־<span dir="ltr"><KatexInline math="\bigcirc" /></span> ולכללי הפריסה של <span dir="ltr"><KatexInline math="\mathrm{U}" /></span>.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">קבלה</div>
אכיפה של הבטחות חיות: אם ניחשנו <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span>, אז <span dir="ltr"><KatexInline math="\psi_2" /></span> חייבת להגיע.
</div>
</div>

<div class="mt-8 text-center text-[24px]">
המצב <span dir="ltr"><KatexInline math="B_i" /></span> מתאר את אמת תת־הנוסחאות על הסיפה <span dir="ltr"><KatexInline math="\sigma[i..]" /></span>.
</div>

---

# שלב 1: סגור תת־נוסחאות

<div class="mt-7 text-right text-[21px] leading-relaxed">
מתחילים מקבוצת הסגור של הנוסחה: כל תת־נוסחה, וגם שלילתה. נסמן אותה <span dir="ltr"><KatexInline math="cl(\varphi)" /></span>.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">דוגמה</div>
<div class="text-center text-[28px]" dir="ltr">
<KatexInline display math="\varphi=a\mathbin{\mathrm{U}}b" />
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">הסגור</div>
<div class="text-center text-[24px]" dir="ltr">
<KatexInline display math="cl(\varphi)=\{a,\neg a,b,\neg b,a\mathbin{\mathrm{U}}b,\neg(a\mathbin{\mathrm{U}}b)\}" />
</div>
</div>
</div>

---

# שלב 2: קבוצות עקביות

<div class="mt-6 text-right text-[21px] leading-relaxed">
מצב באוטומט הוא קבוצה <span dir="ltr"><KatexInline math="B\subseteq cl(\varphi)" /></span> שמייצגת ניחוש מלא ועקבי.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">עקביות בוליאנית</div>
<div dir="ltr"><KatexInline math="\psi_1\land\psi_2\in B\iff \psi_1\in B\land \psi_2\in B" /></div>
<div dir="ltr" class="mt-2"><KatexInline math="\psi\in B\iff \neg\psi\notin B" /></div>
<div dir="ltr" class="mt-2"><KatexInline math="true\in B" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">עקביות מקומית של Until</div>
<div dir="ltr"><KatexInline math="\psi_2\in B\Rightarrow \psi_1\mathbin{\mathrm{U}}\psi_2\in B" /></div>
<div dir="ltr" class="mt-2"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in B\Rightarrow \psi_1\in B\lor\psi_2\in B" /></div>
</div>
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[20px] leading-relaxed">
המקסימליות אומרת שבכל מצב אנחנו בוחרים בדיוק אחד מכל זוג <span dir="ltr"><KatexInline math="\psi,\neg\psi" /></span>.
</div>

---

# המצבים עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<div class="mt-7 grid grid-cols-4 gap-3 text-center text-[18px]" dir="ltr">
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<KatexInline display math="\{a,b,a\mathbin{\mathrm{U}}b\}" />
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<KatexInline display math="\{a,\neg b,a\mathbin{\mathrm{U}}b\}" />
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<KatexInline display math="\{\neg a,b,a\mathbin{\mathrm{U}}b\}" />
</div>
<div class="bg-slate-50 border border-slate-200 rounded p-3">
<KatexInline display math="\{a,\neg b,\neg(a\mathbin{\mathrm{U}}b)\}" />
</div>
</div>

<div class="mt-4 grid grid-cols-2 gap-4 text-center text-[18px]" dir="ltr">
<div class="bg-slate-50 border border-slate-200 rounded p-3">
<KatexInline display math="\{\neg a,\neg b,\neg(a\mathbin{\mathrm{U}}b)\}" />
</div>
<div class="bg-red-50 border border-red-200 rounded p-3">
<KatexInline display math="\{\neg a,\neg b,a\mathbin{\mathrm{U}}b\}" />
<div dir="rtl" class="text-[17px] text-red-700 mt-2">לא עקבי: <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span> מחייב <span dir="ltr"><KatexInline math="a\lor b" /></span>.</div>
</div>
</div>

---

# שלב 3: מצבים התחלתיים

<div class="mt-7 text-right text-[22px] leading-relaxed">
מצב התחלתי הוא ניחוש שבו הנוסחה הראשית נכונה בתחילת המילה.
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="Q_0=\{B\in Q:\varphi\in B\}" />
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-right text-[21px] leading-relaxed">
עבור <span dir="ltr"><KatexInline math="\varphi=a\mathbin{\mathrm{U}}b" /></span>, המצבים ההתחלתיים הם בדיוק המצבים שמכילים את <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.
</div>

---

# שלב 4: יחס המעברים

<div class="mt-6 text-right text-[21px] leading-relaxed">
מעבר <span dir="ltr"><KatexInline math="B'\in\delta(B,A)" /></span> מותר רק אם האות הנקראת והמצב הבא תואמים לניחוש הנוכחי.
</div>

<div class="mt-5 grid grid-cols-3 gap-4 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3">
<div class="font-bold text-blue-700 mb-2">אטומים</div>
<div dir="ltr"><KatexInline math="a\in B\iff a\in A" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<div class="font-bold text-emerald-700 mb-2">Next</div>
<div dir="ltr"><KatexInline math="\bigcirc\psi\in B\iff \psi\in B'" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3">
<div class="font-bold text-amber-700 mb-2">Until</div>
<div dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in B\land\psi_2\notin B\Rightarrow \psi_1\mathbin{\mathrm{U}}\psi_2\in B'" /></div>
<div dir="ltr" class="mt-2"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\notin B\land\psi_1\in B\Rightarrow \psi_1\mathbin{\mathrm{U}}\psi_2\notin B'" /></div>
</div>
</div>

---

# איך לקרוא את כללי המעבר?

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">הבטחה פתוחה</div>
אם <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span> נכון עכשיו, אבל <span dir="ltr"><KatexInline math="\psi_2" /></span> עדיין לא נכון, אז ההבטחה חייבת להמשיך למצב הבא.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">ניחוש שלילי</div>
אם <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span> שקרי עכשיו ו־<span dir="ltr"><KatexInline math="\psi_1" /></span> נכון, אז גם במצב הבא הוא צריך להישאר שקרי.
</div>
</div>

<div class="mt-7 text-center text-[27px]" dir="ltr">
<KatexInline display math="\psi_1\mathbin{\mathrm{U}}\psi_2 \equiv \psi_2\lor(\psi_1\land\bigcirc(\psi_1\mathbin{\mathrm{U}}\psi_2))" />
</div>

---

# שלב 5: תנאי הקבלה

<div class="mt-7 text-right text-[22px] leading-relaxed">
לכל תת־נוסחת <span dir="ltr">Until</span> יוצרים קבוצת קבלה אחת:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="F_{\psi_1\mathrm{U}\psi_2}=\{B\in Q:\psi_1\mathbin{\mathrm{U}}\psi_2\notin B\;\lor\;\psi_2\in B\}" />
</div>

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
אם ההבטחה אינה פתוחה, אין בעיה: המצב נמצא בקבוצת הקבלה.
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
אם ההבטחה פתוחה, חייבים לבקר בעתיד במצב שבו <span dir="ltr"><KatexInline math="\psi_2" /></span> מתקיימת.
</div>
</div>

---

# דוגמה: <span dir="ltr"><KatexInline math="\mathcal{G}_{a\mathrm{U}b}" /></span>

<div class="grid grid-cols-[1.05fr_0.95fr] gap-4 mt-4 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="520" :height="350" :arrowSize="4" :stateLabelFontSize="13" :transitionLabelFontSize="13"
  :states="[
    { id: 'q_both', x: 260, y: 55, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', initial: true, initialDirection: 'top', accepting: true, r: 30, labelWidth: 135, labelHeight: 34 },
    { id: 'q_wait', x: 95, y: 155, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', initial: true, initialDirection: 'left', accepting: false, stroke: '#dc2626', r: 31, labelWidth: 150, labelHeight: 34 },
    { id: 'q_b', x: 425, y: 155, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', initial: true, initialDirection: 'right', accepting: true, r: 31, labelWidth: 150, labelHeight: 34 },
    { id: 'q_no', x: 175, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', accepting: true, r: 32, labelWidth: 170, labelHeight: 34 },
    { id: 'q_dead', x: 355, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', accepting: true, r: 32, labelWidth: 180, labelHeight: 34 }
  ]"
  :transitions="[
    { source: 'q_wait', target: 'q_wait', label: '$\\{a\\}$', loopDirection: '-170deg', labelY: -8, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\{a,b\\}$', labelY: -12, labelWidth: 75, curve: 0.18 },
    { source: 'q_wait', target: 'q_b', label: '$\\{b\\}$', labelY: -8, labelWidth: 60, curve: 0.18 },
    { source: 'q_both', target: 'q_wait', label: '$\\{a\\}$', labelY: 15, labelWidth: 65, curve: 0.18 },
    { source: 'q_both', target: 'q_b', label: '$\\{b\\}$', labelY: 15, labelWidth: 60, curve: -0.18 },
    { source: 'q_no', target: 'q_no', label: '$\\{a\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_dead', target: 'q_dead', label: '$\\emptyset$', loopDirection: '90deg', labelY: 10, labelWidth: 80 },
    { source: 'q_b', target: 'q_dead', label: '$\\emptyset$', labelY: 18, labelWidth: 80, curve: 0.18 },
    { source: 'q_b', target: 'q_both', label: '$\\{a,b\\}$', labelY: -14, labelWidth: 80, curve: 0.18 }
  ]"
/>
</div>

<div class="text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 mb-3">
מצבים התחלתיים: אלה שמכילים <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.
</div>
<div class="bg-red-50 border border-red-200 rounded p-3 mb-3">
המצב האדום אינו מקבל: ההבטחה <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span> פתוחה ו־<span dir="ltr"><KatexInline math="b" /></span> עדיין לא התקיים.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
כל מצב שבו <span dir="ltr"><KatexInline math="b" /></span> מתקיים, או שבו ההבטחה אינה נטענת, שייך לקבוצת הקבלה.
</div>
</div>
</div>

---

# למה צריך תנאי קבלה?

<div class="mt-7 text-right text-[22px] leading-relaxed">
כללי המעבר לבדם אינם מספיקים: הם יכולים להחזיק הבטחת <span dir="ltr">Until</span> פתוחה לנצח.
</div>

<div class="mt-6 grid grid-cols-2 gap-5 text-right text-[21px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">ריצה לא טובה</div>
כל הזמן <span dir="ltr"><KatexInline math="a" /></span> מתקיים ו־<span dir="ltr"><KatexInline math="b" /></span> לא מתקיים, אבל ממשיכים לנחש <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">תיקון Büchi</div>
הריצה חייבת לבקר אינסוף פעמים במצב שבו ההבטחה אינה פתוחה או שכבר מומשה.
</div>
</div>

<div class="mt-7 text-center text-[27px]" dir="ltr">
<KatexInline display math="F_{a\mathrm{U}b}=\{B:a\mathbin{\mathrm{U}}b\notin B\lor b\in B\}" />
</div>

---

# נכונות הבנייה: הכיוון האינטואיטיבי

<div class="mt-7 text-right text-[21px] leading-relaxed">
נניח שיש ריצה מקבלת של <span dir="ltr"><KatexInline math="\mathcal{G}_{\varphi}" /></span> על מילה <span dir="ltr"><KatexInline math="\sigma=A_0A_1A_2\ldots" /></span>:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="B_0 \xrightarrow{A_0} B_1 \xrightarrow{A_1} B_2 \xrightarrow{A_2}\cdots" />
</div>

<div class="mt-6 bg-blue-50 border border-blue-200 rounded p-4 text-right text-[21px] leading-relaxed">
מוכיחים באינדוקציה מבנית על תת־נוסחאות:
<div class="mt-3 text-center text-[27px]" dir="ltr">
<KatexInline display math="\sigma[i..]\models\psi \iff \psi\in B_i" />
</div>
</div>

---

# מקרה Until בהוכחת הנכונות

<div class="mt-6 text-right text-[21px] leading-relaxed">
החלק העדין הוא <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span>.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
אם <span dir="ltr"><KatexInline math="\psi_2\in B_i" /></span>, ה־<span dir="ltr">Until</span> נכון מייד.
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
אם <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in B_i" /></span> ו־<span dir="ltr"><KatexInline math="\psi_2\notin B_i" /></span>, כללי המעבר מעבירים את ההבטחה ל־<span dir="ltr"><KatexInline math="B_{i+1}" /></span>.
</div>
</div>

<div class="mt-6 bg-red-50 border border-red-200 rounded p-4 text-right text-[20px] leading-relaxed">
תנאי הקבלה מונע מצב שבו ההבטחה מועברת לנצח בלי ש־<span dir="ltr"><KatexInline math="\psi_2" /></span> תופיע.
</div>

---

# התוצאה המרכזית

<div class="mt-7 bg-emerald-50 border border-emerald-200 rounded p-5 text-right text-[22px] leading-relaxed">
לכל נוסחת <span dir="ltr">LTL</span> <span dir="ltr"><KatexInline math="\varphi" /></span> מעל <span dir="ltr"><KatexInline math="AP" /></span> אפשר לבנות <span dir="ltr">GNBA</span> <span dir="ltr"><KatexInline math="\mathcal{G}_{\varphi}" /></span> כך ש:
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="\mathcal{L}_{\omega}(\mathcal{G}_{\varphi})=Words(\varphi)" />
</div>

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
גודל האוטומט חסום אקספוננציאלית בגודל הנוסחה.
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4">
מספר קבוצות הקבלה חסום על ידי מספר תת־נוסחאות ה־<span dir="ltr">Until</span>.
</div>
</div>

---

# מה זה נותן לאימות?

<div class="mt-7 grid grid-cols-3 gap-4 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מתרגמים</div>
בונים אוטומט עבור <span dir="ltr"><KatexInline math="\neg\varphi" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">מרכיבים</div>
יוצרים מכפלה עם מערכת המעברים <span dir="ltr"><KatexInline math="TS" /></span>.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">מחפשים</div>
בודקים אם קיימת ריצה מקבלת, כלומר דוגמה נגדית.
</div>
</div>

<div class="mt-8 text-center text-[29px]" dir="ltr">
<KatexInline display math="TS\models\varphi \iff \mathcal{L}_{\omega}(TS\times\mathcal{A}_{\neg\varphi})=\emptyset" />
</div>

---

# סיכום

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מצבים הם ניחושים</div>
כל מצב מתאר אילו תת־נוסחאות נכונות בסיפה הנוכחית.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">מעברים הם בדיקות עקביות</div>
האות הנקראת, <span dir="ltr">Next</span>, וכללי הפריסה של <span dir="ltr">Until</span> קובעים אילו מעברים מותרים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">קבלה סוגרת הבטחות</div>
קבוצות הקבלה מבטיחות שכל <span dir="ltr">Until</span> שנפתח גם יגיע בסוף לצד הימני.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">LTL היא ω-רגולרית</div>
כל נוסחת <span dir="ltr">LTL</span> מגדירה שפה שמתקבלת על ידי אוטומט Büchi.
</div>
</div>
