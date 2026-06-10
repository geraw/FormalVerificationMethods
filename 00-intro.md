---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: true
download: true
exportFilename: 00-intro
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

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; top: 40px; right: 40px; width: 80px; z-index: 100;" />


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
| עבודות תכנותיות | 10% | שתי עבודות הכוללות לימוד עצמי באמצעות LLM .אפשר בזוגות. |
| עבודות עיוניות | 10% | ארבע עבודות הכוללות תרגילי רשות וחובה ברמה של הבוחן והמבחן. הגשה אישית. |
| **בוחן אמצע** | 20% | מתוכנן להתקיים ב-1/5/26 |
| **מבחן סופי** | 60% | מתוכנן להתקיים ב-8/7/26 (מועד א') וב-5/8/26 (מועד ב')|

</div>

> **תנאי מעבר:** מעבר בוחן ומבחן, והגשת כל תרגילי הבית.
> **השקעה נדרשת:** 5-10 שעות עבודה עצמית בשבוע.

פירוט מתווה המילואים מופיע בשקף הבא.

---

# למשרתי ומשרתות המילואים

<div dir="rtl" class="text-right text-[12px] leading-[1.28] mt-1">
  <p class="mb-2">
    מעבר למתווה הכללי של האוניברסיטה, ננסה לסייע לכם בקורס בהיבטים הבאים:
  </p>

  <div class="grid grid-cols-3 gap-2 mb-2">
    <div class="p-2 bg-sky-50 border border-sky-200 border-r-4 border-r-sky-500 rounded">
      <div class="font-bold mb-1">השלמת חומר והרצאות</div>
      <div>
        אם החומר באתר (סיכומי הרצאות, מצגות, הרצאות מוקלטות) ושעות הקבלה הרגילות אינם מספיקים,
        אפשר לקבוע איתי (<a href="mailto:geraw@bgu.ac.il">geraw@bgu.ac.il</a>) פגישה אישית להשלמת הפערים.
      </div>
    </div>
    <div class="p-2 bg-emerald-50 border border-emerald-200 border-r-4 border-r-emerald-500 rounded">
      <div class="font-bold mb-1">תרגולים ועבודות תכנותיות</div>
      <div>
        אם החומר באתר ושעות הקבלה הרגילות של המתרגלים אינם מספיקים, אפשר לפנות למתרגלים להשלמת פערים.
        שתי העבודות התכנותיות מוגשות בזוגות, בהתאם לשקף מרכיבי הציון.
      </div>
    </div>
    <div class="p-2 bg-amber-50 border border-amber-200 border-r-4 border-r-amber-500 rounded">
      <div class="font-bold mb-1">הארכות</div>
      <div>
        לכל משרת מילואים על פי סיווג האוניברסיטה ניתנת הארכה ללא הגבלה לכל העבודות.
        היא חלה גם על השותף בזוג.
        בקשות להארכות יש לשלוח לטל בראמי (<a href="mailto:baramit@post.bgu.ac.il">baramit@post.bgu.ac.il</a>), המתרגל האחראי בקורס.
      </div>
    </div>
  </div>

  <div class="p-2 bg-slate-50 border border-slate-200 border-r-4 border-r-slate-500 rounded mb-3">
    <div class="font-bold mb-1">פטורים וחישוב ציון מיטבי</div>
    <div class="grid grid-cols-2 gap-3">
      <div class="p-1 bg-white/70 border border-slate-200 rounded"> 
        <div class="font-bold mb-1">עבודות תכנותיות: 2 עבודות בזוגות</div>
        <div class="mb-1">לקבוצות 2-3 פטור על עבודה תכנותית אחת; גם השותף בזוג נהנה מאותו מתווה.</div>
        <div class="mb-1">אם העבודה לא תוגש: משקל העבודה התכנותית האחרת יהיה 7.5% עבור קבוצה 2 ו-10% עבור קבוצה 3.</div>
        <div class="mb-1">אם העבודה תוגש למרות הפטור: בחישוב הציון תילקח בחשבון העבודה הגבוהה מבין השתיים, במשקל 10%.</div>
        <div class="mb-1">עבור משרת/ת מילואים בלבד מקבוצה 3, משקל שתי העבודות התכנותיות יכול להגיע ל-15% מהציון הסופי.</div>
      </div>
      <div class="p-2 bg-white/70 border border-slate-200 rounded">
        <div class="font-bold mb-1">עבודות עיוניות: 4 עבודות אישיות</div>
        <div class="mb-1">לקבוצות 2-3 ניתן לקבל פטור על עבודה עיונית אחת.</div>
        <div class="mb-1">אם העבודה לא תוגש: משקל שלוש העבודות העיוניות האחרות יהיה 7.5% עבור קבוצה 2 ו-10% עבור קבוצה 3.</div>
        <div class="mb-1">אם העבודה תוגש למרות הפטור: בחישוב הציון יילקחו בחשבון שלוש העבודות הגבוהות מבין הארבע, במשקל 10%.</div>
        <div class="mb-1">עבור משרת/ת מילואים בלבד מקבוצה 3, משקל ארבע העבודות העיוניות יכול להגיע ל-15% מהציון הסופי.</div>
      </div>
    </div>
  </div>
<div class="mb-1">ככלל, ההמלצה היא לנסות להגיש את כל העבודות, כי זה חיוני להבנת החומר ולהצלחה במבחן.</div>
<div class="mb-1">הגשת העבודה למרות הפטור לא תפגע בציון: ייבחר הציון האופטימלי מבין כל האפשרויות.</div>
<div>מי שמסווג/ת לקטגוריית 300+ ישודרג/תשודרג ברמה אחת לצורך מתווה זה; למשל, קבוצה 2 תיחשב כקבוצה 3.</div>
</div>

<img src="./images/lecturer_saluting_soldier.png" class="absolute top-1 left-5 h-35 rounded-lg shadow-xl" />


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

# לוגיקה בפעולה 🧠


* **שורשים פילוסופיים:** הבנת תהליכי הסקת מסקנות אנושיים ותיאורם המדויק.
* **בעידן המחשב:**
    * בסיס למעגלים לוגיים.
    * פיתוח מנגנונים לניתוח לוגיקת תוכנה.
    * גילוי שגיאות לוגיות בתכנון ובמימוש.

<div class="absolute top-40 left-40">
  <img src="./images/logic_evolution_cartoon_2.png" class="h90" />
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

# שזירת תהליכים (Threads Interleaving) 🧵

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

<div class="absolute  bottom-20 left-60 h-50 overflow-hidden shadow-xl rounded-lg bg-white border border-gray-100">
  <img src="./images/verification_history_timeline.png" class="w-120 max-w-none -mt-30 opacity-95" />
</div>

<div class="mt-4 space-y-2">
  <li><strong>1940:</strong> הוכחה מתמטית ידנית (אלן טיורינג).</li>
  <li><strong>1969:</strong> לוגיקת הואר (Hoare) לתוכנות סדרתיות.</li>
  <li><strong>1977:</strong> אמיר פנואלי מכניס את לוגיקת הזמן (פרס טיורינג 1996).</li>
  <li><strong>2008:</strong> פרס טיורינג לקלארק, אמרסון וסיפאקיס על פיתוח Model Checking.</li>
</div>


---

# מערכות סדרתיות vs. מערכות ריאקטיביות 🔄

<div class="grid grid-cols-2 gap-10 mt-10">
  <div class="flex flex-col items-center">
    <div class="font-bold mb-4 text-red-700">מערכת סדרתית (Sequential)</div>
    <img src="./images/sequential_system.png" class="h-50 mb-6" />
    <ul class="text-right space-y-2 text-sm">
      <li>📥 <strong>קלט:</strong> ניתן במלואו בתחילת הריצה.</li>
      <li>⚙️ <strong>עיבוד:</strong> תהליך טרנספורמטיבי (Input to Output).</li>
      <li>📤 <strong>פלט:</strong> מתקבל בסיום הריצה.</li>
      <li>🛑 <strong>סיום:</strong> מצפים מהמערכת לעצור.</li>
    </ul>
  </div>

  <div class="flex flex-col items-center border-r-2 border-gray-100 pr-10">
    <div class="font-bold mb-4 text-green-700">מערכת ריאקטיבית (Reactive)</div>
    <img src="./images/reactive_cactus.png" class="h-50 mb-6" />
    <ul class="text-right space-y-2 text-sm">
      <li>🌵 <strong>מטפורת הקקטוס:</strong> אינטראקציה מתמשכת.</li>
      <li>⚡ <strong>אירועים:</strong> זורמים למערכת באופן שוטף.</li>
      <li>🎯 <strong>תגובות:</strong> המערכת מגיבה לאירועים בזמן אמת.</li>
      <li>🔄 <strong>ריצה:</strong> לרוב אינה אמורה להסתיים (למשל: בקר טיסה).</li>
    </ul>
  </div>
</div>

