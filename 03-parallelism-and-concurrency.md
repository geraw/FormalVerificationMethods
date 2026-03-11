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

<div class="flex justify-center -mt-10">
    <img src="/images/pg_interleaving_comic_he.png" class="w-70" style="clip-path: inset(25% 0 25% 0);" />
</div>

---

# הגדרה פורמלית: שזירה של גרפי תוכנית

יהיו $PG_i = (Loc_i, Act_i, Effect_i, \rightarrow_i, Loc_{0,i}, g_{0,i})$ עבור $i=1, 2$ שני גרפי תוכנית מעל משתנים $Var_i$. 
גרף התוכנית $PG_1 \,|||\, PG_2$ מעל $Var_1 \cup Var_2$ מוגדר ע"י:

$$PG_1 \,|||\, PG_2 = (Loc_1 \times Loc_2, Act_1 \uplus Act_2, Effect, \rightarrow, Loc_{0,1} \times Loc_{0,2}, g_{0,1} \land g_{0,2})$$

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

---

# פעולות קריטיות לעומת לא קריטיות

ההבחנה בין משתנים מקומיים למשותפים משפיעה על סיווג הפעולות ב-$PG_1 \,|||\, PG_2$:

1.  **פעולות קריטיות (Critical Actions)**: פעולות שניגשות (קריאה או כתיבה) למשתנים **משותפים**.

2.  **פעולות לא קריטיות (Noncritical Actions)**: פעולות הניגשות רק למשתנים **מקומיים**.

* פרשנות האי-דטרמיניזם ב-$TS(PG_1 \,|||\, PG_2)$ - אי-דטרמיניזם במצב של מערכת המעברים יכול לנבוע מ:
  - **בחירה פנימית**: בחירה אי-דטרמיניסטית בתוך $PG_1$ או $PG_2$ עצמם.

  - **שזירה של פעולות לא קריטיות**: הסדר אינו משנה לתוצאה הסופית. 
  - **תחרות (Contention)**: התנגשות בין פעולות קריטיות (Concurrency).

<div class="mt-4 p-4 bg-blue-50 border-r-4 border-blue-500 text-blue-900">

📌 <b>שימו לב:</b> פעולה לא קריטית של $PG_1$ יכולה להתבצע במקביל לכל פעולה של $PG_2$ מבלי להשפיע על נכונותה. לעומת זאת, פעולות קריטיות דורשות <b>אסטרטגיית תזמון</b> (Scheduling) כדי ליישב את התחרות על המשתנה המשותף.
</div>

---

# על אטומיות (Atomicity)

<div class="text-sm my-2 ml-4">

- בתהליך המידול של מערכת מקבילית באמצעות אופרטור השזירה, נקודת ההנחה המכרעת היא שהפעולות $\alpha \in Act$  **בלתי ניתנות לחלוקה**.
  - מערכת המעברים מבטאת רק את האפקט של הפעולה $\alpha$ לאחר שבוצעה במלואה.
  - אם פעולה מוגדרת ע"י רצף של פקודות, ההנחה היא שהמימוש **אינו מאפשר שזירה** עם תהליכים מקביליים אחרים.

- דוגמה לפעולה אטומית מורכבת:
נניח פעולה $\alpha$ המוגדרת ע"י רצף הפקודות:


<div class="flex justify-center -my-4 text-5 mb-4">

`x := x + 1; y := 2x + 1; if x < 12 then z := (x - z)^2 * y fi`

</div>


 האפקט הפורמלי $Effect(\alpha, \eta)$ מחושב כיחידה אחת:
</div>
<div class="text-left dir-ltr text-sm -my-8 ml-4">

$Effect(\alpha, \eta)(x) = \eta(x) + 1$<br><br>
$Effect(\alpha, \eta)(y) = 2(\eta(x) + 1) + 1$<br><br>
$Effect(\alpha, \eta)(z) = \begin{cases} (\eta(x) + 1 - \eta(z))^2 \cdot (2(\eta(x) + 1) + 1) & \text{if } \eta(x) + 1 < 12 \\ \eta(z) & \text{otherwise} \end{cases}$
</div>

<div class="mt-8 p-4 bg-orange-50 border-r-4 border-orange-500 text-orange-900 text-sm">

ניתן להצהיר על רצפי פקודות כאטומיים ע"י הצבתם כתווית בודדת על קשת בגרף התוכנית. בטקסט התוכנית, נקיף בלוקים כאלו בסוגריים משולשים: 
$\langle \text{statement}_1; \dots; \text{statement}_n \rangle$.
</div>

---

# דוגמה: מניעה הדדית (Mutual Exclusion) עם סמפורים

נבחן שני תהליכים $P_i$ (עבור $i=1, 2$) מהצורה הבאה:

<div class="flex justify-center my-4" dir="ltr">
<div class="border border-slate-300 p-6 rounded bg-white shadow-sm text-lg leading-relaxed w-fit text-left">
$$
\begin{array}{ll}
P_i & \mathbf{loop \ forever} \\
& \vdots \qquad \qquad \qquad \qquad (* \text{ noncritical actions } *) \\
& \mathit{request} \\
& \mathit{critical \ section} \\
& \mathit{release} \\
& \vdots \qquad \qquad \qquad \qquad (* \text{ noncritical actions } *) \\
& \mathbf{end \ loop}
\end{array}
$$
</div>
</div>

- התהליכים משתמשים בסמפור בינארי משותף $y$:
  - $y=1$: הסמפור חופשי.
  - $y=0$: הסמפור תפוס ע"י אחד התהליכים.

--

<div class="grid grid-cols-2 gap-x-10 scale-[0.8] origin-top">

<!-- PG1 -->
<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-500 mb-2">$PG_1$:</h4>
<TransitionSystemD3  
  :width="250" :height="220"
  :states="[
    { id: 'n1', text: '$noncrit_1$', initial: true, initialDirection: 'top', x: 125, y: 20, width: 100, rx:10 },
    { id: 'w1', text: '$wait_1$', x: 125, y: 100, width: 80, rx:10 },
    { id: 'c1', text: '$crit_1$', x: 125, y: 190, width: 80, rx:10 }
  ]"
  :transitions="[
    { source: 'n1', target: 'w1', action: ' ' },
    { source: 'w1', target: 'c1', action: '$y > 0 : y := y-1$', actionX: 60 },
    { source: 'c1', target: 'n1', action: '$y := y+1$', actionX: -70, type: 'curved', curve: -1 }
  ]"
/>
</div>

<!-- PG2 -->
<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-500 mb-2">$PG_2$:</h4>
<TransitionSystemD3  
  :width="250" :height="220"
  :states="[
    { id: 'n2', text: '$noncrit_2$', initial: true, initialDirection: 'top', x: 125, y: 20, width: 100, rx:10 },
    { id: 'w2', text: '$wait_2$', x: 125, y: 100, width: 80, rx:10 },
    { id: 'c2', text: '$crit_2$', x: 125, y: 190, width: 80, rx:10 }
  ]"
  :transitions="[
    { source: 'n2', target: 'w2', action: ' ' },
    { source: 'w2', target: 'c2', action: '$y > 0 : y := y-1$', actionX: 60 },
    { source: 'c2', target: 'n2', action: '$y := y+1$', actionX: -70, type: 'curved', curve: -60 }
  ]"
