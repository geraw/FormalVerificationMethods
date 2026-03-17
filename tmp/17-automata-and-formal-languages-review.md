---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 17-automata-and-formal-languages-review
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
חזרה על נושאים
באוטומטים ושפות פורמאליות
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ראשי פרקים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
3
</div>
</div>
<div class="ppt-text-layer" style="left:3.7500%;top:21.1111%;width:92.5000%;height:73.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת זמן ליניארי 𝑃𝑠𝑎𝑓𝑒 היא תכונת בטיחות אם לכל 𝜎𝑃𝑠𝑎𝑓𝑒 קיימת רישא סופית 𝜌 כך ש:
𝑃 𝑠𝑎𝑓𝑒 ∩ 𝜎 ′ ∈ 2 𝐴𝑃 𝜔 :𝜌∈𝑝𝑟𝑒𝑓 𝜎 ′ =∅
• הקבוצה 𝑏𝑝 של &quot;רישות רעות&quot; של 𝑃𝑠𝑎𝑓𝑒:
𝑏𝑝 𝑃 𝑠𝑎𝑓𝑒 = 2 𝐴𝑃 ∗ ∖𝑝𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 )
• הקבוצה 𝑚𝑏𝑝 של &quot;רישות רעות מינימאליות&quot; של 𝑃𝑠𝑎𝑓𝑒:
𝑚𝑏𝑝 𝑃 𝑠𝑎𝑓𝑒 = 𝜌∈ 2 𝐴𝑃 ∗ : 𝑝𝑟𝑒𝑓 𝜌 ∩𝑏𝑝 𝑃 𝑠𝑎𝑓𝑒 = 𝜌
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:89.7539%;width:93.7575%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#a0a0a0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
רישא רעה מינימאלית איננה בהכרח הרישא הרעה הקצרה ביותר – זאת רישא רעה שאין לה רישא אחרת שהיא רישא רעה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: תכונות בטיחות לרמזור
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
4
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:16.6667%;width:92.5000%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נניח 𝐴𝑃={𝑟𝑒𝑑, 𝑔𝑟𝑒𝑒𝑛, 𝑦𝑒𝑙𝑙𝑜𝑤}. מתאר איזה פנס דולק ברמזור.
• &quot;תמיד אחד הפנסים דולק&quot;
  • הגדרה: { 𝑞 = 𝐴0 𝐴1  : 𝐴𝑗⊆ 𝐴𝑃∧ 𝐴𝑗  ∅ }
  • רישות רעות: מילים סופיות המכילות את ∅
  • רישא רעה מינימאלית: המופע הראשון של האות ∅ הוא בסוף המילה
• &quot;אף פעם לא מדליקים שני פנסים ביחד&quot;
  • הגדרה: { 𝑞 = 𝐴0 𝐴1  : 𝐴𝑗⊆𝐴𝑃∧ 𝐴𝑗 ≤1 }
  • רישות רעות: מילים סופיות המכילות אותיות כמו {𝑟𝑒𝑑, 𝑔𝑟𝑒𝑒𝑛}, {𝑟𝑒𝑑, 𝑦𝑒𝑙𝑙𝑜𝑤}, …
  • רישא רעה מינימאלית: מילה בה המופע הראשון של אחת האותיות האלו הוא בסוף
