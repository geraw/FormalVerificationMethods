---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 23-ltl-model-checking
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בדיקת תכונות LTL
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:82.6247%;top:-0.5006%;width:11.4335%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Aharoni','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
620
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: נוסחה ב-LTL
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
<div class="ppt-text-layer" style="left:7.5778%;top:45.2525%;width:87.1512%;height:9.4340%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜙∷= 𝑡𝑟𝑢𝑒 𝑎 𝜙 1 ∧ 𝜙 2 ¬𝜙 °𝜙 | 𝜙 1 U 𝜙 2
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:27.7778%;width:91.6667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דקדוק ל-LTL מעל 𝐴𝑃 באשר 𝑎∈𝐴𝑃 יכול להיות כל פסוק אטומי:
</div>
</div>
<div class="ppt-text-layer" style="left:17.4606%;top:59.9349%;width:42.1668%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
הנוסחה 𝜙 תתקיים בצעד הבא
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:68.9288%;width:64.1667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
הנוסחה 𝜙 1 תתקיים עד שהנוסחה 𝜙 2 תתקיים
</div>
</div>
<div class="ppt-text-layer" style="left:1.9720%;top:84.0892%;width:96.2502%;height:7.6462%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
LTL מגדירה תכונות זמן לינארי = המודל הוא מילים ב 2 𝐴𝑃 𝜔
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:0.0000%;top:14.4444%;width:99.1667%;height:83.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת הזמן הליניארי המוגדרת ע&quot;י נוסחה 𝜓 מעל AP היא:
𝑊𝑜𝑟𝑑𝑠 𝜓 ={𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎⊨𝜓}
כאשר ⊨ הוא היחס הקטן ביותר המקיים:
</div>
</div>
<div class="ppt-text-layer" style="left:3.2128%;top:41.1111%;width:94.3750%;height:53.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜎⊨𝑡𝑟𝑢𝑒
𝜎⊨𝑎 ⇔ 𝑎∈𝜎 0
𝜎⊨ 𝜓 1 ∧ 𝜓 2 ⇔ 𝜎⊨ 𝜓 1 ∧𝜎⊨ 𝜓 2
𝜎⊨¬𝜓 ⇔ 𝜎⊭𝜓
𝜎⊨°𝜓 ⇔ 𝜎 1.. ⊨𝜓
𝜎⊨ 𝜓 1 U 𝜓 2 ⇔ ∃j≥0 . 𝜎 𝑗.. ⊨ 𝜓 2 ∧ ∀0≤𝑖&lt;𝑗 . 𝜎 𝑖.. ⊨ 𝜓 1
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-4.0791%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: סמנטיקה כקבוצות מילים
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סמנטיקה של ,}, }, }
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת תכונות LTL
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
5
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:18.7755%;width:91.2450%;height:69.6586%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה:
𝑇𝑆⊨𝜑 ⇔ 𝑇𝑆⊨𝑊𝑜𝑟𝑑𝑠 𝜑
בעיית החלטה (decision problem):
בהינתן מערכת מעברים 𝑇𝑆 ונוסחת LTL 𝜑:
ענו &quot;כן&quot; אם 𝑇𝑆⊨𝜑 ו &quot;לא&quot; אם 𝑇𝑆⊭𝜑 (עם דוגמה נגדית)
</div>
</div>
<div class="ppt-text-layer" style="left:63.8621%;top:73.8517%;width:10.2303%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:65.4350%;top:86.6334%;width:8.1410%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:18.8090%;top:74.8760%;width:14.0556%;height:5.9583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
&quot;כן&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:18.9652%;top:85.4058%;width:13.7431%;height:9.4340%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
&quot;לא&quot;
דוגמה נגדית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת תכונות LTL
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
6
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:18.7755%;width:91.2450%;height:69.6586%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה:
𝑇𝑆⊨𝜑 ⇔ 𝑇𝑆⊨𝑊𝑜𝑟𝑑𝑠 𝜑
בעיית החלטה (decision problem):
בהינתן מערכת מעברים 𝑇𝑆 ונוסחת LTL 𝜑:
ענו &quot;כן&quot; אם 𝑇𝑆⊨𝜑 ו &quot;לא&quot; אם 𝑇𝑆⊭𝜑 (עם דוגמה נגדית)
</div>
</div>
<div class="ppt-text-layer" style="left:63.8621%;top:73.8517%;width:10.2303%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:65.4350%;top:86.6334%;width:8.1410%;height:10.0729%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:18.8090%;top:74.8760%;width:14.0556%;height:5.9583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
&quot;כן&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:18.9652%;top:85.4058%;width:13.7431%;height:9.4340%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffc000;opacity:0.259;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
&quot;לא&quot;
דוגמה נגדית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
ניסיון ראשון
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
<div class="ppt-text-layer" style="left:2.7937%;top:71.0025%;width:93.5471%;height:11.2196%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
בעיה: השלמה (בניית אוטומט שיקבל את המשלים לשפה) של אוטומט NBA
עשויה לעלות בניפוח אֶקְסְפּוֹנֶנְצְיָאלִי של גודל האוטומט
</div>
</div>
<div class="ppt-text-layer" style="left:33.3570%;top:84.6738%;width:63.2176%;height:7.0768%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
פתרון: נשתמש בעובדה ש- ℒ 𝜔 𝒜 𝜑 = ℒ 𝜔 𝒜 ¬𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:7.6302%;top:23.3333%;width:81.5365%;height:34.9790%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆⊨𝜑 ⇔ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑊𝑜𝑟𝑑𝑠(𝜑) ℒ 𝜔 𝒜 𝜑
⇔ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ∩ ℒ 𝜔 𝒜 𝜑 =∅
</div>
</div>
<div class="ppt-text-layer" style="left:56.1994%;top:59.8665%;width:29.7180%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
אוטומט לשפה המשלימה
</div>
</div>
<div class="ppt-text-layer" style="left:61.2982%;top:41.1111%;width:26.5400%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
אוטומט ל-𝑊𝑜𝑟𝑑𝑠(𝜑)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:6.6187%;top:20.3465%;width:89.1667%;height:44.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆⊨𝜑 ⟺ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆𝑊𝑜𝑟𝑑𝑠 𝜑
⟺ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ∩ 2 𝐴𝑃 𝜔 ∖𝑊𝑜𝑟𝑑𝑠 𝜑 =∅
⟺ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ∩ ℒ 𝜔 𝒜 ¬𝜑 =∅
⟺ 𝑇𝑆× 𝒜 ¬𝜑 ⊨  𝑞∈𝐹 ¬𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אלגוריתם לאימות תכונת LTL
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
<div class="ppt-text-layer" style="left:8.3333%;top:82.7403%;width:80.6165%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
מסקנה: תרגמנו בדיקת תכונת LTL לבדיקת תכונת הַתְמָדָה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:61.4938%;width:34.1028%;height:8.8467%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
הרכבה המתארת את כל הריצות של 𝒜 ¬𝜑 על כל רצפי העקבות של 𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:72.9166%;top:55.8284%;width:26.5266%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
אוטומט המקבל מילה אם היא לא מקיימת את 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:51.2021%;top:67.0042%;width:26.5266%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
קבוצת המצבים המקבלים של האוטומט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:5.8333%;top:36.6667%;width:87.5000%;height:46.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#c7bba6;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
Model Checker
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת תכונותLTL
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
<div class="ppt-text-layer" style="left:62.0833%;top:18.8889%;width:20.8333%;height:4.8611%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#463e2c;white-space:pre-wrap;width:100%;">
מערכת
</div>
</div>
<div class="ppt-text-layer" style="left:62.0833%;top:28.4722%;width:20.8333%;height:4.8611%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#463e2c;white-space:pre-wrap;width:100%;">
מודל של המערכת
</div>
</div>
<div class="ppt-text-layer" style="left:54.1667%;top:42.7778%;width:36.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d8d0c0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4a3128;white-space:pre-wrap;width:100%;">
מערכת מעברים 𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:30.4333%;top:60.0000%;width:36.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d8d0c0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4a3128;white-space:pre-wrap;width:100%;">
המכפלה𝑇𝑆× 𝒜 ¬𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:30.4333%;top:70.2778%;width:36.6667%;height:10.8333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d8d0c0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆× 𝒜 ¬𝜑 ⊨ 𝑞∈𝐹 ¬𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:13.3333%;top:87.7778%;width:15.0000%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#009900;opacity:1.000;border:0.75px solid #336600;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
כן
</div>
</div>
<div class="ppt-text-layer" style="left:66.6667%;top:87.7778%;width:21.6667%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#840900;opacity:1.000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
דוגמה נגדית
</div>
</div>
<div class="ppt-text-layer" style="left:16.2500%;top:18.8889%;width:20.8333%;height:4.8611%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#463e2c;white-space:pre-wrap;width:100%;">
תכונה
</div>
</div>
<div class="ppt-text-layer" style="left:16.2500%;top:28.8889%;width:20.8333%;height:4.8611%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#463e2c;white-space:pre-wrap;width:100%;">
נוסחת LTL 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:42.7778%;width:36.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d8d0c0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4a3128;white-space:pre-wrap;width:100%;">
אוטומט Büchi מוכלל 𝒢 ¬𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:51.1111%;width:36.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d8d0c0;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4a3128;white-space:pre-wrap;width:100%;">
אוטומט Büchi 𝒜 ¬𝜑
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-010.png" alt="" />
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
<div class="ppt-text-layer" style="left:8.7256%;top:10.0189%;width:86.0434%;height:20.0981%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
בהנתן פסוק LTL, 𝜑, נבנה אוטומט 𝒢 𝜑 כך ש- ℒ 𝜔 𝒢 =𝑊𝑜𝑟𝑑𝑠 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:61.5801%;top:65.5464%;width:16.6050%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
משה ורדי
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:77.7778%;width:89.1667%;height:14.8099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
Moshe Y. Vardi, Pierre Wolper:
Automata-Theoretic Techniques for Modal Logics of Programs
J. Comput. Syst. Sci. 32(2): 183-221 (1986)
</div>
</div>
<div class="ppt-text-layer" style="left:18.3521%;top:65.6549%;width:17.4991%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
פייר וולפר
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: אוטומט עבור } g𝑟𝑒𝑒𝑛
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
<div class="ppt-text-layer" style="left:5.0000%;top:20.0000%;width:90.1468%;height:76.7422%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור AP = fgreeng והתכונה } green (לעיתים תכופות נדלק הפנס הירוק)
אפשר לבנות את האוטומט:
האוטומט נמצא במצב מקבל רק אם האות האחרונה שנקראה מכילה את green.
( L!(A) היא קבוצת המילים האינסופיות A0A1A2… כך שיש אינסוף i-ים שעבורם green 2 Ai
( L!(A)=Words(} green)
למשל: הריצה המקבלת את המילה ¾ = fgreeng;fgreeng;… היא (q0q1)!
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:5.8333%;top:-1.0991%;width:88.5666%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎 ∧(𝑏)
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
<div class="ppt-text-layer" style="left:23.7340%;top:50.9596%;width:10.2362%;height:13.6483%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, ¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:67.4541%;top:50.9312%;width:10.2362%;height:13.6483%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:46.4456%;top:35.2659%;width:10.2362%;height:13.6483%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:46.3297%;top:67.7165%;width:10.2362%;height:13.6483%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:51.6666%;top:26.3976%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:79.4792%;top:51.1474%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:52.2377%;top:83.7339%;width:6.1070%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:17.6855%;top:51.1474%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה נוספת: אוטומט עבור (a ) }b)
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
<div class="ppt-text-layer" style="left:5.0000%;top:20.0000%;width:90.1468%;height:82.1276%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עבור AP = fa, bg והתכונה (a ) }b) (בכל פעם שקורה a, יקרה b מאוחר יותר)
אפשר לבנות את האוטומט:
האוטומט נמצא במצב מקבל אם עוד לא קרה a או לאחר b
( L!(A) היא קבוצת המילים האינסופיות A0A1A2… עם אינסוף bים או עם מספר סופי של aים שאחריהם יש b
(
למשל: הריצה המקבלת את המילה ¾ = fag;fbg;! היא q0q1q1(q0)!
</div>
</div>
<div class="ppt-text-layer" style="left:60.0000%;top:80.0000%;width:30.8638%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
L!(A)=Words((a ) }b))
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לצורך באוטומט שאינו דטרמיניסטי
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
<div class="ppt-text-layer" style="left:5.0000%;top:20.0000%;width:90.1468%;height:76.7422%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור AP ¶ fag והתכונה } a (בסופו של דבר, כל הזמן a)
אפשר לבנות את האוטומט:
האוטומט &quot;מנחש&quot; באופן לא דטרמיניסטי מתי מתייצבת התכונה a. המילה מתקבלת אם קיים ניחוש נכון.
( L!(A) היא קבוצת המילים האינסופיות A0A1A2… כך שיש i שעבורו a 2 Aj לכל j ¸ i
( L!(A)=Words(} a)
למשל: הריצה המקבלת את המילה ¾ =; 578fag! … היא q0578 q1!
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משימה: בניית NBA לנוסחת LTL
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
<div class="ppt-text-layer" style="left:7.5000%;top:26.6667%;width:85.0000%;height:60.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נציע אלגוריתם לבניית אוטומט NBA בהינתן נוסחת LTL
יעילות:
  • הנוסחאות בדרך כלל קטנות
  • אוטומט Büchi בגודל אקספוננציאלי יחסית לגודל הנוסחה
  • עלות בדיקות מודל פולינומיאלית ביחס לגודל האוטומט
  • NBA אינם שקולים ל-DBA ⇐ מזעור האוטומט הוא NP-שלם
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תזכורת: GNBA
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
16
</div>
</div>
<div class="ppt-text-layer" style="left:17.5000%;top:74.4444%;width:67.7551%;height:15.7075%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
ריצה מקבלת צריכה לעבור בכל אחת מהקבוצות המקבלות אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:21.1610%;width:89.5853%;height:15.7075%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מאפשרים שיהיו מספר קבוצות מקבלות
(מסומנות, בדרך כלל, ע&quot;י צבעים שונים)
</div>
</div>
<div class="ppt-text-layer" style="left:50.7187%;top:61.7785%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:36.8096%;top:44.2786%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:52.2689%;top:45.9046%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:51.9903%;top:51.7689%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.7950%;top:51.5278%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐
</div>
</div>
<div class="ppt-text-layer" style="left:37.0992%;top:62.5634%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:44.9129%;top:66.3682%;width:3.9708%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה:אוטומט עבור Words }𝑎
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
<div class="ppt-text-layer" style="left:22.7000%;top:25.7333%;width:18.6853%;height:22.2222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:22.7000%;top:57.8667%;width:18.6853%;height:22.2222%;padding:0.00pt 21.60pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:61.8521%;top:40.6436%;width:20.6479%;height:24.5564%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, 𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:16.6862%;top:51.3701%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:43.2821%;top:51.2843%;width:5.9380%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:30.3811%;top:15.5556%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:70.7173%;top:30.4000%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:28.7024%;top:85.7257%;width:5.9380%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:48.0996%;top:69.0812%;width:5.9380%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:4.9084%;top:91.4182%;width:91.6667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: ריצה מקבלת המתחילה במצב מקיימת את כל התכונות הכתובות בו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
רעיון הבניה
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
<div class="ppt-text-layer" style="left:1.6667%;top:18.8889%;width:96.6667%;height:78.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:19.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נבחן את אוסף תת הנוסחאות של הנוסחה הנתונה:
𝑠𝑢𝑏 𝑎 ={𝑎,𝑎, 𝑎}
• כל מצב של האוטומט יבטא &quot;ניחוש&quot; לנכונות כל אחת מתת הטענות בהמשך המילה שֶׁיִּקָּרֵא לאחר שביקרנו במצב:
• בהתחלה ננחש שהנוסחה הכוללת מתקיימת ונדאג שיחס המעברים
&quot;יפיל אותנו מהאוטומט&quot; אם נגלה שניחוש שעשינו אינו נכון.
• בעיה: בנוסחה מהצורה 𝑎, למשל, כשלא רואים אף אות המכילה את 𝑎, לא ניתן
&quot;להפיל מהאוטומט&quot; כי אין זמן סופי שבו ניתן לקבוע שהניחוש אינו מתקיים (תכונת חַיּוּת).
• פתרון: נקרא לזה &quot;הבטחה שצריך לקיים&quot; ונאכוף קיום על ידי זה שהמצב לא יהיה מקבל = מותר להמשיך במצב זמן סופי, אבל בסופו של דבר חייבים לצאת ממנו.
</div>
</div>
<div class="ppt-text-layer" style="left:41.5381%;top:42.2222%;width:15.2570%;height:10.0000%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:18.0711%;top:44.6045%;width:20.6147%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
האות הבאה תכיל את 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:54.6479%;width:28.6437%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
לא כל האותיות הבאות יכילו את 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:64.7813%;top:44.4535%;width:20.1960%;height:10.7708%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
יהיה רגע בעתיד שממנו והלאה כל האותיות יכילו את 𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה: אוטומט עבור Words 𝑎
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
<div class="ppt-text-layer" style="left:4.6156%;top:89.1476%;width:91.6667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
המצבים הם הֲשָׂמוֹת האמת האפשריות לתת הנוסחאות
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:28.5453%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:54.7830%;width:15.2570%;height:18.1450%;padding:0.00pt 86.40pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.0490%;top:40.7199%;width:16.8596%;height:20.0509%;padding:0.00pt 0.00pt 0.00pt 36.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, 𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.0620%;top:26.8084%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.9787%;top:57.9408%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,¬}𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
20
</div>
</div>
<div class="ppt-text-layer" style="left:5.5363%;top:84.5534%;width:91.6667%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
המעברים נקבעים לפי ההשמה לפסוקים האטומיים וכללי הפריסה:
}𝜑⇔𝜑∨°}𝜑, 𝜑⇔𝜑∧°𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:9.2615%;top:49.4784%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:30.8861%;top:49.4083%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.2002%;top:20.4054%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:52.9895%;top:32.3558%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:18.9814%;top:77.5306%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:34.8197%;top:63.9400%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:28.5453%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:54.7830%;width:15.2570%;height:18.1450%;padding:0.00pt 86.40pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.0490%;top:40.7199%;width:16.8596%;height:20.0509%;padding:0.00pt 0.00pt 0.00pt 36.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, 𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.0620%;top:26.8084%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.9787%;top:57.9408%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:81.3312%;top:19.0222%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:72.0576%;top:49.2122%;width:3.3757%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:90.7225%;top:48.1669%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.4004%;top:79.9214%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה: אוטומט עבור Words 𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-021.png" alt="" />
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
<div class="ppt-text-layer" style="left:2.4630%;top:89.1418%;width:95.0740%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טריק מרכזי: המצבים המקבלים נקבעים על פי &quot;הבטחות צריך לקיים&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:9.2615%;top:49.4784%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:30.8861%;top:49.4083%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.2002%;top:20.4054%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:52.9895%;top:32.3558%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:18.9814%;top:77.5306%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:34.8197%;top:63.9400%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:28.5453%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:54.7830%;width:15.2570%;height:18.1450%;padding:0.00pt 86.40pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.0490%;top:40.7199%;width:16.8596%;height:20.0509%;padding:0.00pt 0.00pt 0.00pt 36.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, 𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.0620%;top:26.8084%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.9787%;top:57.9408%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:81.3312%;top:19.0222%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:72.0576%;top:49.2122%;width:3.3757%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:90.7225%;top:48.1669%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.4004%;top:79.9214%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה:אוטומט עבור Words 𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-022.png" alt="" />
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
<div class="ppt-text-layer" style="left:4.6156%;top:89.1476%;width:91.6667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#494142;white-space:pre-wrap;width:100%;">
מצבי ההתחלה הם המצבים המכילים בחיוב את הפסוק הראשי
</div>
</div>
<div class="ppt-text-layer" style="left:9.2615%;top:49.4784%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:30.8861%;top:49.4083%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.2002%;top:20.4054%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:52.9895%;top:32.3558%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:18.9814%;top:77.5306%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:34.8197%;top:63.9400%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:28.5453%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:54.7830%;width:15.2570%;height:18.1450%;padding:0.00pt 86.40pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.0490%;top:40.7199%;width:16.8596%;height:20.0509%;padding:0.00pt 0.00pt 0.00pt 36.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, 𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.0620%;top:26.8084%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.9787%;top:57.9408%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:81.3312%;top:19.0222%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:72.0576%;top:49.2122%;width:3.3757%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:90.7225%;top:48.1669%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.4004%;top:79.9214%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה:אוטומט עבור Words 𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-023.png" alt="" />
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
<div class="ppt-text-layer" style="left:4.6156%;top:89.1476%;width:91.6667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: ℒ 𝜔 𝒢 =𝑊𝑜𝑟𝑑𝑠 }𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:9.2615%;top:49.4784%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:30.8861%;top:49.4083%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.2002%;top:20.4054%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:52.9895%;top:32.3558%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:18.9814%;top:77.5306%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:34.8197%;top:63.9400%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:28.5453%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:14.0803%;top:54.7830%;width:15.2570%;height:18.1450%;padding:0.00pt 86.40pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.0490%;top:40.7199%;width:16.8596%;height:20.0509%;padding:0.00pt 0.00pt 0.00pt 36.00pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, 𝑎,}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.0620%;top:26.8084%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 28.80pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.9787%;top:57.9408%;width:15.2570%;height:18.1450%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑎,¬}𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:81.3312%;top:19.0222%;width:2.4052%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:72.0576%;top:49.2122%;width:3.3757%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:90.7225%;top:48.1669%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.4004%;top:79.9214%;width:4.6379%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה:אוטומט עבור Words 𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:6.8434%;top:-3.2443%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה: NBA עבור הנוסחה 𝑎 U 𝑏
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
<div class="ppt-text-layer" style="left:31.4616%;top:62.2396%;width:22.1933%;height:17.1173%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:7.3429%;top:41.9263%;width:22.1933%;height:17.1173%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:10.6086%;top:33.2536%;width:8.1423%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:34.1642%;top:42.7073%;width:8.1423%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:23.3833%;width:11.5523%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:65.5144%;top:39.4053%;width:23.3272%;height:18.5880%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:89.1277%;top:29.7601%;width:6.5038%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:10.6597%;top:65.8177%;width:8.1423%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:60.5228%;top:70.4932%;width:8.0760%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:31.4704%;top:21.8256%;width:22.1933%;height:17.1173%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, 𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:5.7548%;top:90.2435%;width:85.5881%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: ריצה מקבלת המתחילה במצב מקיימת את כל התכונות הכתובות בו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
NBA עבור הנוסחה 𝑎∧¬𝑏∧ 𝑎U𝑏
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
<div class="ppt-text-layer" style="left:31.4616%;top:62.3252%;width:22.1933%;height:17.1173%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:7.3429%;top:42.0119%;width:22.1933%;height:17.1173%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:10.6086%;top:33.3392%;width:8.1423%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:34.1642%;top:42.7928%;width:8.1423%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:23.4689%;width:11.5523%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:65.5144%;top:39.4909%;width:23.3272%;height:18.5880%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:89.1277%;top:29.8457%;width:6.5038%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:10.6597%;top:65.9033%;width:8.1423%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:60.5228%;top:70.5788%;width:8.0760%;height:4.9806%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:31.4704%;top:21.9111%;width:22.1933%;height:17.1173%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, 𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:28.3333%;top:88.7070%;width:41.3525%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שינינו רק את מצבי ההתחלה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מ-LTL ל-GNBA
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
<div class="ppt-text-layer" style="left:1.6667%;top:19.6444%;width:96.6667%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:17.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בניית GNBA G מעל 2AP עבור נוסחת LTL  עם L!(G) = Words():
• נניח ש- מכילה רק את הַקַּשָּׁרִים Æ, :, °, U
  • הַקַּשָּׁרִים Ç, ), },  ואחרים ניתנים לביטוי באמצעות קַּשָּׁרִים בסיסיים אלה
