---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: true
download: true
exportFilename: 01-transition-systems
htmlAttrs:
    dir: rtl
    lang: heb
drawings:
  enabled: true
info: |
  ## מערכות מעברים (Transition Systems)
  מרצה: גרא וייס
---

# מערכות מעברים <br> (Transition Systems)

##  הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**<br>


<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/graphics/just-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# נושאי הקורס 

<div class="flex justify-center">
  <img src="/images/course_topics_diagram_v2_mine.png" class="h-110 w-140"  /> 
</div>
 
---

#  בדיקות מודל (Model Checking)
 

<div class="flex justify-center">
  <img src="/images/model-checking-4.png" class="h-110 w-180"  /> 
</div>


---

# מערכת מעברים – Transition System

בקורס זה נתאר מערכות תגובתיות באמצעות מודל מתמטי הנקרא "מערכות מעברים".

<div class="grid grid-cols-2 gap-8">

<div>

מערכת מעברים נתונה על-ידי $\langle S, Act, \to, I, AP, L \rangle$ באשר:

- $S$ היא קבוצת המצבים.

- $I \subseteq S$ היא קבוצת המצבים ההתחלתיים.
- $Act$ היא קבוצת הפעולות.
- $\to \subseteq S \times Act \times S$ הוא יחס המעברים.
- $AP$ היא קבוצת הפסוקים האטומיים.
- $L\colon S \to 2^{AP}$ היא פונקצית התיוג.

</div>

<div class="flex flex-col items-center justify-start -mt-30">

<TransitionSystemD3  
  :states="[
      { id: 's0', text: '$s_0$', label: '$\{p\}$', initial: true, x: 230, y: 270 },
      { id: 's1', text: '$s_1$', label: '$\{q\}$', x: 440, y: 270 },
      { id: 's2', text: '$s_2$', label: '$\{p,q\}$', x: 335, y: 140 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$\\alpha$' },
    { source: 's1', target: 's2', action: '$\\beta$' },
    { source: 's2', target: 's0', action: '$\\gamma$' },
    { source: 's2', target: 's2', action: '$\\delta$' }
  ]"
/>

<div dir="ltr" class="text-xs text-center -mt-16">

$S = \{s_0, s_1, s_2\}$, $\mathit{Act} = \{\alpha, \beta, \gamma, \delta\}$, $I = \{s_0\}$, $\mathit{AP} = \{p, q\}$

$\to = \{\langle s_0, \alpha, s_1 \rangle, \langle s_1, \beta, s_2 \rangle, \langle s_2, \gamma, s_0 \rangle, \langle s_2, \delta, s_2 \rangle\}$

$L(s_0) = \{p\}, L(s_1) = \{q\}, L(s_2) = \{p,q\}$

</div>

</div>

</div>




---

# התנהגות אינטואיטיבית ואי-דטרמיניזם

לשם נוחות, נסמן $s \xrightarrow{\alpha} s'$ במקום $\langle s, \alpha, s' \rangle \in\ \to$. 

ההתנהגות של מערכת מעברים מתוארת באופן הבא:

* המערכת מתחילה במצב התחלתי כלשהו $s_0 \in I$ ומתפתחת על פי יחס המעברים $\to$.
  
* בכל שלב, אם $s$ הוא המצב הנוכחי, מעבר יוצא $s \xrightarrow{\alpha} s'$ נבחר באופן אי-דטרמיניסטי ומבוצע.
  כלומר, הפעולה $\alpha$ מתבצעת והמערכת עוברת מ-$s$ למצב $s'$.
* תהליך זה חוזר על עצמו במצב $s'$, ומסתיים רק כאשר נתקלים במצב שאין ממנו מעברים יוצאים.

<div class="mt-8 p-4 bg-blue-50 text-base rounded shadow border-l-4 border-blue-500" dir="rtl">

<b>אי-דטרמיניזם, לא הסתברות:</b> <br/>
חשוב להבין שבמקרה שלמצב יש יותר ממעבר יוצא אחד, המעבר הבא נבחר באופן <b>אי-דטרמיניסטי טהור</b>.
כלומר, תוצאת הבחירה אינה ידועה מראש, ולכן <b>לא ניתן להביע שום טענה על ההסתברות או הסבירות שמעבר מסוים ייבחר</b>.<br>
באופן דומה, כאשר קבוצת המצבים ההתחלתיים כוללת יותר ממצב אחד, מצב הפתיחה נבחר אי-דטרמיניסטית.

</div>

---

# פונקציית התיוג (Labeling Function)

פונקציית התיוג $L \colon S \to 2^{AP}$ מקשרת בין קבוצת פסוקים אטומיים $L(s) \in 2^{AP}$ לכל מצב $s \in S$. 

באופן אינטואיטיבי, $L(s)$ מייצגת בדיוק את אותם פסוקים אטומיים $a \in AP$ שמתקיימים במצב $s$.

