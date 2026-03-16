---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 14-property-closure
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
סְגוֹר של תכונה
Property Closure
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
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: תכונות זמן לינארי
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:23.3333%;width:88.3333%;height:64.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 היא קבוצה של מילים באורך אין-סופי שהאותיות שלהן הן קבוצות של פסוקים אטומיים:
𝑃⊆ 2 𝐴𝑃 𝜔
אומרים שמערכת מקיימת תכונה אם כל רצפי העקבות שהמערכת משאירה, בכל הריצות שלה, נמצאות בקבוצה:
𝑇𝑆⊨𝑃 ⇔ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:21.3863%;top:84.4444%;width:22.6812%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
הסימון שלנו לאמירה
&quot;𝑇𝑆 מקיימת את 𝑃&quot;
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
3
</div>
</div>
<div class="ppt-text-layer" style="left:25.9317%;top:31.4630%;width:9.4946%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑇𝑆=
</div>
</div>
<div class="ppt-text-layer" style="left:17.6582%;top:55.9314%;width:66.3503%;height:9.6536%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑃 1 ={𝜎∈ 2 𝐴𝑃 𝜔 : ∃ ∞ 𝑖 . 𝜎[𝑖]⊨𝑞 }
</div>
</div>
<div class="ppt-text-layer" style="left:38.7129%;top:41.0468%;width:3.5885%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:54.8270%;top:40.9985%;width:4.9907%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞,𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:54.8381%;top:26.8417%;width:3.5947%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞}
</div>
</div>
<div class="ppt-text-layer" style="left:17.6582%;top:67.8288%;width:66.3503%;height:9.6536%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#336600;white-space:pre-wrap;width:100%;">
𝑃 2 ={𝜎∈ 2 𝐴𝑃 𝜔 : ∃ ∞ 𝑖 . 𝜎[𝑖]⊨𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:17.6412%;top:84.5834%;width:23.4821%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;background:#009900;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑇𝑆⊨ 𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:58.1845%;top:84.5834%;width:23.4821%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ff0000;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆⊭ 𝑃 1
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
4
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:15.9722%;width:88.3333%;height:78.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 נקראת תכונת בטיחות אם לכל 𝜎 שאינה מקיימת את התכונה יש רֵישָׁא סופית 𝜌 כך שכל 𝜎 ′ ש-𝜌 היא רֵישָׁא שלה לא מקיימת את התכונה.
• התכונה
{𝜎∈ 2 𝐴𝑃 𝜔 :∀𝑖 . 𝜎 𝑖 ⊨𝑝 ⇒ 𝜎 𝑖+3 ⊨𝑝∨𝑞 }
  היא תכונת בטיחות כי בכל מילה שאינה מקיימת את התכונה יש אות𝜎[𝑖] המכילה את 𝑝 והאות 𝜎[𝑖+3], שלושה מקומות אחריה, אינה מכילה לא את 𝑝 ולא את 𝑞. לכן ניתן לבחור רישא סופית 𝜌=𝜎 ..(𝑖+3) כך שכל מילה אינסופית ש-𝜌 היא רישא שלה לא תקיים את התכונה.
• התכונה
𝜎∈ 2 𝐴𝑃 𝜔 :∀𝑖 . 𝜎[𝑖]⊨𝑝 ⇒∃𝑗&gt;𝑖 . 𝜎[𝑗]⊨𝑞
איננה תכונת בטיחות כי כל רישה סופית של המילה𝜎= 𝑝 { } 𝜔 , למשל, שאיננה מקיימת את התכונה, ניתן להמשיך למילה אינסופית שתקיים את התכונה.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
5
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונת בטיחות רגולרית
</div>
</div>
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
<div class="ppt-text-layer" style="left:13.3333%;top:18.8889%;width:77.6198%;height:14.3789%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
  &quot;אור אדום נדלק רק אחרי אור צהוב&quot;
    {𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎 𝑖 ⊨𝑟𝑒𝑑⇒ 𝑖&gt;0 ∧𝜎 𝑖−1 ⊨𝑦𝑒𝑙𝑙𝑜𝑤 }
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:38.8889%;width:88.3333%;height:17.5026%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לפעמים ניתן לתאר את הרישות הרעות כשפה רגולרית. לדוגמה, קבוצת הרישות הרעות המינימאליות עבור התכונה למעלה היא השפה המתקבלת על ידי האוטומט:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-007.png" alt="" />
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
7
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
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-008.png" alt="" />
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
8
</div>
</div>
<div class="ppt-text-layer" style="left:33.9657%;top:31.5110%;width:63.7976%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
כל תכונת שמורה היא תכונת בטיחות רֵגוּלָרִית :
</div>
</div>
<div class="ppt-text-layer" style="left:14.5444%;top:33.3333%;width:6.3685%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝜙
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:25.5555%;width:4.4752%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜙
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:16.5468%;width:90.0935%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
תכונה שקבוצת הרישות הרעות המינימליות שלה היא שפה רֵגוּלָרִית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-009.png" alt="" />
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
9
</div>
</div>
<div class="ppt-text-layer" style="left:1.5816%;top:16.6667%;width:97.5850%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• דרישה טבעית :
&quot;מספר המטבעות שהוכנסו הוא לפחות מספר המשקאות שניתנו&quot;
• לכל 𝑖≥0:
0≤𝑗≤𝑖 :𝑑𝑟𝑖𝑛𝑘∈𝜎[𝑗] ≤ 0≤𝑗≤𝑖 :𝑝𝑎𝑦∈𝜎[𝑗]
• רישות רעות:
∅ {𝑝𝑎𝑦}{𝑑𝑟𝑖𝑛𝑘}{𝑑𝑟𝑖𝑛𝑘}
∅ 𝑝𝑎𝑦 𝑑𝑟𝑖𝑛𝑘 ∅{𝑝𝑎𝑦}{𝑑𝑟𝑖𝑛𝑘}{𝑑𝑟𝑖𝑛𝑘}
• כל הגרסאות שהצגנו למכונות מכירת השתייה עומדות בדרישה
• זאת דוגמה לתכונת בטיחות
שלא ניתן לבטא את הרישות הרעות שלה כשפה רֵגוּלָרִית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות בטיחות ורצפי עקבות סופיים
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
<div class="ppt-text-layer" style="left:0.0000%;top:34.4444%;width:97.5000%;height:31.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
משפט:
עבור מערכת מעברים 𝑇𝑆 בלי מצבים סופניים ותכונת בטיחות 𝑃:
𝑇𝑆⊨𝑃 ⇔𝑇𝑟𝑎𝑐𝑒 𝑠 fin 𝑇𝑆 ∩𝐵𝑎𝑑𝑃𝑟𝑒𝑓 𝑃 =∅
</div>
</div>
<div class="ppt-text-layer" style="left:15.4167%;top:75.0574%;width:42.5000%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#422e2e;white-space:pre-wrap;width:100%;">
קבוצת הרישות הסופיות של מילים ב-𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:7.6112%;top:-4.6090%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחת כיוון ראשון
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
11
</div>
</div>
<div class="ppt-text-layer" style="left:44.7817%;top:15.7099%;width:14.2987%;height:5.7099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:justify;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆⊭ 𝑃 𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:39.4920%;top:32.2222%;width:24.8781%;height:5.7099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:justify;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊈ 𝑃 𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:49.7172%;top:23.4014%;width:4.3161%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
⇓
</div>
</div>
<div class="ppt-text-layer" style="left:27.5457%;top:23.4014%;width:22.5655%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
לפי הגדרת הסימן⊭
</div>
</div>
<div class="ppt-text-layer" style="left:29.2443%;top:50.0671%;width:44.8112%;height:5.7099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:justify;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
∃𝜎∈𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 such that 𝜎∉ 𝑃 𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:49.7172%;top:39.9138%;width:4.3161%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
⇓
</div>
</div>
<div class="ppt-text-layer" style="left:23.0053%;top:39.9138%;width:27.1059%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
לפי הגדרת הכלת קבוצות
</div>
</div>
<div class="ppt-text-layer" style="left:23.0756%;top:70.4176%;width:57.7109%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:justify;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
∃𝜌∈𝑇𝑟𝑎𝑐𝑒 𝑠 fin 𝑇𝑆 such that 𝜌∈ 𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃 𝑠𝑎𝑓𝑒 )
</div>
</div>
<div class="ppt-text-layer" style="left:49.4793%;top:60.3644%;width:4.6946%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
⇓
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:59.0114%;width:46.9793%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כי יש ל-𝜎 רישא רעה ובגלל שכל רישא סופית של סדרת עקבות היא סדרת עקבות סופית
</div>
</div>
<div class="ppt-text-layer" style="left:49.7172%;top:78.1091%;width:4.3161%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
⇓
</div>
</div>
<div class="ppt-text-layer" style="left:22.9351%;top:78.1091%;width:27.1760%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
לפי הגדרת חיתוך קבוצות
</div>
</div>
<div class="ppt-text-layer" style="left:30.0486%;top:87.6235%;width:43.7649%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:justify;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒 𝑠 fin 𝑇𝑆 ∩ 𝐵𝑎𝑑𝑃𝑟𝑒𝑓(𝑃 𝑠𝑎𝑓𝑒 )≠∅
</div>
</div>
<div class="ppt-text-layer" style="left:61.6234%;top:59.0114%;width:28.7357%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
כאן השתמשנו בנתון שמדובר בתכונת בטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:7.6112%;top:-2.6645%;width:87.2566%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחת הכיוון שני
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:101.9444%;width:27.8024%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.1327%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
12
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:20.8012%;width:96.6667%;height:68.8090%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
  נניח ש- 𝑇𝑟𝑎𝑐𝑒 𝑠 fin 𝑇𝑆 ∩𝐵𝑎𝑑𝑃𝑟𝑒𝑓 𝑃 safe ≠∅
  ניקח 𝜌 כלשהי ב-𝑇𝑟𝑎𝑐𝑒 𝑠 fin 𝑇𝑆 ∩𝐵𝑎𝑑𝑃𝑟𝑒𝑓 𝑃 safe
  בגלל שאין מצבים סופניים, ניתן להמשיך כל ריצה סופית לריצה אינסופית
  תהי 𝜎 עקבות ריצה של 𝑇𝑆 שהתחלתה היא הריצה הסופית שעקבותיה הן 𝜌
  ע&quot;פ הגדרת 𝐵𝑎𝑑𝑃𝑟𝑒𝑓 𝑃 safe , מקבלים ש 𝜎∉ 𝑃 safe
  קיבלנו שקיימת ריצה של 𝑇𝑆 שעקבותיה אינן ב 𝑃 safe ולכן 𝑇𝑆⊭ 𝑃 safe
