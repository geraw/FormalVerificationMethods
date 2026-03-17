---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 16-fairness
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
הוֹגְנוּת (Fairness)
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:87.3772%;top:-0.8058%;width:11.4335%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Aharoni','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
584
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:8.8680%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תוכן
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:7.8107%;top:-3.4074%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לצורך בהנחות הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:0.8414%;top:14.1585%;width:98.9386%;height:84.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
במקרים רבים לא ניתן להוכיח תכונות חַיּוּת בלי הנחות נוספות
למשל:
נוכל להוכיח תכונה זאת רק אם נניח שמנגנון השיבוץ הוגן
במובן שהוא לא מרעיב את 𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:7.8107%;top:26.5466%;width:77.8107%;height:9.4058%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : ∃𝑖≥0 ∀𝑗&gt;𝑖 𝜎 𝑗 ⊨ 𝑥=1
</div>
</div>
<div class="ppt-text-layer" style="left:52.0942%;top:62.9274%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 1
</div>
</div>
<div class="ppt-text-layer" style="left:76.1411%;top:62.9274%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 1
</div>
</div>
<div class="ppt-text-layer" style="left:67.4097%;top:41.3538%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:62.5452%;top:56.4925%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:72.2097%;top:45.9999%;width:13.0410%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑥=1}
</div>
</div>
<div class="ppt-text-layer" style="left:44.3885%;top:46.0808%;width:13.0410%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑥=0}
</div>
</div>
<div class="ppt-text-layer" style="left:8.1802%;top:59.1852%;width:34.4239%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#742217;white-space:pre-wrap;width:100%;">
הפעולה הראשונה של 𝑃 2 היא
השמת הערך 1 למשתנה 𝑥
</div>
</div>
<div class="ppt-text-layer" style="left:14.2550%;top:43.0290%;width:13.9376%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffc5;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑑𝑒𝑓 𝑃 2 ():
𝑥≔1
…
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:6.2054%;top:-1.1111%;width:88.7946%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
חוסר הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:71.7076%;top:100.0000%;width:28.2924%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.4434%;top:2.2222%;width:5.2232%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
4
</div>
</div>
<div class="ppt-text-layer" style="left:6.2054%;top:21.1111%;width:88.7946%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נניח שֶׁשָּׁרָת מְשָׁרֵת תהליכים 𝑃 1 , 𝑃 2 ,…, 𝑃 𝑛 באופן הבא:
  • אם התהליך הראשון צריך שירות הוא מקבל
  • אחרת, אם התהליך השני צריך שירות הוא יקבל
  • ...
  • תהליך 𝑃 𝑛 יקבל שירות רק אם אף אחד אחר לא צריך שירות
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:88.8889%;width:97.5000%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
קשה להבטיח שהמערכת תתפקד נכון בתנאים כאלה !!!
</div>
</div>
<div class="ppt-text-layer" style="left:55.0000%;top:59.0373%;width:13.0075%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#e4dbd4;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מי הבא בתור?
</div>
</div>
<div class="ppt-text-layer" style="left:41.5540%;top:60.0000%;width:9.1822%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#e4dbd4;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אולי אני?
</div>
</div>
<div class="ppt-text-layer" style="left:29.8970%;top:60.5499%;width:9.0913%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#e4dbd4;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אולי אני?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: האם התוכנית תמיד עוצרת?
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
<div class="ppt-text-layer" style="left:47.4859%;top:27.7732%;width:15.9958%;height:11.7857%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שלב ההגרלה
</div>
</div>
<div class="ppt-text-layer" style="left:47.4859%;top:51.3446%;width:15.9958%;height:7.8571%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עצירה
</div>
</div>
<div class="ppt-text-layer" style="left:34.1667%;top:41.3098%;width:20.9940%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הסתברות 1-𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:66.6191%;top:22.5131%;width:17.8210%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הסתברות 𝑝
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:67.3273%;width:90.3316%;height:15.7075%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אבסטרקציה: בשלב ראשון, לפני שידוע לנו הערך של 𝑝, ממדלים כמעבר לא דטרמיניסטי
</div>
</div>
<div class="ppt-text-layer" style="left:24.5280%;top:87.6328%;width:52.6831%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בעיה: לא ניתן להוכיח עצירה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמא: שני רמזורים בלתי תלויים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
6
</div>
</div>
<div class="ppt-text-layer" style="left:65.6978%;top:21.1111%;width:13.4409%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אדום
</div>
</div>
<div class="ppt-text-layer" style="left:65.6978%;top:30.9641%;width:13.4409%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ירוק
</div>
</div>
<div class="ppt-text-layer" style="left:64.3537%;top:47.1584%;width:13.4409%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אדום
</div>
</div>
<div class="ppt-text-layer" style="left:64.3537%;top:57.0113%;width:13.4409%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ירוק
</div>
</div>
<div class="ppt-text-layer" style="left:45.0806%;top:73.6601%;width:20.1613%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אדום, אדום
</div>
</div>
<div class="ppt-text-layer" style="left:45.0806%;top:91.1765%;width:20.1613%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ירוק, ירוק
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:82.4183%;width:20.1613%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ירוק, אדום
</div>
</div>
<div class="ppt-text-layer" style="left:77.3387%;top:81.3235%;width:20.1613%;height:4.3791%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אדום, ירוק
</div>
</div>
<div class="ppt-text-layer" style="left:2.0864%;top:27.0998%;width:17.4720%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑟𝐿𝑖𝑔ℎ𝑡1
</div>
</div>
<div class="ppt-text-layer" style="left:1.3235%;top:51.5505%;width:17.4720%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑟𝐿𝑖𝑔ℎ𝑡2
</div>
</div>
<div class="ppt-text-layer" style="left:2.0864%;top:66.4791%;width:33.3333%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑟𝐿𝑖𝑔ℎ 𝑡 1 ||| 𝑇𝑟𝐿𝑖𝑔ℎ 𝑡 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המשך הדוגמה...
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
<div class="ppt-text-layer" style="left:4.1667%;top:16.6667%;width:95.0000%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת הַחַיּוּת:
&quot;כל אחד מהרמזורים ירוק לעיתים תכופות&quot;
• אינה מתקיימת בגלל שהמילה:
𝑟𝑒 𝑑 1 , 𝑟𝑒 𝑑 2 𝑔𝑟𝑒𝑒 𝑛 1 , 𝑟𝑒 𝑑 2 𝑟𝑒 𝑑 1 , 𝑟𝑒 𝑑 2 𝑔𝑟𝑒𝑒 𝑛 1 , 𝑟𝑒 𝑑 2 . ..
שייכת לעקבות של המערכת אבל רק הרמזור הראשון ירוק לעיתים תכופות.
• מה רע בדוגמה?
  • אין רע. הריצה שיצרה את רצף העקבות למעלה היא ריצה חוקית של המערכת.
  • כאן, אי הדטרמיניזם מייצג מערכות שרצות בקצב שונה.
  • הריצה הזאת משקפת רצף בחירות לא דטרמיניסטיות לא ריאלי - אין מערכת שרצה פי אינסוף יותר מהר מאחרת.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: האם התוכנית עוצרת?
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
<div class="ppt-text-layer" style="left:18.3333%;top:18.4722%;width:26.7202%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
[Inc, Reset]
</div>
</div>
<div class="ppt-text-layer" style="left:18.3333%;top:30.6944%;width:63.7120%;height:20.1953%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
proc Inc {
do ∷𝑥≥0 -&gt; 𝑥≔𝑥+1 od
}
</div>
</div>
<div class="ppt-text-layer" style="left:18.4432%;top:54.9436%;width:63.6021%;height:20.1953%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
proc Reset {
𝑥≔−1
}
</div>
</div>
<div class="ppt-text-layer" style="left:6.7138%;top:82.2222%;width:83.7306%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑥 משתנה שלם (integer) משותף שערכו ההתחלתי 0
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מהי הוֹגְנוּת?
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
<div class="ppt-text-layer" style="left:3.3333%;top:21.1111%;width:91.6667%;height:51.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הנחה סבירה:
לא ייתכן שמערכת ההפעלה תתעלם מפעולה לעד
• אבסטרקציה:
לא רוצים לדעת כלום על מנגנון בחירת האירועים
אבל לא סביר שהמנגנון אינו &quot;הוגן&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:11.5104%;top:72.0820%;width:75.3125%;height:13.9123%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ff0000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
חשוב לזכור: הנחות ההוֹגְנוּת הן חלק מהמודל
ולא תכונות שרוצים להוכיח
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה הוֹגְנוּת?
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
<div class="ppt-text-layer" style="left:3.3333%;top:20.0000%;width:90.8333%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• מחשבה אבסטרקטית על פרטי השיבוץ שעדיין לא נקבעו, שלא ניתן לדעת או כאלה המסבכים את המודל
• למשל:
  • לא ידועה המהירות היחסית בין הַמְּעַבְּדִים
    • אבל מניחים ששני המעבדים רצים ולא נתקעו
  • לא נקבעו ההסתברויות לבחירת מעבר 𝐴 או מעבר 𝐵
    • אבל מניחים שההסתברות לא אפס
  • לא הוחלט איך יקבע השיבוץ
    • אבל מניחים שמנגנון השיבוץ לא יתעלם מפעולה לָעַד
