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
החלק הנגיש: <KatexInline math="\{\langle s_0,0\rangle,\langle s_1,1\rangle,\langle s_2,0\rangle,\langle s_1,0\rangle\}" />: 4 מתוך 6 הצירופים (<KatexInline math="\langle s_0,1\rangle,\langle s_2,1\rangle" /> אינם נגישים). שימו לב: <KatexInline math="s_1" /> <span dir="rtl">מתפצל לשני מצבים נגישים</span>: <KatexInline math="\langle s_1,1\rangle" /> מגיעים אליו ב-<KatexInline math="\gamma" />, <KatexInline math="\langle s_1,0\rangle" /> ב-<KatexInline math="\delta" />. לכן <KatexInline math="TS'" /> אכן <span class="font-bold">גדול ממש</span> מ-<KatexInline math="TS" />.
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
<span class="font-bold">מקרה 1 (לולאת <KatexInline math="\alpha" /> לעד):</span> <KatexInline math="en_{\gamma}" /> מתקיים תמיד אך <KatexInline math="tk_{\gamma}" /> לעולם לא, כך ש-<span dir="ltr"><KatexInline math="\theta_{\mathcal{F}}=(\Box\Diamond en_{\gamma}\Rightarrow\Box\Diamond tk_{\gamma})" /></span> שקרי, ו-<KatexInline math="\varphi'=\theta_{\mathcal{F}}\Rightarrow\varphi" /> מתקיים באופן ריק.
</div>

<div v-click class="mt-3 bg-blue-50 border border-blue-200 rounded p-2 text-[15px] leading-relaxed text-right">
<span class="font-bold">מקרה 2 (יוצאים בשלב סופי):</span> מאז <KatexInline math="\gamma" /> אינו זמין עוד, ולכן <KatexInline math="\Box\Diamond en_{\gamma}" /> שקרי ו-<KatexInline math="\theta_{\mathcal{F}}" /> מתקיים שוב באופן ריק. (וגם בלי ריקנות: במחזור <KatexInline math="\langle s_1,\cdot\rangle" />, ולכן <KatexInline math="p" />, חוזר אינסוף פעמים, כך ש-<KatexInline math="\Box\Diamond p" /> מתקיים ישירות.)
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-2 text-[16px] leading-relaxed">
בשני המקרים <span dir="ltr"><KatexInline math="TS'\models\varphi'" /></span>, ולפי סעיף ב' מתקיים <span dir="ltr"><KatexInline math="TS\models_{\mathcal{F}}\varphi" /></span>. בניגוד לדוגמה "שקופה": כאן <span dir="ltr"><KatexInline math="TS\not\models\varphi" /></span> בלי הנחת ההוֹגְנוּת (הריצה <KatexInline math="s_0^\omega" /> מפרה אותה), וההוֹגְנוּת היא שמכריחה בסוף לבחור ב-<KatexInline math="\gamma" /> ומכאן את קיום <KatexInline math="\varphi" />.
</div>

---

# שאלה: תרגום LTL לאוטומט Büchi עם Always במקום Until (20 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
נתבונן בתחביר LTL מצומצם, בלי אופרטור <span dir="ltr">Until</span> כלל:
</div>

<div class="text-center text-[20px] mt-3" dir="ltr">
<KatexInline display math="\varphi ::= true \mid p \mid \neg\varphi \mid \varphi\land\varphi \mid \bigcirc\varphi \mid \textcolor{blue}{\Box\varphi} \qquad (p\in AP)" />
</div>

<div class="text-right text-[16px] leading-relaxed mt-3 text-gray-600">
(<KatexInline math="\Box" /> הוא אופרטור <span class="font-bold">יסודי</span> בתחביר זה, לא סוכר תחבירי; <KatexInline math="\Diamond\psi:=\neg\Box\neg\psi" /> נשארת הגדרה.)
</div>

<div class="text-right text-[15px] leading-relaxed mt-2 text-gray-600">
הערה: התחביר הזה חלש ממש מ-LTL המלא; ניתן להוכיח שאי אפשר לבטא בו את <KatexInline math="p\mathbin{\mathrm{U}}q" /> (גם בעזרת הסוכרים התחביריים <KatexInline math="\Diamond,\lor,\Rightarrow" />).
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
הפעילו את הבנייה על <span dir="ltr"><KatexInline math="\varphi=\Box a\land\neg\Box b" /></span> מעל <span dir="ltr"><KatexInline math="AP=\{a,b\}" /></span>: רשמו את <KatexInline math="cl(\varphi)" />, מצב התחלה אחד לדוגמה עם המעבר היוצא ממנו, ואת <KatexInline math="\mathcal{F}" />.
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
שימו לב: בניגוד ל-<span dir="ltr">Until</span>, אין כאן כלל "מספיק" חד-מצבי (כמו <span dir="ltr"><KatexInline math="\psi_2\in B\Rightarrow\psi_1\mathbin{\mathrm{U}}\psi_2\in B" /></span>): אי אפשר להיפטר מההתחייבות לעתיד באף שלב.
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
    { source: 'q', target: 'q', label: '', loopDirection: '-90deg', loopRadius: 90, stroke: '#dc2626', labelX: 0, labelY: -10 }
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

# פתרון ד': הבנייה על <span dir="ltr"><KatexInline math="\Box a\land\neg\Box b" /></span>

<div class="text-right text-[16px] leading-relaxed mt-2" dir="ltr">
<KatexInline math="cl(\varphi)=\{a,\neg a,\ b,\neg b,\ \Box a,\neg\Box a,\ \Box b,\neg\Box b,\ \varphi,\neg\varphi\}" />, כאשר <KatexInline math="\varphi=\Box a\land\neg\Box b" />.
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[17px]" dir="ltr">
<div class="text-right font-bold mb-1">מצב התחלה לדוגמה (חייב להכיל <KatexInline math="\varphi" />, ולכן <KatexInline math="\Box a" /> ו-<KatexInline math="\neg\Box b" />)</div>
<KatexInline display math="B=\{\varphi,\ \Box a,\ a,\ \neg\Box b,\ b\}" />
</div>

<div v-click class="mt-2 bg-amber-50 border border-amber-200 rounded p-3 text-[16px] leading-relaxed text-right">
לפי סעיף א': <KatexInline math="\Box a\in B\Rightarrow a\in B" />; ובחרנו <KatexInline math="b\in B" /> כדי שההבטחה <KatexInline math="\neg\Box b" /> (כלומר <KatexInline math="\Diamond\neg b" />) תישאר פתוחה (שאר התוויות, כגון <KatexInline math="\neg\Box a" />, נקבעות במשתמע ע"י המקסימליות).
</div>

<div v-click class="mt-2 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed text-right">
לפי סעיף א': <KatexInline math="\Box a\in B\Rightarrow\Box a\in B'" />. לפי סעיף ג' (<KatexInline math="b\in B" />): אין אילוץ על <KatexInline math="\neg\Box b" /> ב-<KatexInline math="B'" /> (יכול להיפתח או להיסגר). מעבר חוקי אחד: <KatexInline math="B'=\{\Box a,a,\neg\Box b,\neg b\}" /> (סוגרים את ההבטחה: <KatexInline math="\neg b\in B'" />).
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[18px] text-center" dir="ltr">
<KatexInline math="\mathcal{F}=\{F_{\neg\Box b}\},\qquad F_{\neg\Box b}=\{B\mid \neg\Box b\notin B\lor\neg b\in B\}" />
</div>

<div v-click class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed">
שימו לב: <KatexInline math="\Box a" /> לא תורם אף קבוצת קבלה (לפי סעיף ב'); כל ה-<KatexInline math="\mathcal{F}" /> מגיע מההבטחה הנסתרת בתוך <KatexInline math="\neg\Box b" />, אף שאין <span dir="ltr">Until</span> ולא <span dir="ltr">Diamond</span> בתחביר כלל.
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
    { source: 'q0', target: 'q1', label: '$a$', labelY: 12, curve: 0.15 },
    { source: 'q1', target: 'q1', label: '$a$', loopDirection: '-90deg', labelY: -10, labelWidth: 40 },
    { source: 'q1', target: 'q0', label: '$true$', labelY: -12, curve: 0.15 }
  ]"
/>
</div>
<div class="bg-white rounded border border-slate-200 shadow-sm p-1">
<div class="text-center text-[14px] font-bold text-slate-600 -mb-1">המערכת <span dir="ltr">TS</span></div>
<TransitionSystemD3
  :width="320" :height="190"
  :states="[
    { id: 's0', text: 's0', label: '$\\{a\\}$', initial: true, initialDirection: 'top', x: 220, y: 40, width: 80 },
    { id: 's1', text: 's1', label: '$\\{\\}$', x: 220, y: 160, width: 80 }
  ]"
  :transitions="[
    { source: 's0', target: 's1', action: 'step', curve: 0.3, actionX: -22 },
    { source: 's1', target: 's0', action: 'step', curve: 0.3, actionX: 22 }
  ]"
/>
</div>
</div>

<div v-click class="mt-1 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] leading-relaxed">
<KatexInline math="\delta(q_0,\{a\})=\{q_0,q_1\}" /> ו-<KatexInline math="\delta(q_1,\{a\})=\{q_0,q_1\}" />: בכל פעם ש-<KatexInline math="a" /> מופיע, אפשר <span class="font-bold">לבחור</span> אם "לחגוג" (לעבור/להישאר ב-<KatexInline math="q_1" />) או להישאר סקפטי ב-<KatexInline math="q_0" />. אותה מילה יכולה להתקבל ע"י ריצה אחת ולהיכשל בריצה אחרת.
</div>

---

# פתרון א' (המשך): המכפלה חושפת את הבעיה

