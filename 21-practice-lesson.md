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

כל פעם ש־<KatexInline math="p" /> מתקיים במצב <KatexInline math="i" />, נפתחת "חובה": במצב <KatexInline math="i+1" /> צריך <KatexInline math="q" />, **או** ש־<KatexInline math="p" /> יחזור בעתיד (<KatexInline math="\lozenge p" />). כל מצב מייצג את מידת החוב הפתוח:
**0 (מקבל)** — אין חוב; <KatexInline math="p" /> פותח חוב ← 1.
**1 (מקבל)** — חוב חדש, <KatexInline math="q" /> עדיין רלוונטי: <KatexInline math="\neg p \wedge q" /> סוגר ← 0; <KatexInline math="\neg p \wedge \neg q" /> מעביר להמתנה ← 2; <KatexInline math="p" /> סוגר וגם פותח חוב חדש (נשארים ב-1).
**2 (לא מקבל)** — ממתינים רק ל־<KatexInline math="\lozenge p" /> (<KatexInline math="q" /> לא רלוונטי יותר); <KatexInline math="p" /> סוגר וחוזר ← 1.
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
**0 (התחלתי)** — עדיין לא ידוע אם <KatexInline math="p" /> יחזיק במצב זה; <KatexInline math="\neg p" /> ← 1 (בודקים אם זה כבר "המצב הבא" שצריך בו <KatexInline math="q" />), <KatexInline math="p" /> ← 2 (עדיין בתוך שרשרת ה-<KatexInline math="p" />).
**1** — כאן בודקים <KatexInline math="q" />: אם מתקיים ← 3 (התקבלנו); אחרת אין מעבר מוגדר — נדחה (הפרה של <KatexInline math="\varphi" />).
**2** — בתוך שרשרת ה-<KatexInline math="p" />: <KatexInline math="p \wedge \neg q" /> נשארים (השרשרת ממשיכה), <KatexInline math="\neg p \wedge \neg q" /> ← 1 (השרשרת נגמרה, בודקים אם זה כן "המצב הבא"), <KatexInline math="q" /> ← 3 (התקבלנו מוקדם).
**3** — בור מקבל, נשארים בו לנצח.

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

**תווית היציאה מ-<KatexInline math="B" />** נקבעת ישירות: <KatexInline math="a \in B \iff a \in L(B)" /> כאשר <KatexInline math="L(B)" /> היא התווית של <KatexInline math="B" /> (וכאן <KatexInline math="a\in\{p,q\}" />) — כלומר <KatexInline math="B" /> "קורא" בדיוק את <KatexInline math="p,q" /> שהוא מכיל.

**מעבר**: <KatexInline math="B \xrightarrow{\;B\cap AP\;} B'" /> מותר אם"ם <KatexInline math="\bigcirc q \in B \iff q \in B'" /> (זו ההגבלה היחידה — <KatexInline math="\bigcirc q" /> הוא איבר ה-<KatexInline math="\bigcirc" /> היחיד ב-<KatexInline math="\operatorname{cl}(\varphi)" />). כלומר מ-<KatexInline math="B" /> אפשר לעבור לכל אחת מ-9 הקבוצות (מתוך ה-18) שבהן <KatexInline math="q" /> תואם את <KatexInline math="\bigcirc q" /> של <KatexInline math="B" /> — אוטומט לא-דטרמיניסטי לגמרי. לפי מספור השורות מהטבלה הקודמת (וללא תלות בביט <KatexInline math="q" /> החופשי של המקור, שרק קובע את חלק התווית הנקרא):

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

**תנאי קבלה מוכלל** — קבוצת קבלה אחת לכל תת-נוסחת <KatexInline math="\mathsf{U}" /> ב-<KatexInline math="\operatorname{cl}(\varphi)" />:

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

