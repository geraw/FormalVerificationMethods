---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 20-practice-problems
htmlAttrs:
  dir: rtl
  lang: he
drawings:
  enabled: true
info: |
  ## שאלות תרגול
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# שאלות תרגול

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# שאלה: אלגוריתם לטיפול בהוֹגְנוּת על ידי הרחבת המערכת (20 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
נתונים: מערכת מעברים <KatexInline math="TS=\langle S,Act,\to,I,AP,L\rangle" />, נוסחת LTL <KatexInline math="\varphi" /> מעל <KatexInline math="AP" />, והנחת הוֹגְנוּת <span dir="ltr"><KatexInline math="\mathcal{F}=\langle\mathcal{F}_{uncond},\mathcal{F}_{strong},\mathcal{F}_{weak}\rangle" /></span>.
</div>

<div class="mt-6 bg-blue-50 border border-blue-200 rounded p-4 text-[20px] leading-relaxed">
<span class="font-bold">המשימה:</span> הציעו אלגוריתם הבונה מערכת מעברים <span dir="ltr"><KatexInline math="TS'" /></span> ונוסחת LTL <span dir="ltr"><KatexInline math="\varphi'" /></span> (ללא כל אזכור של הוֹגְנוּת) כך ש:
</div>

<div class="mt-5 text-center text-[28px]" dir="ltr">
<KatexInline display math="TS'\models\varphi' \iff TS\models_{\mathcal{F}}\varphi" />
</div>

<div class="text-right text-[16px] leading-relaxed mt-5 text-gray-600">
סימון: <KatexInline math="\Gamma=\mathcal{F}_{uncond}\cup\mathcal{F}_{strong}\cup\mathcal{F}_{weak}\subseteq 2^{Act}" />, אוסף קבוצות הפעולות שמוזכרות ב-<KatexInline math="\mathcal{F}" /> (סופי).
</div>

---

# הסעיפים

<div class="space-y-3 text-right text-[18px] leading-relaxed mt-3">

<div class="bg-slate-50 border border-slate-200 rounded p-3">
<span class="font-bold">א'. (5 נק')</span>
תארו בנייה כללית של <KatexInline math="TS'" /> מתוך <KatexInline math="TS" /> ו-<KatexInline math="\mathcal{F}" /> (מצבים, <KatexInline math="AP'" />, תיוג, מצבי התחלה, יחס מעברים), כך שלכל <KatexInline math="A\in\Gamma" /> יהיו ב-<KatexInline math="AP'" /> תוויות <KatexInline math="en_A" /> ו-<KatexInline math="tk_A" /> המבטאות נכונה "<KatexInline math="A" /> מאופשרת" ו"<KatexInline math="A" /> נבחרה".
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3">
<span class="font-bold">ב'. (5 נק')</span>
כתבו את <KatexInline math="\theta_{\mathcal{F}}" /> מעל <KatexInline math="AP'" /> (קוניונקציה לפי שלושת מרכיבי <KatexInline math="\mathcal{F}" />), הגדירו <KatexInline math="\varphi'=\theta_{\mathcal{F}}\Rightarrow\varphi" />, ונמקו בקצרה מדוע <span dir="ltr"><KatexInline math="TS'\models\varphi'\iff TS\models_{\mathcal{F}}\varphi" /></span>.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<span class="font-bold">ג'. (5 נק')</span>
<div class="grid grid-cols-[1fr_auto] gap-2 items-center mt-1">
<div class="text-right text-[14px] leading-snug">
הפעילו את הבנייה על הדוגמה (התרשים), עם <KatexInline math="AP=\{p\},\ L(s_1)=\{p\}" /> (אחרת <KatexInline math="\emptyset" />), <KatexInline math="\varphi=\Box\Diamond p" />, <span dir="ltr"><KatexInline math="\mathcal{F}=\langle\emptyset,\{\{\gamma\}\},\emptyset\rangle" /></span>. רשמו את <KatexInline math="TS'" /> ואת <KatexInline math="\varphi'" />.
</div>
<div class="flex justify-center -mt-8">
<TransitionSystemD3
  :width="380" :height="100" :auto="false"
  :states="[
    { id: 's0', text: 's0', x: 70, y: 55, initial: true, initialDirection: 'top', width: 56, label: '$\\{\\}$', labelX: 20, labelY: 14 },
    { id: 's1', text: 's1', label: '$\\{p\\}$', labelX: 20, labelY: 14, x: 195, y: 55, width: 56 },
    { id: 's2', text: 's2', x: 335, y: 55, width: 56, label: '$\\{\\}$', labelX: 20, labelY: 14, }
  ]"
  :transitions="[
    { source: 's0', target: 's0', action: '$\\alpha$', loopDirection: '180deg', loopRadius: 82, actionX: 5 },
    { source: 's0', target: 's1', actionY: -12, action: '$\\gamma$' },
    { source: 's1', target: 's2', actionY: 12, action: '$\\beta$' },
    { source: 's2', target: 's1', actionY: -12, action: '$\\delta$' }
  ]"
/>
</div>
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-3">
<span class="font-bold">ד'. (5 נק')</span>
הראו שהחלק הנגיש של <KatexInline math="TS'" /> שקול ל-<KatexInline math="TS" /> המקורית (במובן שהגדרנו: מקיים את אותן תכונות זמן ליניארי), והסיקו אם <span dir="ltr"><KatexInline math="TS'\models\varphi'" /></span>.
</div>

</div>

---

# פתרון א': בניית <span dir="ltr">TS'</span>

<div class="text-right text-[17px] leading-relaxed mt-2">
מוסיפים לכל מצב סיבית-זיכרון אחת לכל <KatexInline math="A\in\Gamma" />, המתעדת אם הפעולה האחרונה שננקטה הייתה ב-<KatexInline math="A" />:
</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-[16px]" dir="ltr">
<div class="bg-slate-50 border border-slate-200 rounded p-3"><KatexInline display math="S'=S\times\{0,1\}^{\Gamma}" /></div>
<div class="bg-slate-50 border border-slate-200 rounded p-3">
<KatexInline display math="AP'=AP\uplus\{en_A,tk_A\mid A\in\Gamma\}" />
<div dir="rtl" class="text-right text-[13px] mt-1">בהנחה שהפסוקים האטומיים האלה אינם מופיעים כבר ב-<KatexInline math="AP" />.</div>
</div>
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[16px]" dir="ltr">
<KatexInline display math="L'(\langle s,b\rangle)=L(s)\cup\{en_A\mid Post(s,A)\neq\emptyset\}\cup\{tk_A\mid b(A)=1\}" />
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[16px]" dir="ltr">
<KatexInline display math="\langle s,b\rangle\xrightarrow{\alpha}{}'\langle t,b'\rangle \iff s\xrightarrow{\alpha}t \ \land\ \forall A\in\Gamma\ \left(b'(A)=[\alpha\in A]\right)" />
</div>

<div class="mt-3 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] leading-relaxed">
<div class="text-center" dir="ltr"><KatexInline math="I'=\{\langle s_0,\vec{0}\rangle\mid s_0\in I\}" /></div>
<div class="text-center mt-1">הבחירה ההתחלתית של <KatexInline math="b" /> שרירותית, היא במילא לא משפיעה על <span dir="ltr"><KatexInline math="\Box\Diamond" />/<KatexInline math="\Diamond\Box" /></span>.</div>
</div>

---

# פתרון ב': <span dir="ltr"><KatexInline math="\theta_{\mathcal{F}},\varphi'" /></span> ונכונות

<div class="text-center text-[18px] mt-2" dir="ltr">
<KatexInline display math="\theta_{\mathcal{F}}=\bigwedge_{U\in\mathcal{F}_{uncond}}\Box\Diamond tk_U\ \land\ \bigwedge_{S\in\mathcal{F}_{strong}}(\Box\Diamond en_S\Rightarrow\Box\Diamond tk_S)\ \land\ \bigwedge_{W\in\mathcal{F}_{weak}}(\Diamond\Box en_W\Rightarrow\Box\Diamond tk_W)" />
</div>

<div class="mt-1 bg-slate-50 border border-slate-200 rounded p-1 text-[13px] leading-tight text-right">
<div class="font-bold tracking-wide">נכונות <KatexInline math="\theta_{\mathcal{F}}" />:</div>
כל מחובר הוא הגדרת הוגנות אחת (<KatexInline math="tk_X" />="נבחרה לאחרונה", <KatexInline math="en_X" />="מאופשרת כעת").
<ul class="list-disc ps-4 space-y-0 mt-0">
<li>בלתי-מותנית <KatexInline math="U" />: נבחרת אינסוף פעמים.</li>
<li>חזקה <KatexInline math="S" />: מאופשרת אינסוף פעמים גוררת נבחרת אינסוף פעמים.</li>
<li>חלשה <KatexInline math="W" />: מאופשרת מרגע מסוים גוררת נבחרת אינסוף פעמים.</li>
</ul>
</div>

<div class="text-center text-[16px] mt-0" dir="ltr">
<KatexInline display math="\varphi'=\theta_{\mathcal{F}}\Rightarrow\varphi" />
</div>

<div class="text-[13px] -mt-2 text-right mx-2">
<div class="font-bold tracking-wide">נכונות <KatexInline math="\varphi'" />:</div>
הגרירה ריקה (אמת) בריצה לא-הוגנת, ודורשת קיום <KatexInline math="\varphi" /> רק בריצה הוגנת, כלומר שקולה ל-<KatexInline math="\rho\models_{\mathcal{F}}\varphi" />.
</div>

<div v-click class="mt-0.5 bg-blue-50 border border-blue-200 rounded p-0.5 text-[12px] leading-tight">
לכל ריצה <KatexInline math="\rho" /> של <KatexInline math="TS" />, יש בדיוק ריצה <KatexInline math="\rho'" /> של <KatexInline math="TS'" /> מעליה (ה-<KatexInline math="b" />-ים נקבעים חד-משמעית מהפעולות, פרט לראשון שאינו משנה); ולהפך, השמטת הסיביות מכל ריצה של <KatexInline math="TS'" /> נותנת ריצה של <KatexInline math="TS" />.
</div>