* בהינתן ש-$\Phi$ היא נוסחת לוגיקה פסוקית, נאמר ש-$s$ מקיים את הנוסחה $\Phi$ אם ההשמה שמושרה על ידי הקבוצה $L(s)$ הופכת את הנוסחה לאמיתית. 

* כלומר, נסמן:
$$ s \models \Phi \quad \text{iff} \quad L(s) \models \Phi $$   

* **השמה שמושרה על ידי קבוצה:** כל פסוק מקבל ערך True אם הוא שייך לקבוצה, ו-False אם הוא לא שייך לקבוצה.

<div class="mt-8 p-4 bg-yellow-100 rounded text-center">


<b>משמעות:</b> פונקציית התיוג מעניקה לשמות המצבים את המשמעות מנקודת המבט של התכונות שניתן להביע על המערכת. היא הופכת את מצבי המערכת מ"סתם משתנים" לייצוג לוגי הניתן לאימות.

</div>


---

# דוגמה: רובוט במבוך

נניח רובוט שנע בתוך מבוך המיוצג כרשת משבצות $4 \times 4$.
המצבים של המערכת הם הקואורדינטות של הרובוט: $S = \{ \langle i,j \rangle \mid 1 \le i \le 4, 1 \le j \le 4 \}$.
פעולות המעבר האפשריות הן תזוזה לאחת מארבעת הכיוונים (למשבצות פנויות בלבד).

נגדיר שני פסוקים אטומיים: $AP = \{\text{TH}, \text{EH}\}$.   (קיצור של- **T**op**H**alf, **R**ight**H**alf)

פונקציית התיוג $L$ מתרגמת את המטריקה של הרשת לתכונות לוגיות פשוטות :
- רובוט נמצא בחצי העליון של הרשת: $\text{TH} \in L(\langle i,j \rangle) \iff j \ge 3$
- רובוט נמצא בחצי הימני של הרשת: $\text{RH} \in L(\langle i,j \rangle) \iff i \ge 3$

<div class="grid grid-cols-2 gap-0 mt-6">
<div>

* **לדוגמה:**
  - $L(\langle 4,4 \rangle) = \{\text{TH}, \text{RH}\}$

  - $L(\langle 1,1 \rangle) = \emptyset$
  - $L(\langle 3,1 \rangle) = \{\text{RH}\}$

</div>
<div>

* **אימות תכונות:**
  - ניתן לשאול: <br/>
    <span class="text-sm">האם אפשר להגיע ל-$s \models\text{TH} {\land} \text{RH}$ מבלי לעבור ב-$s \models \neg\text{RH}$?</span>
  - הפרדה בין האימות למבנה הפנימי של המערכת
</div>
</div>

---

# דוגמה: מסלול במבוך

נבחן שני מסלולים אפשריים במערכת המעברים של הרובוט מרגע ההתחלה $\langle 3,1 \rangle$.
המטרה: **להגיע ל-$TH \land RH$ (כלומר $i \ge 3, j \ge 3$) מבלי לצאת מה-$RH$ ($i \ge 3$)**.

<div class="grid grid-cols-2 gap-4 mt-4">
<div>

<div class="bg-green-100 p-2 rounded text-center mb-2 text-sm font-bold border border-green-400">
✅ מסלול עומד בדרישה
</div>

<TransitionSystemD3  
  :width="400" :height="200"
  :states="[
    { id: 's0', text: '$\\langle 3,1 \\rangle$', label: '$\\{RH\\}$', initial: true, initialDirection: 'right', x: 200, y: 180 },
    { id: 's1', text: '$\\langle 3,2 \\rangle$', label: '$\\{RH\\}$', x: 200, y: 90 },
    { id: 's2', text: '$\\langle 3,3 \\rangle$', label: '$\\{TH, RH\\}$', x: 200, y: 0 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$Up$' },
    { source: 's1', target: 's2', action: '$Up$' }
  ]"
/>

<div class="text-xs text-center mt-2" dir="ltr">

$L: \{RH\} \to \{RH\} \to \{TH,RH\}$

</div>
<div class="text-sm text-center mt-1">
הרובוט נע צפונה פעמיים, נשאר בחצי הימני כל הדרך עד למטרה.
</div>

</div>
<div>

<div class="bg-red-100 p-2 rounded text-center mb-2 text-sm font-bold border border-red-400">
❌ מסלול אינו עומד בדרישה
</div>

<TransitionSystemD3  
  :width="400" :height="200" 
  :states="[
    { id: 's0', text: '$\\langle 3,1 \\rangle$', label: '$\\{RH\\}$', initial: true, initialDirection: 'right',  x: 280, y: 180 },
    { id: 's1', text: '$\\langle 2,1 \\rangle$', label: '$\\emptyset$', x: 120, y: 180 },
    { id: 's2', text: '$\\langle 2,2 \\rangle$', label: '$\\emptyset$', x: 120, y: 90 },
    { id: 's3', text: '$\\langle 2,3 \\rangle$', label: '$\\{TH\\}$', x: 120, y: 0 },
    { id: 's4', text: '$\\langle 3,3 \\rangle$', label: '$\\{TH, RH\\}$', x: 280, y: 0 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: '$Left$' },
    { source: 's1', target: 's2', action: '$Up$' },
    { source: 's2', target: 's3', action: '$Up$' },
    { source: 's3', target: 's4', action: '$Right$' }
  ]"
