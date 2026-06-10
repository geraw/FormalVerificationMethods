---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 05-deadlock
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## Deadlock
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# קיפאון

## הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">נבין מהו <span dir="ltr">deadlock</span></div>

- למה מצב סופי הוא טבעי בתוכנית סדרתית אבל לרוב בעייתי במערכת מקבילית.
- מה ההבדל בין עצירה "לגיטימית" לבין עצירה שנובעת מהמתנה הדדית.
- למה קל מאוד להכניס קיפאון גם במודלים שנראים פשוטים.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">נראה שתי דוגמאות קלאסיות</div>

- רמזורים מסונכרנים שתוכננו לא נכון.
- בעיית הסועדים של דייקסטרה.
- הרעיון שמאחורי שבירת סימטריה כדי למנוע קיפאון.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
המצגת משמשת כהקדמה לפרק התכונות הלינאריות, דרך הדוגמאות הקלאסיות של קיפאון במערכות מקביליות.
</div>

---

# מתי מצב סופי הוא בעיה?

<div class="grid grid-cols-2 gap-8 mt-8 text-right items-start">
<div class="bg-green-50 border border-green-200 rounded p-5">
<div class="font-bold mb-3">תוכנית סדרתית</div>

<div class="w-26 h-38 overflow-hidden rounded-lg border border-green-200 mb-1 -ml-10 -mt-20 float-left bg-white shadow-sm relative">
  <img
    src="./public/terminal_states_comic.png"
    alt="תוכנית סדרתית שמסתיימת בהצלחה"
    class="absolute inset-y-0 left-0 h-full max-w-none"
    style="width: 200%;"
  />
</div>

מצב סופי הוא בדרך כלל תוצאה צפויה:

- התוכנית רצה.
- מגיעה למצב בלי מעברים יוצאים.
- והמשמעות היא פשוט: החישוב הסתיים.

<div class="mt-4 text-center">

$$
\operatorname{Post}(s)=\varnothing
$$

</div>
<div class="clear-both"></div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold mb-3">מערכת מקבילית</div>

<div class="w-26 h-38 overflow-hidden rounded-lg border border-red-200 mb-1 -ml-15 -mt-20 float-left bg-white shadow-sm relative">
  <img
    src="./public/terminal_states_comic.png"
    alt="מערכת מקבילית שנתקעת בקיפאון"
    class="absolute inset-y-0 left-0 h-full max-w-none"
    style="width: 200%; transform: translateX(-50%);"
  />
</div>

כאן מצב סופי הוא בדרך כלל סימן אזהרה:

- המערכת הגלובלית נתקעה.
- לפחות רכיב אחד עדיין לא "סיים באמת".
- הוא היה יכול להמשיך, אילו רכיב אחר לא היה חוסם אותו.

<div class="mt-4 text-center">

$$
\text{terminal global state} \;\not\Rightarrow\; \text{successful termination}
$$

</div>
<div class="clear-both"></div>
</div>
</div>

<div class="-mt-4 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[15px]">
<b>אינטואיציה מרכזית:</b> קיפאון מתרחש כאשר המערכת כולה נמצאת במצב סופני,
אף שלפחות רכיב אחד נמצא מקומית במצב לא־סופני. התרחיש הטיפוסי הוא המתנה הדדית בין רכיבים.
</div>

---

# דוגמה 1: רמזורים שתוכננו לא נכון

<div class="grid grid-cols-3 gap-4 mt-6 items-start">
<div class="flex flex-col items-center">
<div class="font-bold mb-2">

$TrLight_1$
</div>
<TransitionSystemD3
  :width="220" :height="180"
  :states="[
    { id: 'r1', text: 'red', initial: true, initialDirection: 'top', x: 110, y: 25, width: 70, color: '#ffebee' },
    { id: 'g1', text: 'green', x: 110, y: 130, width: 78, color: '#e8f5e9' }
  ]"
  :transitions="[
    { source: 'r1', target: 'g1', action: '$\\alpha$', curve: 0.35, actionX: -12 },
    { source: 'g1', target: 'r1', action: '$\\beta$', curve: 0.35, actionX: 12 }
  ]"
/>
</div>

<div class="flex flex-col items-center">
<div class="font-bold mb-2">

