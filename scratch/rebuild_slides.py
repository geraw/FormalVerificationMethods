import os

file_path = '19-ltl-to-generalized-buchi-automata.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We want to replace lines 592 to 678 (1-indexed, so 591 to 677 in 0-indexed)
# Let's verify what those lines are:
start_idx = 591
end_idx = 678 # exclusive, so lines[591:678]

print("Replacing from line", start_idx+1, "to", end_idx)
print("Start line content:", repr(lines[start_idx]))
print("End line content:", repr(lines[end_idx-1]))

new_slides = """---

# דוגמה: מצבי האוטומט עבור <span dir="ltr"><KatexInline math="a\\mathbin{\\mathrm{U}}b" /></span>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="$slidev.nav.clicks === 0 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c3', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\\\neg a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c7', x: 175, y: 285, label: '$\\\\neg a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c8', x: 345, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : $slidev.nav.clicks === 1 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c3', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\\\neg a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c7', x: 175, y: 285, label: '$\\\\neg a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c8', x: 345, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : $slidev.nav.clicks === 2 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.3 },
    { id: 'c3', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\\\neg a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.3 },
    { id: 'c7', x: 175, y: 285, label: '$\\\\neg a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c8', x: 345, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c3', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c5', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c6', x: 430, y: 175, label: '$\\\\neg a,b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c7', x: 175, y: 285, label: '$\\\\neg a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c8', x: 345, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' }
  ]"
  :transitions="[]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
בודקים את 8 המצבים המועמדים מול כללי העקביות של Until.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-red-50 border border-red-200 rounded p-3 text-red-900" dir="rtl">
<b>כלל 1 נפרץ:</b> <span dir="ltr">$b \\in B \\Rightarrow a\\mathbin{\\mathrm{U}}b \\in B$</span><br/>
המצבים <span dir="ltr">$\\{a,b,\\neg(a\\mathbin{\\mathrm{U}}b)\\}$</span> ו-<span dir="ltr">$\\{\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)\\}$</span> מכילים את $b$ אך לא את ההבטחה, ולכן נפסלים.
</div>
<div v-show="$slidev.nav.clicks === 2" class="bg-red-50 border border-red-200 rounded p-3 text-red-900" dir="rtl">
<b>כלל 2 נפרץ:</b> <span dir="ltr">$a\\mathbin{\\mathrm{U}}b \\in B \\Rightarrow a \\in B \\lor b \\in B$</span><br/>
המצב <span dir="ltr">$\\{\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b\\}$</span> מכיל את ההבטחה למרות שגם $a$ וגם $b$ שקריים, ולכן נפסל.
</div>
<div v-show="$slidev.nav.clicks === 3" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
נשארים עם 5 מצבים עקביים שיהוו את מצבי האוטומט.
</div>
</div>
</div>

---

# דוגמה: מעברים ממצב הבטחה פתוחה

<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, opacity: 0.8 },
    { id: 'q_wait', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_b', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_no', x: 90, y: 285, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, opacity: 0.8 },
    { id: 'q_dead', x: 430, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.8 }
  ]"
  :transitions="$slidev.nav.clicks === 0 ? [
    { source: 'q_wait', target: 'q_wait', label: '$\\\\{a\\\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\\\{a,b\\\\}$', labelY: -12, labelWidth: 75, curve: 0.15 },
    { source: 'q_wait', target: 'q_b', label: '$\\\\{b\\\\}$', labelY: -8, labelWidth: 60, curve: 0 },
    { source: 'q_wait', target: 'q_no', label: '$\\\\{a\\\\}$', labelY: 10, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נשברת' },
    { source: 'q_wait', target: 'q_dead', label: '$\\\\emptyset$', labelY: 10, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נשברת' }
  ] : [
    { source: 'q_wait', target: 'q_wait', label: '$\\\\{a\\\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\\\{a,b\\\\}$', labelY: -12, labelWidth: 75, curve: 0.15 },
    { source: 'q_wait', target: 'q_b', label: '$\\\\{b\\\\}$', labelY: -8, labelWidth: 60, curve: 0 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצב <span dir="ltr">$q_{\\text{wait}}$</span>, מאחר שהבטחת ה-Until פתוחה (<span dir="ltr">$a\\mathbin{\\mathrm{U}}b \\in B$</span>) ואינה מתממשת כעת (<span dir="ltr">$b \\notin B$</span>), <b>היא חייבת לעבור למצב הבא:</b> <span dir="ltr">$a\\mathbin{\\mathrm{U}}b \\in B'$</span>.<br/>
לכן מעברים למצבים שאינם מכילים את ההבטחה (הקווים המקווקווים באדום) <b>נפסלים</b>.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
אנו משאירים רק את המעברים התקינים למצבים שמכילים את ההבטחה (<span dir="ltr">$q_{\\text{wait}}, q_{\\text{both}}, q_{\\text{b}}$</span>).
</div>
</div>
</div>

---

# דוגמה: מעברים ממצב ללא הבטחה

<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, opacity: 0.8 },
    { id: 'q_wait', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_b', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_no', x: 90, y: 285, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_dead', x: 430, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.8 }
  ]"
  :transitions="$slidev.nav.clicks === 0 ? [
    { source: 'q_no', target: 'q_no', label: '$\\\\{a\\\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '$\\\\emptyset$', labelY: -10, labelWidth: 60, curve: 0 },
    { source: 'q_no', target: 'q_both', label: '$\\\\{a,b\\\\}$', labelY: 10, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין' },
    { source: 'q_no', target: 'q_wait', label: '$\\\\{a\\\\}$', labelY: -10, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין' },
    { source: 'q_no', target: 'q_b', label: '$\\\\{b\\\\}$', labelY: 10, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין' }
  ] : [
    { source: 'q_no', target: 'q_no', label: '$\\\\{a\\\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '$\\\\emptyset$', labelY: -10, labelWidth: 60, curve: 0 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצב <span dir="ltr">$q_{\\text{no}}$</span>, מאחר שההבטחה אינה מתקיימת (<span dir="ltr">$a\\mathbin{\\mathrm{U}}b \\notin B$</span>) אך התנאי השמאלי מתקיים (<span dir="ltr">$a \\in B$</span>), <b>ההבטחה לא יכולה להיווצר סתם כך במצב הבא:</b> <span dir="ltr">$a\\mathbin{\\mathrm{U}}b \\notin B'$</span>.<br/>
לכן מעברים למצבים שמכילים את ההבטחה (באדום מקווקו) <b>נפסלים</b>.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
נשארים רק המעברים התקינים למצבים שלא מכילים את ההבטחה (<span dir="ltr">$q_{\\text{no}}, q_{\\text{dead}}$</span>).
</div>
</div>
</div>

---

# דוגמה: מעברים ממצבים ללא הגבלה

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_wait', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30 },
    { id: 'q_b', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_no', x: 90, y: 285, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30 },
    { id: 'q_dead', x: 430, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 'q_both', target: 'q_wait', label: '$\\\\{a\\\\}$', labelY: 8, labelWidth: 65, curve: 0 },
    { source: 'q_both', target: 'q_b', label: '$\\\\{b\\\\}$', labelY: 12, labelWidth: 60, curve: -0.18 },
    { source: 'q_b', target: 'q_dead', label: '$\\\\emptyset$', labelY: 16, labelWidth: 80, curve: 0 },
    { source: 'q_b', target: 'q_both', label: '$\\\\{a,b\\\\}$', labelY: -14, labelWidth: 80, curve: 0.15 },
    { source: 'q_dead', target: 'q_dead', label: '$\\\\emptyset$', loopDirection: '90deg', labelY: 10, labelWidth: 80 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצבים אלו (המסומנים בצהוב), כללי ה-Until אינם מגבילים את המצב הבא:
<ul>
<li>במצבים <span dir="ltr">$q_{\\text{both}}$</span> ו-<span dir="ltr">$q_{\\text{b}}$</span> התנאי הימני $b$ מתקיים, ולכן ההבטחה מומשה ואין המשכיות כפויה.</li>
<li>במצב <span dir="ltr">$q_{\\text{dead}}$</span> התנאי השמאלי $a$ שקרי, ולכן אין דרישה למנוע יצירת הבטחה.</li>
</ul>
המעברים האפשריים מהם נקבעים אך ורק לפי התאמת האות הנקראת למצב היעד.
</div>
</div>
</div>

---

# דוגמה: תנאי הקבלה של האוטומט עבור <span dir="ltr"><KatexInline math="a\\\\mathbin{\\mathrm{U}}b" /></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 65, label: '$a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, initial: true, initialDirection: 'left', accepting: true },
    { id: 'q_wait', x: 430, y: 65, label: '$a,\\\\neg b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'right', accepting: false, stroke: '#dc2626' },
    { id: 'q_b', x: 260, y: 175, label: '$\\\\neg a,b,a\\\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'bottom', accepting: true },
    { id: 'q_no', x: 90, y: 285, label: '$a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, accepting: true },
    { id: 'q_dead', x: 430, y: 285, label: '$\\\\neg a,\\\\neg b,\\\\neg(a\\\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, accepting: true }
  ]"
  :transitions="[
    { source: 'q_wait', target: 'q_wait', label: '$\\\\{a\\\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\\\{a,b\\\\}$', labelY: -12, labelWidth: 75, curve: 0.15 },
    { source: 'q_wait', target: 'q_b', label: '$\\\\{b\\\\}$', labelY: -8, labelWidth: 60, curve: 0 },
    { source: 'q_both', target: 'q_wait', label: '$\\\\{a\\\\}$', labelY: 8, labelWidth: 65, curve: 0 },
    { source: 'q_both', target: 'q_b', label: '$\\\\{b\\\\}$', labelY: 12, labelWidth: 60, curve: -0.18 },
    { source: 'q_no', target: 'q_no', label: '$\\\\{a\\\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_dead', target: 'q_dead', label: '$\\\\emptyset$', loopDirection: '90deg', labelY: 10, labelWidth: 80 },
    { source: 'q_b', target: 'q_dead', label: '$\\\\emptyset$', labelY: 16, labelWidth: 80, curve: 0 },
    { source: 'q_b', target: 'q_both', label: '$\\\\{a,b\\\\}$', labelY: -14, labelWidth: 80, curve: 0.15 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
קבוצת הקבלה עבור הבטחת ה-Until היא:
<div dir="ltr" class="text-center my-1"><KatexInline math="F_{a\\mathbin{\\mathrm{U}}b} = \\{B \\mid a\\mathbin{\\mathrm{U}}b \\notin B \\lor b \\in B\\}" /></div>
המצבים שמקיימים זאת הם אלו שבהם <b>אין הבטחה פתוחה שטרם מומשה</b>:<br/>
<ul>
<li><span dir="ltr">$q_{\\text{both}}, q_{\\text{b}}$</span> (ההבטחה $a\\mathrm{U}b$ מתממשת כעת כי $b$ נכון)</li>
<li><span dir="ltr">$q_{\\text{no}}, q_{\\text{dead}}$</span> (ההבטחה $a\\mathrm{U}b$ שקרית)</li>
</ul>
רק המצב <span dir="ltr">$q_{\\text{wait}}$</span> אינו מקבל (מסומן באדום), כי בו ההבטחה פתוחה וממתינה למימוש.
</div>
</div>
</div>"""

# Replace the range
lines[start_idx:end_idx] = [new_slides]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Replacement complete successfully!")