</div>
</div>
<div class="ppt-text-layer" style="left:19.2066%;top:52.7374%;width:52.0818%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כאן השתמשנו בנתון שאין מצבים סופניים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:7.9167%;top:0.0000%;width:87.5000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: שקילות עקבות ותכונות זמן ליניארי
</div>
</div>
<div class="ppt-text-layer" style="left:72.0833%;top:105.5556%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
13
</div>
</div>
<div class="ppt-text-layer" style="left:9.1667%;top:26.6667%;width:85.0000%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עבור מערכות מעברים 𝑇𝑆 ו 𝑇𝑆’ ללא מצבים סופניים:
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:36.6667%;width:89.1667%;height:21.9904%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
אם ורק אם
לכל תכונת זמן ליניארי 𝑃 מתקיים: 𝑇𝑆’⊨𝑃 גורר 𝑇𝑆⊨𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:70.0000%;width:89.1667%;height:21.9904%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆) = 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
אם ורק אם
𝑇𝑆’ ו 𝑇𝑆 מקיימות את אותן התכונות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הכלת עקבות סופיים ותכונות בטיחות
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
<div class="ppt-text-layer" style="left:10.0000%;top:21.1111%;width:85.0000%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עבור מערכות מעברים 𝑇𝑆 ו 𝑇𝑆’ ללא מצבים סופניים:
</div>
</div>
<div class="ppt-text-layer" style="left:6.8349%;top:34.0788%;width:86.3302%;height:22.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒 𝑠 fin (𝑇𝑆)⊆ 𝑇𝑟𝑎𝑐𝑒 𝑠 fin (𝑇𝑆’)
אם ורק אם
לכל תכונת בטיחות 𝑃safe מתקיים: 𝑇𝑆’⊨ 𝑃safe גורר 𝑇𝑆⊨𝑃safe
</div>
</div>
<div class="ppt-text-layer" style="left:6.8349%;top:67.3523%;width:86.3302%;height:22.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒 𝑠 fin (𝑇𝑆) = 𝑇𝑟𝑎𝑐𝑒 𝑠 fin (𝑇𝑆’)
אם ורק אם
𝑇𝑆’ ו 𝑇𝑆 מקיימות את אותן תכונות הבטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:4.8333%;top:-4.8074%;width:91.5517%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: הכלת עקבות  הכלת עקבות סופיים
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
<div class="ppt-text-layer" style="left:56.2562%;top:56.7468%;width:6.1070%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:69.9349%;width:48.3333%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆) ⊈ 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:85.5581%;width:47.3650%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠fin 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠fin(𝑇𝑆’)
</div>
</div>
<div class="ppt-text-layer" style="left:44.7693%;top:40.1173%;width:6.1070%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:69.4378%;top:71.0880%;width:6.1070%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:83.4048%;top:85.8203%;width:6.1070%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑏}
</div>
</div>
<div class="ppt-text-layer" style="left:15.3387%;top:33.2401%;width:5.5923%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:75.1293%;top:17.2915%;width:6.1918%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑇𝑆′
</div>
</div>
<div class="ppt-text-layer" style="left:19.2678%;top:25.5556%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:56.2938%;top:42.2192%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:69.2497%;top:43.0192%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:69.4993%;top:57.0536%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:83.2171%;top:43.6275%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:83.4048%;top:57.0668%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:83.4048%;top:71.7765%;width:4.6667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:83.4343%;top:34.0440%;width:9.8990%;height:4.0391%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
עקבות סופיים / עקבות אינסופיים
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
<div class="ppt-text-layer" style="left:41.6667%;top:27.7778%;width:55.0000%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עבור 𝑇𝑆 בלי מצבים סופניים
ו- 𝑇𝑆’ בעלת מספר סופי של מצבים:
</div>
</div>
<div class="ppt-text-layer" style="left:23.6104%;top:50.6155%;width:50.5808%;height:28.8709%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
אם ורק אם
𝑇𝑟𝑎𝑐𝑒 𝑠 fin 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒 𝑠 fin (𝑇𝑆’)
</div>
</div>
<div class="ppt-text-layer" style="left:2.0842%;top:85.5673%;width:95.8333%;height:9.7695%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#f3f7bb;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו או הפריכו: קיימת תכונת זמן לינארי שמערכת 𝑇 𝑆 ′ מקיימת ומערכת 𝑇𝑆 לא מקיימת אם ורק אם קיימת תכונת בטיחות שמערכת 𝑇 𝑆 ′ מקיימת ומערכת 𝑇𝑆 לא מקיימת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחה
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
<div class="ppt-text-layer" style="left:2.5000%;top:20.0000%;width:93.7500%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כיוון ראשון: אם 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’) אז 𝑇𝑟𝑎𝑐𝑒𝑠𝑓𝑖𝑛 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠𝑓𝑖𝑛(𝑇𝑆’)
  • תרגיל קל
