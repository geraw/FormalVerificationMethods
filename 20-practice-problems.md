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

# שאלה: אלגוריתם לטיפול בהוֹגְנוּת על ידי הרחבת המערכת

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
מהתרשים, כל ריצה של <span dir="ltr"><KatexInline math="TS'" /></span> (ההרכבה) מתחילה ב-<KatexInline math="\langle s_0,0\rangle" />, ומתפצלת לשני מקרים בלבד: נשארת בו לעד (לולאת <KatexInline math="\alpha" />), או עוברת בשלב סופי ב-<KatexInline math="\gamma" /> ונכנסת למחזור <span dir="ltr"><KatexInline math="\langle s_1,1\rangle\to\langle s_2,0\rangle\to\langle s_1,0\rangle\to\langle s_2,0\rangle\to\cdots" /></span> (אין דרך לחזור ל-<KatexInline math="\langle s_0,0\rangle" />).
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

# שאלה: תרגום LTL לאוטומט Büchi עם Always במקום Until

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
שימו לב: <KatexInline math="\Box a" /> לא תורם אף קבוצת קבלה (לפי סעיף ב'); כל ה-<KatexInline math="\mathcal{F}" /> מגיע מההבטחה הנסתרת בתוך <KatexInline math="\neg\Box b" />, אף שאין <span dir="ltr">Until</span> ולא <span dir="ltr"><KatexInline math="\Diamond" /></span> בתחביר כלל.
</div>

---

# שאלה: אלגוריתם חלופי לבדיקת <span dir="ltr"><KatexInline math="TS\models P" /></span>

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

# שאלה: פירוק אוטומט Büchi לבטיחות וחַיּוּת

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

# שאלה: מעבר מ-LTL ל-QPTL

<div class="text-right text-[15px] leading-snug mt-2">
נניח <KatexInline math="AP=\{p\}" /> ונתבונן בשפת המילים שבהן <KatexInline math="p" /> מופיע מספר סופי וזוגי של פעמים:
</div>

<div class="mt-1 text-center text-[17px]" dir="ltr">
<KatexInline display math="L_{\mathrm{even}}=\{\sigma\in(2^{\{p\}})^\omega\mid |\{i\in\mathbb{N}\mid p\in\sigma[i]\}|\in 2\mathbb{N}\}" />
</div>

<div class="mt-1 bg-amber-50 border border-amber-200 rounded p-2 text-[14px] leading-snug text-right">
קבלו ללא הוכחה: אין נוסחת <span dir="ltr">LTL</span> שמתארת את <KatexInline math="L_{\mathrm{even}}" />.
</div>

<div class="mt-2 bg-blue-50 border border-blue-200 rounded p-2 text-[14px] leading-snug text-right">
<div class="font-bold mb-1">הגדרה: <span dir="ltr">QPTL</span></div>
<b>תחביר</b> - נוסחת <span dir="ltr">QPTL</span> מעל <KatexInline math="AP" /> נבנית על ידי:
<div class="mt-1 text-center" dir="ltr">
<KatexInline math="\varphi \;::=\; \mathit{true} \;\mid\; p \;\mid\; \neg\varphi \;\mid\; \varphi\land\varphi \;\mid\; \bigcirc\varphi \;\mid\; \varphi\,\mathbin{\mathrm{U}}\,\varphi \;\mid\; \exists q.\,\varphi" />
</div>
כאשר <KatexInline math="p\in AP" /> ו-<KatexInline math="q\notin AP" /> פסוק חדש (<b>משתנה מכומת</b>).
<div class="mt-2"><b>סמנטיקה</b> - מתי מילה <KatexInline math="\sigma\in(2^{AP})^\omega" /> מקיימת נוסחה: כל כללי <span dir="ltr">LTL</span> נשמרים, ועבור כימות:</div>
<div class="mt-1 text-center" dir="ltr">
<KatexInline math="\sigma\models\exists q.\,\varphi \;\iff\; \exists\tau\in(2^{AP\cup\{q\}})^\omega.\;\bigl(\forall i{:}\ \tau[i]\cap AP=\sigma[i]\bigr)\land\tau\models\varphi" />
</div>
כלומר, קיימת הרחבת המילה ל-<KatexInline math="AP\cup\{q\}" /> שעולה בקנה אחד עם <KatexInline math="\sigma" /> ומקיימת את <KatexInline math="\varphi" />.
</div>

<div class="mt-2 bg-amber-50 border border-amber-200 rounded p-2 text-[14px] leading-snug text-right">
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
<KatexInline display math="\exists q.\ q\ \land\ \Box\bigl(\bigcirc q\leftrightarrow(q\leftrightarrow\neg p)\bigr)\ \land\ \Diamond(q\land\Box\neg p)" />
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

# שאלה: טופולוגיה של בטיחות וחַיּוּת

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

<div class="mt-2 bg-blue-50 border border-blue-200 rounded p-2 text-[15px] leading-snug text-right">
כלומר, ככל שהרישא המשותפת ארוכה יותר, המרחק קטן יותר. 
המושגים "סגורה" ו"צפופה" שמופיעים בסעיפים ב'-ג' הם מושגים סטנדרטיים במרחבים מטריים (קבוצות עם מטריקה) ובשאלה זאת נראה את הקשר שלהם אלינו.
</div>

<div class="mt-2 space-y-1.5 text-right text-[14.5px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-2">
<span class="font-bold">א'.</span>
הראו ש-<KatexInline math="d" /> היא מטריקה על <KatexInline math="\Sigma^\omega" />.
</div>

<div class="bg-amber-50 border border-amber-200 rounded p-2">
<span class="font-bold">ב'.</span>
נאמר ש-<KatexInline math="P" /> <b>סגורה</b> אם המשלים שלה פתוח, כלומר: לכל <KatexInline math="\sigma\notin P" /> קיים <KatexInline math="\varepsilon>0" /> כך שהכדור הפתוח <KatexInline math="B(\sigma,\varepsilon)=\{\tau\mid d(\sigma,\tau)<\varepsilon\}" /> מוכל כולו מחוץ ל-<KatexInline math="P" />. הוכיחו: <KatexInline math="P" /> היא תכונת בטיחות אם ורק אם <KatexInline math="P" /> סגורה.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-2">
<span class="font-bold">ג'.</span>
נאמר ש-<KatexInline math="P" /> <b>צפופה</b> אם כל כדור פתוח חותך את <KatexInline math="P" />, כלומר: לכל <KatexInline math="\sigma\in\Sigma^\omega" /> ולכל <KatexInline math="\varepsilon>0" /> קיימת <KatexInline math="\tau\in P" /> עם <KatexInline math="d(\sigma,\tau)<\varepsilon" />. <br/> הוכיחו: <KatexInline math="P" /> היא תכונת חַיּוּת אם ורק אם <KatexInline math="P" /> צפופה.
</div>
</div>

---


# פתרון א': כדורים פתוחים = קונוסי רישות

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[16px] leading-relaxed text-right">
<b>א'. d מטריקה.</b> אי-שליליות, סימטריה, וזהות מיידיות. אי-שוויון משולש מתקיים בצורה חזקה יותר:
</div>
<div class="mt-2 text-center" dir="ltr">
<KatexInline display math="d(\sigma,\tau)\;\le\;\max\bigl(d(\sigma,\eta),\,d(\eta,\tau)\bigr)" />
</div>
<div class="mt-2 text-right text-[16px] leading-relaxed">
שכן אם <KatexInline math="\sigma" /> ו-<KatexInline math="\eta" /> מסכימות על <KatexInline math="k" /> אותיות ראשונות, ו-<KatexInline math="\eta" /> ו-<KatexInline math="\tau" /> מסכימות על <KatexInline math="m" /> אותיות ראשונות, אז <KatexInline math="\sigma" /> ו-<KatexInline math="\tau" /> מסכימות לפחות על <KatexInline math="\min(k,m)" /> - לכן <KatexInline math="d(\sigma,\tau)\le 2^{-\min(k,m)}=\max(2^{-k},2^{-m})" />.
</div>
<div class="mt-3 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] text-right leading-snug">
<b>תצפית מפתח:</b> כדור פתוח = קונוס רישא. <KatexInline math="B(\sigma,2^{-(n+1)})=\{\tau\mid\tau[0..n]=\sigma[0..n]\}" /> - המילים שמסכימות עם <KatexInline math="\sigma" /> על <KatexInline math="n+1" /> האותיות הראשונות. לכל <KatexInline math="\varepsilon>0" /> בחירת <KatexInline math="n\ge\lceil\log_2(1/\varepsilon)\rceil" /> נותנת <KatexInline math="B(\sigma,2^{-(n+1)})\subseteq B(\sigma,\varepsilon)" />.
</div>

---

# פתרון ב' (כיוון ⟹): בטיחות → סגורה

<div class="mt-4 bg-blue-50 border border-blue-200 rounded p-4 text-[16px] leading-relaxed text-right">
<b>נניח</b> <KatexInline math="P" /> תכונת בטיחות. רוצים: לכל <KatexInline math="\sigma\notin P" /> קיים <KatexInline math="\varepsilon>0" /> כך ש-<KatexInline math="B(\sigma,\varepsilon)\subseteq\Sigma^\omega\setminus P" />.
</div>
<div class="mt-3 text-right text-[16px] leading-relaxed">
<ol class="list-decimal list-inside space-y-2">
<li>יהי <KatexInline math="\sigma\notin P" />. מכיוון ש-<KatexInline math="P" /> בטיחות, קיימת <b>רישא רעה</b>: <KatexInline math="u=\sigma[0..n]" /> כך שלכל <KatexInline math="\tau\in\Sigma^\omega" /> עם <KatexInline math="u\sqsubseteq\tau" /> מתקיים <KatexInline math="\tau\notin P" />.</li>
<li>נבחר <KatexInline math="\varepsilon=2^{-(n+1)}" />. אז <KatexInline math="B(\sigma,\varepsilon)=\{\tau\mid\tau[0..n]=\sigma[0..n]\}=\{\tau\mid u\sqsubseteq\tau\}" />.</li>
<li>מהרישא הרעה: כל <KatexInline math="\tau\in B(\sigma,\varepsilon)" /> מקיים <KatexInline math="\tau\notin P" />, כלומר <KatexInline math="B(\sigma,\varepsilon)\subseteq\Sigma^\omega\setminus P" />. <span dir="ltr">□</span></li>
</ol>
</div>

---

# פתרון ב' (כיוון ⟸): סגורה → בטיחות

<div class="mt-4 bg-blue-50 border border-blue-200 rounded p-4 text-[16px] leading-relaxed text-right">
<b>נניח</b> <KatexInline math="P" /> סגורה. רוצים: לכל <KatexInline math="\sigma\notin P" /> קיימת רישא <KatexInline math="u\sqsubseteq\sigma" /> כך שכל <KatexInline math="\tau" /> עם <KatexInline math="u\sqsubseteq\tau" /> מקיים <KatexInline math="\tau\notin P" />.
</div>
<div class="mt-3 text-right text-[16px] leading-relaxed">
<ol class="list-decimal list-inside space-y-2">
<li>יהי <KatexInline math="\sigma\notin P" />. מכיוון ש-<KatexInline math="P" /> סגורה, המשלים <KatexInline math="\Sigma^\omega\setminus P" /> פתוח, לכן קיים <KatexInline math="\varepsilon>0" /> כך ש-<KatexInline math="B(\sigma,\varepsilon)\subseteq\Sigma^\omega\setminus P" />.</li>
<li>נבחר <KatexInline math="n" /> כך ש-<KatexInline math="2^{-(n+1)}\le\varepsilon" />. אז <KatexInline math="B(\sigma,2^{-(n+1)})\subseteq B(\sigma,\varepsilon)\subseteq\Sigma^\omega\setminus P" />.</li>
<li>נגדיר <KatexInline math="u=\sigma[0..n]" />. לכל <KatexInline math="\tau" /> עם <KatexInline math="u\sqsubseteq\tau" />: <KatexInline math="\tau\in B(\sigma,2^{-(n+1)})\subseteq\Sigma^\omega\setminus P" />, כלומר <KatexInline math="\tau\notin P" />.</li>
<li><KatexInline math="u" /> היא רישא רעה של <KatexInline math="\sigma" />. <span dir="ltr">□</span></li>
</ol>
</div>

---

# פתרון ג' (כיוון ⟹): חַיּוּת → צפופה

<div class="mt-4 bg-emerald-50 border border-emerald-200 rounded p-4 text-[16px] leading-relaxed text-right">
<b>נניח</b> <KatexInline math="P" /> תכונת חַיּוּת. רוצים: לכל <KatexInline math="\sigma\in\Sigma^\omega" /> ולכל <KatexInline math="\varepsilon>0" /> קיימת <KatexInline math="\tau\in P" /> עם <KatexInline math="d(\sigma,\tau)<\varepsilon" />.
</div>
<div class="mt-3 text-right text-[16px] leading-relaxed">
<ol class="list-decimal list-inside space-y-2">
<li>יהי <KatexInline math="\sigma\in\Sigma^\omega" /> ו-<KatexInline math="\varepsilon>0" />. נבחר <KatexInline math="n" /> כך ש-<KatexInline math="2^{-(n+1)}<\varepsilon" />.</li>
<li>נגדיר רישא <KatexInline math="u=\sigma[0..n]" />. מכיוון ש-<KatexInline math="P" /> חַיּוּת, קיימת <KatexInline math="\tau\in P" /> עם <KatexInline math="u\sqsubseteq\tau" />.</li>
<li>מהגדרת המטריקה: <KatexInline math="\tau[0..n]=\sigma[0..n]" />, לכן <KatexInline math="d(\sigma,\tau)\le 2^{-(n+1)}<\varepsilon" />. <span dir="ltr">□</span></li>
</ol>
</div>

---

# פתרון ג' (כיוון ⟸): צפופה → חַיּוּת

<div class="mt-4 bg-emerald-50 border border-emerald-200 rounded p-4 text-[16px] leading-relaxed text-right">
<b>נניח</b> <KatexInline math="P" /> צפופה. רוצים: לכל רישא סופית <KatexInline math="u\in\Sigma^*" /> קיימת <KatexInline math="\tau\in P" /> עם <KatexInline math="u\sqsubseteq\tau" />.
</div>
<div class="mt-3 text-right text-[16px] leading-relaxed">
<ol class="list-decimal list-inside space-y-2">
<li>יהי <KatexInline math="u\in\Sigma^*" /> רישא באורך <KatexInline math="n" />. נבחר מילה כלשהי <KatexInline math="\sigma\in\Sigma^\omega" /> עם <KatexInline math="u\sqsubseteq\sigma" />, ונגדיר <KatexInline math="\varepsilon=2^{-(n+1)}" />.</li>
<li>מכיוון ש-<KatexInline math="P" /> צפופה, קיימת <KatexInline math="\tau\in P" /> עם <KatexInline math="d(\sigma,\tau)<\varepsilon=2^{-(n+1)}" />.</li>
<li>לכן <KatexInline math="\tau[0..n]=\sigma[0..n]=u" />, כלומר <KatexInline math="u\sqsubseteq\tau" /> ו-<KatexInline math="\tau\in P" />.</li>
<li>לכן <KatexInline math="P" /> חַיּוּת. <span dir="ltr">□</span></li>
</ol>
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
שאלות מייצגות על נושאי הקורס שמעבר לבעיית התפוצצות המצבים - מבוי סתום, שמורות, בדיקת תכונות בטיחות רגולריות, ואוטומטי <span dir="ltr">Büchi</span> דטרמיניסטיים.
</div>

---

# שאלה: בטיחות, חַיּוּת, גם וגם, או לא ולא?

<div class="text-center text-slate-500 text-[13px]">לכל תכונה: שמורה? התמדה? חַיּוּת? בטיחות? (כל שמורה היא בטיחות, כל התמדה היא חַיּוּת) - לחצו לפתרון, אחת בכל פעם.</div>

<div class="mt-2 grid grid-cols-1 gap-1 text-right text-[15px] leading-snug">
<div class="bg-white border border-slate-200 rounded p-1.5"><b>א.</b> <span dir="ltr"><KatexInline math="\Box\neg(c_1\land c_2)" /></span></div>
<div class="bg-white border border-slate-200 rounded p-1.5"><b>ב.</b> <span dir="ltr"><KatexInline math="\Diamond(x=0)" /></span></div>
<div class="bg-white border border-slate-200 rounded p-1.5"><b>ג.</b> <span dir="ltr"><KatexInline math="\Box(\mathit{req}\to\Diamond\,\mathit{grant})" /></span></div>
<div class="bg-white border border-slate-200 rounded p-1.5"><b>ד.</b> <span dir="ltr"><KatexInline math="\Box\,\mathit{even}(x)\;\land\;\Diamond(x=10)" /></span></div>
<div class="bg-white border border-slate-200 rounded p-1.5"><b>ה.</b> <span dir="ltr"><KatexInline math="\mathit{true}" /></span> (טאוטולוגיה בזמן לינארי)</div>
</div>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="mt-2 min-h-[210px]">
<div v-show="$slidev.nav.clicks === 0" class="bg-slate-50 border border-slate-200 rounded p-3 text-slate-600 text-center text-[16px]">
לחצו להצגת התשובות, אחת בכל פעם.
</div>

<div v-show="$slidev.nav.clicks === 1" class="bg-blue-50 border-2 border-blue-300 rounded p-2 text-blue-900 text-[13px] leading-snug">
<div class="font-bold text-center mb-1">א. <span dir="ltr">□¬(c₁∧c₂)</span></div>
<div class="grid grid-cols-2 gap-1">
<div><b>שמורה: כן.</b> זו ממש <span dir="ltr">□p</span> עם תנאי-מצב <span dir="ltr">p≡¬(c₁∧c₂)</span> שנבדק בכל מצב בנפרד.</div>
<div><b>התמדה: לא.</b> התמדה היא תת-מחלקה של חַיּוּת, וזו אינה חַיּוּת (ראו להלן) - שמורה לא-טריוויאלית לעולם אינה התמדה. (גם ישירות: <span dir="ltr">□p</span> הוא תת-קבוצה ממש של <span dir="ltr">◇□p</span>, לא שווה לה - למשל <span dir="ltr">c₁∧c₂</span> רק בצעד הראשון ו-<span dir="ltr">¬(c₁∧c₂)</span> לנצח אח"כ מקיים <span dir="ltr">◇□¬(c₁∧c₂)</span> אך לא <span dir="ltr">□¬(c₁∧c₂)</span>.)</div>
<div><b>חַיּוּת: לא.</b> ברישא הסופית שבה <span dir="ltr">c₁∧c₂</span> מתקיים פעם אחת אין שום המשך שמתקן את ההפרה שכבר קרתה.</div>
<div><b>בטיחות: כן.</b> כל רישא שמסתיימת במצב עם <span dir="ltr">c₁∧c₂</span> היא רישא רעה - הדוגמה הקנונית לתכונת בטיחות.</div>
</div>
</div>

<div v-show="$slidev.nav.clicks === 2" class="bg-emerald-50 border-2 border-emerald-300 rounded p-2 text-emerald-900 text-[13px] leading-snug">
<div class="font-bold text-center mb-1">ב. <span dir="ltr">◇(x=0)</span></div>
<div class="grid grid-cols-2 gap-1">
<div><b>שמורה: לא.</b> כל שמורה היא תכונת בטיחות, וזו אינה בטיחות (ראו להלן) - ולכן אינה יכולה להיות שמורה.</div>
<div><b>התמדה: לא.</b> הרישא שבה <span dir="ltr">x=0</span> פעם אחת ואז <span dir="ltr">x≠0</span> לנצח מקיימת <span dir="ltr">◇(x=0)</span> אך לא <span dir="ltr">◇□(x=0)</span> - שתי השפות שונות.</div>
<div><b>חַיּוּת: כן.</b> לכל רישא סופית (גם אם <span dir="ltr">x</span> טרם התאפס) אפשר להמשיך ולהציב <span dir="ltr">x=0</span> בצעד הבא - אין רישא שמכריחה הפרה.</div>
<div><b>בטיחות: לא.</b> בריצה שבה <span dir="ltr">x≠0</span> לנצח, לכל רישא סופית שלה יש המשך עם <span dir="ltr">x=0</span> שמקיים את התכונה - אין רישא רעה.</div>
</div>
</div>

<div v-show="$slidev.nav.clicks === 3" class="bg-amber-50 border-2 border-amber-300 rounded p-2 text-amber-900 text-[13px] leading-snug">
<div class="font-bold text-center mb-1">ג. <span dir="ltr">□(req→◇grant)</span></div>
<div class="grid grid-cols-2 gap-1">
<div><b>שמורה: לא.</b> שמורה היא בטיחות, וזו אינה בטיחות (ראו להלן).</div>
<div><b>התמדה: לא.</b> ריצה עם בקשות ומענקים החוזרים אינסוף פעמים מקיימת את התכונה בלי ש-<span dir="ltr">req</span> או <span dir="ltr">grant</span> מתייצבים לנצח על ערך קבוע.</div>
<div><b>חַיּוּת: כן.</b> לכל רישא, גם עם בקשה פתוחה, אפשר להמשיך כך שהבקשה תיענה מיידית וכל בקשה עתידית תיענה - אין רישא שמכריחה הפרה. (התכונה "מרגישה" כמו בטיחות בגלל ה־<span dir="ltr">□</span>, אך אין לה רישא רעה סופית.)</div>
<div><b>בטיחות: לא.</b> כל רישא עם בקשה פתוחה ללא מענק ניתנת להשלמה ע"י מענק בצעד הבא - שום רישא סופית אינה דנה את התכונה לכישלון.</div>
</div>
</div>

<div v-show="$slidev.nav.clicks === 4" class="bg-red-50 border-2 border-red-300 rounded p-2 text-red-900 text-[13px] leading-snug">
<div class="font-bold text-center mb-1">ד. <span dir="ltr">□even(x) ∧ ◇(x=10)</span></div>
<div class="grid grid-cols-2 gap-1">
<div><b>שמורה: לא.</b> כולל דרישת "אי-פעם" (<span dir="ltr">◇</span>) שאינה תנאי-מצב הנבדק בכל רגע בנפרד.</div>
<div><b>התמדה: לא.</b> הריצה <span dir="ltr">10,8,10,8,...</span> מקיימת את שני האגפים בלי להתייצב לנצח על שום ערך קבוע.</div>
<div><b>חַיּוּת: לא.</b> ברישא עם ערך אי-זוגי יחיד כבר אין המשך שמקיים <span dir="ltr">□even(x)</span> - העבר דן את התכונה.</div>
<div><b>בטיחות: לא.</b> בריצה <span dir="ltr">x=0</span> לנצח (זוגי תמיד, לעולם לא 10), לכל רישא שלה יש המשך עם <span dir="ltr">x=10</span> שמקיים את התכונה - אין רישא רעה.</div>
</div>
<div class="text-center mt-1 font-bold">שילוב אמיתי של בטיחות (<span dir="ltr">□even(x)</span>) וחַיּוּת (<span dir="ltr">◇(x=10)</span>) שאינו שקול לאף אחת מהן.</div>
</div>

<div v-show="$slidev.nav.clicks >= 5" class="bg-purple-50 border-2 border-purple-300 rounded p-2 text-purple-900 text-[13px] leading-snug">
<div class="font-bold text-center mb-1">ה. <span dir="ltr">true</span></div>
<div class="grid grid-cols-2 gap-1">
<div><b>שמורה: כן.</b> <span dir="ltr">p≡true</span> מתקיים בכל מצב בנפרד.</div>
<div><b>התמדה: כן.</b> <span dir="ltr">◇□true</span> מתקיים טריוויאלית.</div>
<div><b>חַיּוּת: כן.</b> כל רישא סופית מקיימת המשך (כל המשך, באופן ריק) שמקיים <span dir="ltr">true</span>.</div>
<div><b>בטיחות: כן.</b> אין כלל ריצות מפרות, ולכן התנאי על רישא רעה מתקיים באופן ריק.</div>
</div>
<div class="text-center mt-1 font-bold">היחידה מבין החמש שהיא גם שמורה, גם התמדה, גם חַיּוּת וגם בטיחות בו-זמנית.</div>
</div>
</div>

---

# שאלה: שמורה גוררת התמדה?

<div class="text-center text-[19px] mt-6">
הוכיחו או הפריכו: <b>כל תכונת שמורה היא גם תכונת התמדה.</b>
</div>

---

# פתרון: לא נכון - שמורה לא-טריוויאלית אינה התמדה

<div class="mt-3 bg-red-50 border border-red-200 rounded p-3 text-red-900 text-right text-[16px] leading-relaxed">
<b>הטענה אינה נכונה.</b> התמדה (<span dir="ltr"><KatexInline math="\Diamond\Box p" /></span>) היא תת-מחלקה של חַיּוּת: לכל רישא סופית, אפשר להמשיך כך שמרגע מסוים <span dir="ltr">p</span> יחזיק לנצח - העבר לעולם אינו דן אותה. שמורה לא-טריוויאלית (<span dir="ltr"><KatexInline math="\Box p" /></span> עבור <span dir="ltr">p</span> לא-טאוטולוגי) <b>אינה</b> חַיּוּת: רישא עם מצב יחיד שמפר את <span dir="ltr">p</span> דנה את התכונה לנצח, ואין המשך שמתקן זאת. מכיוון ש<b>כל התמדה היא חַיּוּת</b> אך שמורה לא-טריוויאלית אינה חַיּוּת, היא בפרט אינה התמדה.
</div>
<div class="mt-2 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[15px] leading-relaxed">
<b>ישירות:</b> <span dir="ltr"><KatexInline math="\Box p" /></span> הוא תת-קבוצה <b>ממש</b> של <span dir="ltr"><KatexInline math="\Diamond\Box p" /></span>, לא שווה לה - מילה שבה <span dir="ltr">p</span> מופר רק באות הראשונה ומחזיק לנצח אח"כ מקיימת <span dir="ltr"><KatexInline math="\Diamond\Box p" /></span> אך לא <span dir="ltr"><KatexInline math="\Box p" /></span>.
</div>

---

# שאלה: סיווג תכונות

<div class="text-right text-[18px] leading-relaxed mt-3">
יהי <span dir="ltr"><KatexInline math="AP=\{A,B\}" /></span>. נסחו את התכונות הבאות כתכונות בזמן לינארי, וסווגו כל אחת - שמורה, תכונת בטיחות, תכונת חַיּוּת, או אף אחת מהן:
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> <span dir="ltr">A</span> לעולם לא מתקיימת.<br/>
<b>ב.</b> <span dir="ltr">A</span> מתקיימת פעם אחת בדיוק.<br/>
<b>ג.</b> <span dir="ltr">A</span> ו-<span dir="ltr">B</span> מתחלפות אינסוף פעמים.<br/>
<b>ד.</b> <span dir="ltr">A</span> תמיד מלווה בהמשך ע"י <span dir="ltr">B</span> (בסופו של דבר).
</div>

---

# פתרון: ארבע תכונות, ארבע מחלקות

<div class="grid grid-cols-2 gap-3 mt-3 text-[14.5px] text-right leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900">
<div class="font-bold mb-1">א. שמורה</div>
"<span dir="ltr">A</span> לא מתקיימת" היא תנאי בוליאני על כל מצב בנפרד - <b>שמורה</b> (ולכן גם תכונת בטיחות).
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900">
<div class="font-bold mb-1">ב. בטיחות (לא שמורה)</div>
מופע שני של <span dir="ltr">A</span> הוא רישא רעה סופית שמפרה את התכונה - <b>תכונת בטיחות</b>, אך לא שמורה (תלויה בהיסטוריה, לא רק במצב הנוכחי).
</div>
<div class="bg-red-50 border border-red-200 rounded p-3 text-red-900">
<div class="font-bold mb-1">ג. לא בטיחות ולא חַיּוּת</div>
זו דרישת "אינסוף פעמים" (לא בטיחות, אין רישא רעה סופית) <b>וגם</b> דרישה שמתקיימת רק חלקית ע"י כל המשך (לא חַיּוּת גרידא, כי כל רישא סופית מפירה את ה"לעולם לא תיפר") - <b>אף אחת מהשתיים</b>.
</div>
<div class="bg-amber-50 border border-amber-200 rounded p-3 text-amber-900">
<div class="font-bold mb-1">ד. חַיּוּת</div>
לכל רישא סופית יש המשך שמקיים את הדרישה (פשוט תוסיפו <span dir="ltr">B</span> אחרי כל <span dir="ltr">A</span> מאותה נקודה) - <b>תכונת חַיּוּת</b> גרידא.
</div>
</div>

---

# שאלה: הוכחת בטיחות באמצעות שמורה אינדוקטיבית

<div class="text-right text-[18px] leading-relaxed mt-3">
משתנה <span dir="ltr">x</span> מתחיל ב-<span dir="ltr"><KatexInline math="x=0" /></span>, ובכל צעד: אם <span dir="ltr"><KatexInline math="x<10" /></span> מתבצע <span dir="ltr"><KatexInline math="x:=x+2" /></span>, אחרת <span dir="ltr">x</span> נשאר ללא שינוי.
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> הציעו שמורה אינדוקטיבית <span dir="ltr"><KatexInline math="I(x)" /></span> שמוכיחה <span dir="ltr"><KatexInline math="\Box(0\le x\le 10\land \mathit{even}(x))" /></span>.<br/>
<b>ב.</b> הוכיחו: (1) תנאי הבסיס במצב ההתחלה. (2) סגירות תחת המעבר.
</div>

---

# פתרון: זוגיות וחסם נשמרים יחד

<div class="text-right text-[16px] leading-relaxed mt-3">
<div class="mt-1 bg-blue-50 border border-blue-200 rounded p-3 text-blue-900 mb-2">
<b>שמורה:</b> <span dir="ltr"><KatexInline math="I(x)\;\equiv\;0\le x\le 10 \land \mathit{even}(x)" /></span>.
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
לכן <span dir="ltr"><KatexInline math="I" /></span> סגור תחת המעבר, ומתקיים בכל מצב נגיש - מה שמוכיח את תכונת הבטיחות.
</div>
</div>

---

# שאלה: בדיקת תכונת בטיחות רגולרית במכפלה

<div class="text-right text-[18px] leading-relaxed mt-3">
תכונת בטיחות רגולרית מעל <span dir="ltr"><KatexInline math="AP=\{\mathit{req},\mathit{ack}\}" /></span>: "כל <span dir="ltr">req</span> חייב להיות מלווה ב-<span dir="ltr">ack</span> בתוך הצעד שאחריו" (אחרת - הפרה).
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
<b>ב.</b> בונים <span dir="ltr"><KatexInline math="TS\times\mathcal{A}" /></span> ובודקים אם המצב <span dir="ltr">bad</span> <b>נגיש</b> (חיפוש גרף רגיל, <span dir="ltr">BFS/DFS</span>). אם כן - קיימת ריצה מפרה.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900">
<b>ג.</b> תכונת בטיחות נשברת ב<b>רישא סופית</b> - הגעה למצב <span dir="ltr">bad</span>. אין צורך לבדוק התנהגות אינסופית או "אינסוף פעמים" כמו ב-<span dir="ltr">LTL</span> כללית, ולכן הישגות (לא קבלת <span dir="ltr">Büchi</span>) מספיקה.
</div>
</div>

---

# שאלה: אוטומט מונה, מבוי-סתום, והאם זו שמורה?

<div class="text-right text-[16px] leading-relaxed mt-3">
יהי <span dir="ltr"><KatexInline math="TS" /></span>, <span dir="ltr"><KatexInline math="\Phi" /></span> פסוק מצב, <span dir="ltr"><KatexInline math="n\in\mathbb{N}" /></span>. נגדיר <span dir="ltr"><KatexInline math="P_{\Phi,n}=\{\sigma\mid \forall i\ge0,\ \neg\bigwedge_{j=i}^{i+n}(\sigma[j]\models\Phi)\}" /></span> - בכל ריצה, <span dir="ltr">Φ</span> לא יחזיק <span dir="ltr">n+1</span> צעדים רצופים. בודקים זאת ע"י מכפלה <span dir="ltr"><KatexInline math="TS'=TS\times \mathcal{A}_{n,\Phi}" /></span> עם אוטומט מונה: <span dir="ltr"><KatexInline math="q_i\xrightarrow{\Phi}q_{i+1}" /></span>, <span dir="ltr"><KatexInline math="q_i\xrightarrow{\neg\Phi}q_0" /></span>, <span dir="ltr"><KatexInline math="q_n\xrightarrow{\Phi}q_{err}" /></span>, <span dir="ltr"><KatexInline math="q_{err}\xrightarrow{\mathit{true}}q_{err}" /></span> (המעבר במכפלה נקבע לפי תווית <b>מצב היעד</b> ב-<span dir="ltr">TS</span>).
</div>

<div class="mt-3 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[16px] leading-relaxed">
הוכיחו או הפריכו כל אחת:<br/>
<b>א.</b> <span dir="ltr"><KatexInline math="TS\models P_{\Phi,n}" /></span> אם ורק אם אין מצב מהצורה <span dir="ltr"><KatexInline math="\langle s,q_{err}\rangle" /></span> נגיש ב-<span dir="ltr">TS'</span>.<br/>
<b>ב.</b> <span dir="ltr"><KatexInline math="P_{\Phi,n}" /></span> היא תכונת שמורה.<br/>
<b>ג.</b> <span dir="ltr">TS</span> מפרה את <span dir="ltr"><KatexInline math="P_{\Phi,n}" /></span> אם ורק אם ניתן להגיע למצב מבוי-סתום ב-<span dir="ltr">TS'</span>.
</div>

---

# פתרון: שלוש הפרכות, שלושה כשלים אופייניים

<div class="grid grid-cols-1 gap-2 mt-2 text-right text-[14px] leading-snug">
<div class="bg-red-50 border border-red-200 rounded p-2 text-red-900">
<b>א. לא נכון.</b> דוגמה נגדית: <span dir="ltr"><KatexInline math="AP=\{a\}" /></span>, <span dir="ltr"><KatexInline math="\Phi=a" /></span>, <span dir="ltr">n=1</span>, ו-<span dir="ltr">TS</span>: <span dir="ltr"><KatexInline math="s_0\to s_1\to s_2\to s_2\to\cdots" /></span> עם <span dir="ltr"><KatexInline math="L(s_0)=L(s_1)=\{a\}" /></span>, <span dir="ltr"><KatexInline math="L(s_2)=\emptyset" /></span>. הריצה <span dir="ltr"><KatexInline math="\{a\}\{a\}\emptyset\cdots" /></span> מפרה (שני <span dir="ltr">a</span> רצופים בהתחלה) - <span dir="ltr"><KatexInline math="TS\not\models P_{a,1}" /></span>. אבל במכפלה תמיד מתחילים ב-<span dir="ltr"><KatexInline math="q_0" /></span> בלי תלות ב-<span dir="ltr"><KatexInline math="L(s_0)" /></span>, כך שהריצה היחידה היא <span dir="ltr"><KatexInline math="\langle s_0,q_0\rangle\to\langle s_1,q_1\rangle\to\langle s_2,q_0\rangle\to\cdots" /></span> - <span dir="ltr"><KatexInline math="q_{err}" /></span> לעולם לא נגיש. <b>שקר ⟺ אמת</b> - הבנייה "מפספסת" הפרה שמתחילה כבר במצב ההתחלתי, כי המונה לא סופר את <span dir="ltr"><KatexInline math="L(s_0)" /></span> עצמו.
</div>
<div class="bg-red-50 border border-red-200 rounded p-2 text-red-900">
<b>ב. לא נכון.</b> שמורה מאופיינת ע"י פסוק מצב <span dir="ltr"><KatexInline math="\psi" /></span> שמחזיק בכל מצב בנפרד. בשלילה: אם <span dir="ltr"><KatexInline math="P_{\Phi,n}" /></span> הייתה שמורה כזו, מילה שרק האות הראשונה שלה מקיימת <span dir="ltr"><KatexInline math="\Phi" /></span> (ושאר האותיות <span dir="ltr"><KatexInline math="\neg\Phi" /></span>) מקיימת <span dir="ltr"><KatexInline math="P_{\Phi,n}" /></span> (אין רצף של <span dir="ltr">n+1</span> הפרות) - כל אות בה מקיימת <span dir="ltr"><KatexInline math="\psi" /></span>, ובפרט האות הראשונה, ולכן <span dir="ltr"><KatexInline math="\Phi\Rightarrow\psi" /></span>. אבל אז המילה הקבועה שכל אותיותיה מקיימות <span dir="ltr"><KatexInline math="\Phi" /></span> מקיימת גם היא <span dir="ltr"><KatexInline math="\psi" /></span> בכל מקום - ולכן לפי ההנחה צריכה לקיים <span dir="ltr"><KatexInline math="P_{\Phi,n}" /></span>, בסתירה לכך שהיא מפרה אותה (רצף אינסופי של <span dir="ltr"><KatexInline math="\Phi" /></span>). תכונה שתלויה ב<b>חלון</b> של <span dir="ltr">n+1</span> צעדים, ולא במצב בודד, אינה שמורה.
</div>
<div class="bg-red-50 border border-red-200 rounded p-2 text-red-900">
<b>ג. לא נכון.</b> מבוי-סתום הוא מצב <b>בלי יציאות בכלל</b>. הפרת התכונה מתבטאת בהגעה ל-<span dir="ltr"><KatexInline math="q_{err}" /></span>, אבל זהו מצב <b>מלכודת</b> (יש ממנו מעבר עצמי) ולא מצב סופי. אם ל-<span dir="ltr">s</span> יש יציאות ב-<span dir="ltr">TS</span>, גם ל-<span dir="ltr"><KatexInline math="\langle s,q_{err}\rangle" /></span> יש יציאות (ל-<span dir="ltr"><KatexInline math="\langle s',q_{err}\rangle" /></span>) - הפרת התכונה <b>אינה</b> גוררת מבוי-סתום.
</div>
</div>

---

# שאלה: רדוקציה שבורה - בטיחות "אף פעם לא bad"

<div class="text-right text-[16px] leading-relaxed mt-3">
תכונת הבטיחות <span dir="ltr"><KatexInline math="P=\{\sigma\mid\forall i,\ \sigma[i]\ne\sigma[i+1]\}" /></span> ("שני מצבים עוקבים לא מתויגים אותו דבר"). מציעים לבדוק אותה ע"י <span dir="ltr"><KatexInline math="TS'=\langle S\times 2^{AP},\,Act,\,\to',\,I\times\{L(s):s\in I\},\,\{bad\},\,L'\rangle" /></span> כאשר <span dir="ltr"><KatexInline math="\langle s,S\rangle\xrightarrow{\alpha}\langle t,L(s)\rangle" /></span> לכל <span dir="ltr"><KatexInline math="s\xrightarrow{\alpha}t" /></span>, ו-<span dir="ltr"><KatexInline math="L'(\langle s,S\rangle)=\{bad\}" /></span> אם ורק אם <span dir="ltr">S=L(s)</span> (המרכיב השני "זוכר" את התווית הקודמת).
</div>

<div class="mt-3 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[16px] leading-relaxed">
<b>א.</b> הראו שלא לכל <span dir="ltr">TS</span> מתקיים <span dir="ltr"><KatexInline math="TS\models P \iff TS'\models\Box\neg bad" /></span>.<br/>
<b>ב.</b> הציעו תיקון פשוט לבנייה כך שהשקילות תתקיים תמיד.
</div>

---

# פתרון: הבעיה היא ב"זיכרון" של המצב ההתחלתי

<div class="grid grid-cols-1 gap-2 mt-2 text-right text-[14.5px] leading-snug">
<div class="bg-red-50 border border-red-200 rounded p-2 text-red-900">
<b>א.</b> דוגמה נגדית: <span dir="ltr"><KatexInline math="S=\{s_0,s_1\}" /></span>, <span dir="ltr"><KatexInline math="I=\{s_0\}" /></span>, <span dir="ltr"><KatexInline math="L(s_0)=\{a,b\}" /></span>, <span dir="ltr"><KatexInline math="L(s_1)=\{a\}" /></span>, <span dir="ltr"><KatexInline math="s_0\to s_1\to s_0\to\cdots" /></span>. <span dir="ltr"><KatexInline math="TS\models P" /></span> (התוויות מתחלפות, לעולם לא שוות ברצף). אבל המצב ההתחלתי ב-<span dir="ltr">TS'</span> הוא <span dir="ltr"><KatexInline math="\langle s_0,L(s_0)\rangle=\langle s_0,\{a,b\}\rangle" /></span> - ולכן מיד <span dir="ltr"><KatexInline math="L'(\langle s_0,\{a,b\}\rangle)=\{bad\}" /></span>, כלומר <span dir="ltr"><KatexInline math="TS'\not\models\Box\neg bad" /></span>. הבנייה מניחה "תווית קודמת" למצב ההתחלתי, אבל אין כזו בפועל - <span dir="ltr"><KatexInline math="TS\models P" /></span> ועדיין <span dir="ltr"><KatexInline math="TS'\not\models\Box\neg bad" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-2 text-emerald-900">
<b>ב. התיקון:</b> מוסיפים סימן טרי <span dir="ltr"><KatexInline math="start\notin AP" /></span> ומשנים רק את <b>המצבים ההתחלתיים</b>: <span dir="ltr"><KatexInline math="I'=I\times\{\{start\}\}" /></span> (במקום <span dir="ltr"><KatexInline math="I\times\{L(s):s\in I\}" /></span>). כך, בצעד הראשון <span dir="ltr"><KatexInline math="S=\{start\}\ne L(s_0)" /></span> בוודאות (כי <span dir="ltr"><KatexInline math="start\notin AP" /></span>), ואין הפרת-שווא. כל שאר הבנייה (מעברים ותיוג <span dir="ltr">bad</span>) נשארת זהה. עכשיו <span dir="ltr"><KatexInline math="\langle s,S\rangle" /></span> "זוכר" תווית אמיתית קודמת בכל מצב חוץ מההתחלה, ושם בדיוק לא נדרשת השוואה - מתקיים <span dir="ltr"><KatexInline math="TS\models P\iff TS'\models\Box\neg bad" /></span> לכל <span dir="ltr">TS</span>.
</div>
</div>

---

# שאלה: שמורה, סגירות, ופירוק לבטיחות וחיות

<div class="mt-3 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[16px] leading-relaxed">
קבעו נכון/שגוי, והוכיחו:<br/>
<b>א.</b> אם <span dir="ltr">P</span> וגם המשלים שלה <span dir="ltr"><KatexInline math="\overline{P}" /></span> הן שתיהן תכונות בטיחות, אז <span dir="ltr">P</span> היא תכונת שמורה.<br/>
<b>ב.</b> יהי <span dir="ltr"><KatexInline math="AP=\{p\}" /></span>, <span dir="ltr"><KatexInline math="\psi=\Box(p\to\bigcirc p)" /></span>. הטענה: <span dir="ltr"><KatexInline math="closure(\mathit{Words}(\psi))=\mathit{Words}(\psi)" /></span> (כלומר <span dir="ltr"><KatexInline math="\psi" /></span> מגדירה תכונת בטיחות).<br/>
<b>ג.</b> כל תכונה <span dir="ltr"><KatexInline math="\omega" /></span>-רגולרית <span dir="ltr">P</span> ניתנת לכתיבה כ-<span dir="ltr"><KatexInline math="P=P_{safe}\cap P_{live}" /></span> עם <span dir="ltr"><KatexInline math="P_{safe}" /></span> תכונת בטיחות <b>רגולרית</b>.
</div>

---

# פתרון: שמורה היא יותר מבטיחות-בשני-הכיוונים

<div class="grid grid-cols-1 gap-2 mt-2 text-right text-[14.5px] leading-snug">
<div class="bg-red-50 border border-red-200 rounded p-2 text-red-900">
<b>א. לא נכון.</b> דוגמה נגדית פשוטה: <span dir="ltr"><KatexInline math="P=\mathit{Words}(p)" /></span> ("האות הראשונה היא <span dir="ltr">p</span>", שאר האותיות חופשיות). <span dir="ltr">P</span> בטיחות: הרישא הרעה המינימלית היחידה היא אות ראשונה <span dir="ltr"><KatexInline math="\neg p" /></span> - אם נצפה בה, אין דרך לתקן. <span dir="ltr"><KatexInline math="\overline P=\mathit{Words}(\neg p)" /></span> בטיחות בדיוק מאותה סיבה (בתמורה). אך <span dir="ltr">P</span> אינה שמורה: שמורה דורשת תנאי-מצב יחיד שמתקיים <b>בכל</b> מצב, ואילו <span dir="ltr">P</span> מגבילה רק את הצעד הראשון - המילים <span dir="ltr"><KatexInline math="p\,p\,p\,\cdots" /></span> ו-<span dir="ltr"><KatexInline math="p\,\neg p\,\neg p\,\cdots" /></span> שתיהן ב-<span dir="ltr">P</span> אך אין תנאי-מצב יחיד שמחזיק בכל אות בשתיהן ומבדיל אותן מ-<span dir="ltr"><KatexInline math="\neg p\,p\,p\,\cdots" /></span>. <b>מסקנה:</b> "בטיחות + משלים בטיחות" (סגור-ופתוח) הוא תנאי חלש מ"שמורה" - הוא מבטיח החלטה מוקדמת אך לא בהכרח <b>חזרה על אותו תנאי בכל צעד</b>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-2 text-emerald-900">
<b>ב. נכון.</b> מספיק להראות רישא רעה לכל מילה שמפרה. אם <span dir="ltr"><KatexInline math="\sigma\notin\mathit{Words}(\psi)" /></span>, קיים <span dir="ltr">i</span> עם <span dir="ltr"><KatexInline math="\sigma[i]\models p" /></span> וגם <span dir="ltr"><KatexInline math="\sigma[i+1]\not\models p" /></span>. הרישא <span dir="ltr"><KatexInline math="\rho=\sigma[0..i+1]" /></span> היא רישא רעה: <b>כל</b> המשך שלה כבר מכיל את ההפרה ב-<span dir="ltr">i</span>, ולכן לעולם לא יקיים <span dir="ltr"><KatexInline math="\psi" /></span>. לכן <span dir="ltr"><KatexInline math="\psi" /></span> בטיחות, ועל כן <span dir="ltr"><KatexInline math="closure(\mathit{Words}(\psi))=\mathit{Words}(\psi)" /></span>.
</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-2 text-emerald-900">
<b>ג. נכון.</b> משפט הפירוק: <span dir="ltr"><KatexInline math="P_{safe}=closure(P)" /></span>, <span dir="ltr"><KatexInline math="P_{live}" /></span> חיות, ו-<span dir="ltr"><KatexInline math="P=P_{safe}\cap P_{live}" /></span> תמיד. נשאר להראות ש-<span dir="ltr"><KatexInline math="P_{safe}" /></span> רגולרית כש-<span dir="ltr">P</span> <span dir="ltr"><KatexInline math="\omega" /></span>-רגולרית: אם <span dir="ltr"><KatexInline math="P=L_\omega(\mathcal{A})" /></span>, אז קבוצת <b>הרישות הסופיות</b> <span dir="ltr">pref(P)</span> מתקבלת ע"י <span dir="ltr"><KatexInline math="\mathcal{A}" /></span> עם כל מצביו מוגדרים כמקבלים (הישגות גרידא) - שפה רגולרית. <span dir="ltr">closure(P)</span> הוא בדיוק קבוצת המילים שכל הרישות שלהן ב-<span dir="ltr">pref(P)</span>, כלומר המשלים של "יש רישא מחוץ ל-<span dir="ltr">pref(P)</span>" - ומכיוון שרגולריות סגורות להשלמה, גם זו תכונת בטיחות רגולרית.
</div>
</div>

---

# שאלה: בניית NBA לפי זוגיות

<div class="text-right text-[18px] leading-relaxed mt-3">
יהי <span dir="ltr"><KatexInline math="\Sigma=\{A,B\}" /></span>. בנו <span dir="ltr">NBA</span> שמקבל את המילים האינסופיות <span dir="ltr">σ</span> מעל <span dir="ltr">Σ</span> כך ש־<span dir="ltr">A</span> מופיעה בהן אינסוף פעמים, ובין כל שתי הופעות <span dir="ltr">A</span> עוקבות מופיע מספר <b>אי־זוגי</b> של <span dir="ltr">B</span>.
</div>

---

# פתרון: שלושה מצבים, מעקב זוגיות

<div class="bg-white rounded border border-slate-200 shadow-sm p-2 mt-2">
<AutomatonD3 variant="classic" :width="560" :height="180" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="12"
  :states="[
    { id: 'init', x: 80,  y: 90, label: '$init$', r: 30, initial: true, initialDirection: 'top' },
    { id: 'ev',   x: 280, y: 90, label: '$even$', r: 30, accepting: true },
    { id: 'od',   x: 480, y: 90, label: '$odd$', r: 30 }
  ]"
  :transitions="[
    { source: 'init', target: 'init', label: '$B$', loopDirection: '-90deg', labelY: -16 },
    { source: 'init', target: 'ev', label: '$A$', curve: 0.1 },
    { source: 'ev', target: 'od', label: '$B$', labelY: -12, curve: 0.15 },
    { source: 'od', target: 'ev', label: '$B$', labelY: 12, curve: 0.15 },
    { source: 'od', target: 'ev', label: '$A$', labelY: 24, curve: 0.45 }
  ]"
