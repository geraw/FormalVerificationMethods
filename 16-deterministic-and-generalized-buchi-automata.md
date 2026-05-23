---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: false
download: true
exportFilename: 16-deterministic-and-generalized-buchi-automata
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## אוטומטי Büchi דטרמיניסטיים ומוכללים
  הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות
---

# אוטומטי Büchi דטרמיניסטיים ומוכללים

הרצאה בקורס מבוא לאימות תוכנה בשיטות פורמליות

הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מטרות ההרצאה

<div class="grid grid-cols-3 gap-4 mt-8 text-right text-[18px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">ריקות של אוטומט Büchi</div>
נזהה מתי קיימת מילה אינסופית שהאוטומט מקבל, ונראה שהבעיה מצטמצמת לחיפוש מצב מקבל נגיש שניתן לחזור אליו.
</div>

<div class="bg-orange-50 border border-orange-200 rounded p-4">
<div class="font-bold text-orange-700 mb-2">דטרמיניזם אינו מספיק</div>
נראה ש־<span dir="ltr">DBA</span> חלשים מ־<span dir="ltr">NBA</span>, ולמה בניית החזקה הרגילה לא משמרת קבלת Büchi.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">אוטומטי Büchi מוכללים</div>
נכיר <span dir="ltr">GNBA</span>, נתרגם אותם ל־<span dir="ltr">NBA</span>, ונשתמש בהם לבניית חיתוך שפות.
</div>
</div>

---

# תזכורת: אוטומט Büchi

<div class="grid grid-cols-[0.9fr_1.1fr] gap-5 mt-5 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="500" :height="230" :arrowSize="4.2" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'q1', x: 85, y: 115, label: '$q_1$', initial: true, initialDirection: 'left', r: 25, labelWidth: 70 },
    { id: 'q2', x: 245, y: 115, label: '$q_2$', r: 25, labelWidth: 70 },
    { id: 'q3', x: 405, y: 115, label: '$q_3$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'q1', target: 'q1', label: '$\\neg req$', loopDirection: '-90deg', labelY: -12, labelWidth: 80 },
    { source: 'q1', target: 'q2', label: '$req$', labelY: -10, labelWidth: 50 },
    { source: 'q2', target: 'q2', label: '$\\neg grant$', loopDirection: '-90deg', labelY: -12, labelWidth: 90 },
    { source: 'q2', target: 'q3', label: '$grant$', labelY: -10, labelWidth: 65 },
    { source: 'q3', target: 'q1', label: '$\\neg req$', labelY: 18, labelWidth: 80, curve: -0.22 },
    { source: 'q3', target: 'q2', label: '$req$', labelY: -12, labelWidth: 50, curve: 0.3 }
  ]"
/>
</div>

<div class="text-right text-[20px] leading-relaxed">
אוטומט Büchi מעל <KatexInline math="\Sigma=2^{AP}" />, כאשר <KatexInline math="AP=\{req,grant\}" />, הוא חמישייה:

<div class="my-3 text-center text-[27px]" dir="ltr">
<KatexInline display math="\mathcal{A}=\langle Q,\Sigma,\delta,Q_0,F\rangle" />
</div>

מילה אינסופית מתקבלת אם קיימת ריצה שבה מבקרים במצבים מתוך <KatexInline math="F" /> אינסוף פעמים.
</div>
</div>

<div class="-mt-3 rounded border border-emerald-200 bg-emerald-50 px-4 py-2 text-right text-[18px] leading-snug">
בדוגמה, כל אות היא קבוצה של פסוקים אטומיים. <KatexInline math="q_2" /> מסמן שיש בקשה פתוחה, ו־<KatexInline math="q_3" /> מסמן שהבקשה קיבלה אישור. לכן השפה היא כל המילים שבהן מופיעים אינסוף מחזורים של בקשה <KatexInline math="req" /> שלאחריה, אחרי מספר צעדים סופי, מופיע <KatexInline math="grant" />.

