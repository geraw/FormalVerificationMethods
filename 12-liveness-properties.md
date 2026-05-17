---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 12-liveness-properties
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## תכונות חַיּוּת
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תכונות חַיּוּת

## Liveness Properties

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">נגדיר תכונות חַיּוּת</div>

- תכונות שאינן פוסלות אף רישא סופית.
- תכונות שמבטאות התקדמות: “משהו טוב יקרה”.
- נלמד איך להוכיח שתכונה היא חַיּוּת, ואיך להפריך זאת.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">נחבר לבטיחות ולסְגוֹר</div>

- נראה שתכונת חַיּוּת ובטיחות יחד כמעט לא משאירות חופש.
- ננסח את משפט הפירוק.
- נבין איך כל תכונת זמן ליניארי מתפרקת לבטיחות ולחַיּוּת.
</div>
</div>

---

# האינטואיציה

<div class="grid grid-cols-2 gap-8 mt-7 text-right">
<div class="bg-red-50 border border-red-200 rounded p-4 min-h-[405px]">
<img src="/images/liveness-intuition-safety-comic.png" class="w-full h-[178px] object-cover rounded border border-red-100 mb-4" />
<div class="text-[27px] font-bold text-red-700 mb-3">בטיחות</div>
<div class="text-[22px] font-bold mb-3">“משהו רע לא יקרה”</div>
<div class="text-[18px] leading-relaxed">
אם הדבר הרע קרה, כבר אי אפשר לתקן אותו.
אפשר להצביע על רישא סופית שבה ההפרה כבר נחשפה.
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 min-h-[405px]">
<img src="/images/liveness-intuition-liveness-comic.png" class="w-full h-[178px] object-cover rounded border border-emerald-100 mb-4" />
<div class="text-[27px] font-bold text-emerald-700 mb-3">חַיּוּת</div>
<div class="text-[22px] font-bold mb-3">“משהו טוב יקרה בסופו של דבר”</div>
<div class="text-[18px] leading-relaxed">
אחרי כל רישא סופית עדיין יכול להיות שהדבר הטוב יקרה בהמשך.
לכן הפרה אמיתית מתגלה רק על ריצה אינסופית.
</div>
</div>
</div>

---

# הגדרה: תכונת חַיּוּת

<div class="mt-8 text-right text-[24px] leading-relaxed">

תכונת זמן ליניארי <KatexInline math="P" /> מעל <KatexInline math="AP" /> היא <span class="font-bold">תכונת חַיּוּת</span> אם:

</div>

<div class="mt-8 text-center text-[33px]" dir="ltr">
<KatexInline display math="\operatorname{pref}(P) = (2^{AP})^*" />
</div>

<div class="mt-8 text-right text-[22px] leading-relaxed">

כלומר, לכל מילה סופית <KatexInline math="\rho \in (2^{AP})^*" /> קיימת מילה אינסופית
<KatexInline math="\sigma \in (2^{AP})^\omega" /> כך ש־<KatexInline math="\rho \prec \sigma" />
וגם <KatexInline math="\sigma \in P" />.

</div>

<div class="mt-5 bg-blue-50 border border-blue-200 rounded p-4 text-center text-[22px] leading-relaxed">
תכונת חַיּוּת אינה פוסלת אף רישא סופית.
</div>

---

# דרך עבודה עם ההגדרה

<div class="grid grid-cols-2 gap-7 mt-8 text-right">
<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-[24px] mb-4 text-emerald-700">כדי להוכיח חַיּוּת</div>
<div class="text-[20px] leading-relaxed">
לוקחים רישא סופית שרירותית <KatexInline math="\rho" /> ובונים לה המשך אינסופי
<KatexInline math="\sigma" /> כך שהמילה <KatexInline math="\rho\sigma" /> תקיים את <KatexInline math="P" />.
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold text-[24px] mb-4 text-red-700">כדי להפריך חַיּוּת</div>
<div class="text-[20px] leading-relaxed">
מספיק למצוא רישא אחת <KatexInline math="\rho" /> שאי אפשר להציל:
לכל המשך אינסופי <KatexInline math="\sigma" />, מתקיים <KatexInline math="\rho\sigma \notin P" />.
</div>
</div>
</div>