**לא.** נציב <KatexInline math="q \equiv \mathit{false}" /> תמיד (הצבה זו היא תכונת בטיחות, ולכן אם היה קיים DBA ל-<KatexInline math="\varphi" /> היה קיים גם לחיתוך שלו איתה):

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="\bigcirc q \equiv \mathit{false} \;\Rightarrow\; \alpha = p\,\mathsf{U}\,\bigcirc q \equiv \mathit{false}" /></div>
<div><KatexInline math="\psi = \alpha \vee \neg\beta \equiv \neg\beta \equiv \square p" /></div>
<div><KatexInline math="\varphi \equiv p\,\mathsf{U}\,\square p \;=\; \lozenge\square p" /></div>
</div>

כלומר על התת-שפה <KatexInline math="q\equiv \mathit{false}" />, השפה של <KatexInline math="\varphi" /> שקולה בדיוק ל־<KatexInline math="\lozenge\square p" /> ("מתישהו <KatexInline math="p" /> מחזיק לצמיתות") — הדוגמה הקלאסית מההרצאה לתכונה **בלי** אוטומט Büchi דטרמיניסטי (כל DBA שמנחש "עכשיו מתחיל הלעד" יכול תמיד להיות מופרך על ידי הפרה מאוחרת ככל שנרצה של <KatexInline math="p" />).

מאחר שאוטומטים דטרמיניסטיים סגורים לחיתוך עם תכונות בטיחות, אילו קיים DBA ל-<KatexInline math="\varphi" /> היה קיים גם ל-<KatexInline math="\lozenge\square p" /> — סתירה. **לכן לא קיים אוטומט Büchi דטרמיניסטי המקבל את <KatexInline math="\varphi" />.**

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

**נכון.** יהי <KatexInline math="A=(Q,\Sigma,\delta,q_0,\{F_1,\dots,F_k\})" /> GNBA דטרמיניסטי (כלומר <KatexInline math="\delta" /> היא פונקציה). בונים אוטומט בוקי רגיל <KatexInline math="A'=(Q\times\{1,\dots,k\},\Sigma,\delta',(q_0,1),F)" /> — בדיוק הבנייה הרגילה מהקורס להמרת GNBA ל-NBA:

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="\delta'((q,j),a) = (\delta(q,a),\, \mathrm{next}(q,j))" /></div>
<div><KatexInline math="\mathrm{next}(q,j) = \begin{cases} (j \bmod k) + 1 & q \in F_j \\ j & q \notin F_j \end{cases}" /></div>
<div><KatexInline math="F = F_1 \times \{1\}" /></div>
</div>

הרכיב השני "זוכר" איזו קבוצת קבלה מחכים לה כרגע; כשמגיעים אליה עוברים לחכות לקבוצה הבאה. ריצה מבקרת ב-<KatexInline math="F_1\times\{1\}" /> אינסוף פעמים אם"ם היא "מסתובבת" סביב כל ה-<KatexInline math="F_1,\dots,F_k" /> אינסוף פעמים, כלומר מבקרת בכל אחת מהן אינסוף פעמים — בדיוק תנאי הקבלה המוכלל המקורי.

**דטרמיניזם נשמר:** <KatexInline math="\mathrm{next}(q,j)" /> נקבע לגמרי לפי <KatexInline math="(q,j)" /> (ללא ניחוש), ו-<KatexInline math="\delta" /> דטרמיניסטית בהנחה — ולכן גם <KatexInline math="\delta'" /> היא פונקציה. קיבלנו אוטומט בוקי רגיל **דטרמיניסטי** לאותה שפה.

</div>

---

# פתרון שאלה 3 <span class="text-[16px] text-gray-500 font-normal">— סעיף 2: סגירות דטרמיניסטית לחיתוך</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

**נכון.** יהיו <KatexInline math="\mathcal{A}_1=(Q_1,\Sigma,\delta_1,q_1^0,F_1)" />, <KatexInline math="\mathcal{A}_2=(Q_2,\Sigma,\delta_2,q_2^0,F_2)" /> אוטומטי בוקי דטרמיניסטיים (מלאים) עם <KatexInline math="P_i=\mathcal{L}_\omega(\mathcal{A}_i)" />. בונים מכפלה:

<div class="flex flex-col items-end gap-1 mt-2">
<div><KatexInline math="\delta_\times((s_1,s_2),a) = (\delta_1(s_1,a),\, \delta_2(s_2,a))" /> &nbsp; — פונקציה, כי <KatexInline math="\delta_1,\delta_2" /> פונקציות</div>
<div><KatexInline math="G_1 = F_1\times Q_2, \qquad G_2 = Q_1\times F_2" /></div>
</div>

ריצה יחידה <KatexInline math="\rho" /> של המכפלה על <KatexInline math="\sigma" /> מוקרנת לריצות היחידות <KatexInline math="\rho_1,\rho_2" /> של <KatexInline math="\mathcal{A}_1,\mathcal{A}_2" />. מכיוון שהאוטומטים דטרמיניסטיים ומלאים: <KatexInline math="\rho" /> מבקרת ב-<KatexInline math="G_1" /> אינסוף פעמים <KatexInline math="\iff" /> <KatexInline math="\rho_1" /> מבקרת ב-<KatexInline math="F_1" /> אינסוף פעמים <KatexInline math="\iff" /> <KatexInline math="\sigma\in P_1" />, ובאותו אופן עבור <KatexInline math="G_2,P_2" />. לכן:

<div class="mt-2"><KatexInline math="\sigma \text{ מתקבל לפי } \{G_1,G_2\} \iff \sigma \in P_1\cap P_2" /></div>

כלומר <KatexInline math="(Q_1\times Q_2,\Sigma,\delta_\times,(q_1^0,q_2^0),\{G_1,G_2\})" /> הוא **GNBA דטרמיניסטי** ל-<KatexInline math="P_1\cap P_2" />. לפי סעיף 1, קיים ממנו גם אוטומט בוקי **רגיל דטרמיניסטי** <KatexInline math="\mathcal{A}" /> עם <KatexInline math="P_1\cap P_2=\mathcal{L}_\omega(\mathcal{A})" />. (כלומר: אוטומטי בוקי דטרמיניסטיים סגורים לחיתוך — אך, כידוע, לא לשלילה.)

</div>

---

# פתרון שאלה 3 <span class="text-[16px] text-gray-500 font-normal">— סעיף 3: קיים בוקי, אך לא LTL</span>

<div class="text-right text-[14px] leading-snug mt-3">

**נכון.** נסמן <KatexInline math="AP=\{0,\dots,9\}" />, כך ש-<KatexInline math="\sigma[0]\subseteq AP" />, ונגדיר <KatexInline math="p := |\sigma[0]|\in\{0,\dots,10\}" /> — **גודל** (עוצמת) הקבוצה במיקום 0, לא תוכנה. התכונה, בניסוח מדויק, היא <KatexInline math="\{\sigma:\forall i.\ \sigma[\,|\sigma[0]|\cdot i\,]=\sigma[1]\}" />: כל מיקום שהוא כפולה של <KatexInline math="p" /> (<KatexInline math="0,p,2p,\dots" />) נושא את אותה אות כמו <KatexInline math="\sigma[1]" />.

**קיים אוטומט בוקי (אף דטרמיניסטי!):** בונים אוטומט עם שלב "קריאת <KatexInline math="\sigma[0]" />" (קביעת <KatexInline math="p=|\sigma[0]|" />), שלב "קריאת <KatexInline math="\sigma[1]" />" (שמירת האות <KatexInline math="b" />), ואז מונה <KatexInline math="c\in\{0,\dots,p-1\}" /> (מיקום מודולו <KatexInline math="p" />, סופי כי <KatexInline math="p\le 10" />): בכל <KatexInline math="c=0" /> בודקים שהאות הנוכחית <KatexInline math="=b" />; אם לא — עוברים למצב "מלכודת" לא-מקבל עם לולאה עצמית לנצח. <KatexInline math="F=" /> כל המצבים חוץ מהמלכודת. זו תכונת בטיחות: המילה מתקבלת אם"ם אף פעם לא נכנסים למלכודת אם"ם התכונה מתקיימת — ולכן זהו למעשה DBA (מספר המצבים סופי כי <KatexInline math="p\le 10" />).