<div v-click class="mt-0.5 bg-blue-50 border border-blue-200 rounded p-0.5 text-[12px] leading-tight">
מבניית <KatexInline math="L'" />: <span dir="ltr"><KatexInline math="\rho'\models\theta_{\mathcal{F}}\iff\rho" /> הוגנת ביחס ל-<KatexInline math="\mathcal{F}" /></span> (כל מחובר תואם מילה במילה את הגדרת ההוֹגְנוּת), ו-<span dir="ltr"><KatexInline math="\rho'\models\varphi\iff\rho\models\varphi" /></span> (כי <KatexInline math="AP\subseteq AP'" /> והתיוג על <KatexInline math="AP" /> לא השתנה).
</div>

<div v-click class="mt-0.5 bg-emerald-50 border border-emerald-200 rounded p-0.5 text-[13px] leading-tight text-center">
לכן <span dir="ltr"><KatexInline math="TS'\models(\theta_{\mathcal{F}}\Rightarrow\varphi)\iff\forall\rho\ (\rho\ \mathcal{F}\text{-הוגנת}\Rightarrow\rho\models\varphi)\iff TS\models_{\mathcal{F}}\varphi" /></span>.
</div>

---

# פתרון ג': הבנייה על הדוגמה

<div class="text-right text-[16px] leading-relaxed mt-2">
<span dir="ltr"><KatexInline math="\Gamma=\{\{\gamma\}\}" /></span>, סיבית יחידה <KatexInline math="b\in\{0,1\}" />, <span dir="ltr"><KatexInline math="AP'=\{p,en_{\gamma},tk_{\gamma}\}" /></span>.
</div>

<div class="flex justify-center -mt-1 scale-[0.82] origin-top">
<TransitionSystemD3
  :width="850" :height="160"
  :states="[
    { id: 'a', text: '$\\langle s_0,0 \\rangle$', initial: true, initialDirection: 'top', x: 95, y: 70, width: 110 },
    { id: 'b', text: '$\\langle s_1,1 \\rangle$', x: 315, y: 70, width: 110 },
    { id: 'c', text: '$\\langle s_2,0 \\rangle$', x: 535, y: 70, width: 110 },
    { id: 'd', text: '$\\langle s_1,0 \\rangle$', x: 755, y: 70, width: 110 }
  ]"
  :transitions="[
    { source: 'a', target: 'a', action: '$\\alpha$', loopDirection: '180deg', loopRadius: 150, actionX: 30 },
    { source: 'a', target: 'b', actionY: -12, action: '$\\gamma$' },
    { source: 'b', target: 'c', actionY: -12, action: '$\\beta$' },
    { source: 'c', target: 'd', actionY: 22, action: '$\\delta$' },
    { source: 'd', target: 'c', actionY: -22, action: '$\\beta$' }
  ]"
/>
</div>

<div class="text-center text-[15px] -mt-2" dir="ltr">
<KatexInline math="L'(\langle s_0,0\rangle)=\{en_{\gamma}\},\quad L'(\langle s_1,1\rangle)=\{p,tk_{\gamma}\},\quad L'(\langle s_2,0\rangle)=\emptyset,\quad L'(\langle s_1,0\rangle)=\{p\}" />
</div>

<div v-click class="mt-1 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed" dir="ltr">
החלק הנגיש: <KatexInline math="\{\langle s_0,0\rangle,\langle s_1,1\rangle,\langle s_2,0\rangle,\langle s_1,0\rangle\}" /> — 4 מתוך 6 הצירופים (<KatexInline math="\langle s_0,1\rangle,\langle s_2,1\rangle" /> אינם נגישים). שימו לב: <KatexInline math="s_1" /> <span dir="rtl">מתפצל לשני מצבים נגישים</span> — <KatexInline math="\langle s_1,1\rangle" /> מגיעים אליו ב-<KatexInline math="\gamma" />, <KatexInline math="\langle s_1,0\rangle" /> ב-<KatexInline math="\delta" /> — כך ש-<KatexInline math="TS'" /> אכן <span class="font-bold">גדול ממש</span> מ-<KatexInline math="TS" />.
</div>

<div v-click class="mt-2 text-center text-[20px]" dir="ltr">
<KatexInline display math="\varphi'=\left(\Box\Diamond en_{\gamma}\Rightarrow\Box\Diamond tk_{\gamma}\right)\Rightarrow\Box\Diamond p" />
</div>

---

# פתרון ד': ניתוח הריצות ומסקנה

<div class="text-right text-[16px] leading-relaxed mt-2">
מהתרשים, כל ריצה של <span dir="ltr"><KatexInline math="TS'" /></span> (הח"נ) מתחילה ב-<KatexInline math="\langle s_0,0\rangle" />, ומתפצלת לשני מקרים בלבד: נשארת בו לעד (לולאת <KatexInline math="\alpha" />), או עוברת בשלב סופי ב-<KatexInline math="\gamma" /> ונכנסת למחזור <span dir="ltr"><KatexInline math="\langle s_1,1\rangle\to\langle s_2,0\rangle\to\langle s_1,0\rangle\to\langle s_2,0\rangle\to\cdots" /></span> (אין דרך לחזור ל-<KatexInline math="\langle s_0,0\rangle" />).
</div>

<div v-click class="mt-3 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] leading-relaxed text-right">
<span class="font-bold">מקרה 1 (לולאת <KatexInline math="\alpha" /> לעד):</span> <KatexInline math="en_{\gamma}" /> מתקיים תמיד אך <KatexInline math="tk_{\gamma}" /> לעולם לא, כך ש-<span dir="ltr"><KatexInline math="\theta_{\mathcal{F}}=(\Box\Diamond en_{\gamma}\Rightarrow\Box\Diamond tk_{\gamma})" /></span> שקרי — ו-<KatexInline math="\varphi'=\theta_{\mathcal{F}}\Rightarrow\varphi" /> מתקיים באופן ריק.
</div>

<div v-click class="mt-3 bg-blue-50 border border-blue-200 rounded p-2 text-[15px] leading-relaxed text-right">
<span class="font-bold">מקרה 2 (יוצאים בשלב סופי):</span> מאז <KatexInline math="\gamma" /> אינו זמין עוד, ולכן <KatexInline math="\Box\Diamond en_{\gamma}" /> שקרי ו-<KatexInline math="\theta_{\mathcal{F}}" /> מתקיים שוב באופן ריק. (וגם בלי ריקנות: במחזור <KatexInline math="\langle s_1,\cdot\rangle" /> — ולכן <KatexInline math="p" /> — חוזר אינסוף פעמים, כך ש-<KatexInline math="\Box\Diamond p" /> מתקיים ישירות.)
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-2 text-[16px] leading-relaxed">
בשני המקרים <span dir="ltr"><KatexInline math="TS'\models\varphi'" /></span>, ולפי סעיף ב' מתקיים <span dir="ltr"><KatexInline math="TS\models_{\mathcal{F}}\varphi" /></span>. בניגוד לדוגמה "שקופה": כאן <span dir="ltr"><KatexInline math="TS\not\models\varphi" /></span> בלי הנחת ההוֹגְנוּת (הריצה <KatexInline math="s_0^\omega" /> מפרה אותה), וההוֹגְנוּת היא שמכריחה בסוף לבחור ב-<KatexInline math="\gamma" /> ומכאן את קיום <KatexInline math="\varphi" />.
</div>

---

# שאלה: תרגום LTL לאוטומט Büchi עם Always במקום Until (20 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
נתבונן בתחביר LTL מצומצם, בלי אופרטור <span dir="ltr">Until</span> כלל: הבסיס הוא <span dir="ltr"><KatexInline math="\{AP,\neg,\land,\bigcirc,\Box\}" /></span> (כש-<KatexInline math="\Box" /> הוא אופרטור <span class="font-bold">יסודי</span>, לא סוכר תחבירי; <KatexInline math="\Diamond\psi:=\neg\Box\neg\psi" /> נשארת הגדרה).
</div>

<div class="mt-5 bg-blue-50 border border-blue-200 rounded p-4 text-[19px] leading-relaxed">
<span class="font-bold">המשימה:</span> הציעו את שלבי הבנייה (סגירה, עקביות, מעברים, תנאי קבלה) לתרגום נוסחה בתחביר הזה לאוטומט Büchi מוכלל, באותה שיטה שנלמדה עבור <span dir="ltr">Until</span>.
</div>

<div class="text-right text-[16px] leading-relaxed mt-5 text-gray-600">
תזכורת לחוק הפריסה: <span dir="ltr"><KatexInline math="\Box\psi\equiv\psi\land\bigcirc\Box\psi" /></span> (במקום <KatexInline math="\psi_1\mathbin{\mathrm{U}}\psi_2\equiv\psi_2\lor(\psi_1\land\bigcirc(\psi_1\mathbin{\mathrm{U}}\psi_2))" />).
</div>

---

# הסעיפים

<div class="space-y-3 text-right text-[18px] leading-relaxed mt-3">

<div class="bg-slate-50 border border-slate-200 rounded p-3">
<span class="font-bold">א'. (5 נק')</span>
גזרו, מתוך חוק הפריסה של <KatexInline math="\Box" />, את כלל העקביות הבוליאנית ואת כללי המעברים (<KatexInline math="\delta" />) עבור תת־נוסחה <span dir="ltr"><KatexInline math="\Box\psi\in cl(\varphi)" /></span>, באותה שיטה שבה נגזרו כללי ה-<span dir="ltr">Until</span>.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3">
<span class="font-bold">ב'. (5 נק')</span>
הסבירו מדוע <span class="font-bold">אין</span> צורך בקבוצת קבלה עבור תת־נוסחאות <KatexInline math="\Box\psi" />, בניגוד ל-<span dir="ltr">Until</span>.
</div>

