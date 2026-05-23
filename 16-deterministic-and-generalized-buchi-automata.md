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
<div class="bg-white rounded border border-slate-200 shadow-sm p-2 w-[340px] relative">
<div class="text-[11px] text-slate-400 absolute top-2 right-3 font-mono font-semibold"><KatexInline math="\mathcal{A}_1" /></div>
<AutomatonD3 variant="classic" :width="320" :height="135" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="13"
:states="[
{ id: 's0', x: 80, y: 75, label: '$s_0$', initial: true, initialDirection: 'left', r: 20 },
{ id: 's1', x: 240, y: 75, label: '$s_1$', accepting: true, r: 20 }
]"
:transitions="[
{ source: 's0', target: 's1', label: '$a$', labelY: -10, labelWidth: 40 },
{ source: 's1', target: 's1', label: '$a$', loopDirection: '-90deg', labelY: -12, labelWidth: 40 }
]"
/>
</div>

<!-- Nondeterminism Arrow and Badge Overlay -->
<svg v-click="2" style="width: 340px; height: 310px;" class="absolute z-20 top-0 left-0 pointer-events-none overflow-visible" viewBox="0 0 340 310">
<defs>
<marker id="nondet-arrow-marker" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626" />
</marker>
</defs>
</svg>

<div v-click="2" class="absolute z-30 top-[180px] left-[140px] -rotate-[29deg] pointer-events-none">
<div class="relative bg-red-600 text-white font-bold py-1 px-3 text-[12px] rounded-r shadow-md border border-red-700 whitespace-nowrap">
<div class="absolute top-1/2 left-[-15px] -translate-y-1/2 w-0 h-0 border-y-[14px] border-y-transparent border-r-[15px] border-r-red-600"></div>
<div class="absolute top-1/2 left-[-17px] -translate-y-1/2 w-0 h-0 border-y-[16px] border-y-transparent border-r-[17px] border-r-red-700 -z-10"></div>
בחירה לא דטרמיניסטית
</div>
</div>

<!-- Automaton 2 -->
<div class="bg-white rounded border border-slate-200 shadow-sm p-2 w-[340px] relative">
<div class="text-[11px] text-slate-400 absolute top-2 right-3 font-mono font-semibold"><KatexInline math="\mathcal{A}_2" /></div>
<AutomatonD3 variant="classic" :width="320" :height="135" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="13"
:states="[
{ id: 's0', x: 80, y: 75, label: '$s_0$', initial: true, initialDirection: 'left', r: 20 },
{ id: 's1', x: 240, y: 75, label: '$s_1$', accepting: true, r: 20 }
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

# שקילות אוטומטים דטרמיניסטיים: שלבי ההוכחה

<div class="mt-2 text-right text-[18px] leading-snug">
נניח ש־<KatexInline math="\mathcal{A}_1,\mathcal{A}_2" /> דטרמיניסטיים ושלמים, וש־<KatexInline math="L(\mathcal{A}_1)=L(\mathcal{A}_2)" />.
נוכיח שגם <KatexInline math="L_\omega(\mathcal{A}_1)=L_\omega(\mathcal{A}_2)" />.
</div>

<div class="mt-3 mx-auto w-[860px] rounded border border-slate-200 bg-white px-5 py-3 shadow-sm" dir="ltr">
<div class="flex flex-col items-center gap-0 text-center">
<div v-click="1" class="text-[22px]"><KatexInline math="w\in L_\omega(\mathcal{A}_1)" /></div>

<div class="relative h-[31px] w-[640px]">
<div v-click="2" class="absolute left-1/2 top-0 -translate-x-1/2 text-[26px] leading-none text-slate-500">⇕</div>
<div v-click="3" class="absolute left-[10px] top-[6px] w-[285px] text-[14px] text-slate-600 leading-tight text-right" dir="rtl">
הגדרת קבלת Büchi
<span v-click="9" class="text-amber-700 font-bold"> באוטומט דטרמיניסטי</span>
</div>
</div>

<div v-click="2" class="text-[20px]"><KatexInline math="\underset{\infty}{\exists} i\ \left(w[0..i]\in L(\mathcal{A}_1)\right)" /></div>

<div class="relative h-[31px] w-[640px]">
<div v-click="4" class="absolute left-1/2 top-0 -translate-x-1/2 text-[26px] leading-none text-rose-700">⇕</div>
<div v-click="5" class="absolute left-[30px] top-[6px] w-[260px] text-[14px] text-rose-700 font-bold leading-tight text-right" dir="rtl">
מההנחה <KatexInline math="L(\mathcal{A}_1)=L(\mathcal{A}_2)" />
</div>
</div>