/>

<div class="text-xs text-center mt-2" dir="ltr">

$L: \{RH\} \to \emptyset \to \emptyset \to \{TH\} \to \{TH,RH\}$

</div>
<div class="text-sm text-center mt-1">
הרובוט עוקף מכשול דרך החצי השמאלי, תוך הפרת הדרישה.
</div>

</div>
</div>


---

# התייחסות למרכיבים $Act$ ו-$AP$ בפועל

למרות שההגדרה הפורמלית של מערכת מעברים דורשת קביעה של קבוצת הפעולות $Act$ וקבוצת הפסוקים האטומיים $AP$, בהמשך נתייחס לרכיבים אלו בגמישות רבה יותר:

* **פעולות ($Act$):** נחוצות בעיקר למידול מנגנוני תקשורת (כפי שנראה בהמשך). במקרים שבהם שמות הפעולות אינם רלוונטיים (למשל, כאשר המעבר מייצג פעילות פנימית של תהליך), נשתמש בסמל מיוחד $\tau$ או שפשוט נשמיט לחלוטין את תווית הפעולה.

* **פסוקים אטומיים ($AP$):** קבוצת הפסוקים האטומיים $AP$ נבחרת תמיד בהתאם לתכונות שמעניינות אותנו. כאשר משרטטים מערכות מעברים, לעיתים קרובות קבוצת $AP$ לא מצוינת במפורש. במקרים אלו, נהוג להניח ש-$AP \subseteq S$ (כלומר, הפסוקים הם פשוט קבוצת מצבים מיוחדים) ופונקציית התיוג היא פשוט $L(s) = \{ s \} \cap AP$.

---

# חשיבות האי-דטרמיניזם במערכות מעברים

<div class="grid grid-cols-[1fr_.6fr] gap-8 mt-4">

<div>

אי-דטרמיניזם מאפשר לנו לייצג:

* **שזירה**
  - סדרי ריצה שונים של תהליכים מקבילים.

* **קונפליקט**
  - תחרות על משאב משותף.

* **הפשטה וחופש מימוש**
  - כמה חלופות אפשריות באותו מודל.
  - ההכרעה נדחית לשלבי התכנון הבאים.

* **סביבה לא צפויה**
  - משתמש, קלט או תנאי שטח משתנים.

</div>



<div class="flex items-center justify-center">
  <img src="/images/nondeterminism_uses.png" class="rounded-xl shadow-2xl border border-white/10" />
</div>


</div>

---

# קבוצות קודמים ועוקבים ישירים 

<img src="/predecessors_successors_comic.png" class="absolute right-95 bottom-2 w-55" />

תהי $TS = \langle S, Act, \to, I, AP, L \rangle$ מערכת מעברים. עבור מצב $s \in S$ ופעולה $\alpha \in Act$:

<div class="grid grid-cols-2 gap-4 mt-4">

<div>

* **קבוצת העוקבים הישירים של $s$ ב-$\alpha$:**
  $$Post(s, \alpha) = \{s' \in S \mid s \xrightarrow{\alpha} s' \}$$

* **עוקבים ישירים (לכל הפעולות):**
  $$Post(s) = \bigcup_{\alpha \in Act} Post(s, \alpha)$$

</div>
<div>

* **קבוצת הקודמים הישירים של $s$ ב-$\alpha$:**
  $$Pre(s, \alpha) = \{s' \in S \mid s' \xrightarrow{\alpha} s\}$$

* **קודמים ישירים (לכל הפעולות):**
  $$Pre(s) = \bigcup_{\alpha \in Act} Pre(s, \alpha)$$

</div>

</div>


---

# הרחבה לקבוצות

<img src="/pointwise_extension_comic.png" class="absolute right-95 bottom-2 w-55" />

תהי $TS = \langle S, Act, \to, I, AP, L \rangle$ מערכת מעברים. עבור קבוצת מצבים $C \subseteq S$ ופעולה $\alpha \in Act$:

<div class="grid grid-cols-2 gap-4 mt-4">

<div>

* **עוקבים לקבוצה (עבור פעולה $\alpha$):** 
  $$Post(C, \alpha) = \bigcup_{s \in C} Post(s, \alpha)$$

* **עוקבים לקבוצה (לכל הפעולות):** 
  $$Post(C) = \bigcup_{s \in C} Post(s)$$

</div>
<div>

* **קודמים לקבוצה (עבור פעולה $\alpha$):** 
  $$Pre(C, \alpha) = \bigcup_{s \in C} Pre(s, \alpha)$$

* **קודמים לקבוצה (לכל הפעולות):** 
  $$Pre(C) = \bigcup_{s \in C} Pre(s)$$

