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

# תכונה של מצב / תכונה של ריצה

<div class="mt-6 text-right">

הפסוקים האטומיים והפונקציה $L$ המתאימה אותם למצבים מאפשרים לנו לדבר על **תכונות של מצבים**.

<div class="grid grid-cols-[1fr_1.1fr] gap-6 mt-6 items-center">

<div class="bg-slate-50 border border-slate-200 rounded p-4 text-[15px]">
<div class="font-bold mb-3">למשל:</div>

- "תהליך 1 נמצא בקטע הקריטי"

- "המצב $s$ מקיים את הפסוק $p \lor q$"  <br/> (מסומן ב-$s \models p \lor q$).   

</div>

<div class="text-[15px]">

אבל בתכונות בטיחות רבות אנו מתעניינים גם ב**תכונות של ריצות**:

<div class="mt-4 text-red-600 font-bold text-[16px] leading-snug">
"הרמזור לא יישאר אדום למשך יותר משלושה צעדים רצופים"
</div>

<div class="-mt-25 -mb-6 scale-80" dir="ltr">

<TransitionSystemD3 :width="430" :height="240" :auto="false"
  :states="[
    { id: 'green',  text: ' ', label: '$\\{\\}$', initial: true, x: 55, y: 118, width: 50, color: '#ffffff', stroke: '#111827' },
    { id: 'yellow', text: ' ', label: '$\\{\\}$', x: 150, y: 118, width: 50, color: '#ffffff', stroke: '#111827' },
    { id: 'red1',   text: ' ', label: '$\\{red\\}$', x: 245, y: 118, width: 52, color: '#fee2e2', stroke: '#dc2626' },
    { id: 'red2',   text: ' ', label: '$\\{red\\}$', x: 340, y: 118, width: 52, color: '#fee2e2', stroke: '#dc2626' },
    { id: 'red3',   text: ' ', label: '$\\{red\\}$', x: 340, y: 205, width: 52, color: '#fee2e2', stroke: '#dc2626' },
    { id: 'bad',    text: ' ', label: '$\\{red\\}$', x: 245, y: 205, width: 52, color: '#fecaca', stroke: '#b91c1c', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 'green', target: 'yellow' },
    { source: 'yellow', target: 'red1' },
    { source: 'red1', target: 'red2', stroke: '#dc2626' },
    { source: 'red2', target: 'red3', stroke: '#dc2626' },
    { source: 'red3', target: 'bad', stroke: '#dc2626', strokeWidth: 3 },
    // { source: 'bad', target: 'green', curve: 0.35, stroke: '#dc2626', strokeWidth: 3 },
    // { source: 'red2', target: 'green', curve: 0.35 },
    // { source: 'red3', target: 'green', curve: 0.45 }
  ]"
/>

</div>

</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-[18px] font-bold">
לא מספיק לבדוק מצבים לחוד כפי שבדקנו תכונות שמורה; צריך להסתכל על רישות סופיות של ריצות.
</div>

</div>

---

# תכונות בטיחות ורישות רעות

<div class="mt-8 text-right">

תכונת בטיחות כללית מוגדרת על ידי העובדה ש**כל הפרה שלה ניתן לזהות על ידי רצף סופי**.

<div class="bg-blue-50 border border-blue-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">הגדרה: תכונת בטיחות ורֵישָׁא רעה</div>

תכונת זמן לינארי $P$ מעל $AP$ נקראת **תכונת בטיחות** (Safety Property) אם לכל מילה אינסופית $\sigma \in (2^{AP})^\omega \setminus P$ שמפרה את התכונה, קיימת **רֵישָׁא סופית** (prefix) $\rho \prec \sigma$ כך ש:
$$ P \cap \{ \sigma' \in (2^{AP})^\omega \mid \rho \prec \sigma' \} = \emptyset $$
</div>

- רֵישָׁא סופית כזו $\rho$ נקראת **רֵישָׁא רעה** (Bad Prefix). ברגע שהיא מתרחשת, לא משנה מה יקרה בעתיד, העקבה כולה לעולם לא תקיים את התכונה.

- אוסף כל הרישות הרעות של תכונה מסומן ב-**$\operatorname{BadPref}(P)$**.

<div class="mt-4 text-sm font-bold text-blue-700">
כל שמורה (Invariant) היא מקרה פרטי של תכונת בטיחות! הָרֵישָׁא הרעה שלה מסתיימת במצב שמפר את תנאי השמורה.
</div>

</div>

---

# ניסוח שקול

<div class="mt-6 text-right text-[24px] leading-relaxed">

תכונת זמן לינארי $P \subseteq (2^{AP})^\omega$ היא <span class="text-red-600 font-bold">תכונת בטיחות</span> אם ורק אם:

</div>

<div class="mx-auto mt-6 w-4/5 bg-white border border-slate-200 rounded shadow-md p-5 text-[22px] leading-relaxed text-right">

