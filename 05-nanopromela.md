---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: true
download: true
exportFilename: 05-nanopromela
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## NanoPromela
  מרצה: גרא וייס
---

# NanoPromela
## הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מחסנית שפות המידול עד עכשיו

<ModelingLanguageStack>
  <template #intro>
    במהלך הקורס בנינו שכבות תיאור שהולכות ונעשות קרובות יותר לשפת מפרט,
    אבל בסוף כולן מתורגמות אל <b>מערכת מעברים</b> שעליה אנחנו יודעים להפעיל אימות פורמלי.
  </template>
  <template #ts>מערכת מעברים</template>
  <template #pg>גרף תוכנית</template>
  <template #ts-weave>שזירת מערכות מעברים</template>
  <template #circuit>שערים לוגיים</template>
  <template #channels>מערכת ערוצים</template>
  <template #sync>שזירה עם תקשורת סנכרונית</template>
  <template #async>שזירה בלי תקשורת</template>
  <template #nano>Nano <br> Promela</template>
  <template #before-note>
    עד כאן המחסנית שבנינו: שכבות מידול שונות, שכולן עדיין נגזרות בסוף למערכת מעברים.
  </template>
  <template #after-note>
    ההרצאה הנוכחית מוסיפה את שכבת <span dir="ltr">NanoPromela</span>, שממנה נגזור
    <span dir="ltr">Channel System</span>, אחר כך <span dir="ltr">Program Graph</span>,
    ולבסוף <span dir="ltr">Transition System</span>.
  </template>
</ModelingLanguageStack>

---

# NanoPromela

<div class="text-[15px] leading-snug">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 mt-2">
המודלים שראינו עד עכשיו, כמו <span dir="ltr">program graphs</span>, הרכבה מקבילית
ו־<span dir="ltr">channel systems</span>, מספקים בסיס מתמטי מדויק למידול מערכות תגובתיות.
אבל כדי לבנות כלים אוטומטיים לאימות, נוח יותר לעבוד עם
<b>שפת מפרט קטנה ופשוטה</b> שממנה אפשר לגזור את המודל הפורמלי.
</div>

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="bg-blue-50 p-3 rounded border border-blue-200">
<div class="font-bold mb-2">מה אנחנו רוצים משפת מפרט?</div>
<ul class="list-disc pr-5 space-y-4">
<li>שתהיה קלה להבנה, גם עבור משתמשים שאינם מומחים.</li>
<li>שתהיה מספיק אקספרסיבית כדי לתאר התנהגות צעד־אחר־צעד של תהליכים ואינטראקציות.</li>
<li>שתאפשר לתאר גם חישוב וגם תקשורת.</li>
</ul>
</div>

<div class="bg-orange-50 p-3 rounded border border-orange-200">
<div class="font-bold mb-2">למה חייבים סמנטיקה פורמלית?</div>
<ul class="list-disc pr-5 space-y-6">
<li>כדי שהמשמעות של כל פקודה תהיה חד־משמעית.</li>
<li>כדי לשייך לכל תוכנית מערכת מעברים פורמלית.</li>
<li>כדי לאפשר אימות פורמלי.</li>
</ul>
</div>
</div>

<div class="mt-4 bg-purple-50 p-3 rounded border border-purple-200 text-center">

$$
\text{Specification program}
\Longrightarrow
\text{Channel System}
\Longrightarrow
\text{Transition System}
$$

</div>

</div>

---

# משתנים, ביטויים וערוצים

<div class="text-[13px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
ב־NanoPromela המשתנים יכולים להיות מטיפוסים שונים
כמו <span dir="ltr">integer</span>, <span dir="ltr">Boolean</span>,
<span dir="ltr">char</span> או <span dir="ltr">real</span>,
ויכולים להיות גלובליים או מקומיים לתהליך מסוים.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">הפשטה של משתנים</div>

<ul class="list-disc pr-5 mt-1 space-y-4">
<li>אם צריך, אפשר לשנות־שם כדי למנוע התנגשויות.</li>
<li>לכן אפשר להתייחס לכל המשתנים כאילו הם גלובליים.</li>
<li>נסמן ב־<span dir="ltr"><code>Var</code></span> את קבוצת המשתנים של התוכנית.</li>
<li>לכל משתנה <span dir="ltr"><code>x</code></span> יש תחום ערכים
<span dir="ltr"><code>dom(x)</code></span>.</li>
</ul>
</div>

<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">ערוצים ותנאי התחלה</div>

<ul class="list-disc pr-5 mt-1 space-y-2">
<li>לכל ערוץ <span dir="ltr"><code>c</code></span> יש טיפוס
<span dir="ltr"><code>dom(c)</code></span>.</li>
<li>לכל ערוץ יש גם קיבולת
<span dir="ltr"><code>cap(c)</code></span>.</li>
<li>הכרזת הערוץ קובעת  את תכונותיו.</li>
<li>חלק ההכרזות כולל גם פסוק בוליאני שמגדיר את הערכים ההתחלתיים החוקיים.</li>
</ul>
</div>
</div>

<div class="mt-2 bg-amber-50 px-4 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">מה חשוב פורמלית?</div>

הפרטים המלאים של ההכרזות פחות חשובים כאן.
לצורך הסמנטיקה מספיק לדעת מהי קבוצת המשתנים
<span dir="ltr"><code>Var</code></span>,
מהם התחומים <span dir="ltr"><code>dom(x)</code></span> ו־<span dir="ltr"><code>dom(c)</code></span>,
מהי הקיבולת <span dir="ltr"><code>cap(c)</code></span>,
ואילו השמות התחלתיות חוקיות.
</div>