<div class="mt-8 text-center text-[26px]" dir="ltr">
<KatexInline math="P \text{ is live} \iff \forall \rho \in (2^{AP})^*\ \left(\exists \sigma \in (2^{AP})^\omega\ \left(\rho\sigma \in P\right)\right)" />
</div>

---

# תרשים רצף: איך מוכיחים חַיּוּת?

<div class="relative mx-auto mt-2 h-[440px] w-[720px]" dir="ltr">
  <svg class="absolute inset-0 h-full w-full overflow-visible" viewBox="0 0 720 440" aria-hidden="true">
    <defs>
      <marker id="liveness-seq-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 Z" fill="#8b5a44" />
      </marker>
    </defs>
    <line x1="170" y1="96" x2="170" y2="382" stroke="#8b5a44" stroke-width="3" stroke-dasharray="10 10" />
    <line x1="550" y1="96" x2="550" y2="382" stroke="#8b5a44" stroke-width="3" stroke-dasharray="10 10" />
    <path d="M 170 175 L 550 175" fill="none" stroke="#8b5a44" stroke-width="4" stroke-linecap="round" marker-end="url(#liveness-seq-arrow)" />
    <path d="M 550 315 L 170 315" fill="none" stroke="#8b5a44" stroke-width="4" stroke-linecap="round" marker-end="url(#liveness-seq-arrow)" />
  </svg>

  <div class="absolute left-[2%] top-[0%] w-[250px] text-center text-[18px] leading-snug">
    מתמטיקאי שמוכיח<br/>ש־<KatexInline math="P" /> אינה חַיּוּת
  </div>
  <div class="absolute right-[2%] top-[0%] w-[250px] text-center text-[18px] leading-snug">
    מתמטיקאי שמוכיח<br/>ש־<KatexInline math="P" /> היא תכונת חַיּוּת
  </div>

  <div class="absolute left-1/2 top-[28%] -translate-x-1/2 text-center text-[22px] text-[#8b5a44]" dir="ltr">
    <KatexInline math="\rho \in (2^{AP})^*" />
  </div>
  <div class="absolute left-1/2 top-[60%] -translate-x-1/2 text-center text-[22px] text-[#8b5a44] whitespace-nowrap" dir="ltr">
    <KatexInline math="\rho\sigma \in P\ \text{ for some }\sigma \in (2^{AP})^\omega" />
  </div>
</div>

<div class="text-center text-[24px] -mt-12">
מראים שלכל רישא שהיריב בוחר, יש המשך שמציל אותה ומכניס את המילה ל־<KatexInline math="P" />.
</div>

---

# דוגמאות לתכונות חַיּוּת

<div class="mt-7 text-right text-[21px] leading-relaxed">

<span class="font-bold">דוגמה 1:</span>
מתישהו בעתיד יופיע <KatexInline math="p" />:

</div>

<div class="text-center text-[28px] mt-3" dir="ltr">
<KatexInline math="P = \{\sigma \mid \exists j \ge 0\ \left(\sigma[j] \models p\right)\}" />
</div>

<div class="mt-7 text-right text-[21px] leading-relaxed">

<span class="font-bold">דוגמה 2:</span>
<KatexInline math="p" /> יופיע אינסוף פעמים:

</div>

<div class="text-center text-[28px] mt-3" dir="ltr">
<KatexInline math="P = \{\sigma \mid \forall i \ge 0\ \left(\exists j > i\ \left(\sigma[j] \models p\right)\right)\}" />
</div>

<div class="mt-7 text-right text-[21px] leading-relaxed">

<span class="font-bold">דוגמה 3:</span>
מתישהו, מכאן ואילך, כל מופע של <KatexInline math="p" /> ילווה מיד ב־<KatexInline math="q" />:

</div>

<div class="text-center text-[25px] mt-3" dir="ltr">
<KatexInline math="P = \{\sigma \mid \exists i > 0\ \left(\forall j > i\ \left(\sigma[j] \models p \Rightarrow \sigma[j+1] \models q\right)\right)\}" />
</div>

---

# למה הדוגמאות הן חַיּוּת?

<div class="mt-8 text-right text-[23px] leading-relaxed">

בכל אחת מהדוגמאות, אחרי כל רישא סופית <KatexInline math="\rho" /> אפשר לבחור המשך שמתקן את העתיד:

</div>

<div class="grid grid-cols-3 gap-5 mt-7 text-right text-[18px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">מתישהו <KatexInline math="p" /></div>
נמשיך ב־<KatexInline math="\{p\}" /> פעם אחת, ואחר כך כרצוננו.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">אינסוף פעמים <KatexInline math="p" /></div>
נמשיך ב־<KatexInline math="\{p\}^\omega" />.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">לבסוף <KatexInline math="p \Rightarrow \bigcirc q" /></div>
נמשיך ב־<KatexInline math="\{\}^\omega" />, ולכן התנאי מתקיים באופן ריק.
</div>
</div>

<div class="mt-7 bg-emerald-50 border border-emerald-200 rounded p-4 text-[21px] leading-relaxed">
הרישא לא חייבת להיות “טובה”. כל עוד העתיד יכול להציל אותה, אין רישא רעה.
</div>

---

# איך מראים שתכונה אינה חַיּוּת?

<div class="mt-7 text-right text-[21px] leading-relaxed">

נמצא רישא סופית שממנה כבר אי אפשר להגיע למילה שמקיימת את התכונה.

</div>

<div class="mt-6 bg-red-50 border border-red-200 rounded p-4 text-right text-[21px] leading-relaxed">
<span class="font-bold">דוגמה:</span>
בכל מקום זוגי חיובי צריך להתקיים <KatexInline math="p" />:
</div>

<div class="text-center text-[28px] mt-5" dir="ltr">
<KatexInline math="P = \{\sigma \mid \forall i > 0\ \left(\sigma[2i] \models p\right)\}" />
</div>

<div class="mt-7 text-right text-[21px] leading-relaxed">

הרישא
<span dir="ltr"><KatexInline math="\rho = \{\}\ \{\}\ \{\}" /></span>
כבר קובעת שבמקום <KatexInline math="2" /> אין <KatexInline math="p" />.
לכן לכל המשך <KatexInline math="\sigma" /> מתקיים <KatexInline math="\rho\sigma \notin P" />.

</div>

<div class="mt-7 text-[24px] text-red-700 font-bold">
רישא אחת בלתי ניתנת לתיקון מספיקה כדי לשלול חַיּוּת.
</div>

---

# חַיּוּת באלגוריתמי מניעה הדדית

<div class="mt-7 text-right text-[22px] leading-relaxed">

עבור שני תהליכים, עם פסוקים אטומיים
<KatexInline math="wait_1, crit_1, wait_2, crit_2" />,
תכונות חַיּוּת טבעיות הן:

</div>

<div class="grid grid-cols-3 gap-5 mt-7 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">כניסה לפחות פעם אחת</div>
כל תהליך ייכנס בסוף לקטע הקריטי.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">כניסה אינסוף פעמים</div>
כל תהליך ייכנס לקטע הקריטי שוב ושוב.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-2">חופש מהרעבה</div>
אם תהליך מחכה, הוא ייכנס בסוף.
</div>
</div>

<div class="mt-8 text-center text-[25px]" dir="ltr">
<KatexInline math="\forall i \ge 0\ \left(\sigma[i] \models wait_k \Rightarrow \exists j \ge i\ \left(\sigma[j] \models crit_k\right)\right)" />
</div>

---

# המשמעות המעשית

