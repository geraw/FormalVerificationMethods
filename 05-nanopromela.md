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
  ## NanoPromela
  מרצה: גרא וייס
---

# NanoPromela
## הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="https://in.bgu.ac.il/marketing/DocLib/Pages/graphics/just-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# 2.2.5 NanoPromela

<div class="text-[13px] leading-snug">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 mt-2">
המודלים שראינו עד עכשיו, כמו <span dir="ltr">program graphs</span>, הרכבה מקבילית ו־<span dir="ltr">channel systems</span>,
מספקים בסיס מתמטי מדויק למידול מערכות תגובתיות. אבל כדי לבנות כלים אוטומטיים לאימות,
נוח יותר לעבוד עם <b>שפת מפרט קטנה ופשוטה</b> שממנה אפשר לגזור את המודל הפורמלי.
</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="bg-blue-50 p-3 rounded border border-blue-200">
    <div class="font-bold mb-2">מה אנחנו רוצים משפת מפרט?</div>
    <ul class="list-disc pr-5 space-y-1">
      <li>שתהיה פשוטה וקלה להבנה, גם עבור משתמשים שאינם מומחים.</li>
      <li>שתהיה מספיק אקספרסיבית כדי לתאר התנהגות צעד־אחר־צעד של תהליכים ואינטראקציות.</li>
      <li>שתאפשר לתאר גם חישוב מקומי וגם תקשורת בין תהליכים.</li>
    </ul>
  </div>

  <div class="bg-orange-50 p-3 rounded border border-orange-200">
    <div class="font-bold mb-2">למה חייבים סמנטיקה פורמלית?</div>
    <ul class="list-disc pr-5 space-y-1">
      <li>כדי שהמשמעות של כל פקודה תהיה חד־משמעית.</li>
      <li>כדי לשייך לכל תוכנית מערכת מעברים פורמלית.</li>
      <li>כדי לאפשר סימולציה ו־model checking מול נוסחאות זמן.</li>
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

# NanoPromela ו־Promela

<div class="text-[12.5px] leading-snug">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 mt-2">
<b>NanoPromela</b> היא תת־שפה קטנה של <b>Promela</b>, שפת הקלט של בודק המודלים
<b>SPIN</b>. הרעיון הוא לעבוד עם גרסה קומפקטית של השפה, אבל עם סמנטיקה שמתבססת
בדיוק על אותם מושגים שכבר פיתחנו.
</div>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="bg-green-50 p-3 rounded border border-green-200">
    <div class="font-bold mb-2">מבנה התוכנית</div>

    $$
    P = [P_1 \mid \ldots \mid P_n]
    $$

    כל תוכנית מורכבת ממספר סופי של תהליכים שרצים במקביל.

    התקשורת יכולה להיעשות באמצעות:
    <ul class="list-disc pr-5 mt-1 space-y-1">
      <li>משתנים משותפים</li>
      <li>ערוצי FIFO סינכרוניים או מאוגרים</li>
    </ul>
  </div>

  <div class="bg-blue-50 p-3 rounded border border-blue-200">
    <div class="font-bold mb-2">איך מתארים התנהגות?</div>

    Promela משתמשת בשפת <span dir="ltr">guarded commands</span>:
    תנאי (guard) יחד עם פעולה.

    היא כוללת בין היתר:
    <ul class="list-disc pr-5 mt-1 space-y-1">
      <li>השמות למשתנים</li>
      <li>תנאים, לולאות והרכבה סדרתית</li>
      <li>שליחה וקבלה מערוצים</li>
      <li>אזורים אטומיים שמונעים interleavings לא רצויים</li>
    </ul>
  </div>
</div>

<div class="mt-4 bg-amber-50 p-3 rounded border border-amber-200">
Promela אינה משתמשת בדרך כלל ב־<span dir="ltr">action names</span> נפרדים; במקום זאת,
הפקודה עצמה מתארת ישירות את האפקט של הצעד. הסמנטיקה הפורמלית של תוכנית Promela
ניתנת דרך <span dir="ltr">channel system</span>, ומשם נפרסת ל־<span dir="ltr">transition system</span>.
</div>

</div>

