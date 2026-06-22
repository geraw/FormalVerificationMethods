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
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">רדוקציה</div>
נראה איך בדיקת <span dir="ltr">LTL</span> הופכת לחיפוש ריצה מקבלת במכפלה עם אוטומט.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">בניית האוטומט</div>
נבנה <span dir="ltr">GNBA</span> שמקבל בדיוק את המילים שמקיימות נוסחת <span dir="ltr">LTL</span>.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2">הבטחות Until</div>
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
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">כן</div>
כל עקבה של המערכת מקיימת את הנוסחה.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
<div class="font-bold text-red-800 mb-2">לא</div>
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
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
מערכת המעברים<br />
<span dir="ltr"><KatexInline math="TS" /></span>
</div>
<div class="text-[34px]">×</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
אוטומט עבור ההפרה<br />
<span dir="ltr"><KatexInline math="\mathcal{A}_{\neg\varphi}" /></span>
</div>
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-4 text-slate-800 text-right text-[20px] leading-relaxed">
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

<div class="mt-5 bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900 text-center text-[28px]" dir="ltr">
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
    { source: 'q0', target: 'qb', label: '$b$', labelY: 16, labelWidth: 45, curve: 0.15 },
    { source: 'qa', target: 'qa', label: '$a$', loopDirection: '-90deg', labelY: -10, labelWidth: 45 },
    { source: 'qb', target: 'qb', label: '$b$', loopDirection: '90deg', labelY: 10, labelWidth: 45 },
    { source: 'qa', target: 'qb', label: '$b$', labelY: 18, labelWidth: 45, curve: 0.28 },
    { source: 'qb', target: 'qa', label: '$a$', labelY: -18, labelWidth: 45, curve: 0.28 }
  ]"
/>
</div>
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-slate-800 text-right text-[16px] leading-snug">
<div class="font-bold mb-1">הוכחה ששפת האוטומט היא <span dir="ltr"><KatexInline math="\Box\Diamond a\land\Box\Diamond b" /></span></div>
אם ריצה מתקבלת, היא מבקרת ב־<span dir="ltr"><KatexInline math="q_a" /></span> וב־<span dir="ltr"><KatexInline math="q_b" /></span> אינסוף פעמים; לכן נקראו אותיות עם <span dir="ltr"><KatexInline math="a" /></span> ועם <span dir="ltr"><KatexInline math="b" /></span> אינסוף פעמים.
להפך, אם במילה יש אינסוף מופעים של <span dir="ltr"><KatexInline math="a" /></span> ואינסוף מופעים של <span dir="ltr"><KatexInline math="b" /></span>, אפשר לבחור בכל מופע כזה מעבר אל <span dir="ltr"><KatexInline math="q_a" /></span> או <span dir="ltr"><KatexInline math="q_b" /></span>, ולכן הריצה מבקרת בשתי קבוצות הקבלה אינסוף פעמים.
</div>
</div>

<div class="text-right text-[19px] leading-relaxed -mt-4">
<div class="bg-slate-50 border border-slate-200 rounded p-3 mb-3 w-full text-slate-800">
ב־<span dir="ltr">GNBA</span> ריצה מתקבלת אם ורק אם היא מבקרת בכל אחת מקבוצות הקבלה אינסוף פעמים.
</div>

<div class="grid grid-cols-1 gap-3">
<div class="bg-blue-50 border border-blue-200 rounded p-3 w-full text-blue-900">
<span dir="ltr"><KatexInline math="F_a=\{q_a\}" /></span>: צריך לראות <span dir="ltr"><KatexInline math="a" /></span> אינסוף פעמים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3 w-full text-emerald-900">
<span dir="ltr"><KatexInline math="F_b=\{q_b\}" /></span>: צריך לראות <span dir="ltr"><KatexInline math="b" /></span> אינסוף פעמים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3 text-center w-full text-amber-900">
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

<div class="mt-4 text-center text-[21px]">
נבנה אוטומט Büchi מוכלל "שינחש" באופן אי-דטרמיניסטי אילו נוסחאות עומדות להתקיים בהמשך המילה בכל רגע, ויצליח ליצור ריצה אינסופית מקבלת רק אם הניחושים שלו היו נכונים.
</div>

<div class="mt-4 grid grid-cols-3 gap-4 text-right text-[16px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">מצב</div>
השמה עקבית לתת־נוסחאות של <span dir="ltr"><KatexInline math="\varphi" /></span>: מה נכון עכשיו לגבי הַסֵּיפָא הנוכחית של המילה.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">יחס המעברים</div>
בדיקה שהניחוש במצב הבא מתאים לכללי הפריסה של <span dir="ltr"><KatexInline math="\bigcirc" /></span> ושל <span dir="ltr"><KatexInline math="\mathrm{U}" /></span>.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2">תנאי הקבלה</div>
אכיפה של הבטחות חַיּוּת: אם ניחשנו <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span>, אז <span dir="ltr"><KatexInline math="\psi_2" /></span> חייבת להגיע.
</div>
</div>

<div class="mt-5 text-center text-[15px] text-slate-600">
נמחיש על <span dir="ltr"><KatexInline math="\varphi=a\mathbin{\mathrm{U}}b" /></span> לאורך המילה <span dir="ltr"><KatexInline math="\{a\},\{a\},\{b\},\ldots" /></span>
</div>

<div class="mt-3 flex items-center justify-center gap-2" dir="ltr">

<div class="bg-blue-50 border-2 border-blue-300 rounded-lg p-2 text-center text-[13px] w-[155px]">
<div class="font-bold text-blue-700" dir="ltr">מצב 0</div>
<div class="text-[11px] text-slate-500">
<KatexInline math="\{a\}" /></div>
<div class="mt-1"><KatexInline math="a\mathbin{\mathrm{U}}b,\;a,\;\neg b" /></div>
</div>

<div v-click class="text-blue-400 text-[24px]">→</div>

<div v-click class="bg-blue-50 border-2 border-blue-300 rounded-lg p-2 text-center text-[13px] w-[155px]">
<div class="font-bold text-blue-700" dir="ltr">מצב 1</div>
<div class="text-[11px] text-slate-500"><KatexInline math="\{a\}" /></div>
<div class="mt-1"><KatexInline math="a\mathbin{\mathrm{U}}b,\;a,\;\neg b" /></div>
</div>

<div v-click class="text-emerald-500 text-[24px]">→</div>