$$TrLight_2$$
</div>
<TransitionSystemD3
  :width="220" :height="180"
  :states="[
    { id: 'r2', text: 'red', initial: true, initialDirection: 'top', x: 110, y: 25, width: 70, color: '#ffebee' },
    { id: 'g2', text: 'green', x: 110, y: 130, width: 78, color: '#e8f5e9' }
  ]"
  :transitions="[
    { source: 'r2', target: 'g2', action: '$\\beta$', curve: 0.35, actionX: -12 },
    { source: 'g2', target: 'r2', action: '$\\alpha$', curve: 0.35, actionX: 12 }
  ]"
/>
</div>

<div class="flex flex-col items-center">
<div class="font-bold mb-2">


$$TrLight_1 \;\vert\!\vert\!\vert_{\{\alpha,\beta\}}\; TrLight_2$$
</div>
<TransitionSystemD3
  :width="260" :height="180"
  :states="[
    { id: 'rr', text: '$\\langle red, red \\rangle$', initial: true, initialDirection: 'top', x: 130, y: 78, width: 120, rx: 10, stroke: '#c62828', strokeWidth: 3, color: '#fff5f5' }
  ]"
  :transitions="[]"
/>
</div>
</div>

<div class="grid grid-cols-3 gap-4 mt-3 text-right text-[14px]">
<div class="bg-slate-50 border border-slate-200 rounded p-3">

במצב <span dir="ltr">red</span> של הרמזור הראשון, הפעולה האפשרית היא רק $\alpha$.
</div>
<div class="bg-slate-50 border border-slate-200 rounded p-3">

במצב <span dir="ltr">red</span> של הרמזור השני, הפעולה האפשרית היא רק $\beta$.
</div>
<div class="bg-red-50 border border-red-200 rounded p-3">

לכן ב־$\langle red, red \rangle$ אין פעולה משותפת שניתן לסנכרן עליה, והמערכת נתקעת מיד.
</div>
</div>

---

# למה זה באמת <span dir="ltr">deadlock</span>?

<div class="grid grid-cols-2 gap-8 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">מה קרה גלובלית?</div>

- המצב ההתחלתי של המערכת המורכבת הוא $\langle red, red \rangle$.
- למצב הזה אין שום מעבר יוצא.
- לכן המערכת הגלובלית היא במצב סופני כבר בצעד הראשון.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">למה זה לא "סיום תקין"?</div>

- אף אחד מהרמזורים לא הגיע למצב סופי במובן התכנוני.
- הרמזור הראשון "רוצה" לבצע $\alpha$.
- הרמזור השני "רוצה" לבצע $\beta$.
- כל אחד ממתין לאחר שיספק את הסנכרון שחסר לו.
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
זו בדיוק רוח ההגדרה: המערכת כולה עצרה, אף שיש רכיבים שבאופן מקומי עדיין אמורים להמשיך.
</div>

---

# דוגמה 2: הסועדים של דייקסטרה

<div class="text-right text-[15px] leading-snug mt-2">
ארבעה פילוסופים יושבים סביב שולחן עגול. בין כל שני שכנים יש מקל אכילה אחד בלבד.
כדי לאכול, פילוסוף חייב להחזיק <b>שני</b> מקלות: את השמאלי ואת הימני.
</div>

<div class="grid grid-cols-3 gap-5 mt-6 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">המבנה</div>

- פילוסופים: $P_0,\dots,P_3$
- מקלות: $S_0,\dots,S_3$
- כל החישובים הם מודולו $4$
- לפילוסוף $i$ יש משמאל את $S_i$ ומימין את $S_{i-1}$
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold mb-2">תרחיש הסכנה</div>

- כל פילוסוף מרים קודם את המקל השמאלי.
- אחר כך הוא מנסה לקחת את הימני.
- אם כולם עשו זאת יחד, כל אחד מחזיק מקל אחד ומחכה לשני.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">מטרת הפרוטוקול</div>

- למנוע <span dir="ltr">deadlock</span>
- לאפשר התקדמות אינסופית של המערכת
- ובפתרון חזק יותר: למנוע גם רעב אישי
</div>
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[14px]">
כאן, פעולות <span dir="ltr">request</span> ו־<span dir="ltr">release</span> מייצגות סנכרון בין תהליך פילוסוף לתהליך מקל.
</div>

---

# תיאור כהרכבה של מערכות מעברים עם סנכרון

<div class="grid grid-cols-2 gap-8 mt-6 items-start">
<div class="flex flex-col items-center">
<div class="font-bold mb-2">