• מקבלים אנליזה יותר חסינה (robust) שאינה תלויה בפרטים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:4.9256%;top:2.2222%;width:89.7688%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה שכבר ראינו:
מניעה הדדית מבוססת אַתָּת (semaphore)
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
<div class="ppt-text-layer" style="left:70.0688%;top:31.1131%;width:11.1451%;height:8.1650%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#0070c0;opacity:1.000;border:3.35px solid #002060;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑛𝑜𝑛𝑐𝑟𝑖𝑡2
</div>
</div>
<div class="ppt-text-layer" style="left:70.0688%;top:66.8350%;width:11.1451%;height:8.1650%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#0070c0;opacity:1.000;border:3.35px solid #002060;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖𝑡2
</div>
</div>
<div class="ppt-text-layer" style="left:70.0688%;top:48.9741%;width:11.1451%;height:8.1650%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#0070c0;opacity:1.000;border:3.35px solid #002060;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑤𝑎𝑖𝑡2
</div>
</div>
<div class="ppt-text-layer" style="left:75.6341%;top:59.6906%;width:22.4680%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦&gt;0 :𝑦 :=𝑦−1
</div>
</div>
<div class="ppt-text-layer" style="left:49.8100%;top:48.4996%;width:14.1150%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦 :=𝑦+1
</div>
</div>
<div class="ppt-text-layer" style="left:22.2910%;top:31.1131%;width:12.5186%;height:8.1650%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑛𝑜𝑛𝑐𝑟𝑖𝑡1
</div>
</div>
<div class="ppt-text-layer" style="left:22.2910%;top:66.8350%;width:12.7090%;height:8.1650%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖𝑡1
</div>
</div>
<div class="ppt-text-layer" style="left:22.2910%;top:48.9741%;width:12.7090%;height:8.1650%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑤𝑎𝑖𝑡1
</div>
</div>
<div class="ppt-text-layer" style="left:28.7235%;top:58.6518%;width:23.0290%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦&gt;0 : 𝑦 :=𝑦−1
</div>
</div>
<div class="ppt-text-layer" style="left:2.6077%;top:49.2327%;width:14.1325%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦 :=𝑦+1
</div>
</div>
<div class="ppt-text-layer" style="left:4.9256%;top:87.6601%;width:86.0411%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑦=0 מסמל &quot;המנעול בשימוש&quot;, 𝑦=1 מסמל &quot;המנעול חופשי&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:25.1305%;top:78.6373%;width:6.8398%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 𝐺 1
</div>
</div>
<div class="ppt-text-layer" style="left:72.2142%;top:78.6373%;width:6.8980%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 𝐺 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: מערכת המעברים למניעה ההדדית
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
<div class="ppt-text-layer" style="left:43.3970%;top:21.9568%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8215%;top:39.5678%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:55.9724%;top:39.5678%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:43.0271%;top:58.1572%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:12.3283%;top:58.1572%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑛2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:75.2054%;top:58.1572%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:26.3832%;top:77.7250%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑤2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:62.6300%;top:77.7250%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:67.3043%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.5832%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:19.4125%;top:38.0397%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:74.8766%;top:38.0397%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:58.9123%;top:29.1509%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:37.3156%;top:29.1509%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.4205%;top:69.1509%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:82.3156%;top:68.0397%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:13.9822%;top:68.0397%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:69.7539%;top:69.1509%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4042%;top:46.9286%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:55.7716%;top:46.9286%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.4383%;top:51.3731%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:64.9383%;top:51.3731%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:10.3001%;top:90.0134%;width:79.3998%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
ראינו שהמערכת אינה מקיימת את תכונת מניעת ההרעבה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הרעבת תהליך 2
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
<div class="ppt-text-layer" style="left:43.3970%;top:21.9568%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8215%;top:39.5678%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:55.9724%;top:39.5678%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:43.0271%;top:58.1572%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:12.3283%;top:58.1572%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑛2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:75.2054%;top:58.1572%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:26.3832%;top:77.7250%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑤2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:62.6300%;top:77.7250%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:67.3043%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.5832%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:19.4125%;top:38.0397%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:74.8766%;top:38.0397%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:58.9123%;top:29.1509%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:37.3156%;top:29.1509%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.4205%;top:69.1509%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:82.3156%;top:68.0397%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:13.9822%;top:68.0397%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:69.7539%;top:69.1509%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4042%;top:46.9286%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:55.7716%;top:46.9286%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.4383%;top:51.3731%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:64.9383%;top:51.3731%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:2.0782%;top:90.0000%;width:95.8436%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
האם הוגן שלתהליך 2יהיו אינסוף אפשרויות להיכנס לקטע הקריטי, אבל הוא אינו נכנס לעולם?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הרעבת תהליך 2
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
<div class="ppt-text-layer" style="left:43.3970%;top:21.9568%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8215%;top:39.5678%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:55.9724%;top:39.5678%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:43.0271%;top:58.1572%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:12.3283%;top:58.1572%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑛2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:75.2054%;top:58.1572%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:26.3832%;top:77.7250%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #d34817;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑤2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:62.6300%;top:77.7250%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:3.35px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:67.3043%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.5832%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:19.4125%;top:38.0397%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:74.8766%;top:38.0397%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:58.9123%;top:29.1509%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:37.3156%;top:29.1509%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.4205%;top:69.1509%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:82.3156%;top:68.0397%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:13.9822%;top:68.0397%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:69.7539%;top:69.1509%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4042%;top:46.9286%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:55.7716%;top:46.9286%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.4383%;top:51.3731%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:64.9383%;top:51.3731%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:1.1053%;top:89.3711%;width:97.7895%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
האם הוגן שיהיו אינסוף אפשרויות להיכנס לקטע הקריטי, אבל נכנסים רק מספר סופי של פעמים?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת
</div>
</div>
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
<div class="ppt-text-layer" style="left:0.8333%;top:21.3037%;width:96.6667%;height:67.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• מניעת הרעבה מנותחת בד&quot;כ תחת הנחות הוֹגְנוּת בין תהליכים
  • מניחים שמנגנון השיבוץ בין התהליכים פועל באופן סביר