/>
</div>

<div class="mt-2 grid grid-cols-3 gap-2 text-[14px] text-right leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-2 text-blue-900"><span dir="ltr">init</span>: לפני ה־<span dir="ltr">A</span> הראשונה - אין דרישה, <span dir="ltr">B</span> חופשי.</div>
<div class="bg-emerald-50 border border-emerald-200 rounded p-2 text-emerald-900"><span dir="ltr">even</span>: נספרו <span dir="ltr">0</span> (זוגי) <span dir="ltr">B</span>-ים מאז ה־<span dir="ltr">A</span> האחרונה. <b>אין</b> מעבר על <span dir="ltr">A</span> מכאן - זה היה אוסר ספירה זוגית.</div>
<div class="bg-amber-50 border border-amber-200 rounded p-2 text-amber-900"><span dir="ltr">odd</span>: נספרו אי־זוגי <span dir="ltr">B</span>-ים. מעבר על <span dir="ltr">A</span> מכאן <b>חוקי</b> וחוזר ל־<span dir="ltr">even</span> (איפוס המונה).</div>
</div>

<div class="mt-2 bg-red-50 border-2 border-red-300 rounded p-2 text-red-900 text-center text-[14px] leading-snug">
<span dir="ltr"><KatexInline math="F=\{even\}" /></span>: ביקור חוזר ואינסופי ב־<span dir="ltr">even</span> מתאפשר רק דרך מעברי <span dir="ltr">A</span> תקפים מ־<span dir="ltr">odd</span> - ולכן הוא שקול ל"<span dir="ltr">A</span> אינסוף פעמים, כל פעם אחרי מספר אי־זוגי של <span dir="ltr">B</span>".
</div>

