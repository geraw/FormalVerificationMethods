---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 10-invariant-properties
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## תכונות שמורה
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תכונות שמורה

## הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

---

# מהי שמורה?

<div class="mt-8 text-right">

חלק גדול מהתכונות שאנחנו רוצים לאמת במערכות מקביליות מתארות מצבים ש**אסור** שיתקיימו. 
תכונות אלו נקראות לעיתים קרובות תכונות בטיחות (Safety Properties), שהאינטואיציה מאחוריהן היא ש"שום דבר רע לעולם לא יקרה".

הסוג הפשוט והנפוץ ביותר של תכונות בטיחות הוא **שמורות (Invariants)**.

<div class="bg-blue-50 border border-blue-200 rounded p-4 mt-6">
<div class="font-bold mb-2">הרעיון המרכזי:</div>
שמורה היא תנאי על מצב המערכת, שצריך להיות תמיד נכון. היא תלויה אך ורק ב**מצב הנוכחי** של המערכת, ולא בהיסטוריה שלה או בסדר הפעולות.
</div>

</div>

---

# הגדרה פורמלית

<div class="mt-8 text-right">

כדי להגדיר שמורה באופן פורמלי בתור תכונת זמן לינארי (קבוצה של עקבות), נשתמש בלוגיקה פסוקית (Propositional Logic).

<div class="bg-slate-50 border border-slate-200 rounded p-4 mt-6">
<div class="font-bold mb-2 text-lg">הגדרה</div>

תהי $\Phi$ נוסחה בלוגיקה פסוקית מעל קבוצת הפסוקים האטומיים $AP$.
תכונת זמן לינארי $P_{inv(\Phi)}$ נקראת **שמורה** אם:
$$P_{inv(\Phi)} = \left\{ \sigma \in (2^{AP})^\omega \;\middle|\; (\forall j \ge 0) (\sigma[j] \models \Phi) \right\}$$

הנוסחה $\Phi$ נקראת **תנאי השמורה** (Invariant Condition).
</div>

לכן, מערכת מקיימת שמורה ($TS \models P_{inv(\Phi)}$) אם ורק אם התנאי $\Phi$ מתקיים ב**כל המצבים הנגישים** במערכת:
$$ (\forall s \in \operatorname{Reach}(TS)) (L(s) \models \Phi) $$

</div>

---

# פירוש של נוסחה על מצב יחיד

<div class="text-right">

כדי לקבוע אם מצב מקיים שמורה המוגדרת על ידי התנאי $\Phi$, אנו בודקים האם המצב הבודד $s$ מקיים את $\Phi$. 
הפירוש מסתמך על פונקציית התיוג $L(s)$, אשר מחזירה את קבוצת הפסוקים האטומיים שמתקיימים במצב $s$.

<div class="bg-blue-50 border border-blue-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-4">

יחס הסיפוק $s \models \Phi$ מוגדר בצורה רקורסיבית (אינדוקציה מבנית):
</div>

- **פסוק אטומי:** $s \models a \iff a \in L(s)$

- **שלילה (Not):** $s \models \neg \Phi \iff s \not\models \Phi$
- **וגם (And):** $s \models \Phi_1 \land \Phi_2 \iff s \models \Phi_1 \text{ וגם } s \models \Phi_2$
- **או (Or):** $s \models \Phi_1 \lor \Phi_2 \iff s \models \Phi_1 \text{ או } s \models \Phi_2$

</div>

</div>

<div class="bg-red-50 border border-red-200 rounded p-1">

אינטואיציה: פסוק אטומי מקבל ערך אמת אם ורק אם הוא ב-$L(s)$, וקשרים מפורשים כפי שלמדנו בקורסים קודמים

</div>

---

# דוגמאות לשמורות

<div class="mt-8 text-right">

### מניעה הדדית (Mutual Exclusion)
התכונה "תמיד לכל היותר תהליך אחד נמצא בקטע הקריטי".
התנאי הלוגי:
$$ \Phi = \neg crit_1 \lor \neg crit_2 $$

### חסינות לקיפאון (Deadlock Freedom) בדוגמת הפילוסופים
לפילוסופים הסועדים, קיפאון מתרחש כאשר כולם מחכים למקל השני (נמצאים במצב $wait$). 
תנאי השמורה לחסינות מקיפאון יבטיח שלפחות פילוסוף אחד *לא* ממתין:
$$ \Phi = \neg wait_0 \lor \neg wait_1 \lor \dots \lor \neg wait_4 $$

</div>

---

# דוגמה: חידת הכדורים

<div class="grid grid-cols-[1fr_.5fr] gap-8 mt-4 text-right">

<div>

- בשק יש 2026 כדורים שחורים ו-2026 כדורים לבנים.
- בכל צעד מוציאים שני כדורים:
  - אם הם בצבעים שונים מחזירים כדור שחור.
  - אם שניהם באותו הצבע מחזירים כדור לבן.
- **השאלה:** מה צבע הכדור האחרון?

</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4 text-[14px]">

**מידול ראשוני כמערכת מעברים:**
- מצב: מילה $w \in \{B, W\}^*$
- התחלתי: מילה עם 2026 'B' ו-2026 'W'
- מעברים (תת-מחרוזות):
  - $uBBv \to uWv$
  - $uWWv \to uWv$
  - $uBWv \to uBv$

**מידול מופשט (ספירת כדורים):**
מכיוון שסדר הכדורים אינו משנה, נעבור למצב $\langle b, w \rangle$:
- `BB`: $\langle b,w \rangle \to \langle b-2, w+1 \rangle$
- `WW`: $\langle b,w \rangle \to \langle b, w-1 \rangle$
- `BW`: $\langle b,w \rangle \to \langle b, w-1 \rangle$

