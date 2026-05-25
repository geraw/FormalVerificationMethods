---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 13-fairness
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## הוֹגְנוּת
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# הוֹגְנוּת

## Fairness

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# תזכורת: סיכום סיווג תכונות זמן ליניארי

<div class="relative mt-1 h-[455px]" dir="ltr">
  <div class="absolute left-[2%] top-[28%] h-[240px] w-[470px] rounded-[50%] border-2 border-[#6f6366] bg-[radial-gradient(circle_at_45%_35%,#b8a5a8_0%,#88777b_70%,#6f6366_100%)] shadow-xl z-0"></div>
  <div class="absolute left-[23%] top-[38%] h-[130px] w-[280px] rounded-[50%] border-2 border-[#776b6e] bg-[radial-gradient(circle_at_45%_35%,#c9babd_0%,#7d7073_100%)] shadow-xl z-10"></div>
  <div class="absolute left-[40%] top-[45%] h-[68px] w-[136px] rounded-[50%] border-2 border-[#776b6e] bg-[radial-gradient(circle_at_45%_35%,#c9babd_0%,#7d7073_100%)] shadow-xl z-20"></div>
  <div class="absolute left-[55%] top-[29%] h-[240px] w-[445px] rounded-[50%] border-2 border-[#6f6366] bg-[radial-gradient(circle_at_45%_35%,#b8a5a8_0%,#88777b_70%,#6f6366_100%)] shadow-xl z-0"></div>

  <div class="absolute left-[10%] top-[50%] text-[26px] text-white z-30">בטיחות</div>
  <div class="absolute left-[29%] top-[45%] text-[25px] text-white z-30">בטיחות  <br> רגולרית</div>
  <div class="absolute left-[45%] top-[50%] text-[24px] text-white z-30">שמורה</div>
  <div class="absolute left-[73%] top-[50%] text-[26px] text-white z-30">חַיּוּת</div>

  <div class="absolute left-[18.8%] top-[45%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[38%] top-[42%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[43.2%] top-[53%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[55%] top-[53%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
  <div class="absolute left-[74.5%] top-[43%] h-[10px] w-[10px] rounded-full bg-red-600 shadow-md z-40"></div>
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
    <path d="M 145 40 L 171 205" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 360 79 L 348 185" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 401 375 L 396 255" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 496 333 L 500 250" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <path d="M 700 72 L 678 196" stroke="#ef4444" stroke-width="2" marker-end="url(#class-red-arrow-html)" />
    <!-- <path d="M 610 407 L 690 392" stroke="#2563eb" stroke-width="2.5" marker-end="url(#class-blue-arrow-html)" /> -->
  </svg>

  <div class="absolute left-[0%] top-[0%] text-[21px] text-red-600" dir="ltr">
    <KatexInline math="P=\{\sigma \mid \operatorname{pref}(\sigma)\cap BadPref=\emptyset\}" />
  </div>
  <div class="absolute left-[30%] top-[12%] text-[22px] text-red-600" dir="rtl">
    <KatexInline math="BadPref" /> רגולרית
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

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">למה צריך הוֹגְנוּת?</div>

- נבין מדוע תכונות חַיּוּת רבות אינן ניתנות להוכחה בלי הנחות נוספות.
- נראה כיצד אי-דטרמיניזם במודל עלול לייצר ריצות לא מציאותיות.
- נבחין בין תכונה שרוצים להוכיח לבין הנחה שמגבילה את המודל.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">מה נלמד להגדיר?</div>

- אילוצי הוֹגְנוּת בלתי מותנית, חזקה וחלשה.
- הנחת הוֹגְנוּת כשלישייה של קבוצות פעולות.
- קיום תכונה תחת הנחות הוֹגְנוֹת.
- הקשר בין הוֹגְנוּת לתכונות בטיחות.
</div>
</div>

---

# למה צריך הוֹגְנוּת?

<img src="/lazy_scheduler_comic.png" class="absolute left-8 top-10 w-[160px] rounded-xl shadow-2xl border border-slate-200/85 transform -rotate-2 hover:rotate-0 hover:scale-105 transition-all duration-300 z-50" />

<div class="mt-7 text-right text-[23px] leading-relaxed">

במערכות מקביליות, תכונת חַיּוּת כמו "בסוף תהליך 2 ירוץ" אינה נובעת רק ממבנה התוכנית.
צריך גם לומר משהו על מנגנון השיבוץ.

</div>

<div class="grid grid-cols-[1.15fr_0.85fr] gap-6 mt-6 items-center">
<div class="bg-amber-50 border border-amber-200 rounded p-5 text-right text-[21px] leading-relaxed">
<p>
נניח שתהליך <KatexInline math="P_2"></KatexInline> מתחיל בפעולה <KatexInline math="x := 1"></KatexInline>, ושאף תהליך אחר אינו נוגע במשתנה <KatexInline math="x"></KatexInline>.
</p>

