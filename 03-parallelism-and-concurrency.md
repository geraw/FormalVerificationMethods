---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: true
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## מערכות מעברים (Transition Systems)
  מרצה: גרא וייס
---

# מקביליות ותקשורת 

##  הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**<br>



<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/graphics/just-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מבוא 

בפרקים הקודמים הראינו כיצד למדל מעגלי חומרה ותוכניות מחשב סדרתיות כמערכות מעברים.
אך במציאות, רוב מערכות החומרה והתוכנה הן **מקביליות (parallel)** במהותן.

פרק זה מציג מודלים אופרטיביים למערכות מקביליות באמצעות מערכות מעברים:
- החל ממנגנונים פשוטים **ללא תקשורת** בין המערכות.

- ועד למנגנונים מתקדמים של **תקשורת**:

    - **סינכרונית** (Synchronous) – למשל באמצעות לחיצת יד (Handshaking).

    - **אסינכרונית** (Asynchronous) – למשל באמצעות חוצצים (Buffers).

---

# הרכבה מקבילית (Parallel Composition)

נניח שהתנהגות התהליכים הרצים במקביל נתונה על ידי מע"מ $TS_1, \dots, TS_n$.
נרצה להגדיר אופרטור $\|$ כך ש:
$$TS = TS_1 \,\|\, TS_2 \,\|\, \dots \,\|\, TS_n$$
היא מערכת מערכת המגדירה את ההתנהגות של ההרכבה המקבילית.

- נניח ש-$\|$ הוא אופרטור **קומוטטיבי** ו**אסוציאטיבי** (בדרך כלל).

- הגדרת $\|$ תלויה בסוג התקשורת הנתמכת (נראה שחלק מההגדרות אינן אסוציאטיביות).

- שימו לב: אם האופרטור לא אסוציאטיבי, הסימון למעלה לא נכון, כי יש כמה דרכים לפרש אותו <br>
  (אפשר לשים סוגריים במקומות שונים)

- שימוש בקומוטטיביות ובאסוציאטיביות מאפשר לתאר מערכות מורכבות בצורה מובנית (Structured), שבה כל רכיב עצמו יכול להיות מורכב מתת-רכיבים מקבילים.


---

# מקביליות ושזירה (Interleaving)

פרדיגמה נפוצה למידול מערכות מקביליות היא **שזירה (Interleaving)**.

- במודל זה, אנו מפשטים את העובדה שהמערכת מורכבת מרכיבים עצמאיים. 

- **המצב הגלובלי** של המערכת – המורכב מהמצבים האינדיבידואליים של הרכיבים – משחק תפקיד מרכזי.

- הפעולות של רכיבים עצמאיים ממוזגות ("נשזרות") אלו באלו.

- מקביליות מיוצגת על ידי **בחירה אי-דטרמיניסטית** בין הפעילויות של התהליכים הפועלים בו-זמנית.

<br>
<br>
<br>
<br>

<div class="flex items-top justify-center space-x-6 my-10 rtl:space-x-reverse scale-110">
  <span class="text-xl text-slate-400 font-serif">...</span>
  <div class="bg-gradient-to-br from-blue-600 to-blue-700 text-white px-6 py-3 rounded-xl shadow-xl border-2 border-blue-400/30 font-bold transition-all hover:scale-105">
    <div class="text-[10px] uppercase opacity-80 mb-1">
    צעד של רובוט א'
    </div>
  </div>
  <span class="text-xl text-slate-400 font-serif">...</span>
  <div class="bg-gradient-to-br from-blue-500 to-blue-600 text-white px-6 py-3 rounded-xl shadow-xl border-2 border-blue-300/30 font-bold transition-all hover:scale-105">
    <div class="text-[10px] uppercase opacity-80 mb-1">
    צעד של רובוט ב'
    </div>
  </div>
  <span class="text-xl text-slate-400 font-serif">...</span>
</div>


<!-- Comic Panel 1: Robot A moves -->
<div class="absolute bottom-25 left-87 w-20 h-30" 
     style="background-image: url('/interleaving_comic.png'); background-size: 200% 100%; background-position: left center;">
</div>
 
<!-- Comic Panel 2: Robot B moves -->
<div class="absolute bottom-25 right-87 w-20 h-30" 
     style="background-image: url('/interleaving_comic.png'); background-size: 200% 100%; background-position: right center;">
</div>

---