<div class="grid grid-cols-[1.1fr_0.9fr] gap-7 mt-8 items-center text-right">
<div class="text-[22px] leading-relaxed">

במערכת אמיתית קשה “לראות” הפרה של חַיּוּת, כי ההפרה עשויה להתברר רק אחרי זמן אינסופי.

לכן חַיּוּת היא לעיתים קרובות קירוב נקי לתכונה המעשית שרצינו:

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-5">
רצינו להוכיח שהתוכנית תסתיים בתוך 100 שנה.
בפועל מוכיחים את התנאי החלש יותר: התוכנית תסתיים בסופו של דבר.
</div>

</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-[22px] leading-relaxed">
<img src="/images/leslie-lamport-cutout.png" class="h-[170px] mx-auto -mt-3 mb-2 object-contain" />
<div class="font-bold text-[26px] mb-3">Leslie Lamport</div>
חַיּוּת לא נותנת חסם זמן, אבל היא שוללת לולאות אינסופיות שמונעות התקדמות.
</div>
</div>

---

# גם בטיחות וגם חַיּוּת?

<div class="mt-8 text-right text-[24px] leading-relaxed">

משפט:
אם <KatexInline math="P" /> היא גם תכונת בטיחות וגם תכונת חַיּוּת מעל <KatexInline math="AP" />, אז:

</div>

<div class="mt-8 text-center text-[34px]" dir="ltr">
<KatexInline display math="P = (2^{AP})^\omega" />
</div>

<div class="mt-8 text-right text-[22px] leading-relaxed">

כלומר, התכונה היחידה שהיא גם בטיחות וגם חַיּוּת היא התכונה הטריוויאלית שמקבלת כל התנהגות.

</div>

<div class="mt-8 grid grid-cols-2 gap-6 text-[20px]">
<div class="bg-red-50 border border-red-200 rounded p-4">
בטיחות אומרת: אם משהו אסור, יש רישא שחושפת זאת.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
חַיּוּת אומרת: אין אף רישא שאסור להתחיל ממנו.
</div>
</div>

---

# הוכחת המשפט

<div class="mt-8 text-right text-[23px] leading-relaxed">

אם <KatexInline math="P" /> היא תכונת חַיּוּת אז:

</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline math="\operatorname{pref}(P) = (2^{AP})^*" />
</div>

<div class="mt-7 text-right text-[23px] leading-relaxed">

לכן לכל מילה אינסופית, כל הרישות שלה הן רישות של מילים ב־<KatexInline math="P" />.
כלומר:

</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline math="\operatorname{closure}(P) = (2^{AP})^\omega" />
</div>

<div class="mt-7 text-right text-[23px] leading-relaxed">

אם <KatexInline math="P" /> היא גם תכונת בטיחות, אז מההרצאה הקודמת: <KatexInline math="P = \operatorname{closure}(P)" />.

ולכן <KatexInline math="P = (2^{AP})^\omega" />.

</div>

---

# תכונה שאינה בטיחות ואינה חַיּוּת

<div class="mt-8 text-right text-[23px] leading-relaxed">

התכונה:

</div>

<div class="mt-5 bg-slate-50 border border-slate-200 rounded p-5 text-[26px] leading-relaxed">
“המכונה נותנת בירה אינסוף פעמים, לאחר שבהתחלה נתנה סודה שלוש פעמים ברצף”
</div>

<div class="grid grid-cols-2 gap-6 mt-7 text-right text-[20px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">רכיב חַיּוּת</div>
דורשים שבירה תופיע אינסוף פעמים.
אי אפשר להכריע זאת לפי רישא סופית.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">רכיב בטיחות</div>
שלושת המשקאות הראשונים חייבים להיות סודה.
אם אחד מהם בירה, יש רישא רעה.
</div>
</div>

<div class="mt-7 text-[24px] font-bold">
התכונה היא חיתוך של דרישת בטיחות ודרישת חַיּוּת.
</div>

---