לכל מילה שלא מקיימת את התכונה, $\sigma \notin P$, קיים $i \ge -1$ כך ש־

<div class="mt-4 text-center" dir="ltr">

$\sigma'[..i] = \sigma[..i] \;\Rightarrow\; \sigma' \notin P$

</div>

</div>

<div class="relative mx-auto mt-3 w-[40%]">
  <img src="/safety_equivalent_branching.png" class="w-full" />
  <svg class="absolute left-[47%] bottom-[2%] w-[12%] h-[30%] overflow-visible" viewBox="0 0 60 150" aria-hidden="true">
    <defs>
      <marker id="sigma-prefix-arrow" markerWidth="9" markerHeight="9" refX="4.5" refY="4.5" orient="auto">
        <path d="M 0 0 L 9 4.5 L 0 9 z" fill="#1e04e3" />
      </marker>
    </defs>
    <line x1="440" y1="10" x2="60" y2="15" stroke="#1e04e3" stroke-width="6" marker-end="url(#sigma-prefix-arrow)" />
  </svg>
  <div class="absolute bottom-[18%] -right-[35%] text-blue-800 text-[22px] font-bold" dir="ltr">

  $\sigma[..i]$
  </div>
</div>


---

# דוגמאות

<div class="mt-4 text-right text-[24px]">
מי מהבאות הן תכונות בטיחות? הוכיחו טענותיכם.
</div>

<div class="grid grid-cols-2 gap-6 mt-6 text-[23px]">
  <div class="bg-green-50 text-green-800 border border-green-100 rounded p-3 text-center">
    איך נוכיח שתכונה היא תכונת בטיחות?
  </div>
  <div class="bg-red-50 text-red-800 border border-red-100 rounded p-3 text-center">
    איך נוכיח שתכונה אינה תכונת בטיחות?
  </div>
</div>

<div class="mt-10 text-left text-[22px] leading-[4.2]" dir="ltr">

$P_1 = \{\sigma \in (2^{AP})^\omega : \forall i.\; \sigma[i] \models p \to (q \lor \neg r)\}$
<br/><br/>

$P_2 = \{\sigma \in (2^{AP})^\omega : p \in \sigma[0] \to \forall i.\; p \in \sigma[i]\}$

$P_3 = \{\sigma \in (2^{AP})^\omega : p \in \sigma[2i] \to p \in \sigma[i]\}$

$P_4 = \{\sigma \in (2^{AP})^\omega : \exists i \text{ such that } p \in \sigma[i]\}$

</div>

---

# דוגמה: הוכחת בטיחות


<div class="mt-6 text-right text-[18px]">

**טענה:** התכונה הבאה היא תכונת בטיחות:

<div class="mt-3 text-center" dir="ltr">

$P = \{\sigma \in (2^{AP})^\omega :  \forall i \geq 0 ((p \in \sigma[2i]) \to (p \in \sigma[i]))\}$
</div>

<div class="-mt-0">
<span class="font-bold underline">הוכחה:</span>
</div>

- תהי $\sigma \notin P$ כלשהי.

- לפי הגדרת $P$, קיים $i$ כך ש־$p \in \sigma[2i]$ ו־$p \notin \sigma[i]$.
- תהי $\sigma'$ כך ש־$\sigma'[..2i] = \sigma[..2i]$.
- לפי הגדרת $P$, גם $\sigma' \notin P$.
- לכן ל־$\sigma$ יש רֵישָׁא רעה: $\sigma[..2i]$, וכל המשך שלה לא יקיים את התכונה.

</div>

<div class="relative mx-auto -mt-8 -ml-20 w-[78%] h-[120px] scale-60" dir="ltr">
  <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 900 120" aria-hidden="true">
    <defs>
      <marker id="bad-suffix-arrow" markerWidth="6" markerHeight="6" refX="5.5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 z" fill="#9a3412" />
      </marker>
    </defs>
    <path d="M 10 48 C 90 20, 170 36, 245 44 S 300 18, 360 38 S 430 50, 465 45"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" />
    <circle cx="465" cy="45" r="7" fill="#9a3412" />
    <path d="M 465 45 C 525 5, 610 38, 680 28 S 800 25, 890 12"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-suffix-arrow)" />
    <path d="M 465 45 C 525 38, 560 78, 635 74 S 800 70, 885 78"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-suffix-arrow)" />
    <path d="M 465 45 C 520 78, 540 120, 625 100 S 785 92, 890 150"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-suffix-arrow)" />
    <path d="M 430 102 C 440 82, 452 68, 462 55"
          fill="none" stroke="#dc2626" stroke-width="5" marker-end="url(#bad-suffix-arrow)" />
  </svg>
  <div class="absolute left-[24%] -top-[5%] text-[#5f1f1a] text-[22px] font-bold">

  $\sigma[..2i]$
  </div>
  <div class="absolute left-[24%] top-[82%] text-red-600 text-[15px] leading-tight text-center" dir="rtl">
    רֵישָׁא רעה שכל המשך שלה לא<br/>
    מקיים את התכונה
  </div>
