---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 09-linear-time-behavior
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## תכונות זמן לינארי
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# תכונות זמן לינארי

## הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה


<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">נעבור ממסלולים להתנהגות נצפית</div>

- מהו מקטע מסלול, ומהו מסלול של מערכת מעברים.
- איך מפיקים עקבה מתוך מסלול.
- למה עקבות הן מה שתכונות זמן לינארי "רואות".
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">נגדיר תכונות זמן לינארי</div>

- תכונת זמן לינארי היא קבוצה של מילים אינסופיות.
- מערכת מקיימת תכונה אם כל עקבותיה שייכות לקבוצה.
- נראה איך הכלת עקבות ושקילות עקבות שומרות תכונות.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
זהו הפרק שבו עוברים מהמודל האופרטיבי של מערכת מעברים אל השפה שבה ננסח את דרישות המערכת.
</div>

---

# מקטעי מסלול

<div class="mt-8 grid grid-cols-2 gap-6 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5 text-[16px]">
<div class="font-bold mb-3">מקטע מסלול סופי</div>

$$
s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} \cdots \xrightarrow{\alpha_n} s_n
$$

נסמן:

$$
\operatorname{first}(\pi)=s_0
$$

$$
\operatorname{last}(\pi)=s_n
$$

$$
\operatorname{len}(\pi)=n
$$
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-[16px]">
<div class="font-bold mb-3">מקטע מסלול אינסופי</div>

$$
s_0 \xrightarrow{\alpha_1} s_1 \xrightarrow{\alpha_2} s_2 \xrightarrow{\alpha_3} \cdots
$$

כאן:

$$
\operatorname{first}(\pi)=s_0
$$

$$
\operatorname{len}(\pi)=\infty
$$

$$
\operatorname{last}(\pi)=\bot
$$
</div>
</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right text-[16px]">

נכתוב
$
\pi[j]
$
עבור המצב ה־$j$ במסלול,
$\pi[..j]$
עבור הרישא עד $j$,
$
\pi[j..]
$
עבור הסיפא מ־$j$ והלאה.

</div>

---

# מסלולים של מערכת מעברים

<div class="grid grid-cols-2 gap-8 mt-8 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5 text-[16px]">
<div class="font-bold mb-3">מקטע מקסימלי</div>

מקטע מסלול הוא מקסימלי אם:

- הוא אינסופי, או
- שהוא סופי ומסתיים במצב סופני
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-[16px]">
<div class="font-bold mb-3">מסלול</div>

מסלול של מערכת מעברים הוא מקטע מסלול שהוא:

- התחלתי
- וגם מקסימלי

כלומר, מתחיל במצב התחלתי ואי אפשר להאריך אותו.
</div>
</div>

<div class="mt-8 bg-rose-50 border border-rose-200 rounded p-4 text-right text-[15px]">
בפרק הזה עובדים בדרך כלל עם מערכות ללא מצבים סופניים, ולכן המסלולים המקסימליים הם אינסופיים.
</div>

---

# עקבות

<div class="text-right text-[15px] leading-snug mt-2">
בבדיקת תכונות זמן לינארי, לא הפעולות עצמן ולא זהות המצבים הם העיקר, אלא קבוצת הפסוקים האטומיים שמתקיימת לאורך הריצה.
</div>

<div class="mt-8 text-center">

$$
trace(\pi)=L(s_0)L(s_1)L(s_2)\dots
$$

</div>



<div class="grid grid-cols-3 gap-4 mt-6 items-center text-center">


<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">עקבה</div>
<div dir="ltr">

$L(s_0)L(s_1)L(s_2)L(s_3)\dots$
</div>
</div>

<div class="text-2xl font-bold">⟶</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מסלול</div>
<div dir="ltr">

$s_0s_1s_2s_3\dots$
</div>
</div>
</div>

<img
  src="/trace-footprints-comic.png"
  alt="איור קומי של אדם הולך ואדם אחר בוחן את העקבות שלו"
  class="absolute bottom-5 left-75 w-90 opacity-90 pointer-events-none"
/>


---

# קבוצות עקבות

<div class="mt-8 space-y-6 text-right max-w-3xl mx-auto">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">עקבות אינסופיות</div>

$$
\operatorname{Traces}(s)=\operatorname{trace}(\operatorname{Paths}(s))
$$

$$
\operatorname{Traces}(TS)=\bigcup_{s \in I} \operatorname{Traces}(s)
$$
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">עקבות סופיות</div>

