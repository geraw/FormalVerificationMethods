---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 06-SMV
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## SMV / NuSMV
  מרצה: גרא וייס
---

# SMV / NuSMV
## מבוא לשפת המידול ולאימות מודלים של מערכות תגובתיות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-4 items-center">
<div class="text-[15px] leading-snug text-right">

- להכיר את <span dir="ltr">SMV / NuSMV</span> ככלי מעשי לניתוח מערכות סופיות.

- להבין איך מתרגמים מודל של מערכת תגובתית ליחס מעברים פורמלי.
- לראות את אבני הבניין של שפת <span dir="ltr">SMV</span>: משתנים, טיפוסים, <span dir="ltr">MODULE</span>, השמות, <span dir="ltr">DEFINE</span>, <span dir="ltr">INIT/TRANS</span>, ותכונות.
- להבין את זרימת העבודה: סימולציה, בדיקת <span dir="ltr">CTL</span>, בדיקת <span dir="ltr">LTL</span>, ו-<span dir="ltr">Bounded Model Checking</span>.
- לעבוד דרך דוגמאות של מערכות תגובתיות מעניינות: בקר פשוט, רמזור, סמפור, ארביטר ומונה מודולו.

</div>
<div class="flex justify-center">
  <img src="/images/engineer_model.png" class="rounded shadow-lg" style="height: 320px;" />
</div>
</div>


---

# איפה אנחנו במסלול הקורס?

<div class="text-[13px] leading-snug text-right">

<div class="bg-yellow-50 border border-yellow-200 rounded-xl p-3 mb-3">
עד עכשיו למדנו איך <b>למדל מערכות</b> בעזרת <b>מערכות מעברים</b> ו-<b dir="ltr">(Nano)Promela</b>.
עכשיו אנחנו עושים <b>תחנת ביניים קצרה</b>: בוחן והיכרות עם כלי נוסף שממדל מערכות מעברים בצורה קצת אחרת.
בשיעור הבא נמשיך עם אימות אוטומטי של דרישות.
</div>

<div class="grid grid-cols-4 gap-3" dir="ltr">
  <div class="bg-sky-50 border-2 border-sky-200 rounded-xl p-3 shadow-sm">
    <div class="text-3xl mb-1">🧩</div>
    <div class="font-bold text-sky-800 text-[12px]">מה שכבר עשינו</div>
    <div class="text-[11px] text-slate-700 mt-1" dir="rtl">מערכות מעברים + פרומלה</div>
    <div class="mt-2 text-[10px] bg-white/80 border border-sky-100 rounded p-1" dir="rtl">"אני יודע לתאר מערכת פורמלית"</div>
  </div>

  <div class="bg-amber-50 border-2 border-amber-200 rounded-xl p-3 shadow-sm">
    <div class="text-3xl mb-1">☕📝</div>
    <div class="font-bold text-amber-800 text-[12px]">תחנת ביניים</div>
    <div class="text-[11px] text-slate-700 mt-1" dir="rtl">הפסקה לבוחן + שיעור על כלי חדש</div>
    <div class="mt-2 text-[10px] bg-white/80 border border-amber-100 rounded p-1" dir="rtl">"אותו רעיון, כלי עבודה אחר"</div>
  </div>

  <div class="bg-emerald-50 border-2 border-emerald-200 rounded-xl p-3 shadow-sm">
    <div class="text-3xl mb-1">🏠💻</div>
    <div class="font-bold text-emerald-800 text-[12px]">תרגול עצמי</div>
    <div class="text-[11px] text-slate-700 mt-1" dir="rtl">תרגיל בית לעבודה עצמית עם הכלי</div>
    <div class="mt-2 text-[10px] bg-white/80 border border-emerald-100 rounded p-1" dir="rtl">"עכשיו מתנסים לבד"</div>
  </div>

  <div class="bg-violet-50 border-2 border-violet-200 rounded-xl p-3 shadow-sm">
    <div class="text-3xl mb-1">🔍✅</div>
    <div class="font-bold text-violet-800 text-[12px]">המשך הקורס</div>
    <div class="text-[11px] text-slate-700 mt-1" dir="rtl">סוגי תכונות ואימות אוטומטי של דרישות</div>
    <div class="mt-2 text-[10px] bg-white/80 border border-violet-100 rounded p-1" dir="rtl">"לא רק לבנות מודל, גם לבדוק אותו"</div>
  </div>
</div>

<div class="text-center text-2xl mt-2" dir="ltr">🧩 ➜ ☕📝 ➜ 🏠💻 ➜ 🔍✅</div>

</div>

---

# מהו NuSMV?

<div class="text-[14px] leading-snug">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 mt-2 text-right"> <b>NuSMV</b> הוא מימוש מחדש והרחבה של <b>SMV</b>, כלי האימות הסימבולי הראשון שהתבסס על <span dir="ltr">BDD</span>. הכלי מיועד לאימות פורמלי של <b>מערכות סופיות ומערכות תגובתיות</b>.
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-right">
<div class="bg-blue-50 p-3 rounded border border-blue-200 text-left">
<div class="font-bold mb-2">מה הכלי יודע לעשות?</div>
<ul class="list-disc pr-5 space-y-2">
<li>לנתח מודלים סינכרוניים וא-סינכרוניים.</li>
<li>לבדוק <span dir="ltr">Invariants</span>, נוסחאות <span dir="ltr">CTL</span> ו-<span dir="ltr">LTL</span>.</li>
<li>להציג עקבות נגדיות כאשר תכונה נכשלת.</li>
<li>לתמוך גם ב-<span dir="ltr">BDD-based model checking</span> וגם ב-<span dir="ltr">SAT-based BMC</span>.</li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">למה זה מתאים לקורס?</div>
<ul class="list-disc pr-5 space-y-2">
<li>השפה קרובה לרעיון של מערכת מעברים.</li>
<li>אפשר לכתוב מודלים קטנים אבל לא טריוויאליים.</li>
<li>קל לראות את הקשר בין המודל, הלוגיקה והתוצאה.</li>
<li>הכלי מייצר <b>counterexample</b>, כלומר ריצה שמפריכה את התכונה.</li>
</ul>
</div>
</div>

</div>

---

# דוגמה: ניתוח סימבולי אחורה

<div class="text-[13px] leading-snug text-right">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 mt-2">
נרצה להוכיח שהמערכת <b>לא יכולה להגיע ל-<span dir="ltr">l4</span></b>.
במקום למנות את כל המצבים האפשריים, נייצג <b>קבוצות של מצבים</b> בעזרת פסוקים
ונחשב אותן <b>אחורה</b>.
</div>

