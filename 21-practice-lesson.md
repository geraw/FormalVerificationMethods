---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 21-practice-lesson
htmlAttrs:
  dir: rtl
  lang: he
drawings:
  enabled: true
info: |
  ## שאלות ממבחנים קודמים
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# שאלות ממבחנים קודמים

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="./public/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# שאלה 1 <span class="text-[16px] text-gray-500 font-normal">— מבחן ג', 2022, שאלה 2</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q01.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# פתרון שאלה 1 <span class="text-[16px] text-gray-500 font-normal">— סעיף 1</span>

<div class="text-right text-[14px] leading-snug mt-2">
הנוסחה בשאלה היא <KatexInline math="\square(p \rightarrow \bigcirc(\lozenge p \vee q))" />, וזו שקולה ל־<KatexInline math="\varphi = \square(\neg p \vee \bigcirc(\lozenge p \vee q))" /> לפי השקילות <KatexInline math="p \rightarrow \psi \equiv \neg p \vee \psi" />. לכן קיים עבורה אוטומט Büchi דטרמיניסטי:
</div>

<div class="mt-2 flex justify-center bg-white rounded-lg shadow border-2 border-slate-200 p-2">
<AutomatonD3 variant="classic" :width="420" :height="140" :arrowSize="4" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { id: 'q0', x: 75, y: 70, label: '$0$', initial: true, initialDirection: 'left', accepting: true, r: 18, labelWidth: 40 },
    { id: 'q1', x: 215, y: 70, label: '$1$', accepting: true, r: 18, labelWidth: 40 },
    { id: 'q2', x: 355, y: 70, label: '$2$', r: 18, labelWidth: 40 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$\\neg p$', loopDirection: '-90deg', labelWidth: 50, labelY: -8 },
    { source: 'q1', target: 'q1', label: '$p$', loopDirection: '-90deg', labelWidth: 35, labelY: -8 },
    { source: 'q2', target: 'q2', label: '$\\neg p$', loopDirection: '-90deg', labelWidth: 50, labelY: -8  },
    { source: 'q0', target: 'q1', label: '$p$', curve: 0.3, labelY: 10, labelWidth: 25 },
    { source: 'q1', target: 'q0', label: '$\\neg p \\wedge q$', curve: 0.3, labelY: -12, labelWidth: 80 },
    { source: 'q1', target: 'q2', label: '$\\neg p \\wedge \\neg q$', curve: 0.3, labelY: 10, labelWidth: 85 },
    { source: 'q2', target: 'q1', label: '$p$', curve: 0.3, labelY: -12, labelWidth: 25 }
  ]"
/>
</div>

<div class="text-right text-[12.5px] leading-snug mt-2">

כל פעם ש־<KatexInline math="p" /> מתקיים במצב <KatexInline math="i" />, נפתחת "חובה": במצב <KatexInline math="i+1" /> צריך <KatexInline math="q" />, <b>או</b> ש־<KatexInline math="p" /> יחזור בעתיד (<KatexInline math="\lozenge p" />). כל מצב מייצג את מידת החוב הפתוח:
<b>0 (מקבל)</b> — אין חוב; <KatexInline math="p" /> פותח חוב ← 1.
<b>1 (מקבל)</b> — חוב חדש, <KatexInline math="q" /> עדיין רלוונטי: <KatexInline math="\neg p \wedge q" /> סוגר ← 0; <KatexInline math="\neg p \wedge \neg q" /> מעביר להמתנה ← 2; <KatexInline math="p" /> סוגר וגם פותח חוב חדש (נשארים ב-1).
<b>2 (לא מקבל)</b> — ממתינים רק ל־<KatexInline math="\lozenge p" /> (<KatexInline math="q" /> לא רלוונטי יותר); <KatexInline math="p" /> סוגר וחוזר ← 1.
תנאי הקבלה (ביקור אינסופי ב-0/1) = כל חוב נסגר בזמן סופי; היתקעות לנצח ב-2 (אין עוד <KatexInline math="p" />) נדחית, כמו אי-קיום <KatexInline math="\varphi" />.

</div>

---

# פתרון שאלה 1 <span class="text-[16px] text-gray-500 font-normal">— סעיף 2</span>

<div class="text-right text-[14px] leading-snug mt-2">
גם עבור <KatexInline math="\varphi = p \, \mathsf{W} \, \bigcirc q" /> (כאשר <KatexInline math="\mathsf{W}" /> היא ה-Weak Until) קיים אוטומט דטרמיניסטי:
</div>

<div class="mt-2 flex justify-center bg-white rounded-lg shadow border-2 border-slate-200 p-2">
<AutomatonD3 variant="classic" :width="440" :height="230" :arrowSize="4" :stateLabelFontSize="14" :transitionLabelFontSize="13"
  :states="[
    { accepting: true, id: 'q0', x: 70, y: 100, label: '$0$', initial: true, initialDirection: 'left', r: 18, labelWidth: 40 },
    { accepting: true, id: 'q1', x: 230, y: 40, label: '$1$', r: 18, labelWidth: 40 },
    { accepting: true, id: 'q2', x: 230, y: 160, label: '$2$', r: 18, labelWidth: 40 },
    { accepting: true, id: 'q3', x: 380, y: 100, label: '$3$', r: 18, labelWidth: 40 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q1', label: '$\\neg p$', curve: -0.2, labelY: -8, labelWidth: 35 },
    { source: 'q0', target: 'q2', label: '$p$', curve: 0.2, labelY: 8, labelWidth: 25 },
    { source: 'q1', target: 'q3', label: '$q$', curve: -0.2, labelY: -8, labelWidth: 25 },
    { source: 'q2', target: 'q3', label: '$q$', curve: 0.2, labelY: 8, labelWidth: 25 },
    { source: 'q2', target: 'q1', label: '$\\neg p \\wedge \\neg q$', curve: 0, labelX: 36, labelWidth: 80 },
    { source: 'q2', target: 'q2', label: '$p \\wedge \\neg q$', loopDirection: '90deg', labelWidth: 70, labelY: 10 },
    { source: 'q3', target: 'q3', label: '$\\mathit{true}$', loopDirection: '-90deg', labelWidth: 50, labelY: -10 }
  ]"
/>
</div>

<div class="text-right text-[12.5px] leading-snug mt-2">

<KatexInline math="\varphi" /> אומרת: <KatexInline math="p" /> מחזיק עד (כולל) המצב שבו <KatexInline math="q" /> מתקיים במצב הבא, או ש־<KatexInline math="p" /> מחזיק לנצח. מצב 3 הוא "בור מקבל" — ברגע שנכנסים אליו (כי <KatexInline math="q" /> כבר הופיע) הכול מקבל תמיד.
<b>0 (התחלתי)</b> — עדיין לא ידוע אם <KatexInline math="p" /> יחזיק במצב זה; <KatexInline math="\neg p" /> ← 1 (בודקים אם זה כבר "המצב הבא" שצריך בו <KatexInline math="q" />), <KatexInline math="p" /> ← 2 (עדיין בתוך שרשרת ה-<KatexInline math="p" />).
<b>1</b> — כאן בודקים <KatexInline math="q" />: אם מתקיים ← 3 (התקבלנו); אחרת אין מעבר מוגדר — נדחה (הפרה של <KatexInline math="\varphi" />).
<b>2</b> — בתוך שרשרת ה-<KatexInline math="p" />: <KatexInline math="p \wedge \neg q" /> נשארים (השרשרת ממשיכה), <KatexInline math="\neg p \wedge \neg q" /> ← 1 (השרשרת נגמרה, בודקים אם זה כן "המצב הבא"), <KatexInline math="q" /> ← 3 (התקבלנו מוקדם).
<b>3</b> — בור מקבל, נשארים בו לנצח.