<div class="text-right text-[16px] leading-relaxed mt-1">
<span dir="ltr"><KatexInline math="\mathit{Traces}(TS)=\{(\{a\}\emptyset)^\omega\}" /></span>, ו-<KatexInline math="a" /> מתקיים אינסוף פעמים בה, אז <span dir="ltr"><KatexInline math="TS\models P" /></span> (באופן <span class="font-bold">טריוויאלי</span>: זו העקבה היחידה).
</div>

<div class="flex justify-center mt-1 scale-[0.88] origin-top">
<AutomatonD3 variant="classic" :width="600" :height="200" :arrowSize="3.5" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { id: 'p1', x: 100, y: 160, label: '$\\langle s_0,q_0\\rangle$', initial: true, initialDirection: 'top', r: 34, labelWidth: 90 },
    { id: 'p2', x: 300, y: 160, label: '$\\langle s_1,q_0\\rangle$', r: 34, labelWidth: 90, stroke: '#dc2626', strokeWidth: 2.5 },
    { id: 'p3', x: 500, y: 160, label: '$\\langle s_0,q_1\\rangle$', initial: true, initialDirection: 'top', r: 34, labelWidth: 90, accepting: true, fill: '#d1fae5', stroke: '#059669' }
  ]"
  :transitions="[
    { source: 'p1', target: 'p2', label: '', curve: 0, stroke: '#dc2626' },
    { source: 'p2', target: 'p1', label: '', curve: 0.2, stroke: '#dc2626' },
    { source: 'p2', target: 'p3', label: '', curve: -0.2 },
    { source: 'p3', target: 'p2', label: '', curve: 0 }
  ]"
/>
</div>

<div v-click class="mt-1 bg-red-50 border border-red-200 rounded p-2 text-[15px] leading-relaxed text-right">
<span class="font-bold text-red-700">ריצה לא טובה:</span> <KatexInline math="\langle s_0,q_0\rangle\langle s_1,q_0\rangle\langle s_0,q_0\rangle\cdots" /> (המעגל האדום) קיימת, ולעולם לא מבקרת ב-<KatexInline math="F=\{q_1\}" />.
</div>

<div v-click class="mt-1 bg-blue-50 border border-blue-200 rounded p-2 text-[15px] leading-relaxed text-right">
הריצה הזאת מתאימה לשילוב של ריצת מערכת שהאוטומט <span class="font-bold">מקבל</span> (זו שעוברת תמיד ל-<KatexInline math="q_1" />) עם ריצה אחרת שהאוטומט <span class="font-bold">לא מקבל</span> (זו שנשארת ב-<KatexInline math="q_0" />).
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
מכיוון ש-<KatexInline math="\delta" /> פונקציה חד-ערכית (ו-<KatexInline math="|Q_0|=1" />), הרצף <span dir="ltr"><KatexInline math="q_0q_1\cdots" /></span> <span class="font-bold">נקבע ביחידות</span> ע"י <KatexInline math="trace(\rho)" />. זו <span class="font-bold">הריצה היחידה האפשרית</span> של <KatexInline math="\mathcal{A}" /> על המילה הזו (לא ריצה כלשהי מבין כמה).
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[17px] leading-relaxed">
מ-<span dir="ltr"><KatexInline math="TS\models P" /></span> נובע <span dir="ltr"><KatexInline math="trace(\rho)\in L_\omega(\mathcal{A})" /></span>, כלומר <span class="font-bold">הריצה היחידה</span> של <KatexInline math="\mathcal{A}" /> על <KatexInline math="trace(\rho)" /> מבקרת ב-<KatexInline math="F" /> אינסוף פעמים. אבל זו בדיוק הריצה <span dir="ltr"><KatexInline math="q_0q_1\cdots" /></span> של <KatexInline math="\pi" />! לכן <KatexInline math="\pi" /> מבקרת ב-<KatexInline math="F" /> אינסוף פעמים.
</div>

<div v-click class="mt-2 bg-blue-50 border border-blue-200 rounded p-2 text-[16px] leading-relaxed text-right">
<KatexInline math="\pi" /> הייתה שרירותית, ולכן <span dir="ltr"><KatexInline math="TS\times\mathcal{A}\models\Box\Diamond F" /></span>.
</div>

---

# שאלה: פירוק אוטומט Büchi לבטיחות וחַיּוּת (20 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
נתון אוטומט Büchi <span dir="ltr"><KatexInline math="\mathcal{A}=\langle Q,2^{AP},\delta,Q_0,F\rangle" /></span> המייצג תכונת זמן ליניארי <KatexInline math="\omega" />-רגולרית <span dir="ltr"><KatexInline math="P=L_\omega(\mathcal{A})" /></span> (לאו דווקא בטיחות או חַיּוּת).
</div>

<div class="mt-6 bg-blue-50 border border-blue-200 rounded p-4 text-[20px] leading-relaxed">
<span class="font-bold">המשימה:</span> בנו שני אוטומטי Büchi <span dir="ltr"><KatexInline math="\mathcal{A}_{safe},\mathcal{A}_{live}" /></span> מעל אותו א"ב <span dir="ltr"><KatexInline math="2^{AP}" /></span> כך ש:
</div>

<div class="mt-5 text-center text-[24px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A}_{safe})\cap L_\omega(\mathcal{A}_{live})=P" />
</div>

<div class="text-right text-[16px] leading-relaxed mt-3 text-gray-600">
כאשר <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{safe})" /></span> היא תכונת בטיחות ו-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{live})" /></span> היא תכונת חַיּוּת.
</div>

---

# הסעיפים

<div class="space-y-3 text-right text-[18px] leading-relaxed mt-3">

<div class="bg-slate-50 border border-slate-200 rounded p-3">
<span class="font-bold">א'. (5 נק')</span>
בנו אוטומט Büchi שקול ל-<KatexInline math="\mathcal{A}" /> בעזרת פרוצדורת המחיקה הבאה:

<div dir="ltr" class="text-left text-[15px] leading-relaxed bg-white border border-slate-200 rounded p-2 mt-2 font-mono">
<div><KatexInline math="R := Q" /></div>
<div><KatexInline math="\texttt{repeat}" /></div>
<div class="pl-6"><KatexInline math="Dead := \{q\in R \mid \nexists\ \text{path inside }R\text{ of length }>0\text{ from }q\text{ to }F\cap R\}" /></div>
<div class="pl-6"><KatexInline math="R := R\setminus Dead" /></div>
<div><KatexInline math="\texttt{until } Dead=\emptyset" /></div>
<div class="mt-2"><KatexInline math="Q' := R" /></div>
<div><KatexInline math="\texttt{return }\mathcal{A}' := \langle Q',2^{AP},\delta|_{Q'},Q_0\cap Q',F\cap Q'\rangle" /></div>
</div>

הוכיחו שבכל איטרציה המחיקה אינה משנה את שפת Büchi של האוטומט, ולכן <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}')=L_\omega(\mathcal{A})" /></span>.

<div class="mt-3 bg-rose-50 border border-rose-200 rounded p-2 text-[16px] leading-relaxed">
<span class="font-bold">שימו לב:</span> גם מצב מקבל נמחק אם אין ממנו מסלול באורך גדול מאפס למצב מקבל שנותר.
</div>

<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-2 text-[16px] leading-relaxed">
ב-<KatexInline math="\mathcal{A}'" /> מכל מצב אפשר להמשיך לריצה מקבלת.
</div>
</div>

</div>

---

<div class="space-y-3 text-right text-[18px] leading-relaxed mt-3">

<div class="bg-amber-50 border border-amber-200 rounded p-3">
<span class="font-bold">ב'. (5 נק')</span>
בנו את <span dir="ltr"><KatexInline math="\mathcal{A}_{safe}" /></span> מתוך <KatexInline math="\mathcal{A}'" /> על ידי החלפת תנאי הקבלה בקבלה טריוויאלית (כל ריצה אינסופית מתקבלת). הוכיחו ש-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{safe})=closure(P)" /></span>.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<span class="font-bold">ג'. (5 נק')</span>
בנו אוטומט החזקה <KatexInline math="\mathcal{D}" /> מעל <span dir="ltr"><KatexInline math="2^{Q'}" /></span> עבור <KatexInline math="\mathcal{A}'" /> (בנייה כקבוצת-העל, בלי תנאי קבלה), והגדירו <span dir="ltr"><KatexInline math="\mathcal{A}_{bad}" /></span> עם קבוצת קבלה <span dir="ltr"><KatexInline math="\{\emptyset\}" /></span>. הוכיחו ש-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{bad})=(2^{AP})^\omega\setminus closure(P)" /></span>.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-3">
<span class="font-bold">ד'. (5 נק')</span>
הגדירו <span dir="ltr"><KatexInline math="\mathcal{A}_{live}" /></span> כך ש-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{live})=L_\omega(\mathcal{A}')\cup L_\omega(\mathcal{A}_{bad})" /></span>. הוכיחו ש-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{live})" /></span> היא תכונת חַיּוּת, וש-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{safe})\cap L_\omega(\mathcal{A}_{live})=P" /></span>.
</div>

</div>

---

# פתרון א': אוטומט שקול אחרי מחיקות

<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-3 text-[16px] leading-relaxed text-right">
<span class="font-bold">פסאודו־קוד:</span>

<div dir="ltr" class="text-left text-[15px] leading-relaxed bg-white border border-slate-200 rounded p-2 mt-2 font-mono">
<div><KatexInline math="R := Q" /></div>
<div><KatexInline math="\texttt{repeat}" /></div>
<div class="pl-6"><KatexInline math="Dead := \{q\in R \mid \nexists\ \text{path inside }R\text{ of length }>0\text{ from }q\text{ to }F\cap R\}" /></div>
<div class="pl-6"><KatexInline math="R := R\setminus Dead" /></div>
<div><KatexInline math="\texttt{until } Dead=\emptyset" /></div>
<div class="mt-2"><KatexInline math="Q' := R" /></div>
<div><KatexInline math="\texttt{return }\mathcal{A}' := \langle Q',2^{AP},\delta|_{Q'},Q_0\cap Q',F\cap Q'\rangle" /></div>
</div>
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[15px] leading-relaxed text-right">
<span class="font-bold">טענת שימור השפה:</span> נסמן ב-<KatexInline math="\mathcal{A}_R" /> את האוטומט המושרה על <KatexInline math="R" /> בתחילת איטרציה. מחיקת <KatexInline math="Dead" /> אינה משנה את שפתו: אם ריצה של <KatexInline math="\mathcal{A}_R" /> עוברת במצב <KatexInline math="q\in Dead" />, אז מאותו רגע אין לה דרך להגיע אפילו פעם אחת נוספת למצב ב-<KatexInline math="F\cap R" />. לכן היא לא יכולה להיות ריצת Büchi מקבלת. מכאן <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_R)=L_\omega(\mathcal{A}_{R\setminus Dead})" /></span>.
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[15px] leading-relaxed text-right">
חזרה על הטיעון בכל איטרציה נותנת <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}')=L_\omega(\mathcal{A})" /></span>. בפרט, מצב מקבל אינו נשאר רק מפני שהוא מקבל: אם אין ממנו מסלול באורך גדול מאפס למצב מקבל שנותר, הוא נמחק.
</div>

