---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 13-safety-properties
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות בטיחות
Safety Properties
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:87.3772%;top:-0.8058%;width:11.4335%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Aharoni','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
576
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:6.6667%;width:85.0000%;height:13.3333%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תזכורת: תכונות זמן ליניארי
Linear Time Properties
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
<div class="ppt-text-layer" style="left:1.6667%;top:26.6667%;width:97.7673%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת זמן ליניארי היא תת-קבוצה של 2 𝐴𝑃 𝜔
• קבוצת רצפי העקבות שאנחנו מחשיבים חוקיים
• מערכת מצבים 𝑇𝑆 מקיימת תכונת זמן ליניארי 𝑃:
𝑇𝑆⊨𝑃 אם ורק אם 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑃
  • התכונה מתקיימת אם כל התנהגויות המערכת &quot;חוקיות&quot;
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
3
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:16.8184%;width:88.3333%;height:32.5996%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 𝐼𝑛𝑣 היא שמורה אם קיים תנאי מצב 𝜙 כך ש-
𝑃 𝐼𝑛𝑣 = { 𝜎∈ 2 𝐴𝑃 𝜔 : ∀𝑗≥ 0 . 𝜎[𝑗]⊨𝜙 }
𝜙 נקרא תנאי השמורה (invariant condition)
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: שמורות (invariants)
</div>
</div>
<div class="ppt-text-layer" style="left:20.3515%;top:55.5556%;width:59.2971%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#9e3611;white-space:pre-wrap;width:100%;">
𝑃 𝑚𝑢𝑡𝑒𝑥 = 𝜎∈ 2 𝐴𝑃 𝜔 :∀𝑖≥0 . 𝜎⊨¬ 𝑐𝑟𝑖 𝑡 1 ∧𝑐𝑟𝑖 𝑡 2
</div>
</div>
<div class="ppt-text-layer" style="left:10.5665%;top:63.6097%;width:80.6522%;height:5.9053%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#9e3611;white-space:pre-wrap;width:100%;">
𝑃 𝑖𝑛𝑑 = 𝜎∈ 2 𝐴𝑃 𝜔 :𝜎 0 ⊨𝑝 ∧ ∀𝑖≥0 . 𝜎 𝑖 ⊨𝑝 → 𝜎 𝑖+1 ⊨𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:81.2132%;top:49.7941%;width:16.9381%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תכונות שמורה:
</div>
</div>
<div class="ppt-text-layer" style="left:76.6435%;top:74.3678%;width:21.1279%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא תכונות שמורה:
</div>
</div>
<div class="ppt-text-layer" style="left:17.2023%;top:80.1293%;width:65.5955%;height:5.4004%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#9e3611;white-space:pre-wrap;width:100%;">
𝑃 𝑠𝑡𝑎𝑟𝑣 = 𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎[𝑖]⊨𝑤𝑎𝑖 𝑡 1 →∃𝑗&gt;𝑖. 𝜎 𝑗 ⊨𝑐𝑟𝑖 𝑡 1
</div>
</div>
<div class="ppt-text-layer" style="left:10.1896%;top:88.1881%;width:79.6207%;height:5.8174%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#9e3611;white-space:pre-wrap;width:100%;">
𝑃 𝑡𝑟𝑎𝑓𝑖𝑐𝑙𝑖𝑔ℎ𝑡 = 𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎 𝑖 ⊨𝑔𝑟𝑒𝑒𝑛 →𝑖&gt;0∧ 𝜎 𝑖−1 ⊨𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונה של מצב / תכונה של ריצה
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
<div class="ppt-text-layer" style="left:7.5000%;top:22.8144%;width:90.8333%;height:67.2127%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הפסוקים האטומיים והפונקציה 𝐿 המתאימה אותם למצבים מְאַפְשְׁרוֹת לנו לדבר על תכונות של מצבים
• למשל:
&quot;תהליך 1 נמצא בקטע הקריטי&quot;
  • &quot;המצב 𝑠 מקיים את הפסוק 𝑝 או את הפסוק 𝑞&quot; (סימון: 𝑠⊨𝑝∨𝑞 )