</div>

</div>

---

# מצבים סופניים (Terminal States)

<img src="/terminal_states_comic.png" class="absolute right-95 bottom-0 w-55" />

מצבים סופניים במערכת מעברים הם מצבים ללא מעברים יוצאים. כשהמערכת מגיעה למצב סופני, פעולתה נעצרת לחלוטין.

<div class="border-2 border-blue-400 bg-blue-50 rounded-lg p-3 my-3" dir="rtl" align="center">

**הגדרה:** מצב $s$ במערכת מעברים $TS$ נקרא **סופני** אם ורק אם $Post(s) = \emptyset$.

</div>

* **תוכניות סדרתיות:** מצבים סופניים הם תופעה טבעית המייצגת את סיום ריצת התוכנית.

* **מערכות מקבילות:** מצבים סופניים נחשבים בדרך כלל ל**בלתי רצויים** (Deadlock), כפי שנראה בהמשך.




---

# מערכות מעברים דטרמיניסטיות

למרות שהאי-דטרמיניזם חיוני למידול מערכות מחשב, לעיתים שימושי להתייחס למערכות מעברים שבהן ההתנהגות ה"נצפית" היא דטרמיניסטית.

קיימות שתי גישות לפורמליזציה של ההתנהגות הנראית:

* **גישה מבוססת פעולות (Action-based):** רק הפעולות המבוצעות נצפות מבחוץ. דטרמיניזם מחייב שלכל מצב $s$ ופעולה $\alpha$ יהיה **לכל היותר** מעבר יוצא אחד המתויג ב-$\alpha$.

* **גישה מבוססת תיוגים (Label-based):** הפעולות נסתרות, ורק הפסוקים האטומיים המתקיימים במצב הנוכחי נראים. דטרמיניזם מחייב שלכל מצב $s$ ותיוג $A \in 2^{AP}$ יהיה **לכל היותר** מעבר יוצא אחד למצב עם תיוג $A$.

בשני המקרים, נדרש שיהיה **לכל היותר מצב התחלתי אחד**.

---

# הגדרה: מערכת מעברים דטרמיניסטית

<img src="/deterministic_observers.png" class="absolute right-95 bottom-5 w-55" />

תהי $TS = \langle S, Act, \to, I, AP, L \rangle$ מערכת מעברים.

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="border-2 border-green-400 bg-green-50 rounded-lg p-3" dir="rtl" align="center">

**דטרמיניסטית על פי פעולות**

$|I| \le 1$ וגם <br> <br> $|Post(s, \alpha)| \le 1$ <br><br>

לכל מצב $s$ ופעולה $\alpha$

</div>

</div>
<div>

<div class="border-2 border-purple-400 bg-purple-50 rounded-lg p-3" dir="rtl" align="center">

**דטרמיניסטית על פי תיוגים**

$|I| \le 1$ וגם <br> <br> $|Post(s) \cap \{ s' \in S \mid L(s') = A \}| \le 1$ <br><br>

לכל מצב $s$ ו-$A \in 2^{AP}$

</div>

</div>

</div>

---

# מקטעי ריצה (Execution Fragments)

עד כה תיארנו את התנהגות מערכת המעברים באופן אינטואיטיבי. כעת נפרמל זאת באמצעות המושג **ריצה** (execution/run). ריצה נוצרת מתוך הכרעת האי-דטרמיניזם האפשרי במערכת, ומתארת התנהגות אפשרית אחת.

תהי $TS = \langle S, Act, \to, I, AP, L \rangle$ מערכת מעברים.

* **מקטע ריצה סופי:** רצף מתחלף של מצבים ופעולות המסתיים במצב:
  $$\varrho = s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} \dots \xrightarrow{\alpha_n} s_n$$
  כך ש- $s_i \xrightarrow{\alpha_{i+1}} s_{i+1}$ לכל $0 \le i < n$. **האורך** של מקטע זה הוא $n$.

* **מקטע ריצה אינסופי:** רצף אינסופי של מצבים ופעולות:
  $$\rho = s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} s_2 \xrightarrow{\alpha_3} \dots$$
  כך ש- $s_i \xrightarrow{\alpha_{i+1}} s_{i+1}$ לכל $i \ge 0$.

<img src="/execution_fragment_comic.png" class="absolute left-10 bottom-10 w-55" />

---

# הערות על מקטעי ריצה

* הרצף $s$ (מצב בודד) הוא מקטע ריצה סופי חוקי באורך $n=0$.

* כל רישא באורך אי-זוגי של מקטע ריצה אינסופי היא מקטע ריצה סופי.

* מעתה, המונח **"מקטע ריצה"** יתייחס הן למקטע סופי והן לאינסופי.

<img src="/execution_notes_comic.png" class="absolute right-90 bottom-2 w-70" />

---

# מקטעי ריצה מקסימליים והתחלתיים

<img v-click-hide src="/maximal_initial_fragments.png" class="absolute right-95 bottom-0 w-45" />