---

# פתרון ב': בניית <span dir="ltr"><KatexInline math="\mathcal{A}_{safe}" /></span>

<div class="mt-1 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed" dir="ltr">
<KatexInline display math="\mathcal{A}_{safe}=\langle Q',\ 2^{AP},\ \delta|_{Q'},\ Q_0\cap Q',\ Q'\rangle" />
</div>

<div class="text-right text-[14px] text-gray-600 -mt-1">
(<KatexInline math="\delta|_{Q'}" />: המעברים של <KatexInline math="\mathcal{A}'" />; קבלה <span dir="ltr"><KatexInline math="F_{safe}=Q'" /></span>, כלומר <span class="font-bold">כל</span> ריצה אינסופית בתוך <KatexInline math="Q'" /> מתקבלת.)
</div>

<div v-click class="mt-2 bg-amber-50 border border-amber-200 rounded p-2 text-[14px] leading-relaxed text-right">
<span class="font-bold"><KatexInline math="\subseteq" />:</span> אם ל-<KatexInline math="\sigma" /> יש ריצה של <KatexInline math="\mathcal{A}_{safe}" />, אז לכל קידומת <KatexInline math="\rho\preceq\sigma" /> המצב בסופה נמצא ב-<KatexInline math="Q'" />. מנקודת השבת של האלגוריתם אפשר להמשיך ממנו למסלול שמגיע למצב מקבל של <KatexInline math="\mathcal{A}'" />, ומשם שוב להמשיך כך, אינסוף פעמים. לכן יש ל-<KatexInline math="\rho" /> המשך ב-<KatexInline math="P" />, ומכאן <span dir="ltr"><KatexInline math="\sigma\in closure(P)" /></span>.
</div>

<div v-click class="mt-2 bg-emerald-50 border border-emerald-200 rounded p-2 text-[14px] leading-relaxed text-right">
<span class="font-bold"><KatexInline math="\supseteq" />:</span> אם <span dir="ltr"><KatexInline math="\sigma\in closure(P)" /></span>, אז לכל אורך <KatexInline math="n" /> יש ל-<KatexInline math="\sigma[0..n]" /> המשך שמתקבל ב-<KatexInline math="\mathcal{A}'" />. לכן קיימת ריצה סופית של <KatexInline math="\mathcal{A}'" /> על <KatexInline math="\sigma[0..n]" />. מכיוון שמספר המצבים סופי, אפשר לבחור מצב ראשון שמופיע בתחילת אינסוף ריצות כאלה, אחריו יורש שמופיע באינסוף מהריצות שנותרו, וכן הלאה. הבחירות האלו מגדירות ריצה אינסופית של <span dir="ltr"><KatexInline math="\mathcal{A}_{safe}" /></span> על <KatexInline math="\sigma" />.
</div>

---

# פתרון ג': בניית <span dir="ltr"><KatexInline math="\mathcal{A}_{bad}" /></span> (אוטומט החזקה)

<div class="mt-1 bg-slate-50 border border-slate-200 rounded p-2 text-[14px] leading-relaxed" dir="ltr">
<KatexInline display math="\mathcal{D}=\langle 2^{Q'},\ 2^{AP},\ \delta_\mathcal{D},\ \{Q_0\cap Q'\}\rangle,\qquad \delta_\mathcal{D}(S,a)=\textstyle\bigcup_{q\in S}\delta|_{Q'}(q,a)" />
</div>

<div class="text-right text-[13px] text-gray-600 -mt-1">
(בנייה דטרמיניסטית סטנדרטית של "כל המצבים האפשריים", בלי תנאי קבלה, רק עקיבת מעברים.)
</div>

<div class="mt-2 bg-amber-50 border border-amber-200 rounded p-2 text-[14px] leading-relaxed" dir="ltr">
<KatexInline display math="\mathcal{A}_{bad}=\langle 2^{Q'},\ 2^{AP},\ \delta_\mathcal{D},\ \{Q_0\cap Q'\},\ \{\emptyset\}\rangle" />
</div>

<div v-click class="mt-2 bg-emerald-50 border border-emerald-200 rounded p-2 text-[14px] leading-relaxed text-right">
המצב <KatexInline math="\emptyset" /> לכוד: אם אין כרגע אף ריצה אפשרית של <KatexInline math="\mathcal{A}'" />, גם בהמשך לא תהיה ריצה כזו. לכן "ביקור אחד" ב-<KatexInline math="\emptyset" /> שווה ל"ביקור אינסוף פעמים", וזה מתאים בדיוק לתנאי Büchi.
</div>

<div v-click class="mt-2 bg-blue-50 border border-blue-200 rounded p-2 text-[14px] leading-relaxed text-right">
<KatexInline math="\sigma" /> מתקבלת ע"י <span dir="ltr"><KatexInline math="\mathcal{A}_{bad}" /></span> אם ורק אם הריצה הדטרמיניסטית של <KatexInline math="\mathcal{D}" /> על <KatexInline math="\sigma" /> מגיעה אי-פעם ל-<KatexInline math="\emptyset" />, כלומר אם ורק אם יש קידומת שאין עליה אף ריצה של <KatexInline math="\mathcal{A}'" />. לפי סעיף ב', זה שקול לכך של-<KatexInline math="\sigma" /> יש קידומת רעה, ולכן <span dir="ltr"><KatexInline math="\sigma\notin closure(P)" /></span>.
</div>

---

# פתרון ד': <span dir="ltr"><KatexInline math="\mathcal{A}_{live}" /></span> וסגירת המעגל

<div class="mt-1 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A}_{live})=L_\omega(\mathcal{A}')\cup L_\omega(\mathcal{A}_{bad})" />
</div>

<div class="text-right text-[13px] text-gray-600 -mt-1">
מכיוון ש-<KatexInline math="\mathcal{A}'" /> שקול ל-<KatexInline math="\mathcal{A}" />, נקבל <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{live})=P\cup\big((2^{AP})^\omega\setminus closure(P)\big)" /></span>.
</div>

<div v-click class="mt-2 bg-amber-50 border border-amber-200 rounded p-2 text-[14px] leading-relaxed text-right">
<span class="font-bold">חַיּוּת:</span> לכל מילה סופית <KatexInline math="\rho" />: אם יש לה המשך ב-<KatexInline math="P" />, סיימנו. אחרת <KatexInline math="\rho" /> עצמה קידומת רעה, ואז <span class="font-bold">כל</span> המשך שלה אינו בסגירה, כלומר נמצא ב-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{bad})" /></span>. כך או כך יש המשך ב-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{live})" /></span>; זו בדיוק הגדרת תכונת חַיּוּת.
</div>

<div v-click class="mt-2 bg-emerald-50 border border-emerald-200 rounded p-2 text-[14px] leading-relaxed text-right">
<span class="font-bold">החיתוך:</span> <KatexInline math="P\subseteq L_\omega(\mathcal{A}_{safe})" /> כי <KatexInline math="\mathcal{A}'" /> שקול ל-<KatexInline math="\mathcal{A}" /> וריצותיו הן בתוך <KatexInline math="Q'" />, ו-<KatexInline math="P\subseteq L_\omega(\mathcal{A}_{live})" /> בבירור. לכן <KatexInline math="P" /> מוכל בחיתוך. ולהפך: מילה בחיתוך שייכת ל-<KatexInline math="closure(P)" />, ולפי סעיף ג' היא <span class="font-bold">אינה</span> ב-<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{bad})" /></span>, כך שמ-<KatexInline math="L_\omega(\mathcal{A}_{live})" /> נשאר רק <KatexInline math="P" />.
</div>

---

# מסקנה: הפירוק נשאר בתוך שפות <span dir="ltr"><KatexInline math="\omega" /></span>-רגולריות

<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[18px] leading-relaxed text-right">
אם <KatexInline math="P" /> היא שפה <KatexInline math="\omega" />-רגולרית, אז קיימות שפות <KatexInline math="\omega" />-רגולריות <KatexInline math="P_{safe}" /> ו-<KatexInline math="P_{live}" /> כך ש:
</div>

<div class="mt-4 text-center text-[24px]" dir="ltr">
<KatexInline display math="P=P_{safe}\cap P_{live}" />
</div>