<div class="bg-red-50 border border-red-200 rounded p-3">
<span class="font-bold">ג'. (5 נק')</span>
הראו שריצה אינסופית שמנחשת <span dir="ltr"><KatexInline math="\neg\Box\psi" /></span> לנצח (לפי כללי סעיף א') בלי ש-<KatexInline math="\neg\psi" /> מתקיים אי-פעם, עוברת את כל בדיקות העקביות והמעברים. הסיקו שיש צורך בקבוצת קבלה גם כשאין <span dir="ltr">Until</span> בתחביר, וכתבו אותה.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-3">
<span class="font-bold">ד'. (5 נק')</span>
הפעילו את הבנייה על <span dir="ltr"><KatexInline math="\varphi=\Box a\land\neg\Box\neg b" /></span> (כלומר <KatexInline math="\Box a\land\Diamond b" />) מעל <span dir="ltr"><KatexInline math="AP=\{a,b\}" /></span>: רשמו את <KatexInline math="cl(\varphi)" />, מצב התחלה אחד לדוגמה עם המעבר היוצא ממנו, ואת <KatexInline math="\mathcal{F}" />.
</div>

</div>

---

# פתרון א': עקביות ומעברים עבור <span dir="ltr"><KatexInline math="\Box" /></span>

<div class="text-right text-[16px] leading-relaxed mt-2">
מחוק הפריסה <span dir="ltr"><KatexInline math="\Box\psi\equiv\psi\land\bigcirc\Box\psi" /></span> (קוניונקציה, לעומת הדיסיונקציה של <span dir="ltr">Until</span>):
</div>

<div class="mt-2 bg-blue-50 border border-blue-200 rounded p-3 text-[17px]" dir="ltr">
<div class="font-bold text-blue-800 mb-1 text-right">עקביות בוליאנית</div>
<div class="text-center"><KatexInline math="\Box\psi\in B\Rightarrow\psi\in B" /></div>
</div>

<div class="mt-2 bg-amber-50 border border-amber-200 rounded p-3 text-[17px]" dir="ltr">
<div class="font-bold text-amber-800 mb-1 text-right">מעברים</div>
<div class="text-center"><KatexInline math="\Box\psi\in B\Rightarrow\psi\in B\ \land\ \Box\psi\in B'" /></div>
<div class="mt-1 text-center"><KatexInline math="\Box\psi\notin B\ \land\ \psi\in B\Rightarrow\Box\psi\notin B'" /></div>
</div>

<div v-click class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed">
שימו לב: בניגוד ל-<span dir="ltr">Until</span>, אין כאן כלל "מספיק" חד-מצבי (כמו <span dir="ltr"><KatexInline math="\psi_2\in B\Rightarrow\psi_1\mathbin{\mathrm{U}}\psi_2\in B" /></span>): קוניונקציה לא מאפשרת "להיפטר" מההתחייבות לעתיד באף שלב.
</div>

---

# פתרון ב': למה <span dir="ltr"><KatexInline math="\Box" /></span> לא דורש קבוצת קבלה?

<div class="text-right text-[18px] leading-relaxed mt-4">
ההתחייבות <span dir="ltr"><KatexInline math="\Box\psi" /></span> מופרת באופן <span class="font-bold">מקומי וסופי</span>: ברגע ש-<KatexInline math="\psi" /> נכשלת איפשהו, כלל העקביות (סעיף א') כבר מוציא את <KatexInline math="\Box\psi" /> מכל מצב מאותו רגע והלאה.
</div>

<div v-click class="mt-4 bg-emerald-50 border border-emerald-200 rounded p-4 text-[18px] leading-relaxed">
אין כאן "הבטחה" שממתינה למימוש עתידי, רק התחייבות שנבדקת אינסוף פעמים מבלי שאפשר לדחות אותה: ניחוש עקבי ל-<KatexInline math="\Box\psi" /> בכל מצב כבר <span class="font-bold">שווה</span> סמנטית לאמת של <KatexInline math="\Box\psi" />, ולכן אין סיכון של "שקר שלא נחשף".
</div>

<div v-click class="mt-4 bg-amber-50 border border-amber-200 rounded p-3 text-[16px] leading-relaxed">
זו אותה תובנה כמו "בלי <span dir="ltr">Until</span> אין הבטחות לאכוף" שראינו בשקפים הקודמים, רק ממוקדת בתת־נוסחה ספציפית: ל-<span dir="ltr"><KatexInline math="\Box\psi" /></span> עצמה (בכיוון החיובי) אין צד חַיּוּת.
</div>

---

# פתרון ג': אבל <span dir="ltr"><KatexInline math="\neg\Box\psi" /></span> זו הבטחה!

<div class="grid grid-cols-[0.95fr_1.05fr] gap-5 items-center mt-2">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="380" :height="220" :arrowSize="4" :stateLabelFontSize="13" :transitionLabelFontSize="13"
  :states="[
    { id: 'q', x: 190, y: 110, label: '$\\neg\\Box\\psi,\\psi$', initial: true, initialDirection: 'left', accepting: false, stroke: '#dc2626', r: 42, labelWidth: 170, labelHeight: 40 }
  ]"
  :transitions="[
    { source: 'q', target: 'q', label: '$\\psi$', loopDirection: '-90deg', labelY: -12, labelWidth: 60 }
  ]"
/>
</div>