$$
\operatorname{Traces}_{fin}(s)=\operatorname{trace}(\operatorname{Paths}_{fin}(s))
$$

$$
\operatorname{Traces}_{fin}(TS)=\bigcup_{s \in I} \operatorname{Traces}_{fin}(s)
$$
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[16px]">

עקבה היא מילה מעל האלפבית $2^{AP}$, כי בכל שלב רואים תת־קבוצה של הפסוקים האטומיים.

</div>

---

# דוגמה: אלגוריתם semaphore

<div class="text-right text-[15px] leading-snug mt-2">

נניח $AP=\{crit_1,crit_2\}$, כאשר $crit_i$ מציין שתהליך $i$ בקטע הקריטי.

</div>

<div class="mt-8 text-center" dir="ltr">

$$
\langle n_1,n_2,y=1 \rangle
\to
\langle w_1,n_2,y=1 \rangle
\to
\langle c_1,n_2,y=0 \rangle
\to
\langle n_1,n_2,y=1 \rangle
\to \cdots
$$

</div>

<div class="mt-8 text-center">

$$
\operatorname{trace}(\pi)=
\{\}\;
\{\}\;
\{crit_1\}\;
\{\}\;
\{\}\;
\{crit_2\}\;\dots
$$

</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right text-[16px]">

העקבה משאירה רק את המידע הדרוש להגדרת התכונה, ומתעלמת מהמשתנה $y$ ומשמות המקומות.

</div>

---

# הגדרה: תכונת זמן לינארי


<div class="mt-6 grid grid-cols-[1fr_auto_1.2fr_auto_1fr] gap-3 items-center text-center">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מערכת</div>
<div dir="ltr">

$TS$
</div>
</div>


<div class="text-2xl font-bold">⟵</div>

<div class="bg-amber-50 border-2 border-amber-300 rounded p-4">
<div class="font-bold mb-2">ממשק האימות</div>
<div dir="ltr">

$\operatorname{Traces}(TS)$
</div>
<div class="text-[13px] mt-1">מה שהבודק רואה</div>
</div>

<div class="text-2xl font-bold">⟶</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">תכונה</div>
<div dir="ltr">

$P$
</div>
</div>
</div>

<div class="grid grid-cols-2 gap-8 mt-6 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">הגדרה</div>

תכונת זמן לינארי
 $P \subseteq (2^{AP})^\omega$.
 היא קבוצה של מילים אינסופיות מעל 
 $2^{AP}$.

</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">סיפוק תכונה</div>

$$
TS \models P
\iff
\operatorname{Traces}(TS) \subseteq P
$$

כל עקבה שהמערכת מייצרת חייבת להיות ב-$P$.

</div>
</div>

---

# דוגמה ($P_{\text{live}}$): הרמזור הראשון ירוק אינסוף פעמים

<div class="mt-8 text-center">

$$
P_{\text{live}}=
\{\sigma \in (2^{AP})^\omega \mid \underset{\infty}{\exists} i \left( green \in \sigma[i] \right) \}
$$

</div>

<div class="grid grid-cols-2 gap-6 -mt-1 text-right text-[12px]">
<div class="bg-green-50 border border-green-200 rounded p-4">
<div class="font-bold mb-2">שייכות</div>

עקבה שבה $green$ מופיע שוב ושוב לאורך הריצה.

$$
\sigma =
\{green\}\emptyset\{green\}\emptyset\{green\}\emptyset\dots
$$

</div>

<div class="bg-red-50 border border-red-200 rounded p-4 text-[12px]">
<div class="font-bold mb-2">אי-שייכות</div>

עקבה שבה אחרי זמן מסוים $green$ מפסיק להופיע.

$$
\sigma =
\{green\}\{green\}\emptyset\emptyset\emptyset\dots
$$

</div>
</div>

<div class="mt-2 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[12px]">

<div class="font-bold mb-2">

גם עקבות לא הגיוניות לרמזור הן מילים מעל $2^{AP}$

</div>

למשל, אם $AP$ כולל גם $yellow,red$, אז העקבה הבאה שייכת ל־$P_{\text{live}}$ למרות שהיא אינה מתארת רמזור תקין:

$$
\sigma =
\{green,yellow,red\}\{green,red\}\{green,yellow\}\dots
$$

והעקבה הבאה אינה שייכת ל־$P_{\text{live}}$, גם אם היא עדיין מכילה צירופים לא הגיוניים:

$$
\sigma =
\{green,red\}\{yellow,red\}\{yellow,red\}\dots
$$

</div>

---

# דוגמה ($P_{\text{safe}}$): לעולם לא שני ירוקים יחד

<div class="mt-8 text-center">

$$
P_{\text{safe}}=
\{\sigma \in (2^{AP})^\omega \mid
\forall i \ge 0 \left(
green_1 \notin \sigma[i] \vee green_2 \notin \sigma[i]
\right)\}
$$

</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[15px]">

זו תכונה שאוסרת התנהגות לא רצויה: בכל רגע לפחות אחד משני הרמזורים אינו ירוק.

</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-right text-[12px]">
<div class="bg-green-50 border border-green-200 rounded p-4">
<div class="font-bold mb-2">שייכות</div>

$$
\sigma =
\{green_1\}\{green_2\}\emptyset\{green_1\}\dots
$$

בכל מקום לכל היותר רמזור אחד ירוק.

</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">אי-שייכות</div>

$$
\sigma =
\{green_1\}\{green_1,green_2\}\emptyset\dots
$$

במקום השני שני הרמזורים ירוקים יחד.

</div>
</div>

---

# דוגמה: מניעה הדדית

<div class="text-right text-[15px] leading-snug mt-2">

אם $AP=\{crit_1,crit_2\}$, אפשר לנסח את תכונת המניעה ההדדית כך:

</div>

<div class="mt-8 text-center">

$$
P_{mutex}=
\{\sigma \in (2^{AP})^\omega \mid
\forall i \left( \{crit_1,crit_2\} \nsubseteq \sigma[i] \right)\}
$$

</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-4 text-right text-[15px]">

כלומר, אף פעם לא נראה בעקבה מצב שבו שני התהליכים בקטע הקריטי בו־זמנית.

</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-right text-[12px]">
<div class="bg-green-50 border border-green-200 rounded p-4">
<div class="font-bold mb-2">שייכות</div>

$$
\sigma =
\emptyset\{crit_1\}\emptyset\{crit_2\}\emptyset\dots
$$

הכניסות לקטע הקריטי מתחלפות, אבל אין חפיפה.

</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">אי-שייכות</div>

$$
\sigma =
\emptyset\{crit_1,crit_2\}\emptyset\dots
$$

יש רגע שבו שני התהליכים בקטע הקריטי יחד.

</div>
</div>

---

# דוגמה ($P_{\text{nostarve}}$): חוסר הרעבה

<div class="text-right text-[15px] leading-snug mt-2">

אם $AP=\{wait_1,crit_1,wait_2,crit_2\}$, דרישה טבעית היא:

</div>

<div class="mt-8 text-center">

$$
P_{\text{nostarve}}=
\left\{ \sigma \in (2^{AP})^\omega \;\middle|\;
\forall i \in \{1,2\} 
\left( \underset{\infty}{\exists} j \bigl( wait_i \in \sigma[j] \bigr) \Rightarrow \underset{\infty}{\exists} j \bigl( crit_i \in \sigma[j] \bigr) \right)
\right\}
$$

</div>

<div class="mt-8 bg-red-50 border border-red-200 rounded p-4 text-right text-[15px]">

זו דוגמה לתכונה שמסתכלת על כל הריצה האינסופית, ולא רק על מצב בודד.

</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-right text-[12px]">
<div class="bg-green-50 border border-green-200 rounded p-4">
<div class="font-bold mb-2">שייכות</div>

$$
\sigma =
\{wait_i\}\{crit_i\}\{wait_i\}\{crit_i\}\dots
$$

אם יש אינסוף המתנות, יש גם אינסוף כניסות לקטע הקריטי.

</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">אי-שייכות</div>

$$
\sigma =
\{wait_i\}\{wait_i\}\{wait_i\}\{wait_i\}\dots
$$

התהליך מחכה אינסוף פעמים, אבל אף פעם לא נכנס לקטע הקריטי.

</div>
</div>

---

# משפט: הכלת עקבות ותכונות זמן לינארי

<div class="mt-8 text-center">

$$
\operatorname{Traces}(TS) \subseteq \operatorname{Traces}(TS')
$$

אם ורק אם

$$
\forall P \subseteq (2^{AP})^\omega \; \bigl(
TS' \models P \;\Rightarrow\; TS \models P \bigr)
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-1 text-right text-[12px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">כיוון ראשון</div>

נניח
$\operatorname{Traces}(TS) \subseteq \operatorname{Traces}(TS')$
וגם
$TS' \models P$.

אז

$$
\operatorname{Traces}(TS)
\subseteq
\operatorname{Traces}(TS')
\subseteq P
$$

ולכן $TS \models P$.

</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">כיוון שני</div>

נניח שכל תכונת זמן לינארי שנשמרת ב־$TS'$ נשמרת גם ב־$TS$.

נבחר
$P=\operatorname{Traces}(TS')$.
אז $TS' \models P$, ולכן גם $TS \models P$.

מכאן:

$$
\operatorname{Traces}(TS)
\subseteq
\operatorname{Traces}(TS')
$$

</div>
</div>

<div class="mt-1 bg-green-50 border border-green-200 rounded p-4 text-right text-[15px]">

אם $TS$ הוא עידון של $TS'$ במובן של הכלת עקבות, אז כל תכונת זמן לינארי שהוכחה עבור $TS'$ נשמרת גם ב־$TS$.

</div>

---

# דוגמה: אפשרות להגיע ל־good אינה תכונת זמן לינארי

<div class="text-right text-[15px] leading-snug mt-2">

נבחן את המאפיין: קיימת ריצה המגיעה למצב שמתוייג $good$ - 
$\exists \sigma \in \operatorname{Traces}(TS) \; \bigl( \exists j \in \mathbb{N} \; (good \in \sigma[j]) \bigr)$.

</div>

<div class="grid grid-cols-2 gap-6 mt-4 text-right text-[12px]">
<div class="bg-green-50 border border-green-200 rounded p-4">
<div class="font-bold mb-2">מערכת עם יותר עקבות: המאפיין מתקיים</div>

<div class="-mt-7 -mb-7" dir="ltr">

<TransitionSystemD3 :width="320" :height="210" :auto="false"
  :states="[
    { id: 'big_s', text: '$s$', label: '$\\{\\}$', initial: true, x: 100, y: 100, width: 46 },
    { id: 'big_b', text: '$b$', label: '$\\{\\}$', x: 255, y: 140, width: 46 },
    { id: 'big_g', text: '$g$', label: '$\\{good\\}$', x: 255, y: 40, width: 46, color: '#dcfce7', stroke: '#16a34a' }
  ]"
  :transitions="[
    { source: 'big_s', target: 'big_b', curve: 0.25 },
    { source: 'big_b', target: 'big_b', loopDirection: '90deg', loopRadius: 74, loopLabelRadius: 30 },
    { source: 'big_s', target: 'big_g', curve: -0.25 },
    { source: 'big_g', target: 'big_g', loopDirection: '90deg', loopRadius: 74, loopLabelRadius: 30 }
  ]"
/>

</div>

יש בחירה שמובילה ל־$g$, ולכן יש ריצה שמגיעה ל־$good$.

</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">מערכת עם פחות עקבות: המאפיין נכשל</div>

<div class="-mt-7 -mb-7" dir="ltr">

<TransitionSystemD3 :width="320" :height="155" :auto="false"
  :states="[
    { id: 'small_s', text: '$s$', label: '$\\{\\}$', initial: true, x: 95, y: 78, width: 46 },
    { id: 'small_b', text: '$b$', label: '$\\{\\}$', x: 210, y: 78, width: 46, color: '#fee2e2', stroke: '#dc2626' }
  ]"
  :transitions="[
    { source: 'small_s', target: 'small_b' },
    { source: 'small_b', target: 'small_b', loopDirection: '-90deg', loopRadius: 72, loopLabelRadius: 32 }
  ]"
/>

</div>

אין אף ריצה שמגיעה ל־$good$.

אבל:

$$
\operatorname{Traces}(TS_{small})
\subseteq
\operatorname{Traces}(TS_{big})
$$

</div>
</div>

<div class="mt-4 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[13px]">

אם המאפיין היה תכונת זמן לינארי, הוא היה נשמר במעבר ממערכת עם יותר עקבות למערכת עם פחות עקבות. הוא לא נשמר, ולכן אינו תכונת זמן לינארי.

</div>

---

# משפט: שקילות עקבות

<div class="mt-8 text-center">

$$
\operatorname{Traces}(TS)=\operatorname{Traces}(TS')
$$

אם ורק אם

$TS$
ו-$TS'$
מקיימות את אותן תכונות זמן לינארי


</div>

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מסקנה</div>

אין תכונת זמן לינארי שיכולה להבדיל בין מערכות שקולות־עקבות.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">דוגמה</div>

שתי מכונות שתייה עם מבנה פנימי שונה יכולות להיות שקולות מבחינת כל התכונות הלינאריות.
</div>
</div>

---

# דוגמה: <a href="https://www.sefaria.org/Pirkei_Avot.3.15?lang=he" target="_blank">הכל צפוי והרשות נתונה</a>


<div class="text-right text-[15px] leading-snug mt-2">

נבחן את המאפיין: מכל מצב אפשר להגיע למצב שמתוייג $good$.

</div>

<div class="grid grid-cols-2 gap-6 mt-4 text-right text-[12px]">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">מערכת א: המאפיין נכשל</div>

<div class="-mt-7 -mb-7" dir="ltr">

<TransitionSystemD3 :width="320" :height="150" :auto="false"
  :states="[
    { id: 'eq1_s', text: '$s$', label: '$\\{\\}$', initial: true, x: 50+100, y: 78, width: 46, initialDirection: 'bottom' },
    { id: 'eq1_b', text: '$b$', label: '$\\{\\}$', x: 50+0, y: 78, width: 46 },
    { id: 'eq1_g', text: '$g$', label: '$\\{good\\}$', x: 50+200, y: 78, width: 46, color: '#dcfce7', stroke: '#16a34a' }
  ]"
  :transitions="[
    { source: 'eq1_s', target: 'eq1_g' },
    { source: 'eq1_s', target: 'eq1_b' },
    { source: 'eq1_g', target: 'eq1_g', loopDirection: '-90deg', loopRadius: 72, loopLabelRadius: 32 },
    { source: 'eq1_b', target: 'eq1_b', loopDirection: '-90deg', loopRadius: 72, loopLabelRadius: 32 },
    { source: 'eq1_s', target: 'eq1_s', loopDirection: '-90deg', loopRadius: 72, loopLabelRadius: 32 }
  ]"
/>

</div>

מהמצב $b$ אי אפשר להגיע ל־$good$.

</div>

<div class="bg-green-50 border border-green-200 rounded p-4">
<div class="font-bold mb-2">מערכת ב: המאפיין מתקיים</div>

<div class="-mt-7 -mb-7" dir="ltr">

<TransitionSystemD3 :width="320" :height="150" :auto="false"
  :states="[
    { id: 'eq1_s', text: '$s$', label: '$\\{\\}$', initial: true, x: 95, y: 78, width: 46 },
    { id: 'eq1_g', text: '$g$', label: '$\\{good\\}$', x: 210, y: 78, width: 46, color: '#dcfce7', stroke: '#16a34a' },
  ]"
  :transitions="[
    { source: 'eq1_s', target: 'eq1_g' },
    { source: 'eq1_g', target: 'eq1_g', loopDirection: '-90deg', loopRadius: 72, loopLabelRadius: 32 },
    { source: 'eq1_s', target: 'eq1_s', loopDirection: '-90deg', loopRadius: 72, loopLabelRadius: 32 }
  ]"