<div v-click class="relative bg-emerald-50 border-2 border-emerald-400 rounded-lg p-2 text-center text-[13px] w-[155px]">
<div class="absolute -top-2 -right-2 bg-emerald-500 text-white text-[9px] rounded-full px-1.5 py-0.5">מקבל</div>
<div class="font-bold text-emerald-700" dir="ltr">מצב 2</div>
<div class="text-[11px] text-slate-500"><KatexInline math="\{b\}" /></div>
<div class="mt-1"><KatexInline math="a\mathbin{\mathrm{U}}b,\;\neg a,\;b" /></div>
</div>

</div>

<div class="mt-3 min-h-[55px] text-center text-[14px] text-slate-700 leading-snug">
<div v-show="!$slidev.nav.clicks">מצב 0 הוא הניחוש: <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span> תתקיים, אבל לא עכשיו — כלומר חייבת להחזיק <span dir="ltr"><KatexInline math="a" /></span> ולהמשיך להבטיח את הניחוש.</div>
<div v-show="$slidev.nav.clicks === 1">יחס המעברים בדק שהניחוש במצב 1 תואם את כלל הפריסה: כיוון ש־<span dir="ltr"><KatexInline math="b" /></span> עדיין לא הגיעה, צריך גם <span dir="ltr"><KatexInline math="a" /></span> עכשיו וגם להמשיך להבטיח <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.</div>
<div v-show="$slidev.nav.clicks === 2">במצב 2 הגיעה <span dir="ltr"><KatexInline math="b" /></span>, ההבטחה התממשה, והמצב נכנס לקבוצת הקבלה — כך תנאי הקבלה מבטיח שההבטחה לא תידחה לנצח.</div>
</div>

---

# אנימציה: שלושה מהמרים

<div class="absolute inset-x-0 bottom-0 h-[310px] overflow-hidden opacity-75">
<img src="./public/gambler-guesses.png" class="w-full h-full object-cover object-bottom" />
</div>
<div class="absolute inset-0 bg-white/45 pointer-events-none"></div>

<div class="relative z-10">
<div class="-mt-1 text-right text-[17px] leading-snug">
<div>ננתח את הנוסחה</div>
<div class="mt-0 text-center text-[21px]" dir="ltr">
<KatexInline display math="\varphi=(a\mathbin{\mathrm{U}}b)\mathbin{\mathrm{U}}(c\mathbin{\mathrm{U}}d)" />
</div>
<div class="mt-0 flex justify-center gap-8 text-[17px]" dir="ltr">
<span><KatexInline math="\alpha=a\mathbin{\mathrm{U}}b" /></span>
<span><KatexInline math="\beta=c\mathbin{\mathrm{U}}d" /></span>
</div>
</div>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="mt-2 min-h-[330px]">
<div v-show="$slidev.nav.clicks === 0">
<div class="text-center text-[18px] mb-2">לפני קריאת המילה: שלושת המהמרים בוחרים ניחוש התחלתי לגבי שני תת־הביטויים.</div>
<div class="grid grid-cols-3 gap-3 text-right text-[17px] leading-snug">
<div class="bg-blue-50/95 border border-blue-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-blue-700 mb-2">מהמר 1</div>
<div class="text-center text-[22px]" dir="ltr"><KatexInline display math="\neg\alpha,\;\beta" /></div>
<div>מהמר שהחלק השמאלי לא מתקיים עכשיו, אבל החלק הימני כן.</div>
</div>
<div class="bg-amber-50/95 border border-amber-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-amber-700 mb-2">מהמר 2</div>
<div class="text-center text-[22px]" dir="ltr"><KatexInline display math="\alpha,\;\neg\beta" /></div>
<div>מהמר שהחלק השמאלי מתקיים עכשיו, והחלק הימני לא.</div>
</div>
<div class="bg-emerald-50/95 border border-emerald-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-emerald-700 mb-2">מהמר 3</div>
<div class="text-center text-[22px]" dir="ltr"><KatexInline display math="\alpha,\;\beta" /></div>
<div>מהמר ששני תת־הביטויים מתקיימים עכשיו.</div>
</div>
</div>
<div class="mt-3 bg-slate-50/95 border border-slate-200 rounded px-4 py-2 text-center text-[16px] leading-snug">
יש לנו רק שלושה מהמרים, כי אנחנו רוצים לבדוק את התכונה למעלה:
אם גם <span dir="ltr"><KatexInline math="\alpha" /></span> וגם <span dir="ltr"><KatexInline math="\beta" /></span> לא יתקיימו,
אז <span dir="ltr"><KatexInline math="\alpha\mathbin{\mathrm{U}}\beta" /></span> לא תתקיים.
</div>
</div>

<div v-show="$slidev.nav.clicks === 1">
<div class="mx-auto mb-2 w-fit bg-yellow-100/95 border-2 border-yellow-400 rounded px-5 py-1.5 text-center shadow-md">
<div class="text-[13px] font-bold text-yellow-800 mb-0.5">האות הנקראת עכשיו</div>
<div class="text-[20px]" dir="ltr"><KatexInline math="A_0=\{a,c\}" /></div>
</div>
<div class="text-center text-[18px] mb-2">מתחילים לעדכן את הניחושים: אף אחד עדיין לא יוצא.</div>
<div class="grid grid-cols-3 gap-3 text-right text-[17px] leading-snug">
<div class="bg-blue-50/95 border border-blue-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-blue-700 mb-2">מהמר 1 נשאר</div>
<div dir="ltr" class="text-center text-[21px]"><KatexInline display math="\neg\alpha,\beta" /></div>
<div><span dir="ltr"><KatexInline math="b" /></span> עוד לא הופיע, ולכן אפשר עדיין לעקוב אחרי ניחוש שבו <span dir="ltr"><KatexInline math="\alpha" /></span> לא נסגר.</div>
</div>
<div class="bg-amber-50/95 border border-amber-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-amber-700 mb-2">מהמר 2 נשאר</div>
<div dir="ltr" class="text-center text-[21px]"><KatexInline display math="\alpha,\neg\beta" /></div>
<div><span dir="ltr"><KatexInline math="d" /></span> עוד לא הופיע, ולכן אי אפשר להכריע עכשיו נגד הניחוש השלילי לגבי <span dir="ltr"><KatexInline math="\beta" /></span>.</div>
</div>
<div class="bg-emerald-50/95 border border-emerald-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-emerald-700 mb-2">מהמר 3 נשאר</div>
<div dir="ltr" class="text-center text-[21px]"><KatexInline display math="\alpha,\beta" /></div>
<div>שני החלקים יכולים עדיין להתקיים בהמשך.</div>
</div>
</div>
</div>