<div v-click="4" class="text-[20px]"><KatexInline math="\underset{\infty}{\exists} i\ \left(w[0..i]\in L(\mathcal{A}_2)\right)" /></div>

<div class="relative h-[31px] w-[640px]">
<div v-click="6" class="absolute left-1/2 top-0 -translate-x-1/2 text-[26px] leading-none text-slate-500">⇕</div>
<div v-click="7" class="absolute left-[-30px] top-[6px] w-[330px] text-[14px] text-slate-600 leading-tight text-right" dir="rtl">
שוב הגדרת קבלת Büchi
<span v-click="9" class="text-amber-700 font-bold"> באוטומט דטרמיניסטי</span>
</div>
</div>

<div v-click="6" class="text-[22px]"><KatexInline math="w\in L_\omega(\mathcal{A}_2)" /></div>
</div>
</div>

<div v-click="8" class="mt-3 rounded border border-amber-200 bg-amber-50 px-5 py-2 text-right text-[17px] leading-snug font-bold text-amber-800">
איפה השתמשנו בנתון שהאוטומטים דטרמיניסטיים?
</div>

<div v-click="9" class="mt-2 rounded border border-amber-200 bg-amber-50 px-5 py-2 text-right text-[16px] leading-snug">
באוטומט דטרמיניסטי יש ריצה יחידה על <KatexInline math="w" />. לכן “התחילית <KatexInline math="w[0..i]" /> מתקבלת” אומר בדיוק שהריצה היחידה נמצאת במצב מקבל בזמן <KatexInline math="i" />. באוטומט לא דטרמיניסטי תחיליות שונות יכולות להתקבל על ידי ריצות שונות, שלא בהכרח מתחברות לריצה אינסופית אחת.
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

<div class="text-right text-[17px] leading-snug mt-3">
נניח בשלילה שקיים <span dir="ltr">DBA</span> <KatexInline math="\mathcal{A}" /> המקבל את
<span dir="ltr"><KatexInline math="(A+B)^*B^\omega" /></span>, 
<br>
כלומר את כל המילים שבהן החל ממקום כלשהו מופיעים רק <KatexInline math="B" />-ים ורק אותן.
</div>

<div class="mt-3 space-y-2 text-right text-[15px] leading-snug">
<div v-click class="bg-blue-50 border border-blue-200 rounded px-4 py-2">
<div class="font-bold text-blue-700 mb-1">1. מתחילים ממילה שחייבת להתקבל</div>
המילה <KatexInline math="B^\omega" /> בשפה, ולכן הריצה היחידה של <KatexInline math="\mathcal{A}" /> עליה מקבלת.
לכן קיים <KatexInline math="n_1" /> כך שאחרי קריאת <KatexInline math="B^{n_1}" /> הריצה נמצאת במצב מקבל.
</div>

<div v-click class="bg-blue-50 border border-blue-200 rounded px-4 py-2">
<div class="font-bold text-blue-700 mb-1">2. מוסיפים <KatexInline math="A" /> וחוזרים על אותו נימוק</div>
גם <KatexInline math="B^{n_1}AB^\omega" /> בשפה, כי אחרי ה־<KatexInline math="A" /> נשארים רק <KatexInline math="B" />-ים.
מכיוון שהאוטומט דטרמיניסטי, הריצה על התחילית <KatexInline math="B^{n_1}A" /> כבר נקבעה.
כדי לקבל את המשך <KatexInline math="B^\omega" />, חייב להיות <KatexInline math="n_2" /> כך שאחרי
<KatexInline math="B^{n_1}AB^{n_2}" /> שוב נמצאים במצב מקבל.
</div>

<div v-click class="bg-orange-50 border border-orange-200 rounded px-4 py-2">
<div class="font-bold text-orange-700 mb-1">3. ממשיכים באינדוקציה</div>
באותו אופן בוחרים <KatexInline math="n_3,n_4,\ldots" /> כך שהריצה על
<span dir="ltr"><KatexInline math="B^{n_1}AB^{n_2}AB^{n_3}A\cdots" /></span>
מבקרת במצב מקבל אחרי כל בלוק <KatexInline math="B^{n_i}" />.
</div>

<div v-click class="bg-red-50 border border-red-200 rounded px-4 py-2">
<div class="font-bold text-red-700 mb-1">4. הסתירה</div>
קיבלנו מילה עם אינסוף מופעים של <KatexInline math="A" />, ולכן היא אינה ב־<KatexInline math="(A+B)^*B^\omega" />.
אבל הריצה הדטרמיניסטית עליה מבקרת במצבים מקבלים אינסוף פעמים, ולכן <KatexInline math="\mathcal{A}" /> מקבל אותה. סתירה.
</div>
</div>