/>
</div>

מכל מצב יש רשות לבחור מסלול שמגיע ל־$good$.

</div>
</div>

<div class="mt-4 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[13px]">

בשתי המערכות קבוצת העקבות היא אותה קבוצה:

$$
\operatorname{Traces}(TS_1)=\operatorname{Traces}(TS_2)
= \left\{ \sigma \in (2^{AP})^\omega \;\middle|\; \sigma[0] = \{\} \land \forall i \ge 0 \bigl( \sigma[i] = \{good\} \Rightarrow \sigma[i+1] = \{good\} \bigr) \right\}
$$

אבל המאפיין מקבל בהן ערך שונה. לכן, לפי משפט שקילות העקבות, הוא אינו תכונת זמן לינארי.


</div>


---

# מה לקחת מכאן?

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">שפת העבודה החדשה</div>

- מסלולים משרים עקבות.
- עקבות הן מילים מעל $2^{AP}$.
- תכונת זמן לינארי היא קבוצה של מילים כאלה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">שימור תכונות</div>

- הכלת עקבות שומרת תכונות זמן לינארי.
- שוויון עקבות אומר שקילות בכל תכונת זמן לינארי.
- לא כל מאפיין של מערכת הוא תכונה לינארית.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
מכאן אפשר לעבור למחלקות של תכונות זמן לינארי:  
שמורות, תכונות בטיחות, ותכונות חַיּוּת.
</div>