<div v-show="$slidev.nav.clicks === 2">
<div class="mx-auto mb-2 w-fit bg-yellow-100/95 border-2 border-yellow-400 rounded px-5 py-1.5 text-center shadow-md">
<div class="text-[13px] font-bold text-yellow-800 mb-0.5">האות הנקראת עכשיו</div>
<div class="text-[20px]" dir="ltr"><KatexInline math="A_1=\{b,c\}" /></div>
</div>
<div class="text-center text-[18px] mb-2">החלק השמאלי נסגר: עכשיו יודעים ש־<span dir="ltr"><KatexInline math="\alpha" /></span> מתקיים, ולכן ממשיכים רק עם השאלה מה יקרה ל־<span dir="ltr"><KatexInline math="\beta" /></span>.</div>
<div class="grid grid-cols-3 gap-3 text-right text-[17px] leading-snug">
<div class="bg-red-50/95 border border-red-200 rounded p-2.5 shadow-sm opacity-90">
<div class="font-bold text-red-700 mb-2">מהמר 1 יוצא</div>
<div class="text-center text-[24px] leading-snug">
<span dir="ltr"><KatexInline math="\alpha" /></span> נסגר כי <span dir="ltr"><KatexInline math="b" /></span> הופיע; <span dir="ltr"><KatexInline math="\beta" /></span> עדיין פתוח
</div>
<div>ההימור ההתחלתי שלו היה <span dir="ltr"><KatexInline math="\neg\alpha" /></span>, ולכן הוא כבר לא מתאים להמשך.</div>
</div>
<div class="bg-amber-50/95 border border-amber-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-amber-700 mb-2">מהמר 2 מעדכן</div>
<div dir="ltr" class="text-center text-[21px]"><KatexInline display math="\alpha,\neg\beta\;\leadsto\;\neg\beta" /></div>
<div>החלק השמאלי מתאים לניחוש שלו וכבר הוכרע, ולכן ההימור הפעיל שנשאר הוא ש־<span dir="ltr"><KatexInline math="\beta" /></span> לא יתקיים.</div>
</div>
<div class="bg-emerald-50/95 border border-emerald-200 rounded p-2.5 shadow-sm">
<div class="font-bold text-emerald-700 mb-2">מהמר 3 מעדכן</div>
<div class="text-center text-[24px] leading-snug">
<span dir="ltr"><KatexInline math="\alpha,\beta\;\leadsto\;\beta" /></span>
</div>
<div>גם אצלו <span dir="ltr"><KatexInline math="\alpha" /></span> כבר נסגר, ולכן נשאר לעקוב רק אחרי ההבטחה <span dir="ltr"><KatexInline math="\beta=c\mathbin{\mathrm{U}}d" /></span>.</div>
</div>
</div>
</div>

<div v-show="$slidev.nav.clicks === 3">
<div class="mx-auto mb-2 w-fit bg-yellow-100/95 border-2 border-yellow-400 rounded px-5 py-1.5 text-center shadow-md">
<div class="text-[13px] font-bold text-yellow-800 mb-0.5">האות הנקראת עכשיו</div>
<div class="text-[20px]" dir="ltr"><KatexInline math="A_2=\{c\}" /></div>
</div>
<div class="text-center text-[18px] mb-2">שני ההימורים שנותרו עדיין אפשריים.</div>
<div class="grid grid-cols-2 gap-4 text-right text-[18px] leading-snug">
<div class="bg-amber-50/95 border border-amber-200 rounded p-3 shadow-sm">
<div class="font-bold text-amber-700 mb-2">מהמר 2 עדיין במשחק</div>
<div>עדיין לא הופיע <span dir="ltr"><KatexInline math="d" /></span>, ולכן הניחוש <span dir="ltr"><KatexInline math="\neg\beta" /></span> עוד לא הופרך בזמן הקריאה.</div>
</div>
<div class="bg-emerald-50/95 border border-emerald-200 rounded p-3 shadow-sm">
<div class="font-bold text-emerald-700 mb-2">מהמר 3 עדיין במשחק</div>
<div>גם ההימור ששני החלקים נכונים לא הופרך: החלק הימני עדיין מחכה ל־<span dir="ltr"><KatexInline math="d" /></span>.</div>
</div>
</div>
</div>

<div v-show="$slidev.nav.clicks === 4">
<div class="mx-auto mb-2 w-fit bg-yellow-100/95 border-2 border-yellow-400 rounded px-5 py-1.5 text-center shadow-md">
<div class="text-[13px] font-bold text-yellow-800 mb-0.5">האות הנקראת עכשיו</div>
<div class="text-[20px]" dir="ltr"><KatexInline math="A_3=\{d\}" /></div>
</div>
<div class="text-center text-[18px] mb-2">החלק הימני נסגר: עכשיו יודעים ש־<span dir="ltr"><KatexInline math="\beta" /></span> מתקיים.</div>
<div class="grid grid-cols-[0.9fr_1.1fr] gap-4 text-right text-[18px] leading-snug">
<div class="bg-red-50/95 border border-red-200 rounded p-3 shadow-sm opacity-90">
<div class="font-bold text-red-700 mb-2">מהמר 2 יוצא</div>
<div>ההימור שלו היה <span dir="ltr"><KatexInline math="\neg\beta" /></span>, אבל <span dir="ltr"><KatexInline math="d" /></span> הופיע וסגר את <span dir="ltr"><KatexInline math="c\mathbin{\mathrm{U}}d" /></span>.</div>
</div>
<div class="bg-emerald-50/95 border border-emerald-200 rounded p-3 shadow-sm">
<div class="font-bold text-emerald-700 mb-2">מהמר 3 צדק</div>
<div class="text-center text-[24px] leading-snug">
<span dir="ltr"><KatexInline math="\alpha" /></span> נסגר ב־<span dir="ltr"><KatexInline math="b" /></span>,
<br />
<span dir="ltr"><KatexInline math="\beta" /></span> נסגר ב־<span dir="ltr"><KatexInline math="d" /></span>
</div>
<div>בסוף מתקבל ניחוש עקבי שבו שני תת־הביטויים מתקיימים, ולכן גם <span dir="ltr"><KatexInline math="\varphi=\alpha\mathbin{\mathrm{U}}\beta" /></span> מתקיימת.</div>
</div>
</div>
</div>
</div>
</div>
---

# שלב 1: סגור תת־נוסחאות

