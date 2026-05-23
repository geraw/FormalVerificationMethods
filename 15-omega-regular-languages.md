---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 15-omega-regular-languages
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## שפות ω-רגולריות
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# שפות <KatexInline math="\omega" />-רגולריות

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# תכנית להמשך: אימות תכונות <KatexInline math="\omega" />-רגולריות

<div class="relative mt-8">
<div class="absolute top-[-14px] bottom-[-34px] left-[33.2%] border-l-2 border-dashed border-slate-700"></div>
<div class="absolute bottom-[-40px] left-[calc(33.2%_+_1rem)] text-[16px] whitespace-nowrap text-slate-700" dir="ltr">
← עד כאן הגענו
</div>

<div class="grid grid-cols-3 gap-5 text-center text-[17px] leading-snug" dir="rtl">
<div class="flex flex-col gap-1.5">
<div class="bg-slate-50 border border-slate-200 text-slate-800 shadow-sm rounded p-3 h-[88px] flex items-center justify-center font-bold">
תכונות שמורה
</div>
<div class="text-slate-400 text-[24px] leading-none">↓</div>
<div class="bg-slate-50 border border-slate-200 text-slate-800 shadow-sm rounded p-3 h-[88px] flex items-center justify-center">
מיוצגות על ידי נוסחה לוגית המתארת מצבים העומדים בתנאי השמורה
</div>
<div class="text-slate-400 text-[24px] leading-none">↓</div>
<div class="bg-slate-50 border border-slate-200 text-slate-800 shadow-sm rounded px-3 py-2 h-[88px] flex items-center justify-center">
<div>
נבדקות באמצעות<br><span dir="ltr">BFS</span> או <span dir="ltr">DFS</span>
</div>
</div>
</div>

<div class="flex flex-col gap-1.5">
<div class="bg-slate-50 border border-slate-200 text-slate-800 shadow-sm rounded p-3 h-[88px] flex items-center justify-center font-bold">
תכונות בטיחות רגולריות
</div>
<div class="text-slate-400 text-[24px] leading-none">↓</div>
<div class="bg-slate-50 border border-slate-200 text-slate-800 shadow-sm rounded p-3 h-[88px] flex items-center justify-center">
מיוצגות על ידי אוטומט המתאר את קבוצת הרישות הרעות
</div>
<div class="text-slate-400 text-[24px] leading-none">↓</div>
<div class="bg-slate-50 border border-slate-200 text-slate-800 shadow-sm rounded px-3 py-2 h-[88px] flex items-center justify-center">
<div>
נבדקות על ידי הרכבה<br><span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span><br>ורדוקציה לשמורה
</div>
</div>
</div>

<div class="flex flex-col gap-1.5">
<div class="bg-blue-50 border-2 border-blue-300 text-blue-900 shadow-md rounded p-3 h-[88px] flex items-center justify-center font-bold">
תכונות   
<KatexInline math="\omega\," />-רגולריות
</div>
<div class="text-slate-400 text-[24px] leading-none">↓</div>
<div class="bg-blue-50 border-2 border-blue-300 text-blue-900 shadow-md rounded p-3 h-[88px] flex items-center justify-center">
מיוצגות על ידי אוטומט המתאר מילים אינסופיות
</div>
<div class="text-slate-400 text-[24px] leading-none">↓</div>
<div class="bg-blue-50 border-2 border-blue-300 text-blue-900 shadow-md rounded px-3 py-2 h-[88px] flex items-center justify-center">
<div>
נבדקות על ידי הרכבה<br><span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span><br>וסריקת מעגלים בגרף
</div>
</div>
</div>
</div>
</div>

---

# חידון

<div class="relative h-[500px] mt-2">
<div class="text-right text-[24px] mb-5">
מי מהבאים הם ביטויים אומגה רגולריים חוקיים?
</div>

<div class="absolute left-[19%] top-[70px] w-[60%] bg-white border border-slate-200 shadow-sm py-3 px-5 text-center text-[25px]" dir="ltr">
<KatexInline display math="(\{a\}+\{a,b\})^*+(\{b\}+\emptyset)^\omega" />
</div>

<div class="absolute left-[19%] top-[160px] w-[60%] bg-white border border-slate-200 shadow-sm py-3 px-5 text-center text-[25px]" dir="ltr">
<KatexInline display math="(\{a\}+\{a,b\})^*\cdot(\{b\}+\epsilon)^\omega+\{a\}^\omega" />
</div>

<div class="absolute left-[19%] top-[250px] w-[60%] bg-white border border-slate-200 shadow-sm py-3 px-5 text-center text-[25px]" dir="ltr">
<KatexInline display math="(\{a\}\cdot\{a\})^*\cdot((\{a\}+\{a,b\})^*)^\omega" />
</div>

<div class="absolute left-[19%] top-[340px] w-[60%] bg-white border border-slate-200 shadow-sm py-3 px-5 text-center text-[25px]" dir="ltr">
<KatexInline display math="(\{a\}\cdot\{a\})^*\cdot((\{a\}+\{a,b\})^+)^\omega" />
</div>

<div v-click class="absolute left-[1%] top-[58px] text-red-600 text-[19px] leading-snug text-right w-[170px]">
כל מחובר חייב<br>להסתיים בביטוי<br>בחזקת <KatexInline math="\omega" />
<svg class="absolute -top-8 left-[70px] w-[220px] h-[80px]" viewBox="0 0 220 80" fill="none">
  <path d="M5 55 C55 5, 120 15, 205 52" stroke="#b23816" stroke-width="4" fill="none"/>
  <path d="M190 42 L205 52 L188 57" stroke="#b23816" stroke-width="4" fill="none"/>
</svg>
</div>

<div v-click class="absolute right-[0%] top-[154px] text-red-600 text-[19px] leading-snug text-right w-[190px]">
לביטוי בחזקת <KatexInline math="\omega" /><br>אסור להכיל את<br>המילה הריקה
<svg class="absolute -top-3 right-[165px] w-[230px] h-[80px]" viewBox="0 0 230 80" fill="none">
  <path d="M225 28 C165 0, 78 5, 15 38" stroke="#b23816" stroke-width="4" fill="none"/>
  <path d="M18 22 L15 38 L31 32" stroke="#b23816" stroke-width="4" fill="none"/>
</svg>
</div>

<div v-click class="absolute right-[12%] top-[238px] text-red-600 text-[19px] leading-snug text-right w-[150px]">
גם כאן יש<br>ביטוי שיכול<br>להיות ריק
<svg class="absolute -top-8 right-[120px] w-[170px] h-[80px]" viewBox="0 0 170 80" fill="none">
  <path d="M165 22 C115 42, 65 5, 18 42" stroke="#b23816" stroke-width="4" fill="none"/>
  <path d="M20 25 L18 42 L33 34" stroke="#b23816" stroke-width="4" fill="none"/>
</svg>
</div>

<div v-click class="absolute right-[6%] top-[362px] text-emerald-700 text-[22px] font-bold">
ביטוי חוקי
</div>
</div>