• המצבים הם קבוצות של תת נוסחאות ב-
  • עבור s=A0A1A2...2 Words() נוסיף ל Ai תת-נוסחאות של  כדי לקבל מילה s’ =B0B1B2... כך ש
  Ã 2 Bi אם ורק אם ¾[i..] = AiAi+1Ai+2... ² Ã
  • ¾’ אמורה להיות ריצה ב-GNBA G עבור ¾
• המעברים נגזרים מהסמנטיקה של ° ומכלל ההרחבה עבור U - כפי שנראה בהמשך
• המצבים המקבלים מבטיחים ש &#x27;¾ היא ריצה מקבלת עבור ¾ אם ורק אם ¾ ² 
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: ממילה לריצה של ה-GNBA
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
<div class="ppt-text-layer" style="left:1.6667%;top:14.4444%;width:96.6667%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נניח = a U (:a Æ b)  ו- ¾ = fag fa,bg fbg...
  • Bi היא תת קבוצה של fa, b, :a Æ b, g [ f :a, :b, :(:a Æ b), :g
  • קבוצת נוסחאות זאת נקראת הסגור של 
• נרחיב את A0=fag, A1=fa,bg, A2=fbg:
  • נוסיף ל-A0 את הנוסחאות :b, :(:a Æ b) המתקיימות ב¾[0..]=¾
  • נוסיף ל-A1 את הנוסחאות, :(:a Æ b)  המתקיימות ב¾[1..]
  • נוסיף ל-A2 את הנוסחאות :a, :a Æ b המתקיימות ב¾[2..]
  • וכך הלאה...
• תוצאה:
¾’ =fa, :b, :(:a Æ b), gfa, b, :(:a Æ b), gf:a, b, :a Æ b, g...
</div>
</div>
<div class="ppt-text-layer" style="left:26.4037%;top:92.3924%;width:4.7719%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
B0
</div>
</div>
<div class="ppt-text-layer" style="left:50.8333%;top:92.3924%;width:6.0963%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
B1
</div>
</div>
<div class="ppt-text-layer" style="left:73.4667%;top:92.3924%;width:6.0963%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
B2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.7500%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תת הנוסחאות
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
<div class="ppt-text-layer" style="left:4.3750%;top:16.6667%;width:93.3333%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור נוסחת LTL 𝜑, הקבוצה 𝑠𝑢𝑏(𝜑)
מורכבת מכל תת-הנוסחאות 𝜓 של 𝜑 והשלילה ¬𝜓 שלהן
למשל:
𝑠𝑢𝑏 𝑎 U 𝑏∧ ¬𝑎 U ¬𝑏 =
</div>
</div>
<div class="ppt-table-layer" style="left:11.6667%;top:57.7778%;width:76.6667%;height:36.6676%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
¬𝑎
</td>
<td class="ppt-table-cell">
𝑎
</td>
</tr>
<tr>
<td class="ppt-table-cell">
¬𝑏
</td>
<td class="ppt-table-cell">
𝑏
</td>
</tr>
<tr>
<td class="ppt-table-cell">
¬ 𝑏∧ ¬𝑎U¬𝑏
</td>
<td class="ppt-table-cell">
𝑏∧ ¬𝑎U¬𝑏
</td>
</tr>
<tr>
<td class="ppt-table-cell">
¬ ¬𝑎U¬𝑏
</td>
<td class="ppt-table-cell">
¬𝑎U¬𝑏
</td>
</tr>
<tr>
<td class="ppt-table-cell">
¬ 𝑎U 𝑏∧ ¬𝑎U¬𝑏
</td>
<td class="ppt-table-cell">
𝑎U 𝑏∧ ¬𝑎U¬𝑏
</td>
</tr>
</table>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:9.7667%;top:-5.2000%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
קבוצות עקביות של נוסחאות
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
<div class="ppt-text-layer" style="left:7.5000%;top:12.2186%;width:85.8333%;height:86.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝐵⊆𝑠𝑢𝑏 𝜑 היא עקבית אם:
𝐵 היא עקבית מבחינה לוגית:
    𝜓 1 ∧ 𝜓 2 ∈𝐵⇔ 𝜓 1 ∈𝐵 ∧ 𝜓 2 ∈𝐵
    𝜓∈𝐵⇒¬𝜓∉𝐵
    𝑡𝑟𝑢𝑒∈𝐵
וגם עקבית מקומית: לכל 𝜓 1 U 𝜓 2 ∈𝑠𝑢𝑏 𝜑
    𝜓 2 ∈𝐵⇒ 𝜓 1 U 𝜓 2 ∈𝐵
    𝜓 1 U 𝜓 2 ∈𝐵⇒ 𝜓 1 ∈𝐵∨ 𝜓 2 ∈𝐵
וגם מקסימאלית: לכל 𝜓∈𝑠𝑢𝑏 𝜑
    𝜓∉𝐵⇒¬𝜓∈𝐵
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סוגי פסוקים
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
<div class="ppt-text-layer" style="left:2.5000%;top:14.4444%;width:93.3333%;height:71.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שלושה סוגים של פסוקים:
• פסוקי מצב:
  • אפשר &quot;לְתַחְזֵק נְכוֹנוּת ניחוש&quot; ע&quot;י בחינת האות הבאה בסדרת העקבות
  • השמת אמת לפסוקים האטומיים משרה ערך אמת לכל פסוק בתחשיב פסוקים
• פסוקים מהצורה°𝜑:
  • הניחוש נכון אם ורק אם 𝜑 נכון במצב הבא
• פסוקים מהצורה 𝜓 1 U 𝜓 2 :
  • או ש- 𝜓 2 נכון עכשיו או ש 𝜓 1 נכון עכשיו וגם 𝜓 1 U 𝜓 2 נכון בצעד הבא
  • מתבסס על כלל הפריסה 𝜑 1 U 𝜑 2 ⇔ 𝜑 2 ∨ 𝜑 1 ∧ ° 𝜑 1 U 𝜑 2
</div>
</div>
<div class="ppt-text-layer" style="left:1.3851%;top:89.2707%;width:95.5631%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
נכונות שאר הנוסחאות נקבעת מֵהֲשָׂמַת אמת לפסוקים האלה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-031.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: GNBA לנוסחת LTL 𝜑
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
<div class="ppt-text-layer" style="left:4.3022%;top:16.9778%;width:91.3956%;height:83.0222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור נוסחת LTL 𝜑 נגדיר 𝐺 𝜑 = 𝑄, 2 𝐴𝑃 , 𝛿, 𝑄 0 , ℱ באשר
• מצבי האוטומט 𝑄⊆𝑠𝑢𝑏(𝜓) הם הקבוצות הַעִקְבִיּוֹת של תת-נוסחאות
• 𝑄 0 ={𝐵∈𝑄:𝜑∈𝐵} – מתחילים מהמצבים המכילים את 𝜑
• 𝐵 ′ ∈𝛿 𝐵,𝐴 אם מתקיימים כל התנאים הבאים:
  • לכל 𝑎∈𝐴𝑃 : 𝑎∈𝐴↔𝑎∈𝐵
  • לכל 𝜓∈𝑠𝑢𝑏 𝜑 : 𝜓∈𝐵↔𝜓∈𝐵’
  • לכל 𝜓 1 U 𝜓 2 ∈𝑠𝑢𝑏 𝜑 :
  𝜓 1 U 𝜓 2 ∈𝐵 ∧ 𝜓 2 ∉𝐵 → 𝜓 1 U 𝜓 2 ∈ 𝐵 ′
  𝜓 1 U 𝜓 2 ∉𝐵 ∧ 𝜓 1 ∈𝐵 → 𝜓 1 U 𝜓 2 ∉ 𝐵 ′
• ℱ= 𝐵∈𝑄: 𝜓 1 U 𝜓 2 ∉𝐵 ∨ 𝜓 2 ∈𝐵 : 𝜓 1 U 𝜓 2 ∈𝑠𝑢𝑏 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:3.2780%;top:85.3656%;width:94.9934%;height:7.0600%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#742217;white-space:pre-wrap;width:100%;">
טענה: ריצה 𝑞 0 𝜎 0 𝑞 1 𝜎 1 𝑞 2 𝜎 2 ⋯ מקבלת אם&quot;ם 𝜙∈ 𝑞 𝑖 ⇔𝜎 𝑖.. ⊨𝜙 לכל 𝜙∈𝑠𝑢𝑏 𝜓
</div>
</div>
<div class="ppt-table-layer" style="left:-51.7286%;top:59.8003%;width:50.0020%;height:13.3333%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
¬𝑎
𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
¬𝑎
¬𝑏
¬ 𝑎 U 𝑏
</td>
</tr>
<tr>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑏}
</td>
<td class="ppt-table-cell">
{}
</td>
</tr>
</table>
</div>
<div class="ppt-table-layer" style="left:-51.7286%;top:38.1817%;width:50.0020%;height:10.6667%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑎
𝜓
</td>
<td class="ppt-table-cell">
𝑎
¬𝜓
</td>
<td class="ppt-table-cell">
¬𝑎
𝜓
</td>
<td class="ppt-table-cell">
𝑎
¬𝜓
</td>
<td class="ppt-table-cell">
¬𝑎
?𝜓
</td>
</tr>
<tr>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{}
</td>
</tr>
</table>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-032.png" alt="" />
<div class="ppt-text-layer" style="left:11.8007%;top:61.3045%;width:7.5800%;height:8.1070%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:3.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎,𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:29.0280%;top:61.2964%;width:7.5800%;height:8.1070%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:3.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:11.8007%;top:79.8187%;width:7.5800%;height:8.1070%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:3.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎,𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:29.0280%;top:79.8187%;width:7.5800%;height:8.1070%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:3.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎, ¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.3045%;top:54.7610%;width:2.9089%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:21.7469%;top:60.4127%;width:1.1249%;height:3.0226%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:33.0256%;top:72.4028%;width:1.1249%;height:3.0226%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:27.1375%;top:76.7961%;width:1.1249%;height:3.0226%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:17.0194%;top:67.3198%;width:6.0607%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.0911%;top:72.4028%;width:6.0607%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:33.3348%;top:89.2964%;width:6.0607%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:23.7092%;top:83.7159%;width:1.1249%;height:3.0226%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-table-layer" style="left:44.2062%;top:64.4288%;width:50.0020%;height:10.6667%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑎
𝜓
</td>
<td class="ppt-table-cell">
𝑎
¬𝜓
</td>
<td class="ppt-table-cell">
¬𝑎
𝜓
</td>
<td class="ppt-table-cell">
𝑎
¬𝜓
</td>
<td class="ppt-table-cell">
¬𝑎
?𝜓
</td>
</tr>
<tr>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{}
</td>
</tr>
</table>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-033.png" alt="" />
<div class="ppt-table-layer" style="left:56.7739%;top:82.0527%;width:38.5307%;height:13.3333%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
¬𝑎
𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
¬𝑎
¬𝑏
¬ 𝑎 U 𝑏
</td>
</tr>
<tr>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑏}
</td>
<td class="ppt-table-cell">
{}
</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:2.2607%;top:61.9034%;width:8.4990%;height:2.2107%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:52.2624%;top:58.3951%;width:7.7191%;height:2.2106%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, 𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:14.0530%;top:61.6970%;width:8.4990%;height:2.2107%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:37.8291%;top:66.8143%;width:10.9879%;height:2.2107%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, ¬𝑏,¬(𝑎 U 𝑏)
</div>
</div>
<div class="ppt-text-layer" style="left:25.3763%;top:68.5122%;width:10.2080%;height:2.2107%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,¬(𝑎 U 𝑏)
</div>
</div>
<div class="ppt-table-layer" style="left:56.7739%;top:66.6840%;width:38.5307%;height:13.3333%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
¬𝑎
¬𝑏
¬𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
<td class="ppt-table-cell">
𝑎
¬𝑏
𝑎 U 𝑏
</td>
</tr>
<tr>
<td class="ppt-table-cell">
{}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
<td class="ppt-table-cell">
{𝑎}
</td>
</tr>
</table>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:5.3608%;top:11.9587%;width:92.2526%;height:32.7005%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• ניבחן ריצה מקבלת 𝐵 0 𝐴 0 𝐵 1 𝐴 1 … של האוטומט ונסמן 𝜎= 𝐴 0 𝐴 1 ….
• נניח, באינדוקציה מבנית:
  𝜎 𝑖.. ⊨ 𝜑 1 אם&quot;ם 𝜑 1 ∈ 𝐵 𝑖 𝜎 𝑖.. ⊨ 𝜑 2 אם&quot;ם 𝜑 2 ∈ 𝐵 𝑖