<div class="mt-1 text-center text-[19px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})=(\neg req)^*\left(req(\neg grant)^*grant(\neg req)^*\right)^\omega" />
</div>
</div>

---

# ריקות של שפת Büchi

<div class="mt-5 text-right text-[22px] leading-relaxed">
השפה של אוטומט Büchi אינה ריקה אם ורק אם קיימים:
</div>

<div class="mt-4 text-center text-[27px]" dir="ltr">
<KatexInline display math="q_0\in Q_0,\quad q\in F,\quad w\in\Sigma^*,\quad v\in\Sigma^+" />
<KatexInline display math="q\in\delta^*(q_0,w)\quad\land\quad q\in\delta^*(q,v)" />
</div>

<div class="grid grid-cols-[0.8fr_1.2fr] gap-5 mt-3 items-center">
<div class="flex items-center justify-center">
  <img src="/images/buchi_emptiness.png" class="h-[260px] object-contain" />
</div>

<div class="text-right text-[20px] leading-snug">
המשמעות: מגיעים ממצב התחלתי למצב מקבל, ואז יש מחזור לא ריק שמחזיר לאותו מצב מקבל.
לכן אפשר לקרוא את <span dir="ltr"><KatexInline math="wv^\omega" /></span> ולקבל ריצה מקבלת.
</div>
</div>

---

# בדיקת ריקות כבעיית גרפים

<div class="grid grid-cols-2 gap-5 mt-7 text-right text-[20px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">מה מחפשים?</div>
מצב <KatexInline math="q\in F" /> שהוא גם נגיש מ־<KatexInline math="Q_0" /> וגם נמצא על מחזור.
באופן שקול: רכיב קשירות חזקה נגיש שמכיל מצב מקבל ומחזור.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-2">איך בודקים?</div>
מריצים חיפוש נגישות, ואז בודקים אם מתוך מצב מקבל נגיש אפשר לחזור אליו.
אפשר לממש זאת באמצעות <span dir="ltr">SCC</span> או באמצעות חיפוש עומק מקונן.
</div>
</div>

<div class="mt-7 text-center text-[29px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A})\neq\emptyset \iff \exists\text{ accepting reachable cycle}" />
</div>

---

# למה ריקות חשובה?

<div class="mt-6 text-right text-[22px] leading-relaxed">
הרבה שאלות על אוטומטי Büchi מצטמצמות לשאלת ריקות:
</div>

<div class="grid grid-cols-2 gap-5 mt-6 text-right text-[20px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-2">הכלת שפות</div>
כדי לבדוק <KatexInline math="L_\omega(\mathcal{A}_1)\subseteq L_\omega(\mathcal{A}_2)" /> בודקים אם ההפרש ריק:
<div class="mt-3 text-center" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{A}_1)\cap\overline{L_\omega(\mathcal{A}_2)}=\emptyset" />
</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-2">שקילות שפות</div>
כדי לבדוק שקילות בודקים ריקות של שני ההפרשים.
זה מניח שיש לנו דרך לבנות חיתוך ומשלים.
</div>
</div>

---

# אוטומט דטרמיניסטי ושלם

<div class="grid grid-cols-2 gap-5 mt-8 text-right text-[21px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">דטרמיניסטי</div>
אוטומט Büchi הוא דטרמיניסטי אם יש מצב התחלתי יחיד ולכל מצב ואות יש לכל היותר מעבר אחד:
<div class="mt-3 text-center" dir="ltr">
<KatexInline display math="|Q_0|=1,\qquad |\delta(q,a)|\le 1" />
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-2">שלם</div>
אוטומט הוא שלם אם לכל מצב ואות יש לפחות מעבר אחד:
<div class="mt-3 text-center" dir="ltr">
<KatexInline display math="|\delta(q,a)|\ge 1" />
</div>
באוטומט דטרמיניסטי שלם יש ריצה יחידה לכל מילת קלט.
</div>
</div>