• &quot;אור אדום חייב להידלק אחרי אור צהוב&quot;
  • הגדרה: { 𝑞 = 𝐴0 𝐴1  : 𝑟𝑒𝑑∈ 𝐴𝑖⇒(𝑖&gt;0∧𝑦𝑒𝑙𝑙𝑜𝑤∈ 𝐴 𝑖−1 )}
  • רישא רעה שאינה מינימאלית: {𝑦𝑒𝑙𝑙𝑜𝑤}{𝑦𝑒𝑙𝑙𝑜𝑤}{𝑟𝑒𝑑}{𝑟𝑒𝑑};{𝑟𝑒𝑑}
  • רישות רעות מינימאליות:∅∅{𝑟𝑒𝑑} וגם ∅{𝑟𝑒𝑑}
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות בטיחות רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
5
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:23.7072%;width:92.5000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הגדרה:
תכונת בטיחות 𝑃𝑠𝑎𝑓𝑒 היא רגולרית אם 𝑏𝑝(𝑃𝑠𝑎𝑓𝑒) היא שפה רגולרית
במילים אחרות:
אם קיים אוטומט סופי מעל האלפבית 2𝐴𝑃 המקבל את 𝑏𝑝(𝑃𝑠𝑎𝑓𝑒)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ראשי פרקים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
6
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט סופי לא דטרמיניסטי (אסל&quot;ד)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
7
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:23.3333%;width:91.6667%;height:70.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט סופי לא דטרמיניסטי (אסל&quot;ד NFA,) הוא :hQ, §, ±, Q0, Fi
• 𝑄 היא קבוצת מצבים סופית
• Σהוא האלפבית
• ±: Q £ §  2Q היא פונקציית מעברים
• Q0 µ Q היא קבוצת מצבים התחלתיים
• F µ Q היא קבוצת מצבים מקבלים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לאוטומט
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
8
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:23.6111%;width:25.9426%;height:33.6589%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑄 = {𝑞0, 𝑞1, 𝑞2}
𝛿 = { 𝐴, 𝐵 }
𝑄0 = {𝑞0}
𝐹 = {𝑞2}
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:67.7778%;width:30.0000%;height:24.5934%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝛿(𝑞0,𝐴)= 𝑞 0
𝛿(𝑞1,𝐴)= 𝑞 2
𝛿(𝑞2,𝐴)= 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:52.5000%;top:67.7778%;width:29.9865%;height:24.5934%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝛿(𝑞0,𝐵)= {𝑞0, 𝑞1}
𝛿(𝑞1,𝐵)= 𝑞 2
𝛿(𝑞2,𝐵)= 𝑞 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת מקורס &quot;אוטומטים ושפות פורמאליות&quot; -שפה של אוטומט
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
9
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:22.2222%;width:85.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• אסל&quot;ד A=hQ,§, ±, Q0,Fi ומילה w = A1  An 2 §*
• ריצה של w ב A היא רצף מצבים q0 q1 ... qn כך ש:
  q0 2 Q0 ו לכל 0 · i &lt; n
• ריצה q0 q1 ... qn היא מקבלת אם qn2 F
• w 2 §* מתקבלת ע&quot;י A אם יש ריצה מקבלת של w ב A
• השפה המתקבלת ע&quot;י A:
g יש ריצה מקבלת שלw ב A L(A) = f w 2 §* :
• אסל&quot;ד A ו A’ הם שקולים אם L(A) = L(A’)
</div>
</div>
<div class="ppt-text-layer" style="left:42.5000%;top:40.8408%;width:12.5000%;height:7.2619%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 𝑖 𝐴 𝑖+1 𝑞 𝑖+1
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: ריצות ומילים מתקבלות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
10
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:28.8889%;width:85.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
• ריצות האוטומט:
  • q0 - עבור המילה הריקה ²
  • q0q1 - עבור המילה B
  • q0q0q0q0 - עבור המילים ABA ו BBA, לדוגמה
• ריצות מקבלות הן כאלה המסתיימות במצב מקבל:
  • q0q1q2 - עבור המילים BA ו BB
  • q0q0q1q2 - עבור המילים ABB, ABA,BBA,BBB