<div v-click class="mt-4 bg-blue-50 border border-blue-200 rounded p-3 text-[17px] leading-relaxed text-right">
הסיבה היא בנייתית: אם <KatexInline math="P=L_\omega(\mathcal{A})" />, אז הפרוצדורה בסעיף א' נותנת אוטומט שקול <KatexInline math="\mathcal{A}'" />. ממנו בנינו בפועל שני אוטומטי Büchi סופיים, ולכן שתי השפות שהתקבלו הן <KatexInline math="\omega" />-רגולריות.
</div>

<div v-click class="mt-4 grid grid-cols-2 gap-3 text-[15px] leading-relaxed">
  <div class="bg-amber-50 border border-amber-200 rounded p-3 text-right">
    <div class="font-bold mb-2">רכיב הבטיחות</div>
    <div dir="ltr" class="text-left">
      <KatexInline display math="P_{safe}=L_\omega(\mathcal{A}_{safe})=closure(P)" />
    </div>
    <div class="text-right">
      את <KatexInline math="\mathcal{A}_{safe}" /> מקבלים מ-<KatexInline math="\mathcal{A}'" /> על ידי קבלה טריוויאלית.
    </div>
  </div>

  <div class="bg-sky-50 border border-sky-200 rounded p-3 text-right">
    <div class="font-bold mb-2">רכיב החַיּוּת</div>
    <div dir="ltr" class="text-left">
      <KatexInline display math="P_{live}=L_\omega(\mathcal{A}_{live})=P\cup\big((2^{AP})^\omega\setminus closure(P)\big)" />
    </div>
    <div class="text-right">
      את <KatexInline math="\mathcal{A}_{live}" /> מקבלים מאיחוד השפות של <KatexInline math="\mathcal{A}'" /> ושל <KatexInline math="\mathcal{A}_{bad}" />.
    </div>
  </div>
</div>

<div v-click class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-[16px] leading-relaxed text-right">
דוגמת בנייה: עבור כל אוטומט Büchi נתון ל-<KatexInline math="P" />, מחשבים <KatexInline math="\mathcal{A}'" />, מחליפים את קבלת <KatexInline math="\mathcal{A}'" /> ב-<KatexInline math="Q'" /> כדי לקבל <KatexInline math="\mathcal{A}_{safe}" />, ובונים אוטומט החזקה שמקבל הגעה ל-<KatexInline math="\emptyset" /> כדי לקבל את <KatexInline math="\mathcal{A}_{bad}" />. מכאן מתקבל <KatexInline math="\mathcal{A}_{live}" />.
</div>

---

# דוגמה פתורה: המחיקה ו-<span dir="ltr"><KatexInline math="\mathcal{A}'" /></span>

<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed text-right">
המצבים המקבלים הם <KatexInline math="q_1,q_2,q_3" />. השרשרת התחתונה בנויה כך שנדרשות שתי איטרציות מחיקה.
</div>

<div class="mt-2 grid grid-cols-[1.35fr_0.95fr] gap-2">
  <div class="bg-white border border-slate-200 rounded p-2">
    <div class="text-center font-bold mb-1" dir="ltr"><KatexInline math="\mathcal{A}" /></div>
    <AutomatonD3 variant="classic" :width="540" :height="225" :arrowSize="3.1" :stateLabelFontSize="13" :transitionLabelFontSize="10.5"
      :states="[
        { id: 'q0', label: '$q_0$', initial: true, initialDirection: 'left', x: 58, y: 65, r: 19, labelWidth: 42 },
        { id: 'q1', label: '$q_1$', x: 205, y: 65, r: 19, labelWidth: 42, accepting: true, fill: '#d1fae5', stroke: '#059669' },
        { id: 'q2', label: '$q_2$', x: 145, y: 152, r: 17, labelWidth: 42, accepting: true, fill: '#fee2e2', stroke: '#dc2626' },
        { id: 'q3', label: '$q_3$', x: 250, y: 152, r: 17, labelWidth: 42, accepting: true, fill: '#fee2e2', stroke: '#dc2626' },
        { id: 'q4', label: '$q_4$', x: 355, y: 152, r: 17, labelWidth: 42, fill: '#fee2e2', stroke: '#dc2626' },
        { id: 'q5', label: '$q_5$', x: 460, y: 152, r: 17, labelWidth: 42, fill: '#fee2e2', stroke: '#dc2626' },
      ]"
      :transitions="[
        { source: 'q0', target: 'q0', label: '$a\\Rightarrow b$', loopDirection: '-90deg', labelY: -8, labelWidth: 78 },
        { source: 'q0', target: 'q1', label: '$true$', labelY: -10, labelWidth: 52 },
        { source: 'q1', target: 'q1', label: '$b$', loopDirection: '-90deg', labelY: -8, labelWidth: 36 },
        { source: 'q0', labelX:-12, target: 'q2', label: '$true$', curve: 0.08, labelY: 10, stroke: '#dc2626', labelColor: '#dc2626', labelWidth: 52 },
        { source: 'q2', labelY:-12, target: 'q3', label: '$true$', stroke: '#dc2626', labelColor: '#dc2626', labelWidth: 52 },
        { source: 'q3', labelY:-12, target: 'q4', label: '$true$', stroke: '#dc2626', labelColor: '#dc2626', labelWidth: 52 },
        { source: 'q4', labelY: -28, target: 'q5', label: '$true$', stroke: '#dc2626', labelColor: '#dc2626', labelWidth: 52 },
        { source: 'q5', target: 'q4', label: '$true$', curve: 0.28, labelY: 28, stroke: '#dc2626', labelColor: '#dc2626', labelWidth: 52 },
      ]"
    />
  </div>

  <div class="bg-white border border-slate-200 rounded p-2">
    <div class="text-center font-bold mb-1" dir="ltr"><KatexInline math="\mathcal{A}'" /></div>
    <AutomatonD3 variant="classic" :width="315" :height="225" :arrowSize="3.1" :stateLabelFontSize="13" :transitionLabelFontSize="10.5"
      :states="[
        { id: 'q0', label: '$q_0$', initial: true, initialDirection: 'left', x: 65, y: 85, r: 19, labelWidth: 42 },
        { id: 'q1', label: '$q_1$', x: 220, y: 85, r: 19, labelWidth: 42, accepting: true, fill: '#d1fae5', stroke: '#059669' },
      ]"
      :transitions="[
        { source: 'q0', target: 'q0', label: '$a\\Rightarrow b$', loopDirection: '-90deg', labelY: -8, labelWidth: 78 },
        { source: 'q0', target: 'q1', label: '$true$', labelY: -10, labelWidth: 52 },
        { source: 'q1', target: 'q1', label: '$b$', loopDirection: '-90deg', labelY: -8, labelWidth: 36 },
      ]"
    />
    <div class="text-center text-[14px] text-red-700 -mt-2">
      <KatexInline math="q_3,q_4,q_5" /> נמחקים תחילה; אחר כך <KatexInline math="q_2" />.
    </div>
  </div>
</div>

---

# דוגמה פתורה: אוטומט החזקה ל-<span dir="ltr"><KatexInline math="\mathcal{A}_{bad}" /></span>

<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed text-right">
אחרי המחיקה עובדים עם <KatexInline math="\mathcal{A}'" /> בלבד. אוטומט ההחזקה עוקב אחרי קבוצת המצבים האפשריים ב-<KatexInline math="\mathcal{A}'" />, ומקבל כאשר מגיעים ל-<KatexInline math="\emptyset" />.
</div>

<div class="mt-2 bg-white border border-slate-200 rounded p-2">
<AutomatonD3 variant="classic" :width="900" :height="280" :arrowSize="3.5" :stateLabelFontSize="15" :transitionLabelFontSize="12"
  :states="[
    { id: 'q0set', label: '$\\{q_0\\}$', initial: true, initialDirection: 'left', x: 120, y: 130, rx: 42, ry: 26, labelWidth: 90 },
    { id: 'both', label: '$\\{q_0,q_1\\}$', x: 360, y: 80, rx: 58, ry: 28, labelWidth: 125 },
    { id: 'q1set', label: '$\\{q_1\\}$', x: 360, y: 195, rx: 42, ry: 26, labelWidth: 90 },
    { id: 'empty', label: '$\\emptyset$', x: 650, y: 195, rx: 42, ry: 26, labelWidth: 90, accepting: true, fill: '#fee2e2', stroke: '#dc2626' },
  ]"
  :transitions="[
    { source: 'q0set', target: 'both', label: '$a\\Rightarrow b$', curve: -0.15, labelY: -10, labelWidth: 78 },
    { source: 'q0set', target: 'q1set', label: '$\\neg(a\\Rightarrow b)$', curve: 0.15, labelY: 14, labelWidth: 112 },
    { source: 'both', target: 'both', label: '$a\\Rightarrow b$', loopDirection: '-90deg', labelY: -10, labelWidth: 78 },
    { source: 'both', target: 'q1set', label: '$\\neg(a\\Rightarrow b)$', curve: 0.12, labelX: 72, labelWidth: 112 },
    { source: 'q1set', target: 'q1set', label: '$b$', loopDirection: '90deg', labelY: 10, labelWidth: 36 },
    { source: 'q1set', target: 'empty', label: '$\\neg b$', labelY: -10, labelWidth: 52 },
    { source: 'empty', target: 'empty', label: '$true$', loopDirection: '90deg', labelY: 10, labelWidth: 52 },
  ]"
/>
</div>

---

# דוגמה פתורה: אוטומטי המטרה