<div class="grid grid-cols-2 gap-4 mt-4 items-start">
<div class="bg-amber-50 p-3 rounded border border-amber-200">
<div class="font-bold mb-2">גרף התוכנית</div>
<div class="flex justify-center">
<TransitionSystemD3
  :width="300"
  :height="255"
  :auto="false"
  :states="[
    {
      id: 'l1sym',
      text: '$l_1$',
      x: 85,
      y: 34,
      width: 52,
      color: '#fde047',
      stroke: '#a16207',
      initial: true,
      initialDirection: 'top',
      initialText: '$1 \\le x \\le 10,\\ 1 \\le y \\le 10$',
      initialTextWidth: 170,
      initialTextHeight: 26,
    },
    {
      id: 'l2sym',
      text: '$l_2$',
      x: 85,
      y: 96,
      width: 52,
      color: '#fde047',
      stroke: '#a16207',
    },
    {
      id: 'l3sym',
      text: '$l_3$',
      x: 85,
      y: 158,
      width: 52,
      color: '#fde047',
      stroke: '#a16207',
    },
    {
      id: 'l4sym',
      text: '$l_4$',
      x: 85,
      y: 220,
      width: 52,
      color: '#dc2626',
      stroke: '#991b1b',
    },
  ]"
  :transitions="[
    {
      source: 'l1sym',
      target: 'l2sym',
      action: '$true : y := y + 10$',
      actionWidth: 126,
      actionX: 84,
      actionY: -2,
    },
    {
      source: 'l2sym',
      target: 'l3sym',
      action: '$true : x := x + 1$',
      actionWidth: 120,
      actionX: 82,
      actionY: -2,
    },
    {
      source: 'l3sym',
      target: 'l4sym',
      action: '$x > y : \\texttt{nothing}$',
      actionWidth: 130,
      actionX: 92,
      actionY: -2,
    },
  ]"
/>
</div>

<div class="text-center text-[12px] text-red-700 -mt-3 font-semibold">Assertion violation</div>
</div>

<div class="space-y-3">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">חישוב אחורה באופן סימבולי</div>

<div dir="ltr" class="text-left">
<div class="symbolic-backward-note">Each line is a symbolic set of states.</div>
<div class="symbolic-backward-row"><span class="symbolic-backward-name">S0</span><span class="symbolic-backward-op">=</span><span class="symbolic-backward-formula">at l4</span></div>
<div class="symbolic-backward-row"><span class="symbolic-backward-name">S1</span><span class="symbolic-backward-op">=</span><span class="symbolic-backward-formula">Pre(S0) = at l3 ∧ x &gt; y</span></div>
<div class="symbolic-backward-row"><span class="symbolic-backward-name">S2</span><span class="symbolic-backward-op">=</span><span class="symbolic-backward-formula">Pre(S1) = at l2 ∧ x + 1 &gt; y</span></div>
<div class="symbolic-backward-row"><span class="symbolic-backward-name">S3</span><span class="symbolic-backward-op">=</span><span class="symbolic-backward-formula">Pre(S2) = at l1 ∧ x + 1 &gt; y + 10</span></div>
</div>

<div class="mt-3 bg-green-50 border border-green-200 rounded p-3 text-[12px]">
<div class="font-bold mb-1">התנגשות עם תנאי ההתחלה</div>
אם <span dir="ltr"><code>1 ≤ x ≤ 10</code></span> ו-<span dir="ltr"><code>1 ≤ y ≤ 10</code></span>,
אז בהכרח <span dir="ltr"><code>x + 1 ≤ 11</code></span> וגם
<br><span dir="ltr"><code>y + 10 ≥ 11</code></span>, ולכן
<span dir="ltr"><code>x + 1 &gt; y + 10</code></span> בלתי אפשרי.
</div>
</div>

<div class="bg-rose-50 p-3 rounded border border-rose-200 text-[11px] leading-snug">
לא רשמנו אפילו מצב אחד במפורש. בכל שורה כתבנו <b>קבוצה שלמה של מצבים</b>, ואז הפעלנו עליה
את <span dir="ltr"><code>Pre</code></span>.

<div class="mt-2">
כאן יש <span dir="ltr"><code>4 · 10 · 10 = 400</code></span> מצבים. אם היינו מכפילים את כל הקבועים פי 10,
היינו מגיעים לכ-<span dir="ltr"><code>4 · 100 · 100 = 40{,}000</code></span> מצבים, כלומר
<b>פי 100 יותר מצבים</b>.
</div>

<div class="mt-2">
אבל עדיין היינו צריכים רק <b>4 צעדי חישוב אחורה</b>, כי מספר הצעדים נקבע על ידי
מבנה הבקרה של הגרף, ולא על ידי מספר המצבים המפורש.
</div>
</div>
</div>
</div>

</div>

---

# אז מה זה BDD?

<div class="text-[14px] leading-snug text-right">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 mt-2">
<span dir="ltr">BDD = Binary Decision Diagram</span>. זהו <b>גרף מכוון, מושרש וחסר-מחזורים</b>
שמייצג פונקציה בוליאנית: בכל צומת פנימי שואלים על משתנה אחד, הקשתות מייצגות
<span dir="ltr">0/1</span>, והעלים הם <span dir="ltr">0</span> ו-<span dir="ltr">1</span>.
בפועל כמעט תמיד משתמשים ב-<span dir="ltr">ROBDD</span>: אותו סדר משתנים על כל מסלול,
איחוד תתי-גרפים זהים והסרת צמתים מיותרים. עבור סדר משתנים קבוע מתקבל ייצוג קנוני.
</div>

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">דוגמה מאימות מערכות</div>
נניח שמצב של פרוטוקול הדדיות מקודד על ידי
<span dir="ltr"><code>crit0, crit1, want0, want1, turn</code></span>.

$$
Bad = crit0 \land crit1
$$

<div class="mt-3">
זו קבוצת המצבים שבה <b>שני התהליכים נמצאים יחד בקטע הקריטי</b>.
יש כאן <span dir="ltr"><code>2^5 = 32</code></span> מצבים אפשריים, אבל
הנוסחה למעלה מתארת בבת אחת את כל <span dir="ltr"><code>8</code></span> המצבים הבעייתיים.
</div>

<div class="mt-2">
המשתנים <span dir="ltr"><code>want0,want1,turn</code></span> בכלל לא משנים כאן, ולכן
ייצוג סימבולי טוב לא צריך "לפתוח" אותם.
</div>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">איך BDD "רואה" את הקבוצה?</div>
<div class="text-[13px]">
במקום למנות מצבים, הוא שואל רק על המשתנים שבאמת קובעים:
</div>

