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

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

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
$$P_{inv(\Phi)} = \left\{ \sigma \in (2^{AP})^\omega \;\middle|\; \forall j \ge 0 (\sigma[j] \models \Phi) \right\}$$

הנוסחה $\Phi$ נקראת **תנאי השמורה** (Invariant Condition).
</div>

לכן, מערכת מקיימת שמורה ($TS \models P_{inv(\Phi)}$) אם ורק אם התנאי $\Phi$ מתקיים ב**כל המצבים הנגישים** במערכת:
$$ \forall s \in \operatorname{Reach}(TS) (L(s) \models \Phi) $$

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

# איך מוכיחים שתכונה נתונה אינה תכונת שמורה?

<div class="text-right">

נבחן את התכונה הבאה מעל $AP = \{p, q\}$: **"כל המצבים במסלול חייבים להיות זהים למצב ההתחלתי"**.
פורמלית: $P = \{ \sigma \in (2^{AP})^\omega \mid \forall i \ge 0 (\sigma[i] = \sigma[0]) \}$.

<div class="bg-amber-50 border border-amber-200 rounded">

**הוכחה בשלילה:**
נניח בשלילה שקיימת נוסחה $\Phi$ המגדירה את $P$ כשמורה, כלומר $P = \{ \sigma \mid \forall i \ge 0 (\sigma[i] \models \Phi) \}$.

1. נסתכל על העקבה $\sigma = \{p\} \{p\} \{p\} \dots$. ברור ש-$\sigma \in P$ כיוון שכל המצבים זהים לראשון.
   לפי הנחת השלילה, כל המצבים ב-$\sigma$ מקיימים את $\Phi$, ובפרט המצב הראשון: **$\{p\} \models \Phi$**.

2. נסתכל על העקבה $\sigma' = \{q\} \{q\} \{q\} \dots$. גם כאן $\sigma' \in P$.
   לפי הנחת השלילה, כל המצבים ב-$\sigma'$ מקיימים את $\Phi$, ובפרט המצב הראשון: **$\{q\} \models \Phi$**.
3. כעת, נבנה עקבה חדשה $\tau = \{p\} \{q\} \{q\} \{q\} \dots$.
   ראינו ש-$\{p\} \models \Phi$ וגם $\{q\} \models \Phi$, ולכן **כל מצב ב-$\tau$ מקיים את $\Phi$**.
   לפי הנחת השלילה $P = Inv(\Phi)$, נובע ש-$\tau \in P$.
4. **סתירה:** לפי הגדרת $P$, כל המצבים ב-$\tau$ חייבים להיות זהים ל-$\tau[0]$.
   אך במקרה שלנו $\tau[1] = \{q\} \neq \{p\} = \tau[0]$.

**מסקנה:** לא קיימת נוסחה $\Phi$ המגדירה את $P$. התכונה $P$ תלויה ב*קשר* בין מצבים (היסטוריה) ולא רק בכל מצב בנפרד.
</div>

</div>

---

# איך מוכיחים שתכונה היא תכונת שמורה?

<div class="text-right">

נבחן את התכונה הבאה: **"הפסוק $p$ מתקיים במצב ההתחלתי, ואם הוא מתקיים בזמן מסוים הוא יתקיים גם בזמן הבא"**.
פורמלית: $P = \{ \sigma \in (2^{AP})^\omega \mid p \in \sigma[0] \land \forall i \ge 0 (p \in \sigma[i] \implies p \in \sigma[i+1]) \}$.

<div class="bg-green-50 border border-green-200 rounded p-4 mt-4">

נראה ש-$P = \{ \sigma \mid \forall i \ge 0 (p \in \sigma[i]) \}$.

**הוכחה (באינדוקציה על $i$):**
תהי $\sigma \in P$. נראה ש-$p \in \sigma[i]$ לכל $i \ge 0$:
1. **בסיס ($i=0$):** לפי הגדרת $P$, מתקיים $p \in \sigma[0]$.

2. **צעד האינדוקציה:** נניח ש-$p \in \sigma[i]$. לפי הגדרת $P$, מתקיים $p \in \sigma[i] \implies p \in \sigma[i+1]$.
   לכן, מהנחת האינדוקציה נובע ש-$p \in \sigma[i+1]$.

מכאן ש-$\forall i \ge 0 (p \in \sigma[i])$.
הכיוון ההפוך (אם $\forall i \ge 0 (p \in \sigma[i])$ אז $\sigma \in P$) הוא מיידי.

**מסקנה:** התכונה $P$ היא שמורה המוגדרת על ידי התנאי $\Phi = p$.
</div>

</div>

---

# דוגמה: חידת הכדורים

<div class="grid grid-cols-[1fr_.8fr] gap-8 mt-4 text-right items-center">

<div>

- בשק יש 2026 כדורים שחורים ו-2026 כדורים לבנים.
- בכל צעד מוציאים שני כדורים:
  - אם שניהם באותו הצבע מחזירים כדור לבן.
  - אם הם בצבעים שונים מחזירים כדור שחור.
- **השאלה:** מה צבע הכדור האחרון?

<div class="bg-blue-50 border border-blue-200 rounded p-4 text-[15px] mt-6">