<div class="mt-2 grid grid-cols-2 gap-3">
  <div class="bg-white border border-amber-200 rounded p-2">
    <div class="text-center font-bold mb-1">
      <span dir="ltr"><KatexInline math="\mathcal{A}_{safe}" /></span>
    </div>
    <AutomatonD3 variant="classic" :width="440" :height="230" :arrowSize="3.3" :stateLabelFontSize="14" :transitionLabelFontSize="11"
      :states="[
        { id: 's0', label: '$q_0$', initial: true, initialDirection: 'left', x: 95, y: 105, r: 21, labelWidth: 46, accepting: true },
        { id: 's1', label: '$q_1$', x: 300, y: 105, r: 21, labelWidth: 46, accepting: true },
      ]"
      :transitions="[
        { source: 's0', target: 's0', label: '$a\\Rightarrow b$', loopDirection: '-90deg', labelY: -8, labelWidth: 78 },
        { source: 's0', target: 's1', label: '$true$', labelY: -10, labelWidth: 52 },
        { source: 's1', target: 's1', label: '$b$', loopDirection: '-90deg', labelY: -8, labelWidth: 36 },
      ]"
    />
    <div class="text-right text-[14px] leading-relaxed -mt-2">
      זהו <KatexInline math="\mathcal{A}'" /> עם קבלה טריוויאלית: שני המצבים מקבלים.
    </div>
  </div>

  <div class="bg-white border border-sky-200 rounded p-2 min-h-[360px]">
    <div class="text-center font-bold mb-1">
      <span dir="ltr"><KatexInline math="\mathcal{A}_{live}" /></span>
    </div>
    <div class="text-right text-[14px] leading-relaxed mb-3">
      שפת האיחוד: רכיב אחד הוא <KatexInline math="\mathcal{A}'" />, והרכיב השני הוא <KatexInline math="\mathcal{A}_{bad}" />.
    </div>
    <AutomatonD3 variant="classic" :width="390" :height="245" :arrowSize="2.4" :stateLabelFontSize="9.5" :transitionLabelFontSize="8.5"
      :states="[
        { id: 'l0', label: '$q_0$', initial: true, initialDirection: 'left', x: 62, y: 62, r: 14, labelWidth: 36 },
        { id: 'l1', label: '$q_1$', x: 155, y: 62, r: 14, labelWidth: 36, accepting: true },
        { id: 'p0', label: '$\\{q_0\\}$', initial: true, initialDirection: 'left', x: 58, y: 178, rx: 27, ry: 16, labelWidth: 66 },
        { id: 'p01', label: '$\\{q_0,q_1\\}$', x: 165, y: 148, rx: 37, ry: 17, labelWidth: 90 },
        { id: 'p1', label: '$\\{q_1\\}$', x: 165, y: 215, rx: 27, ry: 16, labelWidth: 66 },
        { id: 'pe', label: '$\\emptyset$', x: 305, y: 215, rx: 27, ry: 16, labelWidth: 66, accepting: true },
      ]"
      :transitions="[
        { source: 'l0', target: 'l0', label: '$a\\Rightarrow b$', loopDirection: '-90deg', labelY: -6, labelWidth: 68 },
        { source: 'l0', target: 'l1', label: '$true$', labelY: -8, labelWidth: 42 },
        { source: 'l1', target: 'l1', label: '$b$', loopDirection: '-90deg', labelY: -6, labelWidth: 28 },
        { source: 'p0', target: 'p01', label: '$a\\Rightarrow b$', curve: -0.12, labelY: -8, labelWidth: 68 },
        { source: 'p0', target: 'p1', label: '$\\neg(a\\Rightarrow b)$', curve: 0.12, labelY: 10, labelWidth: 86 },
        { source: 'p01', target: 'p01', label: '$a\\Rightarrow b$', loopDirection: '-90deg', labelY: -6, labelWidth: 68 },
        { source: 'p01', target: 'p1', label: '$\\neg(a\\Rightarrow b)$', curve: 0.12, labelX: 45, labelWidth: 86 },
        { source: 'p1', target: 'p1', label: '$b$', loopDirection: '90deg', labelY: 8, labelWidth: 28 },
        { source: 'p1', target: 'pe', label: '$\\neg b$', labelY: -8, labelWidth: 42 },
        { source: 'pe', target: 'pe', label: '$true$', loopDirection: '90deg', labelY: 8, labelWidth: 42 },
      ]"
    />
  </div>
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed text-right">
בדוגמה זו מתקיים <span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_{safe})\cap L_\omega(\mathcal{A}_{live})=L_\omega(\mathcal{A})" /></span>.
</div>

---

# שאלה: מעבר מ-LTL ל-QPTL (25 נק')

<div class="text-right text-[17px] leading-relaxed mt-3">
נניח <KatexInline math="AP=\{p\}" /> ונתבונן בשפת המילים שבהן <KatexInline math="p" /> מופיע מספר סופי וזוגי של פעמים:
</div>

<div class="mt-3 text-center text-[20px]" dir="ltr">
<KatexInline display math="L_{\mathrm{even}}=\{\sigma\in(2^{\{p\}})^\omega\mid |\{i\in\mathbb{N}\mid p\in\sigma[i]\}|\in 2\mathbb{N}\}" />
</div>

<div class="mt-4 bg-amber-50 border border-amber-200 rounded p-3 text-[16px] leading-relaxed text-right">
קבלו ללא הוכחה: אין נוסחת <span dir="ltr">LTL</span> שמתארת את <KatexInline math="L_{\mathrm{even}}" />.
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed text-right">
בשאלה זו נגדיר <span dir="ltr">QPTL</span> כהרחבה של <span dir="ltr">LTL</span> שבה מותר לכמת על פסוקים אטומיים. למשל, <KatexInline math="\exists q.\varphi" /> אומר שקיימת השמה של אמת/שקר לאורך כל המילה עבור פסוק חדש <KatexInline math="q" />, כך שהנוסחה <KatexInline math="\varphi" /> מתקיימת.
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed text-right">
הסבירו איך ההרחבה הזו מאפשרת לעקוף את מגבלת הביטוי של <span dir="ltr">LTL</span>. כתבו נוסחת <span dir="ltr">QPTL</span> עבור <KatexInline math="L_{\mathrm{even}}" />. בנוסף, הוכיחו שכל תכונה אומגה-רגולרית ניתנת לביטוי באמצעות <span dir="ltr">QPTL</span>.
</div>

---

# פתרון: מעבר מ-LTL ל-QPTL

<div class="text-right text-[16px] leading-relaxed mt-3">
ב-<span dir="ltr">QPTL</span> מותר לכמת על פסוק אטומי חדש <KatexInline math="q" />. נשתמש בו כזיכרון: <KatexInline math="q" /> אמת במקום הנוכחי אם מספר מופעי <KatexInline math="p" /> עד לפני המקום הזה זוגי.
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[16px] leading-relaxed text-right">
המעבר מעדכן את הזוגיות: אם <KatexInline math="p" /> מתקיים עכשיו, הערך של <KatexInline math="q" /> מתהפך בצעד הבא; אחרת הוא נשאר כפי שהיה.
</div>

<div class="mt-3 text-center text-[18px]" dir="ltr">
<KatexInline display math="\exists q.\ q\ \land\ \Box\bigl(Xq\leftrightarrow(q\leftrightarrow\neg p)\bigr)\ \land\ \Diamond(q\land\Box\neg p)" />
</div>

<div class="mt-3 grid grid-cols-2 gap-3 text-[15px] leading-relaxed">
  <div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-right">
    <div class="font-bold mb-1">מה הנוסחה דורשת?</div>
    <div><KatexInline math="q" /> מתחיל כזוגי, מתעדכן לפי <KatexInline math="p" />, ובסוף <KatexInline math="p" /> מפסיק להופיע.</div>
  </div>
  <div class="bg-blue-50 border border-blue-200 rounded p-3 text-right">
    <div class="font-bold mb-1">למה זה עוקף את LTL?</div>
    <div>הפסוק <KatexInline math="q" /> מסמן לאורך המילה זיכרון שאינו חלק מ-<KatexInline math="AP" />. הכימות עליו מאפשר לתאר את מצב הזוגיות.</div>
  </div>
</div>

---

# פתרון: כל אומגה-רגולרית היא QPTL

<div class="text-right text-[16px] leading-relaxed mt-3">
תהי <KatexInline math="P" /> תכונה אומגה-רגולרית. קיים אוטומט Büchi <span dir="ltr"><KatexInline math="\mathcal{A}=\langle Q,\Sigma,\delta,Q_0,F\rangle" /></span> כך ש-<span dir="ltr"><KatexInline math="P=L_\omega(\mathcal{A})" /></span>.
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed text-right">
ב-<span dir="ltr">QPTL</span> נכמת פסוק עזר <KatexInline math="r_q" /> לכל מצב <KatexInline math="q\in Q" />. המשמעות: בזמן <KatexInline math="i" />, בדיוק אחד מהפסוקים <KatexInline math="r_q" /> נכון, והוא מציין באיזה מצב נמצאת הריצה.
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[15px] leading-relaxed text-right">
הנוסחה דורשת: מצב התחלתי בזמן <KatexInline math="0" />, בדיוק מצב אחד בכל רגע, כל מעבר מתאים לאות הנקראת, ומצב מקבל מופיע אינסוף פעמים:
</div>

<div class="mt-2 text-center text-[17px]" dir="ltr">
<KatexInline display math="\exists (r_q)_{q\in Q}.\ \mathrm{Init}\land\Box\mathrm{One}\land\Box\mathrm{Step}\land\Box\Diamond\bigvee_{q\in F} r_q" />
</div>

<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[16px] leading-relaxed text-right">
לכן נוסחת <span dir="ltr">QPTL</span> אומרת בדיוק: קיימת ריצה מקבלת של <KatexInline math="\mathcal{A}" /> על המילה. זו בדיוק ההגדרה של קבלה על ידי אוטומט Büchi, ולכן כל תכונה אומגה-רגולרית ניתנת לביטוי ב-<span dir="ltr">QPTL</span>.
</div>

