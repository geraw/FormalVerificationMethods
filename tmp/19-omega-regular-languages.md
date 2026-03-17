---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 19-omega-regular-languages
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
שפות 𝜔-רגולריות
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
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: אימות תכונות בטיחות רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:22.2222%;width:95.1816%;height:54.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת בטיחות 𝑃 היא רגולרית אם 𝑏𝑎𝑑𝑃𝑟𝑒𝑓(𝑃) היא רגולרית
• לכן, יש אוטומט 𝒜 ששפתו היא קבוצת הָרֵישׁוֹת הרעות של 𝑃
• אפשר לתרגם בדיקת 𝑇𝑆⊨𝑃 ל:
  • בדיקת שְׁמוּרָה על ההרכבה 𝑇𝑆×𝒜
  • מימוש: אלגוריתם DFS על גרף המצבים של 𝑇𝑆×𝒜
• סיבוכיות זמן ומקום: 𝒪( 𝑇𝑆 ⋅ 𝒜 )
</div>
</div>
<div class="ppt-text-layer" style="left:1.1142%;top:84.7490%;width:97.7018%;height:7.1806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור תכונות כלליות יותר נזדקק לאוטומטים על מילים אינסופיות 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ראשי פרקים
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-2.2222%;width:84.1667%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכנית להמשך: אימות תכונות 𝜔-רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:68.5396%;top:98.6111%;width:31.4604%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:0.8586%;top:2.2222%;width:5.8081%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
4
</div>
</div>
<div class="ppt-text-layer" style="left:66.7677%;top:25.5556%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#9b2d1f;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות
שְׁמוּרָה
</div>
</div>
<div class="ppt-text-layer" style="left:66.7677%;top:50.8333%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#9b2d1f;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מיוצגות ע&quot;י נוסחה לוגית המתארת מצבים העומדים בתנאי השמורה
</div>
</div>
<div class="ppt-text-layer" style="left:66.8939%;top:76.6667%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#9b2d1f;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
נבדקות באמצעות DFS או BFS
</div>
</div>
<div class="ppt-text-layer" style="left:36.7677%;top:25.5556%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#9b2d1f;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות בטיחות רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:36.7677%;top:50.8333%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#9b2d1f;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מיוצגות ע&quot;י אוטומט המתאר את קבוצת הרישות הרעות
</div>
</div>
<div class="ppt-text-layer" style="left:36.5909%;top:76.6667%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#9b2d1f;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
נבדקות ע&quot;י הרכבה 𝑇𝑆×𝒜
ורדוקציה לשְׁמוּרָה
</div>
</div>
<div class="ppt-text-layer" style="left:6.7677%;top:25.5556%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#855d5d;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות
𝜔-רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:50.8333%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#855d5d;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מיוצגות ע&quot;י אוטומט המתאר מילים אינסופיות
</div>
</div>
<div class="ppt-text-layer" style="left:6.6162%;top:76.6667%;width:23.2323%;height:18.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#855d5d;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
נבדקות ע&quot;י הרכבה 𝑇𝑆×𝒜
וסריקת מעגלים בגרף
</div>
</div>
<div class="ppt-text-layer" style="left:33.2515%;top:16.4328%;width:17.5578%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עד כאן הגענו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:0.0000%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונת חַיּוּת עבור האלגוריתם של פטרסון
</div>
</div>
<div class="ppt-text-layer" style="left:1.4942%;top:82.2222%;width:98.1927%;height:13.6216%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אם מישהו רוצה להיכנס לקטע הקריטי, האם הוא יקבל את ההזדמנות לעשות זאת?
𝑎𝑙𝑤𝑎𝑦𝑠 𝑤𝑎𝑖𝑡𝐿⇒𝑒𝑣𝑒𝑛𝑡𝑢𝑎𝑙𝑙𝑦 𝑐𝑟𝑖𝑡𝐿 ∧ 𝑤𝑎𝑖𝑡𝑅⇒𝑒𝑣𝑒𝑛𝑡𝑢𝑎𝑙𝑙𝑦 𝑐𝑟𝑖𝑡𝑅
</div>
</div>
<div class="ppt-text-layer" style="left:65.1531%;top:60.8859%;width:18.5117%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖 𝑡 𝐿 ,𝑤𝑎𝑖 𝑡 𝑅 }
</div>
</div>
<div class="ppt-text-layer" style="left:34.1968%;top:36.4956%;width:2.8610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:27.4818%;top:48.8869%;width:11.0864%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖 𝑡 𝐿 }
</div>
</div>
<div class="ppt-text-layer" style="left:2.3706%;top:23.3333%;width:28.6514%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 𝑃𝑒𝑡 = 𝑇𝑆 𝑃 𝐺 1 ∥𝑃 𝐺 2
</div>
</div>
<div class="ppt-text-layer" style="left:20.5802%;top:73.3333%;width:17.6001%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖 𝑡 𝐿 , 𝑤𝑎𝑖 𝑡 𝑅 }
</div>
</div>
<div class="ppt-text-layer" style="left:64.8299%;top:73.4808%;width:17.6001%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖 𝑡 𝐿 ,𝑐𝑟𝑖 𝑡 𝑅 }
</div>
</div>
<div class="ppt-text-layer" style="left:8.5548%;top:49.0893%;width:10.1748%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖 𝑡 𝐿 }
</div>
</div>
<div class="ppt-text-layer" style="left:64.7577%;top:48.9831%;width:11.3031%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖 𝑡 𝑅 }
</div>
</div>
<div class="ppt-text-layer" style="left:65.7263%;top:36.3555%;width:2.8610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:83.3585%;top:49.2256%;width:10.3915%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖 𝑡 𝑅 }
</div>
</div>
<div class="ppt-text-layer" style="left:19.6686%;top:61.1410%;width:18.5117%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖 𝑡 𝐿 ,𝑤𝑎𝑖 𝑡 𝑅 }
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
5
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכנית להמשך:
תיאור תכונות באמצעות אוטומט Büchi
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:25.0000%;top:48.2796%;width:16.5707%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑤𝑎𝑖𝑡∨𝑐𝑟𝑖𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:48.4685%;top:28.5781%;width:16.5707%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑤𝑎𝑖𝑡∧¬𝑐𝑟𝑖𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:52.3647%;top:48.5782%;width:6.9372%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:74.2142%;top:48.5782%;width:8.8305%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑐𝑟𝑖𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:12.5524%;top:66.0540%;width:77.8094%;height:10.0313%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑤𝑎𝑖𝑡∨𝑐𝑟𝑖𝑡 + 𝑤𝑎𝑖𝑡∧¬𝑐𝑟𝑖𝑡 . ¬𝑐𝑟𝑖𝑡 ∗ .𝑐𝑟𝑖𝑡 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:36.1417%;top:57.1780%;width:61.4344%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9e3611;white-space:pre-wrap;width:100%;">
נאפשר לתאר גם באמצעות &quot;ביטוי 𝜔-רגולרי&quot;:
</div>
</div>
<div class="ppt-text-layer" style="left:3.7051%;top:43.3333%;width:19.0684%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
Julius Richard Büchi
(1924–1984)
</div>
</div>
<div class="ppt-text-layer" style="left:18.6497%;top:88.4742%;width:64.3950%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎𝑙𝑤𝑎𝑦𝑠 𝑤𝑎𝑖𝑡→𝑒𝑣𝑒𝑛𝑡𝑢𝑎𝑙𝑙𝑦 𝑐𝑟𝑖𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:32.6605%;top:19.7021%;width:66.8479%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9e3611;white-space:pre-wrap;width:100%;">
נאפשר לתאר גם תכונות חַיּוּת באמצעות אוטומט:
</div>
</div>
<div class="ppt-text-layer" style="left:54.9619%;top:80.1470%;width:43.1464%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9e3611;white-space:pre-wrap;width:100%;">
ובאמצעות &quot;לוגיקה טמפורלית&quot;:
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
6
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכנית להמשך:
שפות אומגה רגולריות (𝜔-רגולריות)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:22.4820%;width:90.8333%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שפה רגולרית היא אוסף של מילים באורך סופי
שניתן לתאר באמצעות אוטומט או ביטוי רגולרי
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:77.8828%;width:90.8333%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שפה 𝜔-רגולרית היא אוסף של מילים באורך אינסופי
שניתן לתאר באמצעות אוטומט Büchi או ביטוי 𝜔-רגולרי
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
7
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ראשי פרקים
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:1.5038%;top:-1.1111%;width:91.8295%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אופרטורים מעל שפות פורמאליות
</div>
</div>
<div class="ppt-text-layer" style="left:70.7406%;top:100.0000%;width:29.2594%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:11.3902%;top:34.6756%;width:77.8783%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שרשור: 𝐿 1 . 𝐿 2 = 𝑤 1 . 𝑤 2 : 𝑤 1 ∈ 𝐿 1 , 𝑤 2 ∈ 𝐿 2
</div>
</div>
<div class="ppt-text-layer" style="left:10.8748%;top:60.8088%;width:77.8784%;height:7.0384%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כוכבית של קליני: 𝐿 ∗ = 𝑖=0 ∞ 𝐿 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:10.8748%;top:44.8474%;width:77.8783%;height:12.2902%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
העלאה בחזקה: 𝐿 𝑖 = 𝐿.𝐿. ⋅⋅⋅.𝐿 פעמים 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:71.5184%;width:78.4352%;height:7.0338%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
חזרה פעם אחת או יותר: 𝐿 + = 𝑖=1 ∞ 𝐿 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:2.3976%;top:17.7778%;width:95.9357%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בהינתן שפות (קבוצות של מילים) הגדרנו, בקורס &quot;מבנים חישוביים&quot;
פעולות ליצירת שפות חדשות:
</div>
</div>
<div class="ppt-text-layer" style="left:2.3976%;top:83.3852%;width:94.8326%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרנו את קבוצת השפות הרגולריות באמצעות פעולות אלה
בקורס זה נמשיך את הרעיון להגדרת קבוצת השפות האומגה רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
9
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:8.3775%;top:-3.2724%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה רקוסיבית: ביטויים רגולריים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
10
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:17.4830%;width:90.0000%;height:80.2948%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תחביר ביטויים רגולריים מעל Σ:
𝐸 :≔∅ 𝜖 𝐴∈Σ | 𝐸 + 𝐸’ | 𝐸.𝐸’ | 𝐸 ∗
הסמנטיקה של ביטוי רגולרי 𝐸היא שפה ℒ 𝐸 ⊆ Σ ∗ המוגדרת, באופן רקורסיבי על ידי:
ℒ ∅ =∅
ℒ 𝜖 = 𝜖
ℒ 𝐴 = 𝐴
ℒ 𝐸+𝐸’ =ℒ 𝐸 ∪ℒ(𝐸’)
ℒ 𝐸.𝐸’ =ℒ 𝐸 .ℒ 𝐸’ = 𝑤. 𝑤 ′ : 𝑤∈ℒ 𝐸 , 𝑤 ′ ∈ℒ 𝐸 ′
ℒ 𝐸 ∗ =ℒ 𝐸 ∗ = 𝑤 1 .𝑤 2 … 𝑤 𝑛 : 𝑛∈ℕ, ∀𝑖 𝑤 𝑖 ∈ℒ 𝐸 ∪{𝜖}
</div>
</div>
<div class="ppt-text-layer" style="left:60.9111%;top:50.7608%;width:12.7898%;height:3.2326%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #7030a0;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
𝐴+𝐵.𝐶 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:53.1460%;top:59.4837%;width:9.7657%;height:3.2326%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #7030a0;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:71.2125%;top:59.4837%;width:9.7657%;height:3.2326%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #7030a0;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
𝐵.𝐶
</div>
</div>
<div class="ppt-text-layer" style="left:66.4925%;top:67.0264%;width:9.7657%;height:3.2326%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #7030a0;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:78.5368%;top:67.0264%;width:9.7657%;height:3.2326%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #7030a0;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
𝐶
</div>
</div>
<div class="ppt-text-layer" style="left:85.1569%;top:62.7362%;width:5.3314%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝐶}
</div>
</div>
<div class="ppt-text-layer" style="left:65.0188%;top:62.5716%;width:5.4205%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝐵}
</div>
</div>
<div class="ppt-text-layer" style="left:51.6837%;top:55.2137%;width:5.3342%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝐴}
</div>
</div>
<div class="ppt-text-layer" style="left:76.0153%;top:55.1130%;width:6.6287%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝐵𝐶}
</div>
</div>
<div class="ppt-text-layer" style="left:51.4272%;top:46.2710%;width:36.5682%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝜖,𝐴,𝐵𝐶,𝐴𝐵𝐶,𝐴𝐴,𝐵𝐶𝐵𝐶,𝐵𝐶𝐴,𝐵𝐶𝐴𝐴,…}
</div>
</div>
<div class="ppt-text-layer" style="left:45.5873%;top:71.4812%;width:48.2479%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#7030a0;white-space:pre-wrap;width:100%;">
דוגמה: הגדרת משמעות דרך עץ התחביר לביטוי רגולרי פשוט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:7.8378%;top:-1.1111%;width:88.8288%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מביטויים רגולריים לביטויים -𝜔רגולריים
</div>
</div>
<div class="ppt-text-layer" style="left:73.3634%;top:100.0000%;width:28.3033%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:18.8889%;width:96.6667%;height:78.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ביטויים רגולריים מתארים קבוצות של מילים באורך סופי
  למשל:
  הביטוי 𝐴. 𝐴+𝐵 ∗ .𝐵 מתאר את קבוצת המילים מעל הא&quot;ב Σ= 𝐴,𝐵 המתחילות ב-𝐴 ומסתיימות ב-𝐵
  הביטוי 𝐴.𝐵 ∗ מתאר את קבוצת המילים עם 𝐴 במקומות הזוגיים ו-𝐵 במקומות האי-זוגיים
