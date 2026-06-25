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
הפעילו את הבנייה על הדוגמה: <KatexInline math="TS" /> עם <span dir="ltr"><KatexInline math="S=\{s_0,s_1,s_2\}" /></span>, <span dir="ltr"><KatexInline math="s_0\xrightarrow{submit}s_1,\ s_1\xrightarrow{cancel}s_0,\ s_1\xrightarrow{grant}s_2,\ s_2\xrightarrow{release}s_0" /></span>, <span dir="ltr"><KatexInline math="L(s_0)=\emptyset,L(s_1)=\{requested\},L(s_2)=\{granted\}" /></span>, <KatexInline math="\varphi=\Box\Diamond granted" />, <span dir="ltr"><KatexInline math="\mathcal{F}=\langle\emptyset,\{\{grant\}\},\emptyset\rangle" /></span>. רשמו את <KatexInline math="TS'" /> (החלק הנגיש) ואת <KatexInline math="\varphi'" />.
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
<div class="bg-slate-50 border border-slate-200 rounded p-3"><KatexInline display math="AP'=AP\cup\{en_A,tk_A\mid A\in\Gamma\}" /></div>
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[16px]" dir="ltr">
<KatexInline display math="L'(\langle s,b\rangle)=L(s)\cup\{en_A\mid Post(s,A)\neq\emptyset\}\cup\{tk_A\mid b(A)=1\}" />
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[16px]" dir="ltr">
<KatexInline display math="\langle s,b\rangle\xrightarrow{\alpha}{}'\langle t,b'\rangle \iff s\xrightarrow{\alpha}t \ \land\ \forall A\in\Gamma\ \left(b'(A)=[\alpha\in A]\right)" />
</div>

<div class="mt-3 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] leading-relaxed" dir="ltr">
<KatexInline math="I'=\{\langle s_0,\vec{0}\rangle\mid s_0\in I\}" /> (הבחירה ההתחלתית של <KatexInline math="b" /> שרירותית, שכן אינה משפיעה על <KatexInline math="\Box\Diamond" />/<KatexInline math="\Diamond\Box" />).
</div>

---

# פתרון ב': <span dir="ltr"><KatexInline math="\theta_{\mathcal{F}},\varphi'" /></span> ונכונות

<div class="text-center text-[18px] mt-2" dir="ltr">
<KatexInline display math="\theta_{\mathcal{F}}=\bigwedge_{A\in\mathcal{F}_{uncond}}\Box\Diamond tk_A\ \land\ \bigwedge_{A\in\mathcal{F}_{strong}}(\Box\Diamond en_A\Rightarrow\Box\Diamond tk_A)\ \land\ \bigwedge_{A\in\mathcal{F}_{weak}}(\Diamond\Box en_A\Rightarrow\Box\Diamond tk_A)" />
</div>

<div class="text-center text-[22px] mt-3" dir="ltr">
<KatexInline display math="\varphi'=\theta_{\mathcal{F}}\Rightarrow\varphi" />
</div>

<div v-click class="mt-4 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed">
לכל ריצה <KatexInline math="\rho" /> של <KatexInline math="TS" />, יש בדיוק ריצה <KatexInline math="\rho'" /> של <KatexInline math="TS'" /> מעליה (ה-<KatexInline math="b" />-ים נקבעים חד-משמעית מהפעולות, פרט לראשון שאינו משנה); ולהפך, השמטת הסיביות מכל ריצה של <KatexInline math="TS'" /> נותנת ריצה של <KatexInline math="TS" />.
</div>

<div v-click class="mt-3 bg-blue-50 border border-blue-200 rounded p-3 text-[16px] leading-relaxed">
מבניית <KatexInline math="L'" />: <span dir="ltr"><KatexInline math="\rho'\models\theta_{\mathcal{F}}\iff\rho" /> הוגנת ביחס ל-<KatexInline math="\mathcal{F}" /></span> (כל מחובר תואם מילה במילה את הגדרת ההוֹגְנוּת), ו-<span dir="ltr"><KatexInline math="\rho'\models\varphi\iff\rho\models\varphi" /></span> (כי <KatexInline math="AP\subseteq AP'" /> והתיוג על <KatexInline math="AP" /> לא השתנה).
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-3 text-[17px] leading-relaxed">
לכן <span dir="ltr"><KatexInline math="TS'\models(\theta_{\mathcal{F}}\Rightarrow\varphi)\iff\forall\rho\ (\rho\ \mathcal{F}\text{-הוגנת}\Rightarrow\rho\models\varphi)\iff TS\models_{\mathcal{F}}\varphi" /></span>.
</div>

---

# פתרון ג': הבנייה על הדוגמה