# בטיחות מול חַיּוּת

<div class="mt-8 text-right text-[25px] leading-relaxed">

שתי שאלות טבעיות:

</div>

<div class="grid grid-cols-2 gap-7 mt-8 text-[22px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">האם בטיחות וחַיּוּת שונות?</div>
כן. החיתוך שלהן הוא רק <KatexInline math="(2^{AP})^\omega" />.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">האם כל תכונה היא בטיחות או חַיּוּת?</div>
לא. יש תכונות שיש להן גם רכיב בטיחות וגם רכיב חַיּוּת.
</div>
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-[23px] leading-relaxed">
אבל כל תכונת זמן ליניארי ניתנת לכתיבה כחיתוך של תכונת בטיחות ותכונת חַיּוּת.
</div>

---

# משפט הפירוק

<div class="mt-8 text-right text-[24px] leading-relaxed">

לכל תכונת זמן ליניארי <KatexInline math="P" /> מעל <KatexInline math="AP" />
קיימות תכונת בטיחות <KatexInline math="P_{safe}" /> ותכונת חַיּוּת <KatexInline math="P_{live}" /> כך ש:

</div>

<div class="mt-8 text-center text-[34px]" dir="ltr">
<KatexInline display math="P = P_{safe} \cap P_{live}" />
</div>

<div class="grid grid-cols-2 gap-6 mt-8 text-[22px] text-center">
<div class="bg-emerald-50 border border-emerald-200 rounded p-4 min-h-[78px] flex items-center justify-center" dir="ltr">
<KatexInline math="P_{live} = P \cup \left((2^{AP})^\omega \setminus \operatorname{closure}(P)\right)" />
</div>
<div class="bg-red-50 border border-red-200 rounded p-4 min-h-[78px] flex items-center justify-center" dir="ltr">
<KatexInline math="P_{safe} = \operatorname{closure}(P)" />
</div>
</div>

---

# איור הפירוק

<div class="relative mt-4 h-[390px]" dir="ltr">
  <svg class="absolute inset-0 w-full h-full" viewBox="0 0 900 390" aria-hidden="true">
    <defs>
      <pattern id="decomp-vertical" width="8" height="8" patternUnits="userSpaceOnUse">
        <path d="M 2 0 V 8" stroke="#334155" stroke-width="1.2" />
      </pattern>
      <pattern id="decomp-horizontal" width="8" height="8" patternUnits="userSpaceOnUse">
        <path d="M 0 2 H 8" stroke="#475569" stroke-width="1.2" />
      </pattern>
      <marker id="decomp-green-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 Z" fill="#16a34a" />
      </marker>
    </defs>
    <ellipse cx="420" cy="185" rx="345" ry="155" fill="#f8fafc" stroke="#111827" stroke-width="2.5" />
    <ellipse cx="420" cy="185" rx="245" ry="105" fill="#f8fafc" stroke="#111827" stroke-width="2.5" />
    <ellipse cx="420" cy="185" rx="125" ry="54" fill="#f8fafc" stroke="#111827" stroke-width="2.5" />
    <g v-click>
      <ellipse cx="420" cy="185" rx="345" ry="155" fill="url(#decomp-vertical)" />
      <ellipse cx="420" cy="185" rx="245" ry="105" fill="#f8fafc" />
      <ellipse cx="420" cy="185" rx="125" ry="54" fill="url(#decomp-vertical)" />
      <ellipse cx="420" cy="185" rx="345" ry="155" fill="none" stroke="#111827" stroke-width="2.5" />
      <ellipse cx="420" cy="185" rx="245" ry="105" fill="none" stroke="#111827" stroke-width="2.5" />
      <ellipse cx="420" cy="185" rx="125" ry="54" fill="none" stroke="#111827" stroke-width="2.5" />
    </g>
    <g v-click>
      <ellipse cx="420" cy="185" rx="245" ry="105" fill="url(#decomp-horizontal)" />
      <ellipse cx="420" cy="185" rx="245" ry="105" fill="none" stroke="#111827" stroke-width="2.5" />
      <ellipse cx="420" cy="185" rx="125" ry="54" fill="none" stroke="#111827" stroke-width="2.5" />
    </g>
    <path d="M 790 305 C 770 290, 748 275, 700 260" fill="none" stroke="#16a34a" stroke-width="3" stroke-linecap="round" marker-end="url(#decomp-green-arrow)" />
  </svg>
  <div class="absolute left-[44%] top-[10%] text-[25px] text-blue-700"><KatexInline math="(2^{AP})^\omega" /></div>
  <div class="absolute left-[37%] top-[24%] text-[28px] text-red-700"><KatexInline math="\operatorname{closure}(P)" /></div>
  <div class="absolute left-[45%] top-[45%] text-[30px] text-purple-700"><KatexInline math="P" /></div>
  <div class="absolute left-[85%] top-[82%] text-[20px] text-emerald-700"><KatexInline math="(2^{AP})^\omega \setminus \operatorname{closure}(P)" /></div>