<div class="absolute bottom-7 left-[10%] right-[10%] bg-blue-800 text-yellow-300 text-center text-[18px] py-2" dir="ltr">
https://play.kahoot.it/#/k/15aefb35-8427-4809-807c-7098ee85599f
</div>

---

# מטרות ההרצאה

<div class="grid grid-cols-[1.15fr_0.85fr] gap-6 mt-4 items-center">
<div class="flex flex-col gap-4 text-right">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">להרחיב רגולריות למילים אינסופיות</div>

- ניזכר בשפות רגולריות מעל מילים סופיות.
- נגדיר ביטויי <KatexInline math="\omega" />-רגולריים.
- נתרגם תכונות זמן לינארי לשפות מעל <KatexInline math="2^{AP}" />.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold mb-2">להכיר אוטומטי Büchi</div>

- נגדיר ריצה מקבלת מעל מילה אינסופית.
- נראה דוגמאות לתכונות חַיּוּת.
- נציג את המשפט: <span dir="ltr">NBA</span> מקבלים בדיוק את השפות ה־<KatexInline math="\omega" />-רגולריות.
</div>
</div>

<div class="flex justify-center">
  <img src="/omega_goals_illustration.png" class="rounded-lg shadow-md border border-slate-200 max-h-[380px] w-full object-cover" />
</div>
</div>

---

# למה צריך עוד מודל?

<div class="grid grid-cols-[1.1fr_0.9fr] gap-6 mt-4 items-center">
<div class="text-right text-[22px] leading-relaxed">

בשקפים הקודמים בדקנו:

- <span class="font-bold">שְׁמוּרוֹת</span>: נוסחה על כל מצב נגיש.
- <span class="font-bold">בטיחות רגולרית</span>: אוטומט שמזהה רישות רעות סופיות.

אבל תכונות רבות אינן נחשפות על ידי רישא סופית:

<div class="mt-5 text-center text-[29px]" dir="ltr">
<KatexInline display math="\text{Always }(wait \Rightarrow \text{Eventually }crit)" />
</div>

אי אפשר להפריך “בסוף יקרה” אחרי מספר סופי של צעדים.
</div>

<div class="grid grid-cols-1 gap-4 text-right text-[19px] leading-relaxed">
<div class="bg-white border border-slate-200 rounded p-4">
<div class="font-bold mb-2">שְׁמוּרָה</div>
חיפוש מצב נגיש שמפר נוסחה.
</div>
<div class="bg-white border border-slate-200 rounded p-4">
<div class="font-bold mb-2">בטיחות רגולרית</div>
חיפוש רישא רעה סופית בעזרת אוטומט.
</div>
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2"><KatexInline math="\omega" />־רגולריות</div>
חיפוש דפוס אינסופי: ביקורים חוזרים, מענה לבקשות, והוגנות.
</div>
</div>
</div>

---

# דוגמת מוטיבציה: מניעה הדדית

<div class="mt-4 text-right text-[20px] leading-relaxed">
שאלת החַיּוּת:

<div class="mt-2 text-center text-[18px]" dir="ltr">
<KatexInline display math="\text{Always }(wait_L \Rightarrow \text{Eventually }crit_L)\ \land\ \text{Always }(wait_R \Rightarrow \text{Eventually }crit_R)" />
</div>

<div class="mt-4 text-[19px]">
האימות כבר אינו “האם מגיעים למצב רע”, אלא:
</div>

<div class="grid grid-cols-[1fr_280px] gap-6 mt-4 items-center">
  <div class="text-[19px] leading-relaxed">
    <strong>בקשה ללא מענה:</strong> האם קיימת ריצה אינסופית שבה בקשה נשארת ללא מענה?
  </div>
  <div class="flex justify-center">
    <img src="/unanswered_request_comic.png" class="rounded-lg shadow border border-slate-200 max-h-[130px] object-contain" />
  </div>
</div>

<div class="grid grid-cols-[1fr_280px] gap-6 mt-4 items-center">
  <div class="text-[19px] leading-relaxed">
    <strong>מחזור מפר:</strong> האם במכפלה יש מחזור שמחזיק את ההפרה?
  </div>
  <div class="flex justify-center">
    <img src="/violating_cycle_comic.png" class="rounded-lg shadow border border-slate-200 max-h-[130px] object-contain" />
  </div>
</div>
</div>

---

# המעבר ממילים סופיות לאינסופיות

<div class="grid grid-cols-2 gap-6 mt-3 text-right text-[19px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-3.5 flex flex-col justify-between">
<div>
<div class="font-bold text-slate-700 mb-1">שפה רגולרית</div>
שפה של מילים סופיות:
<div class="mt-1 mb-1 text-center text-[24px]" dir="ltr">
<KatexInline display math="L \subseteq \Sigma^*" />
</div>
מתארת רישות, דוגמאות נגדיות סופיות, או התנהגויות עם סוף.
</div>

<div class="mt-2 pt-2 border-t border-slate-200 text-[15px]">
<div class="font-bold text-slate-600 mb-1">דוגמה:</div>
מילים המכילות אות עם אדום (<KatexInline math="r" />) שלא קדמה לה אות עם צהוב (<KatexInline math="y" />):
<div class="mt-1 text-center text-[19px]" dir="ltr">
<KatexInline display math="(\neg y)^* \cdot r \cdot \text{true}^*" />
</div>
<div class="text-[12px] text-slate-500 mt-0.5 text-right" dir="rtl">
כאשר נוסחה מייצגת את קבוצת האותיות ב־<KatexInline math="\Sigma" /> שמספקות אותה.
</div>
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-3.5 flex flex-col justify-between">
<div>
<div class="font-bold text-blue-700 mb-1">שפה <KatexInline math="\omega" />-רגולרית</div>
שפה של מילים אינסופיות:
<div class="mt-1 mb-1 text-center text-[24px]" dir="ltr">
<KatexInline display math="L \subseteq \Sigma^\omega" />
</div>
מתארת עקבות מלאים של מערכות תגובתיות.
</div>

<div class="mt-2 pt-2 border-t border-blue-200 text-[15px]">
<div class="font-bold text-blue-600 mb-1">דוגמה:</div>
מילים שבהן אות עם ירוק (<KatexInline math="g" />) לא מופיעה אינסוף פעמים (מופיעה מספר סופי של פעמים בלבד):
<div class="mt-1 text-center text-[19px]" dir="ltr">
<KatexInline display math="\text{true}^* \cdot (\neg g)^\omega" />
</div>
<div class="text-[12px] text-blue-500/70 mt-0.5 text-right" dir="rtl">
כאן <KatexInline math="\text{true}" /> מייצג את <KatexInline math="\Sigma" />, ו־<KatexInline math="\neg g" /> מייצג את האותיות ללא <KatexInline math="g" />.
</div>
</div>
</div>
</div>

---

# תזכורת: ביטויים רגולריים

