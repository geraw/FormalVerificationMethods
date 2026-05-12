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

$P_1 = \{\sigma \in (2^{AP})^\omega \mid \forall i \geq 0 ( \sigma[i] \models p \to (q \lor \neg r))\}$
<br/><br/>

$P_2 = \{\sigma \in (2^{AP})^\omega \mid \forall i \geq 0(p \in \sigma[0] \to p \in \sigma[i])\}$
<br/><br/>

$P_3 = \{\sigma \in (2^{AP})^\omega \mid \forall i \geq 0(p \in \sigma[2i] \to p \in \sigma[i])\}$
<br/><br/>

$P_4 = \{\sigma \in (2^{AP})^\omega \mid \exists i \geq 0 (p \in \sigma[i])\}$

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

<div class="relative mx-auto -mt-5 w-[82%] h-[125px] scale-60" dir="ltr">
  <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 900 135" aria-hidden="true">
    <defs>
      <marker id="good-suffix-arrow" markerWidth="6" markerHeight="6" refX="5.5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 z" fill="#2f6b08" />
      </marker>
      <marker id="bad-base-arrow" markerWidth="6" markerHeight="6" refX="5.5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 z" fill="#9a3412" />
      </marker>
    </defs>
    <path d="M 20 52 C 115 74, 220 72, 330 70 S 535 66, 655 72 S 790 46, 880 62"
          fill="none" stroke="#9a3412" stroke-width="5" stroke-linecap="round" marker-end="url(#bad-base-arrow)" />
    <circle cx="135" cy="64" r="7" fill="#2f6b08" />
    <circle cx="225" cy="68" r="7" fill="#2f6b08" />
    <circle cx="355" cy="69" r="7" fill="#2f6b08" />
    <circle cx="585" cy="70" r="7" fill="#2f6b08" />
    <circle cx="635" cy="70" r="7" fill="#2f6b08" />
    <path d="M 135 64 C 210 120, 280 106, 360 110 S 510 180, 880 170"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 225 68 C 305 18, 390 45, 465 30 S 610 8, 880 -10"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 355 69 C 430 100, 500 90, 570 110 S 735 140, 880 140"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 585 70 C 650 100, 705 112, 790 104 S 845 98, 880 100"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
    <path d="M 635 70 C 675 28, 725 42, 765 30 S 835 24, 880 28"
          fill="none" stroke="#2f6b08" stroke-width="5" stroke-linecap="round" marker-end="url(#good-suffix-arrow)" />
  </svg>
  <div class="absolute left-[0%] top-[2%] text-[#5f1f1a] text-[22px] font-bold">

  $\sigma \notin P$


  </div>

  <div class="absolute -left-[10%] top-[48%] text-[#5f1f1a] text-[22px] font-bold" dir="rtl">
  מילה רעה<br/> בלי רישא רעה
  </div>


</div>

---

# היחס בין תכונות בטיחות ותכונות שמורה?

<div class="mt-5 text-center text-[30px] leading-relaxed">
משפט: כל <span class="text-blue-700 font-bold">תכונת שמורה</span> היא גם <span class="text-red-600 font-bold">תכונת בטיחות</span>
</div>

<div class="relative mx-auto mt-7 w-[78%] h-[300px]" dir="rtl">
  <div class="absolute inset-x-0 bottom-2 mx-auto w-full h-[250px] rounded-[50%] bg-[#a45237] border-2 border-[#d98a73] shadow-lg"></div>
  <div class="absolute left-[12%] right-[12%] bottom-[48px] h-[165px] rounded-[50%] bg-[#5aa0a7] border-2 border-[#b5e4e7] shadow-lg"></div>
  <div class="absolute left-[28%] right-[28%] bottom-[83px] h-[82px] rounded-[50%] bg-[#9a8f93] border-2 border-[#d8cfd2] shadow-lg"></div>

  <div class="absolute top-[42px] inset-x-0 text-white text-[24px] font-bold text-center">
    תכונות זמן לינארי
  </div>
  <div class="absolute top-[100px] inset-x-0 text-white text-[24px] font-bold text-center">
    תכונות בטיחות
  </div>
  <div class="absolute top-[160px] inset-x-0 text-white text-[23px] font-bold text-center">
    תכונות שמורה
  </div>
