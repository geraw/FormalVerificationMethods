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

# תוכנית הקורס 📚

1. **מערכות מעברים (Transition Systems):** תיאור תוכנה כגרף תוכנית.
2. **שפת Promela:** תיאור מערכות מבוזרות.
3. **לוגיקת זמן (Temporal Logic):** אפיון תכונות דינמיות.
4. **בדיקות מודל (Model Checking):** אלגוריתמים לאימות אוטומטי.

---

# דוגמאות לאסונות שניתן היה למנוע ⚠️

* **Therac-25:** קרינת יתר קטלנית עקב Race Condition בתוכנה.
* **AT&T Network:** נפילת רשת ל-9 שעות עקב פירוש שגוי של פקודת `break` ב-C.
* **Ariane 5:** התרסקות טיל שעלתה 500 מיליון אירו עקב טעות בהמרת משתנה (Overflow).
* **Intel Pentium:** שגיאת FDIV בחילוק נקודה צפה שעלתה 500 מיליון דולר.

---

# אימות (Verification) ≠ תִּקּוּף (Validation) ✅

* **אימות:** "האם אנחנו בונים את הדבר **נכון**?" (עמידה בדרישות).
* **תִּקּוּף:** "האם אנחנו בונים את הדבר **הנכון**?" (האם זה מה שהלקוח צריך).

---

# שיטות לאימות פורמאלי 🧩

* **שיטות דדוקטיביות:** הוכחה מתמטית של נכונות (Theorem Provers).
* **בדיקות מודל (Model Checking):** בדיקה ממוכנת של כל ריצה אפשרית במכונת מצבים.
* **סימולציה:** בדיקת $P$ על ידי הפעלת התנהגויות (לא מבטיח הוכחה מלאה).

---

# אבני דרך בהיסטוריה 📜

* **1940:** הוכחה מתמטית ידנית (טיורינג).
* **1969:** לוגיקת הואר (Hoare) לתוכנות סדרתיות.
* **1977:** אמיר פנואלי מכניס את לוגיקת הזמן (פרס טיורינג 1996).
* **2008:** פרס טיורינג לקלארק, אמרסון וסיפאקיס על פיתוח Model Checking.

---

# כלי ה-SPIN ומרחב המצבים 🤖

* **SPIN:** כלי לניתוח מודלים מבוזרים ומקביליים.
* **פרויקט הקורס:** פיתוח כלי דומה ל-SPIN.
* **דוגמה:** בחינת תהליכי Inc, Dec ו-Reset על משתנה $x$ ובדיקת חריגות מהטווח $0 \le x \le 200$.