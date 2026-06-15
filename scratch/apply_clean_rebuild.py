import os

file_path = '19-ltl-to-generalized-buchi-automata.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "דוגמה: מצבי האוטומט עבור"
end_marker = "# נכונות הבנייה: הכיוון האינטואיטיבי"

start_pos = content.find(start_marker)
sep_pos = content.rfind("---\n", 0, start_pos)
if sep_pos == -1:
    sep_pos = content.rfind("---\r\n", 0, start_pos)

end_pos = content.find(end_marker)
sep_end_pos = content.rfind("---\n", 0, end_pos)
if sep_end_pos == -1:
    sep_end_pos = content.rfind("---\r\n", 0, end_pos)

if sep_pos == -1 or sep_end_pos == -1:
    print("Error: Could not locate slide markers!")
    print("sep_pos:", sep_pos, "sep_end_pos:", sep_end_pos)
    exit(1)

# We use raw string r"""...""" to write the backslashes EXACTLY as they should appear in the markdown file
new_slides_raw = r"""---

# דוגמה: מצבי האוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<span v-click class="hidden"></span>
<span v-click class="hidden"></span>
<span v-click class="hidden"></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="$slidev.nav.clicks === 0 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : $slidev.nav.clicks === 1 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : $slidev.nav.clicks === 2 ? [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.3 },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.3 },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b' },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#f8fafc', stroke: '#cbd5e1' }
  ] : [
    { id: 'c1', x: 90, y: 65, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c2', x: 260, y: 65, label: '$a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c3', x: 430, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c4', x: 90, y: 175, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c5', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' },
    { id: 'c6', x: 430, y: 175, label: '$\\neg a,b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c7', x: 175, y: 285, label: '$\\neg a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 154, labelHeight: 30, fill: '#fee2e2', stroke: '#dc2626', textColor: '#991b1b', opacity: 0.2 },
    { id: 'c8', x: 345, y: 285, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, fill: '#dcfce7', stroke: '#16a34a', textColor: '#15803d' }
  ]"
  :transitions="[]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
בודקים את 8 המצבים המועמדים מול כללי העקביות של Until.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-red-50 border border-red-200 rounded p-3 text-red-900" dir="rtl">
<b>כלל 1 נפרץ:</b> <span dir="ltr"><KatexInline math="b \in B \Rightarrow a\mathbin{\mathrm{U}}b \in B" /></span><br/>
המצבים <span dir="ltr"><KatexInline math="\{a,b,\neg(a\mathbin{\mathrm{U}}b)\}" /></span> ו-<span dir="ltr"><KatexInline math="\{\neg a,b,\neg(a\mathbin{\mathrm{U}}b)\}" /></span> מכילים את <span dir="ltr"><KatexInline math="b" /></span> אך לא את ההבטחה, ולכן נפסלים.
</div>
<div v-show="$slidev.nav.clicks === 2" class="bg-red-50 border border-red-200 rounded p-3 text-red-900" dir="rtl">
<b>כלל 2 נפרץ:</b> <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b \in B \Rightarrow a \in B \lor b \in B" /></span><br/>
המצב <span dir="ltr"><KatexInline math="\{\neg a,\neg b,a\mathbin{\mathrm{U}}b\}" /></span> מכיל את ההבטחה למרות שגם <span dir="ltr"><KatexInline math="a" /></span> וגם <span dir="ltr"><KatexInline math="b" /></span> שקריים, ולכן נפסל.
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
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, opacity: 0.8 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, opacity: 0.8 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.8 }
  ]"
  :transitions="$slidev.nav.clicks === 0 ? [
    { source: 'q_wait', target: 'q_wait', label: '$\\{a\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\{a\\}$', labelY: -12, labelWidth: 75, curve: 0 },
    { source: 'q_wait', target: 'q_b', label: '$\\{a\\}$', labelY: -8, labelWidth: 60, curve: 0 },
    { source: 'q_wait', target: 'q_no', label: '$\\{a\\}$', labelY: 14, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נשברת', curve: -0.3 },
    { source: 'q_wait', target: 'q_dead', label: '$\\{a\\}$', labelX: 14, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נשברת', curve: 0 }
  ] : [
    { source: 'q_wait', target: 'q_wait', label: '$\\{a\\}$', loopDirection: '-90deg', labelY: -10, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '$\\{a\\}$', labelY: -12, labelWidth: 75, curve: 0 },
    { source: 'q_wait', target: 'q_b', label: '$\\{a\\}$', labelY: -8, labelWidth: 60, curve: 0 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצב הבטחה פתוחה (שבו <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span> ו-<span dir="rtl"><KatexInline math="b \notin B" /></span>), מאחר שהבטחת ה-Until פתוחה (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span>) ואינה מתממשת כעת (<span dir="rtl"><KatexInline math="b \notin B" /></span>), <b>היא חייבת לעבור למצב הבא:</b> <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B'" /></span>.<br/>
לכן מעברים למצבים שאינם מכילים את ההבטחה (הקווים המקווקווים באדום) <b>נפסלים</b>.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
משאירים רק את המעברים התקינים למצבים שבהם ההבטחה מתקיימת (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \in B'" /></span>).
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
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, opacity: 0.8 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, opacity: 0.8 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.8 }
  ]"
  :transitions="$slidev.nav.clicks === 0 ? [
    { source: 'q_no', target: 'q_no', label: '$\\{a\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '$\\{a\\}$', labelY: -10, labelWidth: 60, curve: 0 },
    { source: 'q_no', target: 'q_both', label: '$\\{a\\}$', labelX: -12, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין', curve: 0 },
    { source: 'q_no', target: 'q_wait', label: '$\\{a\\}$', labelY: 14, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין', curve: 0.25 },
    { source: 'q_no', target: 'q_b', label: '$\\{a\\}$', labelY: -14, labelWidth: 60, stroke: '#ef4444', dasharray: '4,4', tooltip: 'נפסל: הבטחה נוצרת יש מאין', curve: 0 }
  ] : [
    { source: 'q_no', target: 'q_no', label: '$\\{a\\}$', loopDirection: '90deg', labelY: 10, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '$\\{a\\}$', labelY: -10, labelWidth: 60, curve: 0 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div v-show="$slidev.nav.clicks === 0" class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצב ללא הבטחה (שבו <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span> אך <span dir="rtl"><KatexInline math="a \in B" /></span>), מאחר שההבטחה אינה מתקיימת (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span>) אך התנאי השמאלי מתקיים (<span dir="rtl"><KatexInline math="a \in B" /></span>), <b>ההבטחה לא יכולה להיווצר סתם כך במצב הבא:</b> <span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B'" /></span>.<br/>
לכן מעברים למצבים שמכילים את ההבטחה (באדום מקווקו) <b>נפסלים</b>.
</div>
<div v-show="$slidev.nav.clicks === 1" class="bg-emerald-50 border border-emerald-200 rounded p-3 text-emerald-900" dir="rtl">
נשארים רק המעברים התקינים למצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B'" /></span>).
</div>
</div>
</div>

---

# דוגמה: מעברים ממצבים ללא הגבלה

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, stroke: '#eab308', strokeWidth: 3 }
  ]"
  :transitions="[
    { source: 'q_both', target: 'q_both', label: '$\\{a,b\\}$', loopDirection: '180deg', labelX: -22, labelWidth: 70 },
    { source: 'q_both', target: 'q_wait', label: '$\\{a,b\\}$', labelY: -10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_b', label: '$\\{a,b\\}$', labelY: 12, labelWidth: 70, curve: 0.18 },
    { source: 'q_both', target: 'q_no', label: '$\\{a,b\\}$', labelY: 10, labelWidth: 70, curve: 0 },
    { source: 'q_both', target: 'q_dead', label: '$\\{a,b\\}$', labelY: -18, labelWidth: 70, curve: -0.55 },
    { source: 'q_b', target: 'q_b', label: '$\\{b\\}$', loopDirection: '45deg', labelY: -22, labelX: 20, labelWidth: 60 },
    { source: 'q_b', target: 'q_both', label: '$\\{b\\}$', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_wait', label: '$\\{b\\}$', labelX: 8, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_dead', label: '$\\{b\\}$', labelY: 12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_no', label: '$\\{b\\}$', labelX: -8, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_dead', label: '$\\emptyset$', loopDirection: '0deg', labelX: 22, labelWidth: 60 },
    { source: 'q_dead', target: 'q_wait', label: '$\\emptyset$', labelY: -10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_b', label: '$\\emptyset$', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_no', label: '$\\emptyset$', labelY: 10, labelWidth: 60, curve: 0 },
    { source: 'q_dead', target: 'q_both', label: '$\\emptyset$', labelY: 18, labelWidth: 60, curve: -0.55 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
ממצבים אלו (המסומנים בצהוב), כללי ה-Until אינם מגבילים את המצב הבא:
<ul>
<li>במצבים שבהם התנאי הימני <span dir="rtl"><KatexInline math="b \in B" /></span> מתקיים, ולכן ההבטחה מומשה ואין המשכיות כפויה.</li>
<li>במצבים שבהם התנאי השמאלי <span dir="rtl"><KatexInline math="a \notin B" /></span> שקרי, ולכן אין דרישה למנוע יצירת הבטחה.</li>
</ul>
המעברים האפשריים מהם נקבעים אך ורק לפי התאמת האות הנקראת למצב היעד.
</div>
</div>
</div>

---

# דוגמה: מצבי ההתחלה של האוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, initial: true, initialDirection: 'bottom', stroke: '#16a34a', strokeWidth: 3 },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', stroke: '#16a34a', strokeWidth: 3 },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', stroke: '#16a34a', strokeWidth: 3 },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, opacity: 0.4 },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, opacity: 0.4 }
  ]"
  :transitions="[]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
מצב התחלה הוא מצב שבו הנוסחה <b>מתקיימת</b> במצב ההתחלתי:<br/>
<div dir="ltr" class="text-center my-1"><KatexInline math="Q_0 = \{B \in Q \mid \varphi \in B\}" /></div>
<ul>
<li><b>שלושה מצבים</b> מכילים <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b \in B" /></span> ולכן הם מצבי התחלה אפשריים (ירוק).</li>
<li><b>שני המצבים הנותרים</b> מכילים <span dir="ltr"><KatexInline math="\neg(a\mathbin{\mathrm{U}}b) \in B" /></span> — הנוסחה שקרית שם, ולכן <b>אינם</b> מצבי התחלה.</li>
</ul>
</div>
</div>
</div>

---



# דוגמה: תנאי הקבלה של האוטומט עבור <span dir="ltr"><KatexInline math="a\mathbin{\mathrm{U}}b" /></span>

<div class="grid grid-cols-[1.1fr_0.9fr] gap-5 mt-2 items-start">
<div class="bg-white rounded border border-slate-200 shadow-sm p-2">
<AutomatonD3 variant="classic" :width="500" :height="360" :arrowSize="4" :stateLabelFontSize="10.5" :transitionLabelFontSize="11"
  :states="[
    { id: 'q_both', x: 90, y: 175, label: '$a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 132, labelHeight: 30, initial: true, initialDirection: 'bottom', accepting: true },
    { id: 'q_wait', x: 260, y: 65, label: '$a,\\neg b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', accepting: false, stroke: '#dc2626' },
    { id: 'q_b', x: 260, y: 175, label: '$\\neg a,b,a\\mathbin{\\mathrm{U}}b$', r: 36, labelWidth: 142, labelHeight: 30, initial: true, initialDirection: 'left', accepting: true },
    { id: 'q_no', x: 260, y: 285, label: '$a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 164, labelHeight: 30, accepting: true },
    { id: 'q_dead', x: 430, y: 175, label: '$\\neg a,\\neg b,\\neg(a\\mathbin{\\mathrm{U}}b)$', r: 36, labelWidth: 176, labelHeight: 30, accepting: true }
  ]"
  :transitions="[
    { source: 'q_wait', target: 'q_wait', label: '', loopDirection: '-90deg', labelY: -22, labelWidth: 70 },
    { source: 'q_wait', target: 'q_both', label: '', labelY: -12, labelWidth: 75, curve: 0.15 },
    { source: 'q_wait', target: 'q_b', label: '', labelX: -12, labelWidth: 60, curve: 0.15 },
    { source: 'q_no', target: 'q_no', label: '', loopDirection: '90deg', labelY: 22, labelWidth: 65 },
    { source: 'q_no', target: 'q_dead', label: '', labelY: 12, labelWidth: 60, curve: 0.15 },
    { source: 'q_both', target: 'q_both', label: '', loopDirection: '180deg', labelX: -22, labelWidth: 70 },
    { source: 'q_both', target: 'q_wait', label: '', labelY: 12, labelWidth: 70, curve: 0.15 },
    { source: 'q_both', target: 'q_b', label: '', labelY: 12, labelWidth: 70, curve: 0.18 },
    { source: 'q_both', target: 'q_no', label: '', labelY: 10, labelWidth: 70, curve: 0.10 },
    { source: 'q_both', target: 'q_dead', label: '', labelY: -18, labelWidth: 70, curve: -0.95 },
    { source: 'q_b', target: 'q_b', label: '', loopDirection: '45deg', labelY: -22, labelX: 20, labelWidth: 60 },
    { source: 'q_b', target: 'q_both', label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_wait', label: '', labelX: 12, labelWidth: 60, curve: 0.15 },
    { source: 'q_b', target: 'q_dead', label: '', labelY: 12, labelWidth: 60, curve: 0.18 },
    { source: 'q_b', target: 'q_no', label: '', labelX: -12, labelWidth: 60, curve: 0.15 },
    { source: 'q_dead', target: 'q_dead', label: '', loopDirection: '0deg', labelX: 22, labelWidth: 60 },
    { source: 'q_dead', target: 'q_wait', label: '', labelY: -10, labelWidth: 60, curve: 0.10 },
    { source: 'q_dead', target: 'q_b', label: '', labelY: -12, labelWidth: 60, curve: 0.18 },
    { source: 'q_dead', target: 'q_no', label: '', labelY: -12, labelWidth: 60, curve: 0.15 },
    { source: 'q_dead', target: 'q_both', label: '', labelY: 18, labelWidth: 60, curve: -0.95 }
  ]"
/>
</div>

<div class="mt-3 text-right text-[17px] leading-relaxed">
<div class="bg-blue-50 border border-blue-200 rounded p-3 text-blue-900" dir="rtl">
קבוצת הקבלה עבור הבטחת ה-Until היא:
<div dir="ltr" class="text-center my-1"><KatexInline math="F_{a\mathbin{\mathrm{U}}b} = \{B \mid a\mathbin{\mathrm{U}}b \notin B \lor b \in B\}" /></div>
המצבים שמקיימים זאת הם אלו שבהם <b>אין הבטחה פתוחה שטרם מומשה</b>:<br/>
<ul>
<li>המצבים שבהם <span dir="rtl"><KatexInline math="b \in B" /></span> (ולכן ההבטחה מתממשת כעת)</li>
<li>המצבים שבהם ההבטחה שקרית (<span dir="rtl"><KatexInline math="a\mathbin{\mathrm{U}}b \notin B" /></span>)</li>
</ul>
רק המצב שבו ההבטחה פתוחה וממתינה למימוש (מסומן באדום) אינו מקבל.
</div>
</div>
</div>"""

# Replace the region in content
new_content = content[:sep_pos] + new_slides_raw + content[sep_end_pos:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Slide content replaced completely and cleanly via raw string!")