/>
</div>

</div>

<div class="-mt-12 text-sm bg-orange-50 p-3 rounded border border-orange-200">
💡 גרף התוכנית המשולב $PG_1 \,|||\, PG_2$ מורכב מ-9 מיקומים. 
ביניהם נמצא המיקום הלא-רצוי $\langle crit_1, crit_2 \rangle$, המייצג מצב שבו שני התהליכים נמצאים בו-זמנית בקטע הקריטי.
</div>

---

# גרף התוכנית המשולב $PG_1 \,|||\, PG_2$


<div class="grid grid-cols-[1fr_1fr_1fr] gap-x-0 items-center scale-[0.8] origin-top mr-5">

<!-- PG2 on the Left -->
<div class="flex flex-col items-center -mr-40">
<h4 class="font-bold text-slate-500 mb-6 text-xl">

$PG_2$
</h4>
<TransitionSystemD3  
  :width="150" :height="350"
  :states="[
    { id: 'n2', text: '$noncrit_2$', initial: true, initialDirection: 'top', x: 75, y: 0, width: 110, rx:8, color: '#fffde7' },
    { id: 'w2', text: '$wait_2$', x: 75, y: 160-50, width: 100, rx:8, color: '#fffde7' },
    { id: 'c2', text: '$crit_2$', x: 75, y: 270-50, width: 100, rx:8, color: '#fffde7' }
  ]"
  :transitions="[
    { source: 'n2', target: 'w2', action: ' ' },
    { source: 'w2', target: 'c2', action: '$y > 0 : y := y-1$', actionX: 0, actionWidth: 140 },
    { source: 'c2', target: 'n2', action: '$y := y+1$', actionX: -15, type: 'curved', curve: -0.8, actionWidth: 100 }
  ]"
/>
</div>

<!-- Interleaved PG in the Center -->
<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-500 mb-4 text-2xl">

$PG_1 \,|||\, PG_2$
</h4>
<TransitionSystemD3  
  :width="800" :height="500"
  :states="[
    { id: 'nn', text: '$\\langle n_1, n_2 \\rangle$', initial: true, initialDirection: 'top', x: 400, y: 0, width: 100, rx:8, color: '#fffde7' },
    { id: 'wn', text: '$\\langle w_1, n_2 \\rangle$', x: 280, y: 150-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'nw', text: '$\\langle n_1, w_2 \\rangle$', x: 520, y: 150-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'cn', text: '$\\langle c_1, n_2 \\rangle$', x: 180, y: 260-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'ww', text: '$\\langle w_1, w_2 \\rangle$', x: 400, y: 260-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'nc', text: '$\\langle n_1, c_2 \\rangle$', x: 620, y: 260-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'cw', text: '$\\langle c_1, w_2 \\rangle$', x: 280, y: 370-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'wc', text: '$\\langle w_1, c_2 \\rangle$', x: 520, y: 370-50, width: 90, rx:8, color: '#fffde7' },
    { id: 'cc', text: '$\\langle c_1, c_2 \\rangle$', x: 400, y: 460-50, width: 100, rx:8, color: '#fffde7' }
  ]"
  :transitions="[
    { source: 'nn', target: 'wn', action: ' ' },
    { source: 'nn', target: 'nw', action: ' ' },
    { source: 'wn', target: 'cn', action: '$y > 0 : y := y-1$', actionX: 20, actionWidth: 150 },
    { source: 'wn', target: 'ww', action: ' ' },
    { source: 'nw', target: 'nc', action: '$y > 0 : y := y-1$', actionX: -20, actionWidth: 150 },
    { source: 'nw', target: 'ww', action: ' ' },
    { source: 'cn', target: 'nn', action: '$y := y+1$', type: 'curved', curve: -0.6, actionWidth: 120, actionX: -10, actionY: 0 },
    { source: 'cn', target: 'cw', action: ' ' },
    { source: 'ww', target: 'cw', action: '$y > 0 : y := y-1$', actionX: -10, actionY: 10, actionWidth: 140 },
    { source: 'ww', target: 'wc', action: '$y > 0 : y := y-1$', actionX: 10, actionY: 10, actionWidth: 140 },
    { source: 'nc', target: 'nn', action: '$y := y+1$', type: 'curved', curve: 0.6, actionWidth: 120, actionX: 10, actionY: 0 },
    { source: 'nc', target: 'wc', action: ' ' },
    { source: 'cw', target: 'cc', action: ' ', type: 'curved', curve: 0.3 },
    { source: 'wc', target: 'cc', action: ' ', type: 'curved', curve: -0.3 },
    { source: 'cc', target: 'cn', action: '$y := y+1$', type: 'curved', curve: -0.6, actionX: -10, actionY: 0, actionWidth: 110 },
    { source: 'cc', target: 'nc', action: '$y := y+1$', type: 'curved', curve: 0.6, actionX: 10, actionY: 0, actionWidth: 110 }
  ]"
/>
</div>

<!-- PG1 on the Right -->
<div class="flex flex-col items-center">
<h4 class="font-bold text-slate-500 mb-6 text-xl">

$PG_1$
</h4>
<TransitionSystemD3  
  :width="150" :height="350"
  :states="[
    { id: 'n1', text: '$noncrit_1$', initial: true, initialDirection: 'top', x: 75, y: 0, width: 110, rx:8, color: '#fffde7' },
    { id: 'w1', text: '$wait_1$', x: 75, y: 160-50, width: 100, rx:8, color: '#fffde7' },
    { id: 'c1', text: '$crit_1$', x: 75, y: 270-50, width: 100, rx:8, color: '#fffde7' }
  ]"
  :transitions="[
    { source: 'n1', target: 'w1', action: ' ' },
    { source: 'w1', target: 'c1', action: '$y > 0 : y := y-1$', actionX: 0, actionWidth: 140 },
    { source: 'c1', target: 'n1', action: '$y := y+1$', actionX: -15, type: 'curved', curve: -0.8, actionWidth: 100 }
  ]"
/>
</div>

</div>

---

# ניתוח מערכת המעברים $TS(PG_1 \,|||\, PG_2)$:

- **מרחב המצבים**: כולל 18 מצבים גלובליים (שילוב של 9 מיקומים וערכי $y \in \{0, 1\}$).

- **אי-דטרמיניזם**: במצבים כמו $\langle n_1, n_2, y=1 \rangle$, שני התהליכים יכולים לפעול במקביל – האי-דטרמיניזם מייצג **שזירה של פעולות לא קריטיות**.

- **מניעה הדדית (Mutual Exclusion)**: ניתן להיווכח כי המצב $\langle crit_1, crit_2, y=\dots \rangle$ **אינו נגיש** (Unreachable) במערכת המעברים, ולכן דרישת המניעה ההדדית מתקיימת.

<div class="flex justify-center mt-4">
  <img src="/images/happy_tester.png" class="w-60" />
</div>

---

# פתרון קונפליקטי תזמון (Scheduling Contention)

במצב $\langle wait_1, wait_2, y=1 \rangle$, קיימת תחרות: מי ייכנס ראשון לקטע הקריטי?

### המודל כ"מופשט" (Abstract):
- האי-דטרמיניזם במודל הנוכחי משאיר את שאלת התזמון **פתוחה**.
- המודל אינו מפרט *כיצד* נפתרת התחרות בין $P_1$ ל-$P_2$.