• אנחנו מתעניינים גם בתכונות של ריצות כמו:
&quot;הרמזור לא יישאר אדום למשך יותר משלושה צעדים רצופים&quot;
• לא מספיק לבדוק מצבים לחוד כפי שבדקנו תכונות שמורה
</div>
</div>
<div class="ppt-text-layer" style="left:-0.1521%;top:76.2987%;width:15.1521%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
הבעיה יכולה להיות במקטע של הריצה, לא רק במצב יחיד
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
5
</div>
</div>
<div class="ppt-text-layer" style="left:2.9167%;top:15.5556%;width:94.1667%;height:78.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃⊆ 2 𝐴𝑃 𝜔 היא תכונת בטיחות אם ורק אם
  לכל מילה שלא מקיימת את התכונה, 𝜎∈ 2 𝐴𝑃 𝜔 ∖𝑃,
  יש רֵישָׁא, 𝜌⊏𝜎, כך שכל מילה שתמשיך את 𝜌 לא תקיים את התכונה:
  𝑃∩ 𝜎 ′ ∈ 2 𝐴𝑃 𝜔 : 𝜌⊏ 𝜎 ′ =∅
• 𝜌 נקראת &quot;רֵישָׁא רעה&quot; של 𝑃
  סימון: 𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃)היא קבוצת הרישות הרעות של 𝑃