התנהגות פילוסוף $Phil_i$
</div>
<TransitionSystemD3
  :width="400" :height="260"
  :states="[
    { id: 'think', text: 'think', textFontSize: 12, initial: true, initialDirection: 'top', x: 210, y: 18, width: 88, color: '#e3f2fd' },
    { id: 'waitL', text: 'wait for<br>left stick', textFontSize: 11, x: 110, y: 112, width: 100, height: 52, color: '#fff8e1' },
    { id: 'waitR', text: 'wait for<br>right stick', textFontSize: 11, x: 270, y: 112, width: 100, height: 52, color: '#fff8e1' },
    { id: 'eat',   text: 'eat', textFontSize: 12, x: 210, y: 196, width: 72, color: '#e8f5e9' },
    { id: 'retL', text: 'return the<br>left stick', textFontSize: 10, x: 10, y: 196, width: 100, height: 52, color: '#fff8e1' },
    { id: 'retR', text: 'return the<br>right stick', textFontSize: 10, x: 400, y: 196, width: 100, height: 52, color: '#fff8e1' },
  ]"
  :transitions="[
    { source: 'think', target: 'waitL', action: '$request_{i-1,i}$', curve: 0.18,  actionX:   0, actionY:0 },
    { source: 'think', target: 'waitR', action: '$request_{i,i}$',   curve: -0.18, actionX:   0, actionY:0 },
    { source: 'waitL', target: 'eat',   action: '$request_{i,i}$',   curve: 0.12,  actionX: -10, actionY:-10 },
    { source: 'waitR', target: 'eat',   action: '$request_{i-1,i}$', curve: -0.12, actionX:  10, actionY:-10 },
    { source: 'eat',   target: 'retL',  action: '$release_{i,i}$',   curve: 0,     actionX:  10, actionY:0 },
    { source: 'eat',   target: 'retR',  action: '$release_{i-1,i}$', curve: 0,     actionX: -10, actionY:0 },
    { source: 'retL',  target: 'think', action: '$release_{i-1,i}$', curve: -0.5,  actionX: -10, actionY:0 },
    { source: 'retR',  target: 'think', action: '$release_{i,i}$',   curve: 0.5,   actionX:  10, actionY:0 }
  ]"
/>
</div>

<div class="flex flex-col items-center">
<div class="font-bold mb-2">

התנהגות מקל $Stick_i$
</div>
<TransitionSystemD3
  :width="400" :height="100"
  :states="[
    { id: 'avail', text: 'available', textFontSize: 12, initial: true, initialDirection: 'top', x: 180, y: 20, width: 120, color: '#e8f5e9' },
    { id: 'occi', text: 'Occupied by the <br> right philosopher', textFontSize: 10, x: 295, y: 196, width: 180, color: '#fff8e1' },
    { id: 'occn', text: 'Occupied by the <br> left philosopher', textFontSize: 10, x: 65,  y: 196, width: 180, color: '#fff8e1' }
  ]"
  :transitions="[
    { source: 'avail', target: 'occi', action: '$request_{i,i}$', curve: 0.2,    actionX: 0 },
    { source: 'avail', target: 'occn', action: '$request_{i,i+1}$', curve: -0.2, actionX: 0 },
    { source: 'occi', target: 'avail', action: '$release_{i,i}$', curve: 0.4,    actionX: 0 },
    { source: 'occn', target: 'avail', action: '$release_{i,i+1}$', curve: -.4,  actionX: 0 }
  ]"
/>
</div>
</div>

<div class="-mt-6 bg-red-50 border border-red-200 rounded  text-right text-[15px]">

פעולות החשבון הן מודולו-4.
$H =\{request_{i,i+1}, request_{i,i}, release_{i,i+1}, release_{i,i}\ \mid i,j \in \{0,\dots,3\} \}$. 

והמערכת המשולבת מתקבלת מההרכבה:
$TS =  Phil_0  \; \|_H \;  Stick_0 \;\|_H\;  \dots \;\|_H\;  Phil_3   \;\|_H\;  Stick_3$
</div>

---

# ריצת קיפאון אופיינית

<DiningPhilosophersDeadlockAnimation :count="4" class="mt-2" />

---

# פתרון באמצעות קביעת פרוטוקול