### אסטרטגיות לפתרון:
1.  **מימוש הסמפור**: בשלבי תכנון מאוחרים יותר, ניתן לממש את $y$ באמצעות תור (Queue).
    - תור **FIFO** (First-In, First-Out)
    - תור **LIFO** (Last-In, First-Out)
2.  **אלגוריתמים קונקרטיים**: בחירת אלגוריתם מורכב יותר הפותר את הבעיה באופן מובנה.
    - דוגמה בולטת: **אלגוריתם פטרסון (Peterson's Algorithm, 1981)**, המבטיח מניעה הדדית ומונע הרעבה (Starvation) ללא צורך בסמפור חומרתי.

<div class=" flex justify-center">
  <div class="p-4 bg-blue-50 border-l-4 border-blue-500 text-blue-900 rounded shadow-sm">
    💡 במודלים פורמליים, אי-דטרמיניזם הוא כלי עוצמתי המאפשר לנו להוכיח תכונות (כמו מניעה הדדית) מבלי להתחייב מראש למדיניות תזמון ספציפית.
  </div>
</div>

---

# דוגמה: אלגוריתם פטרסון (Peterson's Algorithm)

פתרון קונקרטי לבעיית המניעה ההדדית עבור שני תהליכים ($P_1, P_2$).

<div class="grid grid-cols-2 gap-4 text-sm mb-4">
<div>

### משתנים משותפים:
- $b_1, b_2$ (Boolean): $b_i$ מסמן ש-$P_i$ מעוניין להיכנס לקטע הקריטי.
- $x \in \{1, 2\}$: קובע למי התור להיכנס במקרה של תחרות.

<br> 

### פסאודו-קוד ($P_1$):

<div class="text-left w-fit bg-slate-50 border border-slate-100 p-1 px-8 rounded overflow-hidden" dir="ltr">

```text
loop forever
  ... noncritical actions ...
  <b1 := true; x := 2>; // בקשה
  wait until (x = 1 ∨ ¬b2);
  ... critical section ...
  b1 := false; // שחרור
end loop
```

</div>
</div>

<div class="">

### מנגנון הפעולה
בכניסה ל-$wait_1$, תהליך $P_1$ מעלה את הדגל שלו ($b_1$) ונותן את התור ל-$P_2$ ($x:=2$).
$P_1$ ייכנס לקטע הקריטי רק אם $P_2$ לא מעוניין ($\neg b_2$) **או** אם הגיע תורו של $P_1$ ($x=1$).

<div class="flex justify-around gap-2 scale-[0.9] origin-bottom mt-auto">
<div class="flex flex-col items-center ml-15">
<h4 class="font-bold text-slate-500 mb-2 -mt-8 mr-0">      

$PG_1$
</h4>
    <TransitionSystemD3  
      :width="200" :height="120"
      :states="[
        { id: 'n1', text: '$n_1$', initial: true, initialDirection: 'top', x: 100, y: 0, width: 80, rx:8, color: '#e3f2fd' },
        { id: 'w1', text: '$w_1$', x: 100, y: 120-30, width: 80, rx:8, color: '#e3f2fd' },
        { id: 'c1', text: '$c_1$', x: 100, y: 210-30, width: 80, rx:8, color: '#e3f2fd' }
      ]"
      :transitions="[
        { source: 'n1', target: 'w1', action: '$b_1, x:=2$', actionX: 60, actionWidth: 120 },
        { source: 'w1', target: 'c1', action: '$x=1 \\lor \\neg b_2$', actionX: 60, actionWidth: 120 },
        { source: 'c1', target: 'n1', action: '$b_1:=F$', type: 'curved', curve: -0.7, actionX: -40 }
      ]"
    />
  </div>
  <div class="flex flex-col items-center">
    <h4 class="font-bold text-slate-500 mb-2 -mt-8">
    
$PG_2$ 
</h4>
    <TransitionSystemD3  
      :width="200" :height="120"
      :states="[
        { id: 'n2', text: '$n_2$', initial: true, initialDirection: 'top', x: 100, y: 0, width: 80, rx:8, color: '#f3e5f5' },
        { id: 'w2', text: '$w_2$', x: 100, y: 120-30, width: 80, rx:8, color: '#f3e5f5' },
        { id: 'c2', text: '$c_2$', x: 100, y: 210-30, width: 80, rx:8, color: '#f3e5f5' }
      ]"
      :transitions="[
        { source: 'n2', target: 'w2', action: '$b_2, x:=1$', actionX: 60, actionWidth: 120 },
        { source: 'w2', target: 'c2', action: '$x=2 \\lor \\neg b_1$', actionX: 60, actionWidth: 120 },
        { source: 'c2', target: 'n2', action: '$b_2:=F$', type: 'curved', curve: -0.7, actionX: -40 }
      ]"
    />
  </div>
</div>

</div>
</div>

---

# מערכת המעברים של אלגוריתם פטרסון ($TS_{pet}$)

החלק הנגיש של מערכת המעברים $TS(PG_1 \,|||\, PG_2)$ חושף את המנגנון המונע כניסה סימולטנית.

<div class="flex justify-center scale-[0.75] origin-top -mb-30 -mt-5">
<TransitionSystemD3  
  :width="1000" :height="400"
  :states="[
    { id: 'nn2', text: '$\\langle n_1, n_2, x=2 \\rangle$', initial: true, initialDirection: 'top', x: 350, y: 50, width: 140, rx:8, color: '#fffde7' },
    { id: 'nn1', text: '$\\langle n_1, n_2, x=1 \\rangle$', initial: true, initialDirection: 'top', x: 650, y: 50, width: 140, rx:8, color: '#fffde7' },
    { id: 'wn2', text: '$\\langle w_1, n_2, x=2 \\rangle$', x: 350, y: 150, width: 140, rx:8, color: '#fffde7' },
    { id: 'nw1', text: '$\\langle n_1, w_2, x=1 \\rangle$', x: 650, y: 150, width: 140, rx:8, color: '#fffde7' },
    { id: 'cn2', text: '$\\langle c_1, n_2, x=2 \\rangle$', x: 150, y: 150, width: 140, rx:8, color: '#fffde7' },
    { id: 'nc1', text: '$\\langle n_1, c_2, x=1 \\rangle$', x: 850, y: 150, width: 140, rx:8, color: '#fffde7' },
    { id: 'ww1', text: '$\\langle w_1, w_2, x=1 \\rangle$', x: 350, y: 250, width: 140, rx:8, color: '#fffde7' },
    { id: 'ww2', text: '$\\langle w_1, w_2, x=2 \\rangle$', x: 650, y: 250, width: 140, rx:8, color: '#fffde7' },
    { id: 'cw1', text: '$\\langle c_1, w_2, x=1 \\rangle$', x: 350, y: 350, width: 140, rx:8, color: '#fffde7' },
    { id: 'wc2', text: '$\\langle w_1, c_2, x=2 \\rangle$', x: 650, y: 350, width: 140, rx:8, color: '#fffde7' }
  ]"
  :transitions="[
    { source: 'nn2', target: 'wn2', action: ' ' },
    { source: 'nn2', target: 'nw1', action: ' ' },
    { source: 'nn1', target: 'wn2', action: ' ' },
    { source: 'nn1', target: 'nw1', action: ' ' },
    { source: 'wn2', target: 'ww1', action: ' ' },
    { source: 'wn2', target: 'cn2', action: ' ' },
    { source: 'nw1', target: 'ww2', action: ' ' },
    { source: 'nw1', target: 'nc1', action: ' ' },
    { source: 'cn2', target: 'nn2', action: ' ', type: 'curved', curve: -0.3 },
    { source: 'cn2', target: 'cw1', action: ' ', type: 'curved', curve: 0.3 },
    { source: 'nc1', target: 'nn1', action: ' ', type: 'curved', curve: 0.3 },
    { source: 'nc1', target: 'wc2', action: ' ', type: 'curved', curve: -0.3 },
    { source: 'ww1', target: 'cw1', action: ' ' },
    { source: 'ww2', target: 'wc2', action: ' ' },
    { source: 'cw1', target: 'nw1', action: ' '},
    { source: 'wc2', target: 'wn2', action: ' ' }
  ]"