• 𝜌 היא &quot;רֵישָׁא רעה מינימאלית&quot; של 𝑃 אם 𝜌∈𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃) אבל אין רֵישָׁא ממש של𝜌 ב- 𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃)
</div>
</div>
<div class="ppt-text-layer" style="left:2.5393%;top:56.6667%;width:22.7025%;height:14.8958%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#742217;white-space:pre-wrap;width:100%;">
𝜌⊏𝜎 הוא סימון שאומר ש-𝜌 היא רֵישָׁא של 𝜎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
6
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:16.5379%;width:95.0000%;height:78.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 היא תכונת בטיחות אם לכל 𝜎 שאינה מקיימת את 𝑃 יש רֵישָׁא 𝜌 כך שכל 𝜎 ′′ ש-𝜌 היא רֵישָׁא שלה לא מקיימת את 𝑃.
</div>
</div>
<div class="ppt-text-layer" style="left:45.1981%;top:66.4332%;width:8.3432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(6.36deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
𝜎∉𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:42.6125%;top:74.9912%;width:13.3333%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(356.44deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
𝜌⊏𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:39.4222%;top:86.6959%;width:20.1399%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(7.04deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎 ′′ s.t 𝜌 𝜎′ ′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:65.8333%;top:35.5556%;width:29.1667%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#743c29;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מתמטיקאי המנסה להוכיח ש-𝑃 היא תכונת בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:35.5556%;width:24.1667%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#743c29;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
יריב המנסה להראות שההוכחה אינה נכונה
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:85.5556%;width:28.3333%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#336600;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
ההוכחה נכונה אם היריב לא יכול למצוא כזאת 𝜎′′
</div>
</div>
<div class="ppt-text-layer" style="left:8.7530%;top:64.7950%;width:28.3333%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#336600;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
היריב יכול לתת כל 𝜎 שהוא רוצה
</div>
</div>
<div class="ppt-text-layer" style="left:60.8080%;top:74.1766%;width:28.3840%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#336600;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
המוכיח צריך למצוא רישא רעה 𝜌
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ניסוח שקול
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
7
</div>
</div>
<div class="ppt-text-layer" style="left:2.9167%;top:15.7584%;width:94.1667%;height:36.3365%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃⊆ 2 𝐴𝑃 𝜔 היא תכונת בטיחות אם ורק אם
  לכל מילה שלא מקיימת את התכונה, 𝜎⊭𝑃,
  קיים 𝑖≥−1 כך ש- 𝜎 ′ ..𝑖 =𝜎 ..𝑖 ⇒ 𝜎 ′ ⊭𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:65.3527%;top:76.5602%;width:10.8403%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#336600;white-space:pre-wrap;width:100%;">
𝜎 ..𝑖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ניסוח שקול
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
8
</div>
</div>
<div class="ppt-text-layer" style="left:2.9167%;top:15.7584%;width:94.1667%;height:36.3365%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃⊆ 2 𝐴𝑃 𝜔 היא תכונת בטיחות אם ורק אם
  לכל מילה שלא מקיימת את התכונה, 𝜎⊭𝑃,
  קיים 𝑖≥−1 כך ש- 𝜎 ′ ..𝑖 =𝜎 ..𝑖 ⇒ 𝜎 ′ ⊭𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:58.7173%;top:68.0537%;width:35.1282%;height:27.8530%;padding:3.60pt 0.00pt 3.60pt 50.40pt;justify-content:center;text-align:center;direction:rtl;background:#33cc33;opacity:0.169;border:0.75px solid #948182;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#33cc33;white-space:pre-wrap;width:100%;">
תכונת בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:45.4334%;top:52.6504%;width:2.2910%;height:4.3420%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:11.0971%;top:53.6245%;width:72.6282%;height:43.3333%;padding:208.80pt 7.20pt 0.00pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#000000;opacity:0.169;border:0.75px solid #948182;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#494142;white-space:pre-wrap;width:100%;">
𝜎 ′ : 𝜎[..0]⊏ 𝜎 ′
</div>
</div>
<div class="ppt-text-layer" style="left:21.2173%;top:53.6245%;width:50.8333%;height:35.6142%;padding:151.20pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#000000;opacity:0.169;border:0.75px solid #948182;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#494142;white-space:pre-wrap;width:100%;">
𝜎 ′ : 𝜎[..1]⊏ 𝜎 ′
</div>
</div>
<div class="ppt-text-layer" style="left:28.2571%;top:53.7716%;width:35.3400%;height:25.4772%;padding:100.80pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#000000;opacity:0.169;border:0.75px solid #948182;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#494142;white-space:pre-wrap;width:100%;">
𝜎 ′ : 𝜎[.. 2]⊏ 𝜎 ′
</div>
</div>
<div class="ppt-text-layer" style="left:10.9505%;top:50.1835%;width:34.2148%;height:22.2151%;padding:3.60pt 0.00pt 3.60pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#ff0000;opacity:0.169;border:0.75px solid #948182;border-radius:9999px;transform:rotate(340.91deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
לא תכונת בטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.0516%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות
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
<div class="ppt-text-layer" style="left:14.1667%;top:15.3112%;width:85.0000%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מי מהבאות הן תכונות בטיחות? הוכיחו טענותיכם.
</div>
</div>
<div class="ppt-text-layer" style="left:2.7823%;top:38.1384%;width:55.0000%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 1 = 𝜎∈ 2 𝐴𝑃 𝜔 : ∀𝑖. 𝜎 𝑖 ⊨𝑝→ 𝑞∨¬𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:2.7823%;top:54.0655%;width:61.3844%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 2 = 𝜎∈ 2 𝐴𝑃 𝜔 :𝑝∈𝜎 0 →∀𝑖. 𝑝∈𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:2.4605%;top:24.4444%;width:47.1434%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה אינה תכונת בטיחות?
</div>
</div>
<div class="ppt-text-layer" style="left:2.7823%;top:69.9927%;width:55.0000%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 3 = 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑝∈𝜎 2𝑖 → 𝑝∈𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:2.7823%;top:85.9199%;width:55.0000%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 4 = 𝜎∈ 2 𝐴𝑃 𝜔 : ∃𝑖 such that 𝑝∈𝜎[𝑖]
</div>
</div>
<div class="ppt-text-layer" style="left:51.4769%;top:24.4444%;width:47.1434%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#e7fae2;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#336600;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה היא תכונת בטיחות?
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:62.5796%;width:61.3844%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎∈ 𝜎∈ 2 𝐴𝑃 𝜔 :𝑝∈𝜎 0 →∃𝑖. 𝑝∉𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:77.8524%;width:64.1667%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎∈ 𝜎∈ 2 𝐴𝑃 𝜔 :∃𝑖 𝑝∈𝜎 2𝑖 → 𝑝∉𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:91.1111%;width:64.1667%;height:5.8464%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎∈ 𝜎∈ 2 𝐴𝑃 𝜔 :∀𝑖 𝑝∉𝜎 𝑖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.0516%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות
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
<div class="ppt-text-layer" style="left:10.0000%;top:21.1111%;width:84.1667%;height:52.9688%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
טענה: התכונה הבאה היא תכונת בטיחות
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑝∈𝜎 2𝑖 → 𝑝∈𝜎 𝑖
הוכחה:
  • תהי 𝜎⊭𝑃 כלשהי.
  • לפי הגדרת 𝑃, קיים 𝑖 כך ש-𝑝∈𝜎[2𝑖] ו-𝑝∉𝜎[𝑖]
  • תהי 𝜎 ′ כך ש 𝜎 ′ ..2𝑖 =𝜎 ..2𝑖
  • לפי הגדרת 𝑃, 𝜎 ′ ∉𝑃
  • קיבלנו שיש ל-𝜎 רישא רעה שכל המשך שלה לא יקיים את התכונה.
</div>
</div>
<div class="ppt-text-layer" style="left:27.5000%;top:11.7633%;width:47.1434%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#e7fae2;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#336600;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה היא תכונת בטיחות?
</div>
</div>
<div class="ppt-text-layer" style="left:36.0534%;top:84.8773%;width:10.0640%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝜎 ..2𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:26.7312%;top:91.0445%;width:23.9146%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
רישא רעה שכל המשך שלה לא מקיים את התכונה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.0516%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות
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
<div class="ppt-text-layer" style="left:10.0000%;top:21.1111%;width:84.1667%;height:46.3941%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
טענה: התכונה הבאה אינה תכונת בטיחות
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : ∃𝑖 such that 𝑝∈𝜎[𝑖]
הוכחה:
  • ניקח את המילה 𝜎= 𝜔 שאינה שייכת ל-𝑃
  • לכל 𝑖 נבנה את המילה 𝜎 ′ ={ } 𝑖 𝑝 𝜔
  • ע&quot;פ הגדרת 𝑃 , 𝜎 ′ ∈𝑃
  • קיבלנו שלכל 𝑖 קיימת 𝜎 ′ כך ש- 𝜎 ′ ..𝑖 =𝜎 ..𝑖 וגם 𝜎 ′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:14.1005%;top:74.5710%;width:8.7520%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝜎∉𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:25.7732%;top:12.1382%;width:47.1434%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה אינה תכונת בטיחות?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
היחס בין תכונות בטיחות ותכונות שמורה?
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
<div class="ppt-text-layer" style="left:18.7500%;top:20.1852%;width:64.5833%;height:8.1481%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל תכונת שמורה היא גם תכונת בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:43.7047%;top:73.3608%;width:12.5905%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:8.5783%;top:4.3553%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לתכונת בטיחות
שאינה תכונת שמורה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
13
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:24.4444%;width:98.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• מכונה אוטומטית המספקת שירותי בנקאות (ATM)
• דרישה טבעית: &quot;כסף ניתן רק לאחר שהוקלד קוד הסודי נכון (PIN)&quot;
• תכונה זאת אינה שמורה מכיוון שהיא לא תכונה של מצב
• היא תכונת בטיחות (safety property) מכיוון שלכל ריצה שמפירה את התכונה יש רֵישָא (prefix) רעה סופית
• יתרון של תכונות בטיחות: קבוצה רחבה יותר של תכונות שניתן לבדוק באמצעות גרסאות של אלגוריתמי חיפוש בגרף (DFS, BFS)
• תכונות שמורה הם מקרה פרטי של תכונות בטיחות (ראינו בשקף הקודם)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:90.6132%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונת בטיחות רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:28.8719%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.3302%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
14
</div>
</div>
<div class="ppt-text-layer" style="left:3.6586%;top:17.8938%;width:95.1828%;height:15.5532%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
  &quot;אור אדום נדלק רק אחרי אור צהוב&quot;
    {𝜎∈ 2 𝑟𝑒𝑑,𝑦𝑒𝑙𝑙𝑜𝑤 𝜔 : 𝜎 𝑖 ⊨𝑟𝑒𝑑→ 𝑖&gt;0 ∧ 𝜎 𝑖−1 ⊨𝑦𝑒𝑙𝑙𝑜𝑤 }
</div>
</div>
<div class="ppt-text-layer" style="left:3.6586%;top:39.1270%;width:94.1667%;height:17.5026%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לפעמים ניתן לתאר את הרישות הרעות כשפה רגולרית. לדוגמה, קבוצת הרישות הרעות המינימאליות עבור התכונה למעלה היא השפה המתקבלת על ידי האוטומט:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:7.9716%;top:-2.2921%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
כתיבה מקוצרת של האותיות (קבוצות)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
15
</div>
</div>
<div class="ppt-text-layer" style="left:16.0375%;top:19.5075%;width:70.8333%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
  &quot;אור אדום נדלק רק אחרי שדלק קודם אור צהוב&quot;
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונת בטיחות למכונת מכירת המשקאות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
16
</div>
</div>
<div class="ppt-text-layer" style="left:4.4728%;top:16.6667%;width:90.8333%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• דרישה טבעית :
&quot;מספר המטבעות שהוכנסו הוא לפחות מספר המשקאות שניתנו&quot;
• לכל 𝑖≥0:
0≤𝑗≤𝑖 :𝑑𝑟𝑖𝑛𝑘∈ 𝐴 𝑗 ≤ 0≤𝑗≤𝑖 :𝑝𝑎𝑦∈ 𝐴 𝑗
• רישות רעות:
∅ {𝑝𝑎𝑦}{𝑑𝑟𝑖𝑛𝑘}{𝑑𝑟𝑖𝑛𝑘}
∅ 𝑝𝑎𝑦 𝑑𝑟𝑖𝑛𝑘 ∅{𝑝𝑎𝑦}{𝑑𝑟𝑖𝑛𝑘}{𝑑𝑟𝑖𝑛𝑘}
• קל לבדוק שכל הגרסאות שהצגנו למכונות מכירת השתייה עומדות בדרישה
• זאת דוגמה לתכונת בטיחות
שלא ניתן לבטא את הרישות הרעות שלה כשפה רגולרית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: תכונות בטיחות רֵגוּלָרִיּוֹת
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
<div class="ppt-text-layer" style="left:25.4022%;top:26.2502%;width:72.1429%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
משפט: כל תכונת שְׁמוּרָה היא תכונת בטיחות רגולרית
הוכחה:
</div>
</div>
<div class="ppt-text-layer" style="left:52.4925%;top:41.7451%;width:6.3685%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝜙
</div>
</div>
<div class="ppt-text-layer" style="left:47.9481%;top:33.9673%;width:4.4752%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜙
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:16.5468%;width:90.0935%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
תכונה שקבוצת הרישות הרעות המינימליות שלה היא שפה רגולרית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת מול תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
18
</div>
</div>
<div class="ppt-text-layer" style="left:4.5833%;top:21.1111%;width:90.8333%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונות בטיחות מבטאות דרישה &quot;שמשהו רע לא יקרה&quot;
• אפשר לעמוד בדרישה אם לא עושים כלום!
  כך, אף פעם לא נגיע למצב &quot;רע&quot;
• לכן: נוסיף גם תכונות חַיּוּת
  • כדי לדרוש שתהייה &quot;התקדמות&quot;
• דרישות חַיּוּת אומרות:
בסופו של דבר יקרה &quot;משהו טוב&quot; [Lamport 1977]
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/13-safety-properties/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
19
</div>
</div>
<div class="ppt-text-layer" style="left:48.3333%;top:58.1333%;width:45.8333%;height:33.6589%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת
&quot;משהו טוב יקרה&quot;
תמיד יכול להיות
&quot;שהדבר הטוב&quot; יקרה
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:58.1333%;width:32.2113%;height:33.6589%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונות בטיחות
&quot;משהו רע לא יקרה&quot;
לא ניתן לתקן את הדבר הרע
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