**מידול כמערכת מעברים:**
- מצב: מילה $w \in \{B, W\}^*$
- התחלתי: מילה עם 2026 'B' ו-2026 'W'
- מעברים (בחירה מכל מקום, החזרה לראש):
  - $\{ u B v B w \to W u v w \mid u,v,w \in \{B,W\}^*\}$
  - $\{ u W v W w \to W u v w \mid u,v,w \in\{B,W\}^*\}$
  - $\{ u B v W w \to B u v w \mid u,v,w \in \{B,W\}^*\}$

</div>

</div>

<div class="flex justify-center">
  <img src="./images/balls_puzzle_student.png" class="rounded-3xl shadow-2xl border-4 border-white/50 w-full max-w-[400px]" />
</div>

</div>

---

# פתרון דרך שמורות

<div class="text-right">

<div class="bg-amber-50 border border-amber-200 rounded p-6 mt-3">
<div class="font-bold text-lg mb-4">
הבחנה על מספר הכדורים השחורים:
</div>

- בכל אחד מהמעברים (`BB`, `WW`, `BW`), מספר הכדורים השחורים או שנשאר ללא שינוי, או שקטן ב-2.

- **מסקנה:** הזוגיות (Parity) של מספר הכדורים השחורים היא **שמורה**!

</div>

<div class="mt-0">

- התחלנו עם 2026 כדורים שחורים (מספר זוגי).

- לכן, בכל מילה נגישה $w \in Reach(TS)$, מספר ה-'B' במילה חייב להיות זוגי.
- בסוף התהליך נשאר כדור אחד, כלומר המילה היא או `"B"` או `"W"`.
- כיוון שבמילה `"B"` יש מספר אי-זוגי של כדורים שחורים (1), מצב זה אינו נגיש.
- **מסקנה:** הכדור האחרון חייב להיות לבן.

</div>

</div>

---

# איך בודקים אם שמורה מתקיימת?

<div class="mt-2 text-right">

מכיוון ששמורה היא תנאי על מצבים, הבדיקה שלה שקולה ל**בדיקת נגישות** (Reachability Analysis).

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
class: text-right

---

# פסאודו-קוד: בדיקת שמורה

<div class="w-full scale-80 mt-2" dir="ltr" style="text-align: left;">

<div class="shiki-high-contrast">

```javascript
Algorithm CheckInvariant(TS, Φ)
  Visited = ∅
  Worklist = TS.I
  
  for each s in TS.I {
    if (s ⊭ Φ) return "Violation at initial state: " + s
    Visited.add(s)
  }
  
  while (Worklist is not empty) {
    s = Worklist.pop()
    for each s' in Post(s) {
      if (s' ∉ Visited) {
        if (s' ⊭ Φ) return "Violation at state: " + s'
        Visited.add(s')
        Worklist.push(s')
      }
    }
  }
  return "Invariant Holds"
```

</div>

</div>

<div class="-mt-4 text-right text-[14px]">

- **Worklist**: יכול להיות מחסנית (עבור DFS) או תור (עבור BFS).
- **Visited**: קבוצה השומרת את כל המצבים שכבר נסרקו כדי למנוע לולאות אינסופיות.
</div>

<style>
.shiki-high-contrast span {
  filter: brightness(0.8) saturate(2);
  font-weight: 500;
}
</style>

---

# מציאת דוגמה נגדית (Counterexample)

<div class="mt-8 text-right">

אם מצאנו מצב שבו השמורה מופרת, פשוט להחזיר "שקר" אינו מועיל מספיק. אנחנו רוצים להבין **למה** השמורה מופרת.

דוגמה נגדית עבור שמורה היא **מסלול סופי** במערכת:
$$ s_0 \to s_1 \to s_2 \to \dots \to s_n $$
כך ש:
1. $s_0 \in I$ (מצב התחלתי)
2. $\forall 0 \le i < n (L(s_i) \models \Phi)$
3. $L(s_n) \not\models \Phi$ (במצב האחרון השמורה מופרת)

<div class="bg-amber-50 border border-amber-200 rounded p-4 mt-4">
<div class="font-bold mb-2">הפקת הדוגמה הנגדית ב-DFS:</div>
כאשר משתמשים בחיפוש לעומק (DFS), תכולת המחסנית ברגע גילוי המצב הבעייתי מהווה בדיוק את המסלול מהמצב ההתחלתי אל אותו מצב (בסדר הפוך).
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

- **הגדרה:** תנאי פסוקי $\Phi$ שחייב להתקיים ב**כל מצב** נגיש במערכת.
- **היעדר תלות בהיסטוריה:** שמורה תלויה רק במצב הנוכחי. תכונות שתלויות בקשר בין מצבים (כמו "המצב הנוכחי זהה להתחלתי") אינן שמורות.
- **שיטות הוכחה:** ניתן להוכיח שתכונה היא שמורה בעזרת **אינדוקציה** על אורך המסלול, או להפריך זאת בעזרת דוגמה נגדית המראה תלות בעבר.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-6">
<div class="font-bold mb-4 text-blue-700 text-lg">אלגוריתמיקה ואימות</div>

- **בדיקת נגישות:** וידוא שמורות מתבצע באמצעות DFS או BFS על מרחב המצבים הנגישים.
- **סיבוכיות:** לינארית בגודל המערכת $O(N+M)$ ובקושי לבחון מצב בודד.
- **דוגמה נגדית:** אם שמורה מופרת, האלגוריתם מספק מסלול סופי מהמצב ההתחלתי אל מצב השגיאה.
- **המשך:** בהרצאה הבאה נדון בתכונות בטיחות כלליות (Safety).
</div>
</div>
