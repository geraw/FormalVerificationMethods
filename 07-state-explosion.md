---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 07-state-explosion
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## State-Space Explosion
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# בעיית פיצוץ המצבים

##   הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-2 gap-6 mt-6 items-start text-right">
<div class="bg-slate-50 p-4 rounded border border-slate-200">
<div class="font-bold mb-3">נבין מה הבעיה</div>

- למה גודל מערכת המעברים הוא צוואר בקבוק מרכזי באימות.
- למה מערכות פשוטות לכאורה מייצרות מרחבי מצבים עצומים.
- למה משתנים, רכיבים מקבילים וערוצים גורמים לצמיחה אקספוננציאלית.
</div>

<div class="bg-blue-50 p-4 rounded border border-blue-200">
<div class="font-bold mb-3">נלמד לאמוד גדלים</div>

- עבור פריסה של גרפי תוכנית.
- עבור מעגלים סדרתיים.
- עבור הרכבה מקבילית.
- עבור מערכות ערוצים.
</div>
</div>

<div class="mt-6 bg-amber-50 border border-amber-200 rounded p-4 text-right text-[15px]">
המטרה כאן אינה עדיין לפתור את הבעיה, אלא להבין <b>מאיפה היא נוצרת</b> ולמה אי אפשר להתעלם ממנה.
</div>

---

# מאיפה מגיעות מערכות המעברים?

<div class="grid grid-cols-4 gap-4 mt-8 text-right text-[14px]">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold text-slate-700 mb-2">גרף תוכנית</div>
<div>פריסה לפי מיקומים, משתנים ושומרים</div>
<div class="text-center text-2xl my-3">↓</div>
<div class="font-bold">מערכת מעברים</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold text-slate-700 mb-2">מערכת מקבילית</div>
<div>שזירה או מכפלה של רכיבים מקומיים</div>
<div class="text-center text-2xl my-3">↓</div>
<div class="font-bold">מערכת מעברים גלובלית</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold text-slate-700 mb-2">מערכת ערוצים</div>
<div>מיקומים + משתנים + תוכן ערוצים</div>
<div class="text-center text-2xl my-3">↓</div>
<div class="font-bold">TS(CS)</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold text-slate-700 mb-2">מעגל סדרתי</div>
<div>קלטים, אוגרים ופונקציות בקרה</div>
<div class="text-center text-2xl my-3">↓</div>
<div class="font-bold">מערכת מעברים</div>
</div>
</div>

<div class="mt-8 bg-rose-50 border border-rose-200 rounded p-4 text-right">
בכל אחד מן המקרים האלגוריתמים של אימות מודלים פועלים על <b>מערכת המעברים המתקבלת</b>, לא על התיאור הקומפקטי המקורי.
</div>

---

# מהי בעיית פיצוץ המצבים?

<div class="grid grid-cols-2 gap-8 mt-6 items-start text-right">
<div>

מערכת מעברים היא המודל שעליו רצים אלגוריתמי האימות.  
לכן, זמן הריצה וכמות הזיכרון תלויים במידה מכרעת ב:

- מספר המצבים $|S|$
- מספר המעברים $|\to|$

בפועל, הגורם הדומיננטי הוא בדרך כלל גודל מרחב המצבים.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5 text-center">
<div class="text-xl font-bold mb-3">State-Space Explosion</div>
<div class="text-[15px] leading-relaxed">
צמיחה אקספוננציאלית, ולעיתים אף אינסופית, של מערכת המעברים
שמייצרים מן המודל הקומפקטי של המערכת.
</div>
</div>
</div>

<div class="mt-8 bg-red-50 border border-red-200 rounded p-4 text-right">
זהו אחד המחסומים המרכזיים של model checking:  
המודל המקורי קצר, אבל הסמנטיקה המפורשת שלו עלולה להיות עצומה.
</div>

---

# גרפי תוכנית: פריסה למערכת מעברים

<div class="text-right text-[15px] leading-snug">

אם לכל המשתנים יש תחומים סופיים, ומספר המיקומים בגרף סופי, אז מספר המצבים בפריסה הוא:

$$
|Loc| \cdot \prod_{x \in Var} |dom(x)|
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-6 items-start text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">מסקנה</div>