# מבט ה"מעבד היחיד" (One-Processor View)

פרדיגמת השזירה מבוססת על ההשקפה שרק מעבד אחד זמין, ועליו הפעולות של התהליכים השונים משתלבות זו בזו.

- זהו **מושג מידול** בלבד: הוא תקף גם אם התהליכים רצים על מעבדים שונים פיזית.

- (בשלב ראשון) לא מניחים הנחות לגבי הסדר שבו התהליכים השונים מבוצעים.

<div class="flex items-center justify-center space-x-4 my-8 rtl:space-x-reverse">
  <span class="text-2xl text-slate-400">...</span>
  <div class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow-md font-bold text-sm border border-blue-400/20">צעד של רובוט א'</div>
  <div class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md font-bold text-sm border border-blue-300/20">צעד של רובוט ב'</div>
  <div class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow-md font-bold text-sm border border-blue-400/20">צעד של רובוט א'</div>
  <div class="bg-blue-600 text-white px-4 py-2 rounded-lg shadow-md font-bold text-sm border border-blue-400/20">צעד של רובוט א'</div>
  <div class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md font-bold text-sm border border-blue-300/20">צעד של רובוט ב'</div>
  <span class="text-2xl text-slate-400">...</span>
</div>

- דוגמה: עבור שני תהליכים עצמאיים $P$ ו-$Q$, אלו הם שלושה רצפי שזירה אפשריים:
    1. $\dots, P, Q, P, Q, P, Q, Q, Q, P, \dots$
    2. $\dots, P, P, Q, P, P, Q, P, P, Q, \dots$
    3. $\dots, P, Q, P, P, Q, P, P, P, Q, \dots$

- בשלב זה,נניח שכל שזירה היא אפשרית, גם אם היא "לא הוגנת" (למשל מצב שבו $Q$ אף פעם לא רץ). <br>
  נושא ההגינות (Fairness) יידון בהמשך.


---

# דוגמה: שזירה של שתי מנורות חכמות

נדגים שזירה באמצעות שתי מנורות, כאשר לכל מנורה שלוש עוצמות: כבוי (Off), עמום (Dim) ובהיר (Bright).
בכל צעד, רק מנורה אחת משנה סטטוס (מעגל סגור: $O \to D \to B \to O$).

<div class="grid grid-cols-2 gap-0 mt-5 scale-[0.6] origin-top">

<!-- Single Lamp 1 -->
<div class="flex flex-col items-center">
<h4 class="font-bold -mb-20 ml-20">

מערכת $Lamp_1$
</h4>
<TransitionSystemD3  
  :width="300" :height="150"
  :states="[
    { id: 'o1', text: 'Off', initial: true, initialDirection: 'right', x: 350,  y: 75, width: 60 },
    { id: 'd1', text: 'Dim',                                          x: 200, y: 75, width: 60 },
    { id: 'b1', text: 'Bright',                                       x: 50, y: 75, width: 60 }
  ]"
  :transitions="[
    { source: 'o1', target: 'd1', action: 'next' },
    { source: 'd1', target: 'b1', action: 'next' },
    { source: 'b1', target: 'o1', action: 'reset', curve: 0.2, actionY: 5 }
  ]"
/>
</div>

<!-- Single Lamp 2 -->
<div class="flex flex-col items-center">
<h4 class="font-bold -ml-70">

מערכת $Lamp_2$
</h4>
<TransitionSystemD3  
  :width="300" :height="150"
  :states="[
    { id: 'o2', text: 'Off', initial: true, initialDirection: 'left', x: 0, y:0  , width: 60 },
    { id: 'd2', text: 'Dim',                                          x: 0, y:150 , width: 60 },
    { id: 'b2', text: 'Bright',                                       x: 0, y:300 , width: 60 }
  ]"
  :transitions="[
    { source: 'o2', target: 'd2', action: 'next' },
    { source: 'd2', target: 'b2', action: 'next' },
    { source: 'b2', target: 'o2', action: 'reset', curve: 0.3, actionX: 10 }
  ]"
/>
</div>

<!-- Interleaved Product -->
<div class="col-span-2 flex flex-col items-center  -mt-20">
<h4 class="font-bold -mb-10 ml-0 text-blue-700">