/>
</div>

- **מרחב מצבים נגיש**: השמטנו מצבים לא נגישים שבהם למשל $x=1$ בזמן ש-$P_1$ רק התחיל לחכות.

- **הוכחת מניעה הדדית**: ניתן לראות כי מצבים מהצורה $\langle crit_1, crit_2, \dots \rangle$ **אינם נגישים** (Unreachable). 

<div class="absolute bottom-10 left-1">
  <img src="/images/happy_tester.png" class="w-40" />
</div>


---

# אטומיות וסוגיית סדר ההשמות

הערות על המימוש והנחות המודל באלגוריתם פטרסון.

-  אטומיות כפישוט (Abstraction) 
    - הסימון $\langle b_i := true; x := j \rangle$ מעיד על פעולה **אטומית** (בלתי ניתנת לחלוקה).

    - במציאות, הפעולות מבוצעות בזו אחר זו באופן לא אטומי.

    - אלגוריתם פטרסון מבטיח מניעה הדדית **גם ללא אטומיות**, כל עוד נשמר הסדר: קודם $b_i$ ואז $x$.


- אם נהפוך את הסדר (קודם $x$ ואז $b_i$), המניעה ההדדית **תופר**:


$$
\begin{array}{ll}
1. & \langle n_1, n_2, x=1, b_1=F, b_2=F \rangle \text{ (start)} \\
2. & \langle n_1, req_2, x=1, b_1=F, b_2=F \rangle \text{ (} P_2 \text{ performs } x:=1\text{)} \\
3. & \langle req_1, req_2, x=2, b_1=F, b_2=F \rangle \text{ (} P_1 \text{ performs } x:=2\text{)} \\
4. & \langle wait_1, req_2, x=2, b_1=T, b_2=F \rangle \text{ (} P_1 \text{ performs } b_1:=T\text{)} \\
5. & \langle crit_1, req_2, x=2, b_1=T, b_2=F \rangle \text{ (} P_1 \text{ enters as } b_2=F\text{)} \\
6. & \langle crit_1, wait_2, x=2, b_1=T, b_2=T \rangle \text{ (} P_2 \text{ performs } b_2:=T\text{)} \\
7. & \langle crit_1, crit_2, x=2, b_1=T, b_2=T \rangle \text{ (} P_2 \text{ enters as } x=2\text{)} \quad \leftarrow \text{Collision!}
\end{array}
$$ 

---

# סנכרון בלחיצת יד (Handshaking Synchronization)

עד כה ראינו שזירה (Interleaving) ותוכניות עם משתנים משותפים. כעת נבחן מנגנון תקשורת **סינכרוני**.

### מהי "לחיצת יד" (Handshaking)?
תהליכים המתקשרים באמצעות לחיצת יד חייבים לעשות זאת באופן סינכרוני:
- אינטראקציה מתרחשת רק אם **שני הצדדים** משתתפים בה בו-זמנית.
- הם "לוחצים ידיים" כדי להעביר מידע או לסנכרן צעדים.

<br>

### פעולות לחיצת יד ($H$):
נגדיר קבוצת פעולות $H \subseteq Act$ המייצגות לחיצות יד (כאשר $\tau \notin H$):
1.  **פעולות סינכרוניות ($h \in H$):** יכולות להתבצע רק אם שני התהליכים מוכנים לבצע את אותה פעולה $h$ בו-זמנית.
2.  **פעולות עצמאיות ($a \in Act \setminus H$):** מבוצעות באופן אוטונומי בשזירה (Interleaving), ללא תלות בתהליך השני.

<div class="mt-2 flex justify-center">
  <div class="p-4 bg-emerald-50 border-r-4 border-emerald-500 text-emerald-900 rounded shadow-sm">
    💡 בתפיסה זו, אנו מתמקדים בעצם קיום הסנכרון (Synchronization) ולאו דווקא בתוכן ההודעה המועברת.
  </div>
</div>

<img src="/handshaking_robots_comic.png" class="absolute top-30 left-10 w-60" />

---

# קבוצת לחיצות יד ריקה

<img src="/independent_robots.png" class="absolute bottom-0 right-70 w-100" />

כאשר קבוצת לחיצות היד $H$ היא ריקה, כל הפעולות של התהליכים המשתתפים יכולות להתבצע באופן אוטונומי.
במקרה זה, מנגנון לחיצת היד מצטמצם לשזירה רגילה:

$$TS_1 \parallel_{\emptyset} TS_2 = TS_1 \, ||| \,  TS_2$$

---

# תכונות של אופרטור לחיצת היד ($\|_H$)

אופרטור לחיצת היד מגדיר סנכרון בין מערכות מעברים, ולו מספר תכונות חשובות:

- **קומוטטיביות:** האופרטור הוא קומוטטיבי: $TS_1 \|_H TS_2 = TS_2 \|_H TS_1$.
- **אסוציאטיביות:** האופרטור **אינו** אסוציאטיבי באופן כללי (עבור קבוצות $H$ שונות).
- עבור קבוצה קבועה $H$, האופרטור הוא **כן** אסוציאטיבי.

<br>

### לחיצת יד רב-צדדית (Multiway Handshaking)
ניתן להרחיב את המנגנון לסנכרון של $n$ תהליכים:
$$TS = TS_1 \, \|_H  \, TS_2 \, \|_H \, \cdots \, \|_H \, TS_n$$
כאשר $H \subseteq Act_1 \cap \dots \cap Act_n$ היא תת-קבוצה של פעולות המשותפות לכלל המערכות.


### שידור (Broadcasting)
סנכרון רב-צדדי מתאים במיוחד למידול **שידור (Broadcasting)**: 
מצב שבו תהליך אחד משדר נתון למספר תהליכים אחרים שקולטים אותו בו-זמנית ("לוחצים ידיים" כולם יחד).

---

# סנכרון בזוגות (Pairwise Handshaking)

במקרים רבים, תהליכים מתקשרים בזוגות על בסיס פעולות המשותפות להם.

עבור $n$ מערכות מעברים, $TS_i$ ו-$TS_j$ מסתנכרנות מעל קבוצת הפעולות $H_{i,j} = Act_i \cap Act_j$.
המצב הגלובלי מוגדר כ-$\langle s_1, \dots, s_n \rangle$.

