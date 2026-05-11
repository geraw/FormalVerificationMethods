---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 11-safety-properties
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## תכונות בטיחות
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תכונות בטיחות

## הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

---

# מה מעבר לשמורות?

<div class="mt-8 text-right">

בהרצאה הקודמת הכרנו את ה**שמורות** (Invariants) כתכונות שתלויות רק ב*מצב הנוכחי* של המערכת. 

אך קיימות דרישות טבעיות למערכות שהן יותר מורכבות, ועדיין נחשבות לתכונות בטיחות:

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-6">
<div class="font-bold mb-2">דוגמה 1: כספומט (ATM)</div>
הדרישה: "ניתן למשוך כסף רק אם קודם לכן הוקלד קוד סודי (PIN) נכון".
זו אינה שמורה, כי המצב שבו יוצא כסף אינו "רע" בפני עצמו - הוא תלוי במה שקרה קודם. 
עם זאת, זו עדיין תכונת בטיחות: אם משכנו כסף בלי קוד, עשינו מעשה רע **בזמן סופי**.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-4">
<div class="font-bold mb-2">דוגמה 2: מכונת שתייה</div>
הדרישה: "מספר המטבעות שהוכנסו תמיד גדול או שווה למספר המשקאות שסופקו".
גם כאן, כדי לדעת אם מצב תקין, יש לספור את ההיסטוריה עד כה.
</div>

</div>

---

# תכונות בטיחות ורישות רעות

<div class="mt-8 text-right">

תכונת בטיחות כללית מוגדרת על ידי העובדה ש**כל הפרה שלה ניתן לזהות על ידי רצף סופי**.

<div class="bg-blue-50 border border-blue-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">הגדרה: תכונת בטיחות ורישא רעה</div>

תכונת זמן לינארי $P_{safe}$ מעל $AP$ נקראת **תכונת בטיחות** (Safety Property) אם לכל מילה אינסופית $\sigma \in (2^{AP})^\omega \setminus P_{safe}$ שמפרה את התכונה, קיימת **רישא סופית** (prefix) $\rho \prec \sigma$ כך ש:
$$ P_{safe} \cap \{ \sigma' \in (2^{AP})^\omega \mid \rho \prec \sigma' \} = \emptyset $$
</div>

- רישא סופית כזו $\rho$ נקראת **רישא רעה** (Bad Prefix). ברגע שהיא מתרחשת, לא משנה מה יקרה בעתיד, העקבה כולה לעולם לא תקיים את התכונה.
- אוסף כל הרישות הרעות של תכונה מסומן ב-**$\operatorname{BadPref}(P_{safe})$**.

<div class="mt-4 text-sm font-bold text-blue-700">
כל שמורה (Invariant) היא מקרה פרטי של תכונת בטיחות! הרישא הרעה שלה מסתיימת במצב שמפר את תנאי השמורה.
</div>

</div>

---

# המחשת הרישא הרעה

<div class="flex flex-col items-center justify-center mt-10">

<img src="/bad_prefix_concept.png" class="w-1/2 rounded-lg shadow-xl border border-slate-200" />

<div class="mt-6 text-right w-2/3 text-[14px]">
ברגע שהמסלול מבצע צעד "אסור" (הנקודה האדומה), התכונה מופרת באופן בלתי הפיך וזוהי בעצם הרישא הרעה ($\rho$). 
העתיד של המסלול (החלק המעומעם) כבר לא יכול "לתקן" את המצב.
</div>

</div>

---

# דוגמה: רמזור (סדר מופעים)

<div class="mt-8 text-right">

נניח שקבוצת הפסוקים האטומיים היא $AP = \{red, yellow, green\}$.
נדרוש את התכונה הבאה: **"מופע של אור אדום חייב לבוא מיד אחרי מופע של אור צהוב"**.

התכונה הפורמלית:
$$ P_{traffic} = \{ \sigma \in (2^{AP})^\omega \mid \forall i \ge 0, (red \in \sigma[i] \implies i > 0 \land yellow \in \sigma[i-1]) \} $$

### דוגמאות לרישות רעות מינימליות (Minimal Bad Prefixes):
1. **$\emptyset \{red\}$**: הרמזור התחיל כבוי (או לא מוגדר) ועבר לאדום.
2. **$\{green\} \{red\}$**: הרמזור עבר מירוק ישר לאדום.

<div class="mt-6 text-[15px]">

רישות אלו הן "מינימליות" כיוון שאין להן רישא שהיא בעצמה רעה. 
לעומת זאת, $\dots \{yellow\} \{yellow\} \{red\} \{red\} \emptyset \{red\}$ אינה מינימלית כי חלק ממנה מפר את התכונה מוקדם יותר.
</div>

</div>

---
---

<div class="transform scale-90 origin-top-right">

# סיפוק תכונות בטיחות (Satisfaction)