---

# למה בניית החזקה לא עובדת?

<div class="mt-4 text-right text-[19px] leading-relaxed">
עבור מילים סופיות, בניית החזקה עוקבת אחרי קבוצת כל המצבים האפשריים של ה־<span dir="ltr">NFA</span>.
למילים אינסופיות הבעיה היא תנאי הקבלה:
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-right text-[17px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-4">
<div class="font-bold mb-2">מה עובד בסופי?</div>
מספיק שקיימת ריצה אחת שמסתיים במצב מקבל.
לכן אם קבוצת המצבים מכילה מצב מקבל, אפשר לקבל את המילה הסופית.
</div>

<div class="bg-red-50 border border-red-200 rounded p-4">
<div class="font-bold text-red-700 mb-2">מה נכשל באינסופי?</div>
קבלת Büchi דורשת ריצה אחת שמבקרת במצב מקבל אינסוף פעמים.
אוטומט החזקה עלול לראות אינסוף רישות, שבכל אחת מהן ריצה אחרת מגיעה למצב מקבל.
</div>
</div>

<div class="bg-blue-50 border border-blue-200 rounded p-3 mt-4 text-right text-[15px] leading-snug">
<div class="font-bold text-blue-700 mb-1">תזכורת: בניית החזקה (Subset Construction)</div>
בניית החזקה מתרגמת אוטומט לא-דטרמיניסטי לדטרמיניסטי על ידי מעקב אחר קבוצת המצבים האפשריים: 
כל מצב באוטומט החדש הוא קבוצת מצבים <KatexInline math="S \subseteq Q" /> של האוטומט המקורי, ויחס המעברים מוגדר על ידי:
<div class="mt-1 text-center" dir="ltr">
<KatexInline display math="\delta_{\mathcal{D}}(S, a) = \bigcup_{q \in S} \delta(q, a)" />
</div>
</div>

---

# דוגמה: כישלון בניית החזקה ב־Büchi

<div class="grid grid-cols-2 gap-6 mt-4 text-right">
<!-- Left Column: NBA -->
<div class="flex flex-col gap-3">
<div class="font-bold text-[18px] text-slate-700">האוטומט הלא-דטרמיניסטי <KatexInline math="\mathcal{A}" />:</div>
<div class="bg-white rounded border border-slate-200 shadow-sm p-3 w-full relative">
<div class="text-[11px] text-slate-400 absolute top-2 right-3 font-mono font-semibold">NBA</div>
<AutomatonD3 variant="classic" :width="380" :height="140" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="13"
:states="[
{ id: 'q0', x: 100, y: 70, label: '$q_0$', initial: true, initialDirection: 'left', r: 22 },
{ id: 'q1', x: 280, y: 70, label: '$q_1$', accepting: true, r: 22 }
]"
:transitions="[
{ source: 'q0', target: 'q0', label: '$a$', loopDirection: '-90deg', labelY: -12, labelWidth: 40 },
{ source: 'q0', target: 'q1', label: '$a$', labelY: -10, labelWidth: 40 }
]"
/>
</div>
<div class="bg-blue-50 border border-blue-100 rounded p-3 text-[14px] leading-snug">
<div class="font-bold text-blue-700 mb-1">שפת Büchi:</div>
אין אף ריצה אינסופית שיכולה לבקר ב־<KatexInline math="q_1" /> אינסוף פעמים (כי אין מעברים מתוך <KatexInline math="q_1" />).
<div class="mt-2 font-semibold text-center text-blue-800" dir="ltr">
<KatexInline math="L_\omega(\mathcal{A}) = \emptyset" />
</div>
</div>
</div>