---

# שאלה: מענק תמיד יבוא

<div class="text-right text-[18px] leading-relaxed mt-3">
תהליך מבקש שירות (<span dir="ltr">t</span>) ומקבל מענק (<span dir="ltr">c</span>). התכונה הנדרשת: <span dir="ltr"><KatexInline math="\Box(t\to\Diamond c)" /></span> - כל בקשה זוכה <b>בסופו של דבר</b> למענק (ללא חסם זמן קבוע, בניגוד לתכונה "מענק תוך 2 צעדים" שראינו קודם).
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> בנו <span dir="ltr">NBA</span> (2 מצבים) המקבל בדיוק את המילים המקיימות את התכונה.<br/>
<b>ב.</b> הסבירו מדוע <b>לא ניתן</b> להשתמש כאן בבדיקת הישגות בלבד (כפי שעשינו לתכונת הבטיחות עם הניטור הסופי), אלא יש צורך בתנאי קבלה מסוג <span dir="ltr">Büchi</span>.
</div>

---

# פתרון: מצב מקבל "נח", מצב ביניים "חייב לסגור"

<div class="bg-white rounded border border-slate-200 shadow-sm p-2 mt-2">
<AutomatonD3 variant="classic" :width="420" :height="160" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="12"
  :states="[
    { id: 'q0', x: 90, y: 80, label: '$q_0$', r: 30, initial: true, initialDirection: 'top', accepting: true },
    { id: 'q1', x: 290, y: 80, label: '$q_1$', r: 30 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$\\neg t\\lor c$', loopDirection: '-90deg', labelY: -16 },
    { source: 'q0', target: 'q1', label: '$t\\land\\neg c$', curve: 0.15 },
    { source: 'q1', target: 'q1', label: '$\\neg c$', loopDirection: '-90deg', labelY: -16 },
    { source: 'q1', target: 'q0', label: '$c$', labelY: 24, curve: 0.45 }
  ]"