---

# דוגמה: <span dir="ltr">DBA</span> לתכונת זמן לינארי

<div class="grid grid-cols-[0.9fr_1.1fr] gap-5 mt-6 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="500" :height="230" :arrowSize="4.2" :stateLabelFontSize="16" :transitionLabelFontSize="13"
  :states="[
    { id: 'bad', x: 95, y: 115, label: '$q_{\bot}$', r: 25, labelWidth: 70 },
    { id: 'wait', x: 250, y: 115, label: '$q_0$', initial: true, initialDirection: 'top', r: 25, labelWidth: 70 },
    { id: 'seen', x: 405, y: 115, label: '$q_1$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'wait', target: 'seen', label: '$a\\land b$', labelY: -10, labelWidth: 70, curve: -0.18 },
    { source: 'seen', target: 'wait', label: '$\\neg a\\land b$', labelY: 18, labelWidth: 90, curve: -0.18 },
    { source: 'wait', target: 'wait', label: '$\\neg a\\land b$', loopDirection: '90deg', labelY: 8, labelWidth: 90 },
    { source: 'seen', target: 'seen', label: '$a\\land b$', loopDirection: '90deg', labelY: 8, labelWidth: 70 },
    { source: 'wait', target: 'bad', label: '$\\neg b$', labelY: 20, labelWidth: 55, curve: -0.2 },
    { source: 'seen', target: 'bad', label: '$\\neg b$', labelY: -18, labelWidth: 55, curve: 0.35 },
    { source: 'bad', target: 'bad', label: '$true$', loopDirection: '180deg', labelX: -12, labelWidth: 50 }
  ]"
/>
</div>

<div class="text-right text-[22px] leading-relaxed">
האוטומט מקבל בדיוק את התכונה:
<div class="mt-4 text-center text-[29px]" dir="ltr">
<KatexInline display math="\text{Always } b \;\land\; \text{Always Eventually } a" />
</div>
המצב המקבל מציין שראינו <KatexInline math="a" /> תוך שמירה על <KatexInline math="b" />.
</div>
</div>

---

# תזכורת: <span class="text-red-600">שקילות סופית</span> <KatexInline math="\not\Leftrightarrow" /> <span class="text-blue-600">שקילות <KatexInline math="\omega" /></span>

<div class="grid grid-cols-[1.1fr_1.8fr_1.1fr] gap-4 mt-4 items-center text-right">
<!-- Left Column: L_omega -->
<div class="flex flex-col gap-6">
<div class="bg-blue-50 border border-blue-200 rounded p-2.5 text-[13px] leading-snug">
<div class="font-bold text-blue-700 mb-1">שפת <KatexInline math="\omega" /> של <KatexInline math="\mathcal{A}_1" />:</div>
כל המילים האינסופיות שבהן כל האותיות מכילות את <KatexInline math="a" />:
<div class="mt-2 text-center text-blue-800" dir="ltr">
<KatexInline math="L_\omega(\mathcal{A}_1) = \{a\}^\omega" />
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-2.5 text-[13px] leading-snug">
<div class="font-bold text-blue-700 mb-1">שפת <KatexInline math="\omega" /> של <KatexInline math="\mathcal{A}_2" />:</div>
אין אף ריצה אינסופית שמבקרת במצב המקבל אינסוף פעמים:
<div class="mt-2 text-center text-blue-800" dir="ltr">
<KatexInline math="L_\omega(\mathcal{A}_2) = \emptyset" />
</div>
</div>
</div>