**חוק 1: פעולה אוטונומית (עבור $\alpha \notin \bigcup H_{i,j}$)**
פעולות שאינן דורשות לחיצת יד מבוצעות באופן עצמאי:

$$
\frac{s_i \xrightarrow{\alpha} s'_i}{\langle s_1, \dots, s_i, \dots, s_n \rangle \xrightarrow{\alpha} \langle s_1, \dots, s'_i, \dots, s_n \rangle}
$$

**חוק 2: פעולה סינכרונית (עבור $\alpha \in H_{i,j}$)**
שני תהליכים חייבים לבצע את הפעולה המשותפת יחד:

$$
\frac{s_i \xrightarrow{\alpha} s'_i \wedge s_j \xrightarrow{\alpha} s'_j}{\langle s_1, \dots, s_i, \dots, s_j, \dots, s_n \rangle \xrightarrow{\alpha} \langle s_1, \dots, s'_i, \dots, s'_j, \dots, s_n \rangle}
$$

**סיכום:**
החוק הראשון מאפשר ביצוע פעולות בשזירה (Interleaving), בעוד החוק השני דורש תיאום מוחלט בין המשתתפים בלחיצת היד.

---

# דוגמה: מניעה הדדית באמצעות בורר (Arbiter)

פתרון חלופי לבעיית המניעה ההדדית בין $P_1$ ו-$P_2$ הוא שימוש בתהליך חיצוני – **הבורר (Arbiter)**.



<div class="grid grid-cols-2 gap-4">

<div>


**תהליך $T_i$ (עבור $i \in \{1,2ew\}$):**

<div class="grid grid-rows-2 gap-0 -mt-15">

<TransitionSystemD3
  :width="400" :height="130"
  :states="[
    { id: 'n', text: '$noncrit_1$', initial: true, x: 100, y: 100,  width:90 },
    { id: 'c', text: '$crit_1$', x: 300, y: 100 }
  ]"
  :transitions="[
    { source: 'n', target: 'c', action: 'request', type: 'curved', curve: 0.5, actionY:10 },
    { source: 'c', target: 'n', action: 'release', type: 'curved', curve: 0.5, actionY:-10 }
  ]"
/>

<TransitionSystemD3
  :width="400" :height="110"
  :states="[
    { id: 'n', text: '$noncrit_2$', initial: true, x: 100, y: 100,  width:90 },
    { id: 'c', text: '$crit_2$', x: 300, y: 100 }
  ]"
  :transitions="[
    { source: 'n', target: 'c', action: 'request', type: 'curved', curve: 0.5, actionY:10 },
    { source: 'c', target: 'n', action: 'release', type: 'curved', curve: 0.5, actionY:-10 }
  ]"
/>

</div>
</div>
<div>

**הבורר (Arbiter):**
<div class="mt-4 flex justify-center scale-100 origin-top">


<TransitionSystemD3
  :width="60" :height="200"
  :states="[
    { id: 'unlock', text: 'unlock', initial: true, x: 0, y: 0, width:90 },
    { id: 'lock', text: 'lock', x: 0, y: 150, width:90 }
  ]"
  :transitions="[
    { source: 'unlock', target: 'lock', action: 'request', type: 'curved', curve: 0.5 },
    { source: 'lock', target: 'unlock', action: 'release', type: 'curved', curve: 0.5 }
  ]"
/>
</div>
</div>
</div>

---

# שזירת התהליכים עצמם

ללא בורר, התהליכים פועלים בשזירה רגילה (Interleaving). המצב $\langle crit_1, crit_2 \rangle$ אפשרי בגרף זה.

<div class="flex items-center justify-center gap-8 mt-10">
<div class="scale-110">
<TransitionSystemD3
  :width="400" :height="300"
  :states="[
    { id: 'nn', text: '$n_1, n_2$', initial: true, x: 200, y: 50, color: '#e3f2fd' },
    { id: 'cn', text: '$c_1, n_2$', x: 80, y: 150, color: '#e3f2fd' },
    { id: 'nc', text: '$n_1, c_2$', x: 320, y: 150, color: '#e3f2fd' },
    { id: 'cc', text: '$c_1, c_2$', x: 200, y: 250, color: '#ffebee' }
  ]"
  :transitions="[
    { source: 'nn', target: 'cn', action: 'request', curve: 0.2 },
    { source: 'nn', target: 'nc', action: 'request', curve: 0.2 },
    { source: 'cn', target: 'cc', action: 'request', curve: 0.2 },
    { source: 'nc', target: 'cc', action: 'request', curve: 0.2 },
    { source: 'cc', target: 'cn', action: 'release', curve: 0.2 },
    { source: 'cc', target: 'nc', action: 'release', curve: 0.2 },
    { source: 'cn', target: 'nn', action: 'release', curve: 0.2 },
    { source: 'nc', target: 'nn', action: 'release', curve: 0.2 }
  ]"
/>
</div>
  <div class="text-4xl font-mono text-slate-400">
  
  $T_1 \,|||\, T_2 \,\, =$
  </div>


</div>

---

# המערכת המשולבת עם בורר

כאשר מחברים את השזירה לבורר באמצעות לחיצת יד על הקבוצה $H = \{request, release\}$, מתקבל גרף שבו מובטחת מניעה הדדית.

<div class="flex items-center justify-center gap-8 mt-10">
<div class="scale-100">
<TransitionSystemD3
  :width="500" :height="250"
  :states="[
    { id: 'nnu', text: '$n_1, n_2, unlock$', initial: true, x: 250, y: 50, color: '#f1f8e9', width:140 },
    { id: 'cnl', text: '$c_1, n_2, lock$', x: 100, y: 180, color: '#f1f8e9', width:120 },
    { id: 'ncl', text: '$n_1, c_2, lock$', x: 400, y: 180, color: '#f1f8e9', width:120 }
  ]"
  :transitions="[
    { source: 'nnu', target: 'cnl', action: 'request', type: 'curved', curve: 0.2 },
    { source: 'cnl', target: 'nnu', action: 'release', type: 'curved', curve: 0.2 },
    { source: 'nnu', target: 'ncl', action: 'request', type: 'curved', curve: -0.2 },
    { source: 'ncl', target: 'nnu', action: 'release', type: 'curved', curve: -0.2 }
  ]"
/>
</div>
<div class="text-2xl font-mono text-slate-400">
  
  $(T_1 \,|||\, T_2) \parallel Arbiter \,\, =$
</div>

</div>

<div class="mt-8 text-center text-emerald-700 font-bold">
  
  💡 המצב $\langle crit_1, crit_2, lock \rangle$ אינו נגיש – מניעה הדדית מובטחת!
</div>


<div class="absolute bottom-5 left-10">
  <img src="/images/happy_tester.png" class="w-40" />
</div>

---

# דוגמה: מערכת רישום (Booking System)

מערכת המורכבת משלושה רכיבים: קורא ברקוד (BCR), תוכנית רישום (BP) ומדפסת (Printer).

<div class="grid grid-cols-4 gap-2 scale-[0.7] origin-top">

<div class="flex flex-col items-center">
<h4 class="font-bold -mb-10">BCR</h4>
<TransitionSystemD3 :width="150" :height="150"
  :states="[
    { id: '0b', text: '0', initial: true, x: 75, y: 30 },
    { id: '1b', text: '1', x: 75, y: 120 }
]"
  :transitions="[{source:'0b', target:'1b', action:'scan', curve:0.5, actionX:-10}, {source:'1b', target:'0b', action:'store', curve:0.5, actionX:10}]" />