• בד&quot;כ צריך להניח הוֹגְנוּת (fairness) כדי להוכיח חַיּוּת (liveness)
  • לא נדרש עבור תכונות בטיחות
  • כדי להוכיח התקדמות, צריך להניח שמאופשרת פעילות
• הוֹגְנוּת קשורה להסדרה הוֹגֶנֶת של חוסר הדטרמיניסטיות
  • לא הוגן להתעלם מאפשרות באופן עִקְבִי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:8.8680%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תוכן
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
16
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אילוצי הוֹגְנוּת
Fairness Constraints
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
<div class="ppt-text-layer" style="left:6.6667%;top:21.1111%;width:89.5833%;height:45.8376%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הוֹגְנוּת בלתי מותנית
  • פעולה מבוצעת באופן תָּכוּף (infinitely often)
• הוֹגְנוּת חזקה
  • אם הפעולה מאופשרת באופן תָּכוּף (לא בהכרח כל הזמן) אז היא צריכה להתבצע באופן תָּכוּף
• הוֹגְנוּת חלשה
  • אם הפעולה מאופשרת בְּרֶצֶף (מנקודה מסוימת בזמן אין ביטול של הָאִפְשׁוּר) אז היא צריכה להתבצע באופן תָּכוּף
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אילוצי הוֹגְנוּת
Fairness Constraints
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
<div class="ppt-text-layer" style="left:6.6667%;top:21.1111%;width:89.5833%;height:45.8376%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הוֹגְנוּת בלתי מותנית
  • פעולה מבוצעת באופן תָּכוּף (infinitely often)
• הוֹגְנוּת חזקה
  • אם הפעולה מאופשרת באופן תָּכוּף (לא בהכרח כל הזמן) אז היא צריכה להתבצע באופן תָּכוּף
• הוֹגְנוּת חלשה
  • אם הפעולה מאופשרת בְּרֶצֶף (מנקודה מסוימת בזמן אין ביטול של הָאִפְשׁוּר) אז היא צריכה להתבצע באופן תָּכוּף
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אילוצי הוֹגְנוּת
Fairness Constraints
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
<div class="ppt-text-layer" style="left:6.6667%;top:21.1111%;width:89.5833%;height:45.8376%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הוֹגְנוּת בלתי מותנית
  • פעולה מבוצעת באופן תָּכוּף (infinitely often)
• הוֹגְנוּת חזקה
  • אם הפעולה מאופשרת באופן תָּכוּף (לא בהכרח כל הזמן) אז היא צריכה להתבצע באופן תָּכוּף
• הוֹגְנוּת חלשה
  • אם הפעולה מאופשרת בְּרֶצֶף (מנקודה מסוימת בזמן אין ביטול של הָאִפְשׁוּר) אז היא צריכה להתבצע באופן תָּכוּף
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-5.5556%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סוגים שונים של אילוצי הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
20
</div>
</div>
<div class="ppt-text-layer" style="left:11.7405%;top:13.6280%;width:80.8333%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נגיד שריצה 𝑟= 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ של מערכת מעברים 𝑇𝑆 היא:
  הוגנת ללא תנאי ביחס לקבוצת פעולות 𝐴 אם:
  הוגנת חזק ביחס לקבוצת פעולות 𝐴 אם:
  הוגנת חלש ביחס לקבוצת פעולות 𝐴 אם:
</div>
</div>
<div class="ppt-text-layer" style="left:11.9897%;top:28.0725%;width:65.9738%;height:7.2160%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
  ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.9659%;top:64.2907%;width:19.6273%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#002060;white-space:pre-wrap;width:100%;">
𝐴 מאופשרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:8.5750%;top:92.3924%;width:44.3631%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#002060;white-space:pre-wrap;width:100%;">
בסופו של דבר, 𝐴 מאופשרת כל הזמן, ברצף
</div>
</div>
<div class="ppt-text-layer" style="left:33.7009%;top:38.0725%;width:17.2432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴 נבחרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:50.2568%;top:64.9093%;width:17.2432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴 נבחרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:12.1325%;top:52.9313%;width:65.9738%;height:8.9427%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
∃ ∞ 𝑖 .𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:59.4235%;top:92.0643%;width:17.2432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴 נבחרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:12.1794%;top:80.2947%;width:65.9270%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
  ∃𝑗 . ∀𝑖&gt;𝑗 . 𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-5.5556%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סוגים שונים של אילוצי הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