<div class="mt-3 text-right text-[18px] leading-snug">
מתחילים מקבוצת הסגור של הנוסחה: כל תת־עץ בעץ הביטוי, וגם שלילתו. נסמן אותה <span dir="ltr"><KatexInline math="cl(\varphi)" /></span>.
</div>

<div class="mt-2 text-center text-[22px]" dir="ltr">
<KatexInline display math="\varphi=(a\mathbin{\mathrm{U}}b)\land\bigcirc(c\mathbin{\mathrm{U}}d)" />
</div>

<div class="mt-2 grid grid-cols-[0.95fr_1.05fr] gap-4 items-start">
<div class="bg-slate-50 border border-slate-200 rounded p-2 text-center text-slate-800">
<div class="font-bold mb-1 text-right text-[16px]">עץ הביטוי</div>
<div class="relative h-[205px] text-[17px]" dir="ltr">
<div class="absolute left-[50%] top-[6px] -translate-x-1/2 bg-white border border-slate-300 rounded px-4 py-1 z-10"><KatexInline math="\land" /></div>
<div class="absolute left-[31%] top-[64px] -translate-x-1/2 bg-blue-50 border border-blue-200 rounded px-3 py-1 z-10"><KatexInline math="\mathrm{U}" /></div>
<div class="absolute left-[69%] top-[64px] -translate-x-1/2 bg-amber-50 border border-amber-200 rounded px-3 py-1 z-10"><KatexInline math="\bigcirc" /></div>
<div class="absolute left-[69%] top-[118px] -translate-x-1/2 bg-blue-50 border border-blue-200 rounded px-3 py-1 z-10"><KatexInline math="\mathrm{U}" /></div>
<div class="absolute left-[21%] top-[143px] -translate-x-1/2 bg-white border border-slate-200 rounded px-3 py-1 z-10"><KatexInline math="a" /></div>
<div class="absolute left-[41%] top-[143px] -translate-x-1/2 bg-white border border-slate-200 rounded px-3 py-1 z-10"><KatexInline math="b" /></div>
<div class="absolute left-[59%] top-[171px] -translate-x-1/2 bg-white border border-slate-200 rounded px-3 py-1 z-10"><KatexInline math="c" /></div>
<div class="absolute left-[79%] top-[171px] -translate-x-1/2 bg-white border border-slate-200 rounded px-3 py-1 z-10"><KatexInline math="d" /></div>

<div class="absolute left-[40%] top-[47px] w-[2px] h-[28px] bg-slate-300 rotate-[54deg] origin-top"></div>
<div class="absolute left-[60%] top-[47px] w-[2px] h-[28px] bg-slate-300 rotate-[-54deg] origin-top"></div>
<div class="absolute left-[69%] top-[96px] w-[2px] h-[30px] bg-slate-300"></div>
<div class="absolute left-[27%] top-[103px] w-[2px] h-[43px] bg-slate-300 rotate-[35deg] origin-top"></div>
<div class="absolute left-[35%] top-[103px] w-[2px] h-[43px] bg-slate-300 rotate-[-35deg] origin-top"></div>
<div class="absolute left-[64%] top-[151px] w-[2px] h-[27px] bg-slate-300 rotate-[48deg] origin-top"></div>
<div class="absolute left-[74%] top-[151px] w-[2px] h-[27px] bg-slate-300 rotate-[-48deg] origin-top"></div>
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-2 text-right text-[15px] leading-snug text-blue-900">
<div class="font-bold text-blue-800 mb-1"><span dir="ltr"><KatexInline math="cl(\varphi)" /></span>: כל תת־העצים ושלילתם</div>
<div class="grid grid-cols-2 gap-x-3 gap-y-0.5 text-center justify-items-center" dir="ltr">
<div><KatexInline math="a" /></div><div><KatexInline math="\neg a" /></div>
<div><KatexInline math="b" /></div><div><KatexInline math="\neg b" /></div>
<div><KatexInline math="c" /></div><div><KatexInline math="\neg c" /></div>
<div><KatexInline math="d" /></div><div><KatexInline math="\neg d" /></div>
<div><KatexInline math="a\mathbin{\mathrm{U}}b" /></div><div><KatexInline math="\neg(a\mathbin{\mathrm{U}}b)" /></div>
<div><KatexInline math="c\mathbin{\mathrm{U}}d" /></div><div><KatexInline math="\neg(c\mathbin{\mathrm{U}}d)" /></div>
<div><KatexInline math="\bigcirc(c\mathbin{\mathrm{U}}d)" /></div><div><KatexInline math="\neg\bigcirc(c\mathbin{\mathrm{U}}d)" /></div>
<div><KatexInline math="\varphi" /></div><div><KatexInline math="\neg\varphi" /></div>
</div>
<div class="mt-1 text-[14px]" dir="rtl">
כל פריט ברשימה הוא תת־עץ של עץ הביטוי, ולידו מוסיפים גם את השלילה שלו.
</div>
</div>
</div>
---

# שלב 2: מצבי האוטומט הם הקבוצות העקביות

<div class="mt-6 text-right text-[21px] leading-relaxed">
מצב באוטומט הוא קבוצה <span dir="ltr"><KatexInline math="B\subseteq cl(\varphi)" /></span> שמייצגת ניחוש מלא ועקבי.
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">עקביות בוליאנית</div>
<div dir="ltr" class="grid grid-cols-[1fr_42px_1fr] gap-2 items-center text-[17px] leading-snug">
<div class="text-right"><KatexInline math="\psi_1\land\psi_2\in B" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left"><KatexInline math="\psi_1\in B\land\psi_2\in B" /></div>
<div class="text-right"><KatexInline math="\psi\in B" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left"><KatexInline math="\neg\psi\notin B" /></div>
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">עקביות של Until</div>
<div dir="ltr" class="grid grid-cols-[1fr_42px_1fr] gap-2 items-center text-[17px] leading-snug">
<div class="text-right"><KatexInline math="\psi_2\in B" /></div>
<div class="text-center"><KatexInline math="\Rightarrow" /></div>
<div class="text-left"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in B" /></div>
<div class="text-right"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in B" /></div>
<div class="text-center"><KatexInline math="\Rightarrow" /></div>
<div class="text-left"><KatexInline math="\psi_1\in B\lor\psi_2\in B" /></div>
</div>
</div>
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-4 text-amber-900 text-right text-[20px] leading-relaxed">
<div class="mb-2">המקסימליות אומרת שבכל מצב אנחנו בוחרים בדיוק אחד מכל זוג <span dir="ltr"><KatexInline math="\psi,\neg\psi" /></span>:</div>
<div dir="ltr" class="grid grid-cols-[1fr_42px_1fr] gap-2 items-center text-[19px] leading-snug">
<div class="text-right"><KatexInline math="\psi\in B" /></div>
<div class="text-center"><KatexInline math="\iff" /></div>
<div class="text-left"><KatexInline math="\neg\psi\notin B" /></div>
</div>
</div>