</div>

---

# NanoPromela ו־Promela

<div class="text-[14px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
<b>NanoPromela</b> היא גרסה מוקטנת ופשוטה של <b>Promela</b>, שפת הקלט של <b>SPIN</b>.
המטרה היא שפת מפרט קטנה ונוחה, עם סמנטיקה פורמלית שנשענת על
<span dir="ltr">program graphs</span>, <span dir="ltr">channel systems</span>
ו־<span dir="ltr">transition systems</span>.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">מבנה התוכנית</div>

$$
P = [P_1 \mid \ldots \mid P_n]
$$

כל תוכנית מורכבת ממספר סופי של תהליכים שרצים במקביל.

<ul class="list-disc pr-5 mt-1 space-y-0.5">
<li>תקשורת דרך משתנים משותפים</li>
<li>או דרך ערוצי FIFO סינכרוניים /עם תור הודעות </li>
</ul>
</div>

<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">תיאור ההתנהגות</div>

Promela משתמשת ב־<span dir="ltr">guarded commands</span>:
תנאי שמאפשר צעד, יחד עם פקודה שמבצעת אותו.

<ul class="list-disc pr-5 mt-1 space-y-0.5">
<li>השמות למשתנים</li>
<li>תנאים, לולאות והרכבה סדרתית</li>
<li>שליחה וקבלה מערוצים</li>
<li>אזורים אטומיים למניעת interleavings לא רצויים</li>
</ul>
</div>
</div>

<div class="mt-2 bg-amber-50 px-4 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">רעיון סמנטי מרכזי</div>

ב־Promela לרוב אין <span dir="ltr">action names</span> נפרדים:
הפקודה עצמה מגדירה את אפקט הצעד.

$$
\text{Promela program}
\Longrightarrow
\text{Channel System}
\Longrightarrow
\text{Transition System}
$$

</div>

</div>

---

# הפקודות של NanoPromela

<div class="text-[14px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
ההתנהגות הצעד־אחר־צעד של כל תהליך מתוארת בעזרת פקודות פשוטות,
שמהן נבנים צעדים במערכת המעברים.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">פקודות אטומיות</div>

<ul class="list-disc pr-5 mt-1 space-y-3">
<li><span dir="ltr"><code>skip</code></span></li>
<li>השמה: <span dir="ltr"><code>x := expr</code></span></li>
<li>קבלה מערוץ: <span dir="ltr"><code>c?x</code></span></li>
<li>שליחה לערוץ: <span dir="ltr"><code>c!expr</code></span></li>
</ul>

<div class="mt-2">
פקודות אלו הן אבני הבניין הבסיסיות של צעד בודד.
</div>
</div>

<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">פקודות בקרה</div>

<ul class="list-disc pr-5 mt-1 space-y-3">
<li>פקודות תנאי</li>
<li>פקודות חזרה</li>
<li>הרכבה סדרתית של פקודות</li>
</ul>

<div class="mt-2">
ברמה האינטואיטיבית הן ממלאות את התפקיד של
<span dir="ltr"><code>if-then-else</code></span>
ו־<span dir="ltr"><code>while</code></span>.
</div>
</div>
</div>

<div class="mt-2 bg-amber-50 px-4 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">ההבדל החשוב ב־NanoPromela</div>

במקום מבני <span dir="ltr"><code>if</code></span> ו־<span dir="ltr"><code>while</code></span> סטנדרטיים,
השפה תומכת ב־<b>בחירה לא־דטרמיניסטית</b> ומאפשרת לכתוב
<b>מספר סופי של guarded commands</b> בתוך פקודות תנאי ופקודות חזרה.
</div>

</div>

---


# תחביר פורמלי של פקודות

<div class="text-[13px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
איור התחביר של <span dir="ltr">NanoPromela</span> מגדיר כיצד בונים פקודות מתוך השמה, תקשורת,
הרכבה סדרתית, אזור אטומי ומבני <span dir="ltr">guarded commands</span>.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-zinc-900 text-zinc-100 px-4 py-3 rounded">

<div dir="ltr" class="text-left">

```text {lineNumbers: false}
stmt ::= skip
      | x := expr
      | c?x
      | c!expr
      | stmt₁ ; stmt₂
      | atomic{assignments}
      | if :: g₁ -> stmt₁ ... :: gₙ -> stmtₙ fi
      | do :: g₁ -> stmt₁ ... :: gₙ -> stmtₙ od
```

</div>

</div>

<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">עקביות טיפוסים</div>

<ul class="list-disc pr-5 mt-1 space-y-2">
<li>בהשמה <span dir="ltr"><code>x := expr</code></span> נדרש של־<span dir="ltr"><code>x</code></span> ול־<span dir="ltr"><code>expr</code></span> יהיו טיפוסים תואמים.</li>
<li>בקליטה <span dir="ltr"><code>c?x</code></span> נדרש <span dir="ltr"><code>dom(c) ⊆ dom(x)</code></span>.</li>
<li>בשליחה <span dir="ltr"><code>c!expr</code></span> נדרש שהטיפוס של <span dir="ltr"><code>expr</code></span> יתאים ל־<span dir="ltr"><code>dom(c)</code></span>.</li>
</ul>
</div>
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">Guards</div>