• המילים האלה שייכות ל L(A)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מילים מקבלות מזווית אחרת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
11
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:21.1111%;width:90.8333%;height:33.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מרחיבים את פונקצית המעברים ± ל- ±*: Q £ §*  2Q ע&quot;י
±*(q, ²) = fqg ו ±*(q, A) = ±(q, A)
±*(q, A1 A2 An) = p2±(q, A1) ±*(p, A2 An)
</div>
</div>
<div class="ppt-text-layer" style="left:10.3466%;top:58.8238%;width:80.4867%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
±*(q, w) = המצבים שהאוטומט יכול להגיע בסוף קריאת המילה w
</div>
</div>
<div class="ppt-text-layer" style="left:15.8274%;top:86.6667%;width:66.6726%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
שפה היא רגולרית אם ורק אם קיים אסל&quot;ד המקבל אותה
</div>
</div>
<div class="ppt-text-layer" style="left:7.3420%;top:72.6346%;width:85.9914%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
L(A) = fw2§* : ±*(q0, w) Å F  ; for some q0 2 Q0g
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
12
</div>
</div>
<div class="ppt-text-layer" style="left:27.8307%;top:66.6667%;width:44.3385%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
±*(q0, ABBA) = fq0, q2g
</div>
</div>
<div class="ppt-text-layer" style="left:26.0689%;top:80.0000%;width:47.8622%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
±*(q0, ABB) = fq0, q1, q2 g
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט מַכְפֵּלָה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
13
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:21.1111%;width:95.0000%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• עבור שני אס&quot;ד Ai = hQi,§, ±i, Q0,i,Fii (i=1, 2)
• אוטומט המכפלה:
𝒜1×𝒜2 = h Q1£Q2, §, ±, Q0,1£Q0,2, F1£F2 i
כאשר ± מוגדרת ע&quot;י:
• תוצאה ידועה: ℒ 𝐴 1 × 𝐴 2 =ℒ 𝐴 1 ∩ℒ 𝐴 2
</div>
</div>
<div class="ppt-text-layer" style="left:35.8333%;top:56.9923%;width:30.4073%;height:15.8524%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;border:2.25px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 𝐴 1 𝑞 1 ′ ∧ 𝑞 2 𝐴 2 𝑞 2 ′ 𝑞 1 , 𝑞 2 𝐴 𝑞 1 ′ , 𝑞 2 ′
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט דטרמיניסטי ואוטומט מָלֵא
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
14
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:21.1111%;width:86.6667%;height:57.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט A נקרא דטרמיניסטי (אס&quot;ד, DFA) אם
jQ0j = 1 וגם j±(q,A)j · 1 לכל q 2 Q ולכל A 2 §
אס&quot;ד A נקרא שלם (total) אם
jQ0j = 1 וגם j±(q,A)j = 1 לכל q 2 Q ולכל A 2 §
</div>
</div>
<div class="ppt-text-layer" style="left:7.6993%;top:80.0000%;width:87.3938%;height:13.9123%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אפשר להפוך כל אס&quot;ד לאוטומט שלם שקול (איך?)
באוטומט דטרמיניסטי עוקב יחיד ולכן ריצה יחידה לכל מילת קלט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הפיכת אסל&quot;ד לאס&quot;ד באמצעות דטרמינציה
</div>
</div>
<div class="ppt-text-layer" style="left:77.0833%;top:98.7755%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
15
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:22.2222%;width:93.3333%;height:46.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לאסל&quot;ד A=hQ,§, ±, Q0,Fi נגדיר אס&quot;ד Adet=h 2Q, §, ±det, {Q0}, Fdeti ע&quot;י
Fdet = f Q’ µ Q : Q’ Å F  ; g
ופונקצית מעברים שלמה ±det: 2Q £ §  2Q מוגדרת ע&quot;י:
±det(Q’, A) = q 2 Q’ ±(q, A)
</div>
</div>
<div class="ppt-text-layer" style="left:15.0000%;top:73.4638%;width:68.7237%;height:20.9807%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
Adet הוא אס&quot;ד שלם (למה?)
ולכל w2§* מתקיים ±det*(Q0, w) = q0 2 Q0 ±*(q0, w) (למה?)
לכן: L(Adet) = L(A)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: דטרמינציה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
16
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/17-automata-and-formal-languages-review/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיכום עובדות לגבי אוטומטים סופיים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
17
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:18.8889%;width:91.6667%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• יכולים לבטא את כל השפות הרגולריות ורק אותן
• סגורים תחת חיתוך והשלמה (complementation)
  • אוטומט המכפלה A £ B מקבל את השפה L(A) \ L(B)
  • באוטומט דטרמיניסטי שלם מקבלים §* n L(A) ע&quot;י החלפת המצבים המקבלים עם אלה שאינם מקבלים
• סגורים תחת דטרמינציה (הורדת הבחירה)
  • במחיר הגדלה אֶקְסְפּוֹנֶנְצְיָאלִית של מספר המצבים באוטומט
• בדיקת רֵיקוּת השפה ℒ 𝐴 =∅ ?
  • בדיקה אם יש מצב מקבל נגיש באמצעות חיפוש DFS פשוט
• לשפה רגולרית ℒ יש אוטומט דטרמיניסטי מינימאלי יחיד המקבל את ℒ
</div>
</div>
</div>

<style>
.slidev-layout.full {
  padding: 0;
}
.ppt-slide-canvas {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: white;
}
.ppt-slide-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: fill;
}
.ppt-text-layer, .ppt-table-layer {
  position: absolute;
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.ppt-table {
  width: 100%;
  height: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  background: transparent;
}
.ppt-table-cell {
  border: 1px solid #444;
  padding: 4px 6px;
  font-family: 'Gisha','Segoe UI','Arial',sans-serif;
  font-size: 16pt;
  white-space: pre-wrap;
  text-align: right;
  vertical-align: top;
}
</style>