כיוון שני: נניח 𝑇𝑟𝑎𝑐𝑒𝑠𝑓𝑖𝑛 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠𝑓𝑖𝑛(𝑇𝑆’) ונוכיח 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
  • תהי 𝜎∈𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆). צריך למצוא מסלול 𝑠0 𝑠 1 … של 𝑇𝑆’ שאלה עקבותיו.
  • ע&quot;פ ההנחה: לכל 𝑚 קיים מסלול𝜋𝑚 של 𝑇𝑆’ כך ש 𝑡𝑟𝑎𝑐𝑒( 𝜋 𝑚 )=𝜎[..𝑚]
  • למרות ש 𝜎[..𝑚] היא רישא של 𝜎 .. 𝑚+1 לא ברור ש- 𝜋𝑚 הוא רישא של 𝜋 𝑚+1
  • בזכות הסופיות של 𝑇𝑆’ קיימת תת-סידרה 𝜋 𝑠 1 , 𝜋 𝑠 2 …של 𝜋 1 , 𝜋 2 ,… כך ש 𝜋 𝑠 𝑖 ו- 𝜋 𝑠 𝑖+1 מסכימות על 𝑖 האינדקסים הראשונים
  • ניקח את המסלול שבו המצב במקום ה 𝑖 הוא המצב ה 𝑖 של 𝜋 𝑠 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:66.9101%;width:10.8725%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#370f0b;white-space:pre-wrap;width:100%;">