<div class="text-right text-[15px] leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">ריצה לא טובה</div>
בכל צעד <KatexInline math="\psi" /> מתקיים (אז <KatexInline math="\neg\psi" /> לא), אבל לפי סעיף א' (השלילה שלו) <span dir="ltr"><KatexInline math="\neg\Box\psi\notin B\land\psi\in B\Rightarrow\neg\Box\psi\in B'" /></span> אינו אילוץ קיים, כך שהמעבר העצמי שממשיך לנחש <KatexInline math="\neg\Box\psi" /> עובר את כל הבדיקות.
</div>
<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">תיקון Büchi</div>
<KatexInline math="\neg\Box\psi" /> שקול ל-<KatexInline math="\Diamond\neg\psi" />, הבטחה כמו <span dir="ltr"><KatexInline math="true\mathbin{\mathrm{U}}\neg\psi" /></span>. צריך לפסול ריצות שתמיד "פתוחות" בה.
</div>
</div>
</div>

<div class="mt-5 text-center text-[24px]" dir="ltr">
<KatexInline display math="F_{\neg\Box\psi}=\{B\in Q\mid\neg\Box\psi\notin B\ \lor\ \neg\psi\in B\}" />
</div>

---

# פתרון ד': הבנייה על <span dir="ltr"><KatexInline math="\Box a\land\Diamond b" /></span>

<div class="text-right text-[16px] leading-relaxed mt-2" dir="ltr">
<KatexInline math="cl(\varphi)=\{a,\neg a,\ b,\neg b,\ \Box a,\neg\Box a,\ \Box\neg b,\neg\Box\neg b,\ \varphi,\neg\varphi\}" />, כאשר <KatexInline math="\varphi=\Box a\land\neg\Box\neg b" />.
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[17px]" dir="ltr">
<div class="text-right font-bold mb-1">מצב התחלה לדוגמה (חייב להכיל <KatexInline math="\varphi" />, ולכן <KatexInline math="\Box a" /> ו-<KatexInline math="\neg\Box\neg b" />)</div>
<KatexInline display math="B=\{\varphi,\ \Box a,\ a,\ \neg\Box\neg b,\ \neg b\}" />
</div>

<div v-click class="mt-2 bg-amber-50 border border-amber-200 rounded p-3 text-[16px] leading-relaxed" dir="ltr">
לפי סעיף א': <KatexInline math="\Box a\in B\Rightarrow a\in B" />; ובחרנו <KatexInline math="\neg b\in B" /> כדי שההבטחה <KatexInline math="\neg\Box\neg b" /> תישאר פתוחה (שאר התוויות, כגון <KatexInline math="\neg\Box a" />, נקבעות במשתמע ע"י המקסימליות).
</div>

<div v-click class="mt-2 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed" dir="ltr">
לפי סעיף א': <KatexInline math="\Box a\in B\Rightarrow\Box a\in B'" />. לפי סעיף ג' (<KatexInline math="\neg b\in B" />): אין אילוץ על <KatexInline math="\neg\Box\neg b" /> ב-<KatexInline math="B'" /> (יכול להיפתח או להיסגר). מעבר חוקי אחד: <KatexInline math="B'=\{\Box a,a,\Box\neg b,b\}" /> (סוגרים את ההבטחה: <KatexInline math="b\in B'" />).
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[18px] text-center" dir="ltr">
<KatexInline math="\mathcal{F}=\{F_{\neg\Box\neg b}\},\qquad F_{\neg\Box\neg b}=\{B\mid \neg\Box\neg b\notin B\lor\neg b\in B\}" />
</div>

<div v-click class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed">
שימו לב: <KatexInline math="\Box a" /> לא תורם אף קבוצת קבלה (לפי סעיף ב'); כל ה-<KatexInline math="\mathcal{F}" /> מגיע מההבטחה הנסתרת בתוך <KatexInline math="\neg\Box\neg b" />, אף שאין <span dir="ltr">Until</span> בתחביר כלל.
</div>

---

# שאלה: אלגוריתם חלופי לבדיקת <span dir="ltr"><KatexInline math="TS\models P" /></span> (20 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
תהי <KatexInline math="P" /> תכונה <KatexInline math="\omega" />-רגולרית, ויהי <span dir="ltr"><KatexInline math="\mathcal{A}=\langle Q,2^{AP},\delta,Q_0,F\rangle" /></span> אוטומט Büchi עם <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A})=P" /></span> (אוטומט <span class="font-bold">של</span> <KatexInline math="P" /> עצמה, לא של שלילתה).
</div>

<div class="mt-5 bg-blue-50 border border-blue-200 rounded p-4 text-[19px] leading-relaxed">
מרצה הציע: לבדוק <span dir="ltr"><KatexInline math="TS\models P" /></span> על ידי בניית <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span> ווידוא <span dir="ltr"><KatexInline math="TS\times\mathcal{A}\models\Box\Diamond F" /></span> (כל ריצה של המכפלה מבקרת ב-<KatexInline math="F" /> אינסוף פעמים).
</div>

<div class="text-right text-[16px] leading-relaxed mt-5 text-gray-600">
תזכורת: בשיטה שנלמדה, עבדנו עם אוטומט <span class="font-bold">של העקבות הרעות</span> (<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A})=(2^{AP})^\omega\setminus P" /></span>) וחיפשנו ריצה מקבלת <span class="font-bold">אחת</span> במכפלה. כאן, לעומת זאת, משתמשים באוטומט של <KatexInline math="P" /> עצמה ודורשים שכל הריצות יתקבלו.
</div>