</div>

---

# פתרון שאלה 1 <span class="text-[16px] text-gray-500 font-normal">— סעיף 3</span>

<div class="text-right text-[14px] leading-snug mt-2">
גם לשפה <KatexInline math="\{\sigma \in (2^{AP})^\omega : \forall i . \exists j > i . \sigma[j] = \sigma[j+1]\}" /> (אינסוף חזרות עוקבות) קיים אוטומט Büchi דטרמיניסטי — הכי נוח לתאר אותו ישירות מתמטית. המצב הוא פשוט התו האחרון שנקרא (איבר של <KatexInline math="2^{AP}" />), חוץ ממצב התחלה ייעודי:
</div>

<div class="flex flex-col items-end gap-2 text-right text-[15px] mt-3">

<div><KatexInline math="Q = 2^{AP} \cup \{q_0\}" /> &nbsp; (<KatexInline math="q_0 \notin 2^{AP}" /> מצב התחלה)</div>

<div><KatexInline math="F = \{q_0\}" /></div>

<div><KatexInline math="\delta(A,B) = \begin{cases} q_0 & A = B \\ B & A \neq B \end{cases}" /> &nbsp; לכל <KatexInline math="A \in Q,\, B \in 2^{AP}" /></div>

</div>

<div class="text-right text-[12.5px] leading-snug mt-4">

כלומר: מ־<KatexInline math="q_0" /> תמיד עוברים ל־<KatexInline math="B" /> (זוכרים את התו הראשון). ממצב <KatexInline math="A \in 2^{AP}" />, קריאת אותו תו שוב (<KatexInline math="B=A" />) היא "התאמה" — חזרה עוקבת — ועוברים ל־<KatexInline math="q_0" /> (המצב המקבל); קריאת תו אחר פשוט מעדכנת את הזיכרון ל־<KatexInline math="B" />.

תנאי הקבלה <KatexInline math="\mathrm{Inf}(q_0)" /> — ביקור אינסופי ב־<KatexInline math="q_0" /> — שקול בדיוק לכך שקיימת אינסוף פעמים חזרה עוקבת <KatexInline math="\sigma[j]=\sigma[j+1]" />.

</div>

---

# שאלה 2 <span class="text-[16px] text-gray-500 font-normal">— מבחן מועד א', 2022, שאלה 3</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q02.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# פתרון שאלה 2 <span class="text-[16px] text-gray-500 font-normal">— המרה לנוסחה עם U בלבד</span>

<div class="text-right text-[16px] leading-relaxed mt-3">

האלגוריתם לבניית ה-GNBA (סגור, קבוצות עקביות) מוגדר רק על <KatexInline math="\wedge, \neg, \bigcirc, \mathsf{U}" />. לכן קודם ממירים את <KatexInline math="\varphi = p\, \mathsf{U}\, (p\, \mathsf{W}\, \bigcirc q)" /> לנוסחה שקולה בלי <KatexInline math="\mathsf{W}" />, לפי הזהויות מההרצאה:

<div class="flex flex-col items-end gap-2 mt-3">
<div><KatexInline math="\varphi_1 \mathbin{\mathsf{W}} \varphi_2 \equiv (\varphi_1 \mathbin{\mathsf{U}} \varphi_2) \vee \square \varphi_1" /></div>
<div><KatexInline math="\square \varphi \equiv \neg \lozenge \neg \varphi \equiv \neg(\mathit{true} \mathbin{\mathsf{U}} \neg\varphi)" /></div>
</div>

ולכן:

<div class="flex flex-col items-end gap-2 mt-3">
<div><KatexInline math="p \mathbin{\mathsf{W}} \bigcirc q \;\equiv\; (p \mathbin{\mathsf{U}} \bigcirc q) \vee \neg(\mathit{true} \mathbin{\mathsf{U}} \neg p)" /></div>
<div><KatexInline math="\varphi \;\equiv\; p \mathbin{\mathsf{U}} \Big[\, (p \mathbin{\mathsf{U}} \bigcirc q) \vee \neg(\mathit{true} \mathbin{\mathsf{U}} \neg p) \,\Big]" /></div>
</div>

זוהי הנוסחה שעליה נעבוד מכאן והלאה (בניית <KatexInline math="\operatorname{cl}(\varphi)" /> ומציאת הקבוצות העקביות).

</div>

---

# פתרון שאלה 2 <span class="text-[16px] text-gray-500 font-normal">— חישוב מצבי האוטומט</span>

<div class="text-right text-[12px] leading-snug mt-1">

נסמן <KatexInline math="\beta = \mathit{true}\,\mathsf{U}\,\neg p" />, <KatexInline math="\alpha = p\,\mathsf{U}\,\bigcirc q" />, <KatexInline math="\psi = \alpha \vee \neg\beta" />, <KatexInline math="\varphi = p\,\mathsf{U}\,\psi" />. <KatexInline math="\operatorname{cl}(\varphi)" /> מכיל את אלה, <KatexInline math="p,q,\bigcirc q,\mathit{true}" /> ושלילותיהם. כלל עקביות ל-<KatexInline math="\chi=\chi_1\,\mathsf{U}\,\chi_2" />: <KatexInline math="\chi_2\in B \Rightarrow \chi\in B" />, <KatexInline math="\chi\in B \Rightarrow (\chi_1\in B \vee \chi_2\in B)" /> — אם <KatexInline math="\chi_1\in B" /> אז <KatexInline math="\chi" /> חופשי (<KatexInline math="{}^*" />), אחרת נקבע. <KatexInline math="\psi" /> נקבע ישירות מ-<KatexInline math="\alpha,\beta" />.

</div>

<div class="mt-1 flex justify-center gap-6">
<div class="text-[10px]" style="line-height:1.15">

| # | <KatexInline math="p" /> | <KatexInline math="\bigcirc q" /> | <KatexInline math="\alpha" /> | <KatexInline math="\beta" /> | <KatexInline math="\psi" /> | <KatexInline math="\varphi" /> |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | T | T | T | T* | T | T |
| 2 | T | T | T | F* | T | T |
| 3 | T | F | T* | T* | T | T |
| 4 | T | F | T* | F* | T | T |
| 5 | T | F | F* | T* | F | T* |

</div>
<div class="text-[10px]" style="line-height:1.15">

| # | <KatexInline math="p" /> | <KatexInline math="\bigcirc q" /> | <KatexInline math="\alpha" /> | <KatexInline math="\beta" /> | <KatexInline math="\psi" /> | <KatexInline math="\varphi" /> |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 6 | T | F | F* | T* | F | F* |
| 7 | T | F | F* | F* | T | T |
| 8 | F | T | T | T | T | T |
| 9 | F | F | F | T | F | F |

</div>
</div>

<div class="text-right text-[11px] leading-snug mt-1">

<KatexInline math="{}^*" />=בחירה חופשית. גם <KatexInline math="q" /> הנוכחי הוא ביט חופשי בלתי-תלוי (מופיע רק בתוך <KatexInline math="\bigcirc q" />) — כל שורה מתפצלת ל-2 מצבים, ובסך הכול <KatexInline math="9\times2=18" /> קבוצות עקביות. מצב התחלה חוקי = כל קבוצה עם <KatexInline math="\varphi\in B" /> (כל השורות מלבד 6,9).

</div>

---

# פתרון שאלה 2 <span class="text-[16px] text-gray-500 font-normal">— מעברים ותנאי הקבלה (GNBA)</span>

<div class="text-right text-[14px] leading-relaxed mt-2">

<b>תווית היציאה מ-<KatexInline math="B" /></b> נקבעת ישירות: <KatexInline math="a \in B \iff a \in L(B)" /> כאשר <KatexInline math="L(B)" /> היא התווית של <KatexInline math="B" /> (וכאן <KatexInline math="a\in\{p,q\}" />) — כלומר <KatexInline math="B" /> "קורא" בדיוק את <KatexInline math="p,q" /> שהוא מכיל.

<b>מעבר</b>: <KatexInline math="B \xrightarrow{\;B\cap AP\;} B'" /> מותר אם"ם <KatexInline math="\bigcirc q \in B \iff q \in B'" /> (זו ההגבלה היחידה — <KatexInline math="\bigcirc q" /> הוא איבר ה-<KatexInline math="\bigcirc" /> היחיד ב-<KatexInline math="\operatorname{cl}(\varphi)" />). כלומר מ-<KatexInline math="B" /> אפשר לעבור לכל אחת מ-9 הקבוצות (מתוך ה-18) שבהן <KatexInline math="q" /> תואם את <KatexInline math="\bigcirc q" /> של <KatexInline math="B" /> — אוטומט לא-דטרמיניסטי לגמרי. לפי מספור השורות מהטבלה הקודמת (וללא תלות בביט <KatexInline math="q" /> החופשי של המקור, שרק קובע את חלק התווית הנקרא):

<div class="mt-1 flex justify-center gap-6">
<div class="text-[10px]" style="line-height:1.15">

| מ-# | <KatexInline math="p" /> | <KatexInline math="\bigcirc q" /> | יעד: <KatexInline math="q'" /> נדרש |
|:-:|:-:|:-:|:-:|
| 1 | T | T | T |
| 2 | T | T | T |
| 3 | T | F | F |
| 4 | T | F | F |
| 5 | T | F | F |

</div>
<div class="text-[10px]" style="line-height:1.15">

| מ-# | <KatexInline math="p" /> | <KatexInline math="\bigcirc q" /> | יעד: <KatexInline math="q'" /> נדרש |
|:-:|:-:|:-:|:-:|
| 6 | T | F | F |
| 7 | T | F | F |
| 8 | F | T | T |
| 9 | F | F | F |

</div>
</div>

<div class="text-right text-[11px] leading-snug mt-1">

כלומר: מ-<KatexInline math="B" /> בשורה <KatexInline math="\#r" /> (עם <KatexInline math="q" /> נוכחי כלשהו) קוראים את <KatexInline math="(p_r,q)" /> ועוברים לכל אחת מ-9 השורות <KatexInline math="1,\dots,9" /> שבהן <KatexInline math="q'" /> שווה לערך <KatexInline math="\bigcirc q" /> של השורה — היעד תלוי רק בשורה של המקור, לא בביט <KatexInline math="q" /> הנוכחי שלו.

</div>

<b>תנאי קבלה מוכלל</b> — קבוצת קבלה אחת לכל תת-נוסחת <KatexInline math="\mathsf{U}" /> ב-<KatexInline math="\operatorname{cl}(\varphi)" />:

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="F_\varphi = \{B : \varphi\notin B \;\vee\; \psi\in B\}" /></div>
<div><KatexInline math="F_\alpha = \{B : \alpha\notin B \;\vee\; \bigcirc q\in B\}" /></div>
<div><KatexInline math="F_\beta = \{B : \beta\notin B \;\vee\; \neg p\in B\}" /></div>
</div>

ריצה מתקבלת אם"ם היא מבקרת בכל אחת מ-<KatexInline math="F_\varphi,F_\alpha,F_\beta" /> אינסוף פעמים. מצבי התחלה = כל <KatexInline math="B" /> עם <KatexInline math="\varphi\in B" />. זהו ה-GNBA המבוקש (אין צורך להמיר ל-NBA).

</div>

---

# פתרון שאלה 2 <span class="text-[16px] text-gray-500 font-normal">— סעיף 3: האם קיים אוטומט דטרמיניסטי?</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

<b>לא.</b> נציב <KatexInline math="q \equiv \mathit{false}" /> תמיד (הצבה זו היא תכונת בטיחות, ולכן אם היה קיים DBA ל-<KatexInline math="\varphi" /> היה קיים גם לחיתוך שלו איתה):

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="\bigcirc q \equiv \mathit{false} \;\Rightarrow\; \alpha = p\,\mathsf{U}\,\bigcirc q \equiv \mathit{false}" /></div>
<div><KatexInline math="\psi = \alpha \vee \neg\beta \equiv \neg\beta \equiv \square p" /></div>
<div><KatexInline math="\varphi \equiv p\,\mathsf{U}\,\square p \;=\; \lozenge\square p" /></div>
</div>

כלומר על התת-שפה <KatexInline math="q\equiv \mathit{false}" />, השפה של <KatexInline math="\varphi" /> שקולה בדיוק ל־<KatexInline math="\lozenge\square p" /> ("מתישהו <KatexInline math="p" /> מחזיק לצמיתות") — הדוגמה הקלאסית מההרצאה לתכונה <b>בלי</b> אוטומט Büchi דטרמיניסטי (כל DBA שמנחש "עכשיו מתחיל הלעד" יכול תמיד להיות מופרך על ידי הפרה מאוחרת ככל שנרצה של <KatexInline math="p" />).

מאחר שאוטומטים דטרמיניסטיים סגורים לחיתוך עם תכונות בטיחות, אילו קיים DBA ל-<KatexInline math="\varphi" /> היה קיים גם ל-<KatexInline math="\lozenge\square p" /> — סתירה. <b>לכן לא קיים אוטומט Büchi דטרמיניסטי המקבל את <KatexInline math="\varphi" />.</b>

</div>

---

# שאלה 3 <span class="text-[16px] text-gray-500 font-normal">— מבחן מועד ב', 2022, שאלה 2</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q03.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

<div class="text-center text-[12px] text-gray-500 mt-2">
הבהרה לסעיף 3: <KatexInline math="\sigma[0]" /> היא קבוצה (ב-<KatexInline math="2^{\{0,\dots,9\}}" />), לא מספר — יש לקרוא את התכונה כ-<KatexInline math="\{\sigma:\forall i.\ \sigma[\,|\sigma[0]|\cdot i\,]=\sigma[1]\}" />, כאשר <KatexInline math="|\sigma[0]|" /> הוא גודל הקבוצה במיקום 0.
</div>

---