<!-- Center Column: Automata -->
<div class="flex flex-col gap-4 items-center relative">
<!-- Automaton 1 -->
<div class="bg-white rounded border border-slate-200 shadow-sm p-2 w-[340px]">
<div class="text-[10px] text-slate-400 absolute top-2 right-4 font-mono"><KatexInline math="\mathcal{A}_1" /></div>
<AutomatonD3 variant="classic" :width="320" :height="110" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="13"
:states="[
{ id: 's0', x: 80, y: 55, label: '$s_0$', initial: true, initialDirection: 'left', r: 20 },
{ id: 's1', x: 240, y: 55, label: '$s_1$', accepting: true, r: 20 }
]"
:transitions="[
{ source: 's0', target: 's1', label: '$a$', labelY: -10, labelWidth: 40 },
{ source: 's1', target: 's1', label: '$a$', loopDirection: '-90deg', labelY: -12, labelWidth: 40 }
]"
/>
</div>

<!-- Nondeterminism SVG Arrow Overlay -->
<svg v-click="2" class="absolute z-20 top-0 left-0 w-[340px] h-[270px] pointer-events-none overflow-visible">
<path d="M 230,120 L 105,185" stroke="#dc2626" stroke-width="5" marker-end="url(#arrow)" fill="none" />
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626" />
</marker>
</defs>
<g transform="translate(167, 152) rotate(-28)">
<rect x="-80" y="-12" width="160" height="24" rx="4" fill="#dc2626" />
<text x="0" y="4" fill="#ffffff" font-weight="bold" font-size="11" text-anchor="middle" font-family="sans-serif">בחירה לא דטרמיניסטית</text>
</g>
</svg>

<!-- Automaton 2 -->
<div class="bg-white rounded border border-slate-200 shadow-sm p-2 w-[340px]">
<div class="text-[10px] text-slate-400 absolute bottom-2 right-4 font-mono"><KatexInline math="\mathcal{A}_2" /></div>
<AutomatonD3 variant="classic" :width="320" :height="110" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="13"
:states="[
{ id: 's0', x: 80, y: 55, label: '$s_0$', initial: true, initialDirection: 'left', r: 20 },
{ id: 's1', x: 240, y: 55, label: '$s_1$', accepting: true, r: 20 }
]"
:transitions="[
{ source: 's0', target: 's0', label: '$a$', loopDirection: '-90deg', labelY: -12, labelWidth: 40 },
{ source: 's0', target: 's1', label: '$a$', labelY: -10, labelWidth: 40 }
]"
/>
</div>
</div>

<!-- Right Column: L_finite -->
<div class="flex flex-col gap-6">
<div class="bg-emerald-50 border border-emerald-200 rounded p-2.5 text-[13px] leading-snug">
<div class="font-bold text-emerald-700 mb-1">שפה סופית של <KatexInline math="\mathcal{A}_1" />:</div>
כל המילים הסופיות באורך גדול מ-0 שבהן כל האותיות הן <KatexInline math="a" />:
<div class="mt-2 text-center text-emerald-800" dir="ltr">
<KatexInline math="L(\mathcal{A}_1) = \{a\}^+" />
</div>
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-2.5 text-[13px] leading-snug">
<div class="font-bold text-emerald-700 mb-1">שפה סופית של <KatexInline math="\mathcal{A}_2" />:</div>
אותה שפה בדיוק (מגיעים ל מצב המקבל אחרי סדרת מעברי <KatexInline math="a" />):
<div class="mt-2 text-center text-emerald-800" dir="ltr">
<KatexInline math="L(\mathcal{A}_2) = \{a\}^+" />
</div>
</div>
</div>
</div>

<div v-click="1" class="mt-6 flex justify-center gap-8 items-center text-[22px] font-semibold border-t border-slate-100 pt-4">
<div class="text-blue-700" dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_1) \neq L_\omega(\mathcal{A}_2)" /></div>
<div class="text-slate-400">אבל</div>
<div class="text-red-600" dir="ltr"><KatexInline math="L(\mathcal{A}_1) = L(\mathcal{A}_2)" /></div>
</div>

---

# שקילות סופית ושקילות אינסופית: זהירות