---

# שלב 3: מצבי ההתחלה הם אלה המכילים את <span dir="ltr"><KatexInline math="\varphi" /></span>

<div class="mt-7 text-right text-[22px] leading-relaxed">
מצב התחלה הוא ניחוש שבו הנוסחה הראשית נכונה בתחילת המילה.
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="Q_0=\{B\in Q\mid\varphi\in B\}" />
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-blue-900 text-right text-[21px] leading-relaxed">
עבור <span dir="ltr"><KatexInline math="\varphi=a\mathbin{\mathrm{U}}b" /></span>, מצבי ההתחלה הם בדיוק המצבים שמכילים את <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.
</div>

---

# שלב 4: יחס המעברים נקבע על פי כללי הפריסה

<div class="mt-6 text-right text-[21px] leading-relaxed">
מעבר <span dir="ltr"><KatexInline math="B'\in\delta(B,A)" /></span> מותר רק אם האות הנקראת והמצב הבא תואמים לניחוש הנוכחי:
</div>

<div class="mt-5 grid grid-cols-1 gap-3 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900">
<div class="font-bold text-blue-800 mb-2">לכל <span dir="ltr"><KatexInline math="a\in AP" /></span>:</div>
<div dir="ltr" class="text-center"><KatexInline math="a\in B\iff a\in A" /></div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">לכל <span dir="ltr"><KatexInline math="\bigcirc\psi\in cl(\varphi)" /></span>:</div>
<div dir="ltr" class="text-center"><KatexInline math="\bigcirc\psi\in B\iff \psi\in B'" /></div>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3 text-amber-900">
<div class="font-bold text-amber-800 mb-2">לכל <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in cl(\varphi)" /></span>:</div>
<div dir="ltr" class="text-center"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\in B\land\psi_2\notin B\Rightarrow \psi_1\mathbin{\mathrm{U}}\psi_2\in B'" /></div>
<div dir="ltr" class="mt-2 text-center"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\notin B\land\psi_1\in B\Rightarrow \psi_1\mathbin{\mathrm{U}}\psi_2\notin B'" /></div>
</div>
</div>

---
hide: true
---

# איך לקרוא את כללי המעבר?

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">הבטחה פתוחה</div>
אם <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span> נכון עכשיו, אבל <span dir="ltr"><KatexInline math="\psi_2" /></span> עדיין לא נכון, אז ההבטחה חייבת להמשיך למצב הבא.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
<div class="font-bold text-red-800 mb-2">ניחוש שלילי</div>
אם <span dir="ltr"><KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2" /></span> שקרי עכשיו ו־<span dir="ltr"><KatexInline math="\psi_1" /></span> נכון, אז גם במצב הבא הוא צריך להישאר שקרי.
</div>
</div>

<div class="mt-6 text-right text-[19px] leading-snug">
משתמשים בכלל הפריסה שהוכחנו במצגת הקודמת:
</div>

<div class="mt-7 text-center text-[27px]" dir="ltr">
<KatexInline display math="\psi_1\mathbin{\mathrm{U}}\psi_2 \equiv \psi_2\lor(\psi_1\land\bigcirc(\psi_1\mathbin{\mathrm{U}}\psi_2))" />
</div>

---

# שלב 5: תנאי הקבלה ע"פ העיקרון "הבטחות צריך לקיים"

<div class="mt-4 text-right text-[22px] leading-relaxed">
לכל תת־נוסחת <span dir="ltr">Until</span> יוצרים קבוצת קבלה אחת:
</div>

<div class="mt-2 text-center text-[28px]" dir="ltr">
<KatexInline display math="F_{\psi_1\mathrm{U}\psi_2}=\{B\in Q\mid\psi_1\mathbin{\mathrm{U}}\psi_2\notin B\;\lor\;\psi_2\in B\}" />
</div>

<div class="mt-2 text-right text-[20px] leading-relaxed">
משפחת קבוצות הקבלה היא:
</div>

<div class="mt-1 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathcal{F}=\{F_{\psi_1\mathrm{U}\psi_2}\mid \psi_1\mathbin{\mathrm{U}}\psi_2\in cl(\varphi)\}" />
</div>

<div class="mt-4 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
אם ההבטחה אינה פתוחה, אין בעיה: המצב נמצא בקבוצת הקבלה.
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
אם ההבטחה פתוחה, חייבים לבקר בעתיד במצב שבו <span dir="ltr"><KatexInline math="\psi_2" /></span> מתקיימת.
</div>
</div>

---

# למה צריך תנאי קבלה?

<div class="mt-5 text-right text-[21px] leading-relaxed">
תנאי הקבלה נועד לטפל, לדוגמה, בעובדה שהמילה <span dir="ltr"><KatexInline math="\{a\}^{\omega}" /></span> לא נופלת מהאוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.
</div>

<div class="mt-4 grid grid-cols-[0.95fr_1.05fr] gap-5 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="390" :height="235" :arrowSize="4" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { id: 'q_wait_only', x: 195, y: 125, label: '$a\\mathbin{\\mathrm{U}}b,a,\\neg b$', initial: true, initialDirection: 'left', accepting: false, stroke: '#dc2626', r: 42, labelWidth: 215, labelHeight: 42 }
  ]"
  :transitions="[
    { source: 'q_wait_only', target: 'q_wait_only', label: '$\\{a\\}$', loopDirection: '-90deg', labelY: -12, labelWidth: 90 }
  ]"
/>
</div>

<div class="text-right text-[15px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">ריצה לא טובה</div>
קוראים שוב ושוב את <span dir="ltr"><KatexInline math="\{a\}" /></span>: כל הזמן <span dir="ltr"><KatexInline math="a" /></span> מתקיים ו־<span dir="ltr"><KatexInline math="b" /></span> לא מתקיים, אבל המעבר העצמי ממשיך לנחש <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>.
</div>
<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">תיקון Büchi</div>
תנאי הקבלה פוסל ריצה שנשארת לנצח במצב שבו ההבטחה פתוחה ולא רואים את <span dir="ltr"><KatexInline math="b" /></span>.
</div>
</div>
</div>
<div class="mt-7 text-center text-[27px]" dir="ltr">
<KatexInline display math="F_{a\mathrm{U}b}=\{B\mid a\mathbin{\mathrm{U}}b\notin B\lor b\in B\}" />
</div>