<div dir="ltr" class="mt-1 bg-white/80 rounded border border-slate-200 p-3">
<div class="relative -mt-6 mx-auto h-[140px] max-w-[270px] scale-50">
  <div class="absolute left-[134px] top-[28px] border-t-[3px] border-dashed border-slate-500 origin-left" style="width: 166px; transform: rotate(119deg);"></div>
  <div class="absolute left-[134px] top-[28px] border-t-[3px] border-sky-600 origin-left" style="width: 112px; transform: rotate(47deg);"></div>
  <div class="absolute left-[210px] top-[110px] border-t-[3px] border-dashed border-slate-500 origin-left" style="width: 169px; transform: rotate(158deg);"></div>
  <div class="absolute left-[210px] top-[110px] border-t-[3px] border-sky-600 origin-left" style="width: 74px; transform: rotate(65deg);"></div>

  <div class="absolute left-[112px] top-[6px] z-10 h-[44px] w-[44px] rounded-full border-[3px] border-blue-600 bg-blue-100 flex items-center justify-center text-[11px] font-semibold text-blue-900">crit0</div>
  <div class="absolute left-[188px] top-[88px] z-10 h-[44px] w-[44px] rounded-full border-[3px] border-blue-600 bg-blue-100 flex items-center justify-center text-[11px] font-semibold text-blue-900">crit1</div>
  <div class="absolute left-[36px] top-[156px] z-10 h-[34px] w-[34px] rounded-md border-[3px] border-slate-500 bg-slate-50 flex items-center justify-center text-[18px] font-semibold text-slate-700">0</div>
  <div class="absolute left-[224px] top-[160px] z-10 h-[34px] w-[34px] rounded-md border-[3px] border-lime-600 bg-lime-50 flex items-center justify-center text-[18px] font-semibold text-lime-700">1</div>

  <div class="absolute left-[78px] top-[82px] z-20 text-[12px] font-semibold text-slate-600">0</div>
  <div class="absolute left-[182px] top-[52px] z-20 text-[12px] font-semibold text-sky-700">1</div>
  <div class="absolute left-[136px] top-[148px] z-20 text-[12px] font-semibold text-slate-600">0</div>
  <div class="absolute left-[238px] top-[130px] z-20 text-[12px] font-semibold text-sky-700">1</div>
</div>

</div>

<div class="mt-3 text-[13px]">
זה כל הרעיון: הרבה מצבים מפורשים מתכנסים לגרף קטן, וכאן אפילו רואים
ששתי דרכים שונות מגיעות לאותו עלה <span dir="ltr"><code>0</code></span>.
</div>
</div>
</div>

<div class="mt-4 bg-amber-50 p-3 rounded border border-amber-200 text-[13px]">
אין צורך לדעת לבנות <span dir="ltr">BDD</span>-ים ביד. חשוב רק להבין שהם שומרים
תיאורים בוליאניים בצורה קומפקטית, עם הרבה שיתוף פנימי, ולכן הם יכולים לייצג
מרחבי מצבים גדולים הרבה יותר ממה שאפשר לכתוב ידנית.
</div>

</div>

---

# איך NuSMV משתמש בזה?

<div class="text-[13px] leading-snug text-right">

<div class="grid grid-cols-3 gap-4 mt-2">
<div class="bg-blue-50 p-2.5 rounded border border-blue-200">
<div class="font-bold mb-2"><span dir="ltr">Init(V)</span></div>
קבוצת המצבים ההתחלתיים.
</div>

<div class="bg-green-50 p-2.5 rounded border border-green-200">
<div class="font-bold mb-2"><span dir="ltr">Trans(V,V')</span></div>
כל המעברים החוקיים בין <span dir="ltr">V</span> ל-<span dir="ltr">V'</span>.
</div>

<div class="bg-rose-50 p-2.5 rounded border border-rose-200">
<div class="font-bold mb-2"><span dir="ltr">Bad(V)</span></div>
המצבים שמפרים את התכונה.
</div>
</div>

<div class="grid grid-cols-2 gap-4 mt-3">
<div class="bg-slate-50 p-3 rounded border border-slate-200 text-center">

<div class="font-bold text-[12px] mb-2"><span dir="ltr">Forward reachability</span></div>

$$
R_0 = Init
$$

$$
R_{i+1} = R_i \cup Post(R_i)
$$

$$
Post(R) = \{\, s' \mid \exists s \in R : Trans(s,s') \,\}
$$

</div>

<div class="bg-slate-50 p-3 rounded border border-slate-200 text-center">

<div class="font-bold text-[12px] mb-2"><span dir="ltr">Backward reachability</span></div>

$$
P_0 = Bad
$$

$$
P_{i+1} = P_i \cup Pre(P_i)
$$

$$
Pre(P) = \{\, s \mid \exists s' \in P : Trans(s,s') \,\}
$$

</div>
</div>

<div class="grid grid-cols-2 gap-4 mt-3">
<div class="bg-purple-50 p-3 rounded border border-purple-200">
<div class="font-bold mb-2">מה האלגוריתם עושה?</div>
<ul class="list-disc pr-5 space-y-1.5 text-[12px]">
<li>לפעמים נוח לחשב קדימה מ-<span dir="ltr">Init</span>, ולפעמים אחורה מ-<span dir="ltr">Bad</span>.</li>
<li>בכל שלב מוסיפים לא מצב בודד, אלא קבוצה שלמה של מצבים.</li>
<li>עוצרים כשהקבוצה כבר לא משתנה.</li>
<li>בדוגמה הקודמת השתמשנו בדיוק בחישוב אחורה כזה.</li>
</ul>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200">
<div class="font-bold mb-2">המסר החשוב לקורס</div>
<ul class="list-disc pr-5 space-y-1.5 text-[12px]">
<li>לא עובדים על קשתות בודדות, אלא על קבוצות של מצבים ומעברים.</li>
<li><span dir="ltr">BDD</span> הוא אחת הדרכים היעילות לשמור את הייצוגים האלה.</li>
<li>לכן <span dir="ltr">NuSMV</span> יכול לטפל גם במודלים שקשה מאוד לצייר במפורש.</li>
</ul>
</div>
</div>

</div>

---

# התקנת NuSMV

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div class="text-right text-[13px] leading-snug">

<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">Windows</div>
<ul class="list-disc pr-5 space-y-2">
<li>להוריד את <span dir="ltr"><code>NuSMV-2.7.0-win64.zip</code></span> מדף ההורדות הרשמי.</li>
<li>לחלץ לתיקיה קבועה, למשל <span dir="ltr"><code>C:\tools\NuSMV</code></span>.</li>
<li>להוסיף את <span dir="ltr"><code>bin</code></span> ל-<span dir="ltr"><code>PATH</code></span> כדי שאפשר יהיה להריץ מכל טרמינל.</li>
<li>בדיקת תקינות ראשונה: <span dir="ltr"><code>NuSMV.exe -int short.smv</code></span>.</li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200 mt-3">
<div class="font-bold mb-2">Linux / macOS</div>
<ul class="list-disc pr-5 space-y-2">
<li>ב-<span dir="ltr">Linux</span> להוריד את <span dir="ltr"><code>NuSMV-2.7.0-linux64.tar.xz</code></span>, וב-<span dir="ltr">macOS</span> את <span dir="ltr"><code>NuSMV-2.7.0-macos-universal.tar.xz</code></span>.</li>
<li>ב-<span dir="ltr">macOS</span> נדרשים גם <span dir="ltr"><code>Command Line Tools</code></span> ו-<span dir="ltr"><code>gmp</code></span>.</li>
<li>אפשר להוסיף את תיקיית <span dir="ltr"><code>bin</code></span> ל-<span dir="ltr"><code>PATH</code></span> או להריץ ישירות מתוך התיקיה שחולצה.</li>
<li>גם כאן בדיקת העשן הפשוטה היא <span dir="ltr"><code>NuSMV -int short.smv</code></span>.</li>
</ul>
</div>

</div>

<div dir="ltr" class="small-code">