דוגמה נגדית?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
</div>
</div>
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:56.2500%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1,1
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:8.9687%;top:29.8299%;width:47.6238%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆′ המייצרות את הרישא 𝐿( 𝑞 1 ) ←
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:56.2500%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1,1
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 2,1
</td>
<td class="ppt-table-cell">
𝑞 2,2
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:8.9687%;top:29.8299%;width:47.6238%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆′ המייצרות את הרישא 𝐿( 𝑞 1 ) ←
</div>
</div>
<div class="ppt-text-layer" style="left:7.4835%;top:36.1613%;width:61.9224%;height:5.9240%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆′ המייצרות את הרישא 𝐿( 𝑞 1 )𝐿( 𝑞 2 ) ←
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
20
</div>
</div>
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:62.5000%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1,1
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 2,1
</td>
<td class="ppt-table-cell">
𝑞 2,2
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 3,1
</td>
<td class="ppt-table-cell">
𝑞 3,2
</td>
<td class="ppt-table-cell">
𝑞 3,3
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 4,1
</td>
<td class="ppt-table-cell">
𝑞 4,2
</td>
<td class="ppt-table-cell">
𝑞 4,3
</td>
<td class="ppt-table-cell">
𝑞 4,4
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 5,1
</td>
<td class="ppt-table-cell">
𝑞 5,2
</td>
<td class="ppt-table-cell">
𝑞 5,3
</td>
<td class="ppt-table-cell">
𝑞 5,4
</td>
<td class="ppt-table-cell">
𝑞 5,5
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 6,1
</td>
<td class="ppt-table-cell">
𝑞 6,2
</td>
<td class="ppt-table-cell">
𝑞 6,3
</td>
<td class="ppt-table-cell">
𝑞 6,4
</td>
<td class="ppt-table-cell">
𝑞 6,5
</td>
<td class="ppt-table-cell">
𝑞 6,6
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 7,1
</td>
<td class="ppt-table-cell">
𝑞 7,2
</td>
<td class="ppt-table-cell">
𝑞 7,3
</td>
<td class="ppt-table-cell">
𝑞 7,4
</td>
<td class="ppt-table-cell">
𝑞 7,5
</td>
<td class="ppt-table-cell">
𝑞 7,6
</td>
<td class="ppt-table-cell">
𝑞 7,7
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋱
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:39.6794%;top:43.1632%;width:55.8912%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצות של 𝑇𝑆′ המייצרות רישות סופיות של התיוגים ←
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
</div>
</div>
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:62.5000%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1,1
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 2,1
</td>
<td class="ppt-table-cell">
𝑞 2,2
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 3,1
</td>
<td class="ppt-table-cell">
𝑞 3,2
</td>
<td class="ppt-table-cell">
𝑞 3,3
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 4,1
</td>
<td class="ppt-table-cell">
𝑞 4,2
</td>
<td class="ppt-table-cell">
𝑞 4,3
</td>
<td class="ppt-table-cell">
𝑞 4,4
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 5,1
</td>
<td class="ppt-table-cell">
𝑞 5,2
</td>
<td class="ppt-table-cell">
𝑞 5,3
</td>
<td class="ppt-table-cell">
𝑞 5,4
</td>
<td class="ppt-table-cell">
𝑞 5,5
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 6,1
</td>
<td class="ppt-table-cell">
𝑞 6,2
</td>
<td class="ppt-table-cell">
𝑞 6,3
</td>
<td class="ppt-table-cell">
𝑞 6,4
</td>
<td class="ppt-table-cell">
𝑞 6,5
</td>
<td class="ppt-table-cell">
𝑞 6,6
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 7,1
</td>
<td class="ppt-table-cell">
𝑞 7,2
</td>
<td class="ppt-table-cell">
𝑞 7,3
</td>
<td class="ppt-table-cell">
𝑞 7,4
</td>
<td class="ppt-table-cell">
𝑞 7,5
</td>
<td class="ppt-table-cell">
𝑞 7,6
</td>
<td class="ppt-table-cell">
𝑞 7,7
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋱
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:39.6794%;top:43.1632%;width:55.8912%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצות של 𝑇𝑆′ המייצרות רישות סופיות של התיוגים ←
</div>
</div>
<div class="ppt-text-layer" style="left:5.0963%;top:87.3927%;width:5.0145%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 ′
</div>
</div>
<div class="ppt-text-layer" style="left:8.3708%;top:87.2654%;width:49.6503%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מצב שהופיע איסוף פעמים בעמודה הראשונה ←
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
</div>
</div>
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:43.7500%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 3,2
</td>
<td class="ppt-table-cell">
𝑞 3,3
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 4,2
</td>
<td class="ppt-table-cell">
𝑞 4,3
</td>
<td class="ppt-table-cell">
𝑞 4,4
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 6,2
</td>
<td class="ppt-table-cell">
𝑞 6,3
</td>
<td class="ppt-table-cell">
𝑞 6,4
</td>
<td class="ppt-table-cell">
𝑞 6,5
</td>
<td class="ppt-table-cell">
𝑞 6,6
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 7,2
</td>
<td class="ppt-table-cell">
𝑞 7,3
</td>
<td class="ppt-table-cell">
𝑞 7,4
</td>
<td class="ppt-table-cell">
𝑞 7,5
</td>
<td class="ppt-table-cell">
𝑞 7,6
</td>
<td class="ppt-table-cell">
𝑞 7,7
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋱
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:37.1261%;top:36.0714%;width:58.3952%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצות של 𝑇𝑆′ המייצרות
רישות סופיות של התיוגים ומתחילות ב- 𝑞 1 ′ ←
</div>
</div>
<div class="ppt-text-layer" style="left:5.0963%;top:87.3927%;width:5.0145%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 ′
</div>
</div>
<div class="ppt-text-layer" style="left:8.3708%;top:87.2654%;width:49.6503%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מצב שהופיע איסוף פעמים בעמודה הראשונה ←
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:43.7500%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 3,2
</td>
<td class="ppt-table-cell">
𝑞 3,3
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 4,2
</td>
<td class="ppt-table-cell">
𝑞 4,3
</td>
<td class="ppt-table-cell">
𝑞 4,4
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 6,2
</td>
<td class="ppt-table-cell">
𝑞 6,3
</td>
<td class="ppt-table-cell">
𝑞 6,4
</td>
<td class="ppt-table-cell">
𝑞 6,5
</td>
<td class="ppt-table-cell">
𝑞 6,6
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 7,2
</td>
<td class="ppt-table-cell">
𝑞 7,3
</td>
<td class="ppt-table-cell">
𝑞 7,4
</td>
<td class="ppt-table-cell">
𝑞 7,5
</td>
<td class="ppt-table-cell">
𝑞 7,6
</td>
<td class="ppt-table-cell">
𝑞 7,7
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋱
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:37.1261%;top:36.0714%;width:58.3952%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצות של 𝑇𝑆′ המייצרות
רישות סופיות של התיוגים ומתחילות ב- 𝑞 1 ′ ←
</div>
</div>
<div class="ppt-text-layer" style="left:5.0963%;top:87.3927%;width:11.4335%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 ′ 𝑞 2 ′
</div>
</div>
<div class="ppt-text-layer" style="left:17.3554%;top:87.5247%;width:46.8629%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מצב שהופיע איסוף פעמים בעמודה השניה ←
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:37.5000%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 2 ′
</td>
<td class="ppt-table-cell">
𝑞 3,3
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 2 ′
</td>
<td class="ppt-table-cell">
𝑞 6,3
</td>
<td class="ppt-table-cell">
𝑞 6,4
</td>
<td class="ppt-table-cell">
𝑞 6,5
</td>
<td class="ppt-table-cell">
𝑞 6,6
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1 ′
</td>
<td class="ppt-table-cell">
𝑞 2 ′
</td>
<td class="ppt-table-cell">
𝑞 7,3
</td>
<td class="ppt-table-cell">
𝑞 7,4
</td>
<td class="ppt-table-cell">
𝑞 7,5
</td>
<td class="ppt-table-cell">
𝑞 7,6
</td>
<td class="ppt-table-cell">
𝑞 7,7
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋱
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:39.0146%;top:33.1601%;width:58.3952%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצות של 𝑇𝑆′ המייצרות
רישות סופיות של התיוגים ומתחילות ב- 𝑞 1 ′ 𝑞 2 ′ ←
</div>
</div>
<div class="ppt-text-layer" style="left:5.0963%;top:87.3927%;width:21.5515%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 ′ 𝑞 2 ′ 𝑞 3 ′ ⋯
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:59.0780%;width:66.2500%;height:22.4392%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
• אפשר להמשיך ולבחור כך סידרה אינסופית של מצבים.
• זאת ריצה של 𝑇 𝑆 ′ כי כל זוג מצבים עוקבים נבחר מתוך ריצה.
• התיוגים שלה תואמים את סדרת התיוגים של הריצה ב-𝑇𝑆
• לכן סיימנו את ההוכחה.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.7417%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של כיוון ההוכחה השני בשקף הקודם
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
<div class="ppt-table-layer" style="left:3.3333%;top:16.6667%;width:64.8788%;height:56.2500%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
𝑞 1
</td>
<td class="ppt-table-cell">
𝑞 2
</td>
<td class="ppt-table-cell">
𝑞 3
</td>
<td class="ppt-table-cell">
𝑞 4
</td>
<td class="ppt-table-cell">
𝑞 5
</td>
<td class="ppt-table-cell">
𝑞 6
</td>
<td class="ppt-table-cell">
𝑞 7
</td>
<td class="ppt-table-cell">
𝑞 8
</td>
<td class="ppt-table-cell">
𝑞 9
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝐿( 𝑞 1 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 2 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 3 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 4 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 5 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 6 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 7 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 8 )
</td>
<td class="ppt-table-cell">
𝐿( 𝑞 9 )
</td>
<td class="ppt-table-cell">
⋯
</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 1,1
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 2,1
</td>
<td class="ppt-table-cell">
𝑞 2,2
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 3,1
</td>
<td class="ppt-table-cell">
𝑞 3,2
</td>
<td class="ppt-table-cell">
𝑞 3,3
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 4,1
</td>
<td class="ppt-table-cell">
𝑞 4,2
</td>
<td class="ppt-table-cell">
𝑞 4,3
</td>
<td class="ppt-table-cell">
𝑞 4,4
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 5,1
</td>
<td class="ppt-table-cell">
𝑞 5,2
</td>
<td class="ppt-table-cell">
𝑞 5,3
</td>
<td class="ppt-table-cell">
𝑞 5,4
</td>
<td class="ppt-table-cell">
𝑞 5,5
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
𝑞 6,1
</td>
<td class="ppt-table-cell">
𝑞 6,2
</td>
<td class="ppt-table-cell">
𝑞 6,3
</td>
<td class="ppt-table-cell">
𝑞 6,4
</td>
<td class="ppt-table-cell">
𝑞 6,5
</td>
<td class="ppt-table-cell">
𝑞 6,6
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋮
</td>
<td class="ppt-table-cell">
⋱
</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
<div class="ppt-text-layer" style="left:76.4097%;top:16.6667%;width:19.1610%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה של 𝑇𝑆 ←
</div>
</div>
<div class="ppt-text-layer" style="left:76.7392%;top:23.0330%;width:18.8314%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תיוגי הריצה ←
</div>
</div>
<div class="ppt-text-layer" style="left:39.6794%;top:43.1632%;width:55.8912%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצות של 𝑇𝑆′ המייצרות רישות סופיות של התיוגים ←
</div>
</div>
<div class="ppt-text-layer" style="left:37.6545%;top:73.6000%;width:61.1154%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לפי שובך היונים, קיים מצב בעמודה הראשונה החוזר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:14.6893%;top:79.9663%;width:84.0805%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
נמחק את שאר השורות, ובשורות שיישארו, יהיה מצב שיחזור אינסוף פעמים בעמודה השנייה
</div>
</div>
<div class="ppt-text-layer" style="left:12.5307%;top:86.2146%;width:86.5699%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
נמחק את שאר השורות, בשורות שיישארו, יהיה מצב שיחזור אינסוף פעמים בעמודה השלישית
</div>
</div>
<div class="ppt-text-layer" style="left:86.7730%;top:92.1365%;width:12.3276%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
וכך הלאה...
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:2.5925%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
קשר מעניין בין
תכונות זמן לינארי ומספרים
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
<div class="ppt-text-layer" style="left:4.5833%;top:23.3333%;width:90.8333%;height:75.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נניח ש-|𝐴𝑃|=9 ונגדיר עבור תת קבוצה 𝑆⊆ 0,1 :
𝑃 𝑆 = 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑖=1 ∞ 𝜎 𝑖 10 𝑖 ∈𝑆
האם התכונות הבאות הן תכונות בטיחות?
</div>
</div>
<div class="ppt-text-layer" style="left:1.2691%;top:34.4444%;width:19.0524%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
מתייחסים לאותיות כספרות ומפרשים
את המילה כשבר עשרוני אינסופי
</div>
</div>
<div class="ppt-text-layer" style="left:29.8875%;top:75.4842%;width:8.8021%;height:8.9765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#0070c0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
𝑃 ∅
</div>
</div>
<div class="ppt-text-layer" style="left:43.2164%;top:65.3054%;width:11.1924%;height:12.6313%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#0070c0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
𝑃 1 2 , 3 4
</div>
</div>
<div class="ppt-text-layer" style="left:70.8233%;top:65.3620%;width:24.5934%;height:12.7836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#0070c0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
𝑃 0.1,0.2 ∪ 0.3,0.4
</div>
</div>
<div class="ppt-text-layer" style="left:17.4258%;top:60.8389%;width:11.1924%;height:9.5486%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#0070c0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
𝑃 0,1
</div>
</div>
<div class="ppt-text-layer" style="left:56.4788%;top:73.6482%;width:13.5283%;height:12.6484%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#0070c0;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
𝑃 1 3 , 2 3
</div>
</div>
<div class="ppt-text-layer" style="left:22.9989%;top:90.8180%;width:54.0021%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
טענה: 𝑃 𝑆 תכונת בטיחות אם ורק אם 𝑆 קבוצה סגורה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:2.5925%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
<div class="ppt-text-layer" style="left:-2.0794%;top:23.5366%;width:98.8465%;height:75.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• טענה: אם S= 𝑎,𝑏 אז 𝑃 𝑆 אינה תכונת בטיחות
• לנוחות, נזכיר את הנוסחה מהשקף הקודם: 𝑃 𝑆 = 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑖=1 ∞ 𝜎 𝑖 10 𝑖 ∈𝑆
• נכתוב את הצגה של 𝑏 כשבר עשרוני: 𝑏=0. 𝑏 1 𝑏 2 …
• נניח בלי הגבלת הכלליות שהפיתוח לא מסתיים בסדרה אינסופית של אפסים
• המילה 𝜎 שגודל האות ה-𝑖 הוא 𝑏 𝑖 לא נמצאת ב- 𝑃 𝑆
• אבל לכל רישא 𝜎 ..𝑖 מתקיים ש-𝜎 ..𝑖 . {} 𝜔 נמצאת ב- 𝑃 𝑆
• לכן 𝑃 𝑆 אינה תכונת בטיחות.
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:57.0156%;width:12.4921%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
למה זה לא מגביל את הכלליות?
</div>
</div>
<div class="ppt-text-layer" style="left:5.3135%;top:85.3876%;width:59.9921%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
איך נראה שגם אם 𝑆=(𝑎,𝑏] מקבלים ש- 𝑃 𝑆 אינה תכונת בטיחות?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סְגוֹר (closure) של תכונה
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
<div class="ppt-text-layer" style="left:0.8333%;top:21.1111%;width:96.6667%;height:73.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: קבוצת הרישות הסופיות של 𝜎∈ 2𝐴𝑃 𝜔 :
𝑝𝑟𝑒𝑓(𝜎)= { 𝜌∈ 2 𝐴𝑃 ∗ : 𝜌 is a finite prefix of 𝜎 }
הרחבה לתכונות: 𝑝𝑟𝑒𝑓(𝑃) = 𝜎∈𝑃 𝑝𝑟𝑒𝑓(𝜎)
הגדרה: הסְגוֹר של תכונת זמן ליניארי 𝑃 הוא:
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 = 𝜎∈ 2𝐴𝑃 𝜔 : 𝑝𝑟𝑒𝑓 𝜎 ⊆ 𝑝𝑟𝑒𝑓 𝑃
  רצפי העקבות האינסופיים שכל הרישות הסופיות שלהם הן רישות של מילים ב-𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:45.8933%;width:29.1486%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