מקטע ריצה נקרא **מקסימלי** כאשר לא ניתן להאריך אותו, ו**התחלתי** כאשר הוא מתחיל ממצב התחלתי:

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<div class="border-2 border-green-400 bg-green-50 rounded-lg p-3" dir="rtl" align="center">

**מקטע ריצה מקסימלי**

מקטע ריצה **סופי** המסתיים במצב **סופני**, <br> או מקטע ריצה **אינסופי**.

</div>

</div>
<div>

<div class="border-2 border-blue-400 bg-blue-50 rounded-lg p-3" dir="rtl" align="center">

**מקטע ריצה התחלתי**

מקטע ריצה שמתחיל במצב התחלתי, <br> כלומר $s_0 \in I$.

</div>

</div>

</div>

<div class="border-2 border-red-400 bg-red-50 rounded-lg p-3 mt-3 " dir="rtl" align="center">

**ריצה (Execution):** מקטע ריצה שהוא גם **התחלתי** וגם **מקסימלי**.

</div>

<div v-click="1" class="mt-3 border-2 border-yellow-400 bg-yellow-50 rounded-lg p-3">

**שאלה לבחינת הריכוז:** מה צריך להניח על המערכת כדי שלכל רצף תיוגים   $\sigma \in (2^{AP})^*$
תהיה לכל היותר ריצה אחת
$r = s_0 \xrightarrow{\alpha_1} s_1 \cdots \xrightarrow{\alpha_n} s_n$
שעבורה $L(s_i) = \sigma[i]$ לכל $i$? 
( אנחנו מסמנים את האות ה-$i$ של $\sigma$ ב-$\sigma[i]$ )


</div>

---

# מצבים נגישים (Reachable States)

מצב $s$ נקרא **נגיש** אם קיים מקטע ריצה סופי המתחיל במצב התחלתי ומסתיים ב-$s$.

<div class="border-2 border-blue-400 bg-blue-50 rounded-lg p-3 my-3" dir="rtl" align="center">

**הגדרה:** מצב $s \in S$ נקרא **נגיש** ב-$TS$ אם קיים מקטע ריצה התחלתי סופי:

$$s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} \dots \xrightarrow{\alpha_n} s_n = s$$

הקבוצה $Reach(TS)$ מציינת את **קבוצת כל המצבים הנגישים** ב-$TS$.

</div>

---

# דוגמה: חידת כדורים

<div class="grid grid-cols-[1fr_.5fr] gap-8 mt-4">


<div>

- בשק יש 2026 כדורים שחורים ו-2026 כדורים לבנים.

  - בכל צעד מוציאים שני כדורים:
  - אם הם בצבעים שונים מחזירים כדור שחור
  - אם שניהם באותו הצבע מחזירים כדור לבן
- השאלה: מה צבע הכדור האחרון שישאר בשק? <br>
 (בכל צעד יש כדור אחד פחות, בסוף ישאר רק אחד)

נמדל כמערכת מעברים:

- מצב: $\langle b,w \rangle$
- פירוש: $b$ = מספר הכדורים השחורים, $w$ = מספר הכדורים הלבנים
- מצב התחלתי: $\langle 2026,2026 \rangle$
- מצבי סיום: $\langle 1,0 \rangle$ או $\langle 0,1 \rangle$

</div>

<div class="flex flex-col items-center justify-center">
  <img src="/images/balls_puzzle_student.png" class="rounded-xl shadow-2xl border border-white/10 w-90" />
</div>


</div> 

---

# פתרון דרך $Reach(TS)$

- `BB`: $\langle b,w \rangle \xrightarrow{BB} \langle b-2,w+1 \rangle$
- `WW`: $\langle b,w \rangle \xrightarrow{WW} \langle b,w-1 \rangle$
- `BW`: $\langle b,w \rangle \xrightarrow{BW} \langle b,w-1 \rangle$

הבחנה על המצבים הנגישים:

- בכל מעבר מספר הכדורים השחורים נשאר זוגי.
- לכן לכל $\langle b,w \rangle \in Reach(TS)$ מתקיים: $b$ זוגי.
- בפרט, $\langle 1,0 \rangle \notin Reach(TS)$.

מסקנה:

- מצב הסיום הנגיש היחיד הוא $\langle 0,1 \rangle$.
- לכן הכדור האחרון הוא לבן.

---

# שקילות מערכות מעברים

<!-- <div class="rounded-lg border border-slate-300 bg-slate-50 p-3 text-right text-[12px] leading-snug"> -->
<div class="rounded-lg border border-slate-300 bg-slate-50 p-2 text-right text-[12px] leading-tight">

תהי $TS = \langle S, Act, \to, I, AP, L \rangle$ ו-
$\rho = s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} s_2 \xrightarrow{\alpha_3} \cdots$
ריצה שלה. נגידר:
$$
\mathrm{Traces}(TS)=\{\,\mathrm{trace}(\rho)\mid \rho \text{ היא ריצה של } TS\,\}.