• נוכיח חלק מצעד האינדוקציה:
𝜎 𝑖.. ⊨ 𝜑 1 U 𝜑 2 אם&quot;ם 𝜑 1 U 𝜑 2 ∈ 𝐵 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:4.1000%;top:-5.0017%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
נכונות הבניה (עיקר ההוכחה)
</div>
</div>
<div class="ppt-text-layer" style="left:29.4566%;top:51.6441%;width:46.2669%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו את שאר המקרים הנדרשים מה-:BNF
</div>
</div>
<div class="ppt-text-layer" style="left:29.0625%;top:74.4003%;width:38.1397%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜎 𝑖.. ⊨ ¬𝜑 1 אם&quot;ם ¬𝜑 1 ∈ 𝐵 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:60.3252%;width:49.9722%;height:5.9583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜑∷= 𝑡𝑟𝑢𝑒 𝑎 𝜑 1 ∧ 𝜑 2 ¬𝜑 °𝜑 | 𝜑 1 U 𝜑 2
</div>
</div>
<div class="ppt-text-layer" style="left:26.7708%;top:80.6186%;width:45.2557%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜎 𝑖.. ⊨ 𝜑 1 ∧ 𝜑 2 אם&quot;ם 𝜑 1 ∧ 𝜑 2 ∈ 𝐵 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:28.6016%;top:86.8368%;width:40.1031%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜎 𝑖.. ⊨ °𝜑 1 אם&quot;ם °𝜑 1 ∈ 𝐵 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:32.0789%;top:68.1821%;width:32.3153%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜎 𝑖.. ⊨𝑎 אם&quot;ם 𝑎∈ 𝐵 𝑖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:4.1000%;top:-5.0017%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
נכונות הבניה (עיקר ההוכחה)
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:67.0551%;width:12.1943%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:70.3071%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:73.5307%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:76.7827%;width:12.2294%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:88.9479%;top:55.7270%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:38.6315%;top:70.8380%;width:19.4976%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
∗ (𝑛𝑜𝑡 )
</div>
</div>
<div class="ppt-text-layer" style="left:5.3608%;top:11.9587%;width:92.2526%;height:73.6007%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
• נצבע לפי ערכי האמת של 𝜑 1 , 𝜑 2 בכל מצב ונוכיח שהבניה קובעת ערך נכון ל-Until.
• נחלק למקטעים של מצבים מהצורה
• נבחן איך הבניה קובעת ערך ל-Until:
</div>
</div>
<div class="ppt-text-layer" style="left:5.3608%;top:11.9587%;width:92.2526%;height:30.5174%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• ניבחן ריצה מקבלת 𝜎= 𝐵 0 𝐵 1 … של האוטומט.
• נניח, באינדוקציה מבנית:
  𝜎 𝑖.. ⊨ 𝜑 1 אם&quot;ם 𝜑 1 ∈ 𝐵 𝑖 𝜎 𝑖.. ⊨ 𝜑 2 אם&quot;ם 𝜑 2 ∈ 𝐵 𝑖