$Lamp_1 \,|||\, Lamp_2$ (שזירה)
</h4>
<TransitionSystemD3  
  :width="700" :height="350"
  :states="[
    { id: 'oo', text: 'O,O', initial: true, initialDirection: 'top', x: 500, y: 50,  width: 50 },
    { id: 'do', text: 'D,O', x: 350, y: 50,  width: 50 },
    { id: 'bo', text: 'B,O', x: 200,  y: 50,  width: 50 },
    { id: 'od', text: 'O,D', x: 500, y: 175, width: 50 },
    { id: 'dd', text: 'D,D', x: 350, y: 175, width: 50 },
    { id: 'bd', text: 'B,D', x: 200,  y: 175, width: 50 },
    { id: 'ob', text: 'O,B', x: 500, y: 300, width: 50 },
    { id: 'db', text: 'D,B', x: 350, y: 300, width: 50 },
    { id: 'bb', text: 'B,B', x: 200,  y: 300, width: 50 }
  ]"
  :transitions="[
    { source: 'oo', target: 'do', action: '$n_1$' }, { source: 'do', target: 'bo', action: '$n_1$' }, { source: 'bo', target: 'oo', action: '$r_1$', curve: -0.2, actionY:-5 },
    { source: 'od', target: 'dd', action: '$n_1$' }, { source: 'dd', target: 'bd', action: '$n_1$' }, { source: 'bd', target: 'od', action: '$r_1$', curve: 0.2, actionX:30, actionY:4 },
    { source: 'ob', target: 'db', action: '$n_1$' }, { source: 'db', target: 'bb', action: '$n_1$' }, { source: 'bb', target: 'ob', action: '$r_1$', curve: 0.2 },
    { source: 'oo', target: 'od', action: '$n_2$' }, { source: 'od', target: 'ob', action: '$n_2$' }, { source: 'ob', target: 'oo', action: '$r_2$', curve: 0.3, actionX:5 },
    { source: 'do', target: 'dd', action: '$n_2$' }, { source: 'dd', target: 'db', action: '$n_2$' }, { source: 'db', target: 'do', action: '$r_2$', curve: -0.3, actionY: -20, actionX: -5 },
    { source: 'bo', target: 'bd', action: '$n_2$' }, { source: 'bd', target: 'bb', action: '$n_2$' }, { source: 'bb', target: 'bo', action: '$r_2$', curve: -0.3, actionX: -5 }
  ]"
/>
</div>

</div>

<div class="mt-0 text-[10px] text-gray-500 text-center">

רק מנורה אחת משנה מצב בכל צעד. סך הכל $3 \times 3 = 9$ מצבים.

</div>

---

# צידוק לשזירה: פעולות בלתי-תלויות

צידוק לשזירה הוא שהאפקט של ביצוע פעולות בלתי-תלויות $\alpha$ ו-$\beta$ במקביל, זהה לביצוען בזה אחר זה בסדר כלשהו.

$$Effect(\alpha \,|||\, \beta, \eta) = Effect((\alpha ; \beta) + (\beta ; \alpha), \eta)$$

- **דוגמה**: נניח $\alpha \equiv x := x + 1$ ו-$\beta \equiv y := y - 2$.

- אם בתחילה $x=0, y=7$, התוצאה תהיה תמיד $x=1, y=5$.

<div class="flex justify-center items-center scale-90">
<TransitionSystemD3  
  :width="600" :height="200"
  :states="[
    { id: 's0', text: 'x=0, y=7', initial: true, initialDirection: 'left', x: 50, y: 75, width: 90 },
    { id: 'sa', text: 'x=1, y=7', x: 250, y: 0,  width: 90 },
    { id: 'sb', text: 'x=0, y=5', x: 250, y: 150, width: 90 },
    { id: 's1', text: 'x=1, y=5', x: 450, y: 75, width: 90 }
  ]"
  :transitions="[
    { source: 's0', target: 'sa', action: '$\\alpha$' },
    { source: 's0', target: 'sb', action: '$\\beta$' },
    { source: 'sa', target: 's1', action: '$\\beta$' },
    { source: 'sb', target: 's1', action: '$\\alpha$' }
  ]"
/>
</div>

- עבור פעולות **תלויות**, הסדר הוא קריטי! למשל: $x := x + 1 \,|||\, x := 2x$.

---

#  להרכבה בשזירה (Interleaving)

כעת אנו מוכנים להגדיר פורמלית את הרכבת השזירה (Interleaving) של מערכות מעברים. המערכת $TS_1 \,|||\, TS_2$ מייצגת מערכת מקבילית הנוצרת ממיזוג (weaving) של פעולות הרכיבים.

