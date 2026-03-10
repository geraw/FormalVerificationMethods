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
    /* Lamp 1 moves */
    { source: 'oo', target: 'do', action: '$n_1$' }, { source: 'do', target: 'bo', action: '$n_1$' }, { source: 'bo', target: 'oo', action: '$r_1$', curve: -0.2, actionY:-5 },
    { source: 'od', target: 'dd', action: '$n_1$' }, { source: 'dd', target: 'bd', action: '$n_1$' }, { source: 'bd', target: 'od', action: '$r_1$', curve: 0.2, actionX:30, actionY:4 },
    { source: 'ob', target: 'db', action: '$n_1$' }, { source: 'db', target: 'bb', action: '$n_1$' }, { source: 'bb', target: 'ob', action: '$r_1$', curve: 0.2 },
    /* Lamp 2 moves */
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