</div>

</div>

---

# פתרון דרך שמורות

<div class="mt-8 text-right">

נחפש תכונה שנשמרת (Invariant) לאורך כל צעדי המערכת.

<div class="bg-amber-50 border border-amber-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-4">תצפית על מספר הכדורים השחורים ($b$):</div>

- בכל אחד מהמעברים (`BB`, `WW`, `BW`), מספר הכדורים השחורים או שנשאר ללא שינוי, או שקטן ב-2.
- **מסקנה:** הזוגיות (Parity) של מספר הכדורים השחורים היא **שמורה**!

</div>

<div class="mt-6">

- התחלנו עם 2026 כדורים שחורים (מספר זוגי).
- לכן, בכל מצב נגיש $\langle b, w \rangle \in Reach(TS)$, מספר הכדורים השחורים $b$ חייב להיות זוגי.
- בסוף התהליך נשאר כדור אחד (או $\langle 1, 0 \rangle$ או $\langle 0, 1 \rangle$).
- כיוון ש-1 הוא אי-זוגי, המצב $\langle 1, 0 \rangle$ אינו נגיש.
- **מסקנה סופית:** הכדור האחרון חייב להיות לבן.

</div>

</div>

---

# איך בודקים אם שמורה מתקיימת?

<div class="mt-8 text-right">

מכיוון ששמורה היא תנאי על מצבים, הבדיקה שלה שקולה ל**בדיקת נגישות** (Reachability Analysis) בגרף המצבים של המערכת.

<div class="bg-blue-50 border border-blue-200 rounded p-4 mt-6">
<div class="font-bold mb-2">אלגוריתם בסיסי: סריקת מצבים</div>

1. התחל מקבוצת המצבים ההתחלתיים $I$.
2. בצע סריקת עומק (DFS) או סריקת רוחב (BFS) על גרף המצבים.
3. עבור כל מצב $s$ שנצפה, בדוק האם $L(s) \models \Phi$.
4. אם כן - המשך. אם לא - השמורה **הופרה**.
5. אם הסריקה הסתיימה וכל המצבים הנגישים תקינים - השמורה **מתקיימת**.
</div>

זוהי סריקה *קדימה* (Forward Search). ניתן לבצע גם סריקה *אחורה* (Backward Search): להתחיל מהמצבים שבהם $\Phi$ אינו מתקיים, ולבדוק האם קיים מסלול הפוך המגיע למצב התחלתי.

</div>

---

# מציאת דוגמה נגדית (Counterexample)

<div class="mt-8 text-right">

אם מצאנו מצב שבו השמורה מופרת, פשוט להחזיר "שקר" אינו מועיל מספיק. אנחנו רוצים להבין **למה** השמורה מופרת.

דוגמה נגדית עבור שמורה היא **מסלול סופי** במערכת:
$$ s_0 \to s_1 \to s_2 \to \dots \to s_n $$
כך ש:
1. $s_0 \in I$ (מצב התחלתי)
2. $(\forall 0 \le i < n) (L(s_i) \models \Phi)$
3. $L(s_n) \not\models \Phi$ (במצב האחרון השמורה מופרת)

<div class="bg-amber-50 border border-amber-200 rounded p-4 mt-4">
<div class="font-bold mb-2">הפקת הדוגמה הנגדית ב-DFS:</div>
כאשר משתמשים בחיפוש לעומק (DFS), תכולת המחסנית ברגע גילוי המצב הבעייתי $s_n$ מהווה בדיוק את המסלול מהמצב ההתחלתי אל אותו מצב (בסדר הפוך).
</div>

</div>

---

# סיבוכיות זמן לבדיקת שמורות

<div class="mt-8 text-right">

מהי העלות החישובית של וידוא שמורות?

<div class="bg-green-50 border border-green-200 rounded p-6 mt-6">
<div class="font-bold text-lg mb-2 underline">משפט (סיבוכיות זמן)</div>

סיבוכיות הזמן של אלגוריתם בדיקת שמורות מבוסס DFS היא:
$$ O\bigl( N \cdot (1 + |\Phi|) + M \bigr) $$
</div>

כאשר:
- **$N$**: מספר המצבים הנגישים (Reachable states) במערכת.
- **$M$**: מספר המעברים (Transitions) בין המצבים הנגישים.
- **$|\Phi|$**: אורך הנוסחה הפסוקית $\Phi$ (מספר הפעולות). הבדיקה האם מצב מקיים את $\Phi$ לוקחת זמן $O(1 + |\Phi|)$.

לסיכום, הבדיקה היא **לינארית** בגודל החלק הנגיש של מודל המערכת.

</div>

---

# סיכום

<div class="grid grid-cols-2 gap-8 mt-10 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">שמורות (Invariants)</div>

- התכונות הלינאריות הפשוטות והנפוצות ביותר.
- מגדירות תנאי פסוקי שחייב להתקיים ב**כל מצב** נגיש במערכת.
- תלויות רק במצב הנוכחי, ולא בעבר או בעתיד.
- משמשות להוכחת מניעה הדדית, היעדר קיפאון, ותכונות בטיחות בסיסיות נוספות.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">אלגוריתמיקה</div>

- וידוא שמורות שקול לפתרון בעיית נגישות (Reachability) בגרף.
- ניתן לבצע ביעילות (זמן לינארי בגודל המרחב הנגיש) באמצעות DFS או BFS.
- מספק מיד דוגמה נגדית (Counterexample) המציגה את מסלול השגיאה.
- בהרצאה הבאה: תכונות בטיחות שאינן בהכרח שמורות.
</div>
</div>