<!-- Right Column: Subset Construction DBA -->
<div class="flex flex-col gap-3">
<div class="font-bold text-[18px] text-slate-700">אוטומט החזקה המתקבל <KatexInline math="\mathcal{D}" />:</div>
<div class="bg-white rounded border border-slate-200 shadow-sm p-3 w-full relative">
<div class="text-[11px] text-slate-400 absolute top-2 right-3 font-mono font-semibold">DBA (Subset)</div>
<AutomatonD3 variant="classic" :width="380" :height="140" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="13"
:states="[
{ id: 's0', x: 100, y: 70, label: '$\\{q_0\\}$', initial: true, initialDirection: 'left', r: 22 },
{ id: 's1', x: 280, y: 70, label: '$\\{q_0, q_1\\}$', accepting: true, r: 28 }
]"
:transitions="[
{ source: 's0', target: 's1', label: '$a$', labelY: -10, labelWidth: 40 },
{ source: 's1', target: 's1', label: '$a$', loopDirection: '-90deg', labelY: -12, labelWidth: 40 }
]"
/>
</div>
<div class="bg-emerald-50 border border-emerald-100 rounded p-3 text-[14px] leading-snug">
<div class="font-bold text-emerald-700 mb-1">שפת Büchi של אוטומט החזקה:</div>
המצב המקבל <KatexInline math="\{q_0,q_1\}" /> מבוקר אינסוף פעמים על המילה <KatexInline math="a^\omega" />.
<div class="mt-2 font-semibold text-center text-emerald-800" dir="ltr">
<KatexInline math="L_\omega(\mathcal{D}) = \{a^\omega\}" />
</div>
</div>
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-3.5 mt-4 text-right text-[13.5px] leading-snug">
<div class="font-bold text-red-700 mb-1">מדוע זה נכשל?</div>
בכל קידומת סופית של המילה, קיימת ריצה כלשהי שמגיעה למצב המקבל <KatexInline math="q_1" />. 
לכן אוטומט החזקה עוקב אחרי הקבוצה <KatexInline math="\{q_0,q_1\}" /> ומקבל את המילה.
אולם, אין <b>ריצה אינסופית אחת ויחידה</b> שמבקרת ב־<KatexInline math="q_1" /> אינסוף פעמים. בניית החזקה מאבדת את הקישוריות בין הריצות השונות.
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

<div class="flex flex-col items-center gap-3 mt-3 text-right">
<div class="bg-white rounded border border-slate-200 shadow-sm p-1 w-[860px] max-w-full flex justify-center">
<AutomatonD3 variant="classic" :width="450" :height="140" :arrowSize="4" :stateLabelFontSize="15" :transitionLabelFontSize="12"
:states="[
{ id: 'q0', x: 225, y: 65, label: '$q_0$', initial: true, initialDirection: 'top', r: 22, labelWidth: 60 },
{ id: 'q1', x: 75, y: 65, label: '$q_1$', accepting: true, r: 22, labelWidth: 60, stroke: '#2563eb' },
{ id: 'q2', x: 375, y: 65, label: '$q_2$', accepting: true, r: 22, labelWidth: 60, stroke: '#dc2626' }
]"
:transitions="[
{ source: 'q0', target: 'q0', label: '$true$', loopDirection: '90deg', labelY: 8, labelWidth: 50 },
{ source: 'q0', target: 'q1', label: '$crit_1$', labelY: 12, labelWidth: 70, curve: -0.18 },
{ source: 'q1', target: 'q0', label: '$true$', labelY: -12, labelWidth: 50, curve: -0.18 },
{ source: 'q0', target: 'q2', label: '$crit_2$', labelY: -12, labelWidth: 70, curve: -0.18 },
{ source: 'q2', target: 'q0', label: '$true$', labelY: 12, labelWidth: 50, curve: -0.18 }
]"
/>
</div>

<div class="w-[860px] max-w-full flex flex-col gap-2 text-[15px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-2.5">
<div class="font-bold text-blue-700 mb-1">הדרישה:</div>
אינסוף פעמים בקר בקטע הקריטי הראשון <b>וגם</b> אינסוף פעמים בשני:
<div class="mt-1 text-center text-[19px]" dir="ltr">
<KatexInline display math="\text{Always Eventually }crit_1 \;\land\; \text{Always Eventually }crit_2" />
</div>
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-2.5">
<div class="font-bold text-purple-700 mb-1">תנאי הקבלה (Generalized Büchi):</div>
שתי קבוצות קבלה נפרדות, <span class="text-blue-700 font-semibold"><KatexInline math="F_1" /></span> ו־<span class="text-red-600 font-semibold"><KatexInline math="F_2" /></span>, שצריך לבקר בכל אחת מהן אינסוף פעמים:
<div class="mt-1 text-center text-[19px]" dir="ltr">
<KatexInline display math="\mathcal{F} = \{ \textcolor{#2563eb}{F_1}, \textcolor{#dc2626}{F_2} \} = \{ \{ \textcolor{#2563eb}{q_1} \}, \{ \textcolor{#dc2626}{q_2} \} \}" />
</div>
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

<div class="mt-3 text-right text-[16px] leading-snug">
יהי <span dir="ltr"><KatexInline math="\mathcal{G}=\langle Q,\Sigma,\delta,Q_0,\{F_1,\ldots,F_k\}\rangle" /></span>.
נבנה <span dir="ltr"><KatexInline math="\mathcal{A}" /></span> שקול:
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-right text-[14px] leading-snug">
<div class="bg-slate-50 border border-slate-200 rounded p-3">
<div class="font-bold mb-1">מצבים והתחלה</div>
<div class="text-center text-[17px]" dir="ltr">
<KatexInline display math="Q_\mathcal{A}=Q\times\{1,\ldots,k\}" />
<KatexInline display math="Q_{0,\mathcal{A}}=Q_0\times\{1\}" />
</div>
</div>