- **הנחה**: אין תקשורת ואין מאבקים על משאבים (כמו משתנים משותפים).

- **מצבים**: המצבים ה"גלובליים" הם זוגות $\langle s_1, s_2 \rangle$ המורכבים מהמצבים המקומיים.

- **מעברים**: המעברים היוצאים של מצב גלובלי מורכבים מאיחוד המעברים היוצאים של $s_1$ ואלו של $s_2$.

- **ביצוע**: בכל שלב, מתבצעת בחירה אי-דטרמיניסטית בין כל המעברים האפשריים של שני הרכיבים.

<div class="flex justify-center mt-4">
  <img src="/interleaving_comic.png" class="h-50" />
</div>




---

# הגדרה פורמלית: שזירה (Interleaving)

יהיו $TS_1, TS_2$ שתי מערכות מעברים. מערכת המעברים המייצגת את השזירה שלהן, $TS_1 \,|||\, TS_2$, מוגדרת כך:

- **מצבים**: $S = S_1 \times S_2$. המצבים הגלובליים הם זוגות $\langle s_1, s_2 \rangle$.

- **פעולות**: $Act = Act_1 \cup Act_2$.
- **מצבים התחלתיים**: $I = I_1 \times I_2$.
- **פסוקים אטומיים**: $AP = AP_1 \cup AP_2$.
- **פונקציית התיוג**: $L(\langle s_1, s_2 \rangle) = L_1(s_1) \cup L_2(s_2)$.

- **יחס המעברים** $\to$ מוגדר על ידי חוקי הגזירה הבאים:

$$
\frac{s_1 \xrightarrow{\alpha}_1 s_1'}{ \langle s_1, s_2 \rangle \xrightarrow{\alpha} \langle s_1', s_2 \rangle } \quad \quad \frac{s_2 \xrightarrow{\alpha}_2 s_2'}{ \langle s_1, s_2 \rangle \xrightarrow{\alpha} \langle s_1, s_2' \rangle }
$$

הבחירה בין המעברים של $TS_1$ למעברים של $TS_2$ היא אי-דטרמיניסטית. <br>
(בשלב זה) אנו מניחים שאין תקשורת ואין משתנים משותפים.

---

# דוגמה: בנייה צעד-אחר-צעד

נראה איך כללי הגרירה בונים את המערכת השזורה עבור שתי המנורות:

<div class="grid grid-cols-2 gap-4">
<div>

<div v-click="1" class="text-sm bg-blue-50 p-2 rounded border border-blue-200 mb-2">

<b>שלב 1: החלת כלל 1 (מנורה 1 זזה)</b><br>
במנורה 1: $O \xrightarrow{next} D$. <br> 
לכן בשזירה: $\langle O,O \rangle \xrightarrow{n_1} \langle D,O \rangle$
</div>

<div v-click="3" class="text-sm bg-green-50 p-2 rounded border border-green-200 mb-2">

<b>שלב 2: החלת כלל 2 (מנורה 2 זזה)</b><br>
במנורה 2: $O \xrightarrow{next} D$. <br> 
לכן בשזירה: $\langle O,O \rangle \xrightarrow{n_2} \langle O,D \rangle$
</div>

<div v-click="5" class="text-sm bg-purple-50 p-2 rounded border border-purple-200">

<b>שלב 3: המשך הבנייה</b><br>
ממשיכים להחיל את הכללים על כל זוג מצבים וכל פעולה אפשרית עד לקבלת המערכת המלאה.
</div>

</div>