כל עוד יש המשך ב-𝑃 הרישא ב-𝑝𝑟𝑒𝑓(𝑃)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סְגוֹר של תכונה
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
<div class="ppt-text-layer" style="left:7.5000%;top:16.6667%;width:90.8333%;height:17.5026%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה שקולה: הסְגוֹר של תכונת זמן ליניארי 𝑃 היא קבוצת המילים האינסופיות שכל רישא סופית שלהן אפשר להמשיך למילה המקיימת את התכונה:
</div>
</div>
<div class="ppt-text-layer" style="left:3.0946%;top:36.6667%;width:92.2407%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 = 𝜎: ∀𝜌⊏𝜎 ∃ 𝜎 ′′ such that 𝜌𝜎 ′′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:68.3516%;top:60.5269%;width:30.6751%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜎∈𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ∖𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:41.1330%;top:80.5838%;width:7.5838%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜎 10 ′′
</div>
</div>
<div class="ppt-text-layer" style="left:46.2658%;top:54.7306%;width:7.6616%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜎 20 ′′
</div>
</div>
<div class="ppt-text-layer" style="left:64.4693%;top:77.3074%;width:7.6616%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜎 60 ′′
</div>
</div>
<div class="ppt-text-layer" style="left:14.9057%;top:77.8149%;width:7.6371%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜌 10
</div>
</div>
<div class="ppt-text-layer" style="left:25.7022%;top:67.9722%;width:7.7149%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜌 20
</div>
</div>
<div class="ppt-text-layer" style="left:49.6651%;top:74.5528%;width:7.7149%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝜌 60
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:53.0994%;width:28.5186%;height:5.9583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffb66d;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#1c1911;white-space:pre-wrap;width:100%;">
מילים שאין להן רישא רעה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
30
</div>
</div>
<div class="ppt-text-layer" style="left:6.6667%;top:19.5447%;width:89.9911%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור התכונה: האות הראשונה מכילה את 𝑝 ויש אות המכילה את 𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:12.0402%;top:40.6857%;width:78.1287%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#009900;white-space:pre-wrap;width:100%;">
כל רישא של כל מילה המתחילה באות המכילה את 𝑝
ניתן להמשיך למילה אינסופית המקיימת את התכונה
</div>
</div>
<div class="ppt-text-layer" style="left:7.7041%;top:55.5556%;width:86.8010%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
לכל מילה שאינה מתחילה באות המכילה את 𝑝 יש רישא
שלא ניתן להמשיך למילה אינסופית המקיימת את התכונה
</div>
</div>
<div class="ppt-text-layer" style="left:28.5902%;top:86.6667%;width:42.8197%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 = 𝜎: 𝜎 0 ⊨𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:19.6301%;top:71.1111%;width:64.0643%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לכן, הסגור של התכונה הוא כל המילים המתחילות באות המכילה את 𝑝:
</div>
</div>
<div class="ppt-text-layer" style="left:24.6678%;top:30.2656%;width:50.6643%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝜎: 𝜎 0 ⊨𝑝 ∧ ∃𝑖 . 𝜎 𝑖 ⊨𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:4.4635%;top:47.7510%;width:7.5767%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#370f0b;white-space:pre-wrap;width:100%;">
למה?
</div>
</div>
<div class="ppt-text-layer" style="left:4.4635%;top:63.2630%;width:7.5767%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#370f0b;white-space:pre-wrap;width:100%;">
למה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-031.png" alt="" />
<div class="ppt-text-layer" style="left:8.4433%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה גרפית של
הדוגמה מהשקף הקודם
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
31
</div>
</div>
<div class="ppt-text-layer" style="left:24.5833%;top:52.3164%;width:22.5000%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מילים המקיימות
את 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:55.0000%;top:34.4444%;width:22.5000%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מילים שאינן מקיימות את 𝑃
ויש להן רישא &quot;רעה&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:53.9347%;top:81.2413%;width:22.5000%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מילים שאינן מקיימות את 𝑃 ואין להן רישא &quot;רעה&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:38.3085%;top:63.3354%;width:10.1348%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0040c0;white-space:pre-wrap;width:100%;">
𝑝,𝑞 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:24.5833%;top:66.4405%;width:13.1066%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0040c0;white-space:pre-wrap;width:100%;">
𝑝} 𝑞 { 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:50.0625%;top:68.6373%;width:7.7443%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0040c0;white-space:pre-wrap;width:100%;">
𝑝 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:44.0323%;top:77.0794%;width:10.2688%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0040c0;white-space:pre-wrap;width:100%;">
{𝑝} 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:77.5000%;top:46.5852%;width:9.7078%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0040c0;white-space:pre-wrap;width:100%;">
{} 𝑝 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:57.4358%;top:49.2779%;width:15.2103%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0040c0;white-space:pre-wrap;width:100%;">
{}( 𝑞 𝑝 ) 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:25.6112%;top:20.1801%;width:50.6643%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝜎: 𝜎 0 ⊨𝑝 ∧ ∃𝑖 . 𝜎 𝑖 ⊨𝑞
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-032.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
קל להוכיח
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
32
</div>
</div>
<div class="ppt-text-layer" style="left:25.4167%;top:22.6518%;width:57.9167%;height:14.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור כל 𝑃⊆ 2 𝐴𝑃 𝜔 מתקיים
𝑃⊆𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃)
</div>
</div>
<div class="ppt-text-layer" style="left:25.4167%;top:78.2073%;width:57.9167%;height:14.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
יש 𝑃⊆ 2 𝐴𝑃 𝜔 שעבורה
𝑃≠𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-033.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משפט: הגדרה שקולה לתכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
33
</div>
</div>
<div class="ppt-text-layer" style="left:20.0000%;top:21.1111%;width:65.8333%;height:28.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃היא תכונת בטיחות
אם ורק אם
𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃) = 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:56.3501%;top:67.1745%;width:22.7500%;height:5.2394%;padding:11.20pt 11.20pt 11.20pt 11.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:83.0448%;top:72.7977%;width:4.2284%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#ffff00;white-space:pre-wrap;width:100%;">
?
</div>
</div>
<div class="ppt-text-layer" style="left:13.5315%;top:68.6554%;width:8.3432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(6.36deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
𝜎∉𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:10.9459%;top:77.2135%;width:13.3333%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(356.44deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
𝜌⊏𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:7.9571%;top:88.9181%;width:19.7367%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(7.04deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎 ′′ s.t 𝜌 𝜎′ ′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:52.4740%;width:36.3801%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#1c1911;white-space:pre-wrap;width:100%;">
מילה שכל רישא שלה אפשר להמשיך למילה ב-𝑃 והיא עצמה איננה ב-𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:45.9609%;width:9.8382%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:24.6158%;top:62.6276%;width:7.0508%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:70.3916%;top:78.2483%;width:4.2167%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחת כיוון ראשון
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
34
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:17.7778%;width:90.8333%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נניח, בשלילה, ש 𝑃 היא תכונת בטיחות ו 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ≠𝑃
ניקח 𝜎∈𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ∖𝑃
(קיימת כזאת מילה כי 𝑃⊆𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃))
ע&quot;פ הגדרת הסגור, כל רישא של 𝜎 היא רישא של מילה ב 𝑃
בפרט, אין ל-𝜎 רֵישָׁא סופית &quot;רעה&quot; 𝜌 כך
שכל 𝜎 ′ ש-𝜌 היא רֵישָׁא שלה לא מקיימת את 𝑃
בגלל ש-𝑃 תכונת בטיחות, 𝜎∈𝑃
בסתירה להגדרת 𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:9.0417%;top:73.7304%;width:5.5762%;height:3.5903%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(6.36deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
𝜎∉𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:7.3136%;top:79.3941%;width:8.9113%;height:3.7025%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(356.44deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
𝜌⊏𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:5.7250%;top:87.2169%;width:12.3731%;height:3.7025%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(7.04deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎 ′′ s.t 𝜌 𝜎′ ′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:58.5580%;width:6.5775%;height:2.9171%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:7.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:16.1976%;top:69.6972%;width:4.9647%;height:2.9171%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:7.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחת כיוון שני
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
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נניח ש 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 =𝑃
ניקח 𝜎∈ 2 𝐴𝑃 𝜔 ∖𝑃
כיוון ש 𝜎∉𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 , קיימת רישא סופית 𝜌 של 𝜎
שאינה רישא של אף מילה ב-𝑃
בפרט, 𝜌 היא רישא סופית &quot;רעה&quot; של 𝑃
הראינו שלכל מילה שאינה ב-𝑃 יש רישא סופית &quot;רעה&quot;
לכן 𝑃 היא תכונת בטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לשאלה בנושא
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
36
</div>
</div>
<div class="ppt-text-layer" style="left:2.2917%;top:22.2222%;width:95.4167%;height:71.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הוכיחו שלכל זוג תכונות זמן ליניארי 𝑃1 ו 𝑃2 מתקיים:
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃1∪𝑃2 = 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃1 ∪𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃2)
רעיון ההוכחה:
כיוון אחד קל: ברור שמילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 , למשל, היא גם מילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 ∪ 𝑃 2
בכיוון השני צריך להיזהר: איך אנחנו יודעים שכל מילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 ∪ 𝑃 2 היא גם מילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 או שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 2 ?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
על השימוש במילה &quot;סְגוֹר&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
37
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כשיש פונקציית מרחק 𝑑 (מרחבים מֶטְרִיִּים), מגדירים סְגוֹר של קבוצה 𝑆:
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑆 = 𝑥:∀𝜀&gt;0 ∃𝑠∈𝑆 𝑑 𝑥,𝑠 ≤𝜀
</div>
</div>
<div class="ppt-text-layer" style="left:38.9108%;top:55.5775%;width:21.7822%;height:32.8713%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#f4cec9;opacity:1.000;border:3.35px solid #9b2d1f;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
S
</div>
</div>
<div class="ppt-text-layer" style="left:70.7985%;top:50.0000%;width:24.2645%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מעגל ברדיוס 𝜀 סביב 𝑥
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
על השימוש במילה &quot;סְגוֹר&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
38
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כשיש פונקציית מרחק 𝑑 (מרחבים מֶטְרִיִּים), מגדירים סְגוֹר של קבוצה 𝑆:
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑆 = 𝑥:∀𝜀&gt;0 ∃𝑠∈𝑆 𝑑 𝑥,𝑠 ≤𝜀
אם נגדיר מרחק בין מילים ע&quot;י:
𝑑 𝜎 1 , 𝜎 2 ≔ 2 −max 𝑖: 𝜎 1 ..𝑖 = 𝜎 2 ..𝑖
נקבל שההגדרה למעלה שקולה להגדרה שהגדרנו קודם
בפרט, במרחב המטרי הזה, תכונות הבטיחות הן הקבוצות הסגורות
(אלה שהסגור שלהן שווה לקבוצה עצמה)
</div>
</div>
<div class="ppt-text-layer" style="left:1.5667%;top:41.1111%;width:25.0000%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#534733;white-space:pre-wrap;width:100%;">
מרחק קטן = יש רישא משותפת ארוכה
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:75.9609%;width:7.3138%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#370f0b;white-space:pre-wrap;width:100%;">
הוכחה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-039.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המשך: על השימוש במילה &quot;סְגוֹר&quot;
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
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:34.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: לכל 𝑃⊆ 2 𝐴𝑃 𝜔
𝑆 1 = 𝜎:∀𝜀&gt;0 ∃𝜎′∈𝑃 such that 2 −max 𝑖: 𝜎 ..𝑖 = 𝜎 ′ ..𝑖 &lt;𝜀
=
𝑆 2 ={𝜎: ∀𝜌⊏𝜎 ∃ 𝜎 ′ ⊐𝜌 such that 𝜎 ′ ∈𝑃}
</div>
</div>
<div class="ppt-text-layer" style="left:75.5064%;top:54.4444%;width:22.0438%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הכלה 𝑆 1 ⊆ 𝑆 2 :
</div>
</div>
<div class="ppt-text-layer" style="left:1.2667%;top:62.2667%;width:97.9000%;height:34.8837%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜎∈ 𝑆 1 , 𝜌⊏𝜎 ⇒∃ 𝜎 ′ ∈𝑃 such that 2 −max 𝑖: 𝜎 ..𝑖 = 𝜎 ′ ..𝑖 &lt; 2 −𝑙𝑒𝑛 𝜌 −1
⇒ 𝜎 ..𝑙𝑒𝑛 𝜌 = 𝜎 ′ ..𝑙𝑒𝑛 𝜌 =𝜌
⇒ 𝜎 ′ ⊐𝜌
⇒𝜎∈ 𝑆 2
</div>
</div>
<div class="ppt-text-layer" style="left:79.2627%;top:81.3099%;width:14.7391%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
ה-𝜀 שבחרנו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-040.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המשך: על השימוש במילה &quot;סְגוֹר&quot;
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
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:34.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: לכל 𝑃⊆ 2 𝐴𝑃 𝜔
𝑆 1 = 𝜎:∀𝜀&gt;0 ∃𝜎′∈𝑃 such that 2 −max 𝑖: 𝜎 ..𝑖 = 𝜎 ′ ..𝑖 &lt;𝜀
=
𝑆 2 ={𝜎: ∀𝜌⊏𝜎 ∃ 𝜎 ′ ⊐𝜌 such that 𝜎 ′ ∈𝑃}
</div>
</div>
<div class="ppt-text-layer" style="left:75.5630%;top:56.7897%;width:22.0438%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הכלה 𝑆 2 ⊆ 𝑆 1 :
</div>
</div>
<div class="ppt-text-layer" style="left:7.4000%;top:66.3155%;width:84.2667%;height:26.8055%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝜎∈ 𝑆 2 , 𝜀&gt;0 ⇒∃ 𝜎 ′ ∈𝑃 such that 𝜎 ′ ⊐𝜎 .. − log 2 𝜀
⇒ 2 −max 𝑖: 𝜎 ..𝑖 = 𝜎 ′ ..𝑖 &lt;𝜀
⇒𝜎∈ 𝑆 1
</div>
</div>
<div class="ppt-text-layer" style="left:76.3137%;top:84.4444%;width:14.9529%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
ה-𝜌 שבחרנו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-041.png" alt="" />
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
41
</div>
</div>
<div class="ppt-text-layer" style="left:4.5833%;top:23.3333%;width:90.8333%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונות בטיחות מבטאות דרישה &quot;שמשהו רע לא יקרה&quot;
• אפשר לעמוד בדרישה גם אם לא עושים כלום!
  כך, אף פעם לא נגיע למצב &quot;רע&quot;
• לכן: נוסיף גם תכונות חַיּוּת כדי לדרוש שתהייה התקדמות
• דרישות חַיּוּת אומרות:
בסופו של דבר יקרה &quot;משהו טוב&quot; [Lamport 1977]
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/14-property-closure/slide-042.png" alt="" />
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
42
</div>
</div>
<div class="ppt-text-layer" style="left:48.3333%;top:61.1412%;width:47.5000%;height:34.1076%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת
&quot;משהו טוב יקרה בסופו של דבר&quot;
תמיד יכול להיות
&quot;שהדבר הטוב&quot; יקרה
</div>
</div>
<div class="ppt-text-layer" style="left:12.5321%;top:61.1412%;width:31.8359%;height:34.1076%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
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