```sh
# Linux
wget https://nusmv.fbk.eu/distrib/2.7.0/NuSMV-2.7.0-linux64.tar.xz
tar -xf NuSMV-2.7.0-linux64.tar.xz
export PATH="$PWD/NuSMV-2.7.0-linux64/bin:$PATH"
NuSMV -int short.smv


# macOS
xcode-select --install
brew install gmp
curl -LO https://nusmv.fbk.eu/distrib/2.7.0/NuSMV-2.7.0-macos-universal.tar.xz
tar -xf NuSMV-2.7.0-macos-universal.tar.xz
export PATH="$PWD/NuSMV-2.7.0-macos-universal/bin:$PATH"
NuSMV -int short.smv


# Windows PowerShell
Invoke-WebRequest https://nusmv.fbk.eu/distrib/2.7.0/NuSMV-2.7.0-win64.zip -OutFile .\NuSMV-2.7.0-win64.zip
Expand-Archive .\NuSMV-2.7.0-win64.zip C:\tools\NuSMV
$env:Path += ";C:\tools\NuSMV\bin"
NuSMV.exe -int short.smv


```

<!-- <div class="mt-3 bg-amber-50 p-3 rounded border border-amber-200 text-right text-[12px] leading-snug">
מומלץ להוריד תמיד את הגרסה העדכנית ביותר מתוך דף ההורדות הרשמי, ולא להסתמך על קישור ישן.
</div> -->

</div>
</div>

---

# איך NuSMV חושב על מערכת?

<div class="text-[15px] leading-snug">

<div class="mt-3 bg-purple-50 p-4 rounded border border-purple-200 text-center">

$$
\text{קובץ SMV}
\Longrightarrow
\text{Transition System}
\Longrightarrow
\text{Reachability + Temporal Logic}
\Longrightarrow
\text{True / False + Counterexample}
$$

</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-right">
<div class="bg-amber-50 p-3 rounded border border-amber-200">
<div class="font-bold mb-2">המודל מגדיר</div>
<ul class="list-disc pr-5 space-y-2">
<li>קבוצת משתני מצב סופיים.</li>
<li>קבוצת מצבים התחלתיים.</li>
<li>יחס מעברים בין מצב נוכחי למצב הבא.</li>
<li>אילוצי הגינות במידת הצורך.</li>
</ul>
</div>

<div class="bg-rose-50 p-3 rounded border border-rose-200">
<div class="font-bold mb-2">האימות בודק</div>
<ul class="list-disc pr-5 space-y-2">
<li>אילו מצבים נגישים מן ההתחלה.</li>
<li>האם תכונה מתקיימת בכל המסלולים או בחלקם.</li>
<li>האם יש ריצה קצרה שמפריכה תכונה.</li>
<li>האם כשל נובע משגיאת מידול או מחוסר הוגנות.</li>
</ul>
</div>
</div>

</div>

---

# מבנה בסיסי של קובץ SMV

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="text-right text-[14px] leading-snug bg-slate-50 p-3 rounded border border-slate-200">
<div class="font-bold mb-2">מילות מפתח נפוצות</div>
<ul class="list-disc pr-5 space-y-2">
<li><span dir="ltr"><code>MODULE</code></span> – הגדרת מודול.</li>
<li><span dir="ltr"><code>VAR</code></span>, <span dir="ltr"><code>IVAR</code></span> – משתני מצב וקלט.</li>
<li><span dir="ltr"><code>ASSIGN</code></span> – הַשָּׂמוֹת למצב נוכחי, התחלתי והבא.</li>
<li><span dir="ltr"><code>DEFINE</code></span> – קיצור שמחושב פונקציונלית ואינו מגדיל את מרחב המצבים.</li>
<li><span dir="ltr"><code>INIT</code></span>, <span dir="ltr"><code>TRANS</code></span>, <span dir="ltr"><code>INVAR</code></span> – תיאור ישיר של ה-<span dir="ltr">FSM</span>.</li>
<li><span dir="ltr"><code>SPEC</code></span>, <span dir="ltr"><code>INVARSPEC</code></span>, <span dir="ltr"><code>LTLSPEC</code></span> – תכונות לאימות.</li>
</ul>
</div>

<div dir="ltr" class="small-code">

```text
MODULE main
VAR
  x : 0..3;
  mode : {idle, work};
IVAR
  start : boolean;
DEFINE
  busy := mode = work;
ASSIGN
  init(x) := 0;
  init(mode) := idle;
  next(x) := case
    mode = work : (x + 1) mod 4;
    TRUE        : x;
  esac;
  next(mode) := case
    mode = idle & start : work;
    x = 3               : idle;
    TRUE                : mode;
  esac;
INVARSPEC !(busy & x = 0)
LTLSPEC G (start -> F busy)
```

</div>
</div>

---

# דוגמה ראשונה: בקר מוכן/עסוק

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr" class="small-code">

```text
MODULE main
IVAR
  request : boolean;
VAR
  state   : {ready, busy};
ASSIGN
  init(state) := ready;
  next(state) := case
    state = ready & request : busy;
    TRUE                    : {ready, busy};
  esac;
```

<br>
<br>

<TransitionSystemD3 
 :states="[
  { id: 'ready', name: 'ready', initial: true, x: 200, y: 0, initialDirection: 'bottom' },   
  { id: 'busy',  name: 'busy', x: 0, y: 0 }
]"
  :transitions="[
    { source: 'ready', target: 'busy', action: 'true', curve:0.3, actionY: -6 }, 
    { source: 'ready', target: 'ready', action: '!request' },
    { source: 'busy', target: 'ready', action: 'true', curve:0.3, actionY: 7 },
    { source: 'busy', target: 'busy', action: 'true', loopDirection: '90deg', actionY: -10 }
  ]"
  :height="50"
  :width="200"
/>

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">מה רואים כאן?</div>
<ul class="list-disc pr-5 space-y-2">
<li><span dir="ltr"><code>request</code></span> לא מקבל השמה, לכן הוא קלט לא-מוגבל.</li>
<li><span dir="ltr"><code>state</code></span> הוא משתנה סקלרי עם שני ערכים סמליים.</li>
<li><span dir="ltr"><code>init(state)</code></span> קובע מצב התחלתי.</li>
<li><span dir="ltr"><code>{ready, busy}</code></span> מייצג בחירה לא-דטרמיניסטית.</li>
</ul>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200 mt-3">
<div class="font-bold mb-2">המשמעות הסמנטית</div>
המודל מגדיר <b>קבוצת מעברים חוקיים</b>. בכל צעד הכלי בוחר ערך מותר לכל
<span dir="ltr"><code>next(v)</code></span>, ובודק האם יש ריצה שמפרה את התכונות שביקשנו.
</div>
</div>
</div>

---

# כללי עבודה חשובים של ASSIGN

<div class="text-[14px] leading-snug">