<div class="bg-slate-850 rounded-lg p-2 border flex items-center justify-center">
<TransitionSystemD3  
  :width="300" :height="350"
  :states="[
    { id: 'oo', text: 'O,O', initial: true, initialDirection: 'top', x: 300, y: 50,  width: 50 },
    ...($clicks >= 2 ? [{ id: 'do', text: 'D,O', x: 150, y: 50,  width: 50 }] : []),
    ...($clicks >= 4 ? [{ id: 'od', text: 'O,D', x: 300, y: 175, width: 50 }] : []),
    ...($clicks >= 5 ? [
      { id: 'bo', text: 'B,O', x: 0,   y: 50,  width: 50 },
      { id: 'dd', text: 'D,D', x: 150, y: 175, width: 50 },
      { id: 'bd', text: 'B,D', x: 0,   y: 175, width: 50 },
      { id: 'ob', text: 'O,B', x: 300, y: 300, width: 50 },
      { id: 'db', text: 'D,B', x: 150, y: 300, width: 50 },
      { id: 'bb', text: 'B,B', x: 0,   y: 300, width: 50 }
    ] : [])
  ]"
  :transitions="[
    ...($clicks >= 2 ? [{ source: 'oo', target: 'do', action: '$n_1$' }] : []),
    ...($clicks >= 4 ? [{ source: 'oo', target: 'od', action: '$n_2$' }] : []),
    ...($clicks >= 5 ? [
      { source: 'do', target: 'bo', action: '$n_1$' }, { source: 'bo', target: 'oo', action: '$r_1$', curve: -0.2, actionY:-5 },
      { source: 'od', target: 'dd', action: '$n_1$' }, { source: 'dd', target: 'bd', action: '$n_1$' }, { source: 'bd', target: 'od', action: '$r_1$', curve: 0.2, actionX:30, actionY:4 },
      { source: 'ob', target: 'db', action: '$n_1$' }, { source: 'db', target: 'bb', action: '$n_1$' }, { source: 'bb', target: 'ob', action: '$r_1$', curve: 0.2 },
      { source: 'od', target: 'ob', action: '$n_2$' }, { source: 'ob', target: 'oo', action: '$r_2$', curve: 0.3, actionX:5 },
      { source: 'do', target: 'dd', action: '$n_2$' }, { source: 'dd', target: 'db', action: '$n_2$' }, { source: 'db', target: 'do', action: '$r_2$', curve: -0.3, actionY: -20, actionX: -5 },
      { source: 'bo', target: 'bd', action: '$n_2$' }, { source: 'bd', target: 'bb', action: '$n_2$' }, { source: 'bb', target: 'bo', action: '$r_2$', curve: -0.3, actionX: -5 }
    ] : [])
  ]"
/>
</div>
</div>


---

# מגבלות השזירה הפשוטה ($|||$)

אופרטור השזירה ($|||$) מתאים למצבים בהם תתי-התהליכים פועלים באופן **בלתי-תלוי לחלוטין**, ללא העברת הודעות או מאבקים על משתנים משותפים.

אך עבור רוב המערכות המקביליות, האופרטור הזה הוא "פשוט מדי". 

**דוגמה: שזירה של תהליכים מתחרים**
נבחן שתי פקודות המשתמשות באותו משתנה $x$ (בהתחלה $x=3$):
$$\alpha \equiv x := 2x \hspace{1cm} \beta \equiv x := x+1$$

אופרטור השזירה הפשוט בונה את מכפלת מרחבי המצבים באופן "עיוור", מה שיוצר מצב לא עקבי כמו $\langle x=6, x=4 \rangle$:

<div class="flex justify-center items-center scale-75 -mt-17 space-x-4 rtl:space-x-reverse">

<!-- TS1 -->
<div class="flex flex-col items-center">
<TransitionSystemD3  
  :width="120" :height="150"
  :states="[{ id: 's3', text: 'x=3', initial: true, initialDirection: 'top', x: 60, y: 30, width: 70 }, { id: 's6', text: 'x=6', x: 60, y: 120, width: 70 }]"
  :transitions="[{ source: 's3', target: 's6', action: '$\\alpha$' }]"
/>
</div>

<div class="text-3xl font-bold text-slate-400 mx-2">|||</div>

<!-- TS2 -->
<div class="flex flex-col items-center">
<TransitionSystemD3  
  :width="120" :height="150"
  :states="[{ id: 's3b', text: 'x=3', initial: true, initialDirection: 'top', x: 60, y: 30, width: 70 }, { id: 's4', text: 'x=4', x: 60, y: 120, width: 70 }]"
  :transitions="[{ source: 's3b', target: 's4', action: '$\\beta$' }]"
/>
</div>

<div class="text-3xl font-bold text-slate-400 mx-2">=</div>

<!-- Product TS -->
<div class="flex flex-col items-center">
<TransitionSystemD3  
  :width="400" :height="200"
  :states="[
    { id: 's33', text: 'x=3, x=3', initial: true, initialDirection: 'top', x: 200, y: 30, width: 100 },
    { id: 's63', text: 'x=6, x=3', x: 80, y: 100,  width: 100 },
    { id: 's34', text: 'x=3, x=4', x: 320, y: 100, width: 100 },
    { id: 's64', text: 'x=6, x=4', x: 200, y: 170, width: 100, stroke: 'red', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 's33', target: 's63', action: '$\\alpha$' },
    { source: 's33', target: 's34', action: '$\\beta$' },
    { source: 's63', target: 's64', action: '$\\beta$' },
    { source: 's34', target: 's64', action: '$\\alpha$' }
  ]"