**אין נוסחת LTL:** קבעו <KatexInline math="p\ge 2" />. הקבוצה <KatexInline math="\{\sigma:|\sigma[0]|=p\}" /> ניתנת לביטוי ב-LTL (תנאי על שתי האותיות הראשונות בלבד). אילו התכונה כולה הייתה LTL-בת-ביטוי, אז (מסגירות LTL תחת חיתוך/<KatexInline math="\wedge" />) גם החיתוך שלה עם קבוצה זו היה LTL-בת-ביטוי — וזו בדיוק תכונת "ספירה מודולו <KatexInline math="p" />" (כל מיקום ה-<KatexInline math="p" />-י שווה לעוגן קבוע), המקבילה לדוגמה הקלאסית (כגון "<KatexInline math="q" /> מתקיים בכל מיקום זוגי") שאינה שפה star-free/aperiodic, ולכן (ממשפט קמפ, <KatexInline math="\mathrm{LTL}=\text{star-free}" />) אינה LTL-בת-ביטוי — סתירה. לכן אין נוסחת LTL לתכונה.

</div>

---

# שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— מועד א', 2024, שאלה 1</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q04.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף א: מודל צ'קינג ישיר מול אוטומט דטרמיניסטי</span>

<div class="text-right text-[14px] leading-relaxed mt-2">

**נכון** (עבור <KatexInline math="|Q_0|=1" />, ו-<KatexInline math="TS" /> ללא מצבים סופניים, כרגיל). נסמן <KatexInline math="Q_0=\{q_0\}" />. מכיוון ש-<KatexInline math="\delta" /> **פונקציה מלאה**, לכל מילה <KatexInline math="\sigma=A_0A_1\cdots" /> יש **ריצה יחידה** <KatexInline math="q_0,q_1,\dots" /> (<KatexInline math="q_{i+1}=\delta(q_i,A_i)" />), ו-<KatexInline math="\sigma\in\mathcal{L}_\omega(\mathcal{A}) \iff" /> הריצה מבקרת ב-<KatexInline math="F" /> אינסוף פעמים <KatexInline math="\iff" /> (כי <KatexInline math="F" /> סופית, שובך יונים) קיים <KatexInline math="q\in F" /> שמבוקר אינסוף פעמים.

באותה סיבה (דטרמיניזם + שלמות + מצב התחלה יחיד), לכל נתיב <KatexInline math="\pi" /> ב-<KatexInline math="TS" /> מ-<KatexInline math="Init(TS)" /> יש **נתיב מכפלה יחיד** תואם ב-<KatexInline math="TS\times\mathcal{A}" /> מ-<KatexInline math="Init(TS)\times\{q_0\}" />, וההתאמה היא חד-חד-ערכית ועל בין נתיבי <KatexInline math="TS" /> לנתיבי <KatexInline math="TS\times\mathcal{A}" />. לכן:

<div class="mt-2 text-center">
<KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> &nbsp;<KatexInline math="\iff" />&nbsp; כל עקבה של <KatexInline math="TS" /> מתקבלת ע"י <KatexInline math="\mathcal{A}" /> &nbsp;<KatexInline math="\iff" />&nbsp; כל נתיב-מכפלה מבקר ב-<KatexInline math="F" /> אינסוף פעמים &nbsp;<KatexInline math="\iff" />&nbsp; <KatexInline math="TS\times\mathcal{A}\models\bigvee_{q\in F}\square\Diamond q" />
</div>

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף א (המשך): מה קורה אם <KatexInline math="|Q_0|=2" />?</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

**כן, משנה את התשובה — הטענה נהיית שגויה.** ההוכחה למעלה נשענת קריטית על ריצה **יחידה** לכל מילה; עם שני מצבי התחלה זה קורס, כי <KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> דורש **קיום** ריצה מקבלת (מאחד משני המצבים ההתחלתיים), בעוד ש-<KatexInline math="TS\times\mathcal{A}" /> (עם <KatexInline math="Init=Init(TS)\times Q_0" />) דורש שהתנאי יתקיים **לכל** נתיב, כולל אלו שמתחילים במצב ה"לא נכון".