21
</div>
</div>
<div class="ppt-text-layer" style="left:11.7405%;top:13.6280%;width:80.8333%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נגיד שריצה 𝑟= 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ של מערכת מעברים 𝑇𝑆 היא:
  הוגנת ללא תנאי ביחס לקבוצת פעולות 𝐴 אם:
  הוגנת חזק ביחס לקבוצת פעולות 𝐴 אם:
  הוגנת חלש ביחס לקבוצת פעולות 𝐴 אם:
</div>
</div>
<div class="ppt-text-layer" style="left:11.9897%;top:28.0725%;width:65.9738%;height:7.2160%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
  ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.9659%;top:64.2907%;width:19.6273%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#002060;white-space:pre-wrap;width:100%;">
𝐴 מאופשרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:8.5750%;top:92.3924%;width:44.3631%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#002060;white-space:pre-wrap;width:100%;">
בסופו של דבר, 𝐴 מאופשרת כל הזמן, ברצף
</div>
</div>
<div class="ppt-text-layer" style="left:33.7009%;top:38.0725%;width:17.2432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴 נבחרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:50.2568%;top:64.9093%;width:17.2432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴 נבחרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:12.1325%;top:52.9313%;width:65.9738%;height:8.9427%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
∃ ∞ 𝑖 .𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:59.4235%;top:92.0643%;width:17.2432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝐴 נבחרת תָּדִיר
</div>
</div>
<div class="ppt-text-layer" style="left:12.1794%;top:80.2947%;width:65.9270%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
  ∃𝑗 . ∀𝑖&gt;𝑗 . 𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
יחסים בין אילוצי הוֹגְנוּת על ריצה
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
<div class="ppt-text-layer" style="left:3.3333%;top:20.0000%;width:93.3333%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ריצה מקיימת הוֹגְנוּת בלתי מותנית
  𝐴 מבוצעת באופן תָּכוּף (infinitely often)
  ⇓
ריצה מקיימת הוֹגְנוּת חזקה
  אם 𝐴 מאופשרת באופן תָּכוּף (לא בהכרח כל הזמן)
  אז היא מבוצעת באופן תָּכוּף
  ⇓
ריצה מקיימת הוֹגְנוּת חלשה
  אם 𝐴 מאופשרת בְּרֶצֶף (מרגע מסוים אין ביטול של הָאִפְשׁוּר)
  אז היא מבוצעת באופן תָּכוּף
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות לריצות בלתי הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
23
</div>
</div>
<div class="ppt-text-layer" style="left:43.3970%;top:25.0281%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8215%;top:42.6392%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:55.9724%;top:42.6392%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:43.0271%;top:61.2286%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:12.3283%;top:61.2286%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:75.2054%;top:61.2286%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:26.3832%;top:80.7964%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:62.6300%;top:80.7964%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:67.3043%;top:23.0714%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.5832%;top:23.0714%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:19.4125%;top:41.1111%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:74.8766%;top:41.1111%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:58.9123%;top:32.2222%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:37.3156%;top:32.2222%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.4205%;top:72.2222%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:82.3156%;top:71.1111%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:13.9822%;top:71.1111%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:69.7539%;top:72.2222%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4042%;top:50.0000%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:55.7716%;top:50.0000%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.4383%;top:54.4444%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:64.9383%;top:54.4444%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות לריצות בלתי הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
24
</div>
</div>
<div class="ppt-text-layer" style="left:43.3970%;top:25.0281%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8215%;top:42.6392%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑛2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:55.9724%;top:42.6392%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:43.0271%;top:61.2286%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑤2, 𝑦=1
</div>
</div>
<div class="ppt-text-layer" style="left:12.3283%;top:61.2286%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑛2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:75.2054%;top:61.2286%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:26.3832%;top:80.7964%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑤2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:62.6300%;top:80.7964%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑐2, 𝑦=0
</div>
</div>
<div class="ppt-text-layer" style="left:67.3043%;top:23.0714%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:35.2227%;top:23.0714%;width:2.5630%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙
</div>
</div>
<div class="ppt-text-layer" style="left:19.4125%;top:41.1111%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:74.8766%;top:41.1111%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:58.9123%;top:32.2222%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:37.3156%;top:32.2222%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.4205%;top:72.2222%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:82.3156%;top:71.1111%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:13.9822%;top:71.1111%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:69.7539%;top:72.2222%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4042%;top:50.0000%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:55.7716%;top:50.0000%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.4383%;top:54.4444%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:64.9383%;top:54.4444%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:9.3163%;top:91.3430%;width:77.7443%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ביחס ל-𝐴={ 𝑟𝑒𝑞 2 }: לא הוֹגֶנֶת חלש, לא הוֹגֶנֶת חזק וגם לא הוֹגֶנֶת ללא תנאי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמאות לריצות בלתי הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:43.3970%;top:25.0281%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8215%;top:42.6392%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:55.9724%;top:42.6392%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:43.0271%;top:61.2286%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:12.3283%;top:61.2286%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:75.2054%;top:61.2286%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:26.3832%;top:80.7964%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:62.6300%;top:80.7964%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:67.3660%;top:23.0714%;width:4.1407%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.6449%;top:23.0714%;width:4.1407%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:19.5359%;top:41.1111%;width:7.1048%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:75.1227%;top:41.1111%;width:6.9821%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:59.0967%;top:32.2222%;width:5.3854%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:37.5000%;top:32.2222%;width:5.3854%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.6667%;top:72.2222%;width:6.9821%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:82.5000%;top:71.1111%;width:5.3854%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:71.1111%;width:5.3854%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:70.0000%;top:72.2222%;width:6.9821%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4659%;top:50.0000%;width:5.5081%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:55.8333%;top:50.0000%;width:5.5081%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:54.4444%;width:4.1407%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:65.0000%;top:54.4444%;width:4.1407%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:7.7702%;top:91.3814%;width:76.3965%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ביחס ל-𝐴={𝑒𝑛𝑡𝑒 𝑟 2 }: הוֹגֶנֶת חלש, לא הוֹגֶנֶת חזק וגם לא הוֹגֶנֶת ללא תנאי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
באיזה מושג הוֹגְנוּת להשתמש?
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
<div class="ppt-text-layer" style="left:0.0000%;top:21.1111%;width:98.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• מטרת אילוצי הוֹגְנוּת לפסול ריצות &quot;בלתי סבירות&quot;
• אילוצים חזקים מדי? ⇐נפסלות ריצות רלוונטיות
  • אם אימות נותן דוגמה נגדית: מצאנו בָּאג במערכת
  • אם מצליחים לאמת את התכונה: אי אפשר להסיק נכונות המערכת כי יכול להיות שיש שגיאה בריצות הרלוונטיות שנפסלו