\hspace{1cm}
\text{וגם} 
\hspace{1cm}

\mathrm{trace}(\rho)=L(s_0)L(s_1)L(s_2)\cdots \in (2^{AP})^* \cup (2^{AP})^\omega
$$

עבור שתי מערכות מעברים מעל אותה קבוצת פסוקים אטומיים נגדיר:
$TS_1 \equiv_{\mathrm{tr}} TS_2 \iff \mathrm{Traces}(TS_1)=\mathrm{Traces}(TS_2)\hspace{1cm}$.

</div>

<div class="grid grid-cols-2 gap-4 -mt-4 scale-75">
  <div class="rounded-lg border-2 border-blue-200 bg-blue-50 p-3">
    <div class="text-sm font-bold mb-2 text-center">מערכת <span dir="ltr">TS_1</span></div>
    <div class="flex justify-center">
      <TransitionSystemD3
        :width="300" :height="150"
        :states="[
          { id: 's0', text: '$s_0$', label: '$\\{p\\}$', initial: true, x: 50, y: 75 },
          { id: 's1', text: '$s_1$', label: '$\\{q\\}$', x: 250, y: 75 }
        ]"
        :transitions="[
          { source: 's0', target: 's1', action: '$\\alpha$' }
        ]"
      />
    </div>
  </div>
  <div class="rounded-lg border-2 border-emerald-200 bg-emerald-50 p-3">
    <div class="text-sm font-bold mb-2 text-center">מערכת <span dir="ltr">TS_2</span> (שקולה)</div>
    <div class="flex justify-center">
      <TransitionSystemD3
        :width="300" :height="150"
        :states="[
          { id: 'q0', text: '$q_0$', label: '$\\{p\\}$', initial: true, x: 50, y: 75 },
          { id: 'q1', text: '$q_1$', label: '$\\{q\\}$', x: 250, y: 30 },
          { id: 'q2', text: '$q_2$', label: '$\\{q\\}$', x: 250, y: 120 }
        ]"
        :transitions="[
          { source: 'q0', target: 'q1', action: '$\\alpha$' },
          { source: 'q0', target: 'q2', action: '$\\alpha$' }
        ]"
      />
    </div>
  </div>
</div>

<div class="rounded-lg border border-slate-300 bg-slate-50 p-2 text-center text-[12px] leading-tight">

  בדוגמה הזו:
  $\mathrm{Traces}(TS_1)=\mathrm{Traces}(TS_2)=\{\langle \{p\}, \{q\} \rangle\}$.
</div>


---

# שאלת ריכוז: מי שקולה למקור?

הגדרנו ששקילות נבחנת לפי $\mathrm{Traces}(TS)$, כלומר לפי **סדרות התיוגים של הריצות**.

איזו מן המערכות `B` או `C` שקולה למערכת `A`? <br>
האם אפשר להחליף את `A` במערכת קטנה יותר בלי שצופה חיצוני ירגיש?

<div class="grid grid-cols-3 gap-10 -mt-10 scale-70">

<div class="border-2 border-blue-300 bg-blue-50 rounded-lg p-2">

<div class="font-bold text-lg mb-1">A</div>

<TransitionSystemD3
  :width="250" :height="220" 
  :states="[
    { id: 'a0', text: '$s_0$', label: '$\\{p\\}$', initial: true, x: 125, y: 175 },
    { id: 'a1', text: '$s_1$', label: '$\\{q\\}$', x: 65, y: 100 },
    { id: 'a2', text: '$s_2$', label: '$\\{q\\}$', x: 185, y: 100 },
    { id: 'a3', text: '$s_3$', label: '$\\{r\\}$', x: 65, y: 25 },
    { id: 'a4', text: '$s_4$', label: '$\\{r\\}$', x: 185, y: 25 }
  ]"
  :transitions="[
    { source: 'a0', target: 'a1' },
    { source: 'a0', target: 'a2' },
    { source: 'a1', target: 'a3' },
    { source: 'a2', target: 'a4' },
    { source: 'a1', target: 'a2' },
    { source: 'a2', target: 'a1' },
    { source: 'a3', target: 'a3', loopDirection: '180deg' },
    { source: 'a4', target: 'a4', loopDirection: '180deg' }
  ]"
/>

</div>

<div class="border-2 border-green-300 bg-green-50 rounded-lg p-2 ">

<div class="font-bold text-lg mb-1">B</div>

<TransitionSystemD3
  :width="250" :height="220" 
  :states="[
    { id: 'b0', text: '$t_0$', label: '$\\{p\\}$', initial: true, x: 125, y: 175 },
    { id: 'b1', text: '$t_1$', label: '$\\{q\\}$', x: 125, y: 100 },
    { id: 'b2', text: '$t_2$', label: '$\\{r\\}$', x: 125, y: 25 }
  ]"
  :transitions="[
    { source: 'b0', target: 'b1' },
    { source: 'b1', target: 'b2' },
    { source: 'b2', target: 'b2', loopDirection: '180deg' }
  ]"