נגדיר גם ביטויים -𝜔רגולריים לתיאור קבוצות של מילים באורך אינסופי
  למשל:
  הביטוי 𝐴. 𝐴+𝐵 ∗ . 𝐵 𝜔 יתאר את קבוצת כל המילים מעל הא&quot;ב Σ= 𝐴,𝐵 המתחילות ב-𝐴 ומסתיימות ברצף של אינסוף 𝐵-ים
  הביטוי 𝐴. 𝐴+𝐵 𝜔 יתאר את קבוצת המילים עם 𝐴 במקומות הזוגיים
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
11
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: תחביר ביטויים -𝜔רגולריים
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
<div class="ppt-text-layer" style="left:4.1667%;top:21.1111%;width:93.3333%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ביטוי -𝜔רגולרי 𝐺 מעל Σ הוא סכום:
𝐺 = 𝐸 1 . 𝐹 1 𝜔 + ⋅⋅⋅+ 𝐸 𝑛 . 𝐹 𝑛 𝜔
באשר 𝐸 𝑖 , 𝐹 𝑖 הם ביטויים רגולריים (רגילים) מעל Σ כך ש 𝜖ℒ( 𝐹 𝑖 )
דוגמאות ביטויים -𝜔רגולריים מעל Σ= 𝐴, 𝐵 :
𝐴+𝐵 ∗ . 𝐵 𝜔 - רק מספר סופי של האותיות הן 𝐴
𝐵 ∗ .𝐴 𝜔 - אינסוף מהאותיות הן 𝐴
𝐴 ∗ . 𝐵 𝜔 + 𝐴 𝜔 - רצף סופי של 𝐴-ים ואחריו רצף אינסופי של 𝐵-ים או רצף אינסופי של 𝐴-ים.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שאלות?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:22.9167%;top:32.2222%;width:50.0000%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎 + 𝑎,𝑏 ∗ + 𝑏 +{} 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:42.0868%;top:22.2222%;width:55.3478%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מי מהבאים הם ביטויים אומגה רגולריים חוקיים?
</div>
</div>
<div class="ppt-text-layer" style="left:22.9167%;top:46.1823%;width:50.0000%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎 + 𝑎,𝑏 ∗ . 𝑏 +𝜖 𝜔 + 𝑎 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:60.1424%;width:50.0000%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎 . 𝑎 ∗ . 𝑎 + 𝑎,𝑏 ∗ 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:74.1024%;width:50.0000%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎 . 𝑎 ∗ . 𝑎 + 𝑎,𝑏 + 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:89.4158%;width:77.4841%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#003399;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Agency FB','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
https://play.kahoot.it/#/k/f5aefb35-8427-4809-807c-7098ee85599f
</div>
</div>
<div class="ppt-text-layer" style="left:68.9744%;top:75.6374%;width:19.1667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#1f9d25;white-space:pre-wrap;width:100%;">
ביטוי חוקי
</div>
</div>
<div class="ppt-text-layer" style="left:3.2648%;top:29.3793%;width:19.1667%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כל מחובר חייב להסתיים בביטוי בחזקת 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:74.2628%;top:43.3708%;width:19.1667%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
לביטוי בחזקת 𝜔 אסור להכיל את המילה הריקה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
13
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: משמעות ביטויים -𝜔רגולריים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
14
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:25.5556%;width:89.0278%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• עבור 𝐿⊆ Σ + נגדיר 𝐿 𝜔 = 𝑤1.𝑤2.𝑤3… : ∀𝑖 𝑤𝑖∈𝐿
• עבור ביטוי𝜔 -רגולרי 𝐺= 𝐸 1 . 𝐹 1 𝜔 + ⋅⋅⋅+ 𝐸 𝑛 . 𝐹 𝑛 𝜔 נגדיר את המשמעות של 𝐺 כשפה ℒ 𝜔 𝐺 ⊆ Σ 𝜔 :
ℒ 𝜔 𝐺 =ℒ 𝐸 1 . ℒ 𝐹 1 𝜔 ∪ ⋅⋅⋅ ∪ℒ 𝐸 𝑛 . ℒ 𝐹 𝑛 𝜔
• 𝐺1 ו 𝐺2 שקולים, בסימון 𝐺 1 ≡𝐺 2 , אם ℒ 𝜔 𝐺 1 = ℒ 𝜔 𝐺 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שאלות?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:11.3385%;top:24.8642%;width:77.5000%;height:12.9456%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
ℒ 𝜔 𝑝 + 𝑝,𝑞 𝑝 ∗ . 𝑞 +{} ¬𝑝 𝜔 = ℒ ω (𝑝 ∗ .¬ 𝑝) ω
</div>
</div>
<div class="ppt-text-layer" style="left:1.9979%;top:16.6667%;width:96.3120%;height:6.4943%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בהנחה ש- Σ= 2 𝑝,𝑞 = {}, 𝑝 , 𝑞 , 𝑝,𝑞 , מה משמעות הביטויים הרגולריים הבאים?
</div>
</div>
<div class="ppt-text-layer" style="left:11.3385%;top:45.1583%;width:77.5000%;height:10.2940%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
ℒ 𝜔 ( 𝑝,𝑞 𝑝 ∧ 𝑞 ∗ . 𝑝 + 𝑞 +{ } ¬ 𝑝 ∧ 𝑞 𝜔 )= ℒ 𝜔 𝑝∧𝑞 ∗ . ¬ 𝑝∧𝑞 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:11.3385%;top:64.0686%;width:77.5000%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
ℒ 𝜔 𝑝 𝜔 + 𝑞 𝜔 = ℒ 𝜔 𝑝∧¬𝑞 𝜔 + 𝑞∧¬𝑝 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:11.3385%;top:80.0724%;width:77.5000%;height:10.2202%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
ℒ 𝜔 ( {}+ 𝑝 + 𝑞 + 𝑝,𝑞 ∗ 𝑡𝑟𝑢 𝑒 ∗ . 𝑞 + 𝑝,𝑞 𝑞 𝜔 )= ℒ 𝜔 𝑡𝑟𝑢 𝑒 ∗ . 𝑞 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:36.8368%;width:27.1718%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0033cc;white-space:pre-wrap;width:100%;">
always (eventually ¬𝑝)
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:55.7257%;width:35.7352%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0033cc;white-space:pre-wrap;width:100%;">
𝑝∧𝑞 until (always ¬(𝑝∧𝑞) )
</div>
</div>
<div class="ppt-text-layer" style="left:51.6667%;top:72.1921%;width:40.9425%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0033cc;white-space:pre-wrap;width:100%;">
always 𝑝∧¬𝑞 ∨ always 𝑞∧¬𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:57.5000%;top:90.3403%;width:24.9910%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0033cc;white-space:pre-wrap;width:100%;">
eventually (always 𝑞)
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
15
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שפות -𝜔רגולריות
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
<div class="ppt-text-layer" style="left:4.1667%;top:25.5556%;width:92.5000%;height:67.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הגדרה:
𝐿 היא שפה 𝜔-רגולרית אם 𝐿 = ℒ 𝜔 (𝐺) עבור ביטוי 𝜔-רגולרי 𝐺
• דוגמאות מעל Σ= 𝐴, 𝐵 :
  • שפת כל המילים עם מספר אינסופי של 𝐴-ים: 𝐵 ∗ .𝐴 𝜔
  • שפת כל המילים עם מספר סופי של 𝐴-ים: 𝐴+𝐵 ∗ . 𝐵 𝜔
