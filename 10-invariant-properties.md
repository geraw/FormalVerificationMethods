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
  ## Safety Properties and Invariants
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תכונות שמורה ובטיחות

## הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">נבין מהי תכונת בטיחות</div>

- למה האינטואיציה היא: "שום דבר רע לא יקרה".
- איך מזהים הפרה של תכונת בטיחות בזמן סופי.
- למה מספיקה לפעמים ריצה סופית קצרה כדי להפריך תכונה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">נבדיל בין שני מושגים קרובים</div>

- תכונת שמורה: תנאי על מצבים נגישים.
- תכונת בטיחות כללית: תנאי על קטעי ריצה סופיים.
- כל תכונת שמורה היא תכונת בטיחות, אך לא להפך.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
הסעיף הזה הוא הגשר בין "תכונות זמן לינארי" לבין אלגוריתמים קונקרטיים לאימות:  
גם הגדרה מתמטית, גם אינטואיציה, וגם איך בודקים בפועל.
</div>

---

# אינטואיציה: מה פירוש "בטיחות"?

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold mb-3">הניסוח האינטואיטיבי</div>

תכונת בטיחות אומרת:

<div class="text-center text-2xl mt-4 mb-4 font-bold">
"שום דבר רע לא יקרה"
</div>

אם התכונה מופרכת, אפשר לראות זאת אחרי מספר סופי של צעדים.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">דוגמאות טבעיות</div>

- מניעה הדדית: לעולם לא שני תהליכים יחד בקטע קריטי.
- חופש מקיפאון: לא מגיעים למצב שבו כולם תקועים.
- כספומט: לא מחלקים כסף לפני שהוזן PIN תקין.
</div>
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-4 text-right text-[15px]">
הנקודה המרכזית: הפרה של בטיחות איננה דורשת להמתין "לנצח".  
אם משהו רע קרה, יש כבר קידומת סופית שמוכיחה את זה.
</div>

---

# נוסחת מצב

<div class="text-right text-[15px] leading-snug mt-2">

במערכת מעברים, כל מצב $s$ מתויג על ידי קבוצת הפסוקים האטומיים שמתקיימים בו: $L(s) \subseteq AP$.
נוסחת מצב היא נוסחה פסוקית $\Phi$ מעל $AP$.

</div>

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">

מה פירוש $s \models \Phi$?

</div>

המצב $s$ מקיים את $\Phi$ אם ההשמה שבה בדיוק הפסוקים ב־$L(s)$ הם אמת הופכת את $\Phi$ לאמת.

לדוגמה, אם:

$$
L(s)=\{crit_1, wait_2\}
$$

אז $s \models crit_1$ וגם $s \models \neg crit_2$.

</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">מה בודקים בפועל?</div>

נוסחת מצב מסתכלת רק על התווית של המצב הנוכחי, לא על העבר ולא על העתיד.

למשל:

$$
\Phi = \neg crit_1 \vee \neg crit_2
$$

אומרת שבמצב הנוכחי לא שני התהליכים יחד בקטע הקריטי.

</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">

תכונת שמורה תהפוך נוסחת מצב כזו לדרישה על כל המצבים הנגישים לאורך כל הריצות.

</div>

---

# תכונות שמורה

<div class="text-right text-[15px] leading-snug mt-2">

תכונת שמורה היא תכונת זמן לינארי שמוגדרת על ידי נוסחת מצב $\Phi$,
ודורשת שכל מצב נגיש יקיים את $\Phi$.

</div>

<div class="mt-8 text-center">

$$
P_{\mathit{inv}}(\Phi) =
\{\sigma \in (2^{AP})^\omega \mid \forall j \ge 0 \left( \sigma[j] \models \Phi \right) \}
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-green-50 border border-green-200 rounded p-4 text-[15px]">
<div class="font-bold mb-2">פירוש מעשי - הוכחת שמורה באינדוקציה</div>

- כל מצב התחלתי צריך לקיים את נוסחת המצב $\Phi$.

- כל מעבר בין מצבים נגישים צריך לשמר את אמיתות $\Phi$.
- לכן כל מצב נגיש מקיים את נוסחת המצב $\Phi$.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">שקילות שימושית</div>

$$TS \models P_{\mathit{inv}}(\Phi)$$

$$\iff$$

$$\forall s \in Reach(TS) \left( L(s) \models \Phi \right)
$$

</div>
</div>

---

# דוגמאות לתכונות שמורה

<div class="grid grid-cols-2 gap-6 mt-8 items-start text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">מניעה הדדית לשני תהליכים</div>

אם $crit_1, crit_2$ מציינים שתהליך נמצא בקטע הקריטי, נוסחת המצב היא:

$$
\Phi = \neg crit_1 \vee \neg crit_2
$$

כלומר, לא ייתכן ששניהם בקטע הקריטי בו-זמנית.
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold mb-3">חופש מקיפאון לסועדים</div>

אם $wait_i$ מציין שהפילוסוף $i$ ממתין למקל השני, נוסחת המצב היא:

$$
\Phi = \neg wait_0 \vee \neg wait_1 \vee \neg wait_2 \vee \neg wait_3 \vee \neg wait_4
$$

כלומר, תמיד יש לפחות פילוסוף אחד שאינו במצב ההמתנה הבעייתי.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
שתי הדוגמאות הן "תכונות בטיחות", אבל הן אפילו חזקות יותר:  
אפשר לנסח אותן באמצעות נוסחת מצב שנדרשת בכל מצב נגיש.
</div>

---

# איך בודקים שמורה?

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">הרעיון האלגוריתמי</div>

מבצעים חיפוש קדימה ממצבי ההתחלה:

- מחשבים את המצבים הנגישים.
- בכל מצב נגיש בודקים אם נוסחת המצב $\Phi$ מתקיימת.
- אם נמצא מצב שבו נוסחת המצב $\Phi$ שקרית, קיבלנו הפרכה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-left" dir="ltr">
<div class="font-bold mb-3 text-right" dir="rtl">פסאודו-קוד ברוח DFS</div>

```text
R := visited states
U := stack

for each initial state s:
  DFS from s
  whenever a new reachable state t is found:
    check t |= Φ
    if not, stop with counterexample
```
</div>
</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right text-[15px]">

כל עוד בודקים את נוסחת המצב $\Phi$ בזמן ביקור במצב חדש, מקבלים גם חיפוש נגישות וגם בדיקת שמורה באותו מעבר.
</div>

---

# דוגמה: חידת הכדורים

<div class="mt-2 bg-blue-50 border border-blue-200 rounded p-3 text-right text-[13px]">

בשק יש $2026$ כדורים שחורים ו־$2026$ כדורים לבנים. סטודנט חרוץ חוזר על התהליך עד שנשאר כדור אחד:
מוציאים שני כדורים אקראיים; אם הם באותו צבע מחזירים כדור לבן, ואם הם בצבעים שונים מחזירים כדור שחור.
מה יהיה צבע הכדור האחרון?

</div>

<div class="grid grid-cols-2 gap-6 mt-3 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4 text-[13px]">
<div class="font-bold mb-2">מערכת המעברים</div>

מצב הוא מילה
$w \in \{W,B\}^*$,
המתארת את שק הכדורים.

מעבר בוחר שתי אותיות מתוך המילה, מוחק אותן, ומוסיף בתחילת המילה את האות המתאימה:

$$
WW \mapsto W
\qquad
BB \mapsto W
\qquad
WB,BW \mapsto B
$$

למשל:

$$
uXvYz \to Zuvz
$$

כאשר $Z$ נקבע לפי הזוג $XY$.

</div>

<div class="bg-green-50 border border-green-200 rounded p-4 text-[13px]">
<div class="font-bold mb-2">השמורה</div>

נוסחת המצב:

$$
\Phi(w) \equiv \#_B(w) \text{ זוגי}
$$

בסיס: בתחילה $\#_B(w)=2026$, ולכן $\Phi$ מתקיימת.

צעד אינדוקציה:

- $WW \mapsto W$: מספר השחורים לא משתנה.
- $BB \mapsto W$: מספר השחורים קטן ב־$2$.
- $WB \mapsto B$: מספר השחורים לא משתנה.

לכן $\Phi$ נשמרת בכל מעבר.

</div>
</div>

<img
  src="/black-white-balls-comic.png"
  alt="איור קומי של סטודנט צובע כדור שחור בלבן לפני החזרה לשק"
  class="absolute top-40 left-3 w-40 rounded border border-slate-200 shadow-lg"
/>

<div class="mt-5 mr-0 ml-70 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">

כל צעד מקטין את מספר הכדורים באחד, ולכן בסוף נשאר כדור אחד. מספר הכדורים השחורים בסוף עדיין זוגי, ולכן אינו יכול להיות $1$.  
הכדור האחרון הוא לבן.

</div>

---

# סיבוכיות בדיקת שמורה

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">זמן</div>

אם:

- $N$ הוא מספר המצבים הנגישים,
- $M$ הוא מספר המעברים בגרף הנגיש,

אז זמן הריצה הוא:

$$
O\bigl(N \cdot (1 + |\Phi|) + M\bigr)
$$
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-5">
<div class="font-bold mb-3">זיכרון</div>

נשמור בדרך כלל:

- קבוצה של מצבים שכבר בוקרו.
- מחסנית או תור של חיפוש.

לכן תוספת הזיכרון היא לינארית במספר המצבים הנגישים.
</div>
</div>

<div class="mt-8 bg-rose-50 border border-rose-200 rounded p-4 text-right text-[15px]">
מבחינה חישובית, תכונות שמורה הן נוחות במיוחד:  
אין צורך לנתח ריצות אינסופיות באופן ישיר, רק את החלק הנגיש של גרף המצבים.
</div>

---

# תכונת בטיחות כללית

<div class="text-right text-[15px] leading-snug mt-2">

לא כל תכונת בטיחות היא תכונת מצב. לפעמים הדרישה מתייחסת לקטע ריצה סופי, ולא רק למצב האחרון.

</div>

<div class="mt-8 text-center text-[17px] leading-relaxed">

תכונה $P_{\mathit{safe}}$ היא תכונת בטיחות
אם לכל מילה אינסופית $\sigma \notin P_{\mathit{safe}}$
יש קידומת סופית $\hat{\sigma}$ כך שאף המשך אינסופי שלה לא יוכל עוד להיכנס ל־$P_{\mathit{safe}}$.

</div>

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">קידומת רעה</div>

קידומת סופית שמרגע שהופיעה, התכונה כבר אבודה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">קידומת רעה מינימלית</div>

קידומת רעה שאף קידומת ממש שלה עדיין אינה רעה.
</div>
</div>

---

# שמורה היא מקרה פרטי של בטיחות

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-green-50 border border-green-200 rounded p-5">
<div class="font-bold mb-3">

אם נוסחת המצב $\Phi$ מגדירה שמורה

</div>

אז הקידומות הרעות המינימליות הן בדיוק כאלה שבהן:

- כל המצבים עד השלב הקודם מקיימים את נוסחת המצב $\Phi$
- ובשלב האחרון נוסחת המצב $\Phi$ כבר מופרכת

</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5 text-center">
<div class="font-bold mb-3 text-right">צורה אופיינית</div>

$$
\sigma[0]\sigma[1]\ldots\sigma[n]
$$

כך ש:

$$
\sigma[0],\ldots,\sigma[n-1] \models \Phi
\qquad
\sigma[n] \not\models \Phi
$$
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">

מכאן נובע מייד: כל תכונת שמורה היא תכונת בטיחות.  
אבל ההפך אינו נכון, משום שיש תכונות שבודקות גם את ההיסטוריה הקרובה.

</div>

---

# דוגמה: רמזור

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">תכונה שהיא כן שמורה</div>

"לעולם לא דולקים שני אורות יחד"

זהו תנאי על מצב יחיד: בכל מצב בודקים כמה אורות דולקים.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">תכונה שהיא בטיחות אך לא שמורה</div>

"כל מופע של אדום חייב להיות מיד אחרי צהוב"

כדי לבדוק את זה במצב שבו רואים אדום, צריך לדעת גם מה היה בצעד הקודם.
</div>
</div>

<div class="mt-8 bg-red-50 border border-red-200 rounded p-4 text-right text-[15px]">
לכן זו תכונת בטיחות: יש קידומת רעה סופית.  
אבל זו לא תכונת שמורה, כי לא ניתן להכריע אותה מהמצב הנוכחי בלבד.
</div>

---

# דוגמה: מכונת משקאות

<div class="text-right text-[15px] leading-snug mt-2">

דרישה טבעית היא:

</div>

<div class="text-center text-2xl font-bold mt-4 mb-4">
מספר המטבעות שהוכנסו עד כה תמיד לפחות כמספר המשקאות שסופקו
</div>

<div class="mt-6 text-center">

$$
\forall i \ge 0 \left(
\left|\{0 \le j \le i \mid pay \in \sigma[j]\}\right|
\ge
\left|\{0 \le j \le i \mid drink \in \sigma[j]\}\right|
\right)
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">למה זו בטיחות?</div>

אם סופק משקה "מוקדם מדי", יש קידומת סופית שמוכיחה זאת.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold mb-2">למה זו לאו דווקא שמורה?</div>

כי ההכרעה תלויה בספירה המצטברת לאורך הקידומת, לא רק בתווית של המצב האחרון.
</div>
</div>

---

# בדיקת בטיחות דרך קידומות רעות

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">הלמה המרכזית</div>

עבור מערכת ללא מצבים סופניים ותכונת בטיחות $P_{\mathit{safe}}$:

$$
TS \models P_{\mathit{safe}}
\iff
Traces_{fin}(TS) \cap BadPref(P_{\mathit{safe}}) = \varnothing
$$

</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">המשמעות</div>