/>

</div>

<div class="border-2 border-red-300 bg-red-50 rounded-lg p-2">

<div class="font-bold text-lg mb-1">C</div>

<TransitionSystemD3
  :width="250" :height="220" 
  :states="[
    { id: 'c0', text: '$u_0$', label: '$\\{p\\}$', initial: true, x: 125, y: 175, initialDirection: '180deg' },
    { id: 'c1', text: '$u_1$', label: '$\\{q\\}$', x: 125, y: 100 },
    { id: 'c2', text: '$u_2$', label: '$\\{r\\}$', x: 125, y: 25 }
  ]"
  :transitions="[
    { source: 'c0', target: 'c1' },
    { source: 'c1', target: 'c1', loopDirection: '180deg' },
    { source: 'c1', target: 'c2' },
    { source: 'c2', target: 'c2', loopDirection: '180deg' }
  ]"
/>

</div>

</div>

<div v-click="1" class="-mt-8 text-sm bg-blue-50 p-2 rounded border border-blue-200">
רמז: ב-<b>A</b> יש שני מצבי <code>q</code> ושני מצבי <code>r</code> שנראים אותו דבר לצופה החיצוני.
</div>

<div v-click="2" class="mt-2 text-sm p-2 rounded border border-red-300 bg-red-50">
פתרון: <b>C</b> שקולה ל-<b>A</b>. לעומת זאת <b>B</b> אינה שקולה, כי היא מחייבת מעבר ל-<code>r</code> מיד אחרי צעד אחד ב-<code>q</code>, בעוד שב-<b>A</b> (וב-<b>C</b>) ניתן להישאר ב-<code>q</code> מספר צעדים כרצוננו (או לנצח).
</div>

---

# חידה נוספת: פרשי המלך

<div class="grid grid-cols-3 gap-4 mt-4 items-start">

<div class="bg-slate-50 border-2 border-slate-200 rounded-lg p-3">
<div class="font-bold text-center mb-2">התחלה</div>
<div class="grid grid-cols-3 w-48 mx-auto overflow-hidden rounded border border-slate-400 text-center text-lg font-bold">
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">a3</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-white border-2 border-slate-400 shadow-sm text-[28px] leading-none text-slate-800" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♘</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">b3</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">c3</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-white border-2 border-slate-400 shadow-sm text-[28px] leading-none text-slate-800" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♘</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">a2</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">b2</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">c2</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">a1</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-300 shadow-sm text-[28px] leading-none text-white" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♞</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">b1</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">c1</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-300 shadow-sm text-[28px] leading-none text-white" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♞</span></div>
</div>
</div>

<div class="bg-slate-50 border-2 border-slate-200 rounded-lg p-3">
<div class="font-bold text-center mb-2">מטרה</div>
<div class="grid grid-cols-3 w-48 mx-auto overflow-hidden rounded border border-slate-400 text-center text-lg font-bold">
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">a3</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-300 shadow-sm text-[28px] leading-none text-white" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♞</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">b3</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">c3</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-300 shadow-sm text-[28px] leading-none text-white" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♞</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">a2</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">b2</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">c2</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">a1</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-white border-2 border-slate-400 shadow-sm text-[28px] leading-none text-slate-800" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♘</span></div>
  <div class="relative h-14 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">b1</span><span class="text-slate-400">·</span></div>
  <div class="relative h-14 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[10px] text-slate-500 font-normal">c1</span><span class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-white border-2 border-slate-400 shadow-sm text-[28px] leading-none text-slate-800" style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;">♘</span></div>
</div>
</div>

<div class="bg-blue-50 border-2 border-blue-200 rounded-lg p-4 text-sm leading-6">
<div class="font-bold text-base mb-2">השאלה</div>
<ul class="list-disc ps-5">
  <li>פרש נע ב-<code>L</code> כרגיל.</li>
  <li>אסור לשני פרשים לעמוד על אותה משבצת.</li>
  <li>האם ההחלפה אפשרית?</li>
  <li>אם כן, מהו מספר הצעדים המינימלי?</li>
</ul>
</div>

</div>

<div v-click="1" class="mt-4 text-sm bg-yellow-50 p-2 rounded border border-yellow-200">
רמז: בנו מערכת מעברים שבה המצבים הם משבצות הלוח, והמעברים הם מהלכי פרש חוקיים.
</div>

---

# פתרון: מחליפים לוח במעגל

<div class="grid grid-cols-[0.92fr_1.05fr_0.95fr] gap-3 mt-2 items-start text-[12px] leading-5">

<div class="bg-sky-50 border-2 border-sky-200 rounded-lg p-3">
<div class="font-bold text-[14px] mb-1">1. ממספרים את הלוח</div>
<div class="text-[12px]">המשבצת <code>b2</code> מבודדת, ושאר 8 המשבצות מקבלות מספרים.</div>