ביטוי רגולרי מעל אלפבית <KatexInline math="\Sigma" /> מוגדר על ידי הסינטקס:
<div class="mt-4 text-center text-[26px]" dir="ltr">
<KatexInline display math="E ::= \emptyset \mid \epsilon \mid a \mid E_1 + E_2 \mid E_1 \cdot E_2 \mid E^*" />
</div>
כאשר <KatexInline math="a \in \Sigma" />.

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-5 text-right text-[18px] leading-relaxed">
<div class="font-bold text-slate-700 mb-4 text-[20px]">הסמנטיקה הפורמלית: השפה <KatexInline math="L(E) \subseteq \Sigma^*" /> מוגדרת באינדוקציה</div>

<div class="grid grid-cols-2 gap-x-12 gap-y-4 text-left pl-8" dir="ltr">
  <div class="flex items-center"><KatexInline math="L(\emptyset) = \emptyset" /></div>
  <div class="flex items-center"><KatexInline math="L(E_1 + E_2) = L(E_1) \cup L(E_2)" /></div>
  <div class="flex items-center"><KatexInline math="L(\epsilon) = \{\epsilon\}" /></div>
  <div class="flex items-center"><KatexInline math="L(E_1 \cdot E_2) = L(E_1) \cdot L(E_2)" /></div>
  <div class="flex items-center gap-1">
    <KatexInline math="L(a) = \{a\}" />
    <span dir="rtl" class="text-right text-[15px] text-slate-500 mr-2">(לכל <KatexInline math="a \in \Sigma" />)</span>
  </div>
  <div class="flex items-center"><KatexInline math="L(E^*) = (L(E))^*" /></div>
</div>
</div>

---

# תרגום אינדוקטיבי של ביטוי רגולרי לשפה

<ParseTreeTranslation :clicks="$clicks" />

<div v-click></div>
<div v-click></div>
<div v-click></div>
<div v-click></div>

---

# ביטויים <KatexInline math="\omega" />-רגולריים <span class="text-sm bg-blue-100 text-blue-800 px-2 py-0.5 rounded mr-2 font-normal align-middle">תחביר</span>

<img src="https://i5.walmartimages.com/seo/Toy-Story-Infinity-Beyond-Quote-Cartoon-Decors-Wall-Sticker-Art-Design-Decal-Girls-Boys-Kids-Room-Bedroom-Nursery-Kindergarten-House-Fun-Home-Decor-S_ab981502-66fc-426b-9fe0-65d7a8ff4bf5.a57b8b9635572853d29ce8bf6890b552.jpeg?odnHeight=2000&odnWidth=2000&odnBg=FFFFFF" class="absolute top-2 left-12 w-56 rounded-lg" />

<div class="text-right text-[20px] leading-relaxed flex flex-col gap-4 mt-6">
<div>
ביטוי <KatexInline math="\omega" />-רגולרי מעל אלפבית <KatexInline math="\Sigma" /> הוא ביטוי מהצורה:
</div>

<div class="text-center text-[30px]" dir="ltr">
<KatexInline display math="G = E_1.F_1^\omega + \cdots + E_n.F_n^\omega" />
</div>

<div class="grid grid-cols-2 gap-4">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-[18px]">
<KatexInline math="E_i" /> ו־<KatexInline math="F_i" /> הם ביטויים רגולריים רגילים מעל <KatexInline math="\Sigma" />, כך ש־<KatexInline math="\epsilon \notin L(F_i)" />.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3 text-[18px]">
דורשים <KatexInline math="\epsilon \notin L(F_i)" /> כדי שכל חזרה תורמת קטע לא ריק, ולכן השרשור אינסופי באמת.
</div>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-[16px]">
<div class="font-bold mb-2 text-right">דוגמאות:</div>
<div class="grid grid-cols-3 gap-4" dir="rtl">
<div class="border border-slate-200 rounded p-2 bg-white text-center">
<div dir="ltr" class="font-bold mb-1"><KatexInline math="A^\omega" /></div>
<div class="text-[14px] text-slate-600">רק מופעים של <KatexInline math="A" /></div>
</div>
<div class="border border-slate-200 rounded p-2 bg-white text-center">
<div dir="ltr" class="font-bold mb-1"><KatexInline math="(A+B)^*.B^\omega" /></div>
<div class="text-[14px] text-slate-600">מספר סופי של <KatexInline math="A" /></div>
</div>
<div class="border border-slate-200 rounded p-2 bg-white text-center">
<div dir="ltr" class="font-bold mb-1"><KatexInline math="(B^*A)^\omega" /></div>
<div class="text-[14px] text-slate-600">אינסוף מופעים של <KatexInline math="A" /></div>
</div>
</div>
</div>
</div>

---

# קבוצת המילים המוגדרת על ידי ביטוי <KatexInline math="\omega" />-רגולרי <span class="text-sm bg-purple-100 text-purple-800 px-2 py-0.5 rounded mr-2 font-normal align-middle">משמעות</span>

<div class="mt-4 text-right text-[21px] leading-relaxed">
אם <KatexInline math="L\subseteq \Sigma^+" />, אז נגדיר:
</div>

<div class="mt-2 text-center text-[28px]" dir="ltr">
<KatexInline display math="L^\omega = \{w_1w_2w_3\cdots \mid \forall i\ge 1\ (w_i\in L)\}" />
</div>

<div class="mt-4 text-right text-[21px] leading-relaxed">
ובאמצעות הגדרה זו נגדיר:
</div>

<div class="mt-2 text-center text-[28px]" dir="ltr">
<KatexInline display math="L_\omega(G)=L(E_1).L(F_1)^\omega \cup \cdots \cup L(E_n).L(F_n)^\omega" />
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[19px]">
שני ביטויים שקולים אם הם מגדירים את אותה שפה של מילים אינסופיות.
</div>

---

# דוגמאות מעל <KatexInline math="\{A,B\}" />

<div class="grid grid-cols-2 gap-4 mt-4 text-right text-[17px] leading-snug">
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<div class="font-bold text-emerald-700 mb-1.5">אינסוף מופעים של <KatexInline math="A" /></div>

<div class="text-center text-[24px]" dir="ltr">
<KatexInline display math="(B^*A)^\omega" />
</div>

<div class="mt-1.5 bg-white/70 border border-emerald-200 rounded p-2 text-[12px] leading-tight">
אם מילה מכילה אינסוף מופעים של <KatexInline math="A" />, חותכים אותה בכל מופע של <KatexInline math="A" />: כל קטע סופי שמתקבל הוא רצף של אפס או יותר <KatexInline math="B" />-ים ואחריהם <KatexInline math="A" />, כלומר מילה מתוך <KatexInline math="B^*A" />. לכן המילה כולה היא שרשור אינסופי של מילים מתוך <KatexInline math="B^*A" />.

להפך, אם מילה שייכת ל־<KatexInline math="(B^*A)^\omega" />, היא מורכבת מאינסוף בלוקים, וכל בלוק מסתיים ב־<KatexInline math="A" />. לכן מופיעים בה אינסוף <KatexInline math="A" />-ים.
</div>
</div>

<div class="bg-orange-50 border border-orange-200 rounded p-3">
<div class="font-bold text-orange-700 mb-1.5">רק מספר סופי של <KatexInline math="A" /></div>