הביטויים <span dir="ltr"><code>g<sub>1</sub>, ..., g<sub>n</sub></code></span> שמופיעים ב־<span dir="ltr"><code>if-fi</code></span>
וב־<span dir="ltr"><code>do-od</code></span> הם <b>guards</b>.
אנו מניחים ש־<span dir="ltr"><code>g<sub>i</sub> ∈ Cond(Var)</code></span>, כלומר כל guard הוא תנאי בוליאני על ערכי המשתנים.
</div>

<div class="bg-amber-50 px-3 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">גוף של אזור אטומי</div>

הביטוי <span dir="ltr"><code>assignments</code></span> בתוך
<span dir="ltr"><code>atomic{...}</code></span> הוא הרכבה סדרתית לא־ריקה של השמות:

<div dir="ltr" class="text-center text-[12px] mt-3 mb-3 font-mono">
x<sub>1</sub> := expr<sub>1</sub>; x<sub>2</sub> := expr<sub>2</sub>; ...; x<sub>m</sub> := expr<sub>m</sub> &nbsp;&nbsp; (m ≥ 1)
</div>

כאשר לכל <span dir="ltr"><code>i</code></span> הטיפוסים של <span dir="ltr"><code>x<sub>i</sub></code></span> ושל <span dir="ltr"><code>expr<sub>i</sub></code></span> תואמים.
</div>
</div>

</div>

---


# משמעות אינטואיטיבית של הפקודות

<div class="text-[14px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
לפני הסמנטיקה הפורמלית, כדאי להבין אינטואיטיבית מה כל פקודה "עושה" בזמן ריצה.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">פקודות בסיסיות</div>

<ul class="list-disc pr-5 mt-1 space-y-3">
<li><span dir="ltr"><code>skip</code></span> מייצגת תהליך שמסתיים בצעד אחד, בלי לשנות משתנים ובלי לשנות את תוכן הערוצים.</li>
<li>המשמעות של <span dir="ltr"><code>x := expr</code></span> אינטואיטיבית: מחשבים את <span dir="ltr"><code>expr</code></span> לפי ההערכה הנוכחית, ומשייכים את התוצאה ל־<span dir="ltr"><code>x</code></span>.</li>
</ul>
</div>

<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">הרכבה סדרתית</div>

<div>
הפקודה <span dir="ltr"><code>stmt<sub>1</sub> ; stmt<sub>2</sub></code></span> מתארת
<b>ביצוע בזה אחר זה</b>:
</div>

<div class="mt-2">
קודם מבוצעת <span dir="ltr"><code>stmt<sub>1</sub></code></span>, ורק לאחר סיומה
מתחילה <span dir="ltr"><code>stmt<sub>2</sub></code></span>.
</div>

</div>
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-amber-50 px-3 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">אזור אטומי</div>

הפקודה <span dir="ltr"><code>atomic{stmt}</code></span> גורמת לכך שהביצוע של
<span dir="ltr"><code>stmt</code></span> ייתפס כצעד אטומי אחד, כלומר
<b>לא ניתן לשזור</b> לתוכו צעדים של תהליכים אחרים.
</div>

<div class="bg-rose-50 px-3 py-2 rounded border border-rose-200">
<div class="font-bold mb-1">למה זה חשוב?</div>

<ul class="list-disc pr-5 mt-1 space-y-2">
<li>אזור אטומי יכול לשמש גם כטכניקת <b>דחיסה</b> של מרחב המצבים.</li>
<li>מתעלמים מהקונפיגורציות הביניים שבתוך האזור האטומי, ומתייחסים לביצוע כולו כיחידה אחת.</li>
<li>בקורס נניח שגוף אזור אטומי הוא סדרה של השמות, כדי לפשט את כללי ההסקה בהמשך.</li>
</ul>
</div>
</div>

</div>


---


# פקודות תנאי: משמעות אינטואיטיבית

<div class="text-[14px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
הפקודות <span dir="ltr"><code>if-fi</code></span> ו־<span dir="ltr"><code>do-od</code></span>
הן הכללה של מבני <span dir="ltr">if-then-else</span> ו־<span dir="ltr">while</span> הרגילים,
אבל עם <b>בחירה לא־דטרמיניסטית</b> בין guarded commands.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">מה עושה <span dir="ltr"><code>if-fi</code></span>?</div>

<div dir="ltr" class="text-left text-[12px] font-mono mt-1 mb-2">
if :: g<sub>1</sub> -> stmt<sub>1</sub> ... :: g<sub>n</sub> -> stmt<sub>n</sub> fi
</div>

הפקודה מייצגת <b>בחירה לא־דטרמיניסטית</b> בין כל הפקודות
<span dir="ltr"><code>stmt<sub>i</sub></code></span> שעבורן ה־guard
<span dir="ltr"><code>g<sub>i</sub></code></span> מתקיים בהערכת המשתנים הנוכחית.
</div>

<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">הנחת Test-and-Set</div>

אנו מניחים סמנטיקה אטומית שבה שלושת השלבים הבאים קורים כיחידה אחת:

<ul class="list-disc pr-5 mt-1 space-y-1">
<li>בדיקת כל ה־guards.</li>
<li>בחירת אחד מה־guarded commands המאופשרים.</li>
<li>ביצוע הצעד האטומי הראשון של הפקודה שנבחרה.</li>
</ul>

לכן תהליכים מקביליים אחרים <b>אינם יכולים להשתלב</b> באמצע שלושת השלבים הללו.
</div>
</div>