<div class="grid grid-cols-2 gap-8 mt-6 items-start">
<div class="flex flex-col items-center">
<div class="font-bold mb-2">

מקל משופר $Stick_i$
</div>
<TransitionSystemD3
  :width="380" :height="270"
  :states="[
    { id: 'ai', text: '$available_{i,i}$', initial: true, initialDirection: 'top', x: 95, y: 30, width: 125, color: '#e8f5e9' },
    { id: 'ai1', text: '$available_{i,i+1}$', x: 285, y: 30, width: 140, color: '#e8f5e9' },
    { id: 'oi', text: '$occupied_i$', x: 95, y: 185, width: 95, color: '#fff8e1' },
    { id: 'oi1', text: '$occupied_{i+1}$', x: 285, y: 185, width: 120, color: '#fff8e1' }
  ]"
  :transitions="[
    { source: 'ai', target: 'oi', action: '$request_{i,i}$' },
    { source: 'oi', target: 'ai1', action: '$release_{i,i}$', actionY: 30, actionX: -40 },
    { source: 'ai1', target: 'oi1', action: '$request_{i,i+1}$' },
    { source: 'oi1', target: 'ai', action: '$release_{i,i+1}$', actionY: 30, actionX: 40 }
  ]"
/>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-right text-[12px] mt-10">
<div class="font-bold mb-3">מה השתנה?</div>

- המקל אינו "נייטרלי" לגמרי, אלא מציין למי הוא זמין כרגע.
- יש שני מצבי זמינות: $available_{i,i}$ ו־$available_{i,i+1}$.
- אחרי שימוש של פילוסוף אחד, הזמינות עוברת לשכן.

<div class="font-bold mb-3 mt-5">איך זה שובר את הקיפאון?</div>

- מאתחלים חלק מהמקלות במצב $available_{i,i}$ וחלק ב־$available_{i,i+1}$.
- למשל: המקלות הראשון והשלישי בכיוון אחד, והשני והרביעי בכיוון ההפוך.
- כך נשברת הסימטריה, ולכן לא ייתכן שכולם ייקחו "באותו כיוון" ויחסמו זה את זה.
</div>
</div>

<div class="-mt-3 bg-green-50 border border-green-200 rounded p-4 text-right text-[15px]">
אפשר לאמת שהפתרון הזה הוא גם <span dir="ltr">deadlock-free</span> וגם חופשי מרעב אישי.
</div>

---

# גרסא עמידה לתקלות

<div class="grid grid-cols-2 gap-6 mt-8 text-right items-start">
<div class="bg-slate-50 border border-slate-200 rounded p-5 text-[16px]">
<div class="font-bold mb-3">מה רוצים להבטיח?</div>

- שגם אם פילוסוף אחד "נתקע" לנצח במצב <span dir="ltr">think</span>, המערכת לא תיכנס לקיפאון.
- כלומר, שכנים עדיין יוכלו להמשיך להתקדם.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-[16px] leading-snug">
<div class="font-bold mb-3">רעיון המודל</div>

<div class="grid grid-cols-[1.05fr,0.95fr] gap-3 items-start">
<div>

- מוסיפים לכל פילוסוף משתנה בוליאני $x_i$.
- $x_i = true$ אם ורק אם פילוסוף $i$ נמצא במצב <span dir="ltr">think</span>.
- מקל $i$ יכול להיות זמין לשכן גם אם "הכיוון הרשמי" כרגע הפוך, כל עוד הפילוסוף האחר רק חושב ואינו זקוק למקל.
</div>
</div>
</div>
</div>

<div class="mt-30 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[16px]">
כלומר, במקום שהשכנים יחכו עיוור ל"תורם", המידע על מצב החשיבה מאפשר לעקוף חסימה מיותרת.
</div>

<div class="-mt-4 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[16px]">
זאת כבר מערכת ערוצים עם תקשורת סנכרונית באמצעות ערוצים עם קיבולת אפס.
</div>

<img
  src="./images/fault_tolerant_dining_philosophers.png"
  alt="איור של גרסת הפילוסופים העמידה לתקלות"
  class="absolute top-70 w-60 right-30"
/>


---

# קוד Promela לגרסא עמידה לתקלות

<div class="text-right text-[15px] leading-snug mt-2">

נייצג כל פעולה במערכת המעברים כערוץ סינכרוני בגודל אפס. ב־SPIN הערוץ חייב לשאת שדה הודעה, ולכן נשלח ערך דמה $0$.
</div>