<div class="grid grid-cols-2 gap-5 mt-8 text-right text-[21px] leading-snug">
<div class="bg-orange-50 border border-orange-200 rounded p-5">
<div class="font-bold text-orange-700 mb-2">באוטומטים לא דטרמיניסטיים</div>
שקילות כשפות סופיות אינה גוררת שקילות כשפות אינסופיות, וגם להפך.
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">באוטומטים דטרמיניסטיים</div>
אם שני האוטומטים דטרמיניסטיים ושלמים, שקילות סופית כן גוררת שקילות אינסופית.
</div>
</div>

<div class="mt-7 text-center text-[29px]" dir="ltr">
<KatexInline display math="L(\mathcal{A}_1)=L(\mathcal{A}_2)\;\Longrightarrow\;L_\omega(\mathcal{A}_1)=L_\omega(\mathcal{A}_2)" />
</div>

<div class="mt-3 text-center text-[18px]">
הכיוון ההפוך אינו נכון אפילו עבור אוטומטים דטרמיניסטיים.
</div>

---

# <span dir="ltr">NBA</span> עשירים יותר מ־<span dir="ltr">DBA</span>

<div class="mt-6 text-right text-[22px] leading-relaxed">
מעל מילים סופיות, <span dir="ltr">NFA</span> ו־<span dir="ltr">DFA</span> מתארים אותה מחלקת שפות.
מעל מילים אינסופיות זה כבר לא נכון:
</div>

<div class="mt-6 text-center text-[31px]" dir="ltr">
<KatexInline display math="\text{DBA}\subsetneq\text{NBA}" />
</div>

<div class="mt-6 bg-slate-50 border border-slate-200 rounded p-5 text-right text-[21px] leading-snug">
דוגמת המפתח היא השפה של מילים שבהן בשלב כלשהו מתחיל רצף אינסופי של <KatexInline math="B" />-ים:
<span dir="ltr"><KatexInline math="(A+B)^*B^\omega" /></span>.
אוטומט לא דטרמיניסטי יכול “לנחש” מתי התחיל הרצף הסופי האחרון של <KatexInline math="B" />-ים.
</div>

---

# אוטומט לא דטרמיניסטי ל־<span dir="ltr"><KatexInline math="(A+B)^*B^\omega" /></span>

<div class="grid grid-cols-[0.9fr_1.1fr] gap-5 mt-7 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="500" :height="220" :arrowSize="4.2" :stateLabelFontSize="16" :transitionLabelFontSize="14"
  :states="[
    { id: 'q0', x: 120, y: 110, label: '$q_0$', initial: true, initialDirection: 'top', r: 25, labelWidth: 70 },
    { id: 'q1', x: 330, y: 110, label: '$q_1$', accepting: true, r: 25, labelWidth: 70 }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$A,B$', loopDirection: '180deg', labelX: -24, labelWidth: 55 },
    { source: 'q0', target: 'q1', label: '$B$', labelY: -10, labelWidth: 45 },
    { source: 'q1', target: 'q1', label: '$B$', loopDirection: '0deg', labelX: 22, labelWidth: 45 }
  ]"
/>
</div>

<div class="text-right text-[22px] leading-relaxed">
האוטומט נשאר ב־<KatexInline math="q_0" /> כל עוד הוא עדיין “לא החליט”.
בקריאת <KatexInline math="B" /> הוא יכול לנחש שזהו תחילת הסיומת האינסופית של <KatexInline math="B" />-ים.
</div>
</div>

---

# למה אין <span dir="ltr">DBA</span> לשפה הזו?

<div class="text-right text-[20px] leading-snug mt-5">
נניח בשלילה שקיים <span dir="ltr">DBA</span> המקבל את <span dir="ltr"><KatexInline math="(A+B)^*B^\omega" /></span>.
</div>

<div class="grid grid-cols-3 gap-4 mt-5 text-right text-[18px] leading-snug">
<div v-click class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">1. מאלצים ביקורים מקבלים</div>
נזין מילים מהצורה <span dir="ltr"><KatexInline math="B^{n_1}AB^{n_2}A\cdots" /></span>, ובכל פעם נבחר מספיק <KatexInline math="B" />-ים כדי להגיע למצב מקבל.
</div>