<div class="grid grid-cols-2 gap-4 mt-2 text-right">
<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">מה נוח בשיטה הזאת?</div>
<ul class="list-disc pr-5 space-y-2">
<li>כל ההשמות במודול מתבצעות <b>במקביל</b>, לא ברצף אימפרטיבי.</li>
<li>הכלי בודק שגיאות כמו השמה כפולה ומשוב מעגלי.</li>
<li>תיאור כזה בדרך כלל מונע מודלים "לא ניתנים למימוש".</li>
</ul>
</div>

<div class="bg-rose-50 p-3 rounded border border-rose-200">
<div class="font-bold mb-2">ממה צריך להיזהר?</div>
<ul class="list-disc pr-5 space-y-2">
<li>אילוץ סותר ב-<span dir="ltr"><code>INIT</code></span> או <span dir="ltr"><code>TRANS</code></span> עלול ליצור מודל ריק.</li>
<li>מצב בלי יורש יוצר <span dir="ltr">deadlock</span>, ולעתים הופך תכונות לנכונות "רק בגלל תקלה במודל".</li>
<li>לא כל כשל התקדמות הוא כשל במערכת; לפעמים חסר אילוץ הגינות.</li>
</ul>
</div>
</div>

<div class="mt-4 bg-slate-50 p-3 rounded border border-slate-200 text-right">
כלל אצבע: להתחיל עם <span dir="ltr"><code>ASSIGN</code></span> ו-<span dir="ltr"><code>DEFINE</code></span>, ולעבור ל-<span dir="ltr"><code>TRANS</code></span> רק כאשר רוצים תיאור לוגי ישיר של יחס המעבר.
</div>

</div>

---

# טיפוסים, ביטויים ו-CASE

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div class="text-right text-[14px] leading-snug bg-slate-50 p-3 rounded border border-slate-200">
<div class="font-bold mb-2">טיפוסים סופיים נפוצים</div>
<ul class="list-disc pr-5 space-y-2">
<li><span dir="ltr"><code>boolean</code></span></li>
<li>טווחים שלמים: <span dir="ltr"><code>0..7</code></span></li>
<li>טיפוסים סמליים: <span dir="ltr"><code>{idle, wait, critical}</code></span></li>
<li>מערכים קבועים: <span dir="ltr"><code>array 0..1 of boolean</code></span></li>
</ul>

<div class="font-bold mt-4 mb-2">ביטויים חשובים</div>
<ul class="list-disc pr-5 space-y-2">
<li>אופרטורים בוליאניים ואריתמטיים רגילים.</li>
<li><span dir="ltr"><code>case ... esac</code></span> – בחירה מותנית.</li>
<li><span dir="ltr"><code>{a, b}</code></span>, <span dir="ltr"><code>union</code></span>, <span dir="ltr"><code>in</code></span> – קבוצות ובחירה לא-דטרמיניסטית.</li>
</ul>
</div>

<div dir="ltr" class="small-code">

```text
VAR
  turn  : 0..1;
  phase : {green, yellow, red};
  req   : array 0..1 of boolean;

DEFINE
  someone_waits := req[0] | req[1];
  next_phase := case
    phase = green  : yellow;
    phase = yellow : red;
    TRUE           : green;
  esac;

ASSIGN
  next(turn) := {0, 1};
```

</div>
</div>

---

# DEFINE מול VAR

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr" class="small-code">

```text
MODULE counter_cell(carry_in)
VAR
  value : boolean;
ASSIGN
  init(value) := FALSE;
  next(value) := value xor carry_in;
DEFINE
  carry_out := value & carry_in;

MODULE main
VAR
  bit0 : counter_cell(TRUE);
  bit1 : counter_cell(bit0.carry_out);
  bit2 : counter_cell(bit1.carry_out);
```

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">למה להשתמש ב-<span dir="ltr">DEFINE</span>?</div>
<ul class="list-disc pr-5 space-y-2">
<li>הוא מציג שם נוח לביטוי מורכב.</li>
<li>הוא לא מוסיף משתנה חדש למרחב המצבים.</li>
<li>הוא מתאים ל"אותות קומבינטוריים" ולתכונות עזר.</li>
</ul>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200 mt-3">
<div class="font-bold mb-2">מתי כן צריך <span dir="ltr">VAR</span>?</div>
כאשר הערך צריך להשתנות לאורך זמן ולהיות חלק מן המצב. אם צריך
<b>זיכרון</b>, צריך משתנה מצב; אם צריך רק <b>קיצור של ביטוי</b>, מספיק
<span dir="ltr"><code>DEFINE</code></span>.
</div>
</div>
</div>

---

# מודולים והיררכיה

<div class="text-[14px] leading-snug">

<div class="bg-slate-50 p-3 rounded border border-slate-200 text-right">
<span dir="ltr">SMV</span> תומכת ב-<b>תיאור מודולרי והיררכי</b>. אפשר לבנות תת-מודולים, להעביר להם פרמטרים, ולגשת לרכיבים בעזרת
<span dir="ltr"><code>instance.component</code></span>.
</div>

<div class="grid grid-cols-2 gap-4 mt-4 items-start">
<div dir="ltr" class="small-code">

```text
MODULE worker(lock)
VAR
  state : {idle, wait, critical};
ASSIGN
  init(state) := idle;
  next(state) := case
    state = idle            : {idle, wait};
    state = wait & !lock    : critical;
    state = critical        : idle;
    TRUE                    : state;
  esac;
  next(lock) := case
    state = wait     : TRUE;
    state = critical : FALSE;
    TRUE             : lock;
  esac;
```

</div>

<div class="text-right bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">הערה סמנטית חשובה</div>
ב-<span dir="ltr">NuSMV</span>, אינסטנציאציה של מודול מתנהגת בצורה דמוית
<span dir="ltr">call-by-reference</span>: אם מודול מקבל פרמטר שהוא משתנה, הוא יכול להשפיע עליו דרך השמות חוקיות.

<div class="mt-3">
זה חזק מאוד, אבל גם מחייב זהירות: כדאי לשמור על ממשק מודולרי ברור ולא להפוך כל פרמטר לערוץ כתיבה.
</div>
</div>
</div>

</div>

---

# אסינכרוניות עם process

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr" class="small-code">

```text
MODULE inverter(input)
VAR
  output : boolean;
ASSIGN
  init(output) := FALSE;
  next(output) := !input;
FAIRNESS running

MODULE main
VAR
  g1 : process inverter(g3.output);
  g2 : process inverter(g1.output);
  g3 : process inverter(g2.output);
```

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-purple-50 p-3 rounded border border-purple-200">
<div class="font-bold mb-2">מה עושה <span dir="ltr">process</span>?</div>
בכל צעד הכלי בוחר <b>תהליך אחד</b> שרץ, ומבצע את כל ההשמות שלו במקביל.
משתנים שלא הושמו בתהליך הנבחר שומרים על ערכם.
</div>

<div class="bg-rose-50 p-3 rounded border border-rose-200 mt-3">
<div class="font-bold mb-2">למה צריך הגינות?</div>
ללא <span dir="ltr"><code>FAIRNESS running</code></span>, ייתכן שתהליך לעולם לא ייבחר.
אז תכונת ההתקדמות יכולה להיכשל לא בגלל בעיה בפרוטוקול, אלא בגלל מתזמן לא הוגן.
</div>
</div>
</div>