/>
</div>

<div class="mt-2 grid grid-cols-2 gap-3 text-[14.5px] text-right leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-2 text-blue-900">
<b>א.</b> <span dir="ltr">q₀</span> (מקבל): נשארים כל עוד אין בקשה פתוחה, או שבקשה זוכה למענק מיידי. <span dir="ltr">q₁</span>: בקשה פתוחה ללא מענק עדיין - נשארים כאן עד שמגיע <span dir="ltr">c</span> וחוזרים ל-<span dir="ltr">q₀</span>.
</div>
<div class="bg-red-50 border border-red-200 rounded p-2 text-red-900">
<b>ב.</b> ריצה שנתקעת לנצח ב-<span dir="ltr">q₁</span> (בקשה שלעולם לא נענית) חייבת <b>להידחות</b>, אך זו תכונת "אינסוף פעמים" על כלל ההמשך - אין רישא סופית שמעידה על הפרה, ולכן הישגות (כמו בבטיחות) לא מספיקה; צריך לבדוק שהריצה <b>לא</b> נתקעת לנצח מחוץ ל-<span dir="ltr"><KatexInline math="F={q₀}" /></span>, וזה מצריך קבלת <span dir="ltr">Büchi</span>.
</div>
</div>

---

# שאלה: למה לא לכל NBA יש DBA שקול