</div>

<div class="mt-1 text-center text-[30px]">
הוכחה?
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

כיצד בודקים האם מערכת מעברים מקיימת תכונת בטיחות כללית? הקישור נעשה באמצעות קבוצת העקבות ה**סופיות** של המערכת.

<div class="bg-green-50 border border-green-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">למה (Satisfaction Relation)</div>

עבור מערכת מעברים $TS$ ללא מצבים סופניים, ותכונת בטיחות $P_{safe}$:
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

יהיו $TS$ ו-$TS'$ שתי מערכות מעברים ללא מצבים סופניים, מעל אותה קבוצת פסוקים אטומיים $AP$. התנאים הבאים שקולים:
1. $Traces_{fin}(TS) \subseteq Traces_{fin}(TS')$
2. לכל תכונת בטיחות $P_{safe}$: אם $TS' \models P_{safe}$ אזי $TS \models P_{safe}$
</div>

המשמעות: כדי לשמר תכונות בטיחות, מספיק להראות שהמערכת המפורטת $TS$ לא יכולה לייצר אף עקבה **סופית** שלא הייתה אפשרית במערכת האבסטרקטית $TS'$.

</div>

---

# תכונות בטיחות למכונת המשקאות

<div class="mt-5 text-right text-[23px]">

- דרישה טבעית:

<div class="mx-auto my-4 w-[88%] bg-white shadow-md p-3 text-center text-red-600 text-[27px]">
"מספר המטבעות שהוכנסו הוא לפחות מספר המשקאות שניתנו"
</div>

- לכל $i \ge 0$:

<div class="mx-auto my-4 w-[82%] bg-white shadow-md p-3 text-center" dir="ltr">
$|\{0 \le j \le i : drink \in A_j\}| \le |\{0 \le j \le i : pay \in A_j\}|$
</div>

- רישות רעות:

<div class="mt-3 text-left text-[24px] leading-[2.2]" dir="ltr">
$\emptyset\ \{pay\}\ \{drink\}\ \{drink\}$

$\emptyset\ \{pay\}\ \{drink\}\ \emptyset\ \{pay\}\ \{drink\}\ \{drink\}$
</div>

</div>

<div class="mt-4 text-right text-[22px]">
- קל לבדוק שכל הגרסאות שהצגנו למכונות מכירת השתייה עומדות בדרישה.
- זאת דוגמה ל<span class="text-blue-700 font-bold">תכונת בטיחות</span> שלא ניתן לבטא את הרישות הרעות שלה כשפה רגולרית.
</div>

---

# הגדרה: תכונות בטיחות רגולריות

<div class="mt-5 text-right text-[25px]">
תכונה שקבוצת הרישות הרעות המינימליות שלה היא שפה רגולרית
</div>

<div class="mt-7 text-right text-[23px]">
כל תכונת שמורה היא תכונת בטיחות רגולרית:
</div>

<div class="grid grid-cols-[0.9fr_1.5fr] gap-8 mt-6 items-center">

<AutomatonD3 :width="260" :height="150"
  :states="[
    { id: 'ok', x: 90, y: 75, label: ' ', initial: true, r: 36 },
    { id: 'bad', x: 198, y: 75, label: ' ', r: 36 }
  ]"
  :transitions="[
    { source: 'ok', target: 'ok', label: '$\\varphi$', loopDirection: '-90deg', loopRadius: 56, labelY: 20 },
    { source: 'ok', target: 'bad', label: '$\\neg\\varphi$', labelY: 50 }
  ]"
/>

<div class="text-right text-[24px] leading-relaxed">
אם $\varphi$ היא תנאי השמורה, האוטומט שקורא את הרישא עובר למצב כישלון ברגע הראשון שבו מתקיים $\neg\varphi$.
</div>

</div>