---

# הסעיפים

<div class="space-y-4 text-right text-[19px] leading-relaxed mt-4">

<div class="bg-red-50 border border-red-200 rounded p-4">
<span class="font-bold">א'. (10 נק')</span>
הראו, באמצעות דוגמה נגדית קונקרטית (<KatexInline math="TS" /> ו-<KatexInline math="\mathcal{A}" />), שהבנייה <span class="font-bold">אינה נכונה</span> במקרה הכללי: בנו מערכת ואוטומט כך ש-<span dir="ltr"><KatexInline math="TS\models P" /></span> אך <span dir="ltr"><KatexInline math="TS\times\mathcal{A}\not\models\Box\Diamond F" /></span>.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<span class="font-bold">ב'. (10 נק')</span>
הוכיחו שאם <KatexInline math="\mathcal{A}" /> <span class="font-bold">דטרמיניסטי</span> (כלומר <span dir="ltr"><KatexInline math="|Q_0|=1" /></span> ו-<KatexInline math="\delta" /> פונקציה חד-ערכית), אז <span dir="ltr"><KatexInline math="TS\models P\iff TS\times\mathcal{A}\models\Box\Diamond F" /></span>.
</div>

</div>

---

# פתרון א': בניית הדוגמה הנגדית

<div class="text-right text-[16px] leading-relaxed mt-1">
<KatexInline math="AP=\{a\}" />, <KatexInline math="P=\Box\Diamond a" /> ("אינסוף פעמים <KatexInline math="a" />").
</div>

<div class="grid grid-cols-2 gap-4 mt-1 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-1">
<div class="text-center text-[14px] font-bold text-slate-600 -mb-1">האוטומט <span dir="ltr">𝒜</span> (לא דטרמיניסטי!)</div>
<AutomatonD3 variant="classic" :width="380" :height="190" :arrowSize="3.5" :stateLabelFontSize="15" :transitionLabelFontSize="13"
  :states="[
    { id: 'q0', x: 100, y: 100, label: '$q_0$', initial: true, initialDirection: 'left', r: 28 },
    { id: 'q1', x: 300, y: 100, label: '$q_1$', accepting: true, r: 28, fill: '#d1fae5', stroke: '#059669' }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$true$', loopDirection: '-90deg', labelY: -10, labelWidth: 40 },
    { source: 'q0', target: 'q1', label: '$a$', labelY: -10, curve: 0.15 },
    { source: 'q1', target: 'q1', label: '$a$', loopDirection: '-90deg', labelY: -10, labelWidth: 40 },
    { source: 'q1', target: 'q0', label: '$true$', labelY: 10, curve: 0.15 }
  ]"
/>
</div>
<div class="bg-white rounded border border-slate-200 shadow-sm p-1">
<div class="text-center text-[14px] font-bold text-slate-600 -mb-1">המערכת <span dir="ltr">TS</span></div>
<TransitionSystemD3
  :width="320" :height="190"
  :states="[
    { id: 's0', text: 's0', label: '{a}', initial: true, initialDirection: 'top', x: 220, y: 40, width: 80 },
    { id: 's1', text: 's1', label: '∅', x: 220, y: 160, width: 80 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: 'step', curve: 0.3 },
    { source: 's1', target: 's0', action: 'step', curve: 0.3 }
  ]"
/>
</div>
</div>

<div v-click class="mt-1 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] leading-relaxed">
<KatexInline math="\delta(q_0,\{a\})=\{q_0,q_1\}" /> ו-<KatexInline math="\delta(q_1,\{a\})=\{q_0,q_1\}" />: בכל פעם ש-<KatexInline math="a" /> מופיע, אפשר <span class="font-bold">לבחור</span> אם "לחגוג" (לעבור/להישאר ב-<KatexInline math="q_1" />) או להישאר סקפטי ב-<KatexInline math="q_0" /> — אותה מילה יכולה להתקבל ע"י ריצה אחת ולהיכשל בריצה אחרת.
</div>

---

# פתרון א' (המשך): המכפלה חושפת את הבעיה

<div class="text-right text-[16px] leading-relaxed mt-1">
<span dir="ltr"><KatexInline math="\mathit{Traces}(TS)=\{(\{a\}\emptyset)^\omega\}" /></span>, ו-<KatexInline math="a" /> מתקיים אינסוף פעמים בה, אז <span dir="ltr"><KatexInline math="TS\models P" /></span> (באופן <span class="font-bold">טריוויאלי</span> — זו העקבה היחידה).
</div>