</div>

<div class="flex flex-col items-center">
<h4 class="font-bold -mb-10">BP</h4>
<TransitionSystemD3 :width="150" :height="150"
  :states="[{id:'0p', text:'0', initial:true, x:75, y:30}, {id:'1p', text:'1', x:75, y:120}]"
  :transitions="[{source:'0p', target:'1p', action:'store', curve:0.5, actionX:-10}, {source:'1p', target:'0p', action:'$prt\\_cmd$', curve:0.5, actionX:10}]" />
</div>

<div class="flex flex-col items-center">
<h4 class="font-bold -mb-10">Printer</h4>
<TransitionSystemD3 :width="150" :height="150"
  :states="[{id:'0r', text:'0', initial:true, x:75, y:30}, {id:'1r', text:'1', x:75, y:120}]"
  :transitions="[{source:'0r', target:'1r', action:'$prt\\_cmd$', curve:0.5, actionX:-10}, {source:'1r', target:'0r', action:'print', curve:0.5, actionX:10}]" />
</div>

<div class="flex flex-col justify-center items-center p-4 bg-blue-50 border border-blue-200 rounded text-sm">
<b>לחיצות יד:</b>
<br>
BCR ↔ BP : {store}
<br>
BP ↔ Printer : {prt_cmd}
</div>

</div>

<div class="flex flex-col items-center scale-70 -mt-20">
<h4 class="font-bold text-blue-700 -mb-15">

המערכת הכוללת: $BCR \,||\, BP \,||\, Printer$
</h4>

<TransitionSystemD3 :width="800" :height="300"
:states="[
    { id: '000', text: '000', initial: true, initialDirection: 'top', x: 210, y: 190 },
    { id: '100', text: '100', x: 20, y: 190 },
    { id: '010', text: '010', x: 420, y: 330 },
    { id: '001', text: '001', x: 340, y: 190 },
    { id: '110', text: '110', x: 500, y: 190 },
    { id: '101', text: '101', x: 420, y: 50 },
    { id: '011', text: '011', x: 820, y: 190 },
    { id: '111', text: '111', x: 630, y: 190 }
]"
  :transitions="[
    { source: '000', target: '100', action: 'scan' },
    { source: '100', target: '010', action: 'store' },
    { source: '010', target: '110', action: 'scan' },
    { source: '010', target: '001', action: '$prt\\_cmd$' },
    { source: '110', target: '101', action: '$prt\\_cmd$' },
    { source: '001', target: '000', action: 'print'},
    { source: '001', target: '101', action: 'scan' },
    { source: '101', target: '100', action: 'print'},
    { source: '101', target: '011', action: 'store' },
    { source: '011', target: '010', action: 'print'},
    { source: '011', target: '111', action: 'scan' },
    { source: '111', target: '110', action: 'print'}
  ]"
/>
</div>

---

# דוגמה: מחסום רכבת (Railroad Crossing)

במחסום רכבת, המערכת צריכה לסגור את המחסום עם קבלת אות שהרכבת מתקרבת, ולפתוח אותו רק לאחר שהרכבת חצתה את הכביש. 

<div class="grid grid-cols-3 gap-2 scale-[0.7] origin-top -mb-10"> 

<div class="flex flex-col items-center">
<h4 class="font-bold -mb-8">רכבת (Train)</h4>
<TransitionSystemD3 :width="200" :height="150"
  :states="[
    {id:'far', text:'far', initial:true, x:100, y:30}, 
    {id:'near', text:'near', x:170, y:120},
    {id:'in', text:'in', x:30, y:120}
  ]"
  :transitions="[
    {source:'far', target:'near', action:'approach'}, 
    {source:'near', target:'in', action:'enter'},
    {source:'in', target:'far', action:'exit'}
  ]" />
</div>

<div class="flex flex-col items-center">
<h4 class="font-bold -mb-8">בקר (Controller)</h4>
<TransitionSystemD3 :width="150" :height="150"
  :states="[
    {id:'c0', text:'0', initial:true, x:0, y:30}, 
    {id:'c1', text:'1', x:150, y:30},
    {id:'c2', text:'2', x:150, y:120},
    {id:'c3', text:'3', x:0, y:120}
  ]"
  :transitions="[
    {source:'c0', target:'c1', action:'approach'}, 
    {source:'c1', target:'c2', action:'lower'},
    {source:'c2', target:'c3', action:'exit'},
    {source:'c3', target:'c0', action:'raise'}
  ]" />
</div>

<div class="flex flex-col items-center">
<h4 class="font-bold -mb-8">מחסום (Gate)</h4>
<TransitionSystemD3 :width="150" :height="150"
  :states="[{id:'up', text:'up', initial:true, x:75, y:30}, {id:'down', text:'down', x:75, y:120}]"
  :transitions="[{source:'up', target:'down', action:'lower', curve:0.5, actionX:-10}, {source:'down', target:'up', action:'raise', curve:0.5, actionX:10}]" />
</div>

</div>

- **הרכבת (Train):** נעה בין המצבים far (רחוקה), near (מתקרבת) ו-in (במפגש).

- **השער (Gate):** פתוח (up) או סגור (down).

- **הבקר (Controller):** מתאם בין הרכבת לשער. 
  - הוא מקבל התראות מהרכבת (approach, exit) ושולח פקודות לשער (lower, raise).

**הדרישה הבטיחותית:** המחסום חייב להיות סגור תמיד כשהרכבת חוצה את המפגש. כפי שנראה מיד, מודל השזירה חושף כשל תכנוני שבו הרכבת נכנסת לפני שהשער נסגר.


---

# מערכת המעברים המורכבת של מחסום הרכבת

