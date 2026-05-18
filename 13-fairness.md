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

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">למה צריך הוֹגְנוּת?</div>

- נבין מדוע תכונות חיות רבות אינן ניתנות להוכחה בלי הנחות נוספות.
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

<div class="mt-7 text-right text-[23px] leading-relaxed">

במערכות מקביליות, תכונת חיות כמו "בסוף תהליך 2 ירוץ" אינה נובעת רק ממבנה התוכנית.
צריך גם לומר משהו על מנגנון השיבוץ.

</div>

<div class="grid grid-cols-[1.15fr_0.85fr] gap-6 mt-6 items-center">
<div class="bg-amber-50 border border-amber-200 rounded p-5 text-right text-[21px] leading-relaxed">
נניח שתהליך <KatexInline math="P_2" /> מתחיל בפעולה:

<div class="mt-3 text-center" dir="ltr">
<KatexInline display math="x := 1" />
</div>

נרצה להוכיח שמנקודה מסוימת ואילך תמיד <KatexInline math="x=1" />:

<div class="mt-3 text-center" dir="ltr">
<KatexInline display math="P=\{\sigma\in(2^{AP})^\omega \mid \exists i\ge 0.\ \forall j>i.\ \sigma[j]\models x=1\}" />
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

---

# הוֹגְנוּת היא חלק מהמודל

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

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-5 text-[22px]">
ככל שהאילוץ חזק יותר, הוא פוסל יותר ריצות.
</div>

---

# סימון פורמלי

<div class="mt-6 text-right text-[22px] leading-relaxed">
נכתוב ריצה אינסופית במערכת מעברים כך:
</div>

<div class="mt-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="\rho = s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} s_2 \xrightarrow{\alpha_3}\cdots" />
</div>