• נוכיח בהמשך:
קבוצת השפות ה 𝜔-רגולריות סגורה תחת איחוד, חיתוך והשלמה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:94.0426%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: תכונות -𝜔רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:29.9645%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:28.8889%;width:86.6667%;height:48.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 היא 𝜔-רגולרית מעל 𝐴𝑃
אם
𝑃= ℒ 𝜔 (𝐺) עבור ביטוי 𝜔-רגולרי 𝐺 מעל 2 𝐴𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
17
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות כלליות של תכונות -𝜔רגולריות
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
<div class="ppt-text-layer" style="left:-0.8333%;top:15.3249%;width:99.1667%;height:81.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל תכונת שמורה היא תכונה 𝜔-רגולרית
  הוכחה: 𝐴⊨Φ 𝐴 𝜔 , באשר Φ הוא תנאי השמורה, הוא ביטוי 𝜔-רגולרי
  דוגמה: אםΦ=¬ 𝑐𝑟𝑖𝑡 1 ∨¬𝑐𝑟𝑖 𝑡 2 ו-𝐴𝑃= 𝑐𝑟𝑖 𝑡 1 ,𝑐𝑟𝑖 𝑡 2 אז
  𝜎:∀𝑖. 𝜎 𝑖 ⊨Φ = 𝐿 𝜔 {}+ 𝑐𝑟𝑖 𝑡 1 + 𝑐𝑟𝑖 𝑡 2 𝜔
כל תכונת בטיחות רגולרית 𝑃 היא תכונה 𝜔-רגולרית
  הוכחה: השפה המשלימה 𝑏𝑎𝑑𝑃𝑟𝑒𝑓(𝑃). 2𝐴𝑃 𝜔 היא 𝜔-רגולרית וקבוצת השפות ה 𝜔-רגולריות סגורה תחת השלמה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-019.png" alt="" />
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
<div class="ppt-text-layer" style="left:8.3333%;top:0.0000%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות של תכונות מסוימות
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:25.5556%;width:95.0000%;height:64.7260%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝐴𝑃={𝑤𝑎𝑖𝑡, 𝑐𝑟𝑖𝑡}
𝑃𝑝𝑒𝑡 = תהליך מבקר בקטע הקריטי אינסוף פעמים
𝐸=( ∅+ 𝑤𝑎𝑖𝑡 ∗ ¬𝑐𝑟𝑖𝑡 ∗ . 𝑐𝑟𝑖𝑡 + 𝑤𝑎𝑖𝑡,𝑐𝑟𝑖𝑡 𝑐𝑟𝑖𝑡 ) 𝜔
𝑃𝑠𝑡𝑎𝑟𝑣 = אם תהליך ממתין, הוא ייכנס לקטע הקריטי בסופו של דבר
𝐸= ¬𝑤𝑎𝑖𝑡 ∗ .𝑤𝑎𝑖𝑡.𝑡𝑟𝑢 𝑒 ∗ .𝑐𝑟𝑖𝑡 𝜔 + 𝑡𝑟𝑢𝑒 ∗ . ¬𝑤𝑎𝑖𝑡 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:65.0000%;top:37.3472%;width:28.3333%;height:21.5417%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
זה לא ביטוי אומגה רגולרי, רק קיצור נוח לכתיבה עבורנו, בהבנה שכולנו יודעים איך לפרוש אותו לביטוי אומגה רגולרי תקין
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ראשי פרקים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
20
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:7.5765%;top:2.6834%;width:90.2198%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט Büchi לא דטרמיניסטי
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:21.5723%;width:93.7579%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• בדרך כלל: משתמשים באוטומטים להגדרת שפות של מילים באורך סופי
• אנחנו נשתמש באוטומטים גם להגדרת שפות של מילים באורך אינסופי
  • דרך נוספת להגדרת שפות 𝜔-רגולריות
  • נשתמש באוטומטי Büchi לא דטרמיניסטיים (NBA)