נרצה להוכיח שמנקודה מסוימת ואילך תמיד <KatexInline math="x=1" />:

<div class="mt-3 text-center" dir="ltr">
<KatexInline display math="P=\{\sigma\in(2^{AP})^\omega \mid \exists i\ge 0\ \left(\forall j>i\ \left(\sigma[j]\models x=1\right)\right)\}" />
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-5 text-right text-[21px] leading-relaxed">
אם המשבץ לעולם לא בוחר את <KatexInline math="P_2" />, התכונה נכשלת.
זו ריצה חוקית מבחינת מערכת המעברים, אבל לרוב אינה ריצה סבירה של מערכת אמיתית.
</div>
</div>

---

# דוגמה: שיבוץ לא הוגן

<div class="mt-7 text-right text-[23px] leading-relaxed">
שרת משרת תהליכים <KatexInline math="P_1,P_2,\ldots,P_n" /> לפי מדיניות קשיחה:
</div>

<div class="mt-6 mx-auto w-[82%] text-right text-[22px] leading-relaxed bg-slate-50 border border-slate-200 rounded p-5">

- אם התהליך הראשון צריך שירות, הוא מקבל.
- אחרת, אם התהליך השני צריך שירות, הוא מקבל.
- וכן הלאה.
- תהליך <KatexInline math="P_n" /> יקבל שירות רק אם אף אחד מהקודמים אינו צריך שירות.

</div>

<div class="mt-8 bg-red-50 border border-red-200 rounded p-5 text-[23px] leading-relaxed">
קשה להוכיח התקדמות במערכת שבה אפשר להתעלם מתהליך מסוים לנצח.
</div>

<img src="/unfair_scheduling_comic.png" class="absolute left-6 top-10 w-[230px] rounded-xl shadow-2xl border border-slate-200/85 transform -rotate-2 hover:rotate-0 hover:scale-105 transition-all duration-300 z-50" />

---

# הוֹגְנוּת היא חלק מהמודל

<img src="/fairness_filter_comic.png" class="absolute left-6 top-4 w-[130px] rounded-xl shadow-2xl border border-slate-200/80 transform rotate-2 hover:rotate-0 hover:scale-105 transition-all duration-300 z-50" />

<div class="grid grid-cols-2 gap-6 mt-8 text-right text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3">מה ההנחה אומרת?</div>
לא רוצים למדל את כל פרטי מנגנון הבחירה, אבל כן רוצים לפסול ריצות שבהן אפשרות סבירה נדחית לנצח.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-5">
<div class="font-bold text-amber-700 mb-3">מה חשוב לזכור?</div>
הנחת הוֹגְנוּת אינה תכונה שרוצים להוכיח על המערכת; היא מגבלה על קבוצת הריצות שנחשבות רלוונטיות.
</div>
</div>

<div class="mt-10 text-center text-[30px]" dir="ltr">
<KatexInline display math="\text{concurrency} = \text{interleaving} + \text{fairness}" />
</div>

---

# אי-דטרמיניזם כאבסטרקציה

<div class="mt-7 text-right text-[23px] leading-relaxed">
הוֹגְנוּת מופיעה כאשר אי-דטרמיניזם מייצג פרט שלא רצינו או לא יכולנו לקבע במודל:
</div>

<div class="grid grid-cols-3 gap-5 mt-7 text-right text-[19px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">שיבוץ תהליכים</div>
לא ידוע באיזה סדר מערכת ההפעלה תבחר תהליכים, אבל לא סביר שתהליך מוכן יורעב לנצח.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">קצבי רכיבים</div>
שני רכיבים רצים במהירויות שונות, אבל אין רכיב שרץ פי אינסוף מהר מהאחר.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">בחירה הסתברותית</div>
לפני שקבענו הסתברויות, נשתמש באי-דטרמיניזם, אך נרצה לפסול בחירה שמתעלמת לנצח מאפשרות בעלת הסתברות חיובית.
</div>
</div>

---

# דוגמת מניעה הדדית

<div class="grid grid-cols-[23.08fr_1.92fr] gap-0 mt-3 items-start">
<div class="text-right text-[15px] leading-relaxed">
נחזור לאלגוריתם מניעה הדדית מבוסס סמפור.

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-4">
<KatexInline math="y=0" /> מסמל שהמנעול תפוס.
<br>
<KatexInline math="y=1" /> מסמל שהמנעול פנוי.
</div>

<div class="mt-4 bg-red-50 border border-red-200 rounded p-4">
כבר ראינו שהמערכת יכולה להפר את מניעת ההרעבה: תהליך ממתין, ויש אינסוף הזדמנויות להיכנס, אבל הוא לא נכנס לעולם.
</div>
</div>