<div dir="ltr" align="left" class="text-[11px] leading-tight mt-4">

<pre><code>#define REQ(p,s) req[(p)*4+(s)]
#define REL(p,s) rel[(p)*4+(s)]

chan req[16] = [0] of { bit };
chan rel[16] = [0] of { bit };
bool x[4];</code></pre>
</div>

<div class="grid grid-cols-2 gap-4 mt-3" dir="ltr">
<div align="left" class="text-[10px] leading-tight">

<pre><code>proctype Phil(byte i) {
  do
  :: x[i] := true;
     skip;                 /* think */
     x[i] := false;

     REQ(i,i)!0;            /* request right stick */
     REQ((i+3)%4,i)!0;      /* request left stick */

     skip;                 /* eat */

     REL(i,i)!0;            /* release right stick */
     REL((i+3)%4,i)!0;      /* release left stick */
  od
}</code></pre>
</div>

<div align="left" class="text-[10px] leading-tight">

<pre><code>proctype Stick(byte i) {
  do
  :: REQ(i,i)?0;
     REL(i,i)?0
  :: x[(i+1)%4] == true -&gt;
     REQ(i,(i+1)%4)?0;
     REL(i,(i+1)%4)?0
  od
}

init {
  x[0] = true; x[1] = true; x[2] = true; x[3] = true;

  run Stick(0); run Stick(1); run Stick(2); run Stick(3);
  run Phil(0);  run Phil(1);  run Phil(2);  run Phil(3);
}</code></pre>
</div>
</div>

<div class="mt-4 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[12px]">

הענף השני של <span dir="ltr">Stick(i)</span> הוא החלק העמיד לתקלות: אם הפילוסוף השכן רק חושב, המקל מסונכרן עם הפילוסוף האחר במקום לחסום את המערכת.
</div>


---

# אלגוריתם לבדיקת היעדר קיפאון

<div class="grid grid-cols-2 gap-6 mt-8 text-right items-start">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">מה בודקים?</div>

- מריצים סריקה של כל המצבים הנגישים מן המצבים ההתחלתיים.
- בכל מצב $s$ שבודקים, שואלים האם יש לו מעבר יוצא.
- אם נמצא מצב נגיש ללא עוקבים, מצאנו קיפאון.
- אם הסריקה הסתיימה בלי מצב כזה, המערכת היא <span dir="ltr">deadlock-free</span>.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold mb-3">האלגוריתם</div>

1. אתחל מחסנית או תור עם כל המצבים ב־$I$.
2. סמן כל מצב שנשלף כדי לא לבקר בו פעמיים.
3. אם ל־$s$ אין מעבר ב־$\to$, החזר "יש קיפאון".
4. אחרת, הכנס את כל העוקבים של $s$ שעדיין לא בוקרו.
5. אם התור התרוקן, החזר "אין קיפאון נגיש".
</div>
</div>

<div class="mt-8 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
זהו בדיוק חיפוש נגישות רגיל על גרף המצבים.  
העלות היא לינארית בגודל המודל המפורש:

$$
O(|S| + |\to|)
$$
</div>

---

# סיכום

<div class="grid grid-cols-2 gap-6 mt-8 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-3">מה לקחת מכאן?</div>

- במערכות מקביליות, מצב סופני הוא בדרך כלל חשוד.
- קיפאון נובע לעיתים קרובות מהמתנה הדדית.
- קל מאוד לייצר אותו כאשר רכיבים סימטריים מתחרים על משאבים.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-3">ומה עוזר?</div>

- שבירת סימטריה.
- שליטה מפורשת בזמינות משאבים.
- ולעיתים גם חשיפת מידע מקומי נוסף, כמו המשתנה $x_i$.
</div>
</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right text-[15px]">
כאן קיבלנו את האינטואיציה. בהמשך הפרק עוברים להגדרה פורמלית של מסלולים,
עקבות ותכונות זמן לינאריות.
</div>


<div class="-mt-0 bg-tekchakam-50 border border-green-200 rounded p-4 text-right text-[15px]">

כיוון שבמערכות עם קיפאון יש ריצות באורך סופי, ויהיה לנו פשוט יותר לנתח מערכות שכל הריצות שלהן אינסופיות, נניח שאין במערכות שלנו קיפאון וגם שאין מצבים סופניים.
</div>