• ריצה מקבלת צריכה לבדוק את כל מילת הקלט ⇐ הריצה אינסופית
  • הדרישה הרגילה שהריצה תסתיים במצב מקבל לא רלוונטית
  • נדרש תנאי קבלה אחר לריצות אינסופיות
  • התנאי שהגדיר בוקי: הריצה תבקר במצבים המקבלים אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
21
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט Büchi
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
22
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:22.8270%;width:88.3333%;height:70.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט Büchi לא דטרמיניסטי (NBA) הוא :〈𝑄, Σ, 𝛿, 𝑄 0 , 𝐹〉
• 𝑄 היא קבוצת מצבים סופית
• Σהוא האלפבית
• 𝛿: 𝑄×Σ→ 2 𝑄 היא פונקציית מעברים
• 𝑄 0 ⊆𝑄 היא קבוצת מצבים התחלתיים
• 𝐹⊆𝑄 היא קבוצת מצבים מקבלים
</div>
</div>
<div class="ppt-text-layer" style="left:7.1875%;top:40.9491%;width:3.8889%;height:5.2083%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:22.1354%;top:40.9491%;width:3.8889%;height:5.2083%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:38.2118%;top:41.5278%;width:1.7188%;height:3.1019%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'CMMI10','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
q
</div>
</div>
<div class="ppt-text-layer" style="left:39.0625%;top:42.6389%;width:1.2500%;height:2.1991%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'CMR7','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
3
</div>
</div>
<div class="ppt-text-layer" style="left:15.8854%;top:40.6482%;width:1.8056%;height:3.1481%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:8.3854%;top:34.9537%;width:1.8056%;height:3.1481%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐶
</div>
</div>
<div class="ppt-text-layer" style="left:30.7639%;top:40.6482%;width:1.8924%;height:3.1481%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:38.2986%;top:34.7917%;width:1.8924%;height:3.1481%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:23.2986%;top:52.0602%;width:1.8924%;height:3.1481%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.9800%;top:61.3731%;width:13.1314%;height:5.6797%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:right;direction:rtl;background:#f1dec8;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מה ההבדל?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:1.1726%;width:90.9500%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שפה של NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:28.9792%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:21.1111%;width:89.1667%;height:14.8099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ריצה של האוטומט 𝒜=〈𝑄,Σ,𝛿, 𝑄 0 ,𝐹〉 על מילה 𝜎∈ Σ 𝜔 היא 𝑟∈ 𝑄 𝜔 כך ש-
𝑟 0 ∈ 𝑄 0 ולכל 𝑖≥0 מתקיים 𝑟 𝑖+1 ∈𝛿 𝑟 𝑖 ,𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:40.7673%;width:89.1667%;height:10.0724%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ריצה 𝑟∈ 𝑄 𝜔 היא מְקַבֶּלֶת אם ∃ ∞ 𝑖 . 𝑟 𝑖 ∈𝐹
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
23
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:1.1726%;width:90.9500%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שפה של NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:28.9792%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:21.1111%;width:89.1667%;height:14.8099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ריצה של האוטומט 𝒜=〈𝑄,Σ,𝛿, 𝑄 0 ,𝐹〉 על מילה 𝜎∈ Σ 𝜔 היא 𝑟∈ 𝑄 𝜔 כך ש-
𝑟 0 ∈ 𝑄 0 ולכל 𝑖≥0 מתקיים 𝑟 𝑖+1 ∈𝛿 𝑟 𝑖 ,𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:40.7673%;width:89.1667%;height:10.0724%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ריצה 𝑟∈ 𝑄 𝜔 היא מְקַבֶּלֶת אם ∃ ∞ 𝑖 . 𝑟 𝑖 ∈𝐹
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:53.7170%;width:89.1667%;height:8.0781%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מילה 𝜎∈ Σ 𝜔 מִתְקַבֶּלֶת אם יש ריצה מקבלת עליה
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:66.6667%;width:89.1667%;height:15.9964%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שפת האומגה של האוטומט היא הקבוצה:
ℒ 𝜔 𝒜 = 𝜎∈ Σ 𝜔 : האוטומט ידי על מתקבלת 𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:-0.8333%;top:90.4976%;width:22.9821%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
Julius Richard Büchi
(1924–1984)
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
24
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות -𝜔רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:20.0000%;top:31.1111%;width:60.0000%;height:15.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 היא 𝜔-רגולרית אם
𝑃 היא שפה 𝜔-רגולרית מעל האלפבית 2𝐴𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:60.0000%;width:71.6667%;height:20.4852%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 היא 𝜔-רגולרית אם ורק אם
𝑃 היא השפה המתקבלת ע&quot;י אוטומט Büchi
מעל האלפבית 2𝐴𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:5.3331%;top:49.5187%;width:36.0115%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
נוכיח בהמשך המצגת
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
25
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ייצוג תכונה באמצעות אוטומט NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
26
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:58.8889%;width:95.8333%;height:31.6393%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
האוטומט במצב מקבל בכל פעם שנקראת אות המקיימת 𝑔𝑟𝑒𝑒𝑛
לכן קבוצת המילים המקבלות הן המכילות אינסוף אותיות המקיימות 𝑔𝑟𝑒𝑒𝑛
מילה מתקבלת: 𝑔𝑟𝑒𝑒𝑛,𝑟𝑒𝑑 𝑔𝑟𝑒𝑒𝑛,𝑟𝑒𝑑 2 𝑔𝑟𝑒𝑒𝑛,𝑟𝑒𝑑 3 …
מילה שאינה מתקבלת: 𝑔𝑟𝑒𝑒𝑛,𝑟𝑒𝑑 100 𝑟𝑒𝑑 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:-51.6667%;top:-33.7758%;width:43.3333%;height:53.4054%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:8.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
digraph FSA {
fillcolor=&quot;#FFFFFF&quot;;
rankdir=&quot;LR&quot;;
style=&quot;setlinewidth(0)&quot;;
node [fillcolor=&quot;#ffff78&quot;,fixedsize=&quot;true&quot;,height=0.5,shape=&quot;circle&quot;,style=&quot;filled&quot;,width=0.5];
edge [arrowhead=&quot;vee&quot;,color=&quot;#000000&quot;,style=&quot;solid&quot;];
// Dummy nodes for the initial indicators.
{
initial0 [label=&quot;&quot;,shape=&quot;none&quot;,style=&quot;solid&quot;];
}
// Initial states
initial0 -&gt; 0;
// States
0 [];
1 [shape=&quot;doublecircle&quot;];
// Transitions
0 -&gt; 0 [label=&lt;¬&lt;I&gt;green&lt;/I&gt;&gt;];
0 -&gt; 1 [label=&lt;&lt;I&gt;green&lt;/I&gt;&gt;];
1 -&gt; 0 [label=&lt;¬&lt;I&gt;green&lt;/I&gt;&gt;];
1 -&gt; 1 [label=&lt;&lt;I&gt;green&lt;/I&gt;&gt;];
}
}
</div>
</div>
<div class="ppt-text-layer" style="left:31.3934%;top:50.0177%;width:41.1066%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
always eventually 𝑔𝑟𝑒𝑒𝑛
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:3.3333%;top:1.3028%;width:93.3333%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: בקשה ותגובה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:23.5250%;width:93.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונות מהצורה:
  לאחר כל פעם שמתקיים 𝑟𝑒𝑞, בסופו של דבר, גם 𝑟𝑒𝑠𝑝 יתקיים
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:64.3457%;width:24.9292%;height:7.4050%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑞∨𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:42.7329%;top:44.6751%;width:16.1513%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞∧¬𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:44.0028%;top:64.0113%;width:11.9857%;height:7.4050%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:65.8023%;top:63.8914%;width:14.9080%;height:7.4050%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:25.9489%;top:77.6696%;width:48.7415%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
always 𝑟𝑒𝑞 →eventually 𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
27
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:3.3333%;top:1.3028%;width:93.3333%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: בקשה ותגובה
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:23.5250%;width:93.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונות מהצורה:
  לאחר כל פעם שמתקיים 𝑟𝑒𝑞, בסופו של דבר, גם 𝑟𝑒𝑠𝑝 יתקיים
</div>
</div>
<div class="ppt-text-layer" style="left:20.5246%;top:64.3773%;width:8.4947%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:33.4341%;top:41.0201%;width:6.6013%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:53.6263%;top:56.0064%;width:9.6587%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
28
</div>
</div>
<div class="ppt-text-layer" style="left:20.5246%;top:81.5589%;width:59.8384%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
always 𝑟𝑒𝑞 →next(eventually(𝑟𝑒𝑠𝑝)
</div>
</div>
<div class="ppt-text-layer" style="left:35.6312%;top:55.4929%;width:16.1513%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑞∧𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:55.8256%;top:40.8598%;width:14.2580%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞∧𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:66.1050%;top:63.8215%;width:14.2580%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞∧𝑟𝑒𝑠𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:41.7257%;top:66.4338%;width:16.1513%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑟𝑒𝑞∧𝑟𝑒𝑠𝑝
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המרה מתכונת בטיחות רגולרית ל-NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
29
</div>
</div>
<div class="ppt-text-layer" style="left:38.7646%;top:26.8572%;width:58.1443%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
DFA המגדיר את הרישות הסופיות הרעות:
</div>
</div>
<div class="ppt-text-layer" style="left:33.7548%;top:63.4286%;width:63.6748%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
DBA המגדיר את הריצות האינסופיות הטובות:
</div>
</div>
<div class="ppt-text-layer" style="left:20.0000%;top:16.7325%;width:76.0199%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
טענה: כל תכונת בטיחות רגולרית היא תכונה 𝜔-רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:26.6933%;top:33.5890%;width:19.7038%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦𝑒𝑙𝑙𝑜𝑤∧ ¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:59.8553%;top:42.2998%;width:6.5523%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:70.7864%;top:53.7815%;width:7.5270%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:43.6251%;top:53.9166%;width:21.5971%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤∧ ¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:28.5672%;top:55.8677%;width:11.9980%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
<div class="ppt-text-layer" style="left:13.1677%;top:53.9563%;width:11.9980%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
<div class="ppt-text-layer" style="left:25.7849%;top:69.2960%;width:19.7038%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦𝑒𝑙𝑙𝑜𝑤∧ ¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:58.9469%;top:78.0068%;width:6.5523%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:70.0169%;top:90.0441%;width:7.5270%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:42.7168%;top:89.6236%;width:21.5971%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤∧ ¬𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:27.6589%;top:91.5747%;width:11.9980%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
<div class="ppt-text-layer" style="left:12.2593%;top:89.6633%;width:11.9980%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑦𝑒𝑙𝑙𝑜𝑤
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:5.7017%;top:-1.1111%;width:90.9649%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
באופן כללי
</div>
</div>
<div class="ppt-text-layer" style="left:72.6828%;top:100.0000%;width:28.9839%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:2.9825%;top:22.2222%;width:96.1842%;height:68.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• אם 𝒜= 𝑄, 2 𝐴𝑃 , δ, 𝑄 0 , 𝐹 אוטומט שלם דטרמיניסטי עבור הרישות הרעות של תכונת בטיחות רגולרית 𝑃 𝑠𝑎𝑓𝑒
• נניח, בלי הגבלת הכלליות, שכל מצב ב-𝐹 הוא מלכודת (למה?)
• משפט קל להוכחה: האוטומט
𝒜 = 𝑄, 2 𝐴𝑃 , δ, 𝑄 0 , 𝑄∖𝐹
מקיים
ℒ 𝜔 𝒜 = 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑝𝑟𝑒𝑓 𝜎 ∩ℒ 𝒜 =∅ = 𝑃 𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
30
</div>
</div>
<div class="ppt-text-layer" style="left:8.0420%;top:57.7602%;width:29.9778%;height:8.8791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
האם זה יעבוד גם אם האוטומט לא דטרמיניסטי?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-031.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
NBA מול NFA
שקילות סופית ⇍שקילות 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
31
</div>
</div>
<div class="ppt-text-layer" style="left:5.0893%;top:80.0000%;width:87.1842%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ℒ 𝒜 1 =ℒ 𝒜 2 אבל ℒ 𝜔 𝒜 1 ≠ ℒ 𝜔 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.4306%;top:88.4184%;width:38.2098%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#7030a0;white-space:pre-wrap;width:100%;">
כל האותיות הן 𝐴 והאורך גדול מאחד
</div>
</div>
<div class="ppt-text-layer" style="left:47.6783%;top:62.8350%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:38.7734%;top:52.2921%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.7936%;top:61.3474%;width:7.5550%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.7628%;top:32.6640%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:59.5343%;top:21.1111%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.7936%;top:31.3177%;width:7.4772%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:3.6651%;top:87.9710%;width:19.0663%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל האותיות הן 𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:26.1823%;top:88.0494%;width:12.3977%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
שפה ריקה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-032.png" alt="" />
<div class="ppt-text-layer" style="left:46.5696%;top:21.9858%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:45.7719%;top:41.2608%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:22.7805%;top:30.8344%;width:7.4772%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
DBA מול DFA
שקילות 𝜔 ⇍שקילות סופית
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
32
</div>
</div>
<div class="ppt-text-layer" style="left:6.9825%;top:79.0867%;width:87.1842%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ℒ 𝜔 𝒜 1 = ℒ 𝜔 𝒜 2 אבל ℒ 𝒜 1 ≠ℒ 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:48.0558%;top:51.3172%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:47.2581%;top:70.5922%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:22.8242%;top:58.1547%;width:7.5550%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:65.8333%;top:87.4801%;width:19.0663%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#7030a0;white-space:pre-wrap;width:100%;">
כל האותיות הן 𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:22.7805%;top:86.3657%;width:19.0663%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כל האותיות הן 𝐴
והאורך זוגי
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:86.2219%;width:19.0663%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל האותיות הן 𝐴
והאורך אי-זוגי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-033.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ראשי פרקים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
33
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
NBA ושפות 𝜔-רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
34
</div>
</div>
<div class="ppt-text-layer" style="left:1.2107%;top:20.0000%;width:97.5000%;height:15.7075%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
משפט: מַחְלֶקֶת השפות המתקבלות ע&quot;י אוטומטי NBA
היא מַחְלֶקֶת השפות ה-𝜔-רגולריות
</div>
</div>
<div class="ppt-text-layer" style="left:2.0202%;top:41.1443%;width:97.5946%;height:23.3761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הוכחה בשני כיוונים:
לכל אוטומט 𝒜 יש ביטוי 𝜔-רגולרי 𝐺(𝒜) כך ש- ℒ 𝜔 𝐺 𝒜 =ℒ 𝜔 (𝒜)
לכל ביטוי 𝜔-רגולרי 𝐺 יש אוטומט 𝒜(𝐺) כך ש- ℒ 𝜔 𝒜 𝐺 =ℒ 𝜔 (𝐺)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
כיוון ראשון: מאוטומט לביטוי -𝜔רגולרי
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
35
</div>
</div>
<div class="ppt-text-layer" style="left:0.8421%;top:72.0463%;width:94.6623%;height:26.3801%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝐺= (𝐶 ∗ 𝐴𝐵) מילים סופיות בעלות ריצה 𝑞 3 −ל 𝑞 1 −מ . 𝐵+𝐵 𝐶 ∗ 𝐴𝐵 𝜔 מילים סופיות בעלות ריצה 𝑞 3 −ל 𝑞 3 −מ
</div>
</div>
<div class="ppt-text-layer" style="left:48.9925%;top:23.7505%;width:6.1390%;height:7.2919%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:26.4037%;top:23.5661%;width:6.1390%;height:7.2919%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:71.4209%;top:23.4941%;width:6.1390%;height:7.2919%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:25.0433%;top:16.5088%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐶
</div>
</div>
<div class="ppt-text-layer" style="left:70.6008%;top:15.8529%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:61.2705%;top:21.9595%;width:4.4542%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:38.6817%;top:21.5356%;width:4.3406%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:50.0107%;top:35.3649%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:27.5756%;top:56.2310%;width:4.7501%;height:5.6421%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.00px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:16.6256%;top:56.0884%;width:4.7501%;height:5.6421%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.00px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:18.5573%;top:47.1020%;width:2.6331%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝐶
</div>
</div>
<div class="ppt-text-layer" style="left:33.1926%;top:54.0756%;width:4.1660%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:22.0591%;top:53.7476%;width:4.0748%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:70.0456%;top:54.9981%;width:4.1976%;height:5.5718%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:59.2462%;top:54.8573%;width:4.1976%;height:5.5718%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:59.5505%;top:45.5556%;width:2.6331%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐶
</div>
</div>
<div class="ppt-text-layer" style="left:85.4977%;top:52.2435%;width:2.6331%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:74.4831%;top:52.2435%;width:4.1660%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:65.5036%;top:52.4841%;width:4.0748%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:74.6150%;top:64.2250%;width:2.6331%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:89.5638%;top:54.9981%;width:4.1976%;height:5.5718%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:38.3576%;top:56.3014%;width:4.1976%;height:5.5718%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:4.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 3
</div>
</div>
<div class="ppt-text-layer" style="left:79.7790%;top:54.8373%;width:4.1976%;height:5.5718%;padding:0.00pt 0.00pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:4.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 3 ′
</div>
</div>
<div class="ppt-text-layer" style="left:34.5146%;top:40.9109%;width:29.2243%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תרגום שאנחנו מציעים כאן
</div>
</div>
<div class="ppt-text-layer" style="left:35.3879%;top:65.8640%;width:29.2243%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אלג. שלמדנו בקורס קודם
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:9.4871%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
כיוון ראשון: מאוטומט NBA לביטוי 𝜔-רגולרי
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
36
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:16.6667%;width:99.1667%;height:45.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• יהי 𝒜=〈𝑄,Σ, 𝛿, 𝑄 0 , 𝐹〉 אוטומט NBA
• עבור 𝑞, 𝑝∈𝑄 נגדיר 𝒜 𝑞𝑝 =〈𝑄, Σ, 𝛿, {𝑞}, {𝑝}〉 ונסמן 𝐿 𝑞𝑝 =ℒ 𝒜 𝑞𝑝
• משפט:
ℒ 𝜔 𝒜 = 𝑞 0 ∈ 𝑄 0 , 𝑞∈𝐹 𝐿 𝑞 0 𝑞 . 𝐿 𝑞𝑞 ∖ 𝜖 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:2.7475%;top:13.3333%;width:25.2182%;height:9.9371%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#b81e00;opacity:1.000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
למדנו לבנות לזה ביטוי רגולרי בקורס מבנים חישוביים
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:59.2346%;width:94.2708%;height:20.4197%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הוכחה:
• כל ריצה מקבלת של 𝒜 מתחילה מאחד ממצבי ההתחלה 𝑞 0 ∈ 𝑄 0 ועוברת איסוף פעמים באחד מהמצבים המקבלים 𝑞∈𝐹. לכן יש לה רישא ב- 𝐿 𝑞 0 𝑞 ואפשר לפרק אותה לאינסוף מקטעים ב- 𝐿 𝑞𝑞 ∖ 𝜖 .
• כל ריצה שאפשר לפרק אותה כך, עוברת אינסוף פעמים במצב מקבל ולכן המילה שנקראת היא בשפת הבוקי של האוטומט.
</div>
</div>
<div class="ppt-text-layer" style="left:2.3308%;top:51.3142%;width:21.2255%;height:9.9371%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#b81e00;opacity:1.000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
אלג. לתרגום אוטומט Buchi לביטוי 𝜔-רגולרי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:0.0000%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
כיוון שני: לכל שפה 𝜔-רגולרית יש אוטומט NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
37
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:20.5556%;width:99.1667%;height:70.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נבנה NBA עבור הביטוי ה 𝜔-רגולרי:
𝐺 = 𝐸1.𝐹1𝜔 +⋅⋅⋅+ 𝐸 𝑛 . 𝐹 𝑛 𝜔
• נגדיר פעולות על אוטומטים הַמְּחַקּוֹת את האופרטורים בביטויים:
  • עבור אוטומטים 𝒜 1 ו 𝒜 2 קיים NBA המקבל את ℒ 𝜔 𝒜 1 ∪ ℒ 𝜔 ( 𝒜 2 )
  • לכל שפה רגולרית 𝐿⊆ Σ + קיים NBA המקבל את 𝐿 𝜔
  • עבור שפה רגולרית 𝐿⊆ Σ ∗ ואוטומט 𝒜, קיים NBA המקבל את 𝐿. ℒ 𝜔 (𝒜)
• נראה איך מְמַמְּשִׁים כל אחת מהפעולות בשקפים הבאים...
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
38
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:21.1111%;width:85.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
נניח שאנחנו רוצים לתרגם לאוטומט את הביטוי האומגה רגולרי
𝐴+𝐵 ∗ .𝐴. 𝐴 ∗ 𝐵 𝜔 + 𝐴 ∗ . 𝐵 𝜔
באמצעות העובדות הבאות:
ℒ 𝒜 1 =ℒ 𝐴 ∗ 𝐵
ℒ 𝒜 2 =ℒ 𝐴+𝐵 ∗ 𝐴
ℒ 𝒜 3 =ℒ 𝐵
ℒ 𝒜 4 =ℒ 𝐴 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:40.3069%;top:43.5035%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:40.2487%;top:57.8628%;width:6.0355%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:67.5000%;top:61.2813%;width:6.0355%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 3
</div>
</div>
<div class="ppt-text-layer" style="left:67.5000%;top:76.1962%;width:6.0355%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 4
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:75.2878%;width:27.0750%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
שימוש באלגוריתם שלמדנו בקורס קודם
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-039.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שלב ראשון: איחוד של NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
39
</div>
</div>
<div class="ppt-text-layer" style="left:8.0556%;top:26.6667%;width:85.8333%;height:32.7613%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: עבור אוטומטים 𝒜 1 ו 𝒜 2 קיים אוטומט 𝒜 כך ש:
ℒ 𝜔 𝒜 = ℒ 𝜔 𝒜 1 ∪ ℒ 𝜔 𝒜 2
וגם
𝒜 =𝒪 𝒜 1 +| 𝒜 2 |
</div>
</div>
<div class="ppt-text-layer" style="left:14.9161%;top:74.4444%;width:72.1122%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#1f9d25;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תרגיל קל: איך נִבְנֶה כזה אוטומט?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-040.png" alt="" />
<div class="ppt-text-layer" style="left:8.7148%;top:-1.6317%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב שני: אם היו לנו מעברי אפסילון...
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
40
</div>
</div>
<div class="ppt-text-layer" style="left:58.9721%;top:20.0000%;width:38.1846%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מאוטומטNFA המקבל את 𝐴 ∗ 𝐵 :
</div>
</div>
<div class="ppt-text-layer" style="left:40.6072%;top:25.2419%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:50.6072%;top:25.2419%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:4.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:46.4200%;top:24.3865%;width:4.4367%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:44.9809%;top:51.0443%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:55.5127%;top:51.0443%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:4.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:40.9492%;top:59.4472%;width:4.3231%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:51.0197%;top:50.4726%;width:4.4367%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:32.8091%;top:51.0237%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0 ′
</div>
</div>
<div class="ppt-text-layer" style="left:39.0366%;top:50.2211%;width:4.9056%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜖
</div>
</div>
<div class="ppt-text-layer" style="left:53.5239%;top:67.9984%;width:41.9873%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לאוטומט NBA המקבל את ( 𝐴 ∗ 𝐵)𝜔:
</div>
</div>
<div class="ppt-text-layer" style="left:31.7358%;top:42.3917%;width:65.4209%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לאוטומטNFA שקול בלי מעברים הנכנסים למצב התחלה:
</div>
</div>
<div class="ppt-text-layer" style="left:36.9316%;top:34.3964%;width:4.3231%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:45.3814%;top:83.2047%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#dad2c3;opacity:1.000;border:1.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:55.9133%;top:83.2047%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#dad2c3;opacity:1.000;border:1.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:41.6219%;top:91.8099%;width:4.3231%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:51.2316%;top:82.5072%;width:4.4367%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:33.2096%;top:83.1841%;width:5.8333%;height:7.7778%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#dad2c3;opacity:1.000;border:4.00px solid #0d0d0d;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0 ′
</div>
</div>
<div class="ppt-text-layer" style="left:39.8135%;top:82.7253%;width:4.9056%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜖
</div>
</div>
<div class="ppt-text-layer" style="left:45.8527%;top:74.2284%;width:4.9056%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-041.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שלב שני: דוגמה לאופרטור 𝜔 עבור NFA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
41
</div>
</div>
<div class="ppt-text-layer" style="left:39.3539%;top:20.0000%;width:57.8028%;height:13.9123%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מאוטומטNFA המקבל את 𝐴 ∗ 𝐵
לאוטומט NBA המקבל את ( 𝐴 ∗ 𝐵)𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:50.2333%;top:41.9111%;width:41.4333%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;background:#633737;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
שלב א&#x27;: מייצרים &quot;עותק&quot; של כל מצב התחלתי ומקבלים אוטומט שקול שבו אין מעבר לתוך מצב התחלתי
</div>
</div>
<div class="ppt-text-layer" style="left:56.2667%;top:71.2444%;width:41.6667%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;background:#633737;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
שלב ב&#x27;: כל מעבר לתוך מצב מקבל
ישוכפל גם למעברים לכל המצבים ההתחלתיים והמצבים ההתחלתיים הופכים להיות המצבים המקבלים
</div>
</div>
<div class="ppt-text-layer" style="left:8.8542%;top:28.0093%;width:5.3819%;height:7.2454%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:21.9965%;top:28.0093%;width:5.3819%;height:7.2454%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:16.9965%;top:27.6157%;width:2.5609%;height:4.2635%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:19.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:10.5382%;top:19.6991%;width:2.4452%;height:4.2635%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:19.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:14.0104%;top:47.9398%;width:5.8507%;height:7.8241%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:27.9688%;top:48.0787%;width:5.6597%;height:7.5463%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:41.8056%;top:48.0787%;width:5.6771%;height:7.5463%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:22.8646%;top:47.6157%;width:2.5694%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:29.6701%;top:62.0139%;width:2.6910%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:36.5451%;top:47.6157%;width:2.6910%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:29.7569%;top:39.3750%;width:2.5694%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:20.3472%;top:77.6389%;width:5.8333%;height:7.8241%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:34.3229%;top:77.7778%;width:5.6424%;height:7.5695%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:48.0208%;top:77.7778%;width:5.6424%;height:7.5695%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:22.1181%;top:68.5880%;width:2.6910%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:29.2535%;top:77.3611%;width:2.5694%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:36.0243%;top:91.7593%;width:2.6910%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:42.8646%;top:77.3611%;width:2.6910%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:36.1111%;top:69.1204%;width:2.5694%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:29.1667%;top:84.0278%;width:2.6910%;height:4.4907%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-042.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בנייה כללית של אוטומט עבור ℒ 𝒜 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
42
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:18.8889%;width:96.6667%;height:66.4815%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בהנתן אוטומט 𝒜=〈𝑄,Σ,𝛿, 𝑄 0 ,𝐹〉 המקיים 𝑄 0 ∩𝐹=∅
נניח, בלי הגבלת הכלליות, שאין מצב התחלה ב 𝒜 שנכנס אליו מעבר
  אחרת נייצר מצב חדש 𝑞𝑛𝑒𝑤𝐹, נוסיף מעבר 𝑞 𝑛𝑒𝑤 𝐴 𝑞 אם ורק אם 𝑞 0 𝐴 𝑞 עבור איזשהו 𝑞0∈𝑄0 ונשמור על כל המעברים ב 𝒜
נבנה אוטומט חדש 𝒜′=〈𝑄,Σ,𝛿′, 𝑄 0 ,𝐹′〉
  אם יש מעבר 𝑞 𝐴 𝑞′ ו 𝑞 ′ ∈𝐹 אז נוסיף מעבר 𝑞 𝐴 𝑞 0 לכל 𝑞0∈𝑄0. נשמור על כל המעברים ב 𝒜. נקבע את המצבים המקבלים להיות מצבי ההתחלה של 𝒜, 𝐹 ′ =𝑄0
מקבלים:
</div>
</div>
<div class="ppt-text-layer" style="left:29.1667%;top:83.9088%;width:40.0000%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#b81e00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
ℒ 𝜔 𝒜′ =ℒ 𝒜 𝜔
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-043.png" alt="" />
<div class="ppt-text-layer" style="left:6.7453%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחה ש ℒ 𝜔 𝒜’ ⊆ℒ(𝒜)𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
43
</div>
</div>
<div class="ppt-text-layer" style="left:10.6188%;top:39.0766%;width:74.7679%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffff99;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
צריך לקחת מילה אינסופית המתקבלת על ידי 𝒜′ ולפרק אותה לרצף מילים סופיות שכל אחת מהן מתקבלת על ידי 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:24.7192%;top:69.9806%;width:64.0037%;height:11.7002%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0 𝜎[0] 𝑞 1 𝜎[1] 𝑞 2 𝜎[2] ⋯ 𝑞 𝑛 1 𝜎 𝑛 1 ⋯ 𝑞 𝑛 2 𝜎 𝑛 2 ⋯ 𝑞 𝑛 3 𝜎 𝑛 3 ⋯
</div>
</div>
<div class="ppt-text-layer" style="left:23.1978%;top:85.6193%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:46.6424%;top:86.0386%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:58.7657%;top:86.0386%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:70.2933%;top:86.0386%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:36.6424%;top:57.4114%;width:35.7390%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מסלולים ממצבי התחלה
למקבלים ב-𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:86.7417%;top:66.9765%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:84.1424%;top:86.0839%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:4.6534%;top:70.2643%;width:19.0723%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה מקבלת
(אינסופית) של 𝒜′
</div>
</div>
<div class="ppt-text-layer" style="left:18.1996%;top:21.5159%;width:4.7471%;height:6.3672%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:29.5729%;top:21.6289%;width:4.5917%;height:6.1599%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:40.7201%;top:21.6289%;width:4.5917%;height:6.1599%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:19.6407%;top:14.1503%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:25.4474%;top:21.2898%;width:2.0769%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:30.9575%;top:33.0069%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:36.5240%;top:21.2898%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:31.0281%;top:14.5836%;width:2.0769%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:25.3768%;top:26.7151%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:59.9943%;top:21.5262%;width:4.8383%;height:6.5134%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:71.8091%;top:21.5262%;width:4.8383%;height:6.5134%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:67.3142%;top:21.1725%;width:2.1640%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:61.5082%;top:14.0556%;width:2.0728%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-044.png" alt="" />
<div class="ppt-text-layer" style="left:6.7453%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחה ש ℒ 𝜔 𝒜’ ⊇ℒ(𝒜)𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
44
</div>
</div>
<div class="ppt-text-layer" style="left:9.3782%;top:39.0922%;width:83.9720%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffff99;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
צריך לקחת סדרת ריצות סופיות של 𝒜 ולבנות ממנה
ריצה אינסופית של 𝒜 ′ המקבלת את שרשור המילים שהן קיבלו
</div>
</div>
<div class="ppt-text-layer" style="left:22.8970%;top:69.6460%;width:64.0037%;height:11.7002%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0 𝜎[0] 𝑞 1 𝜎[1] 𝑞 2 𝜎[2] ⋯ 𝑞 𝑛 1 𝜎 𝑛 1 ⋯ 𝑞 𝑛 2 𝜎 𝑛 2 ⋯ 𝑞 𝑛 3 𝜎 𝑛 3 ⋯
</div>
</div>
<div class="ppt-text-layer" style="left:21.3756%;top:85.2847%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:44.8202%;top:85.7040%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:56.9435%;top:85.7040%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:68.4711%;top:85.7040%;width:11.8893%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מצב התחלה
של 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:34.8202%;top:57.0768%;width:35.7390%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מסלולים ממצבי התחלה
למקבלים ב-𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:84.9195%;top:66.6419%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:82.3202%;top:85.7492%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:2.8312%;top:69.9297%;width:19.0723%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה מקבלת
(אינסופית) של 𝒜′
</div>
</div>
<div class="ppt-text-layer" style="left:18.1996%;top:21.5159%;width:4.7471%;height:6.3672%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:29.5729%;top:21.6289%;width:4.5917%;height:6.1599%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:40.7201%;top:21.6289%;width:4.5917%;height:6.1599%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:19.6407%;top:14.1503%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:25.4474%;top:21.2898%;width:2.0769%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:30.9575%;top:33.0069%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:36.5240%;top:21.2898%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:31.0281%;top:14.5836%;width:2.0769%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:25.3768%;top:26.7151%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:59.9943%;top:21.5262%;width:4.8383%;height:6.5134%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:71.8091%;top:21.5262%;width:4.8383%;height:6.5134%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:67.3142%;top:21.1725%;width:2.1640%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:61.5082%;top:14.0556%;width:2.0728%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-045.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
סיכום שלב שני: אופרטור 𝜔 עבור NFA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
45
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:22.2222%;width:85.8333%;height:27.1356%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עבור כל אוטומט 𝒜 כך ש 𝜖∉ℒ(𝒜)
קיים אוטומט 𝒜 ′ כך ש:
ℒ 𝜔 𝒜 ′ =ℒ 𝒜 𝜔 ו- 𝒜 ′ =𝒪( 𝒜 )
</div>
</div>
<div class="ppt-text-layer" style="left:21.6667%;top:80.0000%;width:5.0636%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:53.8377%;top:78.6714%;width:5.7858%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 ′
</div>
</div>
<div class="ppt-text-layer" style="left:59.2762%;top:65.5827%;width:4.7471%;height:6.3672%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:70.6495%;top:65.6957%;width:4.5917%;height:6.1599%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:81.7967%;top:65.6957%;width:4.5917%;height:6.1599%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:60.7173%;top:58.2171%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:66.5240%;top:65.3566%;width:2.0769%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:72.0341%;top:77.0737%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:77.6006%;top:65.3566%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:72.1047%;top:58.6504%;width:2.0769%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:66.4534%;top:70.7819%;width:2.1616%;height:3.5980%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:17.2743%;top:68.7842%;width:4.8383%;height:6.5134%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:29.0891%;top:68.7842%;width:4.8383%;height:6.5134%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:24.5941%;top:68.4304%;width:2.1640%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:18.7882%;top:61.3135%;width:2.0728%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-046.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב שלישי: שרשור NFA ו NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
46
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:28.8889%;width:85.8333%;height:26.4783%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עבור אוטומטים 𝒜 1 ו 𝒜 2 (שניהם מעל האלפבית Σ)
קיים 𝒜 כך ש:
ℒ 𝜔 𝒜 =ℒ 𝒜 1 . ℒ 𝜔 𝒜 2 ו- 𝒜 =𝒪 𝒜 1 + 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:46.1501%;top:62.2222%;width:12.0821%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
בניה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-047.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: בניית אוטומט ל-ℒ 𝒜 1 . ℒ 𝜔 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
47
</div>
</div>
<div class="ppt-text-layer" style="left:47.5718%;top:59.2509%;width:2.9487%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:27.7778%;width:99.1660%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ℒ . ℒ 𝜔 ( )
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:36.6667%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:38.3333%;top:69.2259%;width:19.1667%;height:17.0538%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל מעבר שהיה אמור ללכת למצב מקבל עובר גם למצבי ההתחלה של האוטומט השני
</div>
</div>
<div class="ppt-text-layer" style="left:42.6049%;top:88.1149%;width:19.1667%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כולל מצבי התחלה...
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:80.0000%;width:19.1667%;height:10.7708%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
מבטלים את המצבים המקבלים באוטומט הראשון
</div>
</div>
<div class="ppt-text-layer" style="left:84.1667%;top:41.1111%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:24.5486%;top:21.6667%;width:4.1319%;height:7.1759%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:24.3924%;top:36.1111%;width:4.3056%;height:7.1759%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:60.4167%;top:17.2917%;width:3.6111%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:60.3125%;top:43.8658%;width:3.7674%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:68.9931%;top:27.1296%;width:3.7674%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:88.6458%;top:30.5787%;width:3.6111%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.1944%;top:63.8889%;width:4.1319%;height:7.1759%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.0556%;top:78.3102%;width:4.3056%;height:7.1759%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:60.7986%;top:57.2917%;width:3.6111%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:60.6597%;top:83.5417%;width:3.7674%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:69.8438%;top:66.9908%;width:3.7674%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:89.4444%;top:70.4167%;width:3.6111%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-048.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מתכון: שרשור NFA ו NBA
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
48
</div>
</div>
<div class="ppt-text-layer" style="left:2.2917%;top:17.7778%;width:95.4167%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
• שמים את האוטומטים זה לצד זה (ה-NFA משמאל וה-NBA מימין)
• &quot;משכפלים&quot; כל מעבר למצב מקבל ב-NFA ע&quot;י הוספה של מעברים (מאותו המקור ועם אותה אות) לכל מצב התחלתי של ה-NBA.
• מצבים מקבלים: המקבלים של ה-NBA. התחלתיים: ההתחלתיים של ה-NFA ואם יש ל-NFA מצבים התחלתיים שהם גם מקבלים, גם המצבים ההתחלתיים של ה-NBA התחלתיים באוטומט החדש
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:89.9674%;width:62.3432%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0033cc;white-space:pre-wrap;width:100%;">
מקבלים אוטומט לשפה: ℒ(𝒜𝑁𝐹𝐴). ℒ𝜔(𝒜𝑁𝐵𝐴)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-049.png" alt="" />
<div class="ppt-text-layer" style="left:5.4054%;top:-1.1111%;width:89.5946%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחה?
</div>
</div>
<div class="ppt-text-layer" style="left:71.4527%;top:100.0000%;width:28.5473%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.3964%;top:2.2222%;width:5.2703%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
49
</div>
</div>
<div class="ppt-text-layer" style="left:1.3964%;top:31.1111%;width:94.4216%;height:17.7535%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
• כל מילה שמתקבלת ב ℒ(𝒜𝑁𝐹𝐴). ℒ𝜔(𝒜𝑁𝐵𝐴) מתקבלת ע&quot;י האוטומט שבנינו
• כל מילה שמתקבלת ע&quot;י האוטומט שבנינו נמצאת ב- ℒ(𝒜𝑁𝐹𝐴). ℒ𝜔(𝒜𝑁𝐵𝐴)
</div>
</div>
<div class="ppt-text-layer" style="left:46.7938%;top:70.2547%;width:3.8287%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
B
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/19-omega-regular-languages/slide-050.png" alt="" />
<div class="ppt-text-layer" style="left:6.6667%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיכום התוצאות (כל שלושת השלבים)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
50
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:32.2222%;width:85.8333%;height:18.4002%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לכל שפה 𝜔-רגולריתℒ
קיים אוטומט (NBA) 𝒜 כך ש ℒ𝜔(𝒜) =ℒ
</div>
</div>
<div class="ppt-text-layer" style="left:9.1667%;top:61.0425%;width:80.8333%;height:30.0686%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ההוכחה קונסטרוקטיבית:
בהינתן ביטוי אומגה רגולרי,
אנחנו יודעים לבנות אוטומט בוקי
בעל אותה השפה !
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