---

# שאלה: טופולוגיה של בטיחות וחַיּוּת (20 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
נסמן <KatexInline math="\Sigma=2^{AP}" />. עבור שתי מילים אינסופיות <span dir="ltr"><KatexInline math="\sigma,\tau\in\Sigma^\omega" /></span>, נגדיר:
</div>

<div class="mt-4 text-center text-[23px]" dir="ltr">
<KatexInline display math="d(\sigma,\tau)=
\begin{cases}
0 & \sigma=\tau\\
2^{-n} & n=\min\{i\ge 0\mid \sigma_i\ne\tau_i\}
\end{cases}" />
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[17px] leading-relaxed text-right">
כלומר, ככל שהרישא המשותפת ארוכה יותר, המרחק קטן יותר.
</div>

<div class="mt-4 space-y-3 text-right text-[17px] leading-relaxed">
<div class="bg-slate-50 border border-slate-200 rounded p-3">
<span class="font-bold">א'.</span>
הראו ש-<KatexInline math="d" /> היא מטריקה על <KatexInline math="\Sigma^\omega" />.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-3">
<span class="font-bold">ב'.</span>
הוכיחו: <KatexInline math="P\subseteq\Sigma^\omega" /> היא תכונת בטיחות אם ורק אם <KatexInline math="P" /> סגורה ביחס למטריקה <KatexInline math="d" />.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<span class="font-bold">ג'.</span>
נאמר ש-<KatexInline math="P" /> צפופה אם לכל <KatexInline math="\sigma\in\Sigma^\omega" /> ולכל <KatexInline math="\varepsilon>0" /> קיימת <KatexInline math="\tau\in P" /> כך ש-<KatexInline math="d(\sigma,\tau)<\varepsilon" />. הוכיחו: <KatexInline math="P" /> היא תכונת חַיּוּת אם ורק אם <KatexInline math="P" /> צפופה.
</div>
</div>

---

# שאלה: יישום לקידוד עשרוני

<div class="text-right text-[16px] leading-relaxed mt-2">
נניח <KatexInline math="AP=\{p_0,\ldots,p_8\}" />. לכל אות <KatexInline math="A\in2^{AP}" /> נתאים ספרה <KatexInline math="|A|\in\{0,\ldots,9\}" />. עבור מילה <KatexInline math="\sigma" /> נגדיר <KatexInline math="d_i=|\sigma[i]|" />:
</div>

<div class="mt-1 text-center text-[16px]" dir="ltr">
<KatexInline display math="x_\sigma=0.d_0d_1d_2\cdots=\sum_{i=0}^{\infty} d_i\cdot 10^{-(i+1)}" />
</div>

<div class="mt-2 bg-blue-50 border border-blue-200 rounded p-2 text-[16px] leading-relaxed text-right">
עבור כל אחת מהקבוצות הבאות, קבעו האם התכונה <KatexInline math="\{\sigma\mid x_\sigma\in S\}" /> היא בטיחות, חַיּוּת, שתיהן, או אף אחת מהן:
</div>

<div class="mt-4 ml-auto w-[94%] grid grid-cols-2 gap-x-8 gap-y-2 text-[15px] leading-normal" dir="ltr">
  <div class="grid grid-cols-[48px_1fr] items-center gap-x-3 gap-y-2">
    <div><KatexInline math="S_1" /></div><div><KatexInline math="[0,\tfrac12]" /></div>
    <div><KatexInline math="S_2" /></div><div><KatexInline math="(0,1)" /></div>
    <div><KatexInline math="S_3" /></div><div><KatexInline math="[0,\tfrac12]\cup(\tfrac34,1)" /></div>
    <div><KatexInline math="S_4" /></div><div><KatexInline math="[\tfrac14,\tfrac34)" /></div>
  </div>

  <div class="grid grid-cols-[48px_1fr] items-center gap-x-3 gap-y-2">
    <div><KatexInline math="S_5" /></div><div><KatexInline math="\{x\mid \text{some digit of }x\text{ is }7\}" /></div>
    <div><KatexInline math="S_6" /></div><div><KatexInline math="\{x\mid \text{infinitely many digits of }x\text{ are }7\}" /></div>
    <div><KatexInline math="S_7" /></div><div><KatexInline math="\emptyset" /></div>
    <div><KatexInline math="S_8" /></div><div><KatexInline math="[0,1]" /></div>
    <div><KatexInline math="S_9" /></div><div><KatexInline math="[0,1]\cap\mathbb{Q}" /></div>
  </div>
</div>

---

# פתרון: סגור וצפוף

<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-3 text-[16px] leading-relaxed text-right">
זו מטריקה: אי-שליליות וסימטריה מיידיות, ו-<KatexInline math="d(\sigma,\tau)=0" /> רק כאשר <KatexInline math="\sigma=\tau" />. בנוסף מתקיים אי-שוויון חזק יותר מהמשולש: אם <KatexInline math="\sigma" /> ו-<KatexInline math="\tau" /> מסכימות עם <KatexInline math="\eta" /> על רישא ארוכה, אז גם <KatexInline math="\sigma" /> ו-<KatexInline math="\tau" /> מסכימות לפחות עד המינימום מבין שתי הרישות האלה. לכן <span dir="ltr"><KatexInline math="d(\sigma,\tau)\le\max(d(\sigma,\eta),d(\eta,\tau))" /></span>.
</div>

<div class="mt-2 bg-amber-50 border border-amber-200 rounded p-3 text-[16px] leading-relaxed text-right">
כדור פתוח סביב מילה <KatexInline math="\sigma" /> הוא אוסף כל המילים שקרובות מספיק ל-<KatexInline math="\sigma" />. במטריקה הזו, להיות קרוב מספיק פירושו להסכים עם <KatexInline math="\sigma" /> על רישא ארוכה מספיק. למשל, כדור קטן מרדיוס <KatexInline math="2^{-n}" /> מכיל רק מילים שמסכימות עם <KatexInline math="\sigma" /> על <KatexInline math="n" /> האותיות הראשונות.
</div>

<div v-click class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed text-right">
<span class="font-bold">בטיחות:</span> אם <KatexInline math="P" /> סגורה ו-<KatexInline math="\sigma\notin P" />, אז המשלים פתוח. לכן קיים כדור פתוח <KatexInline math="B(\sigma,\varepsilon)" /> שמוכל כולו במשלים. נבחר רישא <KatexInline math="\rho" /> של <KatexInline math="\sigma" /> ארוכה מספיק כך שכל מילה שמתחילה ב-<KatexInline math="\rho" /> נמצאת בכדור הזה. לכן כל המשך של <KatexInline math="\rho" /> מחוץ ל-<KatexInline math="P" />, כלומר <KatexInline math="\rho" /> קידומת רעה. להפך, אם לכל <KatexInline math="\sigma\notin P" /> יש רישא רעה, אז סביב <KatexInline math="\sigma" /> יש כדור שמוכל במשלים, ולכן המשלים פתוח ו-<KatexInline math="P" /> סגורה.
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[16px] leading-relaxed text-right">
<span class="font-bold">חַיּוּת:</span> לפי ההגדרה הטופולוגית, <KatexInline math="P" /> צפופה אם ורק אם כל כדור פתוח מכיל נקודה מתוך <KatexInline math="P" />. לכן, לכל רישא סופית <KatexInline math="\rho" />, ניקח מילה כלשהי <KatexInline math="\sigma" /> שמתחילה ב-<KatexInline math="\rho" /> וכדור קטן מספיק סביב <KatexInline math="\sigma" /> שמכריח את הרישא <KatexInline math="\rho" />. הצפיפות נותנת מילה ב-<KatexInline math="P" /> בתוך הכדור, ולכן יש המשך <KatexInline math="\rho\eta\in P" />. להפך, אם לכל <KatexInline math="\rho" /> יש המשך כזה, אז כל כדור פתוח מכיל מילים עם רישא סופית מסוימת, ואחת מהן נמצאת ב-<KatexInline math="P" />. לכן <KatexInline math="P" /> צפופה.
</div>

---

# פתרון: הקידוד העשרוני

<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-2 text-[14px] leading-relaxed text-right">
רישא משותפת באורך <KatexInline math="n" /> גוררת אותן <KatexInline math="n" /> ספרות ראשונות, ולכן <span dir="ltr"><KatexInline math="|x_\sigma-x_\tau|\le 10^{-n}" /></span>. הסיווג נעשה לפי סגירות וצפיפות בטופולוגיית הרישות.
</div>

<div v-click class="mt-3 grid grid-cols-2 gap-2 text-[13.5px] leading-relaxed">
  <div class="bg-amber-50 border border-amber-200 rounded p-2 text-right">
    <div class="font-bold mb-1">בטיחות</div>
    <div><KatexInline math="S_1=[0,\frac12]" /></div>
    <div><KatexInline math="S_7=\emptyset" /></div>
    <div><KatexInline math="S_8=[0,1]" /></div>
  </div>

  <div class="bg-emerald-50 border border-emerald-200 rounded p-2 text-right">
    <div class="font-bold mb-1">חַיּוּת</div>
    <div><KatexInline math="S_2=(0,1)" /></div>
    <div><KatexInline math="S_5" />: מופיעה ספרה <KatexInline math="7" /></div>
    <div><KatexInline math="S_6" />: אינסוף ספרות <KatexInline math="7" /></div>
    <div><KatexInline math="S_9=[0,1]\cap\mathbb{Q}" /></div>
    <div><KatexInline math="S_8=[0,1]" /></div>
  </div>
</div>