<div v-click class="bg-orange-50 border border-orange-200 rounded p-4">
<div class="font-bold text-orange-700 mb-2">2. שובך היונים</div>
יש רק מספר סופי של מצבים מקבלים, לכן בשלב כלשהו נבקר באותו מצב מקבל פעמיים.
</div>

<div v-click class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">3. סתירה</div>
אפשר לחזור על הקטע שבין שני הביקורים ולקבל ריצה מקבלת על מילה שיש בה אינסוף <KatexInline math="A" />-ים.
אבל מילה כזו אינה בשפה.
</div>
</div>

---

# למה בניית החזקה לא עובדת?

<div class="mt-6 text-right text-[22px] leading-relaxed">
עבור מילים סופיות, בניית החזקה עוקבת אחרי קבוצת כל המצבים האפשריים של ה־<span dir="ltr">NFA</span>.
למילים אינסופיות הבעיה היא תנאי הקבלה:
</div>

<div class="grid grid-cols-2 gap-5 mt-6 text-right text-[20px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-2">מה עובד בסופי?</div>
מספיק שקיימת ריצה אחת שמסתיימת במצב מקבל.
לכן אם קבוצת המצבים מכילה מצב מקבל, אפשר לקבל את המילה הסופית.
</div>

<div class="bg-red-50 border border-red-200 rounded p-5">
<div class="font-bold text-red-700 mb-2">מה נכשל באינסופי?</div>
קבלת Büchi דורשת ריצה אחת שמבקרת במצב מקבל אינסוף פעמים.
אוטומט החזקה עלול לראות אינסוף רישות, שבכל אחת מהן ריצה אחרת מגיעה למצב מקבל.
</div>
</div>

---

# אוטומט Büchi מוכלל <span dir="ltr">(GNBA)</span>

<div class="mt-6 text-right text-[22px] leading-relaxed">
אוטומט Büchi מוכלל מחליף קבוצת קבלה אחת במספר קבוצות קבלה:
</div>

<div class="mt-4 text-center text-[29px]" dir="ltr">
<KatexInline display math="\mathcal{G}=\langle Q,\Sigma,\delta,Q_0,\mathcal{F}\rangle,\qquad \mathcal{F}=\{F_1,\ldots,F_k\}" />
</div>

<div class="grid grid-cols-2 gap-5 mt-5 text-right text-[20px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">תחביר</div>
כל <KatexInline math="F_i\subseteq Q" /> היא קבוצת מצבים שצריך לבקר בה.
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-5">
<div class="font-bold text-purple-700 mb-2">משמעות</div>
ריצה מקבלת אם לכל <KatexInline math="F_i\in\mathcal{F}" /> היא מבקרת ב־<KatexInline math="F_i" /> אינסוף פעמים.
</div>
</div>

---

# דוגמה: שני תנאי קבלה

<div class="grid grid-cols-[0.95fr_1.05fr] gap-5 mt-6 items-center">
<div class="bg-white rounded border border-slate-200 shadow-sm">
<AutomatonD3 variant="classic" :width="500" :height="230" :arrowSize="4.2" :stateLabelFontSize="16" :transitionLabelFontSize="13"
  :states="[
    { id: 'q0', x: 245, y: 115, label: '$q_0$', initial: true, initialDirection: 'top', r: 25, labelWidth: 70 },
    { id: 'q1', x: 95, y: 115, label: '$q_1$', r: 25, labelWidth: 70, stroke: '#2563eb' },
    { id: 'q2', x: 395, y: 115, label: '$q_2$', r: 25, labelWidth: 70, stroke: '#dc2626' }
  ]"
  :transitions="[
    { source: 'q0', target: 'q0', label: '$true$', loopDirection: '90deg', labelY: 8, labelWidth: 50 },
    { source: 'q0', target: 'q1', label: '$crit_1$', labelY: -12, labelWidth: 70, curve: -0.18 },
    { source: 'q1', target: 'q0', label: '$true$', labelY: 18, labelWidth: 50, curve: -0.18 },
    { source: 'q0', target: 'q2', label: '$crit_2$', labelY: -12, labelWidth: 70, curve: -0.18 },
    { source: 'q2', target: 'q0', label: '$true$', labelY: 18, labelWidth: 50, curve: -0.18 }
  ]"