• נוכיח חלק מצעד האינדוקציה:
𝜎 𝑖.. ⊨ 𝜑 1 U 𝜑 2 אם&quot;ם 𝜑 1 U 𝜑 2 ∈ 𝐵 𝑖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:4.1000%;top:-48.9889%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
נכונות הבניה (רעיות ההוכחה)
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:23.0681%;width:12.1943%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:26.3201%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:29.5437%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:32.7956%;width:12.2294%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:88.9479%;top:11.7398%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:5.3608%;top:-32.0275%;width:92.2526%;height:73.1519%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• ניבחן ריצה מקבלת 𝜎= 𝐵 0 𝐵 1 … של האוטומט.
• נניח, באינדוקציה מבנית:
  𝜎 𝑖.. ⊨ 𝜑 1 אם&quot;ם 𝜑 1 ∈ 𝐵 𝑖 𝜎 𝑖.. ⊨ 𝜑 2 אם&quot;ם 𝜑 2 ∈ 𝐵 𝑖
• נוכיח חלק מצעד האינדוקציה:
𝜎 𝑖.. ⊨ 𝜑 1 U 𝜑 2 אם&quot;ם 𝜑 1 U 𝜑 2 ∈ 𝐵 𝑖
• נצבע לפי ערכי האמת של 𝜑 1 , 𝜑 2 בכל מצב ונוכיח שהבניה קובעת ערך נכון ל-Until.
• נחלק למקטעים של מצבים מהצורה
• נבחן איך הבניה קובעת ערך ל-Until:
</div>
</div>
<div class="ppt-text-layer" style="left:38.6315%;top:26.6667%;width:19.4976%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
∗ (𝑛𝑜𝑡 )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:5.3608%;top:-31.8512%;width:92.2526%;height:195.6701%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
  • ע&quot;פ כללי העקביות 𝜓 2 ∈𝐵⇒ 𝜓 1 U 𝜓 2 ∈𝐵 , 𝜓 1 U 𝜓 2 ∈𝐵⇒ 𝜓 1 ∈𝐵∨ 𝜓 2 ∈𝐵 :
  • ע&quot;פ הכללים 𝜓 1 U 𝜓 2 ∈𝐵 ∧ 𝜓 2 ∉𝐵 → 𝜓 1 U 𝜓 2 ∈ 𝐵 ′ , 𝜓 1 U 𝜓 2 ∉𝐵 ∧ 𝜓 1 ∈𝐵 → 𝜓 1 U 𝜓 2 ∉ 𝐵 ′ :
  • קיבלנו שגם מקטעים המסתיימים ב- וגם המסתיימים ב- מסומנים נכון