---

# גם כך אפשר: INIT / TRANS / INVAR

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr" class="small-code">

```text
MODULE main
VAR
  y : 0..7;
INIT
  y = 0
TRANS
  next(y) = (y + 1) mod 8
INVAR
  y >= 0 & y <= 7
```

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">מתי זה נוח?</div>
<ul class="list-disc pr-5 space-y-2">
<li>כאשר רוצים לכתוב אילוץ לוגי ישיר על יחס המעבר.</li>
<li>כאשר המודל נוח יותר כקבוצה של נוסחאות מאשר כהשמות.</li>
<li>כאשר בונים אבסטרקציה או מודל סביבתי מהיר.</li>
</ul>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200 mt-3">
<div class="font-bold mb-2">אבל בזהירות</div>
גישה זו גמישה יותר, ולכן גם מסוכנת יותר: אפשר לכתוב בקלות יחס מעברים לא טוטלי,
או מצב התחלתי ריק. לכן בפרויקטים ראשונים נעדיף לרוב
<span dir="ltr"><code>ASSIGN</code></span>.
</div>
</div>
</div>

---

# סימולציה: להבין את המודל לפני שמוכיחים

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div class="text-right text-[14px] leading-snug bg-slate-50 p-3 rounded border border-slate-200">
<div class="font-bold mb-2">אינטראקציה טיפוסית</div>
<ul class="list-disc pr-5 space-y-2">
<li>הרצה במצב אינטראקטיבי: <span dir="ltr"><code>NuSMV -int model.smv</code></span></li>
<li>טעינת המודל: <span dir="ltr"><code>go</code></span></li>
<li>בחירת מצב התחלתי: <span dir="ltr"><code>pick_state -r</code></span> או <span dir="ltr"><code>pick_state -i</code></span></li>
<li>הרחבת עקבה: <span dir="ltr"><code>simulate -r 5</code></span></li>
<li>הצגת עקבות: <span dir="ltr"><code>show_traces -v</code></span></li>
</ul>

<div class="mt-3">
הסימולציה עוזרת לבדוק אם בכלל בנינו את המערכת הנכונה, עוד לפני בדיקת תכונות.
</div>
</div>

<div dir="ltr" class="small-code">

```sh
system_prompt> NuSMV -int short.smv
NuSMV > go
NuSMV > pick_state -r
NuSMV > simulate -r 3
NuSMV > show_traces -v
```

```text
-> State 1.1 <- request = 0, state = ready
-> State 1.2 <- request = 1, state = busy
-> State 1.3 <- request = 1, state = ready
-> State 1.4 <- request = 1, state = busy
```

</div>
</div>

---

# כתיבת תכונות

<div class="grid grid-cols-3 gap-3 mt-2 text-right text-[13px] leading-snug">
<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2"><span dir="ltr">INVARSPEC</span></div>
מתאים לתכונות מצביות פשוטות.

<div dir="ltr" class="text-left">

```text
INVARSPEC !(p0_crit & p1_crit)
```

</div>

זה שקול ל-<span dir="ltr"><code>SPEC AG ...</code></span>, אבל נבדק באלגוריתם ייעודי.
</div>

<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2"><span dir="ltr">SPEC</span> עבור CTL</div>
מדבר על כל המסלולים או קיום מסלול.

<div dir="ltr" class="text-left">

```text
SPEC AG (request -> AF grant)
SPEC EF error
SPEC AG !(red_ns & red_ew)
```

</div>
</div>

<div class="bg-purple-50 p-3 rounded border border-purple-200">
<div class="font-bold mb-2"><span dir="ltr">LTLSPEC</span></div>
מדבר על ריצות לינאריות.

<div dir="ltr" class="text-left">

```text
LTLSPEC G (req0 -> F grant0)
LTLSPEC G !(overflow)
LTLSPEC G F heartbeat
```

</div>

</div>
</div>

---

# דוגמה 1: רמזור דו-כיווני

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr">

```text
MODULE main

VAR
  phase : {ns_green, ns_yellow, ns_red_wait, 
           ew_green, ew_yellow, ew_red_wait};

ASSIGN
  init(phase) := ns_green;
  next(phase) := case
    phase = ns_green  : ns_yellow;
    phase = ns_yellow : ns_red_wait;
    phase = ns_red_wait : ew_green;
    phase = ew_green  : ew_yellow;
    phase = ew_yellow : ew_red_wait;
    phase = ew_red_wait : ns_green;
    TRUE              : phase;
  esac;

DEFINE
  ns_go := phase = ns_green;
  ew_go := phase = ew_green;
```

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">מה נבדוק?</div>
<div dir="ltr" class="text-left">

```text
INVARSPEC !(ns_go & ew_go)
LTLSPEC G (ns_go -> F ew_go)
LTLSPEC G (ew_go -> F ns_go)
```

</div>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200 mt-3">
<div class="font-bold mb-2">למה זו דוגמה טובה?</div>
יש כאן גם <b>בטיחות</b> וגם <b>התקדמות</b>:
לא ייתכנו שני כיוונים ירוקים יחד, וכל כיוון שמקבל ירוק מפנה בסוף את הבמה לאחר.
</div>
</div>
</div>

---

# דוגמה 2: הדדיות בעזרת סמפור

<div class="grid grid-cols-2 gap-4 mt-2 items-start">

<div dir="ltr" class="small-code">

```text 
MODULE main
VAR
  sem  : boolean;
  p0   : process user(sem);
  p1   : process user(sem);
ASSIGN
  init(sem) := FALSE;

MODULE user(sem)
VAR
  st : {idle, wait, critical, release};
ASSIGN
  init(st) := idle;
  next(st) := case
    st = idle                 : {idle, wait};
    st = wait & !sem          : critical;
    st = critical             : release;
    st = release              : idle;
    TRUE                      : st;
  esac;
  next(sem) := case
    st = wait & !sem : TRUE;
    st = release     : FALSE;
    TRUE             : sem;
  esac;
FAIRNESS running
```

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">תכונות טבעיות</div>
<div dir="ltr" class="text-left">

```text
INVARSPEC !(p0.st = critical & p1.st = critical)
SPEC AG (p0.st = wait -> AF p0.st = critical)
SPEC AG (p1.st = wait -> AF p1.st = critical)
```

</div>
</div>

<div class="bg-rose-50 p-3 rounded border border-rose-200 mt-3">
<div class="font-bold mb-2">מה לומדים מהמודל?</div>
בטיחות ההדדיות לרוב קלה יחסית. תכונות התקדמות, לעומת זאת, תלויות לא רק בפרוטוקול
אלא גם בהנחת הוגנות על המתזמן.
</div>
</div>
</div>

---

# דוגמה 3: בורר בין שני לקוחות

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr" >

```text
MODULE main
IVAR
  req0 : boolean;
  req1 : boolean;
VAR
  turn  : 0..1;
  grant : {none, g0, g1};
ASSIGN
  init(turn) := 0;
  init(grant) := none;
  next(turn) := 1 - turn;
  next(grant) := case
    turn = 0 & req0 : g0;
    turn = 1 & req1 : g1;
    req0 & !req1    : g0;
    req1 & !req0    : g1;
    TRUE            : none;
  esac;
```

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">תכונות מעניינות</div>
<div dir="ltr" class="text-left">