<div class="bg-slate-50 border border-slate-200 rounded p-3">
<div class="font-bold mb-1">קבלה</div>
<div class="text-center text-[17px]" dir="ltr">
<KatexInline display math="F_\mathcal{A}=F_1\times\{1\}" />
</div>
</div>
</div>

<div class="mt-4 text-center text-[18px]" dir="ltr">
<KatexInline display math="\langle q,i\rangle\xrightarrow{a}\langle q',j\rangle\quad\text{if}\quad q'\in\delta(q,a)" />
<KatexInline display math="j=\begin{cases} i & q\notin F_i\\ i\bmod k+1 & q\in F_i\end{cases}" />
</div>

---

# דוגמה לבנייה: מ־<span dir="ltr">GNBA</span> ל־<span dir="ltr">NBA</span>

<div class="grid grid-cols-[0.8fr_1.2fr] gap-4 mt-2 text-right">
<!-- Left Column: Steps of the construction -->
<div class="bg-gray-50 border border-gray-200 rounded p-3 text-[11px] leading-snug">
<ul class="list-disc list-inside space-y-1">
  <li><strong>שלב 1: כותבים שני עותקים עצמאיים.</strong> כל עותק מכיל את כל המצבים והמעברים המקוריים ללא מעברים ביניהם (שני עותקים זהים).</li>
  <li v-click="1" :class="{ 'text-blue-700 font-semibold': $clicks === 1 }"><strong>שלב 2: מעברים מ־<KatexInline math="q_1" /> לעותק השני.</strong> במעבר מ־<KatexInline math="q_1" /> בעותק הראשון (שנמצא ב־<KatexInline math="F_1" />), במקום להיכנס למצב הבא בעותק הראשון, נכנסים אליו בעותק השני.</li>
  <li v-click="2" :class="{ 'text-red-700 font-semibold': $clicks === 2 }"><strong>שלב 3: מעברים מ־<KatexInline math="q_2" /> לעותק הראשון.</strong> במעבר מ־<KatexInline math="q_2" /> בעותק השני (שנמצא ב־<KatexInline math="F_2" />), במקום להיכנס למצב הבא בעותק השני, חוזרים לעותק הראשון.</li>
  <li v-click="3" :class="{ 'text-emerald-700 font-semibold': $clicks >= 3 }"><strong>שלב 4: קביעת המצבים המקבלים ב־NBA.</strong> מסמנים כקבוצת הקבלה החדשה רק את העותק הראשון של <KatexInline math="F_1" />, כלומר <KatexInline math="F_{\mathcal{A}} = \{\langle q_1,1\rangle\}" /> (צבוע בשחור, בעוד העותק השני מאבד את סימון הקבלה).</li>
</ul>
<div class="mt-2 text-xs text-gray-500 font-medium">
  <span v-if="$clicks === 0">לחצו על המצגת כדי להעביר את המעברים מ־<KatexInline math="q_1" />...</span>
  <span v-else-if="$clicks === 1">לחצו כדי להעביר את המעברים מ־<KatexInline math="q_2" />...</span>
  <span v-else-if="$clicks === 2">לחצו כדי לסמן את מצבי הקבלה...</span>
  <span v-else>הבנייה הושלמה! 🎉</span>
</div>
</div>