</div>
</div>
<div class="ppt-text-layer" style="left:4.1000%;top:-48.9889%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
נכונות הבניה (רעיות ההוכחה)
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:23.0681%;width:12.1943%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:26.3201%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:29.5437%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:32.7956%;width:12.2294%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:88.9479%;top:11.7398%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:88.9479%;top:52.1428%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:6.6690%;top:60.6094%;width:10.0745%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 U 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:6.9094%;top:65.0840%;width:10.0920%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 U 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:5.3608%;top:-32.0275%;width:92.2526%;height:73.1519%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• ניבחן ריצה מקבלת 𝜎= 𝐵 0 𝐵 1 … של האוטומט.
• נניח, באינדוקציה מבנית:
  𝜎 𝑖.. ⊨ 𝜑 1 אם&quot;ם 𝜑 1 ∈ 𝐵 𝑖 𝜎 𝑖.. ⊨ 𝜑 2 אם&quot;ם 𝜑 2 ∈ 𝐵 𝑖
• נוכיח חלק מצעד האינדוקציה:
𝜎 𝑖.. ⊨ 𝜑 1 U 𝜑 2 אם&quot;ם 𝜑 1 U 𝜑 2 ∈ 𝐵 𝑖
• נצבע לפי ערכי האמת של 𝜑 1 , 𝜑 2 בכל מצב ונוכיח שהבניה קובעת ערך נכון ל-Until.
• נחלק למקטעים של מצבים מהצורה
• נבחן איך הבניה קובעת ערך ל-Until:
</div>
</div>
<div class="ppt-text-layer" style="left:88.9650%;top:78.2824%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:26.0837%;top:90.5260%;width:1.4476%;height:1.8583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#e9e5dc;opacity:1.000;border:1.50px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4f4b4b;white-space:pre-wrap;width:100%;">
?
</div>
</div>
<div class="ppt-text-layer" style="left:22.2186%;top:45.8863%;width:27.1564%;height:3.1415%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∉𝐵⇐ 𝜓 1 ∉𝐵∧ 𝜓 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:10.0101%;top:70.8408%;width:32.8024%;height:3.1415%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∈𝐵⇐ 𝜓 1 U 𝜓 2 ∈ 𝐵 ′ ∧ 𝜓 1 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:38.6315%;top:26.6667%;width:19.4976%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
∗ (𝑛𝑜𝑡 )
</div>
</div>
<div class="ppt-text-layer" style="left:43.5417%;top:70.8863%;width:32.3328%;height:3.1415%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∉𝐵 ⇐ 𝜓 1 U 𝜓 2 ∉ 𝐵 ′ ∧ 𝜓 2 ∉𝐵
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:5.3608%;top:-65.2937%;width:92.2526%;height:127.2305%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
  • ע&quot;פ כללי העקביות 𝜓 2 ∈𝐵⇒ 𝜓 1 U 𝜓 2 ∈𝐵 , 𝜓 1 U 𝜓 2 ∈𝐵⇒ 𝜓 1 ∈𝐵∨ 𝜓 2 ∈𝐵 :
  • ע&quot;פ הכללים 𝜓 1 U 𝜓 2 ∈𝐵 ∧ 𝜓 2 ∉𝐵 → 𝜓 1 U 𝜓 2 ∈ 𝐵 ′ , 𝜓 1 U 𝜓 2 ∉𝐵 ∧ 𝜓 1 ∈𝐵 → 𝜓 1 U 𝜓 2 ∉ 𝐵 ′ :
  • קיבלנו שגם מקטעים המסתיימים ב- וגם המסתיימים ב- מסומנים נכון