<div class="relative mx-auto mt-5 w-[82%] h-[260px]" dir="rtl">
  <div class="absolute inset-x-0 bottom-0 mx-auto w-full h-[230px] rounded-[50%] bg-red-300/60 border border-red-500 shadow-lg"></div>
  <div class="absolute left-[9%] right-[9%] bottom-[35px] h-[165px] rounded-[50%] bg-red-300/55 border border-red-500 shadow-lg"></div>
  <div class="absolute left-[14%] right-[14%] bottom-[58px] h-[125px] rounded-[50%] bg-red-300/65 border border-red-500 shadow-lg"></div>
  <div class="absolute left-[28%] right-[28%] bottom-[80px] h-[72px] rounded-[50%] bg-red-100/80 border border-red-400 shadow-lg"></div>

  <div class="absolute top-[22px] inset-x-0 text-[#6b2f1f] text-[22px] font-bold text-center">תכונות זמן לינארי</div>
  <div class="absolute top-[95px] inset-x-0 text-[#6b2f1f] text-[22px] font-bold text-center">תכונות בטיחות</div>
  <div class="absolute top-[135px] inset-x-0 text-[#6b2f1f] text-[21px] font-bold text-center">תכונות בטיחות רגולריות</div>
  <div class="absolute top-[184px] inset-x-0 text-[#6b2f1f] text-[21px] font-bold text-center">תכונות שמורה</div>
</div>

---

# תכונות חיות מול תכונות בטיחות

<div class="mt-10 text-right text-[30px] leading-relaxed">

- <span class="text-red-600 font-bold">תכונות בטיחות</span> מבטאות דרישה ש<span class="text-red-600 font-bold">"משהו רע לא יקרה"</span>.

- אפשר לעמוד בדרישה אם לא עושים כלום:

<div class="mx-auto my-4 w-[50%] bg-white shadow-md p-3 text-center text-[26px]">
"כך, אף פעם לא נגיע למצב רע"
</div>

- לכן נוסיף גם <span class="text-blue-700 font-bold">תכונות חַיּוּת</span> כדי לדרוש שתהיה <span class="text-blue-700 font-bold">"התקדמות"</span>.

- דרישות חיות אומרות:

<div class="mx-auto mt-4 w-[74%] bg-white shadow-md p-3 text-center text-[27px]" dir="rtl">
בסופו של דבר יקרה "משהו טוב" [Lamport 1977]
</div>

</div>

---

# המחשה

<div class="grid grid-cols-2 gap-10 mt-8 text-center">

<div>
  <div class="h-[230px] bg-white border border-slate-200 flex items-center justify-center">
    <div class="relative w-[78%] h-[150px]">
      <div class="absolute left-[5%] top-[55%] w-[34%] h-[44%] bg-red-600 rounded border-2 border-red-800"></div>
      <div class="absolute right-[5%] top-[18%] w-[56%] h-[72%] bg-stone-500 rounded border-4 border-stone-700"></div>
      <div class="absolute left-[20%] top-[35%] right-[25%] h-2 bg-red-500"></div>
    </div>
  </div>
  <div class="mt-5 text-blue-700 text-[28px]">תכונות בטיחות</div>
  <div class="mt-8 text-[27px]">"משהו רע לא יקרה"</div>
  <div class="mt-6 text-red-600 text-[29px] leading-snug">לא ניתן לתקן את<br/>הדבר הרע</div>
</div>

<div>
  <div class="h-[230px] bg-white border border-slate-200 flex items-center justify-center">
    <div class="relative w-[86%] h-[170px] bg-slate-100">
      <div class="absolute inset-0 grid grid-cols-4 grid-rows-3 gap-2 p-2">
        <div class="bg-slate-400"></div><div class="bg-slate-300"></div><div class="bg-slate-400"></div><div class="bg-slate-300"></div>
        <div class="bg-slate-300"></div><div class="bg-slate-400"></div><div class="bg-slate-300"></div><div class="bg-slate-400"></div>
        <div class="bg-slate-400"></div><div class="bg-slate-300"></div><div class="bg-slate-400"></div><div class="bg-slate-300"></div>
      </div>
      <div class="absolute left-[8%] top-[35%] w-[28%] h-[18%] bg-blue-700"></div>
      <div class="absolute right-[10%] top-[42%] w-[34%] h-[16%] bg-orange-500"></div>
    </div>
  </div>
  <div class="mt-5 text-blue-700 text-[28px]">תכונות חַיּוּת</div>
  <div class="mt-8 text-[27px]">"משהו טוב יקרה"</div>
  <div class="mt-6 text-red-600 text-[29px] leading-snug">תמיד יכול להיות<br/>שהדבר הטוב יקרה</div>
</div>

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