# פתרון שאלה 3 <span class="text-[16px] text-gray-500 font-normal">— סעיף 1: מוכלל דטרמיניסטי ⇐ רגיל דטרמיניסטי</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

<b>נכון.</b> יהי <KatexInline math="A=(Q,\Sigma,\delta,q_0,\{F_1,\dots,F_k\})" /> GNBA דטרמיניסטי (כלומר <KatexInline math="\delta" /> היא פונקציה). בונים אוטומט בוקי רגיל <KatexInline math="A'=(Q\times\{1,\dots,k\},\Sigma,\delta',(q_0,1),F)" /> — בדיוק הבנייה הרגילה מהקורס להמרת GNBA ל-NBA:

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="\delta'((q,j),a) = (\delta(q,a),\, \mathrm{next}(q,j))" /></div>
<div><KatexInline math="\mathrm{next}(q,j) = \begin{cases} (j \bmod k) + 1 & q \in F_j \\ j & q \notin F_j \end{cases}" /></div>
<div><KatexInline math="F = F_1 \times \{1\}" /></div>
</div>

הרכיב השני "זוכר" איזו קבוצת קבלה מחכים לה כרגע; כשמגיעים אליה עוברים לחכות לקבוצה הבאה. ריצה מבקרת ב-<KatexInline math="F_1\times\{1\}" /> אינסוף פעמים אם"ם היא "מסתובבת" סביב כל ה-<KatexInline math="F_1,\dots,F_k" /> אינסוף פעמים, כלומר מבקרת בכל אחת מהן אינסוף פעמים — בדיוק תנאי הקבלה המוכלל המקורי.

<b>דטרמיניזם נשמר:</b> <KatexInline math="\mathrm{next}(q,j)" /> נקבע לגמרי לפי <KatexInline math="(q,j)" /> (ללא ניחוש), ו-<KatexInline math="\delta" /> דטרמיניסטית בהנחה — ולכן גם <KatexInline math="\delta'" /> היא פונקציה. קיבלנו אוטומט בוקי רגיל <b>דטרמיניסטי</b> לאותה שפה.

</div>

---

# פתרון שאלה 3 <span class="text-[16px] text-gray-500 font-normal">— סעיף 2: סגירות דטרמיניסטית לחיתוך</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

<b>נכון.</b> יהיו <KatexInline math="\mathcal{A}_1=(Q_1,\Sigma,\delta_1,q_1^0,F_1)" />, <KatexInline math="\mathcal{A}_2=(Q_2,\Sigma,\delta_2,q_2^0,F_2)" /> אוטומטי בוקי דטרמיניסטיים (מלאים) עם <KatexInline math="P_i=\mathcal{L}_\omega(\mathcal{A}_i)" />. בונים מכפלה:

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="\delta_\times((s_1,s_2),a) = (\delta_1(s_1,a),\, \delta_2(s_2,a))" /> &nbsp; — פונקציה, כי <KatexInline math="\delta_1,\delta_2" /> פונקציות</div>
<div><KatexInline math="G_1 = F_1\times Q_2, \qquad G_2 = Q_1\times F_2" /></div>
</div>

ריצה יחידה <KatexInline math="\rho" /> של המכפלה על <KatexInline math="\sigma" /> מוקרנת לריצות היחידות <KatexInline math="\rho_1,\rho_2" /> של <KatexInline math="\mathcal{A}_1,\mathcal{A}_2" />. מכיוון שהאוטומטים דטרמיניסטיים ומלאים: <KatexInline math="\rho" /> מבקרת ב-<KatexInline math="G_1" /> אינסוף פעמים <KatexInline math="\iff" /> <KatexInline math="\rho_1" /> מבקרת ב-<KatexInline math="F_1" /> אינסוף פעמים <KatexInline math="\iff" /> <KatexInline math="\sigma\in P_1" />, ובאותו אופן עבור <KatexInline math="G_2,P_2" />. לכן:

<div class="mt-2"><KatexInline math="\sigma \text{ מתקבל לפי } \{G_1,G_2\} \iff \sigma \in P_1\cap P_2" /></div>

כלומר <KatexInline math="(Q_1\times Q_2,\Sigma,\delta_\times,(q_1^0,q_2^0),\{G_1,G_2\})" /> הוא <b>GNBA דטרמיניסטי</b> ל-<KatexInline math="P_1\cap P_2" />. לפי סעיף 1, קיים ממנו גם אוטומט בוקי <b>רגיל דטרמיניסטי</b> <KatexInline math="\mathcal{A}" /> עם <KatexInline math="P_1\cap P_2=\mathcal{L}_\omega(\mathcal{A})" />. (כלומר: אוטומטי בוקי דטרמיניסטיים סגורים לחיתוך — אך, כידוע, לא לשלילה.)

</div>

---

# פתרון שאלה 3 <span class="text-[16px] text-gray-500 font-normal">— סעיף 3: קיים בוקי, אך לא LTL</span>

<div class="text-right text-[14px] leading-snug mt-3">

<b>נכון.</b> נסמן <KatexInline math="AP=\{0,\dots,9\}" />, כך ש-<KatexInline math="\sigma[0]\subseteq AP" />, ונגדיר <KatexInline math="p := |\sigma[0]|\in\{0,\dots,10\}" /> — <b>גודל</b> (עוצמת) הקבוצה במיקום 0, לא תוכנה. התכונה, בניסוח מדויק, היא <KatexInline math="\{\sigma:\forall i.\ \sigma[\,|\sigma[0]|\cdot i\,]=\sigma[1]\}" />: כל מיקום שהוא כפולה של <KatexInline math="p" /> (<KatexInline math="0,p,2p,\dots" />) נושא את אותה אות כמו <KatexInline math="\sigma[1]" />.

<b>קיים אוטומט בוקי (אף דטרמיניסטי!):</b> בונים אוטומט עם שלב "קריאת <KatexInline math="\sigma[0]" />" (קביעת <KatexInline math="p=|\sigma[0]|" />), שלב "קריאת <KatexInline math="\sigma[1]" />" (שמירת האות <KatexInline math="b" />), ואז מונה <KatexInline math="c\in\{0,\dots,p-1\}" /> (מיקום מודולו <KatexInline math="p" />, סופי כי <KatexInline math="p\le 10" />): בכל <KatexInline math="c=0" /> בודקים שהאות הנוכחית <KatexInline math="=b" />; אם לא — עוברים למצב "מלכודת" לא-מקבל עם לולאה עצמית לנצח. <KatexInline math="F=" /> כל המצבים חוץ מהמלכודת. זו תכונת בטיחות: המילה מתקבלת אם"ם אף פעם לא נכנסים למלכודת אם"ם התכונה מתקיימת — ולכן זהו למעשה DBA (מספר המצבים סופי כי <KatexInline math="p\le 10" />).