• אילוצים חלשים מדי? ⇐ מתחשבים ביותר מדי ריצות
  • אם אימות נותן דוגמה נגדית: יכול להיות שהדוגמה היא ריצה לא רלוונטית
  • אם מצליחים לאמת את התכונה: המערכת נכונה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תוכן
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
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
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הנחות הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:1.6667%;top:32.2222%;width:90.8333%;height:44.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• אילוצי הוֹגְנוּת כופים דרישה לקבוצה 𝐴⊆𝐴𝑐𝑡
• במעשה: נדרשים אילוצים שונים לקבוצות שונות של פעולות
• את זה ממדלים באמצעות הנחות הוֹגְנוּת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: הנחות הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:82.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הנחת הוֹגְנוּת ל- 𝑇𝑆=〈𝑆,𝐴𝑐𝑡,→,𝐼,𝐴𝑃,𝐿〉 היא שלישייה
ℱ= ℱ uncond , ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 , ℱ 𝑤𝑒𝑎𝑘 ∈ 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡
נגיד שריצה 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ של 𝑇𝑆 היא ℱ-הוֹגֶנֶת אם:
  לכל 𝐴∈ ℱ uncond : ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 : ∃ ∞ 𝑖 . 𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑤𝑒𝑎𝑘 : ∃𝑗 . ∀𝑖&gt;𝑗 .𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: הנחות הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
30
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:82.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הנחת הוֹגְנוּת ל- 𝑇𝑆=〈𝑆,𝐴𝑐𝑡,→,𝐼,𝐴𝑃,𝐿〉 היא שלישייה
ℱ= ℱ uncond , ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 , ℱ 𝑤𝑒𝑎𝑘 ∈ 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡
נגיד שריצה 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ של 𝑇𝑆 היא ℱ-הוֹגֶנֶת אם:
  לכל 𝐴∈ ℱ uncond : ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 : ∃ ∞ 𝑖 . 𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑤𝑒𝑎𝑘 : ∃𝑗 . ∀𝑖&gt;𝑗 .𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-031.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: הנחות הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
31
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:82.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הנחת הוֹגְנוּת ל- 𝑇𝑆=〈𝑆,𝐴𝑐𝑡,→,𝐼,𝐴𝑃,𝐿〉 היא שלישייה
ℱ= ℱ uncond , ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 , ℱ 𝑤𝑒𝑎𝑘 ∈ 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡
נגיד שריצה 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ של 𝑇𝑆 היא ℱ-הוֹגֶנֶת אם:
  לכל 𝐴∈ ℱ uncond : ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 : ∃ ∞ 𝑖 . 𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑤𝑒𝑎𝑘 : ∃𝑗 . ∀𝑖&gt;𝑗 .𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-032.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: הנחות הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
32
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:20.0000%;width:96.6667%;height:82.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הנחת הוֹגְנוּת ל- 𝑇𝑆=〈𝑆,𝐴𝑐𝑡,→,𝐼,𝐴𝑃,𝐿〉 היא שלישייה
ℱ= ℱ uncond , ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 , ℱ 𝑤𝑒𝑎𝑘 ∈ 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡 × 2 2 𝐴𝑐𝑡
נגיד שריצה 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ של 𝑇𝑆 היא ℱ-הוֹגֶנֶת אם:
  לכל 𝐴∈ ℱ uncond : ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑠𝑡𝑟𝑜𝑛𝑔 : ∃ ∞ 𝑖 . 𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
  לכל 𝐴∈ ℱ 𝑤𝑒𝑎𝑘 : ∃𝑗 . ∀𝑖&gt;𝑗 .𝑝𝑜𝑠𝑡 𝑠 𝑖 ,𝐴 ≠∅ ⇒ ∃ ∞ 𝑖 . 𝛼 𝑖 ∈𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:23.4081%;top:74.1196%;width:22.4252%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