**דוגמה נגדית:** <KatexInline math="AP=\emptyset" /> (אות יחידה <KatexInline math="\emptyset" />), <KatexInline math="Q=\{q_0,q_1\}" />, <KatexInline math="Q_0=\{q_0,q_1\}" />, <KatexInline math="F=\{q_1\}" />, <KatexInline math="\delta(q_0,\emptyset)=q_0" />, <KatexInline math="\delta(q_1,\emptyset)=q_1" /> (שני מצבים בלולאה עצמית). המילה היחידה <KatexInline math="\emptyset^\omega" /> מתקבלת (דרך הריצה המתחילה ב-<KatexInline math="q_1" />), ולכן <KatexInline math="\mathcal{L}_\omega(\mathcal{A})=\{\emptyset^\omega\}" /> = כל השפה. עבור <KatexInline math="TS" /> עם מצב יחיד <KatexInline math="s_0" /> (עם לולאה עצמית): <KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> **מתקיים** (טריוויאלית). אבל ב-<KatexInline math="TS\times\mathcal{A}" /> יש נתיב שמתחיל ב-<KatexInline math="(s_0,q_0)" /> ולעולם לא מבקר ב-<KatexInline math="q_1\in F" /> — ולכן <KatexInline math="TS\times\mathcal{A}\not\models\square\Diamond q_1" />. **סתירה לשקילות.**

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

<KatexInline math="q_1" /> (מקבל, מסומן בכפול) הוא היחיד ב-<KatexInline math="F" />. ב-<KatexInline math="\mathcal{A}" /> עצמו יש **קיום** ריצה מקבלת עבור <KatexInline math="\emptyset^\omega" /> (זו שמתחילה ב-<KatexInline math="q_1" />) — ולכן <KatexInline math="\mathcal{L}_\omega(\mathcal{A})" /> היא כל השפה ו-<KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" /> מתקיים. אבל ב-<KatexInline math="TS\times\mathcal{A}" /> **שני** מצבי ההתחלה ממשיכים כל אחד בנתיב נפרד: הנתיב מ-<KatexInline math="(s_0,q_0)" /> (משמאל, לא מקבל) **לעולם לא** מבקר במצב מקבל — לכן <KatexInline math="TS\times\mathcal{A}\not\models\bigvee_{q\in F}\square\Diamond q" />, למרות ש-<KatexInline math="TS\models\mathcal{L}_\omega(\mathcal{A})" />. אי-ההתאמה בין "קיום ריצה מקבלת" (בהגדרת <KatexInline math="\mathcal{L}_\omega" />) ל"כל הנתיבים במכפלה" (בהגדרת ההתמדה של המכפלה) היא בדיוק מה שדורש מצב התחלה יחיד.

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף ב: האם כל שמורה היא התמדה?</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

**שגוי.** נכון ש-<KatexInline math="P_{\mathrm{inv}}(\Phi)\subseteq P_{\mathrm{per}}(\Phi)" /> באופן טריוויאלי (אם <KatexInline math="\Phi" /> מתקיים תמיד, בפרט הוא מתקיים החל ממקום 0) — אבל השאלה היא האם **שפת** השמורה עצמה **שווה** לאיזושהי שפת התמדה (עם נוסחת מצב <KatexInline math="\Psi" /> כלשהי, לאו דווקא <KatexInline math="\Phi" />), וזה כבר לא נכון עבור שמורה לא-טריוויאלית.

**דוגמה נגדית:** יהי <KatexInline math="p\in AP" />, <KatexInline math="\Phi=p" /> (לא טאוטולוגיה ולא סתירה). <KatexInline math="P_{\mathrm{inv}}(p)=X^\omega" /> כאשר <KatexInline math="X=\{A\subseteq AP: p\in A\}\neq\emptyset,\Sigma" />. נניח בשלילה שקיימת <KatexInline math="\Psi" /> עם <KatexInline math="P_{\mathrm{per}}(\Psi)=X^\omega" />, ונסמן <KatexInline math="Y=\{A:A\models\Psi\}" />, כך ש-<KatexInline math="\Sigma^*Y^\omega = X^\omega" />. אם <KatexInline math="Y\neq\emptyset" />, בחרו <KatexInline math="A_0\notin X" /> (קיים כי <KatexInline math="X\neq\Sigma" />) ו-<KatexInline math="B\in Y" />: המילה <KatexInline math="A_0B^\omega \in \Sigma^*Y^\omega=X^\omega" />, אך אות ראשונה <KatexInline math="A_0\notin X" /> סותרת <KatexInline math="A_0B^\omega\in X^\omega" /> (השמורה דורשת <KatexInline math="X" /> **בכל** מיקום, כולל הראשון). אם <KatexInline math="Y=\emptyset" /> אז <KatexInline math="P_{\mathrm{per}}(\Psi)=\emptyset\neq X^\omega" /> (כי <KatexInline math="X\neq\emptyset" />). בשני המקרים סתירה. **לכן אין <KatexInline math="\Psi" /> כזו — השמורה <KatexInline math="P_{\mathrm{inv}}(p)" /> אינה תכונת התמדה.**

<div class="mt-1 text-[12.5px] text-gray-600">(זהו בדיוק המשפט מההרצאה: שוויון בין שמורה להתמדה מתקיים רק במקרים הטריוויאליים <KatexInline math="\Phi\equiv\mathit{true}" /> או <KatexInline math="\Phi\equiv\mathit{false}" />.)</div>

</div>

---

# פתרון שאלה 4 <span class="text-[16px] text-gray-500 font-normal">— סעיף ג: עקביות בבניית ה-GNBA</span>

<div class="text-right text-[15px] leading-relaxed mt-3">

**לא ייתכן — הצירוף בהכרח לא עקבי**, בלי שום תלות בתנאים על <KatexInline math="\varphi\in B" /> או <KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\notin B" />: הסתירה נובעת רק מ-<KatexInline math="\bigcirc\varphi\notin B" />, <KatexInline math="B'\in\delta(B,B\cap AP)" /> ו-<KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\notin B'" />.

**הוכחה:** לפי כלל המעבר על תת-נוסחאות <KatexInline math="\bigcirc" /> (המשמש בבניה, ראו שאלה 2): <KatexInline math="B\xrightarrow{B\cap AP}B'" /> חוקי רק אם <KatexInline math="\bigcirc\varphi\in B \iff \varphi\in B'" />. בהינתן <KatexInline math="\bigcirc\varphi\notin B" />, נובע <KatexInline math="\varphi\notin B'" />. מעקביות (שלמות) <KatexInline math="B'" /> — לכל תת-נוסחה בדיוק אחת מבין <KatexInline math="\varphi,\neg\varphi" /> שייכת ל-<KatexInline math="B'" /> — מקבלים <KatexInline math="\neg\varphi\in B'" />.

כעת מפעילים את כלל העקביות ל-Until <KatexInline math="\chi=\varphi\,\mathsf{U}\,\neg\varphi" /> (עם <KatexInline math="\chi_1=\varphi,\ \chi_2=\neg\varphi" />) על <KatexInline math="B'" />: <KatexInline math="\chi_2\in B' \Rightarrow \chi\in B'" />, כלומר <KatexInline math="\neg\varphi\in B' \Rightarrow \varphi\,\mathsf{U}\,\neg\varphi\in B'" />. קיבלנו <KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\in B'" /> — **בסתירה** לדרישה <KatexInline math="\varphi\,\mathsf{U}\,\neg\varphi\notin B'" />.

לכן צירוף המצבים המבוקש אינו יכול להתקיים באף הרצה של הבניה. <KatexInline math="\blacksquare" />

</div>

---

# שאלה 5 <span class="text-[16px] text-gray-500 font-normal">— מועד א' מילואים, 2024, שאלה 2</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q05.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 6 <span class="text-[16px] text-gray-500 font-normal">— מועד ג', 2024, שאלה 1</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q06.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
</div>

---

# שאלה 7 <span class="text-[16px] text-gray-500 font-normal">— מועד ד', 2024, שאלה 3</span>

<div class="flex justify-center items-start mt-3">
<img src="./public/practice-lesson-21/q07.png" class="max-w-[92%] max-h-[560px] object-contain rounded-lg border border-slate-200 shadow-md bg-white p-2" />
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