<div class="flex flex-col items-center scale-40">
<TransitionSystemD3 :width="600" :height="50"
  :states="[
    { id: '00up', text: '〈far, 0, up〉', initial: true, initialDirection: 'top', x: 400, y:0, width: 150 },
    { id: '11up', text: '〈near, 1, up〉',          x: 400,     y: 150-50, width: 150 },
    { id: '22down', text: '〈near, 2, down〉',      x: 250,     y: 250-50, width: 180 },
    { id: '11up_bad', text: '〈in, 1, up〉',        x: 550,     y: 250-50, stroke: 'red', strokeWidth: 3, width: 150 },
    { id: '22down_in', text: '〈in, 2, down〉',     x: 250,     y: 350-50, width: 180 },
    { id: '11up_far', text: '〈far, 1, up〉',       x: 550,     y: 350-50, width: 150 },
    { id: '22down_far', text: '〈far, 2, down〉',   x: 550,     y: 450-50, width: 200 },
    { id: '33down', text: '〈far, 3, down〉',       x: 400-150, y: 500-50, width: 200 },
    { id: '33down_near', text: '〈near, 3, down〉', x: 400-150, y: 600-50, width: 200 },
    { id: '00up_near', text: '〈near, 0, up〉',     x: 550-150, y: 700-50, width: 200 },
    { id: '33down_in', text: '〈in, 3, down〉',     x: 250-150, y: 700-50, width: 200 },
    { id: '00up_in', text: '〈in, 0, up〉',         x: 400-150, y: 800-50, width: 200 },
  ]"
  :transitions="[
    { source: '00up', target: '11up', action: 'approach', stroke: 'red', strokeWidth: 4, actionY: -15 },
    { source: '11up', target: '22down', action: 'lower' },
    { source: '11up', target: '11up_bad', action: 'enter', stroke: 'red', strokeWidth: 4 },
    { source: '22down', target: '22down_in', action: 'enter' },
    { source: '11up_bad', target: '11up_far', action: 'exit' },
    { source: '11up_bad', target: '22down_in', action: 'lower' },
    { source: '11up_far', target: '22down_far', action: 'lower' },
    { source: '11up_far', target: '11up', action: 'approach', midPoints: [{ x: 700, y: 300 }, { x: 700, y: 100 }], actionY: 100 },
    { source: '22down_far', target: '22down', action: 'approach' },
    { source: '22down_in', target: '33down', action: 'exit' },
    { source: '33down', target: '33down_near', action: 'approach' },
    { source: '33down', target: '00up', action: 'raise', midPoints: [{ x: 50, y: 450 }, { x: 50, y: 0 }], actionY: 100 },
    { source: '33down_near', target: '33down_in', action: 'enter' },
    { source: '33down_near', target: '00up_near', action: 'raise' },
    { source: '33down_in', target: '00up_in', action: 'exit' },
    { source: '33down_in', target: '33down', action: 'exit', curve: -0.5 },
    { source: '00up_near', target: '00up_in', action: 'enter' },
    { source: '00up_in', target: '00up', action: 'exit', midPoints: [{ x: -40, y: 750 }, { x: -40, y: 0 }], actionY: 100 }
  ]"
/>
</div>

<div class="mt-70 text-sm bg-red-50 p-3 rounded border border-red-200">
⚠️ <b>הבעיה:</b> בשל השזירה (Interleaving), הרכבת יכולה להיכנס למפגש (enter) <b>לפני</b> שהמחסום ירד.  
זוהי הוכחה שהמודל הזה אינו מספיק: במציאות המערכת בטוחה רק אם הורדת המחסום מהירה יותר מהגעת הרכבת.  
<i>(בהמשך הקורס נלמד איך למדל אילוצי זמן אמת כאלו)</i>
</div>

---

# מערכות ערוצים (Channel Systems)

מערכת מקבילית שבה תהליכים מתקשרים דרך **ערוצים (Channels)** — חוצצים מסוג FIFO שמכילים הודעות.

- מערכות ערוצים הן **סגורות**: תהליכים מתקשרים רק עם תהליכים אחרים במערכת, לא עם העולם החיצוני.
- מהוות את הבסיס לשפת **Promela** — שפת הקלט של מאמת המודלים **SPIN**.

<div class="mt-4">

**פעולות תקשורת (Communication Actions):**

$$Comm = \{c!v,\ c?x \mid c \in Chan,\ v \in dom(c),\ x \in Var \text{ with } dom(x) \supseteq dom(c)\}$$

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="bg-blue-50 p-3 rounded border border-blue-200">

**שליחה: $c!v$**  
שולח את הערך $v$ לסוף החוצץ של ערוץ $c$.

</div>
<div class="bg-green-50 p-3 rounded border border-green-200">

**קבלה: $c?x$**  
קורא הודעה מראש החוצץ של ערוץ $c$ <br>
ושם אותה במשתנה $x$.

</div>
</div>

- כל תהליך $P_i$ מוגדר ע"י **גרף תוכנית** $PG_i$ המורחב עם פעולות תקשורת.
- המעברים בגרף הם: מעברים מותנים רגילים (שמירות ופעולות), **או** פעולות תקשורת ($c!v$ / $c?x$).

---

# ערוצים: קיבולת וטיפוסים

לכל ערוץ $c$ שני מאפיינים:

- **תחום (Domain):** $dom(c)$ - טיפוס ההודעות שניתן לשדר.
  - לדוגמה: $dom(c) = \{0, 1\}$ לערוץ ביטים, או $dom(c) = \Sigma^{200}$ לטקסטים.

- **קיבולת (Capacity):** $cap(c) \in \mathbb{N} \cup \{\infty\}$ - מספר ההודעות המרבי שניתן לאחסן בחוצץ.

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="bg-orange-50 p-4 rounded border border-orange-200">

**$cap(c) = 0$ - סינכרוני**

אין חוצץ. התקשורת היא **Handshaking**: שליחה וקבלה מתרחשות **בו-זמנית**.

מקביל למנגנון ה-Handshaking שכבר ראינו!

</div>
<div class="bg-purple-50 p-2 rounded border border-purple-200">

**$cap(c) > 0$ - א-סינכרוני**

יש חוצץ. שליחה וקבלה מתרחשות **ברגעים שונים** - יש עיכוב בין שליחה לקריאה.

שליחה וקריאה של אותה הודעה <br>
 **לעולם אינן בו-זמניות**.

</div>
</div>


מערכות ערוצים מאפשרות מידול של **שני** סוגי התקשורת: סינכרונית וא-סינכרונית.

---

# הגדרה פורמלית: מערכת ערוצים 

**גרף תוכנית מעל $(Var, Chan)$** הוא סדורה:

$$PG = (Loc,\ Act,\ Effect,\ \rightarrow,\ Loc_0,\ g_0)$$

כמו בהגדרה של גרף תוכנית רגיל, עם ההבדל שיחס המעברים מורחב לכלול פעולות תקשורת:

$$\rightarrow\ \subseteq\ Loc \times \big(Cond(Var) \times (Act \cup {\color{red} Comm})\big) \times Loc$$

<div class="mt-6 bg-blue-50 p-4 rounded border border-blue-200">

**מערכת ערוצים** $CS$ מעל $(Var, Chan)$ מורכבת מגרפי תוכנית $PG_i$ מעל $(Var_i, Chan)$ כאשר $Var = \bigcup_{1 \leq i \leq n} Var_i$:

$$CS = [PG_1 \mid \ldots \mid PG_n]$$

</div>

- הסימון $[\cdot | \cdot]$ מציין הרכבה מקבילית של תהליכים עם תקשורת דרך ערוצים.
- כל תהליך $PG_i$ יכול לבצע פעולות מקומיות **או** פעולות תקשורת ($c!v$ / $c?x$).

---

# מתי פעולות תקשורת בנות-ביצוע?

<div class="grid grid-cols-2 gap-4">
<div class="bg-orange-50 p-3 rounded border border-orange-200">

**Handshaking: $cap(c) = 0$**

תהליך $P_i$ יכול לשלוח $c!v$ **רק אם** תהליך אחר $P_j$ מציע פעולת קבלה משלימה $c?x$ **בו-זמנית**.

שני התהליכים מבצעים את הפעולה **יחד**, והאפקט הוא השמה מבוזרת:

$$x := v$$

</div>
<div class="bg-purple-50 p-3 rounded border border-purple-200">

**א-סינכרוני: $cap(c) > 0$**

- **שליחה** $c!v$: בר-ביצוע אם הערוץ **אינו מלא** (פחות מ-$cap(c)$ הודעות). הערך $v$ נכנס לסוף החוצץ.

- **קבלה** $c?x$: בר-ביצוע אם החוצץ **אינו ריק**. האיבר הראשון נשלף ומושם ב-$x$.