</div>
</div>
<div class="ppt-text-layer" style="left:4.1000%;top:-82.2542%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
נכונות הבניה (רעיות ההוכחה)
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:-10.1972%;width:12.1943%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:-6.9452%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∈𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:-3.7216%;width:12.2118%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:7.1641%;top:-0.4697%;width:12.2294%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 ∉𝐵, 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:88.9479%;top:-21.5255%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:88.9479%;top:18.8775%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:6.6690%;top:27.3441%;width:10.0745%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 U 𝜑 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:6.9094%;top:31.8187%;width:10.0920%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜑 1 U 𝜑 2 ∉𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:5.3608%;top:-65.2928%;width:92.2526%;height:73.1519%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• ניבחן ריצה מקבלת 𝜎= 𝐵 0 𝐵 1 … של האוטומט.
• נניח, באינדוקציה מבנית:
  𝜎 𝑖.. ⊨ 𝜑 1 אם&quot;ם 𝜑 1 ∈ 𝐵 𝑖 𝜎 𝑖.. ⊨ 𝜑 2 אם&quot;ם 𝜑 2 ∈ 𝐵 𝑖
• נוכיח חלק מצעד האינדוקציה:
𝜎 𝑖.. ⊨ 𝜑 1 U 𝜑 2 אם&quot;ם 𝜑 1 U 𝜑 2 ∈ 𝐵 𝑖
• נצבע לפי ערכי האמת של 𝜑 1 , 𝜑 2 בכל מצב ונוכיח שהבניה קובעת ערך נכון ל-Until.
• נחלק למקטעים של מצבים מהצורה
• נבחן איך הבניה קובעת ערך ל-Until:
</div>
</div>
<div class="ppt-text-layer" style="left:88.9650%;top:45.0171%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:26.0837%;top:57.2607%;width:1.4476%;height:1.8583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#e9e5dc;opacity:1.000;border:1.50px solid #581904;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4f4b4b;white-space:pre-wrap;width:100%;">
?
</div>
</div>
<div class="ppt-text-layer" style="left:49.6188%;top:63.8369%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
…
</div>
</div>
<div class="ppt-text-layer" style="left:5.4650%;top:-65.4326%;width:92.2526%;height:188.0408%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
  • נשאר לטפל במקטע שלא מסתיים:
  • ריצה כזאת לא תתקבל לפי התנאי: ℱ= 𝐵∈𝑄: 𝜓 1 U 𝜓 2 ∉𝐵 ∨ 𝜓 2 ∈𝐵 : 𝜓 1 U 𝜓 2 ∈𝑠𝑢𝑏 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:43.0864%;top:85.5407%;width:21.1104%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#d34817;white-space:pre-wrap;width:100%;">