- מספר המצבים גדל אקספוננציאלית במספר המשתנים.
- אם יש $N$ משתנים, ולכל אחד עד $k$ ערכים, נקבל סדר גודל של $k^N$.
- אם אחד התחומים אינסופי, מערכת המעברים עלולה להיות אינסופית.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold mb-2">דוגמה</div>

גרף תוכנית עם:

- $10$ מיקומים
- $3$ משתנים בוליאניים
- $5$ משתנים בטווח $\{0,\dots,9\}$

ייתן:

$$
10 \cdot 2^3 \cdot 10^5 = 8{,}000{,}000
$$

מצבים.
</div>
</div>

<div class="mt-6 bg-rose-50 border border-rose-200 rounded p-4 text-right">
הוספת מערך ביטים אחד באורך $50$ מכפילה את המספר ב-$2^{50}$.
</div>

---

# מעגלים סדרתיים

<div class="grid grid-cols-2 gap-6 mt-8 items-center text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
במעגל סדרתי, מצבים נקבעים על ידי:

- ערכי משתני הקלט
- ערכי האוגרים

אם יש $N$ קלטים בינאריים ו-$K$ אוגרים, מספר המצבים הוא:

$$
2^{N+K}
$$
</div>

<div class="bg-green-50 border border-green-200 rounded p-5 text-center">
<div class="text-lg font-bold mb-3">המסר</div>
<div class="text-[16px] leading-relaxed">
גם כאשר כל המשתנים הם רק ביטים,
מספיקים מעט קלטים ואוגרים כדי לייצר מערכת עצומה.
</div>
</div>
</div>

<div class="mt-8 text-right text-[15px]">
לכן גם באימות חומרה, גודל המודל אינו נמדד בשורות תיאור אלא במספר כל הקונפיגורציות האפשריות של האוגרים והקלטים.
</div>

---

# הרכבה מקבילית

<div class="text-right text-[15px] leading-snug">

בכל אופרטור הרכבה מקבילית שראינו, המצב הגלובלי נבנה כמכפלה קרטזית של המצבים המקומיים:

$$
S = S_1 \times S_2 \times \cdots \times S_n
$$

ולכן:

$$
|S| = |S_1| \cdot |S_2| \cdots |S_n|
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-6 items-start text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">בפרט</div>

אם יש $N$ רכיבים, וכל רכיב בגודל $k$, נקבל:

$$
k^N
$$

מצבים.
</div>

<div class="bg-orange-50 border border-orange-200 rounded p-4">
<div class="font-bold mb-2">למה זה קורה?</div>

כל רכיב מוסיף עוד ציר למרחב המצבים.  
גם אם כל רכיב קטן בפני עצמו, המכפלה שלהם גדלה מהר מאוד.
</div>
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-4 text-right">
לכן מערכות מקביליות סובלות באופן טבעי מ-state explosion, אפילו כאשר כל תהליך בודד קטן ופשוט.
</div>

---

# מערכות ערוצים

<div class="text-right text-[15px] leading-snug">
במערכת ערוצים, המצב הגלובלי כולל שלושה מרכיבים:

- המיקום של כל תהליך
- ערכי המשתנים
- תוכן כל אחד מן הערוצים

אם לכל ערוץ $c$ יש קיבולת סופית $cap(c)$, אז מספר האפשרויות לתוכן של $c$ הוא:

$$
\sum_{j=0}^{cap(c)} |dom(c)|^j
$$

ולכן נקבל חסם מהצורה:

$$
\left(\prod_{i=1}^{n} |Loc_i|\right)
\cdot
\left(\prod_{x \in Var} |dom(x)|\right)
\cdot
\left(\prod_{c \in Chan} \sum_{j=0}^{cap(c)} |dom(c)|^j\right)
$$
</div>

<div class="grid grid-cols-2 gap-6 mt-6 items-start text-right">
<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold mb-2">דוגמת ערוץ יחיד</div>

אם:

- $|dom(c)| = 5$
- $cap(c)=3$

אז מספר התכנים האפשריים הוא:

$$
1 + 5 + 5^2 + 5^3 = 156
$$
</div>

<div class="bg-rose-50 border border-rose-200 rounded p-4">
<div class="font-bold mb-2">מסקנה</div>

- אם ערוץ אחד הוא בעל קיבולת אינסופית, מרחב המצבים עלול להיות אינסופי.
- גם קיבולות סופיות יוצרות גידול חד מאוד.
- ערוצים הופכים תקשורת אסינכרונית ליקרה במיוחד מבחינת state space.
</div>
</div>