&quot;מבקש&quot; אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:12.5000%;top:86.8018%;width:34.6441%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
&quot;מבקש&quot; כל הזמן (החל מרגע מסוים)
</div>
</div>
<div class="ppt-text-layer" style="left:52.1575%;top:86.8018%;width:21.5312%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
&quot;נבחר&quot; אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:52.1575%;top:73.8096%;width:21.5312%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
&quot;נבחר&quot; אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:48.8242%;top:60.5051%;width:21.5312%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
&quot;נבחר&quot; אינסוף פעמים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-033.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: ריצה לא הוגנת
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
33
</div>
</div>
<div class="ppt-text-layer" style="left:46.1073%;top:39.3441%;width:10.8611%;height:7.5057%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:1.00px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
&quot;מבקש&quot; את 𝛼 3 ואת 𝛼 6
</div>
</div>
<div class="ppt-text-layer" style="left:24.3850%;top:39.3441%;width:10.8611%;height:7.5057%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:1.00px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
&quot;מבקש&quot; את 𝛼 7 ואת 𝛼 1
</div>
</div>
<div class="ppt-text-layer" style="left:67.8295%;top:39.3441%;width:10.8611%;height:7.5057%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;border:1.00px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
&quot;מבקש&quot; את 𝛼 7 ואת 𝛼 4
</div>
</div>
<div class="ppt-text-layer" style="left:38.3334%;top:37.5755%;width:5.8917%;height:7.2758%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 1
</div>
</div>
<div class="ppt-text-layer" style="left:56.4406%;top:37.8930%;width:11.7361%;height:7.2758%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 3
</div>
</div>
<div class="ppt-text-layer" style="left:17.7703%;top:29.3932%;width:11.7361%;height:7.2758%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 7
</div>
</div>
<div class="ppt-text-layer" style="left:49.5541%;top:47.5890%;width:5.8917%;height:7.2758%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 4
</div>
</div>
<div class="ppt-text-layer" style="left:56.4406%;top:29.5351%;width:11.7361%;height:7.2758%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 6
</div>
</div>
<div class="ppt-text-layer" style="left:80.8915%;top:33.0595%;width:11.7361%;height:7.2758%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 7
</div>
</div>
<div class="ppt-text-layer" style="left:11.6266%;top:62.4431%;width:82.0021%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#840900;opacity:1.000;border:0.75px solid #ba1500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
כל הזמן מבקשים את הקבוצה 𝛼 6 , 𝛼 7 אבל אף איבר בה לא נבחר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:23.9849%;top:71.6515%;width:55.4256%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#840900;opacity:1.000;border:0.75px solid #ba1500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
⇐ הריצה המסומנת אינה הוגנת חלש ביחס ל- 𝛼 6 , 𝛼 7
</div>
</div>
<div class="ppt-text-layer" style="left:28.5095%;top:81.2890%;width:41.6122%;height:5.8856%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#840900;opacity:1.000;border:0.75px solid #ba1500;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
⇐ הריצה אינה ∅,∅, 𝛼 6 , 𝛼 7 -הוגנת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה להנחת הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:3.7502%;top:17.7778%;width:93.7876%;height:7.3984%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
ℱ= 𝛼 1 , 𝛼 2 , 𝛼 3 , 𝛼 4 , 𝛼 4 , 𝛼 5 , 𝛼 5 , 𝛼 6 , 𝛼 6 , 𝛼 7 , 𝛼 7 , 𝛼 8
</div>
</div>
<div class="ppt-text-layer" style="left:21.7103%;top:59.4644%;width:75.4323%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל אחת מהקבוצות 𝛼 1 , 𝛼 2 , 𝛼 3 , 𝛼 4 צריכה להבחר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:9.1878%;top:69.2817%;width:87.9548%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לגבי כל אחת מהקבוצות 𝛼 4 , 𝛼 5 , 𝛼 5 , 𝛼 6 :
אם היא מאופשרת אינסוף פעמים, היא צריכה להיבחר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:5.5064%;top:84.4844%;width:91.6362%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לגבי כל אחת מהקבוצות 𝛼 6 , 𝛼 7 , 𝛼 7 , 𝛼 8 :
אם היא מאופשרת ברצף מזמן מסוים, היא צריכה להבחר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:50.0000%;top:39.2134%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.8653%;top:39.3454%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 3
</div>
</div>
<div class="ppt-text-layer" style="left:41.1259%;top:33.4215%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 7
</div>
</div>
<div class="ppt-text-layer" style="left:56.7590%;top:49.8403%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 4
</div>
</div>
<div class="ppt-text-layer" style="left:58.4752%;top:33.6135%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 6
</div>
</div>
<div class="ppt-text-layer" style="left:70.9001%;top:36.9349%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 7
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה להנחת הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:3.7502%;top:17.7778%;width:92.7007%;height:7.3984%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
ℱ= 𝛼 1 , 𝛼 2 , 𝛼 3 , 𝛼 4 , 𝛼 4 , 𝛼 5 , 𝛼 5 , 𝛼 6 , 𝛼 6 , 𝛼 7 , 𝛼 7 , 𝛼 8
</div>
</div>
<div class="ppt-text-layer" style="left:41.6667%;top:38.1842%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 1
</div>
</div>
<div class="ppt-text-layer" style="left:50.5013%;top:38.3162%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 3
</div>
</div>
<div class="ppt-text-layer" style="left:32.7620%;top:32.3924%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 7
</div>
</div>
<div class="ppt-text-layer" style="left:53.8629%;top:49.0590%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 5
</div>
</div>
<div class="ppt-text-layer" style="left:50.1113%;top:32.5844%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 8
</div>
</div>
<div class="ppt-text-layer" style="left:60.0967%;top:38.0287%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 6
</div>
</div>
<div class="ppt-text-layer" style="left:67.9708%;top:32.2392%;width:5.3847%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼 7
</div>
</div>
<div class="ppt-text-layer" style="left:21.7103%;top:59.4644%;width:75.4323%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל אחת מהקבוצות 𝛼 1 , 𝛼 2 , 𝛼 3 , 𝛼 4 צריכה להבחר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:9.1878%;top:69.2817%;width:87.9548%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לגבי כל אחת מהקבוצות 𝛼 4 , 𝛼 5 , 𝛼 5 , 𝛼 6 :
אם היא מאופשרת אינסוף פעמים, היא צריכה להיבחר אינסוף פעמים
</div>
</div>
<div class="ppt-text-layer" style="left:5.5064%;top:84.4844%;width:91.6362%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לגבי כל אחת מהקבוצות 𝛼 6 , 𝛼 7 , 𝛼 7 , 𝛼 8 :
אם היא מאופשרת ברצף מזמן מסוים, היא צריכה להבחר אינסוף פעמים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת למניעת הרעבה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
36
</div>
</div>
<div class="ppt-text-layer" style="left:42.9828%;top:21.7094%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:31.6217%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.3440%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:42.6487%;top:53.3333%;width:14.0344%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:14.9141%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:71.7198%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:27.6119%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:60.3587%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:64.1759%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.7109%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:20.6163%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:70.7248%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:56.4621%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:36.9508%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.9477%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:78.0653%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8706%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:66.9094%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:38.8378%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:53.6247%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.6765%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:62.0383%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:7.3524%;top:85.4403%;width:84.6268%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שלב ראשון: מריצים Model-Checker ומקבלים דוגמה נגדית 
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:5.0877%;top:78.8179%;width:89.8246%;height:18.6180%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שלב שני: מוסיפים אילוץ הוֹגְנוּת חזקה
ℱ= ∅, ente r 1 ,ente r 2 ,∅
ומקבלים את הדוגמה הנגדית שוב 
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
<div class="ppt-text-layer" style="left:42.9828%;top:21.7094%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:31.6217%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.3440%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:42.6487%;top:53.3333%;width:14.0344%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:14.9141%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:71.7198%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:27.6119%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:60.3587%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:64.1759%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.7109%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:20.6163%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:70.7248%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:56.4621%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:36.9508%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.9477%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:78.0653%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8706%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:66.9094%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:38.8378%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:53.6247%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.6765%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:62.0383%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת למניעת הרעבה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת למניעת הרעבה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
38
</div>
</div>
<div class="ppt-text-layer" style="left:42.9828%;top:21.7094%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:31.6217%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.3440%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:42.6487%;top:53.3333%;width:14.0344%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:14.9141%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:71.7198%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:27.6119%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:60.3587%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:64.1759%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.7109%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:20.6163%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:70.7248%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:56.4621%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:36.9508%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.9477%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:78.0653%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8706%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:66.9094%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:38.8378%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:53.6247%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.6765%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:62.0383%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:78.1197%;width:90.0000%;height:18.6180%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שלב שלישי: הפתרון הוא לחזק את האילוץ
ℱ′= ∅, enter 1 , enter 2 ,∅
עכשיו הריצה המדוברת אינה הוֹגֶנֶת 
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-039.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת למניעת הרעבה
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
<div class="ppt-text-layer" style="left:42.9828%;top:21.7094%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:31.6217%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.3440%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:42.6487%;top:53.3333%;width:14.0344%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:14.9141%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:71.7198%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:27.6119%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:60.3587%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:64.1759%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.7109%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:20.6163%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:70.7248%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:56.4621%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:36.9508%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.9477%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:78.0653%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8706%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:67.1555%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:38.8378%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:53.6247%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.6765%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:62.0383%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:29.8121%;top:84.4444%;width:37.8872%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
אבל יש עוד דוגמה נגדית 
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-040.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת למניעת הרעבה
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
<div class="ppt-text-layer" style="left:42.9828%;top:21.7094%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:31.6217%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.3440%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:42.6487%;top:53.3333%;width:14.0344%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:14.9141%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:71.7198%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:27.6119%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:60.3587%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:64.1759%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.7109%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:20.6163%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:70.7248%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:56.4621%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:36.9508%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.9477%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:78.0653%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8706%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:67.1555%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:38.8378%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:53.6247%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.6765%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:62.0383%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:4.3590%;top:78.3127%;width:91.2821%;height:18.6180%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כדי להתעלם גם מהדוגמה הנגדית הזאת נוסיף אילוצי הוֹגְנוּת חלשה:
ℱ′′= ∅, enter 1 , enter 2 , req 1 , req 2
עכשיו גם הריצה השנייה אינה הוֹגֶנֶת 
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-041.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרות: מסלולים ועקבות הוגנים
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
41
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:23.3333%;width:94.1667%;height:70.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור מערכת מעברים 𝑇𝑆 מסויימת:
מסלול 𝑠 0 → 𝑠 1 → 𝑠 2 ⋯ הוא ℱ-הוגן אם יש ריצה 𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 ⋯ ℱ-הוֹגֶנֶת
סימון: 𝐹𝑎𝑖𝑟𝑃𝑎𝑡ℎ𝑠ℱ 𝑠 היא קבוצת המסלולים ה ℱ-הוגנים המתחילים ב 𝑠
סימון: 𝐹𝑎𝑖𝑟𝑃𝑎𝑡ℎ𝑠ℱ 𝑇𝑆 היא קבוצת המסלולים ה ℱ-הוגנים המתחילים ב-𝐼
רצף עקבות 𝜎 הוא ℱ-הוגן אם קיימת ריצה ℱ-הוֹגֶנֶת 𝜌 כך ש 𝑡𝑟𝑎𝑐𝑒 𝜌 =𝜎
סימון: 𝐹𝑎𝑖𝑟𝑇𝑟𝑎𝑐𝑒 𝑠 ℱ 𝑠 = 𝑡𝑟𝑎𝑐𝑒 𝐹𝑎𝑖𝑟𝑃𝑎𝑡ℎ 𝑠 ℱ 𝑠
סימון:𝐹𝑎𝑖𝑟𝑇𝑟𝑎𝑐𝑒 𝑠 ℱ 𝑇𝑆 = 𝑡𝑟𝑎𝑐𝑒 𝐹𝑎𝑖𝑟𝑃𝑎𝑡ℎ 𝑠 ℱ 𝑇𝑆
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-042.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: קיום תכונה תחת הנחות הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
42
</div>
</div>
<div class="ppt-text-layer" style="left:6.7708%;top:21.1111%;width:88.3333%;height:74.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תזכורת: 𝑇𝑆 מקיימת את תכונת הזמן הליניארי 𝑃:
𝑇𝑆⊨ 𝑃 אם ורק אם 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆𝑃
  • אם כל העקבות שאפשר לקבל הן &quot;חוקיות&quot;