מ.ש.ל
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-039.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:5.5556%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
GNBA לנוסחת LTL 𝜑
כללי היסק למחיקה
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
<div class="ppt-text-layer" style="left:65.5768%;top:28.7783%;width:23.4707%;height:9.9294%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝜓∉𝐵∧𝜓∈𝐵’ 𝐵↛ 𝐵 ′
</div>
</div>
<div class="ppt-text-layer" style="left:39.2056%;top:60.9610%;width:46.9597%;height:10.0088%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∉𝐵 ∧ 𝜓 1 ∈𝐵∧ 𝜓 1 U 𝜓 2 ∈ 𝐵 ′ 𝐵↛ 𝐵 ′
</div>
</div>
<div class="ppt-text-layer" style="left:39.2056%;top:44.0919%;width:47.4611%;height:10.0088%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∈𝐵 ∧ 𝜓 2 ∉𝐵∧ 𝜓 1 U 𝜓 2 ∉ 𝐵 ′ 𝐵↛ 𝐵 ′
</div>
</div>
<div class="ppt-text-layer" style="left:48.3389%;top:81.1111%;width:28.8526%;height:11.1196%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∈𝐵 ∧ 𝜓 2 ∉𝐵 𝐵∉ 𝐹 𝜓 1 U 𝜓 2
</div>
</div>
<div class="ppt-text-layer" style="left:15.9743%;top:39.2243%;width:15.6058%;height:17.5026%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
יחס
המעברים
פוסל ניחושים
לא מוצלחים
</div>
</div>
<div class="ppt-text-layer" style="left:15.0231%;top:79.9396%;width:17.5082%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
תנאי הקבלה פוסל הבטחות שלא מתקיימות
</div>
</div>
<div class="ppt-text-layer" style="left:40.0264%;top:28.9860%;width:23.1243%;height:9.9294%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝜓∈𝐵∧𝜓∉𝐵’ 𝐵↛ 𝐵 ′
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-040.png" alt="" />
<div class="ppt-text-layer" style="left:6.0471%;top:-4.3485%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
40
</div>
</div>
<div class="ppt-text-layer" style="left:27.8313%;top:18.7569%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.6646%;top:32.6230%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,¬ 𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.8270%;top:70.0000%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬ 𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:25.2447%;top:82.2985%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:5.1906%;top:48.8780%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.5594%;top:47.9866%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏, 𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:26.2731%;top:62.5149%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:30.2138%;top:36.5541%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.9516%;top:87.4784%;width:27.9301%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב א&#x27;: מציירים את כל צירופי תת הנוסחאות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-041.png" alt="" />
<div class="ppt-text-layer" style="left:6.0471%;top:-4.3485%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U𝑏
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
<div class="ppt-text-layer" style="left:27.8313%;top:18.7569%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.6646%;top:32.6230%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,¬ 𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.8270%;top:70.0000%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬ 𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:25.2447%;top:82.2985%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:5.1906%;top:48.8780%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.5594%;top:47.9866%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏, 𝑎 U 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:26.2731%;top:62.5149%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:30.2138%;top:36.5541%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:61.2192%;top:56.9946%;width:25.5137%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#c00000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝜓 1 U 𝜓 2 ∈𝐵⇒ 𝜓 1 ∈𝐵∨ 𝜓 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:28.6278%;top:45.4622%;width:20.8333%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#c00000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝜓 2 ∈𝐵⇒ 𝜓 1 U 𝜓 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:26.9903%;top:71.1169%;width:20.8333%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;background:#c00000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝜓 2 ∈𝐵⇒ 𝜓 1 U 𝜓 2 ∈𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:58.9516%;top:87.4784%;width:27.9301%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב ב&#x27;: מוחקים את אלה שאינן עקביים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-042.png" alt="" />
<div class="ppt-text-layer" style="left:6.0471%;top:-4.3485%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U𝑏
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
<div class="ppt-text-layer" style="left:27.8313%;top:18.7569%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.6646%;top:32.6230%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.8270%;top:70.0000%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:25.2447%;top:82.2985%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:5.1906%;top:48.8780%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:18.6133%;top:32.6274%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:5.3313%;top:59.7231%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:22.9497%;top:61.7958%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:17.5164%;top:67.1479%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:24.0030%;top:90.3118%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:48.6374%;top:80.4696%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:42.7607%;top:64.1675%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:29.7198%;top:55.5453%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:70.9935%;top:24.0727%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:72.0986%;top:49.3222%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:48.5471%;top:31.6349%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:61.2640%;top:50.6269%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:41.3939%;top:12.2222%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:35.4215%;top:33.6357%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:51.0180%;top:23.7160%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:24.2253%;top:40.0173%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:71.6306%;top:82.3686%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:65.0001%;top:59.1509%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:45.9422%;top:48.0420%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:41.0023%;top:41.0138%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:46.1646%;top:87.4784%;width:40.7171%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב ג&#x27;: מחברים לפי כללי הפריסה. האות נקבעת ע&quot;פ ההשמות לפסוקים.
</div>
</div>
<div class="ppt-text-layer" style="left:53.1738%;top:11.4731%;width:45.0079%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#c00000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
  𝜓 1 U 𝜓 2 ∈𝐵 ∧ 𝜓 2 ∉𝐵 → 𝜓 1 U 𝜓 2 ∈ 𝐵 ′
  𝜓 1 U 𝜓 2 ∉𝐵 ∧ 𝜓 1 ∈𝐵 → 𝜓 1 U 𝜓 2 ∉ 𝐵 ′
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-043.png" alt="" />
<div class="ppt-text-layer" style="left:6.0471%;top:-4.3485%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U𝑏
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
<div class="ppt-text-layer" style="left:27.8313%;top:18.7569%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.6646%;top:32.6230%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.8270%;top:70.0000%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:25.2447%;top:82.2985%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:5.1906%;top:48.8780%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:18.6133%;top:32.6274%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:5.3313%;top:59.7231%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:22.9497%;top:61.7958%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:17.5164%;top:67.1479%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:24.0030%;top:90.3118%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:48.6374%;top:80.4696%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:42.7607%;top:64.1675%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:29.7198%;top:55.5453%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:70.9935%;top:24.0727%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:72.0986%;top:49.3222%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:41.0023%;top:41.0138%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:48.5471%;top:31.6349%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:61.2640%;top:50.6269%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:41.3939%;top:12.2222%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:35.4215%;top:33.6357%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:51.0180%;top:23.7160%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:24.2253%;top:40.0173%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:71.6306%;top:82.3686%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:65.0001%;top:59.1509%;width:6.1483%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎}
</div>
</div>
<div class="ppt-text-layer" style="left:45.9422%;top:48.0420%;width:8.5178%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎,𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:46.1646%;top:87.4784%;width:40.7171%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב ד&#x27;: קובעים מצבים מקבלים ע&quot;פ &quot;הבטחות צריך לקיים&quot;.
</div>
</div>
<div class="ppt-text-layer" style="left:54.4600%;top:14.1220%;width:42.5369%;height:5.7463%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#c00000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝐵∉ 𝐹 𝜓 1 U 𝜓 2 ⇔ 𝜓 1 U 𝜓 2 ∈𝐵∧ 𝜓 2 ∉𝐵
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-044.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דרך מצומצמת לכתוב את אותו האוטומ
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
<div class="ppt-text-layer" style="left:36.6667%;top:20.1449%;width:18.3333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:67.5000%;top:34.0110%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:67.6623%;top:70.9492%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:34.0801%;top:83.6866%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:14.0260%;top:50.2660%;width:20.8333%;height:8.5357%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎U𝑏
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-045.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U𝑏
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
<div class="ppt-text-layer" style="left:40.7009%;top:22.5102%;width:13.5358%;height:6.6264%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.4657%;top:33.2747%;width:15.3816%;height:6.6264%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.5856%;top:61.9504%;width:15.3816%;height:6.6264%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬ 𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.7912%;top:71.8385%;width:15.3816%;height:6.6264%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎, 𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:23.9849%;top:45.8936%;width:15.3816%;height:6.6264%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑏,𝑎U𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:18.0717%;top:88.8450%;width:64.4672%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
איך יראה אוטומט לפסוק 𝑎∧¬𝑏∧¬ 𝑎U𝑏 ?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-046.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
NBA עבור הנוסחה 𝑎
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
<div class="ppt-text-layer" style="left:20.8333%;top:31.4574%;width:18.3333%;height:14.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎,𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:62.5000%;top:31.4430%;width:18.3333%;height:14.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎, ¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:64.4444%;width:18.3333%;height:14.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎,𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:62.5000%;top:64.4444%;width:18.3333%;height:14.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff99;opacity:1.000;border:5.00px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎, ¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:23.5182%;top:23.4450%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.9150%;top:34.1512%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:72.1689%;top:51.2314%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:57.9277%;top:59.0590%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:40.3063%;top:44.0775%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.8786%;top:54.7387%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:81.3311%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:49.6357%;top:71.3881%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-047.png" alt="" />
<div class="ppt-text-layer" style="left:6.8750%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U (𝑏U¬𝑎) 𝜓 𝜑
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
<div class="ppt-text-layer" style="left:25.0000%;top:92.0581%;width:54.1875%;height:4.5393%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
ℱ= 𝑠 1 , 𝑠 2 , 𝑠 3 , 𝑠 4 , 𝑠 5 , 𝑠 6 , 𝑠 1 , 𝑠 2 , 𝑠 4 , 𝑠 6 , 𝑠 7
</div>
</div>
<div class="ppt-text-layer" style="left:25.1709%;top:86.6667%;width:46.1091%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
המצבים המסומנים הם אלה שאינם מקבלים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-048.png" alt="" />
<div class="ppt-text-layer" style="left:7.9167%;top:2.6512%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
GNBA עבור הנוסחה 𝑎U (𝑏U¬𝑎) 𝜓 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
48
</div>
</div>
<div class="ppt-text-layer" style="left:11.6667%;top:39.5446%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffd9d9;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝜑,𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:28.3333%;top:57.1302%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ccecff;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,𝜑,¬𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:28.3333%;top:78.5691%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,𝑏,¬𝜑,¬𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:41.6667%;top:39.5446%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,𝑏,𝜑,𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:71.6667%;top:39.5446%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎,¬𝑏,𝜑,𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:58.2917%;top:57.3492%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ccecff;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏, 𝜑,¬𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:58.2917%;top:78.4181%;width:19.1667%;height:6.4971%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎,¬𝑏,¬𝜑,¬𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:18.0239%;width:46.1091%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
המצבים המסומנים הם אלה שאינם מקבלים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-049.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:88.1776%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תוצאה עיקרית
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:28.0958%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.1869%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
49
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:28.4889%;width:95.8333%;height:52.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לכל נוסחת LTL  (מעל 𝐴𝑃) קיים GNBA 𝒢 𝜑 מעל 2𝐴𝑃 כך ש:
• 𝑊𝑜𝑟𝑑𝑠(𝜑) = ℒ 𝜔 ( 𝒢 𝜑 )
• ניתן לבנות את 𝒢 𝜑 בזמן וזיכרון 𝒪 2 𝜑
• מספר הקבוצות המקבלות של 𝒢 𝜑 חסום מלמעלה ע&quot;י 𝜑
</div>
</div>
<div class="ppt-text-layer" style="left:5.6391%;top:19.3008%;width:46.2885%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
[Vardi, Wolper &amp; Sistla 1986]
</div>
</div>
<div class="ppt-text-layer" style="left:14.2679%;top:88.8889%;width:62.1379%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
⇐ כל נוסחת LTL מבטאת תכונה 𝜔-רגולרית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-050.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
האם NBA יכולים לבטא יותר מ-LTL?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
50
</div>
</div>
<div class="ppt-text-layer" style="left:3.6512%;top:19.9867%;width:91.6667%;height:37.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נבחן את התכונה:
𝑃= 𝜎: ∀𝑖≥0 . 𝑎∈𝜎 2𝑖
קיים NBA 𝒜 כך ש ℒ 𝜔 (𝒜)=𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:25.7761%;top:85.5556%;width:48.4477%;height:7.3891%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
האם ניתן לבטא תכונה זאת ב-LTL?
</div>
</div>
<div class="ppt-text-layer" style="left:46.4186%;top:74.5044%;width:4.1674%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:44.6775%;top:56.4165%;width:7.6497%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-051.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות חסרות ספירה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
51
</div>
</div>
<div class="ppt-text-layer" style="left:3.0993%;top:53.4118%;width:93.8013%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#002060;opacity:0.500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
דוגמה: התכונה שראינו בשקף הקודם היא לא חסרת ספירה.
הוכחה: נבחר 𝑣=𝜀, 𝑤= 𝑎 , 𝛼={} 𝑎 𝜔 ואז לכל 𝑛 זוגי 𝑣 𝑤 𝑛 𝛼∈𝐿 אבל 𝑣 𝑤 𝑛+1 𝛼∉𝐿
</div>
</div>
<div class="ppt-text-layer" style="left:9.7459%;top:69.0323%;width:87.3749%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#002060;opacity:0.500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
דוגמה נוספת: התכונה {}{} ∗ 𝑝 𝜔 היא לא חסרת ספירה.
הוכחה: נבחר 𝑣=𝜀, 𝑤={}, 𝛼= 𝑝 𝜔 ואז לכל 𝑛 זוגי 𝑣 𝑤 𝑛 𝛼∈𝐿 אבל 𝑣 𝑤 𝑛+1 𝛼∉𝐿
</div>
</div>
<div class="ppt-text-layer" style="left:3.3796%;top:19.3668%;width:93.8013%;height:13.4841%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ccecff;opacity:0.500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000066;white-space:pre-wrap;width:100%;">
𝑃⊆ 2 𝐴𝑃 𝜔 היא חסרת ספירה אם קיים 𝑛 0 כך שלכל 𝑛&gt; 𝑛 0 ולכל 𝑣,𝑤∈ 2 𝐴𝑃 ∗
ו- 𝛼∈ 2 𝐴𝑃 𝜔 מתקיים:
𝑣 𝑤 𝑛 𝛼∈𝑃 ⇔ 𝑣 𝑤 𝑛+1 𝛼∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:3.1246%;top:36.5262%;width:94.1667%;height:13.4738%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffd9d9;opacity:0.500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑃⊆ 2 𝐴𝑃 𝜔 היא לא חסרת ספירה אם קיימים אינסוף𝑛 -ים ו-𝑣,𝑤∈ 2 𝐴𝑃 ∗ ו- 𝛼∈ 2 𝐴𝑃 𝜔 עבורם מתקיים:
𝑣 𝑤 𝑛 𝛼∈𝑃 ⇎ 𝑣 𝑤 𝑛+1 𝛼∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:3.6585%;top:89.1375%;width:93.6327%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffd9d9;opacity:0.500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
משפט: כל תכונה הניתנת לתיאור ב-LTL היא חסרת ספירה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-052.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
52
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:6.1962%;width:59.7837%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
משפט: כל תכונה הניתנת לתיאור ב-LTL היא חסרת ספירה
</div>
</div>
<div class="ppt-text-layer" style="left:60.7969%;top:13.3333%;width:39.6403%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה באינדוקציה על מבנה הנוסחה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-053.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
53
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:6.1962%;width:59.7837%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
משפט: כל תכונה הניתנת לתיאור ב-LTL היא חסרת ספירה
</div>
</div>
<div class="ppt-text-layer" style="left:60.7969%;top:13.3333%;width:39.6403%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה באינדוקציה על מבנה הנוסחה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-054.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
54
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:6.1962%;width:59.7837%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
משפט: כל תכונה הניתנת לתיאור ב-LTL היא חסרת ספירה
</div>
</div>
<div class="ppt-text-layer" style="left:60.7969%;top:13.3333%;width:39.6403%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה באינדוקציה על מבנה הנוסחה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-055.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
55
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:6.1962%;width:59.7837%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
משפט: כל תכונה הניתנת לתיאור ב-LTL היא חסרת ספירה
</div>
</div>
<div class="ppt-text-layer" style="left:60.7969%;top:13.3333%;width:39.6403%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה באינדוקציה על מבנה הנוסחה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-056.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מסקנה: NBA יכולים לבטא יותר מ-LTL
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
56
</div>
</div>
<div class="ppt-text-layer" style="left:3.6512%;top:19.9867%;width:91.6667%;height:37.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לא קיימת נוסחת LTL 𝜑 המקיימת 𝑊𝑜𝑟𝑑𝑠(𝜑)=𝑃 עבור התכונה:
𝑃= 𝜎: ∀𝑖≥0 . 𝑎∈𝜎 2𝑖
אבל קיים NBA 𝒜 כך ש ℒ 𝜔 (𝒜)=𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:9.5913%;top:83.3333%;width:70.5924%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
⇐ קיימות תכונות 𝜔-רגולרית שלא ניתן לבטא ב-LTL
</div>
</div>
<div class="ppt-text-layer" style="left:46.4186%;top:74.5044%;width:4.1674%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:44.6775%;top:56.4165%;width:7.6497%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-057.png" alt="" />
<div class="ppt-text-layer" style="left:9.0657%;top:-1.1053%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
Quantified Propositional Temporal Logic (QPTL)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
57
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:17.2173%;width:40.4818%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
נוסחאת QPTL מוגדרת על ידי התחביר:
</div>
</div>
<div class="ppt-text-layer" style="left:5.5384%;top:43.0998%;width:92.4433%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לקשרים בנוסחת QPTL אותה המשמעות כמו לקשרים ב-LTL בתוספת הקשר ∃ שמשמעותו:
</div>
</div>
<div class="ppt-text-layer" style="left:19.4448%;top:27.3854%;width:61.1105%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜓 ≔𝑝 ¬𝜓 𝜓 1 ∧ 𝜓 2 𝜓 𝜓 1 U 𝜓 2 | ∃𝑝. 𝜓
</div>
</div>
<div class="ppt-text-layer" style="left:18.4692%;top:81.5283%;width:62.6872%;height:6.4120%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
∃𝑡𝑐𝑘. 𝑡𝑐𝑘∧ 𝑡𝑐𝑘↔¬𝑡𝑐𝑘 ∧ 𝑡𝑐𝑘→𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.8609%;top:69.0167%;width:77.1208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דוגמא: ניתן לתאר את התכונה שראינו בשקף הקודם באמצעות נוסאת QPTL:
</div>
</div>
<div class="ppt-text-layer" style="left:84.3746%;top:92.8964%;width:4.1674%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:85.0983%;top:79.7566%;width:4.5439%;height:3.1989%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:10.5854%;top:53.2505%;width:83.4803%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝛼⊨∃𝑝.𝜓 ⇔ ∃ 𝛼 ′ ∈ {}, 𝑝 𝜔 . 𝛼 ′′ ⊨𝜓, ∀𝑖. 𝛼 ′′ 𝑖 =𝛼 𝑖 U 𝛼 ′ 𝑖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-058.png" alt="" />
<div class="ppt-text-layer" style="left:9.0657%;top:-1.1053%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
Quantified Propositional Temporal Logic (QPTL)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
58
</div>
</div>
<div class="ppt-text-layer" style="left:10.9415%;top:33.6227%;width:62.6872%;height:6.4120%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
∃𝑡𝑐𝑘. 𝑡𝑐𝑘∧ 𝑡𝑐𝑘↔¬𝑡𝑐𝑘 ∧ 𝑡𝑐𝑘→𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:13.3333%;top:21.1111%;width:77.1208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דוגמא: ניתן לתאר את התכונה שראינו בשקף הקודם באמצעות נוסאת QPTL:
</div>
</div>
<div class="ppt-text-layer" style="left:10.9415%;top:52.9062%;width:75.8923%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
שאלה: האם ניתן לתאר כך כל שפה 𝜔-רגולרית?
</div>
</div>
<div class="ppt-text-layer" style="left:82.8863%;top:45.0196%;width:2.4754%;height:3.1989%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:81.8521%;top:31.8510%;width:4.5439%;height:3.1989%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-059.png" alt="" />
<div class="ppt-text-layer" style="left:9.0657%;top:-1.1053%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
Quantified Propositional Temporal Logic (QPTL)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
59
</div>
</div>
<div class="ppt-text-layer" style="left:3.7928%;top:19.1003%;width:94.4964%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
משפט: ניתן לתאר כל תכונה 𝜔-רגולרית באמצעות QPTL
</div>
</div>
<div class="ppt-text-layer" style="left:42.3315%;top:29.4750%;width:56.0841%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הוכחה: נוסחה לתרגום אוטומט Büchi לנוסחאת QPTL
</div>
</div>
<div class="ppt-text-layer" style="left:40.0000%;top:60.8418%;width:14.1840%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 ′ ∈𝛿(𝑞,𝐴)
</div>
</div>
<div class="ppt-text-layer" style="left:7.0202%;top:54.8420%;width:15.0000%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
נמצאים במצב אחד בדיוק
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:40.2902%;width:29.1667%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
מכבדים את יחס המעברים
</div>
</div>
<div class="ppt-text-layer" style="left:63.9899%;top:85.6908%;width:29.1667%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
עוברים אינסוף פעמים במצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:5.4175%;top:89.6919%;width:7.2962%;height:8.7513%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו
נכונות
הנוסחה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/23-ltl-model-checking/slide-060.png" alt="" />
<div class="ppt-text-layer" style="left:9.0657%;top:-4.4624%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
איך נבדוק תחת הנחות הוגנות?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
60
</div>
</div>
<div class="ppt-text-layer" style="left:5.9343%;top:24.0038%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1
</div>
</div>
<div class="ppt-text-layer" style="left:27.6010%;top:24.0038%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 2
</div>
</div>
<div class="ppt-text-layer" style="left:48.4343%;top:24.0038%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 3
</div>
</div>
<div class="ppt-text-layer" style="left:33.7580%;top:32.8001%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:56.3520%;top:32.9853%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:12.8602%;top:32.4223%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:19.9109%;top:21.3111%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:41.3520%;top:23.7035%;width:4.1821%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
<div class="ppt-text-layer" style="left:30.1627%;top:44.1769%;width:4.1821%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
<div class="ppt-text-layer" style="left:56.3520%;top:14.2666%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:19.4863%;top:26.9055%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:37.5305%;top:64.1817%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffc000;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1
</div>
</div>
<div class="ppt-text-layer" style="left:59.1971%;top:64.1817%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffc000;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 2
</div>
</div>
<div class="ppt-text-layer" style="left:80.0305%;top:64.1817%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffc000;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 3
</div>
</div>
<div class="ppt-text-layer" style="left:65.6139%;top:72.8831%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:87.9482%;top:73.1632%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:45.1268%;top:72.7438%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:51.5070%;top:61.4890%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:72.9482%;top:63.8814%;width:4.1821%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
<div class="ppt-text-layer" style="left:56.8043%;top:84.9628%;width:4.1821%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
<div class="ppt-text-layer" style="left:87.9482%;top:54.4444%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:51.0824%;top:67.0834%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:24.1829%;top:63.8067%;width:10.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffc000;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1 ′
</div>
</div>
<div class="ppt-text-layer" style="left:30.7661%;top:72.7096%;width:4.6842%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:46.8437%;top:55.6809%;width:4.1646%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
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