<b>אין נוסחת LTL:</b> קבעו <KatexInline math="p\ge 2" />. הקבוצה <KatexInline math="\{\sigma:|\sigma[0]|=p\}" /> ניתנת לביטוי ב-LTL (תנאי על שתי האותיות הראשונות בלבד). אילו התכונה כולה הייתה LTL-בת-ביטוי, אז (מסגירות LTL תחת חיתוך/<KatexInline math="\wedge" />) גם החיתוך שלה עם קבוצה זו היה LTL-בת-ביטוי — וזו בדיוק תכונת "ספירה מודולו <KatexInline math="p" />" (כל מיקום ה-<KatexInline math="p" />-י שווה לעוגן קבוע), המקבילה לדוגמה הקלאסית (כגון "<KatexInline math="q" /> מתקיים בכל מיקום זוגי") שאינה שפה star-free/aperiodic, ולכן (ממשפט קמפ, <KatexInline math="\mathrm{LTL}=\text{star-free}" />) אינה LTL-בת-ביטוי — סתירה. לכן אין נוסחת LTL לתכונה.

</div>

---

# שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— מועד א', 2024, שאלה 1</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q04.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף א: מודל צ'קינג ישיר מול אוטומט דטרמיניסטי</span>

<div class="text-right text-[14px] leading-relaxed mt-2">

<b>נכון</b> (עבור <KatexInline math="|Q_0|=1" />, ו-<KatexInline math="TS" /> ללא מצבים סופניים, כרגיל). נסמן <KatexInline math="Q_0=\{q_0\}" />. מכיוון ש-<KatexInline math="\delta" /> <b>פונקציה מלאה</b>, לכל מילה <KatexInline math="\sigma=A_0A_1\cdots" /> יש <b>ריצה יחידה</b> <KatexInline math="q_0,q_1,\dots" /> (<KatexInline math="q_{i+1}=\delta(q_i,A_i)" />), ו-<KatexInline math="\sigma\in\mathcal{L}_\omega(\mathcal{A}) \iff" /> הריצה מבקרת ב-<KatexInline math="F" /> אינסוף פעמים <KatexInline math="\iff" /> (כי <KatexInline math="F" /> סופית, שובך יונים) קיים <KatexInline math="q\in F" /> שמבוקר אינסוף פעמים.

באותה סיבה (דטרמיניזם + שלמות + מצב התחלה יחיד), לכל נתיב <KatexInline math="\pi" /> ב-<KatexInline math="TS" /> מ-<KatexInline math="Init(TS)" /> יש <b>נתיב מכפלה יחיד</b> תואם ב-<KatexInline math="TS\times\mathcal{A}" /> מ-<KatexInline math="Init(TS)\times\{q_0\}" />, וההתאמה היא חד-חד-ערכית ועל בין נתיבי <KatexInline math="TS" /> לנתיבי <KatexInline math="TS\times\mathcal{A}" />. לכן:

<div class="mt-2 text-center">
<KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> &nbsp;<KatexInline math="\iff" />&nbsp; כל עקבה של <KatexInline math="TS" /> מתקבלת ע"י <KatexInline math="\mathcal{A}" /> &nbsp;<KatexInline math="\iff" />&nbsp; כל נתיב-מכפלה מבקר ב-<KatexInline math="F" /> אינסוף פעמים &nbsp;<KatexInline math="\iff" />&nbsp; <KatexInline math="TS\times\mathcal{A}\models\bigvee_{q\in F}\square\Diamond q" />
</div>

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף א (המשך): מה קורה אם <KatexInline math="|Q_0|=2" />?</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

<b>כן, משנה את התשובה — הטענה נהיית שגויה.</b> ההוכחה למעלה נשענת קריטית על ריצה <b>יחידה</b> לכל מילה; עם שני מצבי התחלה זה קורס, כי <KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> דורש <b>קיום</b> ריצה מקבלת (מאחד משני המצבים ההתחלתיים), בעוד ש-<KatexInline math="TS\times\mathcal{A}" /> (עם <KatexInline math="Init=Init(TS)\times Q_0" />) דורש שהתנאי יתקיים <b>לכל</b> נתיב, כולל אלו שמתחילים במצב ה"לא נכון".

<b>דוגמה נגדית:</b> <KatexInline math="AP=\emptyset" /> (אות יחידה <KatexInline math="\emptyset" />), <KatexInline math="Q=\{q_0,q_1\}" />, <KatexInline math="Q_0=\{q_0,q_1\}" />, <KatexInline math="F=\{q_1\}" />, <KatexInline math="\delta(q_0,\emptyset)=q_0" />, <KatexInline math="\delta(q_1,\emptyset)=q_1" /> (שני מצבים בלולאה עצמית). המילה היחידה <KatexInline math="\emptyset^\omega" /> מתקבלת (דרך הריצה המתחילה ב-<KatexInline math="q_1" />), ולכן <KatexInline math="\mathcal{L}_\omega(\mathcal{A})=\{\emptyset^\omega\}" /> = כל השפה. עבור <KatexInline math="TS" /> עם מצב יחיד <KatexInline math="s_0" /> (עם לולאה עצמית): <KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> <b>מתקיים</b> (טריוויאלית). אבל ב-<KatexInline math="TS\times\mathcal{A}" /> יש נתיב שמתחיל ב-<KatexInline math="(s_0,q_0)" /> ולעולם לא מבקר ב-<KatexInline math="q_1\in F" /> — ולכן <KatexInline math="TS\times\mathcal{A}\not\models\square\Diamond q_1" />. <b>סתירה לשקילות.</b>

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף א: תרשים הדוגמה הנגדית</span>

<div class="mt-4 flex justify-center items-start gap-10">

<div class="flex flex-col items-center">
<div class="text-[13px] font-bold mb-1"><KatexInline math="TS" /></div>
<TransitionSystem
  :width="160" :height="130"
  :states="[
    { id: 's0', name: 's0', x: 80, y: 65, initial: true, initialDirection: 'top' }
  ]"
  :transitions="[
    { source: 's0', target: 's0', loopDirection: '-90deg', loopSweep: '90deg' }
  ]"
/>
</div>

<div class="flex flex-col items-center">
<div class="text-[13px] font-bold mb-1"><KatexInline math="\mathcal{A}" /> &nbsp; (<KatexInline math="|Q_0|=2" />)</div>
<AutomatonD3 variant="classic" :width="260" :height="130" :arrowSize="4" :stateLabelFontSize="14" :transitionLabelFontSize="12"
  :states="[
    { id: 'q0', x: 70, y: 65, label: '$q_0$', initial: true, initialDirection: 'left', accepting: false, r: 18, labelWidth: 30 },
    { id: 'q1', x: 200, y: 65, label: '$q_1$', initial: true, initialDirection: 'right', accepting: true, r: 18, labelWidth: 30 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '', loopDirection: '-90deg', labelWidth: 10, labelY: -8 },
    { source: 'q1', target: 'q1', label: '', loopDirection: '-90deg', labelWidth: 10, labelY: -8 }
  ]"
/>
</div>

<div class="flex flex-col items-center">
<div class="text-[13px] font-bold mb-1"><KatexInline math="TS\times\mathcal{A}" /></div>
<TransitionSystem
  :width="260" :height="130"
  :states="[
    { id: 'p0', name: '(s0,q0)', x: 90, y: 65, initial: true, initialDirection: 'top' },
    { id: 'p1', name: '(s0,q1)', label: 'F', x: 230, y: 65, initial: true, initialDirection: 'top' }
  ]"
  :transitions="[
    { source: 'p0', target: 'p0', loopDirection: '-90deg', loopSweep: '90deg' },
    { source: 'p1', target: 'p1', loopDirection: '-90deg', loopSweep: '90deg' }
  ]"