<div class="-mt-14 -mb-16 -translate-x-7 scale-[0.80]" dir="ltr">
<SemaphoreMutexTs :width="640" :height="430" highlight-starvation />
</div>
</div>

---

# הרעבה כריצה לא הוגנת

<div class="grid grid-cols-[0.82fr_1.18fr] gap-2 mt-2 items-start">
<div class="-mt-14 -mb-16 translate-x-2 scale-[0.80]" dir="ltr">
<SemaphoreMutexTs :width="640" :height="430" highlight-starvation highlight-enter2-opportunity />
</div>

<div class="text-right text-[18px] leading-relaxed">
נשאל שתי שאלות:

<div class="mt-4 bg-red-50 border border-red-200 rounded p-5">
האם הוגן שלתהליך 2 יהיו אינסוף אפשרויות להיכנס לקטע הקריטי, אבל הוא לא ייכנס לעולם?
</div>

<div class="mt-4 bg-amber-50 border border-amber-200 rounded p-5">
האם הוגן שיהיו אינסוף אפשרויות להיכנס לקטע הקריטי, אבל ייכנסו רק מספר סופי של פעמים?
</div>
</div>
</div>

---

# שלושה סוגי אילוצי הוֹגְנוּת

<div class="grid grid-cols-3 gap-5 mt-7 text-right text-[18px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-3">הוֹגְנוּת בלתי מותנית</div>
פעולה מתוך קבוצה <KatexInline math="A" /> מבוצעת אינסוף פעמים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-3">הוֹגְנוּת חזקה</div>
אם פעולה מתוך <KatexInline math="A" /> מאופשרת אינסוף פעמים, אז פעולה מתוך <KatexInline math="A" /> מתבצעת אינסוף פעמים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold text-amber-700 mb-3">הוֹגְנוּת חלשה</div>
אם פעולה מתוך <KatexInline math="A" /> מאופשרת ברצף מנקודה מסוימת, אז פעולה מתוך <KatexInline math="A" /> מתבצעת אינסוף פעמים.
</div>
</div>

<div class="mt-8 w-[68%] bg-slate-50 border border-slate-200 rounded p-5 text-[22px] text-right ml-auto">
ככל שהאילוץ חזק יותר, הוא פוסל יותר ריצות.
</div>

<img src="/three_fairness_types_comic.png" class="absolute left-6 bottom-4 w-[240px] rounded-xl shadow-2xl border border-slate-200/85 transform -rotate-1 hover:rotate-0 hover:scale-105 transition-all duration-300 z-50" />

---

# סימון פורמלי

<div class="mt-6 text-right text-[22px] leading-relaxed">
נתמקד בריצה אינסופית מסויימת של מערכת המעברים:
</div>

<div class="mt-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="\rho = s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} s_2 \xrightarrow{\alpha_3}\cdots" />
</div>