/>
</div>

<div class="text-right text-[21px] leading-relaxed">
הדרישה:
<div class="mt-3 text-center text-[25px]" dir="ltr">
<KatexInline display math="\text{Always Eventually }crit_1 \;\land\; \text{Always Eventually }crit_2" />
</div>
תנאי הקבלה:
<div class="mt-3 text-center text-[25px]" dir="ltr">
<KatexInline display math="\mathcal{F}=\{\{q_1\},\{q_2\}\}" />
</div>
</div>
</div>

---

# מ־<span dir="ltr">GNBA</span> ל־<span dir="ltr">NBA</span>: הרעיון

<div class="mt-6 text-right text-[22px] leading-relaxed">
אם צריך לבקר בכל אחת מהקבוצות <span dir="ltr"><KatexInline math="F_1,\ldots,F_k" /></span> אינסוף פעמים,
נעקוב אחרי “איזו קבוצה אנחנו מחכים לראות עכשיו”.
</div>

<div class="grid grid-cols-3 gap-4 mt-6 text-right text-[18px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">1. משכפלים</div>
בונים <KatexInline math="k" /> עותקים של האוטומט.
עותק <KatexInline math="i" /> מייצג המתנה לביקור הבא ב־<KatexInline math="F_i" />.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">2. עוברים עותק</div>
כאשר המעבר יוצא ממצב שנמצא ב־<KatexInline math="F_i" />, עוברים לעותק הבא.
אחרת נשארים באותו עותק.
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-4">
<div class="font-bold text-purple-700 mb-2">3. מקבלים במחזור</div>
מסמנים קבלה בעותק הראשון.
ביקור אינסופי שם מבטיח שסיימנו אינסוף סבבים דרך כל קבוצות הקבלה.
</div>
</div>

---

# הבנייה הפורמלית

<div class="mt-4 text-right text-[20px] leading-snug">
יהי <span dir="ltr"><KatexInline math="\mathcal{G}=\langle Q,\Sigma,\delta,Q_0,\{F_1,\ldots,F_k\}\rangle" /></span>.
נבנה <span dir="ltr"><KatexInline math="\mathcal{A}" /></span> שקול:
</div>

<div class="grid grid-cols-2 gap-4 mt-5 text-right text-[18px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מצבים והתחלה</div>
<div class="text-center text-[23px]" dir="ltr">
<KatexInline display math="Q_\mathcal{A}=Q\times\{1,\ldots,k\}" />
<KatexInline display math="Q_{0,\mathcal{A}}=Q_0\times\{1\}" />
</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">קבלה</div>
<div class="text-center text-[23px]" dir="ltr">
<KatexInline display math="F_\mathcal{A}=F_1\times\{1\}" />
</div>
</div>
</div>

<div class="mt-5 text-center text-[24px]" dir="ltr">
<KatexInline display math="(q,i)\xrightarrow{a}(q',j)\quad\text{if}\quad q'\in\delta(q,a)" />
<KatexInline display math="j=\begin{cases} i & q\notin F_i\\ i\bmod k+1 & q\in F_i\end{cases}" />
</div>

---

# למה הבנייה נכונה?