<div class="mt-3 bg-yellow-50 px-3 py-2 rounded border border-slate-200">
  <div class="text-[14px] text-slate-600 text-center -mt-1">
    קודם בודקים אילו guards מאופשרים, אחר כך בוחרים אחד מהם, ואת הצעד האטומי הראשון מבצעים בלי interleaving של תהליכים אחרים.
  </div>
</div>

</div>


  <img src=".\images\if-fi-mine.svg" alt="איור קומי של בחירת guarded command ושל סמנטיקת test-and-set" class="absolute bottom-30 right-12 w-110" />

---


# פקודות תנאי: חסימה והקשר ל־if רגיל

<div class="text-[13px] leading-snug -mt-1">

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-amber-50 px-3 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">מתי <span dir="ltr"><code>if-fi</code></span> נתקעת?</div>

אם אף אחד מה־guards <span dir="ltr"><code>g<sub>1</sub>, ..., g<sub>n</sub></code></span>
לא מתקיים במצב הנוכחי, הפקודה <b>נחסמת</b>.

<div class="mt-2">
החסימה נבחנת תמיד בהקשר של מערכת מקבילית: ייתכן שתהליך אחר ישנה משתנים משותפים,
וכך בהמשך אחד ה־guards יהפוך לאמיתי והחסימה תוסר.
</div>
</div>

<div class="bg-rose-50 px-3 py-2 rounded border border-rose-200">
<div class="font-bold mb-1">דוגמה אינטואיטיבית</div>

<div dir="ltr" class="text-left text-[12px] font-mono mt-1 mb-2">
if :: y &gt; 0 -> x := 42 fi
</div>

אם במצב הנוכחי <span dir="ltr"><code>y = 0</code></span>, התהליך ממתין עד שתהליך אחר
ישייך ל־<span dir="ltr"><code>y</code></span> ערך שונה מאפס.
</div>
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">איך מקבלים <span dir="ltr">if-then-else</span> רגיל?</div>

<div dir="ltr" class="text-left text-[12px] font-mono mt-1">
if :: g -> stmt<sub>1</sub> :: !g -> stmt<sub>2</sub> fi
</div>

כך מקודדים מבנה מהצורה:
<span dir="ltr"><code>if g then stmt<sub>1</sub> else stmt<sub>2</sub> fi</code></span>.
</div>

<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">ומה עם <span dir="ltr">if</span> בלי <span dir="ltr">else</span>?</div>

<div dir="ltr" class="text-left text-[12px] font-mono mt-1">
if :: g -> stmt :: !g -> skip fi
</div>

האפשרות השנייה משתמשת ב־<span dir="ltr"><code>skip</code></span>, ולכן אם
<span dir="ltr"><code>g</code></span> שקרי פשוט "לא קורה כלום".
</div>
</div>

</div>

---


# לולאות <span dir="ltr"><code>do-od</code></span>

<div class="text-[13px] leading-snug -mt-1">

<div class="bg-slate-50 px-4 py-2 rounded border border-slate-200 mt-1">
בדומה ל־<span dir="ltr"><code>if-fi</code></span>, גם
<span dir="ltr"><code>do-od</code></span> מבוססת על guarded commands,
אבל כאן מדובר על <b>חזרה</b> כל עוד לפחות guard אחד מתקיים.
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-blue-50 px-3 py-2 rounded border border-blue-200">
<div class="font-bold mb-1">המשמעות האינטואיטיבית</div>

<div dir="ltr" class="text-left text-[12px] font-mono mt-1 mb-2">
do :: g<sub>1</sub> -> stmt<sub>1</sub> ... :: g<sub>n</sub> -> stmt<sub>n</sub> od
</div>

הלולאה מבצעת שוב ושוב בחירה לא־דטרמיניסטית בין כל הפקודות
<span dir="ltr"><code>g<sub>i</sub> -> stmt<sub>i</sub></code></span>
שעבורן ה־guard המתאים מתקיים.
</div>

<div class="bg-amber-50 px-3 py-2 rounded border border-amber-200">
<div class="font-bold mb-1">מה קורה כשאין guard מאופשר?</div>

בשונה מ־<span dir="ltr"><code>if-fi</code></span>, הלולאה <b>אינה נחסמת</b>.
אם כל ה־guards מופרכים במצב הנוכחי, הלולאה פשוט <b>מסתיימת</b>.
</div>
</div>

<div class="grid grid-cols-2 gap-3 mt-2">
<div class="bg-green-50 px-3 py-2 rounded border border-green-200">
<div class="font-bold mb-1">הקשר ל־<span dir="ltr">while</span> רגיל</div>

הלולאה הבודדת

<div dir="ltr" class="text-left text-[12px] font-mono mt-1">
do :: g -> stmt od
</div>

שקולה אינטואיטיבית ל־
<span dir="ltr"><code>while g do stmt od</code></span>,
עם תנאי סיום <span dir="ltr"><code>!g</code></span>.
</div>

<div class="bg-rose-50 px-3 py-2 rounded border border-rose-200">
<div class="font-bold mb-1">הבדל מול Promela</div>

ב־<span dir="ltr">nanoPromela</span> איננו מסיימים לולאות באמצעות
<span dir="ltr"><code>break</code></span>.
הסיום קורה כאשר אין אף guard שמתקיים.
</div>
</div>

</div>


---

 
# דוגמה: אלגוריתם המניעה ההדדית של פטרסון