---

# דוגמה: Alternating Bit Protocol

<div class="grid grid-cols-2 gap-6 mt-6 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">נתוני הדוגמה</div>

- לשולח $8$ מיקומים
- למקבל $6$ מיקומים
- לטיימר $2$ מיקומים
- לערוץ $c$ קיבולת $10$
- בערוץ $c$ נשלחים נתון + ביט בקרה, ולכן $|dom(c)| = 4$
- בערוץ $d$ נשלחים ביטי בקרה, ולכן $|dom(d)| = 2$
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5 text-center">
<div class="font-bold mb-3">מספר המצבים</div>

$$
2 \cdot 8 \cdot 6 \cdot 4^{10} \cdot 2^{10}
$$

$$
= 3 \cdot 2^{35}
\approx 10^{11}
$$

מצבים
</div>
</div>

<div class="mt-6 bg-red-50 border border-red-200 rounded p-4 text-right">
המשמעות: גם מודל קטן ומפושט של פרוטוקול תקשורת קלאסי כבר גדול מכדי לחקור באופן מפורש ותמים.
</div>

---

# למה זה חמור כל כך?

<div class="grid grid-cols-2 gap-6 mt-6 items-start text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">עבור אימות מפורש</div>

- צריך לאחסן מצבים שכבר נצפו.
- צריך לחשב יורשים של מצבים.
- צריך לבדוק תכונות על גרף עצום.

כל אלה צורכים זמן וזיכרון שגדלים יחד עם מרחב המצבים.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-4">
<div class="font-bold mb-2">עבור מודלים לא חסומים</div>

- תחומי ערכים אינסופיים
- ערוצים לא חסומים
- מספר לא חסום של קונפיגורציות

עלולים להוביל אפילו למערכת מעברים אינסופית, ולעיתים לבעיות אימות לא כריעות.
</div>
</div>

<div class="mt-8 bg-green-50 border border-green-200 rounded p-4 text-right">
לכן שאלת המפתח אינה רק <b>"איך מאמתים?"</b> אלא גם <b>"על איזה מודל מאמתים?"</b>.
</div>

---

# איך מתמודדים?

<div class="text-right text-[15px] leading-snug">
לא מסתפקים במודל המפורש כפי שהוא. קיימות כמה משפחות של פתרונות:
</div>

<div class="grid grid-cols-3 gap-5 mt-8 text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">אבסטרקציה ושקילויות</div>

לבנות מודל קטן יותר, אך כזה ששומר את התכונות הרלוונטיות.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold mb-2">ייצוג סימבולי</div>

לייצג קבוצות גדולות של מצבים באופן קומפקטי במקום למנות כל מצב בנפרד.
</div>

<div class="bg-orange-50 border border-orange-200 rounded p-4">
<div class="font-bold mb-2">Partial Order Reduction</div>

לנצל עצמאות בין פעולות כדי לא לחקור את כל השזירות האפשריות.
</div>
</div>

<div class="mt-8 bg-slate-50 border border-slate-200 rounded p-4 text-right">
במילים אחרות: לא מוותרים על אימות מודלים, אלא מחפשים ייצוגים ואלגוריתמים שמנטרלים את הפיצוץ.
</div>

---

# סיכום

<div class="text-right text-[15px] leading-relaxed">

- בעיית פיצוץ המצבים היא תוצאה ישירה של המעבר ממודל קומפקטי למערכת מעברים מפורשת.
- בגרפי תוכנית, מספר המצבים גדל אקספוננציאלית במספר המשתנים.
- במערכות מקבילות, הוא גדל אקספוננציאלית במספר הרכיבים.
- במערכות ערוצים, גם תוכן הערוצים מוסיף גורם קומבינטורי כבד מאוד.
- אם יש תחומים או קיבולות אינסופיים, מתקבלת לעיתים מערכת מעברים אינסופית.
- לכן הצלחתו של model checking תלויה לא רק בלוגיקה ובאלגוריתם, אלא גם ביכולת להקטין או לייצג בחכמה את מרחב המצבים.

</div>

<div class="mt-8 bg-indigo-50 border border-indigo-200 rounded p-4 text-right">
זה בדיוק המניע לשיטות שנפגוש בהמשך: שקילויות, אבסטרקציה, ייצוג סימבולי והפחתת שזירות.
</div>
