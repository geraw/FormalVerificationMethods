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
  ## מבוא לאימות תוכנה בשיטות פורמאליות
  מרצה: גרא וייס
---
 
# מבוא לאימות תוכנה <br>  בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/graphics/just-logo.png" class="bgu-logo" style="position: absolute; top: 40px; right: 40px; width: 80px; z-index: 100;" />


---

# מידע כללי ℹ️

* **מרצה:** גרא וייס

* **משרד:** חדר 123 בבניין 37
* **שעות קבלה:** ימי רביעי, 14:00-16:00 
* **דוא"ל:** geraw@bgu.ac.il
* **אתר הקורס:** [מודל](https://moodle.bgu.ac.il/moodle/course/view.php?id=58529)

---

# מרכיבי הציון 🎓

<div dir="rtl" class="text-right">

| רכיב | משקל | הערות |
| --- | --- | --- |
| עבודות תכנותיות | 10% |  |
| עבודות עיוניות | 10% |  |
| **בוחן אמצע** | 20% | מתוכנן להתקיים ב-1/5/26 |
| **מבחן סופי** | 60% |  |
| עבודות בונוס | +2% | לכל עבודה |

</div>

> **תנאי מעבר:** מעבר בוחן ומבחן, והגשת 80% מתרגילי הבית.
> **השקעה נדרשת:** 5-10 שעות עבודה עצמית בשבוע.

---

# לוגיקה בפעולה 🧠


* **שורשים פילוסופיים:** הבנת תהליכי הסקת מסקנות אנושיים ותיאורם המדויק.
* **בעידן המחשב:**
    * בסיס למעגלים לוגיים.
    * פיתוח מנגנונים לניתוח לוגיקת תוכנה.
    * גילוי שגיאות לוגיות בתכנון ובמימוש.

<div class="absolute top-40 left-40">
  <img src="./images/logic_evolution_cartoon_2.png" class="h-90" />
</div>

---

# מהן שיטות פורמליות? 🛠️

טכניקות **מתמטיות ואלגוריתמיות** לאפיון, פיתוח ואימות תוכנה וחומרה אמינה.

<div class="grid grid-cols-2 gap-8 items-start mt-8 ml-10">
  <div>
    <ul class="space-y-4">
      <li><strong>מוטיבציה:</strong> אנליזה מתמטית מסודרת תורמת ליציבות התכנון (כמו בכל הנדסה).</li>
      <li><strong>שימוש כיום:</strong> בעיקר במערכות קריטיות (בטיחות ואמינות גבוהה) בשל עלות ומורכבות.</li>
    </ul>
  </div>
  <div class="flex justify-center">
    <img src="./images/engineering_comparison.png" class="h-70 rounded-lg shadow-xl border border-blue-100" />
  </div>
</div>

---

# בדיקות (Testing) vs. אימות פורמאלי (Verification) 🔍

<div class="grid grid-cols-2 gap-8 items-center mt-20 ml-10">
  <div class="flex flex-col gap-6">
    <div class="p-4 bg-blue-50 border-r-4 border-blue-500 rounded">     
      <strong>בדיקה רגילה:</strong> נבדק מסלול פעולה יחיד עבור קלט נתון.
    </div>
    <div class="p-4 bg-green-50 border-r-4 border-green-500 rounded">
      <strong>אימות פורמאלי:</strong> סריקת <strong>כל</strong> מצבי המערכת עד גילוי שגיאה או הוכחת נכונות.
    </div>
  </div>
  <div class="flex justify-center">
    <img src="./images/testing_vs_verification.png" class="h-70 rounded-lg shadow-xl border border-gray-100" />
  </div>
</div>

---

# : שזירת תהליכים (Threads Interleaving) 🧵

<div class="grid grid-cols-2 gap-10 items-center mt-5">
  <div>

במערכות מקביליות, מספר הריצות האפשריות ($M$) גדל אקספוננציאלית:

<div class="my-6">

$$M = \frac{(\sum_{i=1}^{N} n_i)!}{\prod_{i=1}^{N} (n_i!)}$$
</div>

<ul class="space-y-4">
  <li>כל מלבן באיור מייצג <strong>פעולה אטומית</strong> של thread.</li>
  <li>אימות פורמאלי נועד לצוד באגים במרחב המצבים העצום שנוצר מהשזירות.</li>
</ul>
  </div>
  <div class="flex justify-center">
    <img src="./images/threads_interleaving.png" class="h-85 crop=" />
  </div>
</div>

---

# "צייד באגים" - חשיבות הגילוי המוקדם 🐛

<div class="grid grid-cols-2 gap-10 items-center mt-10 ml-10">
  <div>
    ככל ששגיאה מתגלה מאוחר יותר בציר הזמן, עלות התיקון שלה מזנקת:
    
<ul class="mt-6 space-y-4">
  
  <li><strong>אפיון ותכנון:</strong> עלות נמוכה, קל לתקן.</li>
  <li><strong>בדיקות ותפעול:</strong> עלות שמגיעה לאלפי דולרים ($12.5K+) לשגיאה.</li>
</ul>
    
<blockquote>
  <strong>מסקנה:</strong> אימות פורמלי בשלב התכנון חוסך הון!
</blockquote>
</div>
<div class="flex justify-center">
<img src="./images/bug_cost_graph_he.png" class="h-80 rounded-lg shadow-xl" />
</div>
</div>

---

# מושגי יסוד שנלמד בקורס  📚

<div class="grid grid-cols-2 gap-x-10 gap-y-6 text-sm">
  <div>
    <strong>1. מערכות מעברים (Transition Systems)</strong>
    <ul class="opacity-80">
      <li>מידול התנהגות תוכנה וחומרה באמצעות מצבים ומעברים.</li>
      <li>טיפול באי-דטרמיניזם וריצה מקבילית.</li>
      <li>גרפי תוכנית (Program Graphs) ומשתנים משותפים.</li>
    </ul>
  </div>
  <div>
    <strong>5. תכונות בטיחות וחיות (Safety & Liveness)</strong>
    <ul class="opacity-80">
      <li><strong>Safety:</strong> "משהו רע לעולם לא יקרה" (למשל: אין Deadlock).</li>
      <li><strong>Liveness:</strong> "משהו טוב יקרה בסופו של דבר" (למשל: שירות יינתן).</li>
    </ul>
  </div>
  <div>
    <strong>2. שפת Promela וכלי הבדיקה SPIN</strong>
    <ul class="opacity-80">
      <li>שפה ייעודית למידול מערכות מבוזרות ומקביליות.</li>
      <li>ניהול ערוצי תקשורת (Channels) וסנכרון.</li>
      <li>אימות אוטומטי של מודלים מורכבים.</li>
    </ul>
  </div>
  <div>
    <strong>6. פיצוץ מצבים והפשטה (State Explosion)</strong>
    <ul class="opacity-80">
      <li>התמודדות עם הצמיחה האקספוננציאלית של מרחב המצבים.</li>
      <li>טכניקות צמצום (Partial Order Reduction).</li>
    </ul>
  </div>
  <div>
    <strong>3. לוגיקת זמן (LTL - Temporal Logic)</strong>
    <ul class="opacity-80">
      <li>שפה פורמלית לתיאור דרישות לאורך זמן (Always, Eventually).</li>
      <li>קשר בין לוגיקה לאוטומטים של בוכי (Büchi Automata).</li>
    </ul>
  </div>
  <div>
    <strong>7. הגינות (Fairness)</strong>
    <ul class="opacity-80">
      <li>הנחות על תזמון תהליכים (Weak/Strong Fairness).</li>
      <li>חיוני להוכחת תכונות חיות (Liveness).</li>
    </ul>
  </div>
  <div>
    <strong>4. בדיקות מודל (Model Checking)</strong>
    <ul class="opacity-80">
      <li>אלגוריתמים לסריקה שיטתית של גרף המצבים.</li>
      <li>יצירת דוגמה נגדית (Counter-example) במקרה של שגיאה.</li>
    </ul>
  </div>
</div>


---

# אימות (Verification) ≠ תִּקּוּף (Validation) ✅

<div class="grid grid-cols-2 gap-10 items-center mt-12 ml-10">
  <div class="flex flex-col gap-6">
    <div class="p-6 bg-blue-50 border-r-8 border-blue-600 rounded-lg shadow-sm">
      <div class="text-xl font-bold mb-2">אימות (Verification)</div>
      "האם אנחנו בונים את הדבר <strong>נכון</strong>?"
      <div class="text-sm opacity-70 mt-2">בדיקה מול המפרט והדרישות הטכניות.</div>
    </div>
    
  <div class="p-6 bg-green-50 border-r-8 border-green-600 rounded-lg shadow-sm">
    <div class="text-xl font-bold mb-2">תִּקּוּף (Validation)</div>
    "האם אנחנו בונים את הדבר <strong>הנכון</strong>?"
    <div class="text-sm opacity-70 mt-2">בדיקה האם המוצר עונה על הצורך האמיתי של המשתמש.</div>
  </div>
  </div>
  
  <div class="flex justify-center">
    <img src="./images/verification_vs_validation.png" class="h-85 rounded-xl shadow-2xl border border-gray-100" />
  </div>
</div>

---

# שיטות לאימות פורמאלי 🧩

<div class="relative h-80 mt-10">
  <!-- שיטות דדוקטיביות - למעלה משמאל -->
  <div class="absolute top-0 right-0 w-65 p-4 bg-blue-50 rounded-lg border border-blue-200 shadow-sm">
    <div class="font-bold text-sm mb-1 text-blue-800 underline">שיטות דדוקטיביות (Deductive)</div>
    <div class="text-[14px] leading-relaxed">
      <strong>מהות:</strong> הוכחה מתמטית ידנית או חצי-ממוכנת באמצעות לוגיקה.
      <ul class="mt-2 space-y-1">
        <li>✅ <strong>יתרון:</strong> טיפול במערכות אינסופיות.</li>
        <li>❌ <strong>חיסרון:</strong> דורש מומחיות וזמן רב.</li>
        <li>🛠️ <strong>דוגמה:</strong> Coq, Isabelle, Lean.</li>
      </ul>
    </div>
  </div>

  <!-- בדיקות מודל - במרכז -->
  <div class="absolute top-20 left-65 w-75 p-5 bg-green-50 rounded-lg border-2 border-green-400 shadow-md z-10 scale-110">
    <div class="font-bold text-base mb-1 text-green-800 underline">בדיקות מודל (Model Checking)</div>
    <div class="text-[12px] leading-relaxed font-semibold">
      <strong>מהות:</strong> סריקה אוטומטית ומלאה של מרחב המצבים.
      <ul class="mt-2 space-y-1">
        <li>✅ <strong>יתרון:</strong> אוטומטי, מספק דוגמה נגדית.</li>
        <li>❌ <strong>חיסרון:</strong> בעיית "פיצוץ המצבים".</li>
        <li>🛠️ <strong>דוגמה:</strong> SPIN, NuSMV, TLC+.</li>
      </ul>
    </div>
  </div>

  <!-- סימולציה - למטה מימין -->
  <div class="absolute top-45 -left-10 w-65 p-4 bg-orange-50 rounded-lg border border-orange-200 shadow-sm">
    <div class="font-bold text-sm mb-1 text-orange-800 underline">סימולציה (Simulation)</div>
    <div class="text-[12px] leading-relaxed">
      <strong>מהות:</strong> הרצת המערכת על תרחישים נבחרים (בדיקות דינמיות).
      <ul class="mt-2 space-y-1">
        <li>✅ <strong>יתרון:</strong> מהיר, זול, על המערכת האמיתית.</li>
        <li>❌ <strong>חיסרון:</strong> לא מבטיח הוכחה מלאה.</li>
        <li>🛠️ <strong>דוגמה:</strong> JUnit, Pytest, Simulink.</li>
      </ul>
    </div>
  </div>
</div>

---

# למה דווקא בדיקות מודל (Model Checking)? 🎯

<div class="grid grid-cols-2 gap-10 items-center">
  <div class="flex justify-center">
    <img src="./images/formal_methods_landscape.png" class="h-85 rounded-xl shadow-2xl" />
  </div>
  
  <div class="space-y-6">
    <div class="p-4 bg-green-50 border-r-4 border-green-600 rounded">
      <strong>השילוב המנצח (Sweet Spot):</strong>
      בדיקות מודל משלבות את הדיוק המתמטי של שיטות הוכחה עם האוטומציה של בדיקות תוכנה.
    </div>
    
  <ul class="space-y-3">
    <li>✅ <strong>ללא הוכחות ידניות:</strong> הכלי עושה את העבודה הקשה.</li>
    <li>✅ <strong>כיסוי מלא:</strong> בניגוד לבדיקות, כאן בודקים את <em>כל</em> המצבים.</li>
    <li>✅ <strong>משוב ישיר:</strong> קבלת מסלול מדויק (Counter-example) המראה איך הגענו לבאג.</li>
  </ul>
  
  <div class="italic text-sm opacity-70">
    זהו הכלי המעשי ביותר כיום לאימות של מערכות מורכבות ומקביליות.
  </div>
  </div>
</div>

---

# התפתחות שיטות אימות 📜

* **1940:** הוכחה מתמטית ידנית (אלן טיורינג).
* **1969:** לוגיקת הואר (Hoare) לתוכנות סדרתיות.
* **1977:** אמיר פנואלי מכניס את לוגיקת הזמן (פרס טיורינג 1996).
* **2008:** פרס טיורינג לקלארק, אמרסון וסיפאקיס על פיתוח Model Checking.

<div class="mt-8 flex justify-center">
  <img src="./images/verification_history_timeline.png" class="h-80 rounded-lg shadow-xl bg-white p-2" />
</div>