</div>

<div class="text-center text-[24px] -mt-5">
<KatexInline math="P_{live}" /> כולל את <KatexInline math="P" /> ואת כל מה שמחוץ ל־<KatexInline math="\operatorname{closure}(P)" />.
<br>
<KatexInline math="P_{safe}" /> הוא בדיוק <KatexInline math="\operatorname{closure}(P)" />.
</div>

---

# למה <KatexInline math="P_{live}" /> היא תכונת חַיּוּת?

<div class="mt-7 text-right text-[22px] leading-relaxed">

צריך להראות שלכל רישא סופית <KatexInline math="\rho" /> יש המשך שנמצא ב־<KatexInline math="P_{live}" />.

</div>

<div class="grid grid-cols-2 gap-6 mt-8 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-3">מקרה א': <KatexInline math="\rho \in \operatorname{pref}(P)" /></div>
קיימת מילה <KatexInline math="\rho\sigma \in P" />.
מכיוון ש־<KatexInline math="P \subseteq P_{live}" />,
קיבלנו המשך טוב.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-3">מקרה ב': <KatexInline math="\rho \notin \operatorname{pref}(P)" /></div>
כל מילה שמתחילה ב־<KatexInline math="\rho" /> איננה בסְגוֹר של <KatexInline math="P" />.
למשל <KatexInline math="\rho\{\}^\omega \in (2^{AP})^\omega \setminus \operatorname{closure}(P)" />.
</div>
</div>

<div class="mt-8 text-center text-[27px]" dir="ltr">
<KatexInline math="\operatorname{pref}(P_{live}) = (2^{AP})^*" />
</div>

---

# דוגמה: הרבה <KatexInline math="a" /> ואז <KatexInline math="a,b" />

<div class="mt-7 text-right text-[22px] leading-relaxed">

ניקח <KatexInline math="AP=\{a,b\}" /> ואת התכונה:

</div>

<div class="mt-5 text-center text-[26px]" dir="ltr">
<KatexInline math="P = \{a\}^* \cdot \{a,b\} \cdot (2^{AP})^\omega" />
</div>

<div class="mt-7 text-right text-[21px] leading-relaxed">

כלומר, בהתחלה מופיע <KatexInline math="a" /> בלבד מספר סופי של פעמים,
ואז מופיע מצב שבו גם <KatexInline math="a" /> וגם <KatexInline math="b" /> נכונים.

</div>

<div class="mt-7 text-center text-[26px]" dir="ltr">
<KatexInline math="\operatorname{closure}(P) = P \cup \{a\}^\omega" />
</div>

<div class="mt-7 bg-slate-50 border border-slate-200 rounded p-4 text-[21px] leading-relaxed">
הריצה <KatexInline math="\{a\}^\omega" /> נמצאת בסְגוֹר: כל רישא שלה עדיין יכולה להמשיך ל־<KatexInline math="P" />,
אבל היא עצמה איננה ב־<KatexInline math="P" />.
</div>