<div class="text-center text-[24px]" dir="ltr">
<KatexInline display math="(A+B)^*.B^\omega" />
</div>

<div class="mt-1.5 bg-white/70 border border-orange-200 rounded p-2 text-[12px] leading-tight">
אם במילה מופיעים רק מספר סופי של <KatexInline math="A" />-ים, נסמן את המקום האחרון שבו מופיע <KatexInline math="A" />. הרישא עד המקום הזה היא מילה סופית כלשהי מעל <KatexInline math="\{A,B\}" />, כלומר מתוך <KatexInline math="(A+B)^*" />. מכאן ואילך מופיעים רק <KatexInline math="B" />-ים, ולכן הזנב הוא מתוך <KatexInline math="B^\omega" />.

להפך, כל מילה מתוך <KatexInline math="(A+B)^*.B^\omega" /> מתחילה ברישא סופית כלשהי, שבה יכולים להופיע רק מספר סופי של <KatexInline math="A" />-ים, ואחריה זנב שמורכב רק מ־<KatexInline math="B" />. לכן במילה כולה יש רק מספר סופי של <KatexInline math="A" />-ים.
</div>
</div>
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[17px]">
קבוצת השפות הניתנות לתיאור באמצעות ביטויי <KatexInline math="\omega" />-רגולריים סגורה תחת איחוד, חיתוך ומשלים.
</div>

---

# תכונות <KatexInline math="\omega" />-רגולריות

<div class="mt-8 text-right text-[23px] leading-relaxed">
תכונת זמן לינארי <KatexInline math="P" /> מעל <KatexInline math="AP" /> היא <span class="font-bold"><KatexInline math="\omega" />-רגולרית</span> אם קיימת שפה <KatexInline math="\omega" />-רגולרית מעל האלפבית <KatexInline math="2^{AP}" /> כך ש:
</div>

<div class="mt-7 text-center text-[31px]" dir="ltr">
<KatexInline display math="P = L_\omega(G)" />
</div>

<div class="mt-7 text-right text-[22px] leading-relaxed">
כל אות במילה האינסופית היא קבוצת התוויות שנכונות במצב הנוכחי.
</div>

<div class="mt-6 text-center text-[23px]" dir="ltr">
<span class="inline-block px-4 py-2 border border-slate-300 rounded bg-white"><KatexInline math="\{\}" /></span>
<span class="mx-2">,</span>
<span class="inline-block px-4 py-2 border border-slate-300 rounded bg-white"><KatexInline math="\{wait\}" /></span>
<span class="mx-2">,</span>
<span class="inline-block px-4 py-2 border border-slate-300 rounded bg-white"><KatexInline math="\{crit\}" /></span>
<span class="mx-2">,</span>
<span class="inline-block px-4 py-2 border border-slate-300 rounded bg-white"><KatexInline math="\{wait,crit\}" /></span>
</div>

---

# שְׁמוּרוֹת ובטיחות רגולרית הן מקרים פרטיים

<div class="grid grid-cols-2 gap-6 mt-6 text-right text-[20px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3">שְׁמוּרָה</div>
אם <KatexInline math="\Phi" /> היא נוסחת מצב, אז כל האותיות שמקיימות אותה יוצרות שפה:

<div class="mt-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="\left(\sum_{A\models\Phi} A\right)^\omega" />
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">בטיחות רגולרית</div>
אם <KatexInline math="\mathit{BadPref}(P)" /> רגולרית, אז ההפרות הן:

<div class="mt-4 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathit{BadPref}(P).(2^{AP})^\omega" />
</div>

ומכאן <KatexInline math="P" /> עצמה <KatexInline math="\omega" />-רגולרית, כי <span class="transition-all duration-300" :class="{ 'text-red-600 font-bold': $clicks >= 1 }">יש סגירות תחת משלים<span v-if="$clicks >= 1"> ⚠️</span></span>.
<div v-click class="hidden"></div>
</div>
</div>

---

# דוגמה: ביקור אינסופי ב־<span dir="ltr">crit</span>

<div class="mt-5 text-right text-[21px] leading-relaxed max-w-2xl mx-auto">
מעל <KatexInline math="AP=\{wait,crit\}" />, התכונה:

<div class="mt-3 text-center text-[28px]" dir="ltr">
<KatexInline display math="\text{Always Eventually }crit" />
</div>

מתוארת על ידי:

<div class="mt-3 text-center text-[27px]" dir="ltr">
<KatexInline display math="((\neg crit)^*.crit)^\omega" />
</div>

<div class="mt-5 text-right text-[18px] bg-slate-50 border border-slate-200 rounded p-3.5 leading-relaxed">
ניתן לפרק את המילה לשרשור של אינסוף מילים באורך סופי שכל אחת מהן מכילה אות המקיימת את <KatexInline math="crit" />.
</div>
</div>

<img src="/crit_decomposition_comic.png" class="absolute bottom-30 left-8 w-40 object-contain pointer-events-none" style="clip-path: inset(20% 0 0 0);" />

---

# אוטומט Büchi <span class="text-sm bg-blue-100 text-blue-800 px-2 py-0.5 rounded mr-2 font-normal align-middle">תחביר</span>

<div class="mt-8 text-right text-[23px] leading-relaxed">
אוטומט Büchi הוא:
</div>

<div class="mt-6 text-center text-[34px]" dir="ltr">
<KatexInline display math="\mathcal{A}=\langle Q,\Sigma,\delta,Q_0,F\rangle" />
</div>

<div class="grid grid-cols-2 gap-6 mt-7 text-right text-[20px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<KatexInline math="Q" /> קבוצה סופית של מצבים, <KatexInline math="\Sigma" /> אלפבית, ו־<KatexInline math="\delta:Q\times\Sigma\to 2^Q" /> יחס המעברים.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<KatexInline math="Q_0\subseteq Q" /> מצבים התחלתיים, ו־<KatexInline math="F\subseteq Q" /> מצבים מקבלים.
</div>
</div>

---

# אוטומט Büchi <span class="text-sm bg-purple-100 text-purple-800 px-2 py-0.5 rounded mr-2 font-normal align-middle">משמעות</span>

<div class="mt-7 text-right text-[22px] leading-relaxed">
עבור מילה אינסופית <KatexInline math="\sigma" />, ריצה היא סדרת מצבים <span dir="ltr"><KatexInline math="q_0q_1q_2\cdots" /></span>
כך ש־<KatexInline math="q_0\in Q_0" /> ו־<KatexInline math="q_{i+1}\in\delta(q_i,\sigma[i])" /> לכל <KatexInline math="i" />.
שימו לב שמדובר בריצה באורך אינסופי.
</div> 

<div class="mt-7 bg-emerald-50 border border-emerald-200 rounded p-5 text-right text-[23px] leading-relaxed">
הריצה <span class="font-bold">מקבלת</span> אם היא מבקרת במצבי <KatexInline math="F" /> אינסוף פעמים:
<span dir="ltr"><KatexInline math="\underset{\infty}{\exists} i\ \left(q_i\in F\right)" /></span>.
</div>