- כדי להפריך בטיחות, מספיק למצוא קידומת רעה ניתנת להשגה.
- כדי להוכיח בטיחות, צריך להראות שאף קידומת רעה אינה מתקבלת כריצה סופית של המערכת.
</div>
</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right text-[15px]">

זהו בדיוק ההבדל מול תכונות חיות:  
כאן קטע ריצה סופי כבר יכול להספיק כדי לקבוע שהמערכת לא תקינה.

</div>

---

# Prefix ו־Closure

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">קבוצת הקידומות</div>

לעקבה $\sigma$:

$$
pref(\sigma) = \{\varepsilon, \sigma[0], \sigma[0]\sigma[1], \sigma[0]\sigma[1]\sigma[2], \dots \}
$$

ולתכונה $P$:

$$
pref(P) = \bigcup_{\sigma \in P} pref(\sigma)
$$
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">הסגור של תכונה</div>

$$
closure(P)=
\{\sigma \in (2^{AP})^\omega \mid pref(\sigma) \subseteq pref(P)\}
$$

כלומר: כל מסלול שכל קידומת סופית שלו עדיין "נראית חוקית" ביחס ל־$P$.

</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">

ה־closure הוא האוסף של כל ההתנהגויות שלא ניתן לפסול על סמך מידע סופי בלבד.

</div>

---

# אפיון חלופי לתכונות בטיחות

<div class="text-center mt-10">

$$
P \text{ היא תכונת בטיחות}
\iff
closure(P)=P
$$

</div>

<div class="grid grid-cols-2 gap-8 mt-10 text-right">
<div class="bg-green-50 border border-green-200 rounded p-5">
<div class="font-bold mb-3">

אם $closure(P)=P$

</div>

אז כל מסלול שאינו ב־$P$ חייב להכיל קידומת שאינה קידומת של שום מסלול חוקי.  
זו בדיוק קידומת רעה.

</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold mb-3">

אם $P$ היא בטיחות

</div>

אז כל מסלול שמחוץ ל־$P$ נפסל כבר בשלב סופי, ולכן לא יכול להישאר בתוך $closure(P)$.

</div>
</div>

---

# שקילות מסלולים סופיים ותכונות בטיחות

<div class="text-right text-[15px] leading-snug mt-2">

לתכונות בטיחות יש קשר עמוק למסלולים סופיים, לא רק למסלולים אינסופיים.

</div>

<div class="mt-8 text-center">

$$
Traces_{fin}(TS) \subseteq Traces_{fin}(TS')
$$

אם ורק אם

$$
\forall P_{\mathit{safe}} \left(
\quad
TS' \models P_{\mathit{safe}}
\Rightarrow
TS \models P_{\mathit{safe}}
\right)
$$

</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-right">
במילים:

- אם כל הריצות הסופיות של $TS$ כבר מותרות ב־$TS'$,  
  אז כל תכונת בטיחות שנכונה ב־$TS'$ נשמרת גם ב־$TS$.
</div>

<div class="mt-6 bg-rose-50 border border-rose-200 rounded p-4 text-right text-[15px]">
זה חשוב במיוחד בריפיינמנט:  
שמירה על מסלולים סופיים מספיקה כדי לשמר תכונות בטיחות.
</div>

---

# למה צריך להיזהר?

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">במערכות סופיות ללא מצבים סופניים</div>

לעיתים קרובות הכל מסתדר יפה:

- מסלולים סופיים מספרים כמעט את כל הסיפור.
- יש קשר הדוק גם למסלולים אינסופיים.
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold mb-3">אבל לא תמיד</div>

במערכות אינסופיות, או כאלה עם מצבים סופניים:

- ייתכן ש־$Traces_{fin}$ ייכלל
- אך $Traces$ לא ייכלל

ולכן תכונות שאינן בטיחות לא בהכרח נשמרות.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
כלומר, תכונות בטיחות הן בדיוק המחלקה שאפשר "לראות" דרך הקידומות הסופיות.
</div>

---

# מה לקחת מכאן?

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">תכונות שמורה</div>

- מוגדרות על ידי נוסחת מצב $\Phi$.
- נבדקות על כל מצב נגיש.
- מאפשרות אלגוריתם DFS/BFS פשוט ויעיל יחסית.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">תכונות בטיחות</div>

- מגלמות את העיקרון "שום דבר רע לא יקרה".
- הפרתן ניתנת לזיהוי על ידי קידומת רעה סופית.
- מאופיינות על ידי $closure(P)=P$.
</div>
</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right text-[15px]">
כל תכונת שמורה היא תכונת בטיחות, אך לא כל תכונת בטיחות היא תכונת שמורה.  
הצעד הבא בקורס הוא להבין את המחלקה המשלימה: תכונות חיות.
</div>