<div class="grid grid-cols-2 gap-5 mt-7 text-right text-[20px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">אם ה־GNBA מקבל</div>
בריצה המקבלת רואים כל <KatexInline math="F_i" /> אינסוף פעמים.
לכן אפשר לעבור שוב ושוב בעותקים <KatexInline math="1,2,\ldots,k" /> ולחזור לעותק הראשון אינסוף פעמים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-2">אם ה־NBA מקבל</div>
ביקור אינסופי בקבוצת הקבלה של העותק הראשון אומר שהאוטומט השלים אינסוף סבבים.
כל סבב כולל ביקור בכל אחת מהקבוצות <KatexInline math="F_i" />.
</div>
</div>

<div class="mt-7 text-center text-[29px]" dir="ltr">
<KatexInline display math="L_\omega(\mathcal{G})=L_\omega(\mathcal{A})" />
</div>

---

# חיתוך שפות באמצעות <span dir="ltr">GNBA</span>

<div class="mt-6 text-right text-[22px] leading-relaxed">
מכפלה רגילה של שני אוטומטי Büchi לא מספיקה, כי צריך לוודא ביקורים אינסופיים בשני תנאי הקבלה.
<span dir="ltr">GNBA</span> נותן בדיוק את הדרך לומר “גם וגם”.
</div>

<div class="mt-6 text-center text-[29px]" dir="ltr">
<KatexInline display math="\mathcal{G}=\mathcal{G}_1\times\mathcal{G}_2" />
</div>

<div class="grid grid-cols-2 gap-5 mt-5 text-right text-[19px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-5">
<div class="font-bold text-blue-700 mb-2">המכפלה</div>
המצבים הם זוגות <KatexInline math="Q_1\times Q_2" /> והמעברים מתקדמים בשני האוטומטים יחד.
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-5">
<div class="font-bold text-purple-700 mb-2">תנאי הקבלה</div>
לוקחים את כל התנאים משני הצדדים:
<div class="mt-2 text-center" dir="ltr">
<KatexInline display math="\mathcal{F}=\{F\times Q_2\mid F\in\mathcal{F}_1\}\cup\{Q_1\times F\mid F\in\mathcal{F}_2\}" />
</div>
</div>
</div>

---

# מסלול הבנייה לחיתוך

<div class="grid grid-cols-3 gap-4 mt-8 text-right text-[18px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">1. בונים GNBA</div>
המכפלה שומרת את כל תנאי הקבלה של שני האוטומטים.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-4">
<div class="font-bold text-emerald-700 mb-2">2. ממירים ל־NBA</div>
משתמשים בבניית העותקים כדי להפוך את תנאי הקבלה המוכללים לתנאי Büchi רגיל.
</div>

<div class="bg-orange-50 border border-orange-200 rounded p-4">
<div class="font-bold text-orange-700 mb-2">3. מקבלים סגירות לחיתוך</div>
כך מקבלים אוטומט Büchi רגיל לשפה
<span dir="ltr"><KatexInline math="L_\omega(\mathcal{A}_1)\cap L_\omega(\mathcal{A}_2)" /></span>.
</div>
</div>

---

# סיכום

<div class="grid grid-cols-2 gap-5 mt-7 text-right text-[20px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-5">
<div class="font-bold mb-2">מה למדנו על Büchi?</div>

- ריקות נבדקת על ידי חיפוש מחזור מקבל נגיש.
- <span dir="ltr">NBA</span> חזקים מ־<span dir="ltr">DBA</span>.
- בניית החזקה אינה משמרת את תנאי הקבלה האינסופי.
</div>

<div class="bg-emerald-50 border border-emerald-200 rounded p-5">
<div class="font-bold text-emerald-700 mb-2">למה GNBA שימושיים?</div>

- הם מאפשרים כמה תנאי קבלה במקביל.
- אפשר לתרגם כל <span dir="ltr">GNBA</span> ל־<span dir="ltr">NBA</span>.
- הם נותנים בנייה נקייה לחיתוך שפות Büchi.
</div>
</div>

<div class="mt-7 text-center text-[29px]" dir="ltr">
<KatexInline display math="\text{NBA}=\omega\text{-regular languages},\qquad \text{GNBA}\equiv\text{NBA}" />
</div>