<div v-click class="mt-2 grid grid-cols-2 gap-2 text-[13.5px] leading-relaxed">
  <div class="bg-blue-50 border border-blue-200 rounded p-2 text-right">
    <div class="font-bold mb-1">אף אחת</div>
    <div><KatexInline math="S_3=[0,\frac12]\cup(\frac34,1)" /> ו-<KatexInline math="S_4=[\frac14,\frac34)" /> אינן סגורות ואינן צפופות.</div>
  </div>

  <div class="bg-slate-50 border border-slate-200 rounded p-2 text-right">
    <div class="font-bold mb-1">שתיהן</div>
    <div><KatexInline math="S_8=[0,1]" /></div>
  </div>
</div>

---
class: text-center
---

# פרק: שאלות הכנה למבחן

<div class="mt-10 text-[20px] text-slate-600">
שאלות מייצגות מכל אחד מהנושאים שנלמדו בקורס — מעבר על גרפי תוכנית ושזירה, מערכות תקשורת, קידוד סימבולי, התפוצצות מצבים ומבוי סתום, אינוריאנטים, בדיקת תכונות בטיחות רגולריות, ואוטומטי <span dir="ltr">Büchi</span> דטרמיניסטיים.
</div>

---

# שאלה: שזירה של שני גרפי תוכנית (15 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
נתונים שני גרפי תוכנית על משתנה משותף <span dir="ltr"><KatexInline math="x" /></span>, מאותחל ב-<span dir="ltr"><KatexInline math="x=1" /></span>:
</div>

<div class="mt-4 grid grid-cols-2 gap-5 text-[17px]">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900 text-right">
<div class="font-bold mb-1"><span dir="ltr">PG₁</span> (תהליך <span dir="ltr">A</span>)</div>
<span dir="ltr"><KatexInline math="l_0\xrightarrow{x:=x+1}l_1\xrightarrow{x:=x+1}l_2" /></span>
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900 text-right">
<div class="font-bold mb-1"><span dir="ltr">PG₂</span> (תהליך <span dir="ltr">B</span>)</div>
<span dir="ltr"><KatexInline math="m_0\xrightarrow{x:=2\cdot x}m_1" /></span>
</div>
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> כמה סדרי שזירה (interleavings) שונים בין שני התהליכים קיימים?<br/>
<b>ב.</b> מהם כל הערכים הסופיים האפשריים של <span dir="ltr">x</span>?<br/>
<b>ג.</b> האם <span dir="ltr"><KatexInline math="TS\models\Box(x\le 4)" /></span>?
</div>

---

# פתרון: שלוש שזירות, שלוש תוצאות

<div class="text-right text-[17px] leading-relaxed mt-3">
תהליך <span dir="ltr">A</span> מבצע 2 צעדים ותהליך <span dir="ltr">B</span> צעד 1 — <span dir="ltr"><KatexInline math="\binom{3}{1}=3" /></span> סדרי שזירה אפשריים, לפי מיקומו של צעד <span dir="ltr">B</span> ביחס לשני צעדי <span dir="ltr">A</span>:
</div>

<div class="mt-3 grid grid-cols-3 gap-3 text-[15px] text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-2 text-blue-900">
<span dir="ltr">B</span> ראשון: <span dir="ltr"><KatexInline math="1\xrightarrow{B}2\xrightarrow{A}3\xrightarrow{A}4" /></span>
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-2 text-emerald-900">
<span dir="ltr">B</span> באמצע: <span dir="ltr"><KatexInline math="1\xrightarrow{A}2\xrightarrow{B}4\xrightarrow{A}5" /></span>
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-2 text-amber-900">
<span dir="ltr">B</span> אחרון: <span dir="ltr"><KatexInline math="1\xrightarrow{A}2\xrightarrow{A}3\xrightarrow{B}6" /></span>
</div>
</div>

<div class="mt-4 bg-red-50 border-2 border-red-300 rounded p-3 text-red-900 text-center text-[17px] leading-relaxed">
הערכים הסופיים האפשריים הם <span dir="ltr"><KatexInline math="\{4,5,6\}" /></span>. מאחר שריצה אחת מגיעה ל-<span dir="ltr"><KatexInline math="x=6" /></span>, <span dir="ltr"><KatexInline math="TS\not\models\Box(x\le 4)" /></span>. כל שזירה אפשרית מוסיפה ערך אפשרי נוסף — זו ההתפוצצות (state explosion) במיניאטורה.
</div>

---

# שאלה: ערוץ חסום וקיבולת (15 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
תהליך שולח מבצע <span dir="ltr"><KatexInline math="c!v_1;\,c!v_2" /></span> ותהליך מקבל מבצע <span dir="ltr"><KatexInline math="c?x" /></span> פעם אחת, על ערוץ <span dir="ltr">c</span> בקיבולת <span dir="ltr">1</span>.
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> מה קורה לפעולת השליחה השנייה לפני שמתבצעת קבלה?<br/>
<b>ב.</b> האם המערכת חשופה למבוי סתום? מתי?<br/>
<b>ג.</b> אילו השלכות (חיוביות ושליליות) יש להחלפת הערוץ בקיבולת אינסופית?
</div>

---

# פתרון: חסימה, מבוי סתום, ומחיר הקיבולת האינסופית

<div class="grid grid-cols-3 gap-3 mt-3 text-[15px] text-right">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900">
<div class="font-bold mb-1">א. חסימה</div>
כל עוד הערוץ מלא (תוכן אחד שלא נקרא), לפעולת <span dir="ltr"><KatexInline math="c!v_2" /></span> <b>אין מעבר מאופשר</b> — התהליך השולח נחסם עד שמתבצעת קבלה שמפנה מקום.
</div>
<div class="bg-red-50 border border-red-200 rounded p-3 text-red-900">
<div class="font-bold mb-1">ב. מבוי סתום</div>
אם המקבל עצמו ממתין (למשל לאירוע מהשולח) לפני שמבצע <span dir="ltr">c?x</span>, ושני התהליכים לא מתקדמים — זה מבוי סתום: אין אף מעבר מאופשר בשום תהליך.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900">
<div class="font-bold mb-1">ג. קיבולת אינסופית</div>
<span dir="ltr">c!v₂</span> תמיד מאופשרת (אין חסימה), אך תוכן הערוץ יכול לצמוח בלי גבול — מרחב המצבים הופך <b>אינסופי</b>, ובדיקת מודלים אוטומטית מאבדת התכנות.
</div>
</div>

---

# שאלה: קידוד בוליאני של משתנה ב-SMV (10 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
משתנה <span dir="ltr">counter</span> מקבל ערכים <span dir="ltr">0..5</span> (6 ערכים), ועובר <span dir="ltr"><KatexInline math="\mathit{counter}'=(\mathit{counter}+1)\bmod 6" /></span> בכל צעד.
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> כמה ביטים בוליאניים <span dir="ltr"><KatexInline math="b_2,b_1,b_0" /></span> דרושים לקידוד בינארי ישיר?<br/>
<b>ב.</b> כתבו נוסחה בוליאנית למצב ההתחלה <span dir="ltr"><KatexInline math="\mathit{counter}=0" /></span>.<br/>
<b>ג.</b> אילו הקצאות לביטים הן "בלתי חוקיות" (לא מתאימות לאף ערך <span dir="ltr">0..5</span>), וכיצד מתייחסים אליהן?
</div>

---

# פתרון: שלושה ביטים, שתי הקצאות חסרות פשר

<div class="text-right text-[16px] leading-relaxed mt-3">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900 mb-2">
<b>א.</b> <span dir="ltr"><KatexInline math="\lceil\log_2 6\rceil=3" /></span> ביטים מספיקים (<span dir="ltr"><KatexInline math="2^3=8\ge 6" /></span>).
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900 mb-2">
<b>ב.</b> מצב התחלה: <span dir="ltr"><KatexInline math="\neg b_2\land\neg b_1\land\neg b_0" /></span> (הקידוד של <span dir="ltr">0</span>).
</div>
<div class="bg-red-50 border border-red-200 rounded p-3 text-red-900">
<b>ג.</b> ההקצאות <span dir="ltr"><KatexInline math="110" /></span> ו-<span dir="ltr"><KatexInline math="111" /></span> (כלומר <span dir="ltr"><KatexInline math="6,7" /></span>) אינן מתאימות לאף ערך של <span dir="ltr">counter</span>. הן נחשבות "לא מגיעות" (unreachable) — או מוחרגות מפורשות מהאינוריאנט הראשוני, או שמוודאים שיחס המעבר לעולם לא מוביל אליהן.
</div>
</div>

---

# שאלה: מבוי סתום והפחתת סדר חלקי (15 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
שני תהליכים, כל אחד צריך לנעול שני נעולים <span dir="ltr">A,B</span> לפני קטע קריטי. תהליך 1 נועל לפי הסדר <span dir="ltr">A</span> ואז <span dir="ltr">B</span>; תהליך 2 נועל <span dir="ltr">B</span> ואז <span dir="ltr">A</span>.
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> תארו ריצה (שזירה) שמובילה למבוי סתום.<br/>
<b>ב.</b> הציעו תיקון פשוט שמסלק את המבוי הסתום.<br/>
<b>ג.</b> הסבירו איך הפחתת סדר חלקי (POR) יכולה לדלג על חלק מהשזירות בלי לפגוע ביכולת לגלות את המבוי הסתום.
</div>

---

# פתרון: נעילה מעגלית, סדר אחיד, ו-POR