<div class="grid grid-cols-3 w-44 mx-auto mt-2 overflow-hidden rounded border border-sky-300 text-center">
  <div class="relative h-12 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">a3</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">7</span></div>
  <div class="relative h-12 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">b3</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">2</span></div>
  <div class="relative h-12 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">c3</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">5</span></div>
  <div class="relative h-12 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">a2</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">4</span></div>
  <div class="relative h-12 bg-amber-100 border border-slate-300 flex flex-col items-center justify-center text-[9px] text-slate-500"><span class="absolute left-1 top-1 text-[9px] text-slate-500">b2</span><span class="font-bold">מבודדת</span></div>
  <div class="relative h-12 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">c2</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">8</span></div>
  <div class="relative h-12 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">a1</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">1</span></div>
  <div class="relative h-12 bg-stone-200 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">b1</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">6</span></div>
  <div class="relative h-12 bg-amber-100 border border-slate-300 flex items-center justify-center"><span class="absolute left-1 top-1 text-[9px] text-slate-500">c1</span><span class="inline-flex items-center justify-center w-7 h-7 rounded-full bg-sky-600 text-white font-bold text-[12px]">3</span></div>
</div>

<div v-click="1" class="mt-2 bg-white border border-sky-200 rounded p-2 text-[11px] leading-4">
כל מהלך פרש מהלוח המקורי עובר בדיוק לאחד משני השכנים של אותו מספר.
</div>
</div>

<div class="bg-sky-50 border-2 border-sky-200 rounded-lg p-3">
<div class="font-bold text-[14px] mb-1">2. מקבלים מעגל שקול</div>

<div class="flex justify-center -mt-4 scale-50">
<TransitionSystemD3  
  :width="110" :height="200"
  :states="[
    { id: '1', text: '1', label: 'a1', x: 250-180, y: 280 },
    { id: '2', text: '2', label: 'b3', x: 370-180, y: 220 },
    { id: '3', text: '3', label: 'c1', x: 420-180, y: 100 },
    { id: '4', text: '4', label: 'a2', x: 370-180, y: -20 },
    { id: '5', text: '5', label: 'c3', x: 250-180, y: -80 },
    { id: '6', text: '6', label: 'b1', x: 130-180, y: -20 },
    { id: '7', text: '7', label: 'a3', x: 80-180, y: 100 },
    { id: '8', text: '8', label: 'c2', x: 130-180, y: 220 },
    { id: 'b2', text: 'b2', label: 'מבודדת', x: 250-180, y: 100, color: '#94a3b8' }
  ]"
  :transitions="[
    { source: '1', target: '2' },
    { source: '2', target: '3' },
    { source: '3', target: '4' },
    { source: '4', target: '5' },
    { source: '5', target: '6' },
    { source: '6', target: '7' },
    { source: '7', target: '8' },
    { source: '8', target: '1' }
  ]"
/>
</div>

<div class="bg-white border border-sky-200 rounded p-2 text-center font-mono text-[11px] leading-4" dir="ltr">

1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 1
</div>

<div v-click="2" class="mt-2 bg-white border border-sky-200 rounded p-2 text-[11px] leading-4">
עכשיו רואים את המערכת השקולה כגרף ממשי: מחזור בן 8 מצבים ועוד מצב מבודד אחד.
</div>
</div>

<div class="bg-emerald-50 border-2 border-emerald-200 rounded-lg p-3">
<div class="font-bold text-[14px] mb-1">3. סופרים צעדים</div>

<div class="grid grid-cols-[auto_1fr] gap-x-2 gap-y-1 items-center text-[11px]">
  <div class="font-bold">התחלה</div>
  <div class="flex gap-[2px]">
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">1</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♞</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">3</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♞</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">5</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♘</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">7</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♘</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
  </div>

  <div class="font-bold">יעד</div>
  <div class="flex gap-[2px]">
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">1</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♘</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">3</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♘</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">5</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♞</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex flex-col items-center justify-center"><div class="text-[8px]">7</div><div style="font-family: 'Noto Sans Symbols 2', 'Segoe UI Symbol', 'DejaVu Sans', serif;" class="text-sm leading-none">♞</div></div>
    <div class="w-7 h-10 rounded border border-emerald-300 bg-white flex items-center justify-center text-slate-300">·</div>
  </div>
 </div>

<div class="mt-2 space-y-1 text-[11px] leading-4">
  <div class="bg-white border border-emerald-200 rounded p-2">אי אפשר לעקוף פרש אחר, לכן הסדר היחסי נשמר לאורך כל הריצה.</div>
  <div class="bg-white border border-emerald-200 rounded p-2">כדי להגיע מהתחלה ליעד, כל אחד מארבעת הפרשים חייב להתקדם בדיוק 4 צעדים על המעגל.</div>
</div>

<div v-click="3" class="mt-2 bg-white border border-emerald-300 rounded p-2 text-[11px] leading-4">
לכן ההחלפה אפשרית, ומספר הצעדים המינימלי הוא <b>16</b>.
</div>
</div>

</div>
