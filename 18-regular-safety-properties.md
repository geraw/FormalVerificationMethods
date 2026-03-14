---
theme: default
defaults:
  layout: full
lineNumbers: false
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בדיקת תכונות בטיחות רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:87.3772%;top:-0.8058%;width:11.4335%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Aharoni','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
585
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: תכונות בטיחות רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:23.3333%;width:97.5000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 היא רגולרית
⇕
𝑏𝑎𝑑𝑃𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 ) היא שפה רגולרית
⇕
קיים אוטומט סופי דטרמיניסטי 𝒜 כך ש-
ℒ(𝒜)=𝑏𝑎𝑑𝑃𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:5.8333%;top:5.5556%;width:88.3333%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מספיק להתייחס לרישות רעות מינימאליות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
3
</div>
</div>
<div class="ppt-text-layer" style="left:16.6667%;top:38.8889%;width:67.5000%;height:33.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 היא רגולרית
אם ורק אם
𝑚𝑖𝑛𝐵𝑎𝑑𝑃𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 ) היא שפה רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:57.5000%;top:82.2222%;width:31.6667%;height:8.9333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#534733;white-space:pre-wrap;width:100%;">
הרישות הרעות שאף רישא שלהן איננה רישא רעה
</div>
</div>
<div class="ppt-text-layer" style="left:4.7234%;top:83.8889%;width:15.5532%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו טענה זאת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחת הטענה מהשקף הקודם
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
4
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:28.8889%;width:94.1667%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מאוטומט המקבל את הרישות הרעות המינימאליות לאוטומט המקבל את כל הרישות הרעות:
  נוסיף לכל מצב מקבל מעבר עצמי מעל כל אות באלף-בית 2 𝐴𝑃
מאוטומט המקבל את כל הרישות הרעות לאוטומט המקבל את הרישות הרעות המינימאליות:
  נוריד את כל המעברים היוצאים ממצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:67.3913%;top:52.1716%;width:2.7032%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
2 𝐴𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:31.5524%;top:84.7490%;width:5.5958%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
×
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:17.9051%;width:95.0000%;height:6.6669%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 היא רגולרית אם ורק אם 𝑚𝑖𝑛𝐵𝑎𝑑𝑃𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 ) היא שפה רגולרית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות בטיחות רגולריות לדוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
5
</div>
</div>
<div class="ppt-text-layer" style="left:6.1896%;top:21.9727%;width:92.2917%;height:80.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• כל תכונת שמורה היא תכונת בטיחות רגולרית
  • הרישות הרעות המינימאליות הן מהצורה Φ ∗ ¬Φ
• דוגמה לתכונת בטיחות רגולרית שאינה שמורה:
  • אור אדום יכול להידלק רק לאחר שהאור הצהוב היה דולק בפרק הזמן הקודם.
• דוגמה לתכונת בטיחות שאינה רגולרית:
  • &quot;מספר המטבעות שהוכנסו לא קטן ממספר המשקאות שניתנו&quot;
  • ניתן להראות, ע&quot;פ לֶמַת הניפוח, שקבוצת הרישות הרעות איננה שפה רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:44.8335%;width:29.0625%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אין לנו עדיין אלגוריתם
לתכונות שאינן שמורה
</div>
</div>
<div class="ppt-text-layer" style="left:1.8703%;top:27.2265%;width:29.0625%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#92d050;opacity:1.000;transform:rotate(353.59deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
  ראינו אלגוריתמים לבדיקת תכונות שמורה