<div class="text-right text-[16px] leading-relaxed mt-2">
<span dir="ltr"><KatexInline math="\Gamma=\{\{grant\}\}" /></span>, סיבית יחידה <KatexInline math="b\in\{0,1\}" />, <span dir="ltr"><KatexInline math="AP'=\{requested,granted,en_{grant},tk_{grant}\}" /></span>.
</div>

<div class="flex justify-center -mt-1 scale-[0.82] origin-top">
<TransitionSystemD3
  :width="600" :height="240"
  :states="[
    { id: 'a', text: '⟨s0,0⟩', initial: true, initialDirection: 'top', x: 300, y: 35, width: 110 },
    { id: 'b', text: '⟨s1,0⟩', x: 90, y: 230, width: 110 },
    { id: 'c', text: '⟨s2,1⟩', x: 510, y: 230, width: 110 }
  ]"
  :transitions="[
    { source: 'a', target: 'b', action: 'submit' },
    { source: 'b', target: 'a', action: 'cancel' },
    { source: 'b', target: 'c', action: 'grant' },
    { source: 'c', target: 'a', action: 'release' }
  ]"
/>
</div>

<div class="text-center text-[15px] -mt-2" dir="ltr">
<KatexInline math="L'(\langle s_0,0\rangle)=\emptyset,\quad L'(\langle s_1,0\rangle)=\{requested,en_{grant}\},\quad L'(\langle s_2,1\rangle)=\{granted,tk_{grant}\}" />
</div>

<div v-click class="mt-1 bg-slate-50 border border-slate-200 rounded p-2 text-[15px] leading-relaxed" dir="ltr">
החלק הנגיש: <KatexInline math="\{\langle s_0,0\rangle,\langle s_1,0\rangle,\langle s_2,1\rangle\}" /> בלבד (המצבים <KatexInline math="\langle s_0,1\rangle,\langle s_1,1\rangle,\langle s_2,0\rangle" /> אינם נגישים).
</div>

<div v-click class="mt-2 text-center text-[20px]" dir="ltr">
<KatexInline display math="\varphi'=\left(\Box\Diamond en_{grant}\Rightarrow\Box\Diamond tk_{grant}\right)\Rightarrow\Box\Diamond granted" />
</div>

---

# פתרון ד': שקילות ומסקנה

<div class="text-right text-[18px] leading-relaxed mt-3">
ההתאמה <span dir="ltr"><KatexInline math="\langle s_0,0\rangle\mapsto s_0,\ \langle s_1,0\rangle\mapsto s_1,\ \langle s_2,1\rangle\mapsto s_2" /></span> משרה התאמה חד-חד-ערכית בין הריצות (אותם מעברים ופעולות), ולכן <span dir="ltr"><KatexInline math="TS'" /></span> (החלק הנגיש) <span class="font-bold">שקול</span> ל-<KatexInline math="TS" />: מקיים בדיוק את אותן תכונות זמן ליניארי (לפי משפט שקילות העקבות), עם ההתאמה:
</div>

<div class="mt-3 bg-slate-50 border border-slate-200 rounded p-3 text-[18px] text-center" dir="ltr">
<KatexInline math="en_{grant}\equiv requested,\qquad tk_{grant}\equiv granted" />
</div>

<div v-click class="mt-3 bg-amber-50 border border-amber-200 rounded p-2 text-[15px] leading-relaxed">
מבנה <KatexInline math="TS" /> מבטיח שכל ריצה אינסופית חוזרת ל-<KatexInline math="s_1" /> אינסוף פעמים (מ-<KatexInline math="s_0" /> היחיד שמובילה ל-<KatexInline math="s_1" />; מ-<KatexInline math="s_2" /> היחיד שמובילה ל-<KatexInline math="s_0" /> ומשם ל-<KatexInline math="s_1" />), ולכן <KatexInline math="\Box\Diamond requested" /> מתקיים בכל ריצה.
</div>

<div v-click class="mt-3 bg-blue-50 border border-blue-200 rounded p-2 text-[15px] leading-relaxed text-right">
לפי השקילות <KatexInline math="(A\Rightarrow B)\Rightarrow B\equiv A\lor B" />: <KatexInline math="\varphi'\equiv\Box\Diamond requested\lor\Box\Diamond granted" />, ומכיוון שהמחובר הראשון מתקיים תמיד, <span class="font-bold">כל</span> ריצה מקיימת את <KatexInline math="\varphi'" />.
</div>

<div v-click class="mt-3 bg-emerald-50 border border-emerald-200 rounded p-2 text-[16px] leading-relaxed">
לכן <span dir="ltr"><KatexInline math="TS'\models\varphi'" /></span>, ולפי סעיף ב' מתקיים <span dir="ltr"><KatexInline math="TS\models_{\mathcal{F}}\varphi" /></span>: קיבלנו את התשובה ישירות מהבנייה, בלי לנמק בנפרד על הוֹגְנוּת על <KatexInline math="TS" /> המקורית.
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