<div class="mt-8 text-right">

כיצד בודקים האם מערכת תלוית-מצב מקיימת תכונת בטיחות כללית? הקישור נעשה באמצעות קבוצת העקבות ה**סופיות** של המערכת.

<div class="bg-green-50 border border-green-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">למה (Satisfaction Relation)</div>

עבור מערכת תלוית-מצב $TS$ ללא מצבי קצה סופיים, ותכונת בטיחות $P_{safe}$:
$$ TS \models P_{safe} \iff Traces_{fin}(TS) \cap \operatorname{BadPref}(P_{safe}) = \emptyset $$
</div>

**הוכחה (רעיון מרכזי):** 
- אם המערכת מפרה את התכונה ($TS \not\models P_{safe}$), יש לה עקבה אינסופית $\sigma \notin P_{safe}$. 
- לפי ההגדרה, ל-$\sigma$ יש רישא רעה $\rho$. 
- כיוון ש-$\rho$ היא רישא של עקבה במערכת, היא בהכרח עקבה סופית של המערכת, כלומר נמצאת ב-$Traces_{fin}(TS)$. 
- לכן החיתוך אינו ריק. ההיקש ההפוך פועל באופן דומה.

</div>

</div>

---

# סגור (Closure)

<div class="mt-8 text-right">

דרך מתמטית אלגנטית נוספת לאפיין תכונות בטיחות היא דרך המושג "סגור" (Closure).
עבור עקבה $\sigma$, נסמן ב-$\operatorname{pref}(\sigma)$ את קבוצת כל הרישות הסופיות שלה. באופן דומה עבור תכונה $P$, נסמן את אוסף הרישות שלה ב-$\operatorname{pref}(P)$.

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-6">
<div class="font-bold mb-2">הגדרה: סגור של תכונה</div>
הסגור של תכונה $P$ הוא קבוצת כל העקבות האינסופיות ש**כל הרישות שלהן** שייכים לקבוצת הרישות של $P$:
$$ \operatorname{closure}(P) = \{ \sigma \in (2^{AP})^\omega \mid \operatorname{pref}(\sigma) \subseteq \operatorname{pref}(P) \} $$
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 mt-6">
<div class="font-bold mb-2">משפט: אפיון אלטרנטיבי לתכונות בטיחות</div>
תכונת זמן לינארי $P$ היא תכונת בטיחות **אם ורק אם** היא שווה לסגור שלה: 
$$ P = \operatorname{closure}(P) $$
</div>

</div>

---

# הכלת עקבות סופיות (Finite Trace Inclusion)

<div class="mt-8 text-right">

כאשר מתכננים מערכת בגישה של עידון הדרגתי (Stepwise Refinement), לרוב אנו מעוניינים להוכיח שאם המודל האבסטרקטי מקיים תכונה, כך גם המודל המפורט (המעודן).

ראינו קודם ש**הכלת עקבות אינסופיות** שומרת על *כל* תכונות הזמן הלינארי. תכונות בטיחות דורשות פחות מזה:

<div class="bg-slate-50 border border-slate-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">משפט: בטיחות והכלת עקבות סופיות</div>

יהיו $TS$ ו-$TS'$ שתי מערכות ללא מצבי סיום, מעל אותה קבוצת פסוקים אטומיים $AP$. התנאים הבאים שקולים:
1. $Traces_{fin}(TS) \subseteq Traces_{fin}(TS')$
2. לכל תכונת בטיחות $P_{safe}$: אם $TS' \models P_{safe}$ אזי $TS \models P_{safe}$
</div>

המשמעות: כדי לשמר תכונות בטיחות, מספיק להראות שהמערכת המפורטת $TS$ לא יכולה לייצר אף עקבה **סופית** שלא הייתה אפשרית במערכת האבסטרקטית $TS'$.

</div>

---

# סיכום

<div class="grid grid-cols-2 gap-8 mt-10 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">תכונות בטיחות</div>

- מאופיינות על ידי האמירה "משהו רע לעולם לא יקרה".
- אם תכונה הופרה, יש לכך עדות ב**זמן סופי** (רישא רעה).
- שמורות הן מקרה פרטי של תכונות בטיחות (התלויות רק במצב בודד).
- ניתן לאפיין תכונות בטיחות באמצעות מושג הסגור ($\operatorname{closure}$).
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">שקילות והכלה</div>

- סיפוק תכונת בטיחות תלוי רק ב**עקבות הסופיות** של המערכת.
- אם מערכת $TS$ מכילה את העקבות הסופיות של מערכת $TS'$ (הכלה), היא "יורשת" ממנה את כל תכונות הבטיחות.
- בהרצאה הבאה: **תכונות חַיּוּת** (Liveness), שמבטיחות ש"משהו טוב יקרה בסופו של דבר".
</div>
</div>
