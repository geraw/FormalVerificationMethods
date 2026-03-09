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