---

# דוגמה: Until

<div class="mt-7 text-right text-[22px] leading-relaxed">

יהיו <KatexInline math="\Phi_1" /> ו־<KatexInline math="\Phi_2" /> פסוקי מצב. התכונה:

</div>

<div class="mt-5 text-center text-[24px]" dir="ltr">
<KatexInline math="P = \{\sigma \mid \exists i \ge 0\ \left(\sigma[i] \models \Phi_2 \land \forall 0 \le j \le i\ \left(\sigma[j] \models \Phi_1\right)\right)\}" />
</div>

<div class="mt-7 text-[28px] font-bold text-blue-700">
<KatexInline math="\Phi_1\ \mathsf{until}\ \Phi_2" />
</div>

<div class="mt-7 text-right text-[21px] leading-relaxed">

גם כאן יש רכיב בטיחות ורכיב חַיּוּת:

</div>

<div class="mt-5 text-center text-[25px]" dir="ltr">
<KatexInline math="\operatorname{closure}(P) = P \cup \{\sigma \mid \forall i \ge 0\ \left(\sigma[i] \models \Phi_1\right)\}" />
</div>

<div class="mt-7 bg-amber-50 border border-amber-200 rounded p-4 text-[20px] leading-relaxed">
הריצה שבה <KatexInline math="\Phi_1" /> מתקיים תמיד ו־<KatexInline math="\Phi_2" /> לעולם לא מגיע נמצאת בסְגוֹר,
אבל לא בתכונה עצמה.
</div>

---

# משפט הפירוק החזק

<div class="mt-7 text-right text-[22px] leading-relaxed">

אם <KatexInline math="P = P_{safe} \cap P_{live}" />,
כאשר <KatexInline math="P_{safe}" /> היא בטיחות ו־<KatexInline math="P_{live}" /> היא חַיּוּת, אז:

</div>

<div class="mt-7 text-center text-[30px]" dir="ltr">
<KatexInline display math=" \operatorname{closure}(P) \subseteq P_{safe}" />
</div>

<div class="mt-5 text-center text-[30px]" dir="ltr">
<KatexInline display math="P_{live} \subseteq P \cup \left((2^{AP})^\omega \setminus \operatorname{closure}(P)\right)" />
</div>

<div class="grid grid-cols-2 gap-6 mt-7 text-[20px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
<KatexInline math="\operatorname{closure}(P)" /> היא תכונת הבטיחות החזקה ביותר שאפשר לבחור בפירוק.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<KatexInline math="P \cup ((2^{AP})^\omega \setminus \operatorname{closure}(P))" />
היא תכונת החַיּוּת החלשה ביותר שאפשר לבחור.
</div>
</div>

---

# סיווג תכונות זמן ליניארי