</div>

---

# דוגמה: הוכחת אי־בטיחות


<div class="mt-6 text-right text-[16px]">

**טענה:** התכונה הבאה אינה תכונת בטיחות:

<div class="mt-3 text-center" dir="ltr">

$P = \{\sigma \in (2^{AP})^\omega \mid \exists i \geq 0 (p \in \sigma[i])\}$
</div>

<div class="mt-5">
<span class="font-bold underline">הוכחה:</span>
</div>

- ניקח את המילה $\sigma = \{\}^{\omega}$ שאינה שייכת ל־$P$.

- לכל $i$ נבנה את המילה $\sigma' = \{\}^{i}\{p\}^{\omega}$.
- על פי הגדרת $P$, מתקיים $\sigma' \in P$.
- קיבלנו שלכל $i$ קיימת $\sigma'$ כך ש־$\sigma'[..i] = \sigma[..i]$ וגם $\sigma' \in P$.
- לכן אין ל־$\sigma$ רֵישָׁא רעה, ולכן $P$ אינה תכונת בטיחות.

</div>

---

# דוגמה: רמזור (סדר מופעים)

<div class="mt-8 text-right">

נניח שקבוצת הפסוקים האטומיים היא $AP = \{red, yellow, green\}$.
נדרוש את התכונה הבאה: **"מופע של אור אדום חייב לבוא מיד אחרי מופע של אור צהוב"**.

התכונה הפורמלית:
$$ P_{traffic} = \{ \sigma \in (2^{AP})^\omega \mid \forall i \ge 0 (red \in \sigma[i] \implies i > 0 \land yellow \in \sigma[i-1]) \} $$

### דוגמאות לרישות רעות מינימליות (Minimal Bad Prefixes):
1. **$\emptyset \{red\}$**: הרמזור התחיל כבוי (או לא מוגדר) ועבר לאדום.
2. **$\{green\} \{red\}$**: הרמזור עבר מירוק ישר לאדום.

<div class="mt-6 text-[15px]">

רישות אלו הן "מינימליות" כיוון שאין להן רֵישָׁא שהיא בעצמה רעה. 
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
- לפי ההגדרה, ל-$\sigma$ יש רֵישָׁא רעה $\rho$. 
- כיוון ש-$\rho$ היא רֵישָׁא של עקבה במערכת, היא בהכרח עקבה סופית של המערכת, כלומר נמצאת ב-$Traces_{fin}(TS)$. 
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
$P = \operatorname{closure}(P)$
</div>

</div>

---

# הוכחת משפט הסגור

<div class="mt-8 text-right text-[15px]">

**כיוון ראשון ($\implies$):** נניח ש-$P$ היא תכונת בטיחות. עלינו להראות ש-$P = \operatorname{closure}(P)$.
- ההכלה $P \subseteq \operatorname{closure}(P)$ נובעת ישירות מההגדרה (כל רֵישָׁא של $\sigma \in P$ שייך ל-$\operatorname{pref}(P)$).
- עבור ההכלה השנייה: יהי $\sigma \in \operatorname{closure}(P)$. נניח בשלילה ש-$\sigma \notin P$. 
- כיוון ש-$P$ תכונת בטיחות, קיים ל-$\sigma$ **רֵישָׁא רעה** $\rho \prec \sigma$. 
- מצד שני, כיוון ש-$\sigma \in \operatorname{closure}(P)$, כל הרישות שלו שייכים ל-$\operatorname{pref}(P)$, ולכן $\rho \in \operatorname{pref}(P)$. 
- משמעות הדבר היא שקיים $\sigma' \in P$ כך ש-$\rho \prec \sigma'$, בסתירה לכך ש-$\rho$ היא רֵישָׁא רעה. לכן $\sigma \in P$.

**כיוון שני ($\impliedby$):** נניח ש-$P = \operatorname{closure}(P)$. נראה ש-$P$ תכונת בטיחות.
- יהי $\sigma \notin P$. כיוון ש-$P = \operatorname{closure}(P)$, הרי ש-$\sigma \notin \operatorname{closure}(P)$.
- לפי הגדרת הסגור, קיים ל-$\sigma$ רֵישָׁא סופית $\rho \prec \sigma$ כך ש-$\rho \notin \operatorname{pref}(P)$.
- המשמעות היא שלא קיימת אף מילה $\sigma'$ המקיימת $\rho \prec \sigma'$ ושייכת ל-$P$.
- לכן $\rho$ היא **רֵישָׁא רעה** עבור $\sigma$, ומכאן ש-$P$ היא תכונת בטיחות.

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
- אם תכונה הופרה, יש לכך עדות ב**זמן סופי** (רֵישָׁא רעה).
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