</div>
</div>
<div class="ppt-text-layer" style="left:2.0579%;top:65.2342%;width:29.0625%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#c00000;opacity:1.000;transform:rotate(9.90deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
לא נתאר אלגוריתם לתכונות שאינן רגולריות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
6
</div>
</div>
<div class="ppt-table-layer" style="left:53.3333%;top:33.3333%;width:45.0000%;height:53.3333%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
while (true) {
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
…
</td>
</tr>
<tr>
<td class="ppt-table-cell">
rq:
</td>
<td class="ppt-table-cell">
𝑏 2 ,𝑥 ≔〈𝑡𝑟𝑢𝑒,1〉;
</td>
</tr>
<tr>
<td class="ppt-table-cell">
wt:
</td>
<td class="ppt-table-cell">
wait until (𝑥=2∨¬𝑏1);
</td>
</tr>
<tr>
<td class="ppt-table-cell">
cs:
</td>
<td class="ppt-table-cell">
accessAccount;
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
𝑏2≔𝑓𝑎𝑙𝑠𝑒;
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
…
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
}
</td>
</tr>
</table>
</div>
<div class="ppt-table-layer" style="left:3.3333%;top:33.3333%;width:47.5510%;height:53.3333%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
while (true) {
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
…
</td>
</tr>
<tr>
<td class="ppt-table-cell">
rq:
</td>
<td class="ppt-table-cell">
〈𝑏1, 𝑥〉 := 〈𝑡𝑟𝑢𝑒, 2〉;
</td>
</tr>
<tr>
<td class="ppt-table-cell">
wt:
</td>
<td class="ppt-table-cell">
wait until (𝑥=1∨¬𝑏2);
</td>
</tr>
<tr>
<td class="ppt-table-cell">
cs:
</td>
<td class="ppt-table-cell">
accessAccount;
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
𝑏1 :=𝑓𝑎𝑙𝑠𝑒;
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
…
</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">
}
</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:69.3526%;top:25.7257%;width:25.8086%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
התנהגות התהליך השני:
</div>
</div>
<div class="ppt-text-layer" style="left:20.9248%;top:25.7257%;width:28.4032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
התנהגות התהליך הראשון:
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: האלגוריתם של פטרסון
</div>
</div>
<div class="ppt-text-layer" style="left:26.7768%;top:87.7778%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 𝐺 1
</div>
</div>
<div class="ppt-text-layer" style="left:74.2768%;top:87.7778%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 𝐺 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-007.png" alt="" />
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
<div class="ppt-text-layer" style="left:4.1667%;top:1.1111%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
האם המערכת אמינה?
</div>
</div>
<div class="ppt-text-layer" style="left:1.3486%;top:79.8090%;width:97.3051%;height:15.4971%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
האם אנחנו יכולים להבטיח שלא יכנסו שני תהליכים לקטע הקריטי?
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : ∀ 𝑖 . 𝜎 𝑖 ⊨¬ 𝑐𝑟𝑖𝑡1 ∧ 𝑐𝑟𝑖𝑡2
</div>
</div>
<div class="ppt-text-layer" style="left:1.3486%;top:22.3924%;width:28.6514%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 𝑃𝑒𝑡 = 𝑇𝑆 𝑃 𝐺 1 ∥𝑃 𝐺 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
האם המערכת אמינה?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
8
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:21.1111%;width:97.5000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אמינה = בכל זמן, לכל היותר משתמש אחד מחזיק גישה לחשבון
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : ∀ 𝑖 . 𝜎 𝑖 ⊨¬ 𝑐𝑟𝑖 𝑡 1 ∧ 𝑐𝑟𝑖 𝑡 2
לא אמינה = יכול להיות ששניים יחזיקו גישה לחשבון ביחד
𝐵𝑎𝑑𝑃𝑟𝑒𝑓 𝑃 = 𝜌∈ 2 𝐴𝑃 ∗ :∃𝑖. 𝜌 𝑖 ⊨𝑐𝑟𝑖 𝑡 1 ∧ 𝑐𝑟𝑖 𝑡 2
רישא רעה מינימאלית = עוצרים בפעם הראשונה שיש תקלה
</div>
</div>
<div class="ppt-text-layer" style="left:47.5000%;top:80.7370%;width:15.9999%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖 𝑡 1 ∧𝑐𝑟𝑖 𝑡 2
</div>
</div>
<div class="ppt-text-layer" style="left:18.3333%;top:73.1098%;width:19.9969%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬(𝑐𝑟𝑖 𝑡 1 ∧𝑐𝑟𝑖 𝑡 2 )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: דוגמת הרמזור
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
9
</div>
</div>
<div class="ppt-text-layer" style="left:1.3861%;top:26.5460%;width:98.6139%;height:14.0414%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
  &quot;אסור שאור אדום יידלק אם לא דלק אור צהוב בדיוק בצעד הקודם.&quot;
    𝜎∈ 2 𝐴𝑃 𝜔 : ∀ 𝑖≥0 𝑟𝑒𝑑∈𝜎 𝑖 ⇒ 𝑖&gt;0 ∧ 𝑦𝑒𝑙𝑙𝑜𝑤∈𝜎 𝑖−1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:47.4991%;width:79.1667%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
קבוצת הרישות הרעות המינימאליות עבור התכונה היא השפה המתקבלת על ידי האוטומט:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
כתיבה מפורשת של האותיות (קבוצות)
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
<div class="ppt-text-layer" style="left:5.2234%;top:19.7664%;width:86.3049%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
  &quot;אסור שאור אדום יידלק בלי שאור צהוב דלק צעד אחד לפני&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:32.0920%;width:15.1376%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
דרכים שונות לכתוב את אותו האוטומט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת תכונת בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
11
</div>
</div>
<div class="ppt-text-layer" style="left:11.2790%;top:29.9349%;width:81.6087%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
נרצה לבדוק אם אחת הריצות של מערכת המעברים מכילה רישא רעה:
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:72.1571%;width:87.8877%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ביטוי המורכב מחיתוך, השלמה ורֵיקוּת של שפות רגולריות...
</div>
</div>
<div class="ppt-text-layer" style="left:14.5833%;top:51.5624%;width:75.8333%;height:8.1324%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠 𝑓𝑖𝑛 𝑇 𝑆 𝑃𝑒𝑡 ∩𝐵𝑎𝑑𝑃𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 ) =∅ ?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ניסוח הבעיה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
12
</div>
</div>
<div class="ppt-text-layer" style="left:1.4583%;top:19.5805%;width:96.6667%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בהנתן:
  𝑃 safe : תכונת בטיחות רגולרית מעל 𝐴𝑃 שאיננה 2 𝐴𝑃 𝜔
  𝒜 : אוטומט סופי המקבל את הרישות הרעות של 𝑃 safe
  𝑇𝑆 : מערכת מעברים סופית בלי מצבים סופיים מעל 𝐴𝑃