```text
INVARSPEC (grant = g0 -> req0)
INVARSPEC (grant = g1 -> req1)
LTLSPEC G (req0 -> F (grant = g0 | !req0))
LTLSPEC G (req1 -> F (grant = g1 | !req1))
```

</div>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200 mt-3">
הדוגמה הזאת מדגימה איך להפריד בין <b>הסביבה</b> לבין <b>המערכת</b>:
הבקשות הן <span dir="ltr"><code>IVAR</code></span> ולכן נקבעות מבחוץ, בעוד הארביטר הוא המערכת שאנו רוצים לאמת.
</div>
</div>
</div>

---

# דוגמה 4: מונה מודולו-8 ו-BMC

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div dir="ltr" class="small-code">

```text
MODULE main
VAR
  y : 0..7;
ASSIGN
  init(y) := 0;
  next(y) := (y + 1) mod 8;

LTLSPEC G (y = 4 -> X y = 6)
LTLSPEC G F (y = 2)
```

<div class="flex justify-center mt-2 scale-85">
<TransitionSystemD3 
  :states="[
    { id: '0', text: '000', initial: true, x: 140, y: 30, initialDirection: 'top' },
    { id: '1', text: '001', x: 218, y: 62 },
    { id: '2', text: '010', x: 250, y: 140 },
    { id: '3', text: '011', x: 218, y: 218 },
    { id: '4', text: '100', x: 140, y: 250 },
    { id: '5', text: '101', x: 62, y: 218 },
    { id: '6', text: '110', x: 30, y: 140 },
    { id: '7', text: '111', x: 62, y: 62 }
  ]"
  :transitions="[
    { source: '0', target: '1' },
    { source: '1', target: '2' },
    { source: '2', target: '3' },
    { source: '3', target: '4' },
    { source: '4', target: '5' },
    { source: '5', target: '6' },
    { source: '6', target: '7' },
    { source: '7', target: '0' }
  ]"
  :width="280"
  :height="280"
  :auto="false"
/>
</div>

</div>

<div class="text-right text-[14px] leading-snug">
<div class="bg-purple-50 p-3 rounded border border-purple-200">
<div class="font-bold mb-2">למה זו דוגמה קלאסית?</div>
<ul class="list-disc pr-5 space-y-2">
<li>הנוסחה הראשונה שקרית, ולכן <span dir="ltr">BMC</span> ימצא דוגמה נגדית קצרה.</li>
<li>הנוסחה השנייה נכונה, אבל אם נחפש את שלילתה ב-<span dir="ltr">BMC</span> נקבל חשיבות לייצוג של <b>לולאה</b>.</li>
</ul>
</div>

<div class="bg-slate-50 p-3 rounded border border-slate-200 mt-3">
<div class="font-bold mb-2">אינטראקציה טיפוסית</div>
<div dir="ltr" class="small-code">

```sh
NuSMV -int modulo8.smv
NuSMV > go_bmc
NuSMV > check_ltlspec_bmc_onepb -k 9 -l 1
```

</div>
</div>
</div>
</div>

---

# איך לקרוא תוצאת כשל?

<div class="grid grid-cols-2 gap-4 mt-2 items-start">
<div class="text-right text-[14px] leading-snug bg-rose-50 p-3 rounded border border-rose-200">
<div class="font-bold mb-2">כאשר תכונה נכשלת</div>
<ul class="list-disc pr-5 space-y-2">
<li>הכלי מציג <b>trace</b> – רצף של מצבים.</li>
<li>ב-<span dir="ltr">CTL</span> זו עדות למסלול שמפריך את הנוסחה.</li>
<li>ב-<span dir="ltr">LTL</span> ייתכן שנראה גם מצבי עזר של הטאבלו.</li>
<li>ב-<span dir="ltr">BMC</span> ייתכן שתופיע גם אינדיקציה ל-<b>loop starts here</b>.</li>
</ul>
</div>

<div dir="ltr" class="small-code">

```text
-- specification G (y = 4 -> X y = 6) is false
-- as demonstrated by the following execution sequence
State 1.1: y = 0
State 1.2: y = 1
State 1.3: y = 2
State 1.4: y = 3
State 1.5: y = 4
State 1.6: y = 5
```

```text
bound:   0    1    2    3    4    5
state:  y=0  y=1  y=2  y=3  y=4  y=5
```

</div>
</div>

---

# מה הכלי יודע לאמת בפועל?

<div class="text-[14px] leading-snug">

<div class="grid grid-cols-2 gap-4 mt-2 text-right">
<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">בטיחות</div>
<ul class="list-disc pr-5 space-y-2">
<li>אי אפשר להיות בשני מצבים קריטיים בו זמנית.</li>
<li>שני כיווני רמזור לא ירוקים יחד.</li>
<li>לא מתקיים <span dir="ltr"><code>overflow</code></span>.</li>
<li>לא ניתן להגיע ל-<span dir="ltr"><code>error</code></span>.</li>
</ul>
</div>

<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">התקדמות</div>
<ul class="list-disc pr-5 space-y-2">
<li>בקשה תטופל בסוף.</li>
<li>תהליך רעב יקבל eventually שירות.</li>
<li>כל מצב "ממתין" יגיע בסוף למצב "משרת".</li>
<li>אות <span dir="ltr"><code>heartbeat</code></span> יופיע אינסוף פעמים.</li>
</ul>
</div>

<div class="bg-amber-50 p-3 rounded border border-amber-200">
<div class="font-bold mb-2">הישגיות</div>
<ul class="list-disc pr-5 space-y-2">
<li>קיים מסלול למצב תקלה?</li>
<li>קיים מסלול למצב מטרה?</li>
<li>אפשר להיתקע ב-<span dir="ltr"><code>wait</code></span> לנצח?</li>
</ul>
</div>

<div class="bg-purple-50 p-3 rounded border border-purple-200">
<div class="font-bold mb-2">כימות זמן מוגבל</div>
<ul class="list-disc pr-5 space-y-2">
<li>יש נגד-דוגמה באורך עד <span dir="ltr">k</span>?</li>
<li>יש מסלול לולאתי קצר שמפריך תכונת התקדמות?</li>
<li>האם אינווריאנט מוכח אינדוקטיבית?</li>
</ul>
</div>
</div>

</div>

---

# מערכות תגובתיות מעניינות מתוך האקו-סיסטם של NuSMV

<div class="text-[14px] leading-snug text-right">

<div class="bg-slate-50 p-3 rounded border border-slate-200">
בדוגמאות הרשמיות של הכלי מופיעות מערכות מגוונות מאוד, לא רק צעצועים:
</div>

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<ul class="list-disc pr-5 space-y-2">
<li><span dir="ltr">Alternating Bit Protocol</span></li>
<li><span dir="ltr">PCI Bus Protocol</span></li>
<li>בקר רובוטי</li>
<li><span dir="ltr">Production Cell</span></li>
</ul>
</div>