<div class="mt-5 bg-purple-50 border border-purple-200 rounded p-5 text-right text-[22px] leading-relaxed">
השפה של האוטומט היא קבוצת כל המילים שיש להן ריצה מקבלת:

$$L_\omega(\mathcal{A})=\{\sigma\in\Sigma^\omega\mid \mathcal{A}\ \text{has an accepting run on }\sigma\}$$
</div>

---

# דוגמה: אינסוף פעמים ירוק

<div class="grid grid-cols-[0.75fr_1.25fr] gap-6 mt-5 items-center">
<div class="text-right text-[18px] leading-relaxed">
התכונה <span dir="ltr"><KatexInline math="\text{Always Eventually }green" /></span> מתקבלת על ידי אוטומט שמסמן קבלה בכל פעם שהאות הנוכחית מכילה <KatexInline math="green" />.

<div class="mt-5 bg-red-50 border border-red-200 rounded p-4">
אם מפסיקים לראות <span dir="ltr">green</span>, הריצה נשארת לנצח מחוץ ל־<KatexInline math="F" /> ולכן אינה מקבלת.
</div>

<div class="mt-4 bg-emerald-50 border border-emerald-200 rounded p-4">
אם רואים <span dir="ltr">green</span> אינסוף פעמים, האוטומט מבקר ב־<KatexInline math="q_1" /> אינסוף פעמים. מכיוון ש־<KatexInline math="q_1\in F" />, המילה מתקבלת.
</div>
</div>

<div>
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="520" :height="250" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'q0', x: 150, y: 125, label: '$q_0$', initial: true, initialDirection: 'top', r: 25, labelWidth: 70 },
    { id: 'q1', x: 365, y: 125, label: '$q_1$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$\\neg green$', loopDirection: '180deg', labelX: -42, labelWidth: 90 },
    { source: 'q0', target: 'q1', label: '$green$', labelY: -12, labelWidth: 70, curve: -0.2 },
    { source: 'q1', target: 'q0', label: '$\\neg green$', labelY: 18, labelWidth: 90, curve: -0.2 },
    { source: 'q1', target: 'q1', label: '$green$', loopDirection: '0deg', labelX: 42, labelWidth: 70 }
  ]"
/>
</div>

<div class="mt-4 bg-cyan-50 border border-cyan-200 rounded p-4" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=\{\sigma\in\Sigma^\omega\mid \underset{\infty}{\exists} i\ \left(green\in\sigma[i]\right)\}" />
</div>
</div>
</div>

---

# דוגמה: בקשה מקבלת מענה

<div class="text-right text-[23px] leading-relaxed mt-5">
התכונה:
</div>

<div class="text-center text-[20px] mt-3" dir="ltr">
<KatexInline display math="\text{Always }(req \Rightarrow \text{Eventually }resp)" />
</div>

<div class="grid grid-cols-[0.85fr_1.15fr] gap-6 mt-4 items-center">
<div class="text-right text-[21px] leading-relaxed">
מצב <KatexInline math="q_0" /> אומר שאין כרגע בקשה פתוחה.
מצב <KatexInline math="q_1" /> אומר שאנחנו מחכים ל־<span dir="ltr">resp</span>.

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-4">
מצב הקבלה הוא <KatexInline math="q_0" />: כדי לקבל, צריך לחזור אליו אינסוף פעמים.
</div>
</div>

<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="540" :height="250" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="13"
  :states="[
    { id: 'q0', x: 170, y: 125, label: '$q_0$', initial: true, initialDirection: 'top', accepting: true, r: 25, labelWidth: 70 },
    { id: 'q1', x: 390, y: 125, label: '$q_1$', r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$\\neg req \\vee resp$', loopDirection: '180deg', labelX: -45, labelWidth: 125 },
    { source: 'q0', target: 'q1', label: '$req \\wedge \\neg resp$', labelY: -12, labelWidth: 135, curve: -0.2 },
    { source: 'q1', target: 'q0', label: '$resp$', labelY: 18, labelWidth: 65, curve: -0.2 },
    { source: 'q1', target: 'q1', label: '$\\neg resp$', loopDirection: '0deg', labelX: 25, labelWidth: 85 }
  ]"
/>
</div>
</div>

---

# בטיחות רגולרית כאוטומט Büchi

<div class="mt-5 text-right text-[21px] leading-snug">
אם יש לנו <span dir="ltr">DFA</span> שלם לרישות הרעות עם מצבי מלכודת מקבלים, אפשר לקרוא אותו גם כאוטומט Büchi.
</div>

<div class="grid grid-cols-2 gap-5 mt-5 text-right text-[18px] leading-snug">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">הֲפָרוֹת</div>
כאוטומט Büchi, האוטומט שמקבל את מצבי המלכודת מקבל בדיוק ריצות שבהן הופיעה רישא רעה: אחרי שנכנסים למלכודת מקבלת, נשארים בה ולכן מבקרים במצב מקבל אינסוף פעמים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">התכונה עצמה</div>
באוטומט דטרמיניסטי שלם, החלפת קבוצת הקבלה ל־<KatexInline math="Q\setminus F" /> מקבלת את העקבות התקינים: אם אין רישא רעה, הריצה לעולם לא נכנסת למלכודת ולכן נשארת במצבים שמחוץ ל־<KatexInline math="F" /> אינסוף פעמים. אם יש רישא רעה, נכנסים למלכודת שב־<KatexInline math="F" /> ונשארים בה, ולכן לא מבקרים ב־<KatexInline math="Q\setminus F" /> אינסוף פעמים.
</div>
</div>

<div class="mt-5 bg-slate-50 border border-slate-200 rounded p-4 text-right text-[18px] leading-snug">
זו הסיבה ש־<KatexInline math="\omega" />־רגולריות באמת מרחיבה את בטיחות רגולרית, ולא מחליפה אותה.
</div>

---

# זהירות: שקילות סופית ושקילות אינסופית אינן שקולות

<div class="grid grid-cols-2 gap-4 mt-4 text-right text-[20px] leading-snug">
<div class="bg-white border border-slate-200 rounded p-4">
<div class="font-bold mb-2"><span dir="ltr">NFA</span> מול <span dir="ltr">NBA</span></div>
שני אוטומטים יכולים לקבל אותה שפה סופית, אבל כשקוראים אותם מעל מילים אינסופיות הם יכולים לקבל שפות שונות.
וגם להפך: הם יכולים לקבל אותה שפה אינסופית, אבל שפות סופיות שונות.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">הָאִינְטוּאִיצְיָה</div>
באוטומט סופי מספיק להגיע פעם אחת למצב מקבל.
באוטומט Büchi צריך לחזור למצבי קבלה אינסוף פעמים.
</div>
</div>

<div class="mt-4 flex flex-col gap-0 text-center text-[25px]" dir="ltr">
<KatexInline display math="L(\mathcal{A}_1)=L(\mathcal{A}_2)\ \not\Rightarrow\ L_\omega(\mathcal{A}_1)=L_\omega(\mathcal{A}_2)" />
<KatexInline display math="L_\omega(\mathcal{A}_1)=L_\omega(\mathcal{A}_2)\ \not\Rightarrow\ L(\mathcal{A}_1)=L(\mathcal{A}_2)" />
</div>