שאלה:
איך נכריע אם 𝑇𝑆⊨ 𝑃 safe ?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:2.2222%;width:85.0000%;height:11.1111%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
רדוקציה לבדיקת שמורה
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
<div class="ppt-text-layer" style="left:15.0000%;top:26.8027%;width:36.6667%;height:21.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c6b7b8;opacity:1.000;border:0.75px solid #948182;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#742217;white-space:pre-wrap;width:100%;">
An automaton 𝒜 such that
ℒ 𝒜 =𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃)
</div>
</div>
<div class="ppt-text-layer" style="left:2.1769%;top:73.3333%;width:44.1667%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#704a3d;white-space:pre-wrap;width:100%;">
A transition system 𝑇 𝑆 ′
and an invariant 𝜙 such that
𝑇 𝑆 ′ ⊨ 𝜎:∀𝑖. 𝜎 𝑖 ⊨𝜙 ⇔𝑇𝑆⊨𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:64.1667%;top:27.5057%;width:27.5000%;height:21.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c6b7b8;opacity:1.000;border:0.75px solid #948182;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#742217;white-space:pre-wrap;width:100%;">
A transition system
𝑇𝑆
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-014.png" alt="" />
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
<div class="ppt-text-layer" style="left:8.5456%;top:2.9158%;width:85.0000%;height:11.1111%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:34.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
רעיון האלגוריתם לבדיקת תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:11.0739%;top:37.1545%;width:35.8333%;height:21.7344%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#0000ff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
נוסיף למערכת רכיב שיזהה אם נצפתה
רישא רעה
</div>
</div>
<div class="ppt-text-layer" style="left:10.7818%;top:59.4609%;width:35.8333%;height:28.2734%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#0000ff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
ונבדוק את תכונת השמורה &quot;אף פעם לא נצפית רישא רעה&quot; על המערכת החדשה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
15
</div>
</div>
<div class="ppt-text-layer" style="left:8.5456%;top:2.9158%;width:85.0000%;height:11.1111%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: רדוקציה לבדיקת שְׁמוּרָה
</div>
</div>
<div class="ppt-text-layer" style="left:2.2693%;top:16.0516%;width:95.4614%;height:81.9238%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נאמר, שבהינתן תכונת מצב 𝜙 נרצה לבדוק אם מערכת המעברים
𝑇𝑆= 𝑆, 𝐴𝑐𝑡, →, 𝐼, 𝐴𝑃, 𝐿
מקיימת את תכונת הבטיחות:
𝑃= 𝜎: ∀𝑖. 𝜎 𝑖 ⊨𝜙 ∨ 𝜎 𝑖+1 ⊨𝜙 ∨ 𝜎 𝑖+2 ⊨𝜙
נבנה מערכת מעברים:
𝑇 𝑆 # = 𝑆×{0,1,2,3} , 𝐴𝑐𝑡, → # , 𝐼 # , {𝑏𝑎𝑑}, 𝐿 #
לפי הכללים:
𝑠 𝛼 𝑡 ∧ 𝑖∈ 0,1,2 ∧ 𝐿 𝑡 ⊭𝜙 𝑠,𝑖 𝛼 # 〈𝑡,𝑖+1〉 𝑠 𝛼 𝑡 ∧ 𝑖∈ 0,1,2 ∧ 𝐿 𝑡 ⊨𝜙 𝑠,𝑖 𝛼 # 〈𝑡,0〉 𝑠 𝛼 𝑡 𝑠,3 𝛼 # 𝑡,3
באשר:
𝐼 # = 𝑠,1 :𝑠∈𝐼∧𝐿 𝑠 ⊭𝜙 ∪ 𝑠,0 :𝑠∈𝐼∧𝐿 𝑠 ⊨𝜙
ו-
𝐿 # 𝑠,𝑖 = 𝑏𝑎𝑑 , 𝑖=3 , 𝑖≠3
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:89.9349%;width:17.8084%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
נסו את הבניה על מערכת כלשהי
</div>
</div>
<div class="ppt-text-layer" style="left:11.5212%;top:49.5333%;width:12.5743%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#5d3619;white-space:pre-wrap;width:100%;">
מוסיפים למכונה מונה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-016.png" alt="" />
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
<div class="ppt-text-layer" style="left:8.5456%;top:2.9158%;width:85.0000%;height:11.1111%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:37.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המשך דוגמה: רדוקציה לבדיקת שְׁמוּרָה
</div>
</div>
<div class="ppt-text-layer" style="left:24.1667%;top:60.8795%;width:54.9796%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#002060;white-space:pre-wrap;width:100%;">
על המערכת שקיבלנו נוכל לבדוק את תכונת השמורה
𝑃 𝑖𝑛𝑣 = 𝜎: ∀𝑖 . 𝜎 𝑖 ⊨¬𝑏𝑎𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:23.5557%;top:81.5490%;width:54.9796%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑇𝑆⊨𝑃 ⇔ 𝑇 𝑆 # ⊨ 𝑃 𝑖𝑛𝑣
</div>
</div>
<div class="ppt-text-layer" style="left:2.2693%;top:16.0516%;width:95.4614%;height:38.5955%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נאמר, שבהינתן תכונת מצב𝜙 נרצה לבדוק אם מערכת המעברים
𝑇𝑆= 𝑆, 𝐴𝑐𝑡, →, 𝐼, 𝐴𝑃, 𝐿
מקיימת את תכונת הבטיחות:
𝑃= 𝜎: ∀𝑖. 𝜎 𝑖 ⊨𝜙 ∨ 𝜎 𝑖+1 ⊨𝜙 ∨ 𝜎 𝑖+2 ⊨𝜙
נבנה מערכת מעברים:
𝑇 𝑆 # = 𝑆×{0,1,2,3} , 𝐴𝑐𝑡, → # , 𝐼 # , {𝑏𝑎𝑑}, 𝐿 #
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:53.3749%;top:53.9392%;width:34.3285%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
הרכבה של אוטומט עם
מערכת מעברים שתוגדר בשקף הבא
</div>
</div>
<div class="ppt-text-layer" style="left:5.9086%;top:26.2496%;width:91.6666%;height:27.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆⊨ 𝑃safe ⇔ 𝑇𝑟𝑎𝑐𝑒𝑠fin 𝑇𝑆 ∩𝑏𝑎𝑑𝑃𝑟𝑒𝑓(𝑃safe)=∅
⇔ 𝑇𝑟𝑎𝑐𝑒𝑠fin 𝑇𝑆 ∩ℒ(𝒜)=∅
⇔ מצב נגיש בו האוטומט נמצא במצב מקבל 𝑇𝑆×𝒜אין ב
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
רעיון בסיסי לאלגוריתם
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
17
</div>
</div>
<div class="ppt-text-layer" style="left:5.4823%;top:66.6667%;width:89.0353%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מסקנה: בדיקת תכונת בטיחות רגולרית שקולה לבדיקת שמורה על 𝑇𝑆×𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:6.2154%;top:79.6584%;width:87.5691%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
משמעות: ניתן לבדוק תכונות בטיחות רגולרית ע&quot;י אלגוריתמים לבדיקת שמורה
(DFS או BFS קדימה או אחורה)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
18
</div>
</div>
<div class="ppt-text-layer" style="left:60.8919%;top:24.6997%;width:27.3829%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#704a3d;white-space:pre-wrap;width:100%;">
A transition system 𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:6.1674%;top:22.4991%;width:33.1301%;height:11.6684%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#742217;white-space:pre-wrap;width:100%;">
An automaton 𝒜 such that
ℒ 𝒜 =𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃)
</div>
</div>
<div class="ppt-text-layer" style="left:2.7084%;top:80.5299%;width:71.6667%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
A transition system 𝑇𝑆×𝒜 and an invariant 𝑃 𝑖𝑛𝑣 such that
𝑇𝑆×𝒜⊨ 𝑃 𝑖𝑛𝑣 ⇔ 𝑇𝑆⊨𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:8.5456%;top:2.9158%;width:85.0000%;height:11.1111%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
רדוקציה לבדיקת שְׁמוּרָה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
רעיון הבניה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
19
</div>
</div>
<div class="ppt-text-layer" style="left:63.3333%;top:24.4444%;width:19.4512%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
מערכת המעברים מייצרת עקבות
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:50.0000%;width:23.6179%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט עוקב אחר העקבות שנוצרות
</div>
</div>
<div class="ppt-text-layer" style="left:38.3333%;top:47.7778%;width:22.9167%;height:5.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#e1e0e0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆×𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:30.5624%;top:68.7500%;width:37.7225%;height:16.0945%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑠 𝛼 𝑡 ∧ 𝑝∈𝛿 𝑞,𝐿 𝑡 𝑠,𝑞 𝛼 × 〈𝑡,𝑝〉
</div>
</div>
<div class="ppt-text-layer" style="left:14.7212%;top:68.7500%;width:16.5110%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#633737;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
קיים מעבר במערכת
המעברים המקורית
</div>
</div>
<div class="ppt-text-layer" style="left:67.6151%;top:68.7500%;width:18.0099%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#633737;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
קיים מעבר באוטומט
הקורא את התיוג של 𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:25.8333%;top:86.0577%;width:47.0541%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#633737;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מערכת המעברים החדשה מתקדמת בשני הרכיבים,
זה שמייצג את מערכת המעברים המקורית וזה שעוקב אחר האוטומט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:6.6667%;top:1.2458%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מערכת מעברים הנוצרת
מֵהַרְכָּבַת אוטומט עם מערכת מעברים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:103.3333%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
20
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:22.2222%;width:96.6667%;height:80.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור מערכת מעברים 𝑇𝑆= 𝑆, 𝐴𝑐𝑡, →, 𝐼, 𝐴𝑃, 𝐿 ואוטומט
𝒜= 𝑄, 2 𝐴𝑃 , 𝛿, 𝑄 0 , 𝐹 המקיים 𝑄 0 ∩𝐹=∅ נגדיר מערכת מעברים:
𝑇𝑆×𝒜 = 𝑆×𝑄, 𝐴𝑐𝑡, → × , 𝐼 × , 𝐴 𝑃 × , 𝐿 ×
באשר 𝐴 𝑃 × =𝑄 , 𝐿 × 𝑠,𝑞 = 𝑞 , יחס המעברים → × מוגדר ע&quot;י
𝑠 𝛼 𝑡 ∧ 𝑝∈𝛿 𝑞,𝐿 𝑡 𝑠,𝑞 𝛼 × 〈𝑡,𝑝〉
וקבוצת המצבים ההתחלתיים 𝐼 × מוגדרת ע&quot;י
𝐼 × = 𝑠 0 ,𝑞 : 𝑠 0 ∈𝐼 ∧ ∃ 𝑞 0 ∈ Q 0 . 𝑞∈𝛿 𝑞 0 ,𝐿 𝑠 0
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
21
</div>
</div>
<div class="ppt-text-layer" style="left:7.0140%;top:7.4114%;width:43.1667%;height:37.7989%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑆 = {0, 1, 2}
𝐴𝑐𝑡 = {𝑡𝑖𝑐𝑘}
→ = { 𝑖, 𝑡𝑖𝑐𝑘, 𝑖+1 mod 3⟩ :𝑖∈𝑆
𝐼 = {0}
𝐴𝑃 = {𝑋}
𝐿 0 = 𝐿 1 ={}
𝐿(2)= {𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:6.9933%;top:53.1541%;width:33.0973%;height:34.3199%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑄 = { 𝑞 0 , 𝑞 1 , 𝑞 2 , 𝑞 3 }
Σ = 2 𝐴𝑃 = {}, 𝑋
𝛿 𝑞 𝑖 , = 𝑞 min 𝑖+1, 3
𝛿 𝑞 𝑖 , 𝑋 = {𝑞 max 0, 𝑖−2 ⋅3 }
𝑄 0 = { 𝑞 0 }
𝐹 ={ 𝑞 3 }
</div>
</div>
<div class="ppt-text-layer" style="left:83.8184%;top:35.0980%;width:8.4763%;height:4.5127%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#336600;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
0, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:83.8184%;top:45.5694%;width:8.4763%;height:4.5127%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#336600;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:83.8184%;top:56.0407%;width:8.4763%;height:4.5127%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#336600;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
2, 𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:54.5803%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
0
</div>
</div>
<div class="ppt-text-layer" style="left:61.1198%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:67.6593%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:55.8832%;top:23.5169%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:62.6208%;top:23.5169%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:69.3584%;top:23.8769%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:45.6083%;top:-6.1111%;width:44.9376%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:45.0655%;top:2.7295%;width:10.2303%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:36.1959%;top:47.4121%;width:7.6368%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:63.6258%;top:38.9719%;width:20.0881%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆×𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:46.0829%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:2.25px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:52.6225%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:2.25px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:59.1620%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:2.25px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:65.7015%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:4.75px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:49.1851%;top:64.0140%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:55.9219%;top:63.8803%;width:2.9004%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:69.7375%;top:75.1534%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑋 , {}
</div>
</div>
<div class="ppt-text-layer" style="left:62.5370%;top:64.0407%;width:2.9004%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:53.5650%;top:80.1600%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:48.5982%;top:74.7849%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:42.7524%;top:57.7936%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:49.2485%;top:56.3899%;width:24.4412%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#d34817;white-space:pre-wrap;width:100%;">
אוטומט לרישות הרעות
</div>
</div>
<div class="ppt-text-layer" style="left:19.7647%;top:90.1563%;width:62.9673%;height:6.6878%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= {}, 𝑋 𝜔 : ∀𝑖≥0 𝜎 𝑖 ⊨ 𝑋 ∨ 𝜎 𝑖+1 ⊨𝑋 ∨ 𝜎 𝑖+2 ⊨𝑋
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
22
</div>
</div>
<div class="ppt-text-layer" style="left:7.0140%;top:7.4114%;width:43.1667%;height:37.7989%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑆 = {0, 1, 2, 3}
𝐴𝑐𝑡 = {𝑡𝑖𝑐𝑘}
→ = { 𝑖, 𝑡𝑖𝑐𝑘, 𝑖+1 mod 4⟩ :𝑖∈𝑆
𝐼 = {0}
𝐴𝑃 = {𝑋}
𝐿 0 = 𝐿 1 =𝐿 2 ={}
𝐿(3)= {𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:6.9933%;top:53.1541%;width:33.0973%;height:34.3199%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑄 = { 𝑞 0 , 𝑞 1 , 𝑞 2 , 𝑞 3 }
Σ = 2 𝐴𝑃 = {}, 𝑋
𝛿 𝑞 𝑖 , = 𝑞 min 𝑖+1, 3
𝛿 𝑞 𝑖 , 𝑋 = {𝑞 max 0, 𝑖−2 ⋅3 }
𝑄 0 = { 𝑞 0 }
𝐹 ={ 𝑞 3 }
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:27.6102%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#336600;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
0, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:38.0815%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#336600;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:59.0242%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c00000;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
3, 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:48.5529%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c00000;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
2, 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:69.4955%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c00000;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
0, 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:79.9669%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c00000;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
1, 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:84.8511%;top:90.4381%;width:8.4763%;height:4.2091%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c00000;opacity:1.000;border:0.25px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
2, 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:54.5803%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
0
</div>
</div>
<div class="ppt-text-layer" style="left:61.1198%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:67.6593%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:74.1988%;top:19.1518%;width:3.6391%;height:5.0674%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
3
</div>
</div>
<div class="ppt-text-layer" style="left:55.8832%;top:23.5169%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:62.6208%;top:23.5169%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:69.3584%;top:23.5169%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:76.0960%;top:23.5169%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:45.6083%;top:-6.1111%;width:44.9376%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:45.0655%;top:2.7295%;width:10.2303%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:63.6258%;top:38.9719%;width:20.0881%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆×𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:36.1959%;top:47.4121%;width:7.6368%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:46.0829%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:2.25px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:52.6225%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:2.25px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:59.1620%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:2.25px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:65.7015%;top:66.7890%;width:3.8629%;height:5.2209%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:4.75px solid #581904;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:49.1851%;top:64.0140%;width:3.1050%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:55.9219%;top:63.8803%;width:2.9004%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:69.7375%;top:75.1534%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑋 , {}
</div>
</div>
<div class="ppt-text-layer" style="left:62.5370%;top:64.0407%;width:2.9004%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:53.5650%;top:80.1600%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:48.5982%;top:74.7849%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:42.7524%;top:57.7936%;width:6.3585%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑋}
</div>
</div>
<div class="ppt-text-layer" style="left:49.2485%;top:56.3899%;width:24.4412%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#d34817;white-space:pre-wrap;width:100%;">
אוטומט לרישות הרעות
</div>
</div>
<div class="ppt-text-layer" style="left:19.7647%;top:90.1563%;width:62.9673%;height:6.6878%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= {}, 𝑋 𝜔 : ∀𝑖≥0 𝜎 𝑖 ⊨ 𝑋 ∨ 𝜎 𝑖+1 ⊨𝑋 ∨ 𝜎 𝑖+2 ⊨𝑋
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
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
23
</div>
</div>
<div class="ppt-text-layer" style="left:28.2597%;top:24.8576%;width:5.7476%;height:6.9575%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:1.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:27.3931%;top:18.0477%;width:7.0432%;height:4.0146%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:73.1780%;top:25.6748%;width:4.1054%;height:4.9697%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:1.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:42.9588%;top:24.8576%;width:5.7476%;height:6.9575%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:1.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:34.5687%;top:24.7921%;width:5.5923%;height:4.0146%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:34.9614%;top:33.8484%;width:7.0432%;height:4.0146%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:50.2205%;top:24.7769%;width:5.5923%;height:4.0146%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:57.6579%;top:24.7047%;width:5.7476%;height:6.9575%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:1.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:64.2265%;top:24.3198%;width:5.5923%;height:4.0146%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:41.6114%;top:40.6981%;width:7.0432%;height:4.0146%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:64.6118%;top:74.8703%;width:13.1718%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑟𝑒𝑑,𝑔𝑟𝑒𝑒𝑛}
</div>
</div>
<div class="ppt-text-layer" style="left:28.2970%;top:74.2235%;width:13.1781%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑦𝑒𝑙𝑜𝑤,𝑟𝑒𝑑}
</div>
</div>
<div class="ppt-text-layer" style="left:46.4352%;top:74.5297%;width:15.9368%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑔𝑟𝑒𝑒𝑛,𝑦𝑒𝑙𝑙𝑜𝑤}
</div>
</div>
<div class="ppt-text-layer" style="left:38.3921%;top:67.6778%;width:5.7476%;height:6.9575%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#a0a0a0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1
</div>
</div>
<div class="ppt-text-layer" style="left:49.8503%;top:67.6778%;width:5.7476%;height:6.9575%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#a0a0a0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 2
</div>
</div>
<div class="ppt-text-layer" style="left:61.7381%;top:67.9142%;width:5.7476%;height:6.9575%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#a0a0a0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 3
</div>
</div>
<div class="ppt-text-layer" style="left:27.3931%;top:46.3666%;width:47.4064%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
אסור שהאור האדום יודלק שלוש פעמים ברצף
</div>
</div>
<div class="ppt-text-layer" style="left:24.9428%;top:87.1840%;width:52.8409%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
האם מערכת המעברים הזאת מקיימת את התכונה?
</div>
</div>
<div class="ppt-text-layer" style="left:71.9227%;top:17.9098%;width:6.4106%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
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
24
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:51.0451%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:60.6747%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:70.3044%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:79.9340%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:48.3696%;top:24.2059%;width:4.5264%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
×
</div>
</div>
<div class="ppt-text-layer" style="left:45.9438%;top:42.4925%;width:8.8039%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆×𝑄
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
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
25
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:51.0451%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:60.6747%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:70.3044%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:79.9340%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:37.8550%;top:2.4900%;width:25.9566%;height:11.1794%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑠 𝛼 𝑡 ∧ 𝑝∈𝛿 𝑞,𝐿 𝑡 𝑠,𝑞 𝛼 × 〈𝑡,𝑝〉
</div>
</div>
<div class="ppt-text-layer" style="left:48.3696%;top:24.2059%;width:4.5264%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
×
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
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
26
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:51.0451%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:60.6747%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:70.3044%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:79.9340%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:37.8550%;top:2.4900%;width:25.9566%;height:11.1794%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑠 𝛼 𝑡 ∧ 𝑝∈𝛿 𝑞,𝐿 𝑡 𝑠,𝑞 𝛼 × 〈𝑡,𝑝〉
</div>
</div>
<div class="ppt-text-layer" style="left:48.3696%;top:24.2059%;width:4.5264%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
×
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
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
27
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:33.1943%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:51.0451%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:60.6747%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:70.3044%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:47.4305%;top:79.9340%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:51.1111%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:60.7407%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:70.3704%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:80.0000%;width:8.3333%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ff7c68;opacity:1.000;border:0.75px solid #ff3100;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑠 3 , 𝑞 4
</div>
</div>
<div class="ppt-text-layer" style="left:37.8550%;top:2.4900%;width:25.9566%;height:11.1794%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑠 𝛼 𝑡 ∧ 𝑝∈𝛿 𝑞,𝐿 𝑡 𝑠,𝑞 𝛼 × 〈𝑡,𝑝〉
</div>
</div>
<div class="ppt-text-layer" style="left:48.3696%;top:24.2059%;width:4.5264%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
×
</div>
</div>
<div class="ppt-text-layer" style="left:23.5582%;top:50.1331%;width:10.7323%;height:16.1563%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(49.85deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:66.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">

</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
28
</div>
</div>
<div class="ppt-text-layer" style="left:7.6104%;top:43.3333%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:20.0000%;top:43.3333%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:45.0000%;top:43.3333%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:13.3333%;top:41.1111%;width:5.0000%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:16.6667%;top:48.8889%;width:3.6944%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:43.3333%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:25.7230%;top:41.6667%;width:5.0000%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:38.2230%;top:41.6667%;width:5.0000%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:20.3611%;top:58.4923%;width:3.6944%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:34.4444%;width:3.6944%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:43.3333%;top:34.4444%;width:6.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:11.7005%;top:82.2112%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 0
</div>
</div>
<div class="ppt-text-layer" style="left:30.9650%;top:82.2112%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠2
</div>
</div>
<div class="ppt-text-layer" style="left:21.3328%;top:66.6667%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:88.6735%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:29.8810%;top:73.3333%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑟}
</div>
</div>
<div class="ppt-text-layer" style="left:39.0476%;top:88.8889%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:21.1111%;width:79.1667%;height:6.4803%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃 refresh = 𝜎∈ 2 𝐴𝑃 𝜔 : ∀𝑖 . 𝑟∈𝜎 𝑖 ∪𝜎 𝑖+ 1 ∪𝜎 𝑖+ 2
</div>
</div>
<div class="ppt-text-layer" style="left:59.2005%;top:63.3223%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 0 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:80.5610%;top:63.4546%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 2 , 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:68.8700%;top:47.7778%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1 , 𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:69.7846%;width:7.1182%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:76.9728%;top:54.4444%;width:7.1763%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 }
</div>
</div>
<div class="ppt-text-layer" style="left:86.5476%;top:70.0000%;width:7.1182%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:72.0468%;top:78.4962%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 0 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:79.8746%;top:85.1738%;width:7.1763%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 2 }
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:5.1576%;top:0.5446%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה להרכבה של אוטומט ומערכת מעברים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
29
</div>
</div>
<div class="ppt-text-layer" style="left:14.6680%;top:28.5523%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:6.8196%;top:43.3223%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑦
</div>
</div>
<div class="ppt-text-layer" style="left:26.0840%;top:43.3223%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑟𝑦
</div>
</div>
<div class="ppt-text-layer" style="left:15.3816%;top:58.0924%;width:11.4160%;height:6.3300%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑔
</div>
</div>
<div class="ppt-text-layer" style="left:11.7380%;top:22.2222%;width:8.4105%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{𝑟𝑒𝑑}
</div>
</div>
<div class="ppt-text-layer" style="left:0.5646%;top:38.2308%;width:11.9629%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{𝑦𝑒𝑙𝑙𝑜𝑤}
</div>
</div>
<div class="ppt-text-layer" style="left:26.7975%;top:38.2088%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:16.8085%;top:52.8174%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:36.6667%;top:88.8889%;width:13.3333%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑦, 𝑞1
</div>
</div>
<div class="ppt-text-layer" style="left:36.6667%;top:70.5556%;width:13.3333%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑔, 𝑞0
</div>
</div>
<div class="ppt-text-layer" style="left:59.5833%;top:70.5556%;width:13.3333%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑟𝑦, 𝑞0
</div>
</div>
<div class="ppt-text-layer" style="left:59.5833%;top:88.8889%;width:13.3333%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠𝑟, 𝑞0
</div>
</div>
<div class="ppt-text-layer" style="left:49.2770%;top:36.6667%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:68.4437%;top:36.3265%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:89.6937%;top:36.1789%;width:5.8333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:50.8333%;top:27.6702%;width:20.2208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦𝑒𝑙𝑙𝑜𝑤∧¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:50.6126%;top:47.7778%;width:20.2208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
<div class="ppt-text-layer" style="left:41.3131%;top:46.0035%;width:11.1944%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
<div class="ppt-text-layer" style="left:77.2845%;top:34.4458%;width:12.3780%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:71.2288%;top:28.2864%;width:20.2208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬(𝑦𝑒𝑙𝑙𝑜𝑤∨𝑟𝑒𝑑)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
התכונה המרכזית של 𝑇𝑆×𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
30
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:22.2222%;width:92.5000%;height:71.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑠 0 , 𝑞 1 , 𝑠 1 , 𝑞 2 ,…,〈 𝑠 𝑛 , 𝑞 𝑛+1 〉
הוא מקטע מסלול התחלתי של המערכת 𝑇𝑆×𝒜
אם ורק אם
𝑠 0 , 𝑠 1 ,…, 𝑠 𝑛 הוא מקטע מסלול התחלתי של 𝑇𝑆
וקיים 𝑞 0 ∈ 𝑄 0 כך ש-
𝑞 0 𝐿( 𝑠 0 ) 𝑞 1 𝐿( 𝑠 1 ) 𝑞 2 𝐿( 𝑠 2 ) ⋯ 𝐿 𝑠 𝑛 𝑞 𝑛+1
היא ריצה של האוטומט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-031.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מצבים סופניים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
31
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:18.8889%;width:85.8333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• למרות שאין ל-𝑇𝑆 מצבים סופניים, ל 𝑇𝑆×𝒜 יכולים להיות
• זה יכול לקרות רק אם 𝛿 𝑞,𝐴 =∅ עבור 𝐴⊆𝐴𝑃 כלשהי
• נניח שקיבלנו אוטומט עם מצב נגיש 𝑞 כך ש 𝛿 𝑞,𝐴 =∅
• נבנה אוטומט שקול:
  • נמציא &quot;מצב מלכודת&quot; חדש 𝑞𝑡𝑟𝑎𝑝
  • בכל פעם ש 𝛿 𝑞,𝐴 =∅ נהפוך את המעבר להיות 𝛿’ 𝑞,𝐴 = 𝑞𝑡𝑟𝑎𝑝
  • נקבע 𝛿’ 𝑞𝑡𝑟𝑎𝑝,𝐴 = 𝑞𝑡𝑟𝑎𝑝
  • בשאר המקרים, פונקצית המעברים 𝛿’ זהה ל 𝛿
</div>
</div>
<div class="ppt-text-layer" style="left:3.7500%;top:85.5556%;width:91.2500%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מסקנה: אפשר להניח, בלי הגבלת הכלליות, שאין ל-𝑇𝑆×𝒜 מצבים סופניים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-032.png" alt="" />
<div class="ppt-text-layer" style="left:4.3333%;top:-1.1111%;width:94.7143%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אימות תכונות בטיחות רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:71.1111%;top:100.0000%;width:30.1786%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.3333%;top:2.2222%;width:5.5714%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
32
</div>
</div>
<div class="ppt-text-layer" style="left:1.3333%;top:20.7143%;width:98.3334%;height:74.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור:
  • מערכת מעברים סופית 𝑇𝑆 מעל 𝐴𝑃בלי מצבים ללא מוצא
  • תכונת בטיחות רגולרית 𝑃
  • אוטומט 𝒜=⟨Σ, 𝑄, 𝑄 0 ,𝐹,𝛿⟩ כך ש 𝑄 0 ∩𝐹=∅- ו- ℒ 𝒜 =𝑏𝑎𝑑𝑃𝑟𝑒𝑓 𝑃
האמירות הבאות שקולות:
  • 𝑇𝑆⊨𝑃
  • 𝑇𝑟𝑎𝑐𝑒 𝑠 fin (𝑇𝑆)∩ℒ 𝒜 =∅
  • 𝑇𝑆×𝒜⊨{𝜎∈ 2 𝑄 𝜔 : ∀𝑖 𝜎 𝑖 ∩𝐹=∅ }
</div>
</div>
<div class="ppt-text-layer" style="left:59.7343%;top:59.9646%;width:29.2442%;height:8.8791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
האם זה יעבוד גם אם האוטומט לא דטרמיניסטי?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-033.png" alt="" />
<div class="ppt-text-layer" style="left:6.6667%;top:22.2681%;width:55.8333%;height:5.5096%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
TS ² Psafe , Tracesfinite(TS) Å BadPref(Psafe) = ;
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
33
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:22.2222%;width:95.8333%;height:39.0443%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שקילות (1) ו (2) נובעת ישירות מ-
(1) ( (3) : TS 2 Psafe גורר TS £ A 2 Pinv(A)
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:46.6814%;width:90.8333%;height:37.6979%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם TS 2 Psafe אז קיים מקטע מסלול סופי ¼ = s0s1  sn של TS כך ש-
.trace(¼) = L(s0) L(s1)  L(sn) 2 L(A)
כיוון ש trace(¼) 2 L(A), קיימת ריצה מקבלת q0q1  qn+1 של A עבור trace(¼). בפרט hs0,q1ihs1,q2i hsn,qn+1i היא ריצה התחלתית של TS £ A עם
𝐿 𝑠 𝑛 , 𝑞 𝑛+1 = 𝑞 𝑛+1 ⊆𝐹
לכן 𝑇𝑆×𝒜⊭ 𝜎:∀𝑖. 𝜎 𝑖 ∩𝐹=∅
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחה (המשך)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
34
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:16.6667%;width:95.8333%;height:13.3139%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
(3) ( (2): 𝑇𝑆×𝒜⊭ 𝜎:∀𝑖. 𝜎 𝑖 ∩𝐹=∅ גורר tracesfin(TS) Å L(A)  ;
</div>
</div>
<div class="ppt-text-layer" style="left:1.9792%;top:32.2222%;width:95.8333%;height:57.6221%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אם 𝑇𝑆×𝒜⊭ 𝜎:∀𝑖. 𝜎 𝑖 ∩𝐹=∅ אז קיים מקטע מסלול התחלתי 𝑠 0 , 𝑞 1 , 𝑠 1 , 𝑞 2 ,…, 𝑠 𝑛 , 𝑞 𝑛+1 כך ש- 𝑞 𝑛+1 ∈𝐹 ולכל 𝑖 מתקיים 𝑞 𝑖 𝐿 𝑠 𝑖 𝑞 𝑖+1 ו- 𝑠 0 , 𝑠 1 ,…, 𝑠 𝑛
הוא מקטע מסלול התחלתי של 𝑇𝑆. בגלל ש 〈 𝑠 0 , 𝑞 1 〉 מצב התחלתי של 𝑇𝑆×𝒜, קיים מצב התחלתי 𝑞0 של 𝒜 כך ש- 𝑞 0 𝐿( 𝑠 0 ) 𝑞 1 ובפרט 𝑞 0 , 𝑞 1 ,…, 𝑞 𝑛+1 היא ריצה מקבלת עבור 𝑡𝑟𝑎𝑐𝑒 𝑠 0 , 𝑠 1 ,…, 𝑠 𝑛 קיבלנו:
𝑡𝑟𝑎𝑐𝑒 𝑠 𝑓𝑖𝑛 𝑇𝑆 ∩ℒ 𝒜 ≠∅
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
איך מייצרים דוגמאות נגדיות?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
35
</div>
</div>
<div class="ppt-text-layer" style="left:7.3148%;top:22.4691%;width:86.6667%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:30.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לכל מקטע ריצה התחלתי hs0, q1i  hsn, qn+1i
של TS £ A:
q1, …, qn  F and qn+1 2 F

trace(s0 s1  sn) 2 L(A)
</div>
</div>
<div class="ppt-text-layer" style="left:22.6858%;top:83.5035%;width:31.5762%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
רישא רעה מינימאלית של Psafe
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:7.0747%;top:-1.1111%;width:87.9253%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אלגוריתם אימות
</div>
</div>
<div class="ppt-text-layer" style="left:71.9846%;top:100.0000%;width:28.0154%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.4946%;top:2.2222%;width:5.1721%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
36
</div>
</div>
<div class="ppt-text-layer" style="left:0.9546%;top:21.1111%;width:96.5454%;height:65.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• קלט: מערכת מעברים סופית 𝑇𝑆 ותכונת בטיחות רגולרית 𝑃𝑠𝑎𝑓𝑒
• פלט: 𝑡𝑟𝑢𝑒 אם 𝑇𝑆⊨ 𝑃𝑠𝑎𝑓𝑒. אחרת, 𝑓𝑎𝑙𝑠𝑒 עם דוגמא נגדית
נבנה אוטומט 𝒜 (עם קבוצת מצבים מקבלים 𝐹) כך ש-ℒ(𝒜)=𝑏𝑎𝑑𝑃𝑟𝑒𝑓(𝑃𝑠𝑎𝑓𝑒)
נבדוק את השמורה 𝑃= 𝜎:∀𝑖. 𝜎 𝑖 ∩𝐹=∅ על 𝑇𝑆×𝒜
אם 𝑇𝑆×𝒜⊨𝑃 אז
נחזיר 𝑡𝑟𝑢𝑒
אחרת
נחזיר מקטע ריצה התחלתי של 𝑇𝑆×𝒜ש איננו מקיים את התכונה כדוגמה נגדית.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שיפור זמן הריצה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
37
</div>
</div>
<div class="ppt-text-layer" style="left:7.6538%;top:22.4274%;width:85.0000%;height:40.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת הבטיחות Psafe היא רגולרית
אם ורק אם
קבוצת הרישות הרעות המינימאליות של Psafe היא רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:80.0000%;width:99.3848%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
נשתמש באוטומט לרישות הרעות המינימאליות בבניית המכפלה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/18-regular-safety-properties/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סִבּוּכִיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
38
</div>
</div>
<div class="ppt-text-layer" style="left:3.7355%;top:29.8249%;width:92.5290%;height:34.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
סִבּוּכִיּוּת זמן ומקום לבדיקה אם𝑇𝑆⊨ 𝑃 𝑠𝑎𝑓𝑒 היא:
𝒪 𝑇𝑆 ⋅ 𝒜
באשר 𝒜 הוא אוטומט כך ש ℒ 𝒜 =𝑚𝑖𝑛𝐵𝑎𝑑𝑃𝑟𝑒𝑓( 𝑃 𝑠𝑎𝑓𝑒 )
</div>
</div>
<div class="ppt-text-layer" style="left:4.3967%;top:78.7688%;width:90.6033%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
גודל אוטומט 𝒜, מסומן ב 𝒜 , הוא מספר המצבים והמעברים ב 𝒜
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