/>
</div>

</div>

<div class="text-right text-[13px] leading-snug mt-6">

<KatexInline math="q_1" /> (מקבל, מסומן בכפול) הוא היחיד ב-<KatexInline math="F" />. ב-<KatexInline math="\mathcal{A}" /> עצמו יש <b>קיום</b> ריצה מקבלת עבור <KatexInline math="\emptyset^\omega" /> (זו שמתחילה ב-<KatexInline math="q_1" />) — ולכן <KatexInline math="\mathcal{L}_\omega(\mathcal{A})" /> היא כל השפה ו-<KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> מתקיים. אבל ב-<KatexInline math="TS\times\mathcal{A}" /> <b>שני</b> מצבי ההתחלה ממשיכים כל אחד בנתיב נפרד: הנתיב מ-<KatexInline math="(s_0,q_0)" /> (משמאל, לא מקבל) <b>לעולם לא</b> מבקר במצב מקבל — לכן <KatexInline math="TS\times\mathcal{A}\not\models\bigvee_{q\in F}\square\Diamond q" />, למרות ש-<KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" />. אי-ההתאמה בין "קיום ריצה מקבלת" (בהגדרת <KatexInline math="\mathcal{L}_\omega" />) ל"כל הנתיבים במכפלה" (בהגדרת ההתמדה של המכפלה) היא בדיוק מה שדורש מצב התחלה יחיד.

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף ב: האם כל שמורה היא התמדה?</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

<b>שגוי.</b> נכון ש-<KatexInline math="P_{\mathrm{inv}}(\Phi)\subseteq P_{\mathrm{per}}(\Phi)" /> באופן טריוויאלי (אם <KatexInline math="\Phi" /> מתקיים תמיד, בפרט הוא מתקיים החל ממקום 0) — אבל השאלה היא האם <b>שפת</b> השמורה עצמה <b>שווה</b> לאיזושהי שפת התמדה (עם נוסחת מצב <KatexInline math="\Psi" /> כלשהי, לאו דווקא <KatexInline math="\Phi" />), וזה כבר לא נכון עבור שמורה לא-טריוויאלית.

<b>דוגמה נגדית:</b> יהי <KatexInline math="p\in AP" />, <KatexInline math="\Phi=p" /> (לא טאוטולוגיה ולא סתירה). <KatexInline math="P_{\mathrm{inv}}(p)=X^\omega" /> כאשר <KatexInline math="X=\{A\subseteq AP: p\in A\}\neq\emptyset,\Sigma" />. נניח בשלילה שקיימת <KatexInline math="\Psi" /> עם <KatexInline math="P_{\mathrm{per}}(\Psi)=X^\omega" />, ונסמן <KatexInline math="Y=\{A:A\models\Psi\}" />, כך ש-<KatexInline math="\Sigma^*Y^\omega = X^\omega" />. אם <KatexInline math="Y\neq\emptyset" />, בחרו <KatexInline math="A_0\notin X" /> (קיים כי <KatexInline math="X\neq\Sigma" />) ו-<KatexInline math="B\in Y" />: המילה <KatexInline math="A_0B^\omega \in \Sigma^*Y^\omega=X^\omega" />, אך אות ראשונה <KatexInline math="A_0\notin X" /> סותרת <KatexInline math="A_0B^\omega\in X^\omega" /> (השמורה דורשת <KatexInline math="X" /> <b>בכל</b> מיקום, כולל הראשון). אם <KatexInline math="Y=\emptyset" /> אז <KatexInline math="P_{\mathrm{per}}(\Psi)=\emptyset\neq X^\omega" /> (כי <KatexInline math="X\neq\emptyset" />). בשני המקרים סתירה. <b>לכן אין <KatexInline math="\Psi" /> כזו — השמורה <KatexInline math="P_{\mathrm{inv}}(p)" /> אינה תכונת התמדה.</b>

<div class="mt-1 text-[12.5px] text-gray-600">(זהו בדיוק המשפט מההרצאה: שוויון בין שמורה להתמדה מתקיים רק במקרים הטריוויאליים <KatexInline math="\Phi\equiv\mathit{true}" /> או <KatexInline math="\Phi\equiv\mathit{false}" />.)</div>

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף ג: עקביות בבניית ה-GNBA</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

<b>לא ייתכן — הצירוף בהכרח לא עקבי</b>, בלי שום תלות בתנאים על <KatexInline math="\varphi\in B" /> או <KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\notin B" />: הסתירה נובעת רק מ-<KatexInline math="\bigcirc\varphi\notin B" />, <KatexInline math="B'\in\delta(B,B\cap AP)" /> ו-<KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\notin B'" />.

<b>הוכחה:</b> לפי כלל המעבר על תת-נוסחאות <KatexInline math="\bigcirc" /> (המשמש בבניה, ראו שאלה 2): <KatexInline math="B\xrightarrow{B\cap AP}B'" /> חוקי רק אם <KatexInline math="\bigcirc\varphi\in B \iff \varphi\in B'" />. בהינתן <KatexInline math="\bigcirc\varphi\notin B" />, נובע <KatexInline math="\varphi\notin B'" />. מעקביות (שלמות) <KatexInline math="B'" /> — לכל תת-נוסחה בדיוק אחת מבין <KatexInline math="\varphi,\neg\varphi" /> שייכת ל-<KatexInline math="B'" /> — מקבלים <KatexInline math="\neg\varphi\in B'" />.

כעת מפעילים את כלל העקביות ל-Until <KatexInline math="\chi=\varphi\,\mathsf{U}\,\neg\varphi" /> (עם <KatexInline math="\chi_1=\varphi,\ \chi_2=\neg\varphi" />) על <KatexInline math="B'" />: <KatexInline math="\chi_2\in B' \Rightarrow \chi\in B'" />, כלומר <KatexInline math="\neg\varphi\in B' \Rightarrow \varphi\,\mathsf{U}\,\neg\varphi\in B'" />. קיבלנו <KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\in B'" /> — <b>בסתירה</b> לדרישה <KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\notin B'" />.

לכן צירוף המצבים המבוקש אינו יכול להתקיים באף הרצה של הבניה. <KatexInline math="\blacksquare" />

</div>

---

# שאלה 5 <span class="text-[16px] text-gray-500 font-normal">— מועד א' מילואים, 2024, שאלה 2</span>

<div class="flex justify-center items-start mt-1">
<img src="./public/practice-lesson-21/q05.png" class="max-w-[85%] max-h-[480px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# פתרון שאלה 5 <span class="text-[16px] text-gray-500 font-normal">— סעיף a: שקילות בין הוגנות ל-LTL</span>

<div class="text-right text-[14px] leading-relaxed mt-2">

<b>שגוי.</b> נסתור כבר את השוויון הראשון (בין שתי צורות ההוגנות <b>על אותה</b> <KatexInline math="TS_1" />), בעזרת <KatexInline math="\varphi=\mathit{false}" /> (למשל <KatexInline math="p\wedge\neg p" /> עבור <KatexInline math="p" /> כלשהו, נוסחה שאינה מכילה <KatexInline math="\alpha,\beta" />).