---

# דוגמה: מצבי האוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="$slidev.nav.clicks === 0 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : $slidev.nav.clicks === 1 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : $slidev.nav.clicks === 2 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.3 },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.3 },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' }
  ]"
  :transitions="[]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
בודקים את 8 המצבים המועמדים מול כללי העקביות של Until.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-red-50 border border-red-200 rounded p-3 text-red-900" dir="rtl">
<b>כלל 1 נפרץ:</b> <span dir="ltr"><KatexInline math="b \in B \Rightarrow a\mathbin{\mathrm{U}}b \in B" /></span><br/>
המצבים <span dir="ltr"><KatexInline math="\{a,b,\neg(a\mathbin{\mathrm{U}}b)\}" /></span> ו-<span dir="ltr"><KatexInline math="\{\neg a,b,\neg(a\mathbin{\mathrm{U}}b)\}" /></span> מכילים את <span dir="ltr"><KatexInline math="b" /></span> אך לא את ההבטחה, ולכן נפסלים.
</div>
<div v-show="$slidev.nav.clicks === 2" class="bg-red-50 border border-red-200 rounded p-3 text-red-900" dir="rtl">
<b>כלל 2 נפרץ:</b> <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b \in B \Rightarrow a \in B \lor b \in B" /></span><br/>
המצב <span dir="ltr"><KatexInline math="\{\neg a,\neg b,a\mathbin{\mathrm{U}}b\}" /></span> מכיל את ההבטחה למרות שגם <span dir="ltr"><KatexInline math="a" /></span> וגם <span dir="ltr"><KatexInline math="b" /></span> שקריים, ולכן נפסל.
</div>
<div v-show="$slidev.nav.clicks === 3" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
נשארים עם 5 מצבים עקביים שיהוו את מצבי האוטומט.
</div>
</div>
</div>

---

# דוגמה: מעברים ממצב הבטחה פתוחה