/>
</div>

</div>

<div class="-mt-8 ">

הבעיה: האופרטור לא מזהה שהמצבים המקומיים $x=6$ ו-$x=4$ הם **מאורעות מתנגשים** כי הם ניגשים לאותו משאב.

</div>

---

# שזירה של גרפי תוכנית (Interleaving of PGs)

כדי לטפל בתוכניות מקביליות עם **משתנים משותפים**, נגדיר אופרטור שזירה ברמת גרפי התוכנית (במקום ישירות על מערכות מעברים).

- השזירה של גרפי תוכנית $PG_1$ ו-$PG_2$ מסומנת ב-$PG_1 \,|||\, PG_2$.

- מערכת המעברים של התוצאה, $TS(PG_1 \,|||\, PG_2)$, מתארת נאמנה מערכת מקבילית שמרכיביה מתקשרים באמצעות משתנים משותפים.

- **שימו לב**: באופן כללי, $TS(PG_1 \,|||\, PG_2) \neq TS(PG_1) \,|||\, TS(PG_2)$.
  - השזירה ברמת ה-PG שומרת על הקשר בין הפעולות למשתנים.

<div class="flex justify-center -mt-20">
  <div class="bg-white p-4 rounded-xl shadow-lg border border-slate-100">
    <img src="/images/pg_interleaving_comic_he.png" class="h-75" />
  </div>
</div>

---

# הגדרה פורמלית: שזירה של גרפי תוכנית

יהיו $PG_i = (Loc_i, Act_i, Effect_i, \rightarrow_i, Loc_{0,i}, g_{0,i})$ עבור $i=1, 2$ שני גרפי תוכנית מעל משתנים $Var_i$. 
גרף התוכנית $PG_1 \,|||\, PG_2$ מעל $Var_1 \cup Var_2$ מוגדר ע"י:

$PG_1 \,|||\, PG_2 = (Loc_1 \times Loc_2, Act_1 \uplus Act_2, Effect, \rightarrow, Loc_{0,1} \times Loc_{0,2}, g_{0,1} \land g_{0,2})$

כאשר $\rightarrow$ מוגדר ע"י חוקי הגזירה:

$$
\frac{ \ell_1 \xrightarrow{g:\alpha}_1 \ell'_1 }{ \langle \ell_1, \ell_2 \rangle \xrightarrow{g:\alpha} \langle \ell'_1, \ell_2 \rangle } \quad \text{and} \quad \frac{ \ell_2 \xrightarrow{g:\alpha}_2 \ell'_2 }{ \langle \ell_1, \ell_2 \rangle \xrightarrow{g:\alpha} \langle \ell_1, \ell'_2 \rangle }
$$

ו-$Effect(\alpha, \eta) = Effect_i(\alpha, \eta)$ אם $\alpha \in Act_i$.

---

# משתנים משותפים לעומת מקומיים

בגרף התוכנית המשולב $PG_1 \,|||\, PG_2$:

1. **משתנים משותפים (Shared/Global Variables)**: המשתנים שנמצאים ב-$Var_1 \cap Var_2$. 
   - אלו משתנים ששני התהליכים יכולים לקרוא ולכתוב אליהם.
   - הם המנגנון המאפשר תקשורת בין התהליכים.

2. **משתנים מקומיים (Local Variables)**: 
   - $Var_1 \setminus Var_2$ הם המשתנים המקומיים של $PG_1$.
   - $Var_2 \setminus Var_1$ הם המשתנים המקומיים של $PG_2$.

<div class="mt-8 p-4 bg-orange-50 border-l-4 border-orange-400 text-orange-800">
💡 השזירה ברמת ה-PG מאפשרת לנו למדל נכון "מצבי תחרות" (Race Conditions) וגישה הדדית למשאבים, שכן כל צעד ב-TS המאוחד מעדכן את מצב המשתנים המשותף בצורה עקבית.
</div>


---

# דוגמה: שזירה עם משתנה משותף