<div class="bg-green-50 p-3 rounded border border-green-200">
<ul class="list-disc pr-5 space-y-2">
<li><span dir="ltr">TCAS II</span> – מערכת למניעת התנגשות מטוסים</li>
<li>פרוטוקולי תקשורת</li>
<li>סמפור ותהליכים מקביליים</li>
<li>דגמים תעשייתיים עם קבצי <span dir="ltr">.ord</span> לייעול <span dir="ltr">BDD</span></li>
</ul>
</div>
</div>

<div class="mt-4 bg-amber-50 p-3 rounded border border-amber-200">
המסקנה: אותה שפה פשוטה יחסית יכולה לתאר גם דוגמאות לימודיות וגם מודלים אמיתיים למדי.
</div>

</div>

---

# טיפים למידול טוב ב-SMV

<div class="text-right text-[14px] leading-snug">

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="bg-green-50 p-3 rounded border border-green-200">
<div class="font-bold mb-2">כדאי לעשות</div>
<ul class="list-disc pr-5 space-y-2">
<li>לשמור על טיפוסים סופיים וקטנים ככל האפשר.</li>
<li>להפריד בין קלטי סביבה (<span dir="ltr"><code>IVAR</code></span>) לבין מצב פנימי.</li>
<li>להשתמש ב-<span dir="ltr"><code>DEFINE</code></span> לשמות עזר במקום להגדיל את מצב המערכת.</li>
<li>להתחיל ב-<span dir="ltr"><code>INVARSPEC</code></span> לפני שעוברים לתכונות התקדמות.</li>
<li>להריץ סימולציה לפני אימות מלא.</li>
</ul>
</div>

<div class="bg-rose-50 p-3 rounded border border-rose-200">
<div class="font-bold mb-2">כדאי להיזהר מ-</div>
<ul class="list-disc pr-5 space-y-2">
<li>אי-דטרמיניזם מיותר שמנפח את המודל.</li>
<li>הגינות חזקה מדי ש"מסתירה" באגים אמיתיים.</li>
<li>שימוש לא זהיר ב-<span dir="ltr"><code>TRANS</code></span> שיוצר deadlock.</li>
<li>בלבול בין "התכונה שקרית" לבין "המודל לא מייצג נכון את המערכת".</li>
</ul>
</div>
</div>

</div>

---

# סיכום

<div class="text-right text-[15px] leading-snug">

- <span dir="ltr">SMV</span> היא שפת מידול של <b>מכונות מצבים סופיות</b> עבור מערכות תגובתיות.
- <span dir="ltr">NuSMV</span> מוסיף סביבת עבודה פרקטית: סימולציה, אימות <span dir="ltr">CTL</span>, אימות <span dir="ltr">LTL</span> ו-<span dir="ltr">BMC</span>.
- החשיבה הנכונה היא תמיד:
  מהו המצב? מהו יחס המעבר? אילו הנחות סביבה? ואיזו תכונה באמת נרצה לבדוק?
- דוגמאות קטנות כמו רמזור, סמפור, ארביטר ומונה כבר מראות את רוב האתגרים האמיתיים:
  בטיחות, התקדמות, הגינות, ואבחון עקבות נגדיות.

<div class="mt-6 bg-slate-50 p-3 rounded border border-slate-200 text-[13px]">
מקורות רשמיים עיקריים: <span dir="ltr">NuSMV 2.7.0 article</span>, אתר הבית של
<span dir="ltr">NuSMV</span>, המדריך הרשמי והעמוד של הדוגמאות.
</div>

</div>

---

# מקורות רשמיים

<div class="text-right text-[14px] leading-snug">

<ul class="list-disc pr-5 space-y-3">
<li><a href="https://nusmv.fbk.eu/articles/270/" target="_blank"><span dir="ltr">NuSMV 2.7.0 article</span></a> – נקודת הכניסה והקישורים לעדכונים, מדריכים וקבצים.</li>
<li><a href="https://nusmv.fbk.eu/" target="_blank"><span dir="ltr">NuSMV home page</span></a> – תיאור הכלי, ארכיטקטורה, מהדורות וקישורים נוספים.</li>
<li><a href="https://nusmv.fbk.eu/downloads.html" target="_blank"><span dir="ltr">NuSMV downloads</span></a> – קבצי ההתקנה העדכניים, בדיקות checksum וחבילות לפי מערכת הפעלה.</li>
<li><a href="https://nusmv.fbk.eu/tutorials.html" target="_blank"><span dir="ltr">NuSMV tutorials</span></a> – מדריכי תרגול וקבצי הדרכה.</li>
<li><a href="https://nusmv.fbk.eu/user-manual.html" target="_blank"><span dir="ltr">NuSMV user manual</span></a> – תחביר מלא ותיעוד פקודות.</li>
<li><a href="https://nusmv.fbk.eu/examples.html" target="_blank"><span dir="ltr">NuSMV examples</span></a> – אוסף מודלים של פרוטוקולים, בקרים ומערכות תעשייתיות.</li>
</ul>

</div>

<style>
.slidev-layout h1 {
  margin-bottom: 0.35rem;
}

.slidev-layout h2 {
  margin-top: 0;
}

.bgu-logo {
  position: absolute;
}

.small-code :is(pre, code) {
  text-align: left !important;
}

.english-code-block {
  direction: ltr;
  text-align: left;
  white-space: pre;
  font-family: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.72rem;
  line-height: 1.25;
  margin: 0.75rem 0 0 0;
  padding: 0.5rem 0.6rem;
  border-radius: 0.4rem;
  background: #f5f5f5;
  overflow-x: auto;
}

.english-code-lines {
  direction: ltr;
  text-align: left !important;
  unicode-bidi: isolate;
  font-family: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.72rem;
  line-height: 1.4;
  width: 100%;
  margin-top: 0.75rem;
  white-space: nowrap;
}

.spec-snippet {
  direction: ltr;
  unicode-bidi: bidi-override;
  display: table;
  width: max-content;
  max-width: 100%;
  margin-top: 0.75rem;
  margin-left: 0;
  margin-right: auto;
  text-align: left !important;
  font-family: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.72rem;
  line-height: 1.4;
}

.spec-snippet-line {
  display: block;
  width: 100%;
  text-align: left !important;
  white-space: nowrap;
}

.symbolic-backward-note {
  margin-bottom: 0.5rem;
  font-size: 0.74rem;
  color: #475569;
}

.symbolic-backward-row {
  display: grid;
  grid-template-columns: 2.1rem 0.7rem 1fr;
  align-items: start;
  gap: 0.35rem;
  margin: 0.28rem 0;
  padding: 0.38rem 0.55rem;
  border: 1px solid #93c5fd;
  border-radius: 0.65rem;
  background: linear-gradient(180deg, #eff6ff 0%, #dbeafe 100%);
  font-size: 0.76rem;
}

.symbolic-backward-name {
  font-weight: 700;
}

.symbolic-backward-op {
  text-align: center;
}

.symbolic-backward-formula {
  white-space: normal;
  overflow-wrap: anywhere;
}
</style>