𝑇𝑆 מקיימת את תכונת הזמן הליניארי 𝑃 תחת הנחת הוֹגְנוּת ℱ :
𝑇𝑆 ⊨ ℱ 𝑃 אם ורק אם 𝐹𝑎𝑖𝑟𝑇𝑟𝑎𝑐𝑒𝑠ℱ 𝑇𝑆 ⊆𝑃
  • אם כל הריצות הוֹגְנוֹת אז 𝑇𝑆 ⊨ ℱ 𝑃 אם ורק אם 𝑇𝑆⊨𝑃
  • אם יש ריצה לא הוֹגֶנֶת אז יכול להיות 𝑇𝑆 ⊨ ℱ 𝑃 אבל לא 𝑇𝑆⊨𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-043.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת למניעה הדדית
</div>
</div>
<div class="ppt-text-layer" style="left:73.1377%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
43
</div>
</div>
<div class="ppt-text-layer" style="left:42.9828%;top:21.7094%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:31.6217%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.3440%;top:37.0940%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:42.6487%;top:53.3333%;width:14.0344%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:14.9141%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:71.7198%;top:53.3333%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:27.6119%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:60.3587%;top:70.4274%;width:13.3660%;height:5.1282%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:64.1759%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:33.7109%;top:20.0000%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:20.6163%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:70.7248%;top:35.7591%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:56.4621%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:36.9508%;top:27.9940%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:26.9477%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
enter1
</div>
</div>
<div class="ppt-text-layer" style="left:78.0653%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:15.8706%;top:61.9665%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:66.9094%;top:62.9371%;width:7.2282%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
enter2
</div>
</div>
<div class="ppt-text-layer" style="left:38.8378%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
req2
</div>
</div>
<div class="ppt-text-layer" style="left:53.6247%;top:43.5243%;width:5.5698%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
req1
</div>
</div>
<div class="ppt-text-layer" style="left:32.6765%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#2e14f0;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:62.0383%;top:47.4069%;width:4.2024%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
rel
</div>
</div>
<div class="ppt-text-layer" style="left:9.5622%;top:78.3127%;width:87.5000%;height:17.5653%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑃 = &quot;כל תהליך נכנס לקטע הקריטי שלו לעיתים תכופות&quot;
𝑇𝑆⊭𝑃 𝑇𝑆 ⊭ ℱ ′ 𝑃 𝑇𝑆 ⊨ ℱ ′′ 𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-044.png" alt="" />
<div class="ppt-text-layer" style="left:8.8680%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תוכן
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-045.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת בת מימוש
(Realizable Fairness)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
45
</div>
</div>
<div class="ppt-text-layer" style="left:6.2811%;top:30.5970%;width:89.1667%;height:32.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור מערכת מעברים 𝑇𝑆 והנחת הוֹגְנוּת ℱ,
ℱ בת מימוש ב-𝑇𝑆 אם לכל 𝑠∈𝑅𝑒𝑎𝑐ℎ(𝑇𝑆) מתקיים:
𝐹𝑎𝑖𝑟𝑃𝑎𝑡ℎ 𝑠 ℱ 𝑠 ≠ ∅
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:71.3863%;width:65.8333%;height:13.9123%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;border:0.75px solid #f2f2f2;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
במקרה כזה, כל מקטע ריצה התחלתי של 𝑇𝑆 ניתן להשלים לריצה הוֹגֶנֶת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-046.png" alt="" />
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
<div class="ppt-text-layer" style="left:1.6667%;top:21.1520%;width:96.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
האם תכונות בטיחות מושפעות מהנחות הוֹגְנוּת ?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:47.8707%;width:26.2500%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:48.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#d8ff7e;white-space:pre-wrap;width:100%;">
הוֹגְנוּת
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:47.7035%;width:30.2938%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:48.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffe45b;white-space:pre-wrap;width:100%;">
בטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-047.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות הַסֵּיפָא
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
<div class="ppt-text-layer" style="left:17.6471%;top:20.0000%;width:63.3333%;height:15.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם מקטע ריצה אינסופי 𝑟 הוא הוגן
אז כל הסיפות (suffixes) שלו הוֹגְנוֹת
</div>
</div>
<div class="ppt-text-layer" style="left:17.6471%;top:42.2222%;width:63.3333%;height:20.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם מקטע ריצה אינסופי 𝑟 הוא הוגן אז שרשור של 𝑟 אחרי כל מקטע ריצה סופי ייתן ריצה הוֹגֶנֶת
</div>
</div>
<div class="ppt-text-layer" style="left:8.2378%;top:82.5986%;width:31.9093%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מקטע התחלתי כלשהו
</div>
</div>
<div class="ppt-text-layer" style="left:60.6426%;top:81.4875%;width:18.9051%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
המשך הוגן 𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:10.1471%;top:72.8123%;width:81.2707%;height:7.0085%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 0 𝛼 0 𝑠 1 𝛼 1 𝑠 2 ⋯ 𝑠 𝑛−1 𝛼 𝑛−1 𝑠 𝑛 𝛼 𝑛 𝑠 𝑛+1 𝛼 𝑛+1 𝑠 𝑛+1 𝛼 𝑛+2 𝑠 𝑛+2 ⋯
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-048.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת בת מימוש ובטיחות
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
<div class="ppt-text-layer" style="left:0.8333%;top:29.4861%;width:96.6667%;height:39.4028%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור מערכת מעברים 𝑇𝑆, תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 (מעל אותה 𝐴𝑃) והנחת הוֹגְנוּת בת מימושℱ עבור 𝑇𝑆:
𝑇𝑆⊨ 𝑃 𝑠𝑎𝑓𝑒 אם ורק אם 𝑇𝑆 ⊨ ℱ 𝑃 𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:80.6298%;width:89.9708%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
תכונות בטיחות לא מושפעות מהנחות הוֹגְנוּת בנות מימוש
</div>
</div>
<div class="ppt-text-layer" style="left:2.6052%;top:68.2542%;width:13.6073%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו טענה זאת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-049.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוֹגְנוּת בת מימוש ובטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
49
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:22.2222%;width:91.9118%;height:71.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
משפט: עבור מערכת מעברים 𝑇𝑆, תכונת בטיחות 𝑃 (שתיהן מעל אותה 𝐴𝑃)
והנחת הוֹגְנוּת בת מימושℱ עבור 𝑇𝑆:
𝑇𝑆⊨𝑃 אם ורק אם 𝑇𝑆 ⊨ ℱ 𝑃
הוכחה: כיוון אחד טריוויאלי - אם 𝑇𝑆⊨𝑃 אז ברור ש- 𝑇𝑆 ⊨ ℱ 𝑃
בכיוון השני –
  אם 𝑇𝑆⊭𝑃
  אז קיימת ריצה 𝑟 שאיננה מקיימת את 𝑃.
  בגלל ש-𝑃 תכונת בטיחות, יש ל-𝑟 רישא שרצף העקבות שלה הוא רישא רעה של 𝑃.
  כיוון שהנחת ההוגנות בת-מימוש, ניתן להמשיך את הרישא הזאת לריצה הוגנת 𝑟′.
  כיוון של𝑟′- יש רישא רעה, רצף העקבות שלה איננו מקיים את 𝑃 ולכן 𝑇𝑆 ⊭ ℱ 𝑃.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-050.png" alt="" />