<!-- Right Column: Automata (GNBA above NBA) -->
<div class="flex flex-col gap-3">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-[14px]">
<span class="font-bold text-blue-700">GNBA המקור (שני תנאי קבלה):</span>
<div class="mt-1 text-xs text-gray-700">
<KatexInline math="F_1=\{q_1\}" /> (כחול), <KatexInline math="F_2=\{q_2\}" /> (אדום).
</div>
<div class="flex justify-center mt-2 bg-white rounded border border-slate-100 p-1">
<AutomatonD3 variant="classic" :width="230" :height="90" :arrowSize="3.5" :stateLabelFontSize="9" :transitionLabelFontSize="9"
:states="[
  { id: 'q0', x: 115, y: 45, label: '$q_0$', initial: true, initialDirection: 'top', r: 15, labelWidth: 40 },
  { id: 'q1', x: 30, y: 45, label: '$q_1$', accepting: true, r: 15, labelWidth: 40, stroke: '#2563eb' },
  { id: 'q2', x: 200, y: 45, label: '$q_2$', accepting: true, r: 15, labelWidth: 40, stroke: '#dc2626' }
]"
:transitions="[
  { source: 'q0', target: 'q0', label: '$true$', loopDirection: '90deg', loopRadius: 40, labelY: 6, labelWidth: 25 },
  { source: 'q0', target: 'q1', label: '$crit_1$', labelY: 8, labelWidth: 35, curve: -0.15 },
  { source: 'q1', target: 'q0', label: '$true$', labelY: -8, labelWidth: 25, curve: -0.15 },
  { source: 'q0', target: 'q2', label: '$crit_2$', labelY: -8, labelWidth: 35, curve: -0.15 },
  { source: 'q2', target: 'q0', label: '$true$', labelY: 8, labelWidth: 25, curve: -0.15 }
]"
/>
</div>
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-3 text-[14px]">
<span class="font-bold text-purple-700">ה־NBA השקול (שני עותקים):</span>
<div class="mt-1 text-xs text-gray-700">
קבוצת הקבלה ב־NBA היא רק העותק הראשון של <KatexInline math="F_1" />, כלומר <KatexInline math="F_{\mathcal{A}} = \{\langle q_1,1\rangle\}" /> (מסומן בכחול).
</div>
<div class="flex justify-center mt-2 bg-white rounded border border-slate-100 p-1">
<AutomatonD3 variant="classic" :width="380" :height="195" :arrowSize="4" :stateLabelFontSize="9" :transitionLabelFontSize="10"
:states="[
  { id: 's1_q1', x: 50, y: 50, label: '$⟨q_1,1⟩$', accepting: true, r: 16, labelWidth: 60, stroke: $clicks >= 3 ? '#000000' : '#2563eb' },
  { id: 's1_q0', x: 190, y: 50, label: '$⟨q_0,1⟩$', initial: true, initialDirection: 'top', r: 16, labelWidth: 60 },
  { id: 's1_q2', x: 330, y: 50, label: '$⟨q_2,1⟩$', r: 16, labelWidth: 60 },
  { id: 's2_q1', x: 50, y: 145, label: '$⟨q_1,2⟩$', r: 16, labelWidth: 60 },
  { id: 's2_q0', x: 190, y: 145, label: '$⟨q_0,2⟩$', r: 16, labelWidth: 60 },
  { id: 's2_q2', x: 330, y: 145, label: '$⟨q_2,2⟩$', accepting: $clicks < 3, r: 16, labelWidth: 60, stroke: $clicks >= 3 ? '#6b7280' : '#dc2626' }
]"
:transitions="[
  { source: 's1_q0', target: 's1_q0', label: '$true$', loopDirection: '90deg', loopRadius: 45, labelY: 6, labelWidth: 30 },
  { source: 's1_q0', target: 's1_q1', label: '$crit_1$', labelY: 10, labelWidth: 35, curve: -0.15 },
  { source: 's1_q0', target: 's1_q2', label: '$crit_2$', labelY: -10, labelWidth: 35, curve: -0.15 },
  { source: 's1_q2', target: 's1_q0', label: '$true$', labelY: 10, labelWidth: 30, curve: -0.15 },
  ...($clicks === 0 ? [{ source: 's1_q1', target: 's1_q0', label: '$true$', labelY: -12, labelWidth: 30, curve: -0.15 }] : []),
  ...($clicks >= 1 ? [{ source: 's1_q1', target: 's2_q0', label: '$true$', labelY: 12, labelWidth: 30, curve: 0, stroke: $clicks === 1 ? '#2563eb' : '#6b7280', strokeWidth: $clicks === 1 ? 3 : 1.6, labelColor: $clicks === 1 ? '#2563eb' : '#6b7280' }] : []),
  { source: 's2_q0', target: 's2_q0', label: '$true$', loopDirection: '90deg', loopRadius: 45, labelY: 6, labelWidth: 30 },
  { source: 's2_q0', target: 's2_q1', label: '$crit_1$', labelY: 10, labelWidth: 35, curve: -0.15 },
  { source: 's2_q1', target: 's2_q0', label: '$true$', labelY: -12, labelWidth: 30, curve: -0.15 },
  { source: 's2_q0', target: 's2_q2', label: '$crit_2$', labelY: -10, labelWidth: 35, curve: -0.15 },
  ...($clicks < 2 ? [{ source: 's2_q2', target: 's2_q0', label: '$true$', labelY: 10, labelWidth: 30, curve: -0.15 }] : []),
  ...($clicks >= 2 ? [{ source: 's2_q2', target: 's1_q0', label: '$true$', labelY: -12, labelWidth: 30, curve: 0, stroke: $clicks === 2 ? '#dc2626' : '#6b7280', strokeWidth: $clicks === 2 ? 3 : 1.6, labelColor: $clicks === 2 ? '#dc2626' : '#6b7280' }] : [])
]"
/>
</div>
</div>
</div>
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
המצבים הם זוגות <KatexInline math="Q_1\times Q_2" /> והמעברים מתקדמים בשני האוטומטים יחד:
<div class="mt-2 text-center text-[16px]" dir="ltr">
<KatexInline display math="\delta(\langle q_1, q_2\rangle, a) = \delta_1(q_1, a) \times \delta_2(q_2, a)" />
</div>
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-5">
<div class="font-bold text-purple-700 mb-2">תנאי הקבלה</div>
לוקחים את כל התנאים משני הצדדים:
<div class="mt-2 text-center text-[13px]" dir="ltr">
<KatexInline display math="\mathcal{F}=\{F\times Q_2\mid F\in\mathcal{F}_1\}\cup\{Q_1\times F\mid F\in\mathcal{F}_2\}" />
</div>
</div>
</div>