<div class="text-right text-[18px] leading-relaxed mt-3">
תהי <span dir="ltr"><KatexInline math="L=\{\sigma\in\{a,b\}^\omega \mid a\text{ מופיעה בה רק סופית פעמים}\}" /></span> (כלומר <span dir="ltr"><KatexInline math="\mathsf{FG}\neg a" /></span>).
</div>

<div class="mt-5 bg-amber-50 border border-amber-200 rounded p-3 text-amber-900 text-right text-[17px] leading-relaxed">
<b>א.</b> תנו <span dir="ltr">NBA</span> בעל 2 מצבים המקבל את <span dir="ltr">L</span>.<br/>
<b>ב.</b> הסבירו אינטואיטיבית מדוע אין <span dir="ltr">DBA</span> שקול ל-<span dir="ltr">L</span>.<br/>
<b>ג.</b> האם לשפה המשלימה <span dir="ltr"><KatexInline math="\{a,b\}^\omega\setminus L" /></span> (כלומר <span dir="ltr">a</span> מופיעה <b>אינסוף</b> פעמים) קיים <span dir="ltr">DBA</span>?
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
<b>א.</b> <span dir="ltr">NBA</span>: <span dir="ltr"><KatexInline math="q_0" /></span> (התחלה, לא מקבל) עם לולאה עצמית על <span dir="ltr">a,b</span> ומעבר <b>לא־דטרמיניסטי</b> ל-<span dir="ltr"><KatexInline math="q_1" /></span> (מקבל) על <span dir="ltr">b</span> - הניחוש: "זו הופעת <span dir="ltr">a</span> האחרונה". מ-<span dir="ltr"><KatexInline math="q_1" /></span>, לולאה עצמית רק על <span dir="ltr">b</span> (אם מגיעה עוד <span dir="ltr">a</span> - אין מעבר, ריצה זו "נכשלת" אך ריצות אחרות עם ניחוש מאוחר יותר עדיין מקבלות).
</div>
<div class="mt-2 bg-red-50 border border-red-200 rounded p-3 text-red-900 text-right text-[15px] leading-relaxed">
<b>ב.</b> אוטומט דטרמיניסטי <b>חייב להחליט עכשיו</b>, ללא יכולת "לנחש ולחזור בו", מתי לעבור סופית למצב מקבל יציב. אבל בכל מילה סופית שנקראה עד כה תמיד <b>אפשרי</b> שתופיע עוד <span dir="ltr">a</span> בעתיד - כל החלטה "כעת אין יותר <span dir="ltr">a</span>" עלולה להתבדות. לכן כל <span dir="ltr">DBA</span> מועמד יוכשל ע"י איזושהי מילה ב-<span dir="ltr">L</span> או חוצה אותה - אין <span dir="ltr">DBA</span> שקול. (<span dir="ltr">L</span> היא תכונת <b>התמדה</b> - <span dir="ltr">◇□¬a</span> - וכפי שראינו, התמדה לא-טריוויאלית "מרגישה כמו" החלטה שלעולם אינה בטוחה.)
</div>
---