את אלגוריתם פטרסון עבור שני תהליכים אפשר לנסח ב־`nanoPromela` באמצעות המשתנים הבוליאניים `b1`, `b2`, המשתנה `x` עם `dom(x) = {1,2}`, והמשתנים `crit1`, `crit2`.

- `skip` מייצג את הפעילות בקטע הלא־קריטי.
- `criti := true` מייצג כניסה של התהליך `Pi` לקטע הקריטי.
- בהתחלה: `b1 = b2 = crit1 = crit2 = false`, ואילו `x` שרירותי.

הקוד של `P1`:
<div dir="ltr" align="left" class="bigger-code-block">

```text {lineNumbers: false}
do :: true -> skip;
  atomic{b1 := true; x := 2};
  if :: (x = 1) or !b2 -> crit1 := true fi;
  atomic{crit1 := false; b1 := false}
od
```
</div>

הקוד של `P2` סימטרי: מחליפים את `1` ו־`2`, ואת `b1`, `crit1` ב־`b2`, `crit2`.



---


# דוגמה נוספת: רובוט על Grid עם קירות

נניח רובוט שנע על לוח `3x3`. המיקום שלו נשמר במשתנה יחיד `pos`, ואנחנו רוצים להבטיח שהוא לעולם לא ייכנס לקיר.

<div dir="ltr" class="absolute top-50 right-50 w-60">
  <div class="grid grid-cols-3 gap-2 text-center font-mono text-[22px]">
    <div class="rounded border border-slate-300 bg-white py-2">1</div>
    <div class="rounded border border-slate-300 bg-white py-2">2</div>
    <div class="rounded border border-slate-300 bg-white py-2">3</div>
    <div class="rounded border border-slate-300 bg-white py-2">4</div>
    <div class="rounded border border-rose-400 bg-rose-100 py-2 font-bold text-rose-700">X</div>
    <div class="rounded border border-slate-300 bg-white py-2">6</div>
    <div class="rounded border border-slate-300 bg-white py-2">7</div>
    <div class="rounded border border-rose-400 bg-rose-100 py-2 font-bold text-rose-700">X</div>
    <div class="rounded border border-slate-300 bg-white py-2">9</div>
  </div>
  <div class="mt-2 text-center text-[13px] text-slate-600">X = קיר</div>
</div>

<div dir="ltr" align="left" >

```text {lineNumbers: false}
do
:: pos = 1 -> pos := 2
:: pos = 1 -> pos := 4
:: pos = 2 -> pos := 1
:: pos = 2 -> pos := 3
:: pos = 3 -> pos := 2
:: pos = 3 -> pos := 6
:: pos = 4 -> pos := 1
:: pos = 4 -> pos := 7
:: pos = 6 -> pos := 3
:: pos = 6 -> pos := 9
:: pos = 7 -> pos := 4
:: pos = 9 -> pos := 6
od
```

</div>

- כל guard מתאר צעד חוקי אחד של הרובוט: למעלה, למטה, ימינה או שמאלה.
- אם אין מעבר חוקי, הלולאה מסתיימת.
- אם מתחילים ב־`pos = 1`, אז לאורך כל ריצה מתקיים תמיד `pos ∈ {1,2,3,4,6,7,9}`.

---


# הדגמה: סמנטיקה של פקודות תנאי

נבחן שתי פקודות תנאי שרצות במקביל, כדי לראות שילוב של בחירה לא דטרמיניסטית בענף ובשיבוץ

<div class="grid grid-cols-[1fr_1.2fr] gap-4 mt-2">

<div>


<div class="relative bg-slate-50 px-3 py-2 rounded border border-slate-200 text-sm ml-8" align="left" dir="ltr">
  <div class="absolute top-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>1</sub></span>
  </div>
  <div class="absolute bottom-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>2</sub></span>
  </div>

```text {lineNumbers: false}
if
  :: true -> x := 3
  :: true -> x := 4
fi 
```

</div>


<div class="relative bg-slate-50 mt-2 px-3 py-2 rounded border border-slate-200 text-sm ml-8" align="left" dir="ltr">
  <div class="absolute top-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>1</sub></span>
  </div>
  <div class="absolute bottom-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>2</sub></span>
  </div>


  ```text {lineNumbers: false}
if
    :: x > 3 -> y := 1
    :: x > 2 -> y := 2 
fi 
  ```

</div>

</div>

<div class="flex flex-col items-center justify-center -mt-0 -ml-6 border border-slate-200 rounded pt-8 bg-slate-50 relative">

<div class="absolute top-2 right-3 font-bold text-slate-500 text-sm">מרחב המצבים</div>

<TransitionSystemD3
  :width="600"
  :height="100"
  :scale="70"
  :states="[
  { id: 's1', text: '$l_1, l_1, x \\mapsto 0, y \\mapsto 0$',     x: 300, y: 50 -140, width: 220, color: '#FEF08A', rx: 0, stroke: '#d4af37', initial: true, initialDirection: 'top' },
  { id: 's2_3', text: '$l_1, l_2, x \\mapsto 3, y \\mapsto 0$',   x: 130, y: 150-140, width: 220, color: '#FEF08A', rx: 0, stroke: '#d4af37' },
  { id: 's2_4', text: '$l_1, l_2, x \\mapsto 4, y \\mapsto 0$',   x: 470, y: 150-140, width: 220, color: '#FEF08A', rx: 0, stroke: '#d4af37' },
  { id: 's3_3_2', text: '$l_2, l_2, x \\mapsto 3, y \\mapsto 2$', x: 130, y: 250-140, width: 220, color: '#FEF08A', rx: 0, stroke: '#d4af37' },
  { id: 's3_4_1', text: '$l_2, l_2, x \\mapsto 4, y \\mapsto 1$', x: 360, y: 250-140, width: 200, color: '#FEF08A', rx: 0, stroke: '#d4af37' },
  { id: 's3_4_2', text: '$l_2, l_2, x \\mapsto 4, y \\mapsto 2$', x: 570, y: 250-140, width: 200, color: '#FEF08A', rx: 0, stroke: '#d4af37' }
  ]"
  :transitions="[
  { source: 's1', target: 's2_3', stroke: '#A1824A', strokeWidth: 2 },
  { source: 's1', target: 's2_4', stroke: '#A1824A', strokeWidth: 2 },
  { source: 's2_3', target: 's3_3_2', stroke: '#A1824A', strokeWidth: 2 },
  { source: 's2_4', target: 's3_4_1', stroke: '#A1824A', strokeWidth: 2 },
  { source: 's2_4', target: 's3_4_2', stroke: '#A1824A', strokeWidth: 2 }
  ]"
/>

</div>

</div>

<div class="mt-4 text-[14px] leading-snug">

- ב־$l_1, l_1$ שתי האפשרויות מאופשרות, לכן אפשר להגיע ל־$x = 3$ וגם ל־$x = 4$.

- אם מגיעים ל־$l_1, l_2$ עם $x = 3$, רק ה־guard $x > 2$ מאופשר ולכן חייבים לקבל $y = 2$ ומגיעים למצב הסיום $l_2, l_2$.
- אם מגיעים ל־$l_1, l_2$ עם $x = 4$, שני ה־guards מאופשרים ולכן אפשר לקבל גם $y = 1$ וגם $y = 2$ ומגיעים למצב הסיום $l_2, l_2$ בכל מקרה.
- כלומר, ה־`if-fi` הראשון מייצר אי־דטרמיניזם, והשני עלול להוסיף עליו אי־דטרמיניזם נוסף.

</div>

---


# הדגמה: סמנטיקה של לולאות

השקפים מדגישים שתי התנהגויות שונות של `do-od`: לולאה שיכולה להסתיים, ולולאה שאין לה מצב יציאה.

<div class="grid grid-cols-[1fr_1.2fr] gap-4 mt-2">

<div>

<div class="relative bg-slate-50 px-3 py-2 rounded border border-slate-200 text-sm ml-8" align="left" dir="ltr">
  <div class="absolute top-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>1</sub></span>
  </div>
  <div class="absolute bottom-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>2</sub></span>
  </div>

  ```text {lineNumbers: false}
do
     :: x < 3 -> skip
od
  ```

</div>

<div class="relative bg-slate-50 mt-2 px-3 py-2 rounded border border-slate-200 text-sm ml-8" align="left" dir="ltr">
  <div class="absolute top-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>1</sub></span>
  </div>
  <div class="absolute bottom-1.5 -left-8 bg-white border border-slate-300 px-1.5 py-0.5 text-xs rounded shadow-sm flex items-center justify-center font-math z-10 w-6 h-6">
      <div class="absolute -right-2 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[6px] border-t-transparent border-b-[6px] border-b-transparent border-l-[6px] border-l-slate-300"></div>
      <div class="absolute -right-1.5 top-1/2 -translate-y-1/2 w-0 h-0 border-t-[5px] border-t-transparent border-b-[5px] border-b-transparent border-l-[5px] border-l-white z-10"></div>
      <span class="-ml-1 text-[13px]"><i class="font-serif">l</i><sub>2</sub></span>
  </div>

  ```text {lineNumbers: false}
do
     :: true -> x := 3
     :: true -> x := 0
od
  ```

</div>

</div>

<div class="flex flex-col items-center justify-center -mt-0 -ml-6 border border-slate-200 rounded pt-8 bg-slate-50 relative">

<div class="absolute top-2 right-3 font-bold text-slate-500 text-sm">מרחב המצבים</div>

<TransitionSystemD3
  :width="640"
  :height="380"
  :scale="80"
  :states="[
  { id: 's1_0', text: '$l_1, l_1, x \\mapsto 0$', x: 350, y: 50,  width: 120, color: '#FEF08A', rx: 0, stroke: '#d4af37', initial: true, initialDirection: 'top' },
  { id: 's1_3', text: '$l_1, l_1, x \\mapsto 3$', x: 350, y: 170, width: 120, color: '#FEF08A', rx: 0, stroke: '#d4af37' },
  { id: 's2_3', text: '$l_2, l_1, x \\mapsto 3$', x: 350, y: 300, width: 120, color: '#FEF08A', rx: 0, stroke: '#d4af37' },
  { id: 's2_0', text: '$l_2, l_1, x \\mapsto 0$', x: 90, y: 300, width: 120, color: '#FEF08A', rx: 0, stroke: '#d4af37' }
  ]"  
  :transitions="[
  { source: 's1_0', target: 's1_3', action: 'x:=3', stroke: '#A1824A', strokeWidth: 2, actionX: 28 },
  { source: 's1_0', target: 's1_0', action: 'x:=0', stroke: '#A1824A', strokeWidth: 2, loopDirection: '-150deg', loopRadius: 108, loopLabelRadius: 96, actionWidth: 72, actionX: -6, actionY: -4 },
  { source: 's1_0', target: 's1_0', action: 'skip', stroke: '#A1824A', strokeWidth: 2, loopDirection: '-30deg', loopRadius: 108, loopLabelRadius: 96, actionWidth: 72, actionX: 8, actionY: -4 },
  { source: 's1_3', target: 's1_3', action: 'x:=3', stroke: '#A1824A', strokeWidth: 2, loopDirection: '10deg', loopRadius: 104, loopLabelRadius: 92, actionWidth: 72, actionX: 8 },
  { source: 's1_3', target: 's1_0', action: 'x:=0', curve: -.5, stroke: '#A1824A', strokeWidth: 2, actionX: -30, actionY: -6 },
  { source: 's1_3', target: 's2_3', action: 'nothing', stroke: '#A1824A', strokeWidth: 2, actionWidth: 86, actionX: 34 },
  { source: 's2_3', target: 's2_3', action: 'x:=3', stroke: '#A1824A', strokeWidth: 2, loopDirection: '20deg', loopRadius: 104, loopLabelRadius: 92, actionWidth: 72, actionX: 10, actionY: 4 },
  { source: 's2_3', target: 's2_0', action: 'x:=0', stroke: '#A1824A', strokeWidth: 2, actionX: 0, actionY: -10 },
  { source: 's2_0', target: 's2_0', action: 'x:=0', stroke: '#A1824A', strokeWidth: 2, loopDirection: '-170deg', loopRadius: 100, loopLabelRadius: 88, actionWidth: 72, actionX: -10 },
  { source: 's2_0', target: 's2_3', action: 'x:=3', curve: .1, stroke: '#A1824A', strokeWidth: 2, actionY: 17 }
  ]"
/>

</div>

</div>

<div class="mt-4 text-[14px] leading-snug">

- אם $x < 3$, הלולאה הראשונה יכולה לבצע צעד $skip$ ולהישאר במקום.
- אם $x \ge 3$, אין אף guard מאופשר והלולאה הראשונה מסתיימת (מעבר $nothing$ מהמיקום הראשון לשני).
- בלולאה השנייה תמיד קיים guard מאופשר ($true$), ולכן היא אינה מסתיימת לעולם.
- המסר העיקרי: לולאות ב־`nanoPromela` אינן נתקעות. הן ממשיכות לרוץ כל עוד יש guard מאופשר, ויוצאות ברגע שכולם שקריים.

</div>
---




# מכאן להגדרות פורמליות


כדי לתת משמעות מדויקת ל־`nanoPromela`, לא מספיק תיאור אינטואיטיבי. אנחנו רוצים לעבור לשפה שכבר למדנו לעבוד איתה: גרפי תוכנית, ואז מערכות ערוצים ולבסוף מערכות מעברים.

$$
\text{stmt}
\Longrightarrow
\text{sub(stmt)}
\Longrightarrow
\text{Program Graph}
\Longrightarrow
\text{Channel System}
\Longrightarrow
\text{Transition System}
$$

1. מגדירים רקורסיבית את קבוצת המקומות: `Loc = sub(stmt)`.
2. גוזרים את המעברים בין המקומות בעזרת כללי היסק.

הטריק הטכני הוא ששם של מקום בתוכנית הוא פשוט "מה עוד נשאר לבצע".

<img src=".\images\location_is_todo.png" alt="איור קומי המסביר שמקום בתוכנית הוא פשוט רשימת המשימות שנותרו" class="absolute bottom-2 left-60 w-50 transform -rotate-1 hover:rotate-10 transition-transform" />

---


# הדגמה חיה: תרגום ננו-פרומלה לגרף תוכנית

<script setup>
const liveNanoPromelaExample = `if
:: x > 1 -> y := x + y
:: true  -> x := 0; y := x
fi`
</script>

<NanoPromelaProgramGraphRunner
  src="nanopromela_pg_lib.py"
  :initial-code="liveNanoPromelaExample"
/>

---


# הגדרה: המקומות הם תת־הפקודות

<div class="text-[0.9em] leading-tight">

נסמן ב־$\operatorname{sub}(stmt)$ את קבוצת תת־הפקודות של `stmt`. זוהי בדיוק קבוצת המקומות בגרף התוכנית, כולל `exit`.

$$
\begin{aligned}
\operatorname{sub}(\texttt{skip})
  &= \{ \texttt{skip}, \texttt{exit} \} \\
\operatorname{sub}(\texttt{x := expr})
  &= \{ \texttt{x := expr}, \texttt{exit} \} \\
\operatorname{sub}(\texttt{c?x})
  &= \{ \texttt{c?x}, \texttt{exit} \} \\
\operatorname{sub}(\texttt{c!expr})
  &= \{ \texttt{c!expr}, \texttt{exit} \} \\
\operatorname{sub}(\mathtt{atomic}\{a_1; \ldots; a_m\})
  &= \{ \mathtt{atomic}\{a_1; \ldots; a_m\}, \texttt{exit} \} \\[0.95em]

\operatorname{sub}(stmt_1 ; stmt_2)
  &= \{\, s' ; stmt_2 \mid s' \in \operatorname{sub}(stmt_1) \setminus \{ \texttt{exit} \} \,\} \cup \operatorname{sub}(stmt_2) \\[0.95em]

\operatorname{sub}(\texttt{if } :: g_1 \texttt{ -> } stmt_1 \cdots :: g_n 
\texttt{ -> } stmt_n \texttt{ fi})
  &= \{ \texttt{cond\_cmd} \} \\
  &\qquad \cup \operatorname{sub}(stmt_1) \cup \cdots \cup \operatorname{sub}(stmt_n) \\[0.95em]

\operatorname{sub}(\texttt{do } :: g_1 \texttt{ -> } stmt_1 \cdots :: g_n \texttt{ -> } stmt_n \texttt{ od})
  &= \{ \texttt{loop\_cmd}, \texttt{exit} \} \\ 
  &\qquad \cup \bigcup_i \{\, s' ; \texttt{loop\_cmd} \mid s' \in \operatorname{sub}(stmt_i) \setminus \{ \texttt{exit} \} \,\}
\end{aligned}
$$

</div>

---
clicks: 5
---

# דוגמה מונחית: חישוב `sub(stmt)` עבור `if`

<NanoPromelaSubTree example="if-basic" />

---
clicks: 5
---

# דוגמה מונחית: חישוב `sub(stmt)` עבור `do`

<NanoPromelaSubTree example="do-basic" />

---
clicks: 4
---

# דוגמה מונחית: קינון של `if` ו־`do`

<NanoPromelaSubTree example="nested-if-do" />

---

# כללי גזירה: פקודות בסיסיות והרכבה

המעברים בגרף התוכנית מתקבלים מכללי גזירה. כל מעבר מסומן על ידי guard ופעולה מן הצורה $g : \alpha$.

<div class="text-[0.9em] leading-tight">

<div class="font-bold mb-1">אקסיומות לפקודות אטומיות</div>

$$
\begin{aligned}
\texttt{skip} &\xrightarrow{true : id} \texttt{exit} \\
\texttt{x := expr} &\xrightarrow{true : \texttt{x := expr}} \texttt{exit} \\
\texttt{c?x} &\xrightarrow{true : \texttt{c?x}} \texttt{exit} \\
\texttt{c!expr} &\xrightarrow{true : \texttt{c!expr}} \texttt{exit} \\
\mathtt{atomic}\{a_1; \ldots; a_m\} &\xrightarrow{true : a_1; \ldots; a_m} \texttt{exit}
\end{aligned}
$$

<div class="font-bold mb-1">כללי הרכבה סדרתית</div>

$$
\frac{stmt_1 \xrightarrow{g : \alpha} stmt_1' \qquad stmt_1' \neq \texttt{exit}}
     {stmt_1 ; stmt_2 \xrightarrow{g : \alpha} stmt_1' ; stmt_2}
\hspace{6em}
\frac{stmt_1 \xrightarrow{g : \alpha} \texttt{exit}}
     {stmt_1 ; stmt_2 \xrightarrow{g : \alpha} stmt_2}
$$

</div>

---


# כללי גזירה: תנאי ולולאה

<div class="text-[0.9em] leading-tight">

<div class="font-bold mb-1">פקודת תנאי</div>

$$
\frac{stmt_i \xrightarrow{h : \alpha} stmt_i'}
     {\texttt{cond\_cmd} \xrightarrow{(g_i \land h) : \alpha} stmt_i'}
$$

<div class="font-bold mb-1">פקודת לולאה</div>

$$
\frac{stmt_i \xrightarrow{h : \alpha} stmt_i' \qquad stmt_i' \neq \texttt{exit}}
     {\texttt{loop\_cmd} \xrightarrow{(g_i \land h) : \alpha} stmt_i' ; \texttt{loop\_cmd}}
$$

$$
\frac{stmt_i \xrightarrow{h : \alpha} \texttt{exit}}
     {\texttt{loop\_cmd} \xrightarrow{(g_i \land h) : \alpha} \texttt{loop\_cmd}}
\hspace{6em}
\texttt{loop\_cmd} \xrightarrow{(\neg g_1 \land \cdots \land \neg g_n) : id} \texttt{exit}
$$

</div>

הכלל האחרון הוא בדיוק הסיבה לכך שלולאות אינן נחסמות: כאשר אין guard מאופשר, יוצאים מן הלולאה.

דוגמה אופיינית: בפקודה `if :: y == 0 -> do :: x < 3 -> x := x + 1 od fi` מתקבל מעבר ראשון עם guard משולב `y == 0 ∧ x < 3`.

---
clicks: 5
---

# דוגמה מונחית: גזירת מעברי PG עבור `if`

<NanoPromelaGraphDerivation example="if-basic" />

---
clicks: 6
---

# דוגמה מונחית: גזירת מעברי PG עבור `do`

<NanoPromelaGraphDerivation example="do-basic" />

---
clicks: 7
---

# דוגמה מונחית: גזירת מעברי PG עבור קינון

<NanoPromelaGraphDerivation example="nested-if-do" />

---

# הדגמה חיה: תרגום ננו-פרומלה לגרף תוכנית

<script setup>
const liveNanoPromelaDoExample = `do
:: x > 1 -> y := x + y
:: y < x -> x := 0; y := x
od`
</script>

<NanoPromelaProgramGraphRunner
  src="nanopromela_pg_lib.py"
  :initial-code="liveNanoPromelaDoExample"
/>

---

# הדגמה חיה: תרגום ננו-פרומלה לגרף תוכנית

<script setup>
const liveNanoPromelaNestedExample = `if
:: y == 0 -> do
             :: x < 3 -> x := x + 1
           od
:: true  -> skip
fi`
</script>

<NanoPromelaProgramGraphRunner
  src="nanopromela_pg_lib.py"
  :initial-code="liveNanoPromelaNestedExample"
/>