---

# מסלול הבנייה לחיתוך

<div class="grid grid-cols-3 gap-4 mt-8 text-right text-[18px] leading-snug">
<div class="bg-blue-50 border border-blue-200 rounded p-4">
<div class="font-bold text-blue-700 mb-2">1. בונים את GNBA המכפלה</div>
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

<div class="mt-5 bg-gray-50 border border-gray-200 rounded p-4 text-right text-[15px] leading-snug">
<div class="font-bold text-gray-700 mb-1">דוגמה למסלול הבנייה:</div>
נניח שרוצים לחתוך את השפות מעל <KatexInline math="\Sigma=\{a,b\}" />:
<ul class="list-disc list-inside mr-2">
<li><KatexInline math="L_1" />: "אינסוף <KatexInline math="a" />-ים" (עם תנאי קבלה <KatexInline math="F_1" />)</li>
<li><KatexInline math="L_2" />: "אינסוף <KatexInline math="b" />-ים" (עם תנאי קבלה <KatexInline math="F_2" />)</li>
</ul>
<div class="mt-2">
<strong>שלב 1:</strong> בונים את GNBA המכפלה <KatexInline math="\mathcal{G} = \mathcal{A}_1 \times \mathcal{A}_2" /> עם שני תנאי קבלה: <KatexInline math="\mathcal{F} = \{F_1 \times Q_2, Q_1 \times F_2\}" />.
<br/>
<strong>שלב 2:</strong> משכפלים לשני עותקים של המכפלה. מעבר מראשון לשני בביקור ב־<KatexInline math="F_1 \times Q_2" />, ובחזרה לראשון בביקור ב־<KatexInline math="Q_1 \times F_2" />.
<br/>
<strong>שלב 3:</strong> מקבלים NBA שבו קבוצת הקבלה היא העותק הראשון של <KatexInline math="F_1 \times Q_2" />.
</div>
</div>

---

# דוגמה לחיתוך: אינסוף <span dir="ltr">a</span>-ים ואינסוף <span dir="ltr">b</span>-ים

<div class="grid grid-cols-2 gap-4 mt-3 text-right">
<div class="flex flex-col gap-4">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-[14px]">
<span class="font-bold text-blue-700">האוטומט <KatexInline math="\mathcal{A}_1" /> (אינסוף <KatexInline math="a" />-ים):</span>
<div class="flex justify-center mt-1 bg-white rounded border border-slate-100 p-1">
<AutomatonD3 variant="classic" :width="320" :height="100" :arrowSize="4" :stateLabelFontSize="13" :transitionLabelFontSize="11"
:states="[
  { id: 'q0', x: 80, y: 30, label: '$q_0$', initial: true, initialDirection: 'left', r: 18, labelWidth: 30 },
  { id: 'q1', x: 220, y: 30, label: '$q_1$', accepting: true, r: 18, labelWidth: 50 }
]"
:transitions="[
  { source: 'q0', target: 'q0', label: '$b$', loopDirection: '90deg', labelY: 8, labelWidth: 30 },
  { source: 'q0', target: 'q1', label: '$a$', labelY: -10, labelWidth: 30, curve: -0.15 },
  { source: 'q1', target: 'q1', label: '$a$', loopDirection: '90deg', labelY: 8, labelWidth: 30 },
  { source: 'q1', target: 'q0', label: '$b$', labelY: 12, labelWidth: 30, curve: -0.15 }
]"
/>
</div>
</div>