---

# <span dir="ltr">NFA</span> מול <span dir="ltr">NBA</span>: שקילות סופית אינה שקילות <KatexInline math="\omega" />

<div class="grid grid-cols-[0.95fr_1.05fr] gap-4 mt-3 items-center">
<div class="text-right text-[18px] leading-snug">
כאוטומטים סופיים, שני האוטומטים מקבלים את אותה שפה:

<div class="mt-2 bg-purple-50 border border-purple-200 rounded p-2 text-center" dir="ltr">
<KatexInline display math="L(\mathcal{A}_1)=L(\mathcal{A}_2)=\{A\}^+" />
</div>

<div class="mt-2 bg-red-50 border border-red-200 rounded p-3">
אבל כאוטומטי Büchi הם אינם שקולים.
ב־<KatexInline math="\mathcal{A}_1" /> הריצה מגיעה למצב המקבל ונשארת בו.
ב־<KatexInline math="\mathcal{A}_2" /> אין ריצה אינסופית שמבקרת במצב המקבל אינסוף פעמים.
</div>

<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-center" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A}_1)=\{A^\omega\}\qquad L_\omega(\mathcal{A}_2)=\emptyset" />
</div>
</div>

<div class="space-y-2">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<div class="px-4 pt-1 font-bold text-blue-700" dir="ltr"><KatexInline math="\mathcal{A}_1" /></div>
<AutomatonD3 variant="classic" :width="500" :height="145" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'a1q0', x: 150, y: 78, label: '$q_0$', initial: true, initialDirection: 'left', r: 25, labelWidth: 70 },
    { id: 'a1q1', x: 355, y: 78, label: '$q_1$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'a1q0', target: 'a1q1', label: '$A$', labelY: -12, labelWidth: 50 },
    { source: 'a1q1', target: 'a1q1', label: '$A$', loopDirection: '0deg', labelX: 12, labelWidth: 50 }
  ]"
/>
</div>

<div class="bg-white rounded border border-slate-200 shadow-sm">
<div class="px-4 pt-1 font-bold text-red-700" dir="ltr"><KatexInline math="\mathcal{A}_2" /></div>
<AutomatonD3 variant="classic" :width="500" :height="145" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'a2q0', x: 150, y: 78, label: '$q_0$', initial: true, initialDirection: 'top', r: 25, labelWidth: 70 },
    { id: 'a2q1', x: 355, y: 78, label: '$q_1$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'a2q0', target: 'a2q0', label: '$A$', loopDirection: '180deg', labelX: -12, labelWidth: 50 },
    { source: 'a2q0', target: 'a2q1', label: '$A$', labelY: -12, labelWidth: 30 }
  ]"
/>
</div>
</div>
</div>

---

# <span dir="ltr">DFA</span> מול <span dir="ltr">DBA</span>: שקילות <KatexInline math="\omega" /> אינה שקילות סופית

<div class="grid grid-cols-[0.95fr_1.05fr] gap-4 mt-3 items-center">
<div class="text-right text-[18px] leading-snug">
כאן האוטומטים אינם שקולים כשקוראים מילים סופיות:

<div class="mt-2 flex flex-col gap-1.5 text-center text-[15px]" dir="ltr">
<div class="bg-blue-50 border border-blue-200 rounded px-2 py-1.5">
<KatexInline display math="L(\mathcal{A}_1)=\{A^{2k+1}\mid k\ge 0\}" />
</div>
<div class="bg-orange-50 border border-orange-200 rounded px-2 py-1.5">
<KatexInline display math="L(\mathcal{A}_2)=\{A^{2k}\mid k\ge 0\}" />
</div>
</div>

<div class="mt-2 bg-emerald-50 border border-emerald-200 rounded p-3">
אבל על המילה האינסופית היחידה מעל האלפבית הזה, הריצה בשני האוטומטים מבקרת במצב מקבל אינסוף פעמים.
</div>

<div class="mt-2 bg-purple-50 border border-purple-200 rounded p-2 text-center" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A}_1)=L_\omega(\mathcal{A}_2)=\{A^\omega\}" />
</div>
</div>

<div class="space-y-2">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<div class="px-4 pt-1 font-bold text-blue-700" dir="ltr"><KatexInline math="\mathcal{A}_1" /></div>
<AutomatonD3 variant="classic" :width="500" :height="160" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'd1q0', x: 150, y: 78, label: '$q_0$', initial: true, initialDirection: 'left', r: 25, labelWidth: 70 },
    { id: 'd1q1', x: 355, y: 78, label: '$q_1$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'd1q0', target: 'd1q1', label: '$A$', labelY: -12, labelWidth: 50, curve: -0.25 },
    { source: 'd1q1', target: 'd1q0', label: '$A$', labelY: 15, labelWidth: 50, curve: -0.25 }
  ]"
/>
</div>

<div class="bg-white rounded border border-slate-200 shadow-sm">
<div class="px-4 pt-1 font-bold text-red-700" dir="ltr"><KatexInline math="\mathcal{A}_2" /></div>
<AutomatonD3 variant="classic" :width="500" :height="160" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'd2q0', x: 150, y: 78, label: '$q_0$', initial: true, initialDirection: 'left', accepting: true, r: 25, labelWidth: 70 },
    { id: 'd2q1', x: 355, y: 78, label: '$q_1$', r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'd2q0', target: 'd2q1', label: '$A$', labelY: -10, labelWidth: 50, curve: -0.25 },
    { source: 'd2q1', target: 'd2q0', label: '$A$', labelY: 15, labelWidth: 50, curve: -0.25 }
  ]"
/>
</div>
</div>
</div>

---

# המשפט המרכזי

<div class="mt-10 text-center text-[34px] leading-relaxed">
השפות שמתקבלות על ידי אוטומטי Büchi לא דטרמיניסטיים הן בדיוק השפות ה־<KatexInline math="\omega" />-רגולריות.
</div>

<div class="grid grid-cols-2 gap-6 mt-10 text-right text-[21px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3">מאוטומט לביטוי</div>
מפרקים ריצה מקבלת לרישא סופית ועוד לולאות שחוזרות שוב ושוב דרך מצב מקבל.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">מביטוי לאוטומט</div>
בונים אוטומטים עבור איחוד, עבור <KatexInline math="L^\omega" />, ועבור שרשור של שפה סופית עם שפת Büchi.
</div>
</div>

---

# מאוטומט לביטוי <KatexInline math="\omega" />-רגולרי: מתכון

<div class="mt-2 text-right text-[18px] leading-tight">
נשתמש בכלי מהקורס <span class="font-bold">מודלים חישוביים</span>:
בונים אוטומט סופי רגיל ומפיקים ממנו ביטוי רגולרי רגיל.
</div>