<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, opacity: 0.8 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, opacity: 0.8 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.8 }
  ]"
  :transitions="$slidev.nav.clicks === 0 ? [
    { source: 'q_wait', target: 'q_wait', label: '$\\{a\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\{a\\}$', labelY: -12, labelWidth: 75, curve: 0 },
    { source: 'q_wait', target: 'q_b', label: '$\\{a\\}$', labelX: -14, labelWidth: 60, curve: 0 },
    { source: 'q_wait', target: 'q_no', label: '$\\{a\\}$', labelX: 14, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נשברת', curve: -0.4 },
    { source: 'q_wait', target: 'q_dead', label: '$\\{a\\}$', labelY: -14, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נשברת', curve: 0 }
  ] : [
    { source: 'q_wait', target: 'q_wait', label: '$\\{a\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\{a\\}$', labelY: -12, labelWidth: 75, curve: 0 },
    { source: 'q_wait', target: 'q_b', label: '$\\{a\\}$', labelX: -14, labelWidth: 60, curve: 0 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצב הבטחה פתוחה (שבו <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span> ו-<span dir="rtl"><KatexInline math="b \notin B" /></span>), מאחר שהבטחת ה-Until פתוחה (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span>) ואינה מתממשת כעת (<span dir="rtl"><KatexInline math="b \notin B" /></span>), <b>היא חייבת לעבור למצב הבא:</b> <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B'" /></span>.<br/>
לכן מעברים למצבים שאינם מכילים את ההבטחה (הקווים המקווקווים באדום) <b>נפסלים</b>.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
משאירים רק את המעברים התקינים למצבים שבהם ההבטחה מתקיימת (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B'" /></span>).
</div>
</div>
</div>

---

# דוגמה: מעברים ממצב ללא הבטחה

<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, opacity: 0.8 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.8 }
  ]"
  :transitions="$slidev.nav.clicks === 0 ? [
    { source: 'q_no', target: 'q_no', label: '$\\{a\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '$\\{a\\}$', labelY: 10, labelWidth: 60, curve: 0 },
    { source: 'q_no', target: 'q_both', label: '$\\{a\\}$', labelY: 16, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין', curve: 0 },
    { source: 'q_no', target: 'q_wait', label: '$\\{a\\}$', labelX: 16, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין', curve: 0.35 },
    { source: 'q_no', target: 'q_b', label: '$\\{a\\}$', labelX: -16, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין', curve: 0 }
  ] : [
    { source: 'q_no', target: 'q_no', label: '$\\{a\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '$\\{a\\}$', labelY: 10, labelWidth: 60, curve: 0 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצב ללא הבטחה (שבו <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span> אך <span dir="rtl"><KatexInline math="a \in B" /></span>), מאחר שההבטחה אינה מתקיימת (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span>) אך התנאי השמאלי מתקיים (<span dir="rtl"><KatexInline math="a \in B" /></span>), <b>ההבטחה לא יכולה להיווצר סתם כך במצב הבא:</b> <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B'" /></span>.<br/>
לכן מעברים למצבים שמכילים את ההבטחה (באדום מקווקו) <b>נפסלים</b>.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
נשארים רק המעברים התקינים למצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B'" /></span>).
</div>
</div>
</div>

---

# דוגמה: מעברים ממצבים ללא הגבלה

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 'q_both', target: 'q_both', label: '', loopDirection: '180deg', labelX: -22, labelWidth: 70 },
    { source: 'q_both', target: 'q_wait', label: '', labelY: -10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_b',    label: '', labelY: 12, labelWidth: 70, curve: 0.18 },
    { source: 'q_both', target: 'q_no',   label: '', labelY: 10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_dead', label: '', labelY: -18, labelWidth: 70, curve: -0.85 },
    { source: 'q_b', target: 'q_b',       label: '', loopDirection: '45deg', labelY: -22, labelX: 20, labelWidth: 60 },
    { source: 'q_b', target: 'q_both',    label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_wait',    label: '', labelX: 8, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_dead',    label: '', labelY: 12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_no',      label: '', labelX: -8, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_dead', label: '', loopDirection: '0deg', labelX: 22, labelWidth: 60 },
    { source: 'q_dead', target: 'q_wait', label: '', labelY: -10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_b',    label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_no',   label: '', labelY: 10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_both', label: '', labelY: 18, labelWidth: 60, curve: -0.85 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצבים אלו (המסומנים בצהוב), כללי ה-Until אינם מגבילים את המצב הבא:
<ul>
<li>במצבים שבהם התנאי הימני <span dir="rtl"><KatexInline math="b \in B" /></span> מתקיים, ולכן ההבטחה מומשה ואין המשכיות כפויה.</li>
<li>במצבים שבהם התנאי השמאלי <span dir="rtl"><KatexInline math="a \notin B" /></span> שקרי, ולכן אין דרישה למנוע יצירת הבטחה.</li>
</ul>
המעברים האפשריים מהם נקבעים אך ורק לפי התאמת האות הנקראת למצב היעד.
</div>
</div>
</div>

---

# דוגמה: מצבי ההתחלה של האוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, initial: true, initialDirection: 'bottom', stroke: '#16a34a', strokeWidth: 3 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', stroke: '#16a34a', strokeWidth: 3 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', stroke: '#16a34a', strokeWidth: 3 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, opacity: 0.4 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.4 }
  ]"
  :transitions="[
    { source: 'q_wait', target: 'q_wait', label: '', loopDirection: '-90deg', labelY: -22, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '', labelY: -12, labelWidth: 75, curve: 0.15 },
    { source: 'q_wait', target: 'q_b',    label: '', labelX: -12, labelWidth: 60, curve: 0.15 },
    { source: 'q_no', target: 'q_no',     label: '', loopDirection: '90deg', labelY: 22, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead',   label: '', labelY: 12, labelWidth: 60, curve: 0.15 },
    { source: 'q_both', target: 'q_both', label: '', loopDirection: '180deg', labelX: -22, labelWidth: 70 },
    { source: 'q_both', target: 'q_wait', label: '', labelY: -10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_b',    label: '', labelY: 12, labelWidth: 70, curve: 0.18 },
    { source: 'q_both', target: 'q_no',   label: '', labelY: 10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_dead', label: '', labelY: -18, labelWidth: 70, curve: -0.95 },
    { source: 'q_b', target: 'q_b',       label: '', loopDirection: '45deg', labelY: -22, labelX: 20, labelWidth: 60 },
    { source: 'q_b', target: 'q_both',    label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_wait',    label: '', labelX: 8, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_dead',    label: '', labelY: 12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_no',      label: '', labelX: -8, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_dead', label: '', loopDirection: '0deg', labelX: 22, labelWidth: 60 },
    { source: 'q_dead', target: 'q_wait', label: '', labelY: -10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_b',    label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_no',   label: '', labelY: 10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_both', label: '', labelY: 18, labelWidth: 60, curve: -0.95 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
מצב התחלה הוא מצב שבו הנוסחה <b>מתקיימת</b> במצב ההתחלתי:<br/>
<div dir="ltr" class="text-center my-1"><KatexInline math="Q_0 = \{B \in Q \mid \varphi \in B\}" /></div>
<ul>
<li><b>שלושה מצבים</b> מכילים <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span> ולכן הם מצבי התחלה אפשריים (ירוק).</li>
<li><b>שני המצבים הנותרים</b> מכילים <span dir="ltr"><KatexInline math="\neg(a\mathbin{\mathrm{U}}b) \in B" /></span> — הנוסחה שקרית שם, ולכן <b>אינם</b> מצבי התחלה.</li>
</ul>
</div>
</div>
</div>

---



# דוגמה: תנאי הקבלה של האוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, initial: true, initialDirection: 'bottom', accepting: true },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', accepting: false, stroke: '#dc2626' },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', accepting: true },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, accepting: true },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, accepting: true }
  ]"
  :transitions="[
    { source: 'q_wait', target: 'q_wait', label: '', loopDirection: '-90deg', labelY: -22, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '', labelY: -12, labelWidth: 75, curve: 0.15 },
    { source: 'q_wait', target: 'q_b', label: '', labelX: -12, labelWidth: 60, curve: 0.15 },
    { source: 'q_no', target: 'q_no', label: '', loopDirection: '90deg', labelY: 22, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '', labelY: 12, labelWidth: 60, curve: 0.15 },
    { source: 'q_both', target: 'q_both', label: '', loopDirection: '180deg', labelX: -22, labelWidth: 70 },
    { source: 'q_both', target: 'q_wait', label: '', labelY: -10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_b',    label: '', labelY: 12, labelWidth: 70, curve: 0.18 },
    { source: 'q_both', target: 'q_no',   label: '', labelY: 10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_dead', label: '', labelY: -18, labelWidth: 70, curve: -0.95 },
    { source: 'q_b', target: 'q_b',       label: '', loopDirection: '45deg', labelY: -22, labelX: 20, labelWidth: 60 },
    { source: 'q_b', target: 'q_both',    label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_wait',    label: '', labelX: 8, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_dead',    label: '', labelY: 12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_no',      label: '', labelX: -8, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_dead', label: '', loopDirection: '0deg', labelX: 22, labelWidth: 60 },
    { source: 'q_dead', target: 'q_wait', label: '', labelY: -10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_b',    label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_no',   label: '', labelY: 10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_both', label: '', labelY: 18, labelWidth: 60, curve: -0.95 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
קבוצת הקבלה עבור הבטחת ה-Until היא:
<div dir="ltr" class="text-center my-1"><KatexInline math="F_{a\mathbin{\mathrm{U}}b} = \{B \mid a\mathbin{\mathrm{U}}b \notin B \lor b \in B\}" /></div>
המצבים שמקיימים זאת הם אלו שבהם <b>אין הבטחה פתוחה שטרם מומשה</b>:<br/>
<ul>
<li>המצבים שבהם <span dir="rtl"><KatexInline math="b \in B" /></span> (ולכן ההבטחה מתממשת כעת)</li>
<li>המצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span>)</li>
</ul>
רק המצב שבו ההבטחה פתוחה וממתינה למימוש (מסומן באדום) אינו מקבל.
</div>
</div>
</div>

---

# מה קורה אם בנוסחה Until בכלל?

<div class="mt-7 text-right text-[21px] leading-relaxed">
אם <span dir="ltr"><KatexInline math="\varphi" /></span> אינה מכילה אף תת־נוסחת <span dir="ltr">Until</span>, אין הבטחות לאכוף כלל.
</div>

<div class="mt-5 bg-blue-50 border border-blue-200 rounded p-4 text-blue-900 text-right text-[20px] leading-relaxed">
קבוצת קבוצות הקבלה <span dir="ltr"><KatexInline math="\mathcal{F}=\emptyset" /></span> — תנאי הקבלה של <span dir="ltr">GNBA</span> הוא קוניונקציה על כל הקבוצות ב־<span dir="ltr"><KatexInline math="\mathcal{F}" /></span>.
</div>

<div class="mt-5 bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900 text-right text-[20px] leading-relaxed">
קוניונקציה על קבוצה ריקה מתקיימת תמיד ("vacuous truth") — כך שכל ריצה אינסופית של האוטומט היא ריצה מקבלת.
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-4 text-amber-900 text-right text-[20px] leading-relaxed">
הגיוני: בלי <span dir="ltr">Until</span> אין דרישת חַיּוּת (liveness) שיש לאכוף — אין מה לבדוק "אינסוף פעמים", ולכן כל ניחוש עקבי לכל אורך הריצה הוא קביל.
</div>

---

# נכונות הבנייה: שני כיווני ההוכחה

<div class="mt-6 text-right text-[20px] leading-relaxed">
צריך להוכיח <span dir="ltr"><KatexInline math="\mathcal{L}_{\omega}(\mathcal{G}_{\varphi})=Words(\varphi)" /></span> — שתי הכלות בנפרד, עבור מילה <span dir="ltr"><KatexInline math="\sigma" /></span>:
</div>

<div class="mt-5 grid grid-cols-2 gap-5 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">⊆ נכונות: ריצה מקבלת ⟸ סיפוק</div>
אם יש ריצה מקבלת <span dir="ltr"><KatexInline math="B_0 \xrightarrow{A_0} B_1 \xrightarrow{A_1}\cdots" /></span> של <span dir="ltr"><KatexInline math="\mathcal{G}_{\varphi}" /></span> על <span dir="ltr"><KatexInline math="\sigma" /></span>, אז <span dir="ltr"><KatexInline math="\sigma\models\varphi" /></span>.
<div class="mt-2 text-[14.5px] text-blue-700">
<b>טיעון:</b> אינדוקציה מבנית על תת־נוסחאות <span dir="ltr"><KatexInline math="\psi" /></span> מוכיחה <span dir="ltr"><KatexInline math="\sigma[i..]\models\psi \iff \psi\in B_i" /></span> לכל <span dir="ltr"><KatexInline math="i" /></span>. עבור אטומים, שלילה וקוניונקציה זה נובע ישירות מעקביות בוליאנית, ועבור <span dir="ltr"><KatexInline math="\bigcirc" /></span> — ישירות מיחס המעברים. החלק העדין הוא <span dir="ltr"><KatexInline math="\mathrm{U}" /></span>: כללי המעבר מאפשרים לדחות את ההבטחה הלאה, ותנאי הקבלה הוא מה שמונע דחייה לנצח — בלעדיו הריצה הייתה יכולה "לשקר".
</div>
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">⊇ שלמות: סיפוק ⟸ קיום ריצה מקבלת</div>
אם <span dir="ltr"><KatexInline math="\sigma\models\varphi" /></span>, אז ל־<span dir="ltr"><KatexInline math="\mathcal{G}_{\varphi}" /></span> יש ריצה מקבלת על <span dir="ltr"><KatexInline math="\sigma" /></span>.
<div class="mt-2 text-[14.5px] text-emerald-700">
<b>טיעון:</b> בונים את "הריצה הקנונית" <span dir="ltr"><KatexInline math="B_i=\{\psi\mid \sigma[i..]\models\psi\}" /></span>. עקביות וההתאמה ליחס המעברים נובעות ישירות מסמנטיקת ה־LTL (כך מוגדרו הכללים). תנאי הקבלה מתקיים כי סמנטיקת <span dir="ltr"><KatexInline math="\mathrm{U}" /></span> עצמה מחייבת שכל הבטחה תתממש בפועל בנקודה כלשהי — כך שזה לא "בנוי" כתנאי נוסף אלא נכון אוטומטית מהגדרת הסיפוק.
</div>
</div>
</div>

---

# התוצאה המרכזית

<div class="mt-7 bg-emerald-50 border border-emerald-200 rounded p-5 text-emerald-900 text-right text-[22px] leading-relaxed">
לכל נוסחת <span dir="ltr">LTL</span> <span dir="ltr"><KatexInline math="\varphi" /></span> מעל <span dir="ltr"><KatexInline math="AP" /></span> אפשר לבנות <span dir="ltr">GNBA</span> <span dir="ltr"><KatexInline math="\mathcal{G}_{\varphi}" /></span> כך ש:
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="\mathcal{L}_{\omega}(\mathcal{G}_{\varphi})=Words(\varphi)" />
</div>

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
גודל האוטומט חסום אקספוננציאלית בגודל הנוסחה.
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
מספר קבוצות הקבלה חסום על ידי מספר תת־נוסחאות ה־<span dir="ltr">Until</span>.
</div>
</div>

---

# מה זה נותן לאימות?

<div class="mt-7 grid grid-cols-3 gap-4 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">מתרגמים</div>
בונים אוטומט עבור <span dir="ltr"><KatexInline math="\neg\varphi" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">מרכיבים</div>
יוצרים מכפלה עם מערכת המעברים <span dir="ltr"><KatexInline math="TS" /></span>.
</div>
<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
<div class="font-bold text-red-800 mb-2">מחפשים</div>
בודקים אם קיימת ריצה מקבלת, כלומר דוגמה נגדית.
</div>
</div>

<div class="mt-8 text-center text-[29px]" dir="ltr">
<KatexInline display math="TS\models\varphi \iff \mathcal{L}_{\omega}(TS\times\mathcal{A}_{\neg\varphi})=\emptyset" />
</div>

---

# סיכום

<div class="mt-7 grid grid-cols-2 gap-5 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4 text-blue-900">
<div class="font-bold text-blue-800 mb-2">מצבים הם ניחושים</div>
כל מצב מתאר אילו תת־נוסחאות נכונות בסיפה הנוכחית.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-emerald-900">
<div class="font-bold text-emerald-800 mb-2">מעברים הם בדיקות עקביות</div>
האות הנקראת, <span dir="ltr">Next</span>, וכללי הפריסה של <span dir="ltr">Until</span> קובעים אילו מעברים מותרים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-amber-900">
<div class="font-bold text-amber-800 mb-2">קבלה סוגרת הבטחות</div>
קבוצות הקבלה מבטיחות שכל <span dir="ltr">Until</span> שנפתח גם יגיע בסוף לצד הימני.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4 text-red-900">
<div class="font-bold text-red-800 mb-2">LTL היא ω-רגולרית</div>
כל נוסחת <span dir="ltr">LTL</span> מגדירה שפה שמתקבלת על ידי אוטומט Büchi.
</div>
</div>