<div class="flex justify-center mt-1 scale-[0.88] origin-top">
<AutomatonD3 variant="classic" :width="480" :height="200" :arrowSize="3.5" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { id: 'p1', x: 240, y: 40, label: '$\\langle s_0,q_0\\rangle$', initial: true, initialDirection: 'top', r: 34, labelWidth: 90 },
    { id: 'p2', x: 100, y: 160, label: '$\\langle s_1,q_0\\rangle$', r: 34, labelWidth: 90, stroke: '#dc2626', strokeWidth: 2.5 },
    { id: 'p3', x: 380, y: 160, label: '$\\langle s_0,q_1\\rangle$', initial: true, initialDirection: 'top', r: 34, labelWidth: 90, accepting: true, fill: '#d1fae5', stroke: '#059669' }
  ]"
  :transitions="[
    { source: 'p1', target: 'p2', label: '', curve: 0 },
    { source: 'p2', target: 'p1', label: '', curve: 0.2, stroke: '#dc2626' },
    { source: 'p2', target: 'p3', label: '', curve: -0.2 },
    { source: 'p3', target: 'p2', label: '', curve: 0 }
  ]"
/>
</div>

<div v-click class="mt-1 bg-red-50 border border-red-200 rounded p-2 text-[15px] leading-relaxed" dir="ltr">
<span class="font-bold text-red-700">ריצה לא טובה:</span> <KatexInline math="\langle s_0,q_0\rangle\langle s_1,q_0\rangle\langle s_0,q_0\rangle\cdots" /> (המעגל האדום) — קיימת, ולעולם לא מבקרת ב-<KatexInline math="F=\{q_1\}" />.
</div>

<div v-click class="mt-2 bg-emerald-50 border border-emerald-200 rounded p-3 text-[17px] leading-relaxed">
לכן <span dir="ltr"><KatexInline math="TS\times\mathcal{A}\not\models\Box\Diamond F" /></span> (לא <span class="font-bold">כל</span> ריצה מבקרת ב-<KatexInline math="F" /> אינסוף פעמים), בעוד <span dir="ltr"><KatexInline math="TS\models P" /></span>. הבנייה המוצעת <span class="font-bold">שגויה</span>: היא נותנת תוצאה שגויה ("דוגמה נגדית" מדומה).
</div>

---

# פתרון ב': נכונות כש-<KatexInline math="\mathcal{A}" /> דטרמיניסטי

<div class="text-right text-[18px] leading-relaxed mt-3">
<span class="font-bold">כיוון 1</span> (<span dir="ltr"><KatexInline math="\Leftarrow" /></span>, לא דורש דטרמיניזם): אם <span dir="ltr"><KatexInline math="TS\times\mathcal{A}\models\Box\Diamond F" /></span>, אז בפרט לכל ריצה <KatexInline math="\rho" /> של <KatexInline math="TS" /> <span class="font-bold">קיימת</span> ריצה של <KatexInline math="\mathcal{A}" /> על <KatexInline math="trace(\rho)" /> שמבקרת ב-<KatexInline math="F" /> אינסוף פעמים (זו שבמכפלה), ולכן <span dir="ltr"><KatexInline math="trace(\rho)\in L_\omega(\mathcal{A})=P" /></span>. מכאן <span dir="ltr"><KatexInline math="TS\models P" /></span>.
</div>

<div v-click class="mt-4 text-right text-[18px] leading-relaxed">
<span class="font-bold">כיוון 2</span> (<span dir="ltr"><KatexInline math="\Rightarrow" /></span>, כאן צריך דטרמיניזם): תהי <span dir="ltr"><KatexInline math="\pi=\langle s_0,q_0\rangle\langle s_1,q_1\rangle\cdots" /></span> ריצה <span class="font-bold">כלשהי</span> של <KatexInline math="TS\times\mathcal{A}" />, ו-<KatexInline math="\rho=s_0s_1\cdots" /> ההיטל שלה על <KatexInline math="TS" />.
</div>

<div v-click class="mt-3 bg-amber-50 border border-amber-200 rounded p-3 text-[16px] leading-relaxed">
מכיוון ש-<KatexInline math="\delta" /> פונקציה חד-ערכית (ו-<KatexInline math="|Q_0|=1" />), הרצף <span dir="ltr"><KatexInline math="q_0q_1\cdots" /></span> <span class="font-bold">נקבע ביחידות</span> ע"י <KatexInline math="trace(\rho)" /> — זו <span class="font-bold">הריצה היחידה האפשרית</span> של <KatexInline math="\mathcal{A}" /> על המילה הזו (לא ריצה כלשהי מבין כמה).
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[17px] leading-relaxed">
מ-<span dir="ltr"><KatexInline math="TS\models P" /></span> נובע <span dir="ltr"><KatexInline math="trace(\rho)\in L_\omega(\mathcal{A})" /></span>, כלומר <span class="font-bold">הריצה היחידה</span> של <KatexInline math="\mathcal{A}" /> על <KatexInline math="trace(\rho)" /> מבקרת ב-<KatexInline math="F" /> אינסוף פעמים. אבל זו בדיוק הריצה <span dir="ltr"><KatexInline math="q_0q_1\cdots" /></span> של <KatexInline math="\pi" />! לכן <KatexInline math="\pi" /> מבקרת ב-<KatexInline math="F" /> אינסוף פעמים.
</div>

<div v-click class="mt-2 bg-blue-50 border border-blue-200 rounded p-2 text-[16px] leading-relaxed text-right">
<KatexInline math="\pi" /> הייתה שרירותית, ולכן <span dir="ltr"><KatexInline math="TS\times\mathcal{A}\models\Box\Diamond F" /></span>.
</div>