<div class="grid grid-cols-2 gap-2 mt-3 text-right text-[16px] leading-tight">
<div class="bg-blue-50 border border-blue-200 rounded p-2.5">
<div class="font-bold text-blue-700 mb-1">1. רישא עד מצב מקבל</div>
לכל <KatexInline math="q_0\in Q_0" /> ולכל <KatexInline math="q\in F" /> בונים אוטומט סופי:
אותם מצבים ומעברים, מצב התחלתי <KatexInline math="q_0" />, וקבוצת קבלה <KatexInline math="\{q\}" />.
מהאוטומט הזה מפיקים ביטוי רגולרי <KatexInline math="E_{q_0,q}" />.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-2.5">
<div class="font-bold text-emerald-700 mb-1">2. לולאה לא ריקה דרך אותו מצב</div>
לכל <KatexInline math="q\in F" /> בונים אוטומט סופי חדש: מוסיפים מצב התחלה חדש <KatexInline math="s" />,
ומ־<KatexInline math="s" /> יוצאים בדיוק כמו שיוצאים מ־<KatexInline math="q" /> באות הראשונה.
מצב הקבלה היחיד הוא <KatexInline math="q" />.
כך מתקבלות בדיוק המילים הלא ריקות שמובילות מ־<KatexInline math="q" /> חזרה ל־<KatexInline math="q" />.
מהאוטומט הזה מפיקים ביטוי רגולרי רגיל <KatexInline math="G_q" />.
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-2.5">
<div class="font-bold text-purple-700 mb-1">3. הופכים ללולאה אינסופית</div>
הביטוי <KatexInline math="G_q^\omega" /> אומר: חזרה אינסופית על מקטעים לא ריקים, שכל אחד מהם מתחיל ב־<KatexInline math="q" /> ומחזיר ל־<KatexInline math="q" />.
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-2.5">
<div class="font-bold text-slate-700 mb-1">4. מחברים את כל האפשרויות</div>
מצב ההתחלה ומצב הקבלה שחוזרים אליו אינם ידועים מראש, לכן כותבים סכום של כל המחוברים.
</div>
</div>

<div class="mt-3 text-center text-[24px]" dir="ltr">
<KatexInline display math="R_{\mathcal{A}}=\sum_{q_0\in Q_0,\ q\in F} E_{q_0,q}\cdot G_q^\omega" />
</div>

<div class="mt-1 text-center text-[20px]" dir="ltr">
<KatexInline display math="L_\omega(R_{\mathcal{A}})=L_\omega(\mathcal{A})" />
</div>

---

# מאוטומט לביטוי: למה המתכון נכון

<div class="grid grid-cols-2 gap-5 mt-6 text-right text-[19px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">מריצה מקבלת לביטוי</div>
אם מילה מתקבלת, יש ריצה שבה מצב מקבל <KatexInline math="q\in F" /> מופיע אינסוף פעמים.
נבחר את הביקור הראשון ב־<KatexInline math="q" />: הרישא עד אליו שייכת ל־<KatexInline math="E_{q_0,q}" />.
בין כל שני ביקורים עוקבים ב־<KatexInline math="q" /> מתקבל מקטע לא ריק ששייך ל־<KatexInline math="G_q" />.
לכן המילה שייכת ל־<KatexInline math="E_{q_0,q}\cdot G_q^\omega" />.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">מהביטוי לריצה מקבלת</div>
אם מילה שייכת ל־<KatexInline math="E_{q_0,q}\cdot G_q^\omega" />, אז יש רישא שמובילה מ־<KatexInline math="q_0" /> ל־<KatexInline math="q" />,
ואחריה אינסוף מקטעים לא ריקים שכל אחד מוביל מ־<KatexInline math="q" /> חזרה ל־<KatexInline math="q" />.
מדביקים את המסלולים האלה ומקבלים ריצה שמבקרת ב־<KatexInline math="q" /> אינסוף פעמים.
מכיוון ש־<KatexInline math="q\in F" />, הריצה מקבלת.
</div>
</div>

<div class="mt-5 bg-white border border-slate-200 rounded p-4 text-center text-[24px]" dir="ltr">
<KatexInline display math="\text{NBA}\ \Longrightarrow\ R_{\mathcal{A}}=\sum E\cdot G^\omega" />
</div>

---

# דוגמה: מצב מקבל שחוזרים אליו

<div class="grid grid-cols-[0.9fr_1.1fr] gap-5 mt-5 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="470" :height="230" :arrowSize="3.2" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'q1', x: 95, y: 115, label: '$q_1$', initial: true, initialDirection: 'top', r: 25, labelWidth: 70 },
    { id: 'q2', x: 235, y: 115, label: '$q_2$', r: 25, labelWidth: 70 },
    { id: 'q3', x: 375, y: 115, label: '$q_3$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'q1', target: 'q1', label: '$C$', loopDirection: '180deg', labelX: -20, labelWidth: 45, stroke: $clicks === 1 ? '#2563eb' : $clicks === 2 ? '#16a34a' : undefined, strokeWidth: $clicks === 1 || $clicks === 2 ? 3.4 : undefined, labelColor: $clicks === 1 ? '#2563eb' : $clicks === 2 ? '#16a34a' : undefined },
    { source: 'q1', target: 'q2', label: '$A$', labelY: -10, labelWidth: 45, stroke: $clicks === 1 ? '#2563eb' : $clicks === 2 ? '#16a34a' : undefined, strokeWidth: $clicks === 1 || $clicks === 2 ? 3.4 : undefined, labelColor: $clicks === 1 ? '#2563eb' : $clicks === 2 ? '#16a34a' : undefined },
    { source: 'q2', target: 'q3', label: '$B$', labelY: -10, labelWidth: 45, stroke: $clicks === 1 ? '#2563eb' : $clicks === 2 ? '#16a34a' : undefined, strokeWidth: $clicks === 1 || $clicks === 2 ? 3.4 : undefined, labelColor: $clicks === 1 ? '#2563eb' : $clicks === 2 ? '#16a34a' : undefined },
    { source: 'q3', target: 'q3', label: '$B$', loopDirection: '0deg', labelX: 20, labelWidth: 45, stroke: $clicks === 2 ? '#d97706' : undefined, strokeWidth: $clicks === 2 ? 3.4 : undefined, labelColor: $clicks === 2 ? '#d97706' : undefined },
    { source: 'q3', target: 'q1', label: '$B$', labelY: 18, labelWidth: 45, curve: -0.2, stroke: $clicks === 2 ? '#16a34a' : undefined, strokeWidth: $clicks === 2 ? 3.4 : undefined, labelColor: $clicks === 2 ? '#16a34a' : undefined }
  ]"
/>
</div>

<div class="text-right text-[20px] leading-snug space-y-1.5">
<div v-click class="bg-blue-50 border border-blue-200 rounded p-2.5">
הרישא שמגיעה ל־<KatexInline math="q_3" />:

<div class="mt-1 text-center text-[25px]" dir="ltr">
<KatexInline display math="\textcolor{blue}{C^*AB}" />
</div>
</div>

<div v-click class="bg-emerald-50 border border-emerald-200 rounded p-2.5">
הלולאות שחוזרות מ־<KatexInline math="q_3" /> אל <KatexInline math="q_3" />:

<div class="mt-1 text-center text-[25px]" dir="ltr">
<KatexInline display math="\textcolor{orange}{B} + \textcolor{green}{BC^*AB}" />
</div>
</div>

<div v-click class="bg-purple-50 border border-purple-200 rounded p-2.5">
ולכן הביטוי ה-<KatexInline math="\omega" />-רגולרי הוא:

<div class="mt-1 text-center text-[25px]" dir="ltr">
<KatexInline display math="\textcolor{blue}{C^*AB}\cdot(\textcolor{orange}{B}+\textcolor{green}{BC^*AB})^\omega" />
</div>
</div>
</div>
</div>

---

# מביטוי לאוטומט: שלושת אבני הבניין

<div class="grid grid-cols-3 gap-5 mt-8 text-right text-[19px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-3">1. איחוד</div>
אם יש אוטומטים ל־<KatexInline math="L_1" /> ול־<KatexInline math="L_2" />, שמים אותם זה לצד זה ומאחדים מצבים התחלתיים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">2. אופרטור <KatexInline math="\omega" /></div>
אם <KatexInline math="L" /> רגולרית ו־<KatexInline math="\epsilon\notin L" />, בונים <span dir="ltr">NBA</span> שמקבל <KatexInline math="L^\omega" />.
</div>

<div class="bg-orange-50 border border-orange-200 rounded p-5">
<div class="font-bold text-orange-700 mb-3">3. שרשור</div>
אם <KatexInline math="L" /> רגולרית ו־<KatexInline math="\mathcal{A}" /> מקבל שפת Büchi, בונים אוטומט עבור <KatexInline math="L.L_\omega(\mathcal{A})" />.
</div>
</div>

<div class="mt-8 text-center text-[29px]" dir="ltr">
<KatexInline display math="E_1.F_1^\omega+\cdots+E_n.F_n^\omega" />
</div>

---

# אופרטור <KatexInline math="\omega" /> עבור <span dir="ltr">NFA</span>

<div class="grid grid-cols-[0.95fr_1.05fr] gap-6 mt-5 items-center">
<div class="text-right text-[21px] leading-relaxed">
נתון <span dir="ltr">NFA</span> עבור <KatexInline math="L" /> ללא <KatexInline math="\epsilon" />.

כדי לקבל <KatexInline math="L^\omega" />:

- שומרים את כל המעברים.
- כל מעבר שמגיע למצב מקבל מקבל גם עותקים אל מצבי ההתחלה.
- מצבי ההתחלה הופכים למצבים המקבלים של ה־<span dir="ltr">NBA</span>.
</div>

<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="560" :height="250" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 's', x: 115, y: 125, label: '$s$', initial: true, initialDirection: 'right', accepting: true, r: 25, labelWidth: 70 },
    { id: 'p', x: 285, y: 125, label: '$p$', r: 25, labelWidth: 70 },
    { id: 'f', x: 455, y: 125, label: '$f$', r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 's', target: 'p', label: '$u$', labelY: -10, labelWidth: 45 },
    { source: 'p', target: 'f', label: '$v$', labelY: -10, labelWidth: 45 },
    { source: 'p', target: 's', label: '$v$', labelY: 38, labelWidth: 45 }
  ]"
/>
</div>
</div>

---

# שרשור <span dir="ltr">NFA</span> ו־<span dir="ltr">NBA</span>

<div class="grid grid-cols-[1.05fr_0.95fr] gap-6 mt-5 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="560" :height="250" :arrowSize="4.5" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'n0', x: 95, y: 125, label: '$n_0$', initial: true, initialDirection: 'right', r: 24, labelWidth: 70 },
    { id: 'nf', x: 235, y: 125, label: '$n_f$', r: 24, labelWidth: 70 },
    { id: 'b0', x: 370, y: 125, label: '$b_0$', r: 24, labelWidth: 70 },
    { id: 'bf', x: 500, y: 125, label: '$b_f$', accepting: true, r: 24, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'n0', target: 'nf', label: '$u$', labelY: -10, labelWidth: 45 },
    { source: 'n0', target: 'b0', label: '$u$', labelY: 42, labelWidth: 45 },
    { source: 'b0', target: 'bf', label: '$a$', labelY: -10, labelWidth: 45 },
    { source: 'bf', target: 'bf', label: '$b$', loopDirection: '0deg', labelX: 32, labelWidth: 45 },
    { source: 'bf', target: 'b0', label: '$c$', labelY: 36, labelWidth: 45 }
  ]"
/>
</div>

<div class="text-right text-[21px] leading-relaxed">
עבור <span dir="ltr">NFA</span> שמקבל <KatexInline math="L" /> ו־<span dir="ltr">NBA</span> שמקבל <KatexInline math="M" />:

<div class="mt-4 text-center text-[28px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A}) = L.L_\omega(\mathcal{A}_2)" />
</div>

מוסיפים מעברים מכל מעבר שנכנס למצב מקבל ב־<span dir="ltr">NFA</span> אל מצבי ההתחלה של ה־<span dir="ltr">NBA</span>.
הקבלה נקבעת רק לפי ה־<span dir="ltr">NBA</span>.
</div>
</div>

---

# מה קיבלנו?

<div class="mt-8 text-right text-[23px] leading-relaxed">
לכל ביטוי <KatexInline math="\omega" />-רגולרי:
</div>

<div class="mt-5 text-center text-[31px]" dir="ltr">
<KatexInline display math="G=E_1.F_1^\omega+\cdots+E_n.F_n^\omega" />
</div>

<div class="mt-7 text-right text-[23px] leading-relaxed">
אפשר לבנות באופן קונסטרוקטיבי <span dir="ltr">NBA</span> כך ש:
</div>

<div class="mt-5 text-center text-[32px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=L_\omega(G)" />
</div>

<div class="mt-8 bg-blue-50 border border-blue-200 rounded p-5 text-right text-[22px] leading-relaxed">
בשיעור הבא משתמשים בזה לבדיקת מודלים: מכפלה של מערכת המעברים עם האוטומט, ואז חיפוש מחזור מקבל.
</div>

---

# סיכום

<div class="grid grid-cols-2 gap-6 mt-8 text-right text-[21px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-3">שפות <KatexInline math="\omega" />-רגולריות</div>

- מתארות עקבות אינסופיים.
- נכתבות כביטויים <KatexInline math="E.F^\omega" /> ואיחודים שלהם.
- כוללות שְׁמוּרוֹת ובטיחות רגולרית.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-3">אוטומטי Büchi</div>

- מקבלים ריצה אם היא מבקרת ב־<KatexInline math="F" /> אינסוף פעמים.
- מבטאים תכונות חַיּוּת כמו <span dir="ltr"><KatexInline math="\text{Always Eventually }p" /></span> ו־<span dir="ltr"><KatexInline math="\text{Always }(req \Rightarrow \text{Eventually }resp)" /></span>.
- שקולים בכוחם לביטויי <KatexInline math="\omega" />-רגולריים.
</div>
</div>