<div class="bg-red-50 border border-red-200 rounded p-3 text-[14px]">
<span class="font-bold text-red-700">האוטומט <KatexInline math="\mathcal{A}_2" /> (אינסוף <KatexInline math="b" />-ים):</span>
<div class="flex justify-center mt-1 bg-white rounded border border-slate-100 p-1">
<AutomatonD3 variant="classic" :width="320" :height="100" :arrowSize="4" :stateLabelFontSize="13" :transitionLabelFontSize="11"
:states="[
  { id: 'p0', x: 80, y: 30, label: '$p_0$', initial: true, initialDirection: 'left', r: 18, labelWidth: 30 },
  { id: 'p1', x: 220, y: 30, label: '$p_1$', accepting: true, r: 18, labelWidth: 50 }
]"
:transitions="[
  { source: 'p0', target: 'p0', label: '$a$', loopDirection: '90deg', labelY: 8, labelWidth: 30 },
  { source: 'p0', target: 'p1', label: '$b$', labelY: -10, labelWidth: 30, curve: -0.15 },
  { source: 'p1', target: 'p1', label: '$b$', loopDirection: '90deg', labelY: 8, labelWidth: 30 },
  { source: 'p1', target: 'p0', label: '$a$', labelY: 12, labelWidth: 30, curve: -0.15 }
]"
/>
</div>
</div>
</div>

<div class="bg-purple-50 border border-purple-200 rounded p-4 text-[14px] flex flex-col justify-between">
<div>
<span class="font-bold text-purple-700">GNBA המכפלה <KatexInline math="\mathcal{G} = \mathcal{A}_1 \times \mathcal{A}_2" />:</span>
<div class="text-[12px] text-gray-600 mt-1">
מצבי המכפלה ותנאי הקבלה (שים לב ש־<KatexInline math="\langle q_1,p_1\rangle" /> אינו נגיש).
</div>
</div>
<div class="flex justify-center mt-2 bg-white rounded border border-slate-100 p-1">
<AutomatonD3 variant="classic" :width="400" :height="220" :arrowSize="4" :stateLabelFontSize="12" :transitionLabelFontSize="11"
:states="[
  { id: 's00', x: 90,  y: 60, label: '$⟨q_0,p_0⟩$', initial: true, initialDirection: 'left', r: 24, labelWidth: 80 },
  { id: 's10', x: 290, y: 60, label: '$⟨q_1,p_0⟩$', accepting: true, r: 24, labelWidth: 80, stroke: '#2563eb' },
  { id: 's01', x: 90,  y: 180, label: '$⟨q_0,p_1⟩$', accepting: true, r: 24, labelWidth: 80, stroke: '#dc2626' },
  { id: 's11', x: 290, y: 180, label: '$⟨q_1,p_1⟩$', accepting: true, r: 24, labelWidth: 80, stroke: '#2563eb', innerStroke: '#dc2626' }
]"
:transitions="[
  { source: 's00', target: 's10', label: '$a$', labelY: -10, labelWidth: 30 },
  { source: 's00', target: 's01', label: '$b$', labelX: -12, labelWidth: 30 },
  { source: 's10', target: 's10', label: '$a$', loopDirection: '0deg', labelX: 8, labelWidth: 30 },
  { source: 's10', target: 's01', label: '$b$', labelX: -12, labelWidth: 30, curve: 0.2 },
  { source: 's01', target: 's01', label: '$b$', loopDirection: '180deg', labelX: -8, labelWidth: 30 },
  { source: 's01', target: 's10', label: '$a$', labelY: -15, labelWidth: 30, curve: 0.2 },
  { source: 's11', target: 's10', label: '$a$', labelX: 12, labelWidth: 30 },
  { source: 's11', target: 's01', label: '$b$', labelY: 12, labelWidth: 30 }
]"
/>
</div>
<div class="mt-2 text-[12px] text-gray-700 leading-tight">
<strong>קבוצות הקבלה:</strong>
<ul class="list-disc list-inside mr-1 mt-1">
<li>קבוצה ראשונה (כחול): <KatexInline math="F_1 \times Q_2 = \{\langle q_1, p_0\rangle, \langle q_1, p_1\rangle\}" /></li>
<li>קבוצה שנייה (אדום): <KatexInline math="Q_1 \times F_2 = \{\langle q_0, p_1\rangle, \langle q_1, p_1\rangle\}" /></li>
</ul>
המצב <KatexInline math="\langle q_1, p_1\rangle" /> (מוקף בכחול ואדום) שייך לשתי הקבוצות. 
<br/>
ריצה מקבלת חייבת לבקר בשתיהן אינסוף פעמים.
</div>
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