ב-<KatexInline math="TS_1" />, הפעולה <KatexInline math="\alpha" /> אפשרית <b>רק</b> מ-<KatexInline math="s_1" /> (ל-<KatexInline math="s_2" />), ואין דרך חזרה מ-<KatexInline math="s_2" /> ל-<KatexInline math="s_1" />. לכן:

<div class="flex flex-col gap-1 mt-2">
<div>• <b>הוגנות בלתי-מותנית</b> <KatexInline math="\langle\{\{\alpha\}\},\emptyset,\emptyset\rangle" />: דורשת <KatexInline math="\alpha" /> <b>נלקחת אינסוף פעמים</b> — בלתי אפשרי (נלקחת לכל היותר פעם אחת, ולאחר מכן לעולם לא זמינה שוב). לכן <KatexInline math="\mathit{FairTraces}=\emptyset" />, וההכלה <KatexInline math="\emptyset\subseteq\mathcal{L}(\varphi)" /> מתקיימת <b>תמיד</b>, טריוויאלית — כלומר <KatexInline math="TS_1\models_{\langle\{\{\alpha\}\},\emptyset,\emptyset\rangle}\varphi" /> <b>לכל</b> <KatexInline math="\varphi" /> (גם <KatexInline math="\varphi=\mathit{false}" />!). זו בדיוק הנחת הוגנות <b>שאינה בת-מימוש</b> (המצב <KatexInline math="s_2" /> נגיש אך חסר ריצות הוגנות ממנו) — בדיוק כפי שראינו בהרצאה שהוגנות בלתי-ממומשת עלולה לקלקל גם תכונות בטיחות.</div>
<div>• <b>הוגנות חזקה</b> <KatexInline math="\langle\emptyset,\emptyset,\{\{\alpha\}\}\rangle" />: דורשת רק <b>אם</b> <KatexInline math="\alpha" /> מאופשרת אינסוף פעמים <b>אז</b> נלקחת אינסוף פעמים. מסלול שנשאר לנצח ב-<KatexInline math="s_1" /> (לוקח רק <KatexInline math="\beta" />): <KatexInline math="\alpha" /> מאופשרת תמיד אך לעולם לא נלקחת — <b>מפר</b> הוגנות חזקה, נפסל. אבל מסלול שעובר בשלב כלשהו ל-<KatexInline math="s_2" />: אחרי המעבר <KatexInline math="\alpha" /> כבר לא מאופשרת אף פעם, כך שהתנאי "מאופשרת אינסוף פעמים" שקרי — ההוגנות מתקיימת <b>בריק</b>. לכן <KatexInline math="\mathit{FairTraces}=\{L_1^k L_2^\omega : k\ge0\}\neq\emptyset" />, וההכלה בתוך <KatexInline math="\mathcal{L}(\mathit{false})=\emptyset" /> <b>נכשלת</b>.</div>
</div>

מכיוון ש-<KatexInline math="\emptyset\subsetneq\{L_1^kL_2^\omega:k\ge0\}" />, קיבלנו <KatexInline math="TS_1\models_{\langle\{\{\alpha\}\},\emptyset,\emptyset\rangle}\mathit{false}" /> (אמת) אך <KatexInline math="TS_1\not\models_{\langle\emptyset,\emptyset,\{\{\alpha\}\}\rangle}\mathit{false}" /> (שקר) — הצדדים <b>אינם שקולים</b>. (בניגוד ל-<KatexInline math="TS_2" />, שם דווקא ניתן לקחת <KatexInline math="\alpha" /> אינסוף פעמים — שם ההנחה <b>כן</b> בת-מימוש, ולכן היא לא נכללת בסתירה הזו, אבל היא גם לא מצילה את השקילות הכוללת הנדרשת.)

</div>

---

# פתרון שאלה 5 <span class="text-[16px] text-gray-500 font-normal">— סעיף b: תכונה ללא אוטומט "כמעט-דטרמיניסטי"</span>

<div class="text-right text-[14px] leading-relaxed mt-2">

<b>כן, קיימת</b> — לדוגמה <KatexInline math="P=\Diamond\square p" /> ("בסופו של דבר <KatexInline math="p" /> מחזיק לצמיתות", תכונת ההתמדה הקלאסית). נשים לב שאוטומט כזה (עם <KatexInline math="\max|\delta(q,A)|=1" />, כלומר מעברים דטרמיניסטיים אך אולי חלקיים, ועם <b>מספר מצבי התחלה חופשי</b>) שקול לגמרי <b>לאיחוד סופי</b> של DBA-ים רגילים (מצב התחלה יחיד, מעברים שלמים) — ולכן לא חזק יותר מאוטומט בוקי דטרמיניסטי רגיל:

<b>שלב 1 — רדוקציה לאיחוד של DBA-ים:</b> אם <KatexInline math="Q_0=\{q_1,\dots,q_k\}" />, אז <KatexInline math="\mathcal{L}_\omega(\mathcal{A})=\bigcup_i \mathcal{L}_\omega(\mathcal{A}_i)" /> כאשר <KatexInline math="\mathcal{A}_i" /> הוא אותו אוטומט עם <KatexInline math="Q_0=\{q_i\}" /> בלבד. משלימים כל <KatexInline math="\mathcal{A}_i" /> למעברים מלאים (מוסיפים מצב "בור" לא מקבל לכל מעבר לא-מוגדר) — בלי לשנות את השפה. כך כל <KatexInline math="\mathcal{L}_\omega(\mathcal{A}_i)" /> מתקבלת ע"י DBA רגיל.

<b>שלב 2 — DBA-ים סגורים לאיחוד סופי:</b> לשני DBA-ים <KatexInline math="B_1,B_2" /> (עם <KatexInline math="F_1,F_2" />), במכפלה הרגילה (מעברים דטרמיניסטיים, מצב התחלה יחיד) עם <KatexInline math="F=(F_1\times Q_2)\cup(Q_1\times F_2)" />: מכיוון ש-<KatexInline math="F" /> <b>סופית</b>, "מבקרים ב-<KatexInline math="F" /> אינסוף פעמים" שקול (שובך יונים) ל"מבקרים ב-<KatexInline math="F_1\times Q_2" /> אינסוף פעמים <b>או</b> ב-<KatexInline math="Q_1\times F_2" /> אינסוף פעמים" — כלומר בדיוק <KatexInline math="\mathcal{L}(B_1)\cup\mathcal{L}(B_2)" />. באינדוקציה, איחוד סופי של DBA-ים הוא שוב DBA.

<b>מסקנה:</b> אילו <KatexInline math="\mathcal{A}" /> (עם ריבוי מצבי התחלה ומעברים חלקיים) הכיר את <KatexInline math="\Diamond\square p" />, היה קיים גם DBA <b>רגיל</b> (מצב יחיד, מעברים מלאים) לה — בסתירה לעובדה הקלאסית (ראו שאלה 3) שאין ל-<KatexInline math="\Diamond\square p" /> אוטומט בוקי דטרמיניסטי.