<div class="mt-6 text-right text-[22px] leading-relaxed">
עבור קבוצת פעולות <KatexInline math="A\subseteq Act" />, נסמן:
</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-[21px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr">
<KatexInline display math="\underset{\infty}{\exists} i\ \left(\alpha_i\in A\right)" />
<div class="text-right mt-2" dir="rtl">נבחרת פעולה מ-<KatexInline math="A" /> אינסוף פעמים.</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr">
<KatexInline display math="Post(s_i,A)\neq\emptyset" />
<div class="text-right mt-2" dir="rtl">במצב <KatexInline math="s_i" /> מאופשרת פעולה מ-<KatexInline math="A" />.</div>
</div>
</div>

---

# הגדרות: הוֹגְנוּת של ריצה ביחס לקבוצת פעולות

<div class="mt-3 text-right text-[20px] leading-relaxed">
ריצה <KatexInline math="\rho" /> היא:
</div>

<div class="mt-3 space-y-4 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<span class="font-bold text-blue-700">הוגנת ללא תנאי ביחס ל-<KatexInline math="A" /></span>
אם:
<span dir="ltr"><KatexInline math="\underset{\infty}{\exists} i\ \left(\alpha_i\in A\right)" /></span>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<span class="font-bold text-emerald-700">הוגנת חזק ביחס ל-<KatexInline math="A" /></span>
אם:
<span dir="ltr"><KatexInline math="\left(\underset{\infty}{\exists} i\ \left(Post(s_i,A)\neq\emptyset\right)\right)\Rightarrow\left(\underset{\infty}{\exists} i\ \left(\alpha_i\in A\right)\right)" /></span>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<span class="font-bold text-amber-700">הוגנת חלש ביחס ל-<KatexInline math="A" /></span>
אם:
<span dir="ltr"><KatexInline math="\left(\exists j\ \left(\forall i>j\ \left(Post(s_i,A)\neq\emptyset\right)\right)\right)\Rightarrow\left(\underset{\infty}{\exists} i\ \left(\alpha_i\in A\right)\right)" /></span>
</div>
</div>


<div class="bg-red-100 border border-red-200 mt-8 text-center text-[20px] leading-relaxed flex items-center justify-center gap-4">
<div>הוגנת ללא תנאי</div>
<div class="text-[20px]" dir="ltr"><KatexInline display math="\Leftarrow" /></div>
<div>הוגנת חזקה</div>
<div class="text-[20px]" dir="ltr"><KatexInline display math="\Leftarrow" /></div>
<div>הוגנת חלשה</div>
</div>


---

# איך בוחרים את סוג ההוֹגְנוּת?

<div class="grid grid-cols-2 gap-6 mt-8 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">הוֹגְנוּת חזקה</div>
מתאימה כאשר פעולה יכולה להיות מאופשרת לסירוגין. אם יש אינסוף הזדמנויות לבצע אותה, לא סביר לדלג עליה לנצח.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-5">
<div class="font-bold text-amber-700 mb-3">הוֹגְנוּת חלשה</div>
מספיקה כאשר פעולה שנשארת מאופשרת לאורך זמן אמורה להתבצע בסוף.
</div>
</div>

<div class="grid grid-cols-[1fr_180px] gap-6 mt-8 items-center">
<div class="bg-red-50 border border-red-200 rounded p-5 text-[21px] leading-relaxed">
אילוץ חזק מדי עלול לפסול התנהגויות אמיתיות; אילוץ חלש מדי עלול להשאיר דוגמאות נגדיות לא מציאותיות.
</div>

<div>
<img src="/pregnancy_test_fairness.png" class="w-full rounded-lg shadow-md" alt="Pregnancy test illustration" />
</div>
</div>

---

# הנחת הוֹגְנוּת

<div class="mt-4 text-right text-[20px] leading-relaxed">
הנחת הוֹגְנוּת עבור קבוצת פעולות <KatexInline math="Act" /> היא שלישייה:
</div>

<div class="mt-3 text-center text-[28px]" dir="ltr">
<KatexInline display math="\mathcal{F}=\langle\mathcal{F}_{uncond},\mathcal{F}_{strong},\mathcal{F}_{weak}\rangle  \subseteq  2^{Act} \times 2^{Act} \times 2^{Act}" /> 
</div>

<div class="mt-4 text-right text-[19px] leading-relaxed">
כלומר: כל רכיב הוא אוסף של קבוצות פעולות
</div>

נגד
<div class="mt-0 bg-slate-50 border border-slate-200 rounded p-0 text-[18px] leading-relaxed">

ריצה תיקרא **<KatexInline math="\mathcal{F}" />-הוגנת** אם היא מקיימת בו-זמנית את  כל התנאים הבאים:

- **הוֹגְנוּת בלתי מותנית** עבור כל קבוצת פעולות ב-<KatexInline math="\mathcal{F}_{uncond}" />.

- **הוֹגְנוּת חזקה** עבור כל קבוצת פעולות ב-<KatexInline math="\mathcal{F}_{strong}" />.
- **הוֹגְנוּת חלשה** עבור כל קבוצת פעולות ב-<KatexInline math="\mathcal{F}_{weak}" />.

</div>

---


<script setup>
const fairnessQuizStates = [
  { id: 'q0', text: ' ', x: 120, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8, initial: true, initialDirection: 'left' },
  { id: 'q1', text: ' ', x: 240, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8 },
  { id: 'q2', text: ' ', x: 360, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8 },
];

const fairnessQuizTransitions = [
  { source: 'q0', target: 'q1', action: '$\\alpha_1$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', actionY: -12 },
  { source: 'q1', target: 'q2', action: '$\\alpha_3$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', actionY: -12 },
  { source: 'q2', target: 'q0', action: '$\\alpha_4$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', curve: -0.35, actionY: 18 },
  { source: 'q0', target: 'q0', action: '$\\alpha_7$', actionFontSize: 17, loopDirection: '-120deg', loopRadius: 85, loopLabelRadius: 65, actionY: -5 },
  { source: 'q1', target: 'q2', action: '$\\alpha_6$', actionFontSize: 17, curve: -0.35, actionY: -20 },
  { source: 'q2', target: 'q0', action: '$\\alpha_7$', actionFontSize: 17, curve: 0.55, actionX: 0, actionY: -20 },
];
</script>

# חידון: האם הריצה הוגנת?

<div class="mt-1 text-center text-[20px]" dir="ltr">
<KatexInline math="\mathcal{F}=\langle" />
<span class="text-blue-700"><KatexInline math="\{\{\alpha_1,\alpha_2\},\{\alpha_2,\alpha_3\}\}" /></span>,
<span class="text-red-600"><KatexInline math="\{\{\alpha_4,\alpha_5\},\{\alpha_5,\alpha_6\}\}" /></span>,
<span class="text-slate-800"><KatexInline math="\{\{\alpha_6,\alpha_7\},\{\alpha_7,\alpha_8\}\}" /></span>
<KatexInline math="\rangle" />
</div>

<div class="mt-1 pr-16 pl-36 text-center text-[20px]" dir="ltr">
  <div class="inline-grid grid-cols-6 gap-[5.54rem]">
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-red-600">✗</div>
    <div v-click class="text-red-600">✗</div>
    <div v-click class="text-emerald-600">✓</div>
  </div>
</div>

<div class="mt-1 mb-6 text-flex justify-center" dir="ltr">
  <TransitionSystemD3
    :width="480"
    :height="185"
    :auto="false"
    :states="fairnessQuizStates"
    :transitions="fairnessQuizTransitions"
  />
</div>

<div class="-mt-4 space-y-3 text-center text-[16px] leading-relaxed">
<div>
כל אחת מהקבוצות <span dir="ltr" class="text-blue-700"><KatexInline math="\{\alpha_1,\alpha_2\},\{\alpha_2,\alpha_3\}" /></span>
צריכה להיבחר אינסוף פעמים.
</div>

<div>
לגבי כל אחת מהקבוצות <span dir="ltr" class="text-red-600"><KatexInline math="\{\alpha_4,\alpha_5\},\{\alpha_5,\alpha_6\}" /></span>:
אם היא מאופשרת אינסוף פעמים, היא צריכה להיבחר אינסוף פעמים.
</div>

<div>
לגבי כל אחת מהקבוצות <span dir="ltr"><KatexInline math="\{\alpha_6,\alpha_7\},\{\alpha_7,\alpha_8\}" /></span>:
אם היא מאופשרת ברצף מזמן מסוים, היא צריכה להיבחר אינסוף פעמים.
</div>
</div>

---

<script setup>
const fairnessQuiz2States = [
  { id: 'r0', text: ' ', x: 80, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8, initial: true, initialDirection: 'left' },
  { id: 'r1', text: ' ', x: 185, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8 },
  { id: 'r2', text: ' ', x: 290, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8 },
  { id: 'r3', text: ' ', x: 395, y: 92, width: 50, rx: 0, color: '#fff200', stroke: '#111827', strokeWidth: 1.8 },
];

const fairnessQuiz2Transitions = [
  { source: 'r0', target: 'r1', action: '$\\alpha_1$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', actionY: -12 },
  { source: 'r1', target: 'r2', action: '$\\alpha_3$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', actionY: -12 },
  { source: 'r2', target: 'r3', action: '$\\alpha_6$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', actionY: -12 },
  { source: 'r3', target: 'r0', action: '$\\alpha_5$', actionFontSize: 18, stroke: '#dc2626', strokeWidth: 3, labelColor: '#dc2626', midPoints: [{ x: 238, y: 150 }], actionY: 17 },
  { source: 'r0', target: 'r0', action: '$\\alpha_7$', actionFontSize: 17, loopDirection: '-120deg', loopRadius: 76, loopLabelRadius: 58, actionY: -5 },
  { source: 'r1', target: 'r2', action: '$\\alpha_8$', actionFontSize: 17, curve: -0.48, actionY: -25 },
  { source: 'r3', target: 'r3', action: '$\\alpha_7$', actionFontSize: 17, loopDirection: '-35deg', loopRadius: 76, loopLabelRadius: 58, actionY: -5 },
];
</script>

# חידון נוסף: האם הריצה הוגנת?

<div class="mt-1 text-center text-[20px]" dir="ltr">
<KatexInline math="\mathcal{F}=\langle" />
<span class="text-blue-700"><KatexInline math="\{\{\alpha_1,\alpha_2\},\{\alpha_2,\alpha_3\}\}" /></span>,
<span class="text-red-600"><KatexInline math="\{\{\alpha_4,\alpha_5\},\{\alpha_5,\alpha_6\}\}" /></span>,
<span class="text-slate-800"><KatexInline math="\{\{\alpha_6,\alpha_7\},\{\alpha_7,\alpha_8\}\}" /></span>
<KatexInline math="\rangle" />
</div>

<div class="mt-1 pr-16 pl-36 text-center text-[20px]" dir="ltr">
  <div class="inline-grid grid-cols-6 gap-[5.54rem]">
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-emerald-600">✓</div>
    <div v-click class="text-red-600">✗</div>
  </div>
</div>

<div class="mt-1 mb-6 text-flex justify-center" dir="ltr">
  <TransitionSystemD3
    :width="520"
    :height="185"
    :auto="false"
    :states="fairnessQuiz2States"
    :transitions="fairnessQuiz2Transitions"
  />
</div>

<div class="-mt-4 space-y-3 text-center text-[16px] leading-relaxed">
<div>
כל אחת מהקבוצות <span dir="ltr" class="text-blue-700"><KatexInline math="\{\alpha_1,\alpha_2\},\{\alpha_2,\alpha_3\}" /></span>
צריכה להיבחר אינסוף פעמים.
</div>

<div>
לגבי כל אחת מהקבוצות <span dir="ltr" class="text-red-600"><KatexInline math="\{\alpha_4,\alpha_5\},\{\alpha_5,\alpha_6\}" /></span>:
אם היא מאופשרת אינסוף פעמים, היא צריכה להיבחר אינסוף פעמים.
</div>

<div>
לגבי כל אחת מהקבוצות <span dir="ltr"><KatexInline math="\{\alpha_6,\alpha_7\},\{\alpha_7,\alpha_8\}" /></span>:
אם היא מאופשרת ברצף מזמן מסוים, היא צריכה להיבחר אינסוף פעמים.
</div>
</div>

---

# דוגמה להנחת הוֹגְנוּת

<div class="mt-5 text-center text-[26px]" dir="ltr">
<KatexInline display math="\mathcal{F}=\langle\emptyset,\{\{enter_1\},\{enter_2\}\},\{\{req_1\},\{req_2\}\}\rangle" />
</div>

<div class="grid grid-cols-2 gap-6 mt-7 text-right text-[21px] leading-relaxed">
<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">אילוץ חזק על כניסה</div>
אם <KatexInline math="enter_i" /> מאופשרת אינסוף פעמים, היא צריכה להיבחר אינסוף פעמים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-5">
<div class="font-bold text-amber-700 mb-3">אילוץ חלש על בקשה</div>
אם <KatexInline math="req_i" /> נשארת מאופשרת ברצף, היא צריכה להיבחר אינסוף פעמים.
</div>
</div>

<div class="mt-7 bg-blue-50 border border-blue-200 rounded p-4 text-[21px] leading-relaxed">
במניעה הדדית, אילוצים כאלה עוזרים להבחין בין הרעבה אמיתית לבין ריצה שנובעת משיבוץ לא סביר.
</div>

---

# מסלולים ועקבות הוגנים

<div class="mt-6 text-right text-[22px] leading-relaxed">
מסלול הוא <KatexInline math="\mathcal{F}" />-הוגן אם קיימת ריצה מעליו שמקיימת את הנחת ההוֹגְנוּת.
</div>

<div class="mt-6 text-center text-[28px]" dir="ltr">
<KatexInline display math="FairPaths_{\mathcal{F}}(s)" />
</div>

<div class="mt-5 text-right text-[22px] leading-relaxed">
עקבה היא <KatexInline math="\mathcal{F}" />-הוגנת אם היא מתקבלת מריצה <KatexInline math="\mathcal{F}" />-הוגנת:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="FairTraces_{\mathcal{F}}(TS)=trace(FairPaths_{\mathcal{F}}(TS))" />
</div>

---

# הגדרה: קיום תכונה תחת הוֹגְנוּת

<div class="mt-7 text-right text-[22px] leading-relaxed">
בלי הנחות הוֹגְנוֹת, מערכת <KatexInline math="TS" /> מקיימת תכונת זמן ליניארי <KatexInline math="P" /> אם:
</div>

<div class="mt-4 text-center text-[30px]" dir="ltr">
<KatexInline display math="Traces(TS)\subseteq P" />
</div>

<div class="mt-7 text-right text-[22px] leading-relaxed">
תחת הנחת הוֹגְנוּת <KatexInline math="\mathcal{F}" />, בודקים רק את העקבות ההוֹגְנוֹת:
</div>

<div class="mt-4 text-center text-[30px]" dir="ltr">
<KatexInline display math="TS\models_{\mathcal{F}} P \quad\Longleftrightarrow\quad FairTraces_{\mathcal{F}}(TS)\subseteq P" />
</div>

<div class="mt-6 bg-amber-50 border border-amber-200 rounded p-4 text-[21px] leading-relaxed">
לכן ייתכן ש-<KatexInline math="TS\models_{\mathcal{F}}P" /> אבל <KatexInline math="TS\not\models P" />: הדוגמאות הנגדיות קיימות, אך אינן הוֹגְנוֹת.
</div>

---

# הוגנות למניעת הרעבה: שלב 1

<div class="-mt-3 text-center text-[23px]" dir="ltr">
<KatexInline display math="\mathcal{F}=\langle\emptyset,\emptyset,\emptyset\rangle" />
</div>

<div class="-mt-14 mb-1 -translate-x-2 scale-[0.78]" dir="ltr">
  <SemaphoreMutexTs :width="460" :height="300" highlight-starvation />
</div>

<div class="mt-12 bg-red-50 border border-red-200 rounded p-3 text-[15px] leading-relaxed text-right">
ללא אילוצי הוֹגְנוּת מתקבלת דוגמה נגדית הנובעת מהרעבה לא רצופה של <span dir="ltr"><KatexInline math="enter_2" /></span>
. 
</div>

---

# הוגנות למניעת הרעבה: שלב 2

<div class="mt-0 text-center text-[23px]" dir="ltr">
<KatexInline display math="\mathcal{F}'=\langle\emptyset,\{\{enter_1\},\{enter_2\}\},\emptyset\rangle" />
</div>

<div class="-mt-14 mb-1 -translate-x-2 scale-[0.78]" dir="ltr">
  <SemaphoreMutexTs :width="460" :height="300" highlight-problematic-run />
</div>

<div class="mt-10 bg-amber-50 border border-amber-200 rounded p-3 text-[15px] leading-relaxed text-right">
הוספת הוֹגְנוּת זאת לא מספיקה: עדיין קיימת הרעבה בעייתית
והחיצים הכחולים מסמנים הזדמנות רצופה ל-<span dir="ltr"><KatexInline math="req_2" /></span> שלא נבחרת.
</div>

---

# הוגנות למניעת הרעבה: שלב 3

<div class="mt-0 text-center text-[23px]" dir="ltr">
<KatexInline display math="\mathcal{F}''=\langle\emptyset,\{\{enter_1\},\{enter_2\}\},\{\{req_1\},\{req_2\}\}\rangle" />
</div>

<div class="-mt-14 mb-1 -translate-x-2 scale-[0.78]" dir="ltr">
  <SemaphoreMutexTs :width="460" :height="300" />
</div>

<div class="mt-12 bg-emerald-50 border border-emerald-200 rounded p-3 text-[15px] leading-relaxed text-right">
לאחר חיזוק באילוצי הוֹגְנוּת חלשה על <span dir="ltr"><KatexInline math="req_1, req_2" /></span>, הריצה המדוברת נפסלת ואין דוגמה נגדית מתאימה.
</div>

---

# סיכום...

<div class="text-center text-[22px] leading-relaxed mt-2 space-y-4">
נגדיר:

<div dir="ltr">
<KatexInline display math="P=\{\sigma\in(2^{AP})^\omega\mid \forall i\ge 0\ \exists j\ge i\ \left(c_1\in\sigma_j\right)\land \forall i\ge 0\ \exists j\ge i\ \left(c_2\in\sigma_j\right)\}" />
</div>

<div class="bg-red-50 border border-red-200 rounded p-4 text-[19px] leading-relaxed">
<span dir="ltr"><KatexInline math="\mathcal{F}=\langle\emptyset,\emptyset,\emptyset\rangle" /></span>
<br>
ללא אילוצי הוֹגְנוּת: <span dir="ltr"><KatexInline math="TS\not\models_{\mathcal{F}} P" /></span>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4 text-[19px] leading-relaxed">
<span dir="ltr"><KatexInline math="\mathcal{F}'=\langle\emptyset,\{\{enter_1\},\{enter_2\}\},\emptyset\rangle" /></span>
<br>
רק הוֹגְנוּת חזקה על <span dir="ltr"><KatexInline math="enter_i" /></span>: עדיין <span dir="ltr"><KatexInline math="TS\not\models_{\mathcal{F}'} P" /></span>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4 text-[19px] leading-relaxed">
<span dir="ltr"><KatexInline math="\mathcal{F}''=\langle\emptyset,\{\{enter_1\},\{enter_2\}\},\{\{req_1\},\{req_2\}\}\rangle" /></span>
<br>
עם הוֹגְנוּת חלשה על <span dir="ltr"><KatexInline math="req_i" /></span>: <span dir="ltr"><KatexInline math="TS\models_{\mathcal{F}''} P" /></span>
</div>
</div>

---

# הוֹגְנוּת בת מימוש

<div class="mt-7 text-right text-[22px] leading-relaxed">
הנחת הוֹגְנוּת <KatexInline math="\mathcal{F}" /> היא <span class="font-bold">בת מימוש</span> ב-<KatexInline math="TS" /> אם מכל מצב נגיש קיימת לפחות ריצה הוגנת אחת:
</div>

<div class="mt-7 text-center text-[31px]" dir="ltr">
<KatexInline display math="\forall s\in Reach(TS)\ \left(FairPaths_{\mathcal{F}}(s)\neq\emptyset\right)" />
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-[22px] leading-relaxed">
משמעות אינטואיטיבית: כל רישא סופית של ריצה במערכת ניתנת להשלמה לריצה הוגנת.
</div>

---

# האם הוֹגְנוּת משפיעה על בטיחות?

<div class="mt-7 text-right text-[22px] leading-relaxed">
הנחות הוֹגְנוֹת בנות מימוש אינן משנות אימות של תכונות בטיחות.
</div>

<div class="mt-7 text-center text-[30px]" dir="ltr">
<KatexInline display math="TS\models_{\mathcal{F}} P_{safe}\quad\Longleftrightarrow\quad TS\models P_{safe}" />
</div>

<div class="mt-7 bg-slate-50 border border-slate-200 rounded p-5 text-[21px] leading-relaxed">
הסיבה: הפרת בטיחות מתגלה ברישא סופית. אם ההוֹגְנוּת בת מימוש, אפשר להשלים את הרישא הזאת לריצה הוגנת, ולכן ההפרה לא יכולה "להיעלם" רק בגלל ההנחה.
</div>

---

<script setup>
const unrealizableFairnessStates = [
  {
    id: 'left',
    text: ' ',
    label: '$\\{\\}$',
    labelFontSize: 20,
    labelX: 25,
    labelY: 26,
    x: 210,
    y: 86,
    width: 78,
    rx: 0,
    color: '#fff200',
    stroke: '#111827',
    strokeWidth: 1.8,
    initial: true,
    initialDirection: 'top',
  },
  {
    id: 'right',
    text: ' ',
    label: '$\\{p\\}$',
    labelFontSize: 20,
    labelX: 25,
    labelY: 26,
    x: 410,
    y: 86,
    width: 78,
    rx: 0,
    color: '#fff200',
    stroke: '#111827',
    strokeWidth: 1.8,
  },
];

const unrealizableFairnessTransitions = [
  {
    source: 'left',
    target: 'left',
    action: '$\\alpha$',
    actionFontSize: 20,
    loopDirection: '160deg',
    loopRadius: 88,
    loopLabelRadius: 77,
    actionX: 0,
    actionY: 0,
  },
  {
    source: 'left',
    target: 'right',
    action: '$\\beta$',
    actionFontSize: 20,
    actionY: 0,
  },
  {
    source: 'right',
    target: 'right',
    action: '$\\beta$',
    actionFontSize: 20,
    loopDirection: '-30deg',
    loopRadius: 88,
    loopLabelRadius: 77,
    actionX: 0,
    actionY: 0,
  },
];
</script>

# כשההנחה אינה בת מימוש

<div class="mt-1 text-right text-[22px] leading-relaxed text-slate-700">
הנחות הוֹגְנוּת שאינן בנות מימוש עלולות לפגוע גם בתכונות בטיחות.
</div>

<div class="-mt-10 flex justify-center h-[225px]" dir="ltr">
  <TransitionSystemD3
    :width="620"
    :height="215"
    :auto="false"
    :states="unrealizableFairnessStates"
    :transitions="unrealizableFairnessTransitions"
  />
</div>

<div class="grid grid-cols-2 gap-4 -mt-10 text-[20px] leading-relaxed">
  <div class="text-right">תכונת בטיחות (שְׁמוּרָה):</div>
  <div class="text-left" dir="ltr"><KatexInline math="P=\{\sigma\in(2^{AP})^\omega\mid \forall i\ge 0\ \left(p\notin\sigma_i\right)\}" /></div>

  <div class="text-right">הנחת הוֹגְנוּת בלתי מותנית:</div>
  <div class="text-left" dir="ltr"><KatexInline math="\mathcal{F}=\langle\{\{\alpha\}\},\emptyset,\emptyset\rangle" /></div>
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[20px] leading-relaxed text-right text-blue-800 ">
הנחה זו אינה בת מימוש כיוון שהמצב הימני נגיש אבל חסר ריצות הוֹגְנוֹת.
</div>

<div class="mt-3 bg-slate-50 border border-slate-300 rounded p-2 text-center text-[20px] text-red-600" dir="ltr">
<KatexInline math="TS\models_{\mathcal{F}} P" />
<span class="mx-8">אבל</span>
<KatexInline math="TS\not\models P" />
<div class="mt-1" dir="rtl">גם עבור תכונת בטיחות</div>
</div>

---

# סיכום

<div class="mt-8 text-right text-[22px] leading-relaxed">

- הוֹגְנוּת פוסלת ריצות לא מציאותיות שנוצרות מאי-דטרמיניזם.

- בדרך כלל צריך הוֹגְנוּת כדי להוכיח תכונות חַיּוּת, במיוחד מניעת הרעבה והתקדמות.
- שלושת האילוצים המרכזיים הם הוֹגְנוּת בלתי מותנית, חזקה וחלשה.
- הנחת הוֹגְנוּת <KatexInline math="\mathcal{F}" /> מגדירה אילוצים שונים על קבוצות פעולות שונות.
- תחת הוֹגְנוּת בודקים רק עקבות הוֹגְנוֹת:
  <KatexInline math="FairTraces_{\mathcal{F}}(TS)\subseteq P" />.
- הנחות הוֹגְנוֹת בנות מימוש אינן משפיעות על תכונות בטיחות.

</div>