<div class="mt-6 text-right text-[22px] leading-relaxed">
עבור קבוצת פעולות <KatexInline math="A\subseteq Act" />, נסמן:
</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-[21px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr">
<KatexInline display math="\exists^\infty i.\ \alpha_i\in A" />
<div class="text-right mt-2" dir="rtl">נבחרת פעולה מ-<KatexInline math="A" /> אינסוף פעמים.</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4" dir="ltr">
<KatexInline display math="Post(s_i,A)\neq\emptyset" />
<div class="text-right mt-2" dir="rtl">במצב <KatexInline math="s_i" /> מאופשרת פעולה מ-<KatexInline math="A" />.</div>
</div>
</div>

---

# הגדרות: הוֹגְנוּת ביחס לקבוצת פעולות

<div class="mt-3 text-right text-[20px] leading-relaxed">
ריצה <KatexInline math="\rho" /> היא:
</div>

<div class="mt-3 space-y-4 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<span class="font-bold text-blue-700">הוגנת ללא תנאי ביחס ל-<KatexInline math="A" /></span>
אם:
<span dir="ltr"><KatexInline math="\exists^\infty i.\ \alpha_i\in A" /></span>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<span class="font-bold text-emerald-700">הוגנת חזק ביחס ל-<KatexInline math="A" /></span>
אם:
<span dir="ltr"><KatexInline math="\left(\exists^\infty i.\ Post(s_i,A)\neq\emptyset\right)\Rightarrow\left(\exists^\infty i.\ \alpha_i\in A\right)" /></span>
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<span class="font-bold text-amber-700">הוגנת חלש ביחס ל-<KatexInline math="A" /></span>
אם:
<span dir="ltr"><KatexInline math="\left(\exists j.\ \forall i>j.\ Post(s_i,A)\neq\emptyset\right)\Rightarrow\left(\exists^\infty i.\ \alpha_i\in A\right)" /></span>
</div>
</div>

---

# יחסים בין סוגי ההוֹגְנוּת

<div class="mt-8 text-center text-[31px]" dir="ltr">
<KatexInline display math="\text{unconditional } A\text{-fair}" />
<div class="my-2">⇓</div>
<KatexInline display math="\text{strong } A\text{-fair}" />
<div class="my-2">⇓</div>
<KatexInline display math="\text{weak } A\text{-fair}" />
</div>

<div class="mt-8 text-right text-[22px] leading-relaxed bg-slate-50 border border-slate-200 rounded p-5">
ההכלה היא חד-כיוונית: ריצה יכולה להיות הוגנת חלש אבל לא הוגנת חזק, או הוגנת חזק אבל לא הוגנת ללא תנאי.
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

<div class="mt-8 bg-red-50 border border-red-200 rounded p-5 text-[21px] leading-relaxed">
אילוץ חזק מדי עלול לפסול התנהגויות אמיתיות; אילוץ חלש מדי עלול להשאיר דוגמאות נגדיות לא מציאותיות.
</div>

---

# הנחת הוֹגְנוּת

<div class="mt-6 text-right text-[22px] leading-relaxed">
הנחת הוֹגְנוּת עבור קבוצת פעולות <KatexInline math="Act" /> היא שלישייה:
</div>

<div class="mt-5 text-center text-[31px]" dir="ltr">
<KatexInline display math="\mathcal{F}=(\mathcal{F}_{uncond},\mathcal{F}_{strong},\mathcal{F}_{weak})" />
</div>

<div class="mt-6 text-right text-[21px] leading-relaxed">
כאשר כל רכיב הוא אוסף של קבוצות פעולות:
</div>

<div class="mt-4 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathcal{F}_{uncond},\mathcal{F}_{strong},\mathcal{F}_{weak}\subseteq 2^{Act}" />
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-5 text-[21px] leading-relaxed">
ריצה היא <KatexInline math="\mathcal{F}" />-הוגנת אם היא מקיימת את כל אילוצי ההוֹגְנוּת שבשלושת האוספים.
</div>

---

# דוגמה להנחת הוֹגְנוּת

<div class="mt-5 text-center text-[26px]" dir="ltr">
<KatexInline display math="\mathcal{F}=(\emptyset,\{\{enter_1\},\{enter_2\}\},\{\{req_1\},\{req_2\}\})" />
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

# קיום תכונה תחת הוֹגְנוּת

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

# מניעת הרעבה תחת הוֹגְנוּת

<div class="grid grid-cols-[1.05fr_0.95fr] gap-6 mt-2 items-center">
<img src="/slide-reference/16-fairness/slide-042.png" class="w-full rounded border border-slate-200" />

<div class="text-right text-[22px] leading-relaxed">
נגדיר:

<div class="mt-4 text-center" dir="ltr">
<KatexInline display math="P=\text{``each process enters its critical section infinitely often''}" />
</div>

<div class="mt-5 bg-slate-50 border border-slate-200 rounded p-4">
ללא הוֹגְנוּת: <span dir="ltr"><KatexInline math="TS\not\models P" /></span>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-4">
עם הנחה חלשה מדי: עדיין מקבלים דוגמה נגדית.
</div>

<div class="mt-4 bg-emerald-50 border border-emerald-200 rounded p-4">
עם הנחה מתאימה: <span dir="ltr"><KatexInline math="TS\models_{\mathcal{F}}P" /></span>
</div>
</div>
</div>

---

# הוֹגְנוּת בת מימוש

<div class="mt-7 text-right text-[22px] leading-relaxed">
הנחת הוֹגְנוּת <KatexInline math="\mathcal{F}" /> היא <span class="font-bold">בת מימוש</span> ב-<KatexInline math="TS" /> אם מכל מצב נגיש קיימת לפחות ריצה הוגנת אחת:
</div>

<div class="mt-7 text-center text-[31px]" dir="ltr">
<KatexInline display math="\forall s\in Reach(TS).\quad FairPaths_{\mathcal{F}}(s)\neq\emptyset" />
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-[22px] leading-relaxed">
משמעות אינטואיטיבית: כל רישא סופית של ריצה במערכת ניתנת להשלמה לריצה הוגנת.
</div>

---

# האם הוֹגְנוּת משפיעה על בטיחות?

<div class="mt-7 text-right text-[22px] leading-relaxed">
לפי סעיף 3.5.3 בספר, הנחות הוֹגְנוֹת בנות מימוש אינן משנות אימות של תכונות בטיחות.
</div>

<div class="mt-7 text-center text-[30px]" dir="ltr">
<KatexInline display math="TS\models_{\mathcal{F}} P_{safe}\quad\Longleftrightarrow\quad TS\models P_{safe}" />
</div>

<div class="mt-7 bg-slate-50 border border-slate-200 rounded p-5 text-[21px] leading-relaxed">
הסיבה: הפרת בטיחות מתגלה ברישא סופית. אם ההוֹגְנוּת בת מימוש, אפשר להשלים את הרישא הזאת לריצה הוגנת, ולכן ההפרה לא יכולה "להיעלם" רק בגלל ההנחה.
</div>

---

# כשההנחה אינה בת מימוש

<div class="grid grid-cols-[0.95fr_1.05fr] gap-6 mt-7 items-center">
<div class="text-right text-[22px] leading-relaxed">
הנחת הוֹגְנוּת שאינה בת מימוש עלולה למחוק את כל ההמשכים האפשריים אחרי מצב נגיש מסוים.

<div class="mt-5 bg-red-50 border border-red-200 rounded p-4">
במצב כזה אפשר "להוכיח" תכונת בטיחות רק כי כל הריצות הבעייתיות נפסלו באופן לא לגיטימי.
</div>
</div>

<div class="relative h-[260px]" dir="ltr">
  <svg class="absolute inset-0 h-full w-full" viewBox="0 0 520 260" aria-hidden="true">
    <defs>
      <marker id="fairness-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 Z" fill="#334155" />
      </marker>
    </defs>
    <circle cx="140" cy="125" r="44" fill="#f8fafc" stroke="#334155" stroke-width="3" />
    <circle cx="380" cy="125" r="44" fill="#dbeafe" stroke="#2563eb" stroke-width="3" />
    <path d="M 184 125 L 336 125" stroke="#334155" stroke-width="4" marker-end="url(#fairness-arrow)" />
    <path d="M 380 81 C 430 35 485 80 430 125" fill="none" stroke="#334155" stroke-width="4" marker-end="url(#fairness-arrow)" />
    <text x="140" y="134" text-anchor="middle" font-size="28" fill="#111827">∅</text>
    <text x="380" y="134" text-anchor="middle" font-size="28" fill="#111827">{p}</text>
    <text x="252" y="106" text-anchor="middle" font-size="24" fill="#111827">α</text>
    <text x="448" y="67" text-anchor="middle" font-size="24" fill="#111827">β</text>
  </svg>
</div>
</div>

---

# סיכום

<div class="mt-8 text-right text-[22px] leading-relaxed">

- הוֹגְנוּת פוסלת ריצות לא מציאותיות שנוצרות מאי-דטרמיניזם.
- בדרך כלל צריך הוֹגְנוּת כדי להוכיח תכונות חיות, במיוחד מניעת הרעבה והתקדמות.
- שלושת האילוצים המרכזיים הם הוֹגְנוּת בלתי מותנית, חזקה וחלשה.
- הנחת הוֹגְנוּת <KatexInline math="\mathcal{F}" /> מגדירה אילוצים שונים על קבוצות פעולות שונות.
- תחת הוֹגְנוּת בודקים רק עקבות הוֹגְנוֹת:
  <KatexInline math="FairTraces_{\mathcal{F}}(TS)\subseteq P" />.
- הנחות הוֹגְנוֹת בנות מימוש אינן משפיעות על תכונות בטיחות.

</div>