</div>
</div>

<div class="mt-4">

| | ...בר-ביצוע אם | אפקט |
|:---:|:---:|:---:|
| $c!v$ | הערוץ $c$ לא מלא | $Enqueue(c, v)$ |
| $c?x$ | הערוץ $c$ לא ריק | $x := Front(c);\ Dequeue(c)$ |

</div>

---

# דוגמה: פרוטוקול הביט המתחלף (ABP)

<img src="/images/abp_channels_comic.png" class="absolute bottom-0 left-0 w-70" />

מערכת תקשורת בין שולח $S$ ומקבל $R$ דרך שני ערוצים:

- **ערוץ $c$** (שולח $\to$ מקבל): לא אמין - הודעות עלולות **ללכת לאיבוד**.
  - $cap(c) = \infty$ (חוצץ אינסופי)
- **ערוץ $d$** (מקבל $\to$ שולח): אמין לחלוטין.
  - $cap(d) = \infty$

**עיקרון Send-and-Wait:** $S$ שולח הודעה ומחכה לאישור (ACK) לפני שליחת ההודעה הבאה.

**ביט בקרה מתחלף:** ההודעות נשלחות כזוגות $\langle m, b \rangle$ כאשר $b \in \{0,1\}$:

$$\langle m_0, 0 \rangle,\ \langle m_1, 1 \rangle,\ \langle m_2, 0 \rangle,\ \langle m_3, 1 \rangle,\ \ldots$$

- $R$ מקבל $\langle m, b \rangle$ ושולח ACK עם ביט $b$ חזרה דרך $d$.
- $S$ מקבל ACK עם $b$ ושולח הודעה חדשה עם ביט $\neg b$.
- אם $S$ מחכה זמן רב מדי - מתרחש **timeout** והוא שולח מחדש.


---

# ABP: גרפי התוכנית

<div class="relative h-[400px] w-full" dir="ltr">

<!-- Sender S -->
<div class="absolute -top-10 -left-10 scale-[0.6] origin-top-left">
  <h4 class="font-bold mb-15 text-center">שולח (Sender S)</h4>
  <TransitionSystemD3 :width="900" :height="250"
    :states="[
      { id: 'snd0', text: 'snd_msg(0)', initial: true, initialDirection: 'top', x: 80, y: 50, width: 130, rx: 20 },
      { id: 'st0', text: 'st_tmr(0)', x: 310, y: 50, width: 110, rx: 20 },
      { id: 'wait0', text: 'wait(0)', x: 540, y: 50, width: 90, rx: 20 },
      { id: 'chk0', text: 'chk_ack(0)', x: 770, y: 50, width: 130, rx: 20 },
      { id: 'chk1', text: 'chk_ack(1)', x: 80, y: 230, width: 130, rx: 20 },
      { id: 'wait1', text: 'wait(1)', x: 310, y: 230, width: 90, rx: 20 },
      { id: 'st1', text: 'st_tmr(1)', x: 540, y: 230, width: 110, rx: 20 },
      { id: 'snd1', text: 'snd_msg(1)', x: 770, y: 230, width: 130, rx: 20 }
    ]"
    :transitions="[
      { source: 'snd0', target: 'st0', action: 'c!⟨m,0⟩' },
      { source: 'snd0', target: 'st0', action: 'lost', curve: 0.2, actionY: 8 },
      { source: 'st0', target: 'wait0', action: 'tmr_on!' },
      { source: 'wait0', target: 'chk0', action: 'd?x' },
      { source: 'chk0', target: 'snd1', action: 'x=0: tmr_off!' },
      { source: 'chk0', target: 'snd0', action: 'x=1', curve: 0.2, actionY: -10 },
      { source: 'wait0', target: 'snd0', action: 'timeout?', curve: 0.2, actionY: -5, actionX: 40 },
      { source: 'snd1', target: 'st1', action: 'c!⟨m,1⟩' },
      { source: 'snd1', target: 'st1', action: 'lost', curve: 0.2, actionY: -8 },
      { source: 'st1', target: 'wait1', action: 'tmr_on!' },
      { source: 'wait1', target: 'chk1', action: 'd?x' },
      { source: 'chk1', target: 'snd0', action: 'x=1 : tmr_off!' },
      { source: 'chk1', target: 'snd1', action: 'x=0', curve: 0.2, actionY: 10 },
      { source: 'wait1', target: 'snd1', action: 'timeout?', curve: 0.2, actionY: 5, actionX: -40 }
    ]"
  />
</div>

<!-- Receiver R -->
<div class="absolute top-20 right-0 scale-[0.6] origin-top-right">
  <h4 class="font-bold mb-4 text-center">מקבל (Receiver R)</h4>
  <TransitionSystemD3 :width="550" :height="150"
    :states="[
      { id: 'w0', text: 'wait(0)', initial: true, initialDirection: 'top', x: 70, y: 50, width: 90, rx: 20 },
      { id: 'pr0', text: 'pr_msg(0)', x: 270, y: 50, width: 120, rx: 20 },
      { id: 'sa0', text: 'snd_ack(0)', x: 470, y: 50, width: 120, rx: 20 },
      { id: 'sa1', text: 'snd_ack(1)', x: 70, y: 220, width: 120, rx: 20 },
      { id: 'pr1', text: 'pr_msg(1)', x: 270, y: 220, width: 120, rx: 20 },
      { id: 'w1', text: 'wait(1)', x: 470, y: 220, width: 90, rx: 20 }
    ]"
    :transitions="[
      { source: 'w0', target: 'pr0', action: 'c?⟨m,y⟩' },
      { source: 'pr0', target: 'sa0', action: 'y=0', actionY: -20 },
      { source: 'pr0', target: 'w0', action: 'y=1', curve: 0.3, actionY: -10 },
      { source: 'sa0', target: 'w1', action: 'd!0' },
      { source: 'w1', target: 'pr1', action: 'c?⟨m,y⟩' },
      { source: 'pr1', target: 'sa1', action: 'y=1', actionY: 5 },
      { source: 'pr1', target: 'w1', action: 'y=0', curve: 0.3, actionY: 10 },
      { source: 'sa1', target: 'w0', action: 'd!1' }
    ]"
  />
</div>

<!-- Timer -->
<div class="absolute bottom-10 left-0 scale-[0.6] origin-bottom-right">
  <h4 class="font-bold -mb-4 text-center">טיימר (Timer)</h4>
  <TransitionSystemD3 :width="200" :height="150"
    :states="[
      { id: 'off', text: 'off', initial: true, initialDirection: 'top', x: 100, y: 50, rx: 20 },
      { id: 'on', text: 'on', x: 100, y: 140, rx: 20 }
    ]"
    :transitions="[
      { source: 'off', target: 'on', action: 'tmr_on?', curve: 1, actionX: -20 },
      { source: 'on', target: 'off', action: 'tmr_off?'  },
      { source: 'on', target: 'off', action: 'timeout!', curve: 1, actionX: 20 }
    ]"
  />
</div>

<!-- Formal Definition -->
<div class="absolute -bottom-15 left-0 w-full text-center">

$$ABP = [S \mid Timer \mid R]$$
$$Chan = \{c, d, tmr\_on, tmr\_off, timeout\}, Var = \{x, y, m_i\}$$

</div>

</div>