# פתרון ג': חזרה, בניגוד להתמדה, כן ניתנת להחלטה דטרמיניסטית

<div class="bg-white rounded border border-slate-200 shadow-sm p-2 mt-2">
<AutomatonD3 variant="classic" :width="420" :height="160" :arrowSize="3.5" :stateLabelFontSize="13" :transitionLabelFontSize="12"
  :states="[
    { id: 'w0', x: 90, y: 80, label: '$wait$', r: 32, initial: true, initialDirection: 'top' },
    { id: 'w1', x: 300, y: 80, label: '$\\mathit{just}\\text{-}a$', r: 38, labelWidth: 76, accepting: true }
  ]"
  :transitions="[
    { source: 'w0', target: 'w0', label: '$\\neg a$', loopDirection: '-90deg', labelY: -16 },
    { source: 'w0', target: 'w1', label: '$a$', curve: 0.1 },
    { source: 'w1', target: 'w1', label: '$a$', loopDirection: '-90deg', labelY: -16 },
    { source: 'w1', target: 'w0', label: '$\\neg a$', curve: 0.1 }
  ]"
/>
</div>
<div class="mt-1 text-center text-slate-500 text-[13px]">כל הופעת <span dir="ltr">a</span> נכנסת ל-<span dir="ltr">just-a</span> (מקבל) - ביקור אינסופי בו שקול ל"<span dir="ltr">a</span> אינסוף פעמים".</div>

<div class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900 text-right text-[15px] leading-relaxed">
<b>ג. כן, יש <span dir="ltr">DBA</span>.</b> המשלים הוא <span dir="ltr"><KatexInline math="\Box\Diamond a" /></span> ("<span dir="ltr">a</span> אינסוף פעמים") - תכונת <b>חזרה</b> (recurrence), לא התמדה. בשונה מהתמדה, חזרה <b>אינה</b> דורשת מהאוטומט להחליט "סופית" שמשהו יציב לנצח - היא רק דורשת לחזור ולעבור דרך מצב מקבל בכל פעם ש-<span dir="ltr">a</span> מופיעה, וזו החלטה מקומית שאפשר לקבל בו-זמנית עם קריאת <span dir="ltr">a</span> עצמה.
</div>