<div class="ppt-text-layer" style="left:-0.3573%;top:3.3333%;width:94.5239%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הנחות הוֹגְנוּת שאינן בנות מימוש
עלולות לפגוע גם בתכונות בטיחות!
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
<div class="ppt-text-layer" style="left:5.8333%;top:58.5634%;width:87.5000%;height:33.3176%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונה: &quot;אף פעם לא 𝑝&quot; 𝑃 =
הנחת הוֹגְנוּת בלתי מותנית: ℱ= 𝛼 ,∅,∅
הנחה זו אינה בת מימוש כיוון שהמצב הימני נגיש אבל חסר ריצות הוֹגְנוֹת
𝑇𝑆 ⊨ ℱ 𝑃 אבל 𝑇𝑆⊭𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:33.4656%;top:51.6673%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:43.3172%;top:44.9455%;width:4.1667%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
∅
</div>
</div>
<div class="ppt-text-layer" style="left:61.5317%;top:44.9455%;width:12.5000%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑝 }
</div>
</div>
<div class="ppt-text-layer" style="left:50.8131%;top:35.5556%;width:4.3224%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
<div class="ppt-text-layer" style="left:68.3333%;top:52.7596%;width:4.3224%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/16-fairness/slide-051.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיכום נושא הוֹגְנוּת
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
<div class="ppt-text-layer" style="left:4.1667%;top:18.8889%;width:91.6667%;height:73.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• אילוצי הוֹגְנוּת פוסלים ריצות לא מציאותיות
  • כלומר: מגבילות את רצפי הפעולות שיכולים לקרות
  • נחוצות לאימות תכונות חַיּוּת
• אילוצי הוֹגְנוּת בלתי מותנית, חזקה וחלשה
  • הוֹגְנוּת בלתי מותנית ⇐ הוֹגְנוּת חזקה ⇐ הוֹגְנוּת חלשה
• הנחות הוֹגְנוּת מאפשרות הגדרת אילוצים על פעולות שונות
• תכונות הוֹגְנוּת בנות מימוש אינן נוגעות לתכונות בטיחות
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