<div class="mt-2 text-[12px] text-gray-600">
תזכורת קצרה מדוע אין ל-<KatexInline math="\Diamond\square p" /> DBA רגיל: בהינתן DBA <KatexInline math="B" /> כזה, בונים באינדוקציה מילה <KatexInline math="\beta" /> עם אינסוף הופעות של <KatexInline math="\neg p" /> (ולכן <KatexInline math="\beta\notin\Diamond\square p" />): מתחילים ב-<KatexInline math="w_0=\varepsilon" />; מכיוון ש-<KatexInline math="w_n\, p^\omega\in\Diamond\square p" /> (יש בו רק סופית הרבה <KatexInline math="\neg p" />), הוא מתקבל, ולכן בהמשכו (הריצה על <KatexInline math="p^\omega" /> אחרי <KatexInline math="w_n" />) מבקרים ב-<KatexInline math="F" /> ולו פעם אחת; מגדירים <KatexInline math="w_{n+1}=w_n\cdot p^{m_n}\cdot\neg p" /> כאשר <KatexInline math="m_n" /> הוא המספר המזערי כזה. הגבול <KatexInline math="\beta=\lim_n w_n" /> מבקר ב-<KatexInline math="F" /> אינסוף פעמים (מבנה הבנייה) — ולכן מתקבל — למרות שהוא מכיל אינסוף <KatexInline math="\neg p" /> וממילא <KatexInline math="\beta\notin\Diamond\square p" />. סתירה.
</div>

</div>

---

# שאלה 6 <span class="text-[16px] text-gray-500 font-normal">— מועד ג', 2024, שאלה 1</span>

<div class="flex justify-center items-start mt-1">
<img src="./public/practice-lesson-21/q06.png" class="max-w-[85%] max-h-[480px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 7 <span class="text-[16px] text-gray-500 font-normal">— מועד ד', 2024, שאלה 3</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q07.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# פתרון שאלה 7 <span class="text-[16px] text-gray-500 font-normal">— סעיף ג: האם הוגנות עולה מונוטונית עם הקבוצות?</span>

<div class="mt-3 text-center text-[20px]">
<span class="inline-block bg-red-100 border border-red-300 text-red-800 rounded px-4 py-1 font-bold">שגוי</span>
</div>

<div class="mt-6 grid grid-cols-2 gap-4 text-right text-[14px] leading-snug">
<div class="bg-emerald-50 border border-emerald-200 rounded p-3">
<div class="font-bold text-emerald-800 mb-1">ללא-תנאי: כן מונוטוני</div>
אם <KatexInline math="S_1\subseteq S_1'" /> ו-<KatexInline math="\alpha_i\in S_1" /> עבור אינסוף <KatexInline math="i" />, אז בוודאי <KatexInline math="\alpha_i\in S_1'" /> עבור אותם <KatexInline math="i" /> — הכלה ישירה, אין כאן בעיה.
</div>
<div class="bg-red-50 border border-red-200 rounded p-3">
<div class="font-bold text-red-800 mb-1">חזק וחלש: לא מונוטוניים</div>
הגדלת <KatexInline math="S" /> רק <b>מקילה על ההיפותזה</b> (ה-<KatexInline math="Post" />), בלי להקל על המסקנה (מה שנלקח בפועל) — ועלולה להפוך ריצה הוגנת ללא-הוגנת.
</div>
</div>

---

# פתרון שאלה 7 <span class="text-[16px] text-gray-500 font-normal">— סעיף ג: דוגמה נגדית</span>

<div class="text-right text-[14px] leading-relaxed mt-2">

<KatexInline math="TS" />: מצב יחיד <KatexInline math="s_0" />, פעולות <KatexInline math="b,c" /> תמיד מאופשרות (לולאה עצמית), <KatexInline math="a" /> אינה מאופשרת אף פעם. ריצה: <KatexInline math="\rho=c^\omega" /> (לוקחת רק <KatexInline math="c" />).

</div>

<div class="mt-3 text-center text-[15px]">
<KatexInline math="S_1=S_1'=\{c\},\qquad S_2=S_2'=\emptyset,\qquad S_3=\{a\}\ \subseteq\ S_3'=\{a,b\}" />
</div>

<div class="mt-4 overflow-x-auto">
<table class="mx-auto text-[13px] text-center border-collapse" dir="rtl">
<tr class="border-b-2 border-slate-300">
<th class="p-2"></th>
<th class="p-2">ללא-תנאי <KatexInline math="\{c\}" /></th>
<th class="p-2">חלש <KatexInline math="\emptyset" /></th>
<th class="p-2">חזק <KatexInline math="S_3" /></th>
<th class="p-2 font-bold">הוגנת?</th>
</tr>
<tr class="border-b border-slate-200">
<td class="p-2 font-bold"><KatexInline math="\mathcal{F}=\langle\{\{c\}\},\{\emptyset\},\{\{a\}\}\rangle" /></td>
<td class="p-2 text-emerald-700">✓ (<KatexInline math="c" /> נלקחת תמיד)</td>
<td class="p-2 text-emerald-700">✓ (בריק, <KatexInline math="Post(s,\emptyset)=\emptyset" />)</td>
<td class="p-2 text-emerald-700">✓ (בריק, <KatexInline math="a" /> אף פעם לא מאופשרת)</td>
<td class="p-2 font-bold text-emerald-700">כן</td>
</tr>
<tr>
<td class="p-2 font-bold"><KatexInline math="\mathcal{F}'=\langle\{\{c\}\},\{\emptyset\},\{\{a,b\}\}\rangle" /></td>
<td class="p-2 text-emerald-700">✓ (זהה)</td>
<td class="p-2 text-emerald-700">✓ (זהה)</td>
<td class="p-2 text-red-700">✗ (<KatexInline math="b" /> מאופשרת תמיד ⟸ היפותזה אמת, אך <KatexInline math="\rho" /> לא לוקחת <KatexInline math="a,b" />)</td>
<td class="p-2 font-bold text-red-700">לא</td>
</tr>
</table>
</div>

<div class="mt-4 bg-slate-50 border border-slate-200 rounded p-3 text-right text-[13.5px] leading-snug">
קיבלנו <KatexInline math="S_1\subseteq S_1',\,S_2\subseteq S_2',\,S_3\subseteq S_3'" /> אך <KatexInline math="\rho" /> הוגנת <KatexInline math="\mathcal{F}" /> ולא הוגנת <KatexInline math="\mathcal{F}'" /> — <b>סתירה לטענה.</b> האינטואיציה: הגדלת קבוצת הפעולות בהוגנות חזקה/חלשה מוסיפה עוד "הזדמנויות" שצריך לנצל (מחמירה את הדרישה), בעוד שבהוגנות בלתי-מותנית היא רק מוסיפה עוד דרכים לקיים את הדרישה (מקלה).
</div>

---

# שאלה 8 <span class="text-[16px] text-gray-500 font-normal">— מועד ב', 2024, שאלה 2</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q08.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 9 <span class="text-[16px] text-gray-500 font-normal">— מועד ג', 2025, שאלה 3</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q09.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 10 <span class="text-[16px] text-gray-500 font-normal">— מבחן מילואים, 2025, שאלה 1</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q10.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 11 <span class="text-[16px] text-gray-500 font-normal">— מבחן ג', 2022, שאלה 1</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q11.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 12 <span class="text-[16px] text-gray-500 font-normal">— מבחן ג', 2022, שאלה 3</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q12.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 13 <span class="text-[16px] text-gray-500 font-normal">— מבחן מועד ב', 2022, שאלה 4</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q13.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>