נבחן שתי פקודות הפועלות על אותו משתנה $x$ המתחיל עם הערך 3: $(x:=2) \,|||\, (x:=x+1)$

<div class="grid grid-cols-2 gap-x-20 gap-y-4 scale-[0.7] origin-top -mt-5">

<!-- Individual PGs -->
<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-500 mb-2 underline">

$PG_1$
</h4>
<TransitionSystemD3  
  :width="200" :height="120"
  :states="[
    { id: 'l1',  text: '$\\ell_1$', initial: true, initialDirection: 'top', x: 100, y: 0, width: 40 },
    { id: 'l1p', text: '$\\ell_1\'$', x: 100, y: 90, width: 40 }
  ]"
  :transitions="[{ source: 'l1', target: 'l1p', action: '$x := 2 \\cdot x$',  actionY: -5 }]"
/>
</div>

<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-500 mb-2 underline">

$PG_2$
</h4>
<TransitionSystemD3  
  :width="200" :height="120"
  :states="[
    { id: 'l2',  text: '$\\ell_2$', initial: true, initialDirection: 'top', x: 100, y: 0, width: 40 },
    { id: 'l2p', text: '$\\ell_2\'$', x: 100, y: 90, width: 40 }
  ]"
  :transitions="[{ source: 'l2', target: 'l2p', action: '$x := x+1$', actionY: -5 }]"
/>
</div>

<!-- PG Interleaving -->
<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-600 mb-2">

גרף התוכנית $PG_1 \,|||\, PG_2$
</h4>
<TransitionSystemD3  
  :width="400" :height="100"
  :states="[
    { id: 'start', text: '$\\ell_1, \\ell_2$', initial: true, initialDirection: 'top', x: 200, y: 0,  width: 80, rx: 10 },
    { id: 'l1',    text: '$\\ell_1\', \\ell_2$', x: 80,  y: 80, width: 80, rx: 10 },
    { id: 'l2',    text: '$\\ell_1, \\ell_2\'$', x: 320, y: 80, width: 80, rx: 10 },
    { id: 'done',  text: '$\\ell_1\', \\ell_2\'$', x: 200, y: 160, width: 80, rx: 10 }
  ]"
  :transitions="[
    { source: 'start', target: 'l1',   action: '$x := 2 \\cdot x$', actionX: -30 },
    { source: 'start', target: 'l2',   action: '$x := x+1$', actionX: 30 },
    { source: 'l1',    target: 'done', action: '$x := x+1$', actionX: -30 },
    { source: 'l2',    target: 'done', action: '$x := 2 \\cdot x$', actionX: 30 }
  ]"
/>
</div>

<!-- TS Unfolding -->
<div class="flex flex-col items-center"> 
<h4 class="font-bold text-blue-700 mb-2">

מערכת המעברים $TS(PG_1 \,|||\, PG_2)$
</h4>
<TransitionSystemD3  
  :width="400" :height="100"
  :states="[
    { id: 's3', text: '$\\langle \\ell_1,   \\ell_2 \\rangle,   x{=}3$', initial: true, initialDirection: 'top', x: 200, y: 0,  width: 120, rx: 10 },
    { id: 's6', text: '$\\langle \\ell_1\', \\ell_2 \\rangle,   x{=}6$', x: 100, y: 80,    width: 120, rx: 10 },
    { id: 's4', text: '$\\langle \\ell_1,   \\ell_2\' \\rangle, x{=}4$', x: 300, y: 80,    width: 120, rx: 10 },
    { id: 's7', text: '$\\langle \\ell_1\', \\ell_2\' \\rangle, x{=}7$', x: 100, y: 160,   width: 120, rx: 10 },
    { id: 's8', text: '$\\langle \\ell_1\', \\ell_2\' \\rangle, x{=}8$', x: 300, y: 160,   width: 120, rx: 10 }
  ]"
  :transitions="[
    { source: 's3', target: 's6', action: ' ' },
    { source: 's3', target: 's4', action: ' ' },
    { source: 's6', target: 's7', action: ' ' },
    { source: 's4', target: 's8', action: ' ' }
  ]"
/>
</div>

</div>

<div class="-mt-20 text-sm">

  האי-דטרמיניזם במצב ההתחלתי מייצג את ה<b>תחרות (Contention)</b> על המשתנה המשותף $x$. <br>
  שימו לב שהתוצאה הסופית תלויה בסדר הביצוע: $x=7$ או $x=8$.
</div>