<div class="grid grid-cols-3 gap-3 mt-3 text-[14.5px] text-right leading-relaxed">
<div class="bg-red-50 border border-red-200 rounded p-3 text-red-900">
<div class="font-bold mb-1">א. הריצה החוסמת</div>
תהליך 1 נועל <span dir="ltr">A</span>, תהליך 2 נועל <span dir="ltr">B</span> (לפני שאחד מהם השלים) — כעת תהליך 1 ממתין ל-<span dir="ltr">B</span> (תפוס) ותהליך 2 ממתין ל-<span dir="ltr">A</span> (תפוס): המתנה מעגלית, אף תהליך לא מתקדם.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900">
<div class="font-bold mb-1">ב. סדר נעילה אחיד</div>
אם שני התהליכים נועלים <span dir="ltr">A</span> לפני <span dir="ltr">B</span>, לא יכולה להיווצר המתנה מעגלית — מי שמחזיק את <span dir="ltr">A</span> תמיד יקבל את <span dir="ltr">B</span> לפני שהשני מתחיל.
</div>
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900">
<div class="font-bold mb-1">ג. הפחתת סדר חלקי</div>
פעולות "נעילת המשאב הראשון" של שני התהליכים <b>תלויות</b> (מתחרות על מצב משאבים), ולכן <b>לא ניתן</b> לבחור רק נציג אחד מבין סדרי הביצוע שלהן — תנאי ה-ample set מחייב לבדוק את שתי האפשרויות בדיוק במקום שבו עלול להיווצר מבוי סתום, כך שהוא לא נסתר.
</div>
</div>

---

# שאלה: הוכחת בטיחות באמצעות אינוריאנט אינדוקטיבי (15 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
משתנה <span dir="ltr">x</span> מתחיל ב-<span dir="ltr"><KatexInline math="x=0" /></span>, ובכל צעד: אם <span dir="ltr"><KatexInline math="x<10" /></span> מתבצע <span dir="ltr"><KatexInline math="x:=x+2" /></span>, אחרת <span dir="ltr">x</span> נשאר ללא שינוי.
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> הציעו אינוריאנט אינדוקטיבי <span dir="ltr"><KatexInline math="I(x)" /></span> שמוכיח <span dir="ltr"><KatexInline math="\Box(0\le x\le 10\land \mathit{even}(x))" /></span>.<br/>
<b>ב.</b> הוכיחו: (1) תנאי הבסיס במצב ההתחלה. (2) סגירות תחת המעבר.
</div>

---

# פתרון: זוגיות וחסם נשמרים יחד

<div class="text-right text-[16px] leading-relaxed mt-3">
<div class="mt-1 bg-blue-50 border border-blue-200 rounded p-3 text-blue-900 mb-2">
<b>אינוריאנט:</b> <span dir="ltr"><KatexInline math="I(x)\;\equiv\;0\le x\le 10 \land \mathit{even}(x)" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900 mb-2">
<b>בסיס:</b> <span dir="ltr"><KatexInline math="x=0" /></span> מקיים <span dir="ltr"><KatexInline math="0\le 0\le 10" /></span> וזוגי. <span dir="ltr">✓</span>
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-3 text-amber-900">
<b>סגירות:</b> נניח <span dir="ltr"><KatexInline math="I(x)" /></span> מתקיים.
<ul class="mt-1">
<li>אם <span dir="ltr"><KatexInline math="x<10" /></span>: בגלל הזוגיות <span dir="ltr"><KatexInline math="x\le 8" /></span>, ולכן <span dir="ltr"><KatexInline math="x'=x+2\le 10" /></span>; וסכום שני זוגיים זוגי, אז <span dir="ltr"><KatexInline math="I(x')" /></span> מתקיים.</li>
<li>אם <span dir="ltr"><KatexInline math="x=10" /></span> (גבול עליון, ובהכרח זוגי): <span dir="ltr"><KatexInline math="x'=x" /></span> ללא שינוי, ועדיין <span dir="ltr"><KatexInline math="I(x')" /></span> מתקיים.</li>
</ul>
לכן <span dir="ltr"><KatexInline math="I" /></span> סגור תחת המעבר, ומתקיים בכל מצב נגיש — מה שמוכיח את תכונת הבטיחות.
</div>
</div>

---

# שאלה: בדיקת תכונת בטיחות רגולרית במכפלה (15 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
תכונת בטיחות רגולרית מעל <span dir="ltr"><KatexInline math="AP=\{\mathit{req},\mathit{ack}\}" /></span>: "כל <span dir="ltr">req</span> חייב להיות מלווה ב-<span dir="ltr">ack</span> בתוך הצעד שאחריו" (אחרת — הפרה).
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> תארו אוטומט ניטור (3 מצבים) שמזהה הפרה.<br/>
<b>ב.</b> כיצד בודקים את <span dir="ltr"><KatexInline math="TS\models" /></span> התכונה באמצעות מכפלה עם הניטור?<br/>
<b>ג.</b> מדוע מספיקה בדיקת <b>הישגות</b> (reachability) ולא צריך תנאי קבלה מסוג <span dir="ltr">Büchi</span>, בשונה מבדיקת <span dir="ltr">LTL</span> כללית?
</div>

---

# פתרון: ניטור, מכפלה, והישגות במקום קבלה אינסופית

<div class="bg-white rounded border border-slate-200 shadow-sm p-2 mt-2">
<AutomatonD3 variant="classic" :width="500" :height="160" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="12"
  :states="[
    { id: 'ok',  x: 80,  y: 80, label: '$ok$', r: 30, initial: true, initialDirection: 'top' },
    { id: 'pend', x: 260, y: 80, label: '$pending$', r: 34, labelWidth: 80 },
    { id: 'bad', x: 440, y: 80, label: '$bad$', r: 30, stroke: '#dc2626', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 'ok', target: 'ok', label: '$\\neg req$', loopDirection: '-90deg', labelY: -16 },
    { source: 'ok', target: 'pend', label: '$req$', curve: 0.1 },
    { source: 'pend', target: 'ok', label: '$ack$', labelY: -14, curve: 0.25 },
    { source: 'pend', target: 'bad', label: '$\\neg ack$', curve: 0.1 },
    { source: 'bad', target: 'bad', label: '$\\mathit{true}$', loopDirection: '-90deg', labelY: -16 }
  ]"
/>
</div>

<div class="mt-3 grid grid-cols-2 gap-3 text-[15px] text-right leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900">
<b>ב.</b> בונים <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span> ובודקים אם המצב <span dir="ltr">bad</span> <b>נגיש</b> (חיפוש גרף רגיל, <span dir="ltr">BFS/DFS</span>). אם כן — קיימת ריצה מפרה.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900">
<b>ג.</b> תכונת בטיחות נשברת ב<b>רישא סופית</b> — הגעה למצב <span dir="ltr">bad</span>. אין צורך לבדוק התנהגות אינסופית או "אינסוף פעמים" כמו ב-<span dir="ltr">LTL</span> כללית, ולכן הישגות (לא קבלת <span dir="ltr">Büchi</span>) מספיקה.
</div>
</div>

---

# שאלה: למה לא לכל NBA יש DBA שקול (10 נק')

<div class="text-right text-[18px] leading-relaxed mt-3">
תהי <span dir="ltr"><KatexInline math="L=\{\sigma\in\{a,b\}^\omega \mid a\text{ מופיעה בה רק סופית פעמים}\}" /></span> (כלומר <span dir="ltr"><KatexInline math="\mathsf{FG}\neg a" /></span>).
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> תנו <span dir="ltr">NBA</span> בעל 2 מצבים המקבל את <span dir="ltr">L</span>.<br/>
<b>ב.</b> הסבירו אינטואיטיבית מדוע אין <span dir="ltr">DBA</span> שקול ל-<span dir="ltr">L</span>.
</div>

---

# פתרון: ניחוש מותר, החלטה דטרמיניסטית אסורה

<div class="bg-white rounded border border-slate-200 shadow-sm p-2 mt-2">
<AutomatonD3 variant="classic" :width="420" :height="160" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="12"
  :states="[
    { id: 'q0', x: 90, y: 80, label: '$q_0$', r: 30, initial: true, initialDirection: 'top' },
    { id: 'q1', x: 290, y: 80, label: '$q_1$', r: 30, accepting: true }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$a,b$', loopDirection: '-90deg', labelY: -16 },
    { source: 'q0', target: 'q1', label: '$b$', curve: 0.1 },
    { source: 'q1', target: 'q1', label: '$b$', loopDirection: '-90deg', labelY: -16 }
  ]"
/>
</div>

<div class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-blue-900 text-right text-[15px] leading-relaxed">
<b>א.</b> <span dir="ltr">NBA</span>: <span dir="ltr"><KatexInline math="q_0" /></span> (התחלה, לא מקבל) עם לולאה עצמית על <span dir="ltr">a,b</span> ומעבר <b>לא־דטרמיניסטי</b> ל-<span dir="ltr"><KatexInline math="q_1" /></span> (מקבל) על <span dir="ltr">b</span> — הניחוש: "זו הופעת <span dir="ltr">a</span> האחרונה". מ-<span dir="ltr"><KatexInline math="q_1" /></span>, לולאה עצמית רק על <span dir="ltr">b</span> (אם מגיעה עוד <span dir="ltr">a</span> — אין מעבר, ריצה זו "נכשלת" אך ריצות אחרות עם ניחוש מאוחר יותר עדיין מקבלות).
</div>
<div class="mt-2 bg-red-50 border border-red-200 rounded p-3 text-red-900 text-right text-[15px] leading-relaxed">
<b>ב.</b> אוטומט דטרמיניסטי <b>חייב להחליט עכשיו</b>, ללא יכולת "לנחש ולחזור בו", מתי לעבור סופית למצב מקבל יציב. אבל בכל מילה סופית שנקראה עד כה תמיד <b>אפשרי</b> שתופיע עוד <span dir="ltr">a</span> בעתיד — כל החלטה "כעת אין יותר <span dir="ltr">a</span>" עלולה להתבדות. לכן כל <span dir="ltr">DBA</span> מועמד יוכשל ע"י איזושהי מילה ב-<span dir="ltr">L</span> או חוצה אותה — אין <span dir="ltr">DBA</span> שקול.
</div>