<div class="relative mt-1 h-[455px]" dir="ltr">
  <div class="absolute left-[2%] top-[28%] h-[240px] w-[470px] rounded-[50%] border-2 border-[#6f6366] bg-[radial-gradient(circle_at_45%_35%,#b8a5a8_0%,#88777b_70%,#6f6366_100%)] shadow-xl z-0"></div>
  <div class="absolute left-[23%] top-[38%] h-[130px] w-[280px] rounded-[50%] border-2 border-[#776b6e] bg-[radial-gradient(circle_at_45%_35%,#c9babd_0%,#7d7073_100%)] shadow-xl z-10"></div>
  <div class="absolute left-[40%] top-[45%] h-[68px] w-[136px] rounded-[50%] border-2 border-[#776b6e] bg-[radial-gradient(circle_at_45%_35%,#c9babd_0%,#7d7073_100%)] shadow-xl z-20"></div>
  <div class="absolute left-[55%] top-[29%] h-[240px] w-[445px] rounded-[50%] border-2 border-[#6f6366] bg-[radial-gradient(circle_at_45%_35%,#b8a5a8_0%,#88777b_70%,#6f6366_100%)] shadow-xl z-0"></div>

  <div class="absolute left-[10%] top-[50%] text-[26px] text-white z-30">בטיחות</div>
  <div class="absolute left-[29%] top-[45%] text-[25px] text-white z-30">בטיחות  <br> רגולרית</div>
  <div class="absolute left-[45%] top-[50%] text-[24px] text-white z-30">שמורה</div>
  <div class="absolute left-[73%] top-[50%] text-[26px] text-white z-30">חַיּוּת</div>

  <div class="absolute left-[12.6%] top-[33.2%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[38%] top-[42%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[43.2%] top-[53%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[55%] top-[53%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[74.5%] top-[34.5%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[76%] top-[85.5%] h-[12px] w-[12px] rounded-full bg-blue-700 shadow-md z-40"></div>

  <svg class="absolute inset-0 w-full h-full z-30 pointer-events-none" viewBox="0 0 900 455" aria-hidden="true">
    <defs>
      <marker id="class-red-arrow-html" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 Z" fill="#ef4444" />
      </marker>
      <marker id="class-blue-arrow-html" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 Z" fill="#2563eb" />
      </marker>
    </defs>
    <path d="M 145 40 L 120 144" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 360 79 L 348 185" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 401 375 L 396 255" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 496 333 L 500 250" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 700 72 L 678 150" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <!-- <path d="M 610 407 L 690 392" stroke="#2563eb" stroke-width="2.5" marker-end="url(#class-blue-arrow-html)" /> -->
  </svg>

  <div class="absolute left-[0%] top-[0%] text-[21px] text-red-600" dir="ltr">
    <KatexInline math="P=\{\sigma \mid \operatorname{pref}(\sigma)\cap BadPref=\emptyset\}" />
  </div>
  <div class="absolute left-[30%] top-[12%] text-[22px] text-red-600" dir="rtl">
    רגולרית <KatexInline math="BadPref" />
  </div>
  <div class="absolute left-[63%] top-[7%] text-[22px] text-red-600" dir="ltr">
    <KatexInline math="\operatorname{pref}(P)=(2^{AP})^*" />
  </div>
  <div class="absolute left-[28%] top-[83%] text-[21px] text-red-600" dir="ltr">
    <KatexInline math="P=\{\sigma \mid \forall i\ \left(\sigma[i]\models\Phi\right)\}" />
  </div>
  <div class="absolute left-[47%] top-[74%] text-[21px] text-red-600" dir="ltr">
    <KatexInline math="P=(2^{AP})^\omega" />
  </div>
  <div class="absolute left-[74%] top-[90%] text-[21px] text-blue-700" dir="ltr">
    <KatexInline math="P=P_{live}\cap P_{safe}" />
  </div>
</div>

---

# סיכום

<div class="mt-8 text-right text-[22px] leading-relaxed">

- תכונת חַיּוּת היא תכונת זמן ליניארי שאינה פוסלת אף רישא סופית:
  <KatexInline math="\operatorname{pref}(P) = (2^{AP})^*" />.
- בטיחות מזהה הפרות בזמן סופי; חַיּוּת דורשת התקדמות בעתיד האינסופי.
- התכונה היחידה שהיא גם בטיחות וגם חַיּוּת היא
  <KatexInline math="(2^{AP})^\omega" />.
- כל תכונת זמן ליניארי מתפרקת כך:
  <KatexInline math="P = \operatorname{closure}(P) \cap \left(P \cup ((2^{AP})^\omega \setminus \operatorname{closure}(P))\right)" />.
- הסְגוֹר מספק את רכיב הבטיחות; המשלים של הסְגוֹר, יחד עם <KatexInline math="P" />, מספק את רכיב החַיּוּת.

</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-[24px]">
השיעור הבא: הוגנות, כלומר אילו הנחות על התזמון נדרשות כדי שחַיּוּת תהיה סבירה במערכות מקביליות.
</div>
