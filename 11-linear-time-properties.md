---
theme: default
defaults:
  layout: full
lineNumbers: false
download: true
exportFilename: 11-linear-time-properties
htmlAttrs:
  dir: rtl
  lang: heb
---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות זמן לינארי
Linear-Time Properties
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:87.3772%;top:-0.8058%;width:11.4335%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Aharoni','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
564
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-002.png" alt="" />
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
<div class="ppt-text-layer" style="left:5.0000%;top:-3.3333%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקות מודל (Model Checking)
</div>
</div>
<div class="ppt-text-layer" style="left:59.1667%;top:24.4444%;width:13.3333%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מערכת
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:42.7778%;width:15.0000%;height:8.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מידול
</div>
</div>
<div class="ppt-text-layer" style="left:49.0000%;top:82.2222%;width:16.0000%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
דוגמה נגדית
</div>
</div>
<div class="ppt-text-layer" style="left:31.5833%;top:57.7778%;width:20.8333%;height:13.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בדיקות מודל
(Model Cecking)
</div>
</div>
<div class="ppt-text-layer" style="left:10.4167%;top:24.4444%;width:13.3333%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דרישות
</div>
</div>
<div class="ppt-text-layer" style="left:9.5833%;top:42.7778%;width:15.0000%;height:8.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
פירמול
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:58.8889%;width:19.1667%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
תכונות פורמליות
</div>
</div>
<div class="ppt-text-layer" style="left:57.5000%;top:58.8889%;width:16.6667%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מודל של המערכת
</div>
</div>
<div class="ppt-text-layer" style="left:72.5000%;top:83.7778%;width:15.0000%;height:8.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
סימולציה
</div>
</div>
<div class="ppt-text-layer" style="left:19.0000%;top:82.2222%;width:16.0000%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
התכונות הוכחה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:7.8526%;top:81.3315%;width:84.4231%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
נגדיר את סוגי התכונות השונים וּנְפַתֵּחַ אלגוריתמים
לבדיקה אם מערכת מעברים נתונה מקיימת תכונות נתונות
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תוכנית לפרק השני
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
<div class="ppt-text-layer" style="left:5.0641%;top:26.3338%;width:90.0000%;height:54.9977%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
קיימים סוגים שונים של תכונות:
  • אנחנו נתמקד בתכונות של הריצות של התוכנית (להבדיל מתכונות של התוכנית עצמה)
  • לתכונות כאלה נקרא &quot;תכונות זמן לינארי&quot; – Linear Time Properties
נעבור מתכונות פשוטות לתכונות מורכבות יותר:
  • קִפָּאוֹן – המערכת אף פעם לא &quot;נתקעת&quot;
  • תכונות &quot;שְׁמוּרָה&quot; – בכל ריצה, בכל מצב בריצה, מתקיים תנאי רצוי
  • תכונות בטיחות – לא יכול להיות שהמערכת תבצע רצף נתון של פעולות לא חוקית
  • תכונות מורכבות יותר (הכוללות חַיּוּת) – למשל, פסוק אטומי מסוים מתקיים באופן תדיר
</div>
</div>
<div class="ppt-text-layer" style="left:13.2845%;top:15.9162%;width:75.9989%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
נְעַמֵּת מערכות מעברים מול תכונות רצויות ושאינן רצויות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-004.png" alt="" />
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
4
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
קִפָּאוֹן (deadlock)
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
<div class="ppt-text-layer" style="left:1.6667%;top:21.1111%;width:96.6667%;height:64.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• לתוכניות סדרתיות יש נקודת התחלה ונקודת סוף
• במערכת תגובתיות, בדרך כלל, לא רוצים שהחישוב יסתיים
• הגדרת המושג קִפָּאוֹן מבחינתנו: אם יש מצב נגיש וסופני (ללא עוקבים)
• מצב נפוץ: שתי מערכות מעברים החוסמות זו את זו
</div>
</div>
<div class="ppt-text-layer" style="left:45.8451%;top:69.5927%;width:5.0000%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1
</div>
</div>
<div class="ppt-text-layer" style="left:45.8451%;top:81.8149%;width:5.0000%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 2
</div>
</div>
<div class="ppt-text-layer" style="left:40.5062%;top:75.5504%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:52.5118%;top:75.1483%;width:4.3224%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
<div class="ppt-text-layer" style="left:21.2953%;top:69.4607%;width:5.0000%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 1
</div>
</div>
<div class="ppt-text-layer" style="left:21.2953%;top:81.6829%;width:5.0000%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:left;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 2
</div>
</div>
<div class="ppt-text-layer" style="left:15.9564%;top:75.6569%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛼
</div>
</div>
<div class="ppt-text-layer" style="left:27.9620%;top:76.1274%;width:4.3224%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝛽
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
6
</div>
</div>
<div class="ppt-text-layer" style="left:13.5098%;top:87.4294%;width:72.9486%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffcc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
האם ניתן להגיע ל-deadlock במערכת הזאת?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:20.0000%;top:4.0624%;width:61.6667%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: תקלה שקרתה
ל-pathfinder במאדים
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
<div class="ppt-text-layer" style="left:5.8563%;top:25.3408%;width:44.6101%;height:30.9661%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#262626;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Consolas','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
active proctype high() /* can run at any time */
{
end: do
:: h_state = waiting;
atomic { mutex == free -&gt; mutex = busy };
h_state = running;
/* critical section - consume data */
atomic { h_state = idle; mutex = free }
od
}
</div>
</div>
<div class="ppt-text-layer" style="left:52.5000%;top:25.4293%;width:44.6101%;height:33.4345%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#262626;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Consolas','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
active proctype low()
provided (h_state == idle) /* scheduling rule */
{
end: do
:: l_state = waiting;
atomic { mutex == free -&gt; mutex = busy };
l_state = running;
/* critical section - produce data */
atomic { l_state = idle; mutex = free }
od
}
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:65.5304%;width:90.0000%;height:25.5807%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
A high-priority process consumes data produced by a low-priority process. Data consumption and production happen under the protection of a mutex lock that conflicts with the scheduling priorities which can deadlock the system if high() starts up while low() has the lock.
There are 12 reachable states in the full state space - two of which are deadlock
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: המיסטיקנים הסינים
Dining Philosophers
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
<div class="ppt-text-layer" style="left:4.1667%;top:60.0000%;width:91.6667%;height:38.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
פילוסופים סינים יושבים סביב שולחן שבמרכזו סיר אורז
חיי הסובבים מורכבים מאכילה, חשיבה והמתנה...
כדי לאכול אורז, פילוסוף זקוק לשני מקלות האכילה
בין שני פילוסופים יש מקל אכילה אחד בלבד
רק אחד יכול להשתמש במקל בזמן נתון
</div>
</div>
<div class="ppt-text-layer" style="left:48.6100%;top:19.0725%;width:5.7823%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.1151%;top:21.9353%;width:9.4736%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
S𝑡𝑖𝑐 𝑘 1
</div>
</div>
<div class="ppt-text-layer" style="left:62.3485%;top:43.8873%;width:9.5318%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
S𝑡𝑖𝑐 𝑘 2
</div>
</div>
<div class="ppt-text-layer" style="left:46.5454%;top:53.5035%;width:9.5318%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
S𝑡𝑖𝑐 𝑘 3
</div>
</div>
<div class="ppt-text-layer" style="left:31.8658%;top:40.3133%;width:10.2155%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐 𝑘 4
</div>
</div>
<div class="ppt-text-layer" style="left:35.8045%;top:22.4352%;width:10.2155%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐 𝑘 0
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:30.0399%;width:5.7823%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.5000%;top:49.0725%;width:5.7444%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 3
</div>
</div>
<div class="ppt-text-layer" style="left:41.0302%;top:49.0725%;width:5.6365%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 4
</div>
</div>
<div class="ppt-text-layer" style="left:36.6667%;top:30.9353%;width:5.7444%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 0
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: המיסטיקנים הסינים
Dining (Chinese) Philosophers
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
<div class="ppt-text-layer" style="left:48.6100%;top:19.0725%;width:5.7823%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.1151%;top:21.9353%;width:9.4736%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
S𝑡𝑖𝑐 𝑘 1
</div>
</div>
<div class="ppt-text-layer" style="left:62.3485%;top:43.8873%;width:9.5318%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
S𝑡𝑖𝑐 𝑘 2
</div>
</div>
<div class="ppt-text-layer" style="left:46.5454%;top:53.5035%;width:9.5318%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
S𝑡𝑖𝑐 𝑘 3
</div>
</div>
<div class="ppt-text-layer" style="left:31.8658%;top:40.3133%;width:10.2155%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐 𝑘 4
</div>
</div>
<div class="ppt-text-layer" style="left:35.8045%;top:22.4352%;width:10.2155%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐 𝑘 0
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:30.0399%;width:5.7823%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.5000%;top:49.0725%;width:5.7444%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 3
</div>
</div>
<div class="ppt-text-layer" style="left:41.0302%;top:49.0725%;width:5.6365%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 4
</div>
</div>
<div class="ppt-text-layer" style="left:36.6667%;top:30.9353%;width:5.7444%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 0
</div>
</div>
<div class="ppt-text-layer" style="left:25.9404%;top:65.4406%;width:48.2128%;height:22.8880%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#677367;white-space:pre-wrap;width:100%;">
לאור הדברים הפשוטים באמת
אנחנו חיים את חיינו
למשל בלי הסברים רק לקבל ולתת
זה לא קל אבל מה יש עוד בינינו?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: המיסטיקנים הסינים
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
<div class="ppt-text-layer" style="left:9.1667%;top:30.0000%;width:87.5000%;height:54.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• מצב קִפָּאוֹן: כשכל פילוסוף מחזיק מקל אכילה אחד
• משימה: תכנון פרוטוקול שֶׁיִּמְנַע קִפָּאוֹן
• פתרון מספק: לפחות אחד יוכל לאכול ולחשוב אינסוף פעמים
• פתרון עדיף: כל הפילוסופים יוכלו לאכול ולחשוב אינסוף פעמים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
פתרון טבעי:
מערכת מעברים לפילוסוף והמקל ה-𝑖
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
<div class="ppt-text-layer" style="left:82.1127%;top:18.8889%;width:15.3765%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:63.3952%;top:20.5636%;width:16.4968%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
חשיבה
</div>
</div>
<div class="ppt-text-layer" style="left:63.3952%;top:54.9898%;width:16.4968%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אכילה
</div>
</div>
<div class="ppt-text-layer" style="left:77.6713%;top:38.2685%;width:16.4968%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
המתנה למקל מימין
</div>
</div>
<div class="ppt-text-layer" style="left:77.6713%;top:72.3735%;width:16.4968%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
החזרת המקל מימין
</div>
</div>
<div class="ppt-text-layer" style="left:47.4873%;top:38.2685%;width:18.1287%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
המתנה למקל משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:47.8501%;top:71.8093%;width:18.0156%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
החזרת המקל משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:47.4873%;top:19.1312%;width:12.9748%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:48.4158%;top:29.5687%;width:15.7986%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:78.9587%;top:29.5800%;width:13.3969%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:76.8938%;top:47.6214%;width:15.7986%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:79.1644%;top:64.0284%;width:11.8961%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:48.7044%;top:63.1080%;width:15.0070%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:52.2789%;top:47.2902%;width:12.8448%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:66.6667%;top:79.2324%;width:8.1749%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃ℎ𝑖 𝑙 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:29.1028%;top:34.6225%;width:12.1431%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:23.7545%;top:47.7425%;width:11.7946%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:1.9942%;top:34.3510%;width:12.4785%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖+1
</div>
</div>
<div class="ppt-text-layer" style="left:7.0417%;top:47.1646%;width:13.9334%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖+1
</div>
</div>
<div class="ppt-text-layer" style="left:15.4355%;top:35.9096%;width:13.4413%;height:6.9154%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
פנוי
</div>
</div>
<div class="ppt-text-layer" style="left:5.0894%;top:54.4711%;width:13.4413%;height:10.6746%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:25.8673%;top:54.3911%;width:13.4413%;height:10.6746%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף מימין
</div>
</div>
<div class="ppt-text-layer" style="left:17.5600%;top:67.7754%;width:9.2169%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐𝑘 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:91.9444%;width:95.2767%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃ℎ𝑖 𝑙 4 ||| 𝑆𝑡𝑖𝑐 𝑘 3 ||| 𝑃ℎ𝑖 𝑙 3 ||| 𝑆𝑡𝑖𝑐 𝑘 2 ||| 𝑃ℎ𝑖 𝑙 2 ||| 𝑆𝑡𝑖𝑐 𝑘 1 ||| 𝑃ℎ𝑖 𝑙 1 ||| 𝑆𝑡𝑖𝑐 𝑘 0 ||| 𝑃ℎ𝑖 𝑙 0 ||| 𝑆𝑡𝑖𝑐 𝑘 4
</div>
</div>
<div class="ppt-text-layer" style="left:54.8391%;top:85.9360%;width:44.3561%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
סנכרון בזוגות על כל פעולה בעלת שם זהה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
פתרון טבעי:
מערכת מעברים לפילוסוף והמקל ה-𝑖
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
<div class="ppt-text-layer" style="left:45.7469%;top:36.4418%;width:10.7085%;height:5.3836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
חושב
</div>
</div>
<div class="ppt-text-layer" style="left:45.7469%;top:59.9951%;width:10.7085%;height:5.3836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוכל
</div>
</div>
<div class="ppt-text-layer" style="left:55.0139%;top:48.5549%;width:10.7085%;height:5.3836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ממתין למקל מימין
</div>
</div>
<div class="ppt-text-layer" style="left:55.0139%;top:71.8884%;width:10.7085%;height:5.3836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מחזיר המקל מימין
</div>
</div>
<div class="ppt-text-layer" style="left:34.8325%;top:48.5549%;width:12.3560%;height:5.3836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ממתין למקל משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:35.6562%;top:71.5024%;width:11.6944%;height:5.3836%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מחזיר המקל משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:57.0216%;top:34.1468%;width:12.4187%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 4,5
</div>
</div>
<div class="ppt-text-layer" style="left:33.5627%;top:34.1468%;width:12.4187%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 5,5
</div>
</div>
<div class="ppt-text-layer" style="left:33.8535%;top:41.7564%;width:12.7672%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 4,5
</div>
</div>
<div class="ppt-text-layer" style="left:55.6088%;top:41.8129%;width:12.7672%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 5,5
</div>
</div>
<div class="ppt-text-layer" style="left:54.5910%;top:54.0236%;width:12.7672%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 4,5
</div>
</div>
<div class="ppt-text-layer" style="left:55.8893%;top:64.9901%;width:7.7221%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 5,5
</div>
</div>
<div class="ppt-text-layer" style="left:35.0324%;top:64.6641%;width:9.7414%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 4,5
</div>
</div>
<div class="ppt-text-layer" style="left:36.3799%;top:54.5836%;width:8.3379%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 5,5
</div>
</div>
<div class="ppt-text-layer" style="left:47.1346%;top:77.2721%;width:7.7941%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃ℎ𝑖 𝑙 5
</div>
</div>
<div class="ppt-text-layer" style="left:87.6068%;top:25.5556%;width:12.7672%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 4,4
</div>
</div>
<div class="ppt-text-layer" style="left:84.7870%;top:39.1588%;width:12.4187%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 4,4
</div>
</div>
<div class="ppt-text-layer" style="left:66.8043%;top:25.6898%;width:8.9644%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 4,5
</div>
</div>
<div class="ppt-text-layer" style="left:69.5155%;top:38.4897%;width:12.4187%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 4,5
</div>
</div>
<div class="ppt-text-layer" style="left:78.8107%;top:27.3259%;width:9.6560%;height:6.9154%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
פנוי
</div>
</div>
<div class="ppt-text-layer" style="left:71.3783%;top:47.8319%;width:9.6560%;height:9.9459%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:86.3048%;top:47.7518%;width:9.6560%;height:10.0259%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף מימין
</div>
</div>
<div class="ppt-text-layer" style="left:80.3370%;top:59.1917%;width:9.5745%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐𝑘 4
</div>
</div>
<div class="ppt-text-layer" style="left:21.7616%;top:26.9198%;width:12.7672%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 5,5
</div>
</div>
<div class="ppt-text-layer" style="left:17.5730%;top:40.0398%;width:12.4187%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 5,5
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:26.4908%;width:9.7727%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 5,6
</div>
</div>
<div class="ppt-text-layer" style="left:0.9244%;top:39.3707%;width:12.4187%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 5,6
</div>
</div>
<div class="ppt-text-layer" style="left:11.0579%;top:28.2069%;width:10.5267%;height:6.9154%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
פנוי
</div>
</div>
<div class="ppt-text-layer" style="left:2.9552%;top:48.7129%;width:10.5267%;height:10.1760%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:19.2277%;top:48.6328%;width:10.5267%;height:10.1760%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף מימין
</div>
</div>
<div class="ppt-text-layer" style="left:12.7217%;top:60.0727%;width:9.5745%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑆𝑡𝑖𝑐𝑘 5
</div>
</div>
<div class="ppt-text-layer" style="left:1.3809%;top:90.8119%;width:95.2767%;height:13.6767%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
|| | 𝑖=0 n−1 ( Phil 𝑖 ||| Stick 𝑖 )
</div>
</div>
<div class="ppt-text-layer" style="left:54.9287%;top:83.7800%;width:44.3561%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
סנכרון בזוגות על כל פעולה בעלת שם זהה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הפילוסופים נתקעים!
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
<div class="ppt-text-layer" style="left:1.6667%;top:27.7778%;width:96.6667%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• אם לא קובעים פרוטוקול אפשר להגיע לקִפָּאוֹן
• לדוגמה: אם כל הפילוסופים מרימים את המקל השמאלי
• מצב התחלתי: 〈𝑡ℎ𝑖𝑛𝑘, 𝑎𝑣𝑎𝑖𝑙, 𝑡ℎ𝑖𝑛𝑘, 𝑎𝑣𝑎𝑖𝑙, 𝑡ℎ𝑖𝑛𝑘, 𝑎𝑣𝑎𝑖𝑙, 𝑡ℎ𝑖𝑛𝑘, 𝑎𝑣𝑎𝑖𝑙, 𝑡ℎ𝑖𝑛𝑘, 𝑎𝑣𝑎𝑖𝑙〉
• רצף פעולות: 𝑟𝑒𝑞𝑢𝑒𝑠𝑡4,3, 𝑟𝑒𝑞𝑢𝑒𝑠𝑡3,2, 𝑟𝑒𝑞𝑢𝑒𝑠𝑡2,1, 𝑟𝑒𝑞𝑢𝑒𝑠𝑡1,0, 𝑟𝑒𝑞𝑢𝑒𝑠𝑡0,4
• מצב אחרון: 〈𝑤𝑎𝑖𝑡𝑅, 𝑜𝑐𝑐𝑅, 𝑤𝑎𝑖𝑡𝑅, 𝑜𝑐𝑐𝑅, 𝑤𝑎𝑖𝑡𝑅, 𝑜𝑐𝑐𝑅, 𝑤𝑎𝑖𝑡𝑅, 𝑜𝑐𝑐𝑅, 𝑤𝑎𝑖𝑡𝑅〉
• המצב האחרון הוא קִפָּאוֹן - כל פילוסוף ממתין לפינוי המקל מימינו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
פתרון לבעיית הפילוסופים שננעלו
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
<div class="ppt-text-layer" style="left:62.5140%;top:20.1830%;width:16.3960%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
חושב
</div>
</div>
<div class="ppt-text-layer" style="left:62.5140%;top:54.6092%;width:16.3960%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוכל
</div>
</div>
<div class="ppt-text-layer" style="left:76.7028%;top:37.8879%;width:16.3960%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ממתין למקל מימין
</div>
</div>
<div class="ppt-text-layer" style="left:76.7028%;top:71.9929%;width:16.3960%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מחזיר המקל מימין
</div>
</div>
<div class="ppt-text-layer" style="left:45.8027%;top:37.8879%;width:18.9184%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ממתין למקל משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:47.0639%;top:71.4287%;width:17.9054%;height:7.8689%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מחזיר המקל משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:81.5444%;top:18.9478%;width:15.3765%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:42.5000%;top:18.7506%;width:12.9748%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:47.1128%;top:28.9096%;width:15.7986%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:78.4461%;top:29.3912%;width:13.4516%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠𝑡𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:76.9476%;top:47.5289%;width:15.7986%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:77.7717%;top:63.6438%;width:12.9748%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:48.2285%;top:62.7843%;width:15.3765%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖−1,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:51.7197%;top:46.9057%;width:13.3969%;height:5.5631%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:24.3549%;top:34.6989%;width:12.1431%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:25.0000%;top:63.1950%;width:11.7946%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:59.8617%;width:14.2819%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑞𝑢𝑒𝑠 𝑡 𝑖,𝑖+1
</div>
</div>
<div class="ppt-text-layer" style="left:10.0724%;top:34.6989%;width:13.9334%;height:5.0937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑙𝑒𝑎𝑠 𝑒 𝑖,𝑖+1
</div>
</div>
<div class="ppt-text-layer" style="left:15.7039%;top:23.5822%;width:13.4413%;height:6.9154%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
פנוי
</div>
</div>
<div class="ppt-text-layer" style="left:4.6594%;top:45.4173%;width:13.4413%;height:10.2795%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש הפילוסוף משמאל
</div>
</div>
<div class="ppt-text-layer" style="left:29.1667%;top:45.4173%;width:13.4413%;height:10.2795%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בשימוש
הפילוסוף מימין
</div>
</div>
<div class="ppt-text-layer" style="left:16.9374%;top:69.8925%;width:13.4413%;height:6.9154%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffcc;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
פנוי
</div>
</div>
<div class="ppt-text-layer" style="left:11.3901%;top:14.9790%;width:24.0380%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקלות 1,3 מתחילים כאן
</div>
</div>
<div class="ppt-text-layer" style="left:9.2638%;top:80.5572%;width:25.7385%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקלות 0,2,4 מתחילים כאן
</div>
</div>
<div class="ppt-text-layer" style="left:14.5833%;top:87.2422%;width:73.3333%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#003fbc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
אפשר לבדוק באמצעות הכלי שתפתחו שהפרוטוקול עונה
על בעיית המניעה ההדדית ועל בעיית ההרעבה
</div>
</div>
<div class="ppt-text-layer" style="left:46.2613%;top:80.9728%;width:48.7387%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מערכות המעברים של הפילוסופים נשארות ללא שינוי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
חסינות לשגיאות (robustness)
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:97.7124%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
15
</div>
</div>
<div class="ppt-text-layer" style="left:3.7745%;top:20.0000%;width:90.8333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• דרישה נוספת, מעבר למניעת קִפָּאוֹן, שלפעמים דורשים ממערכות מבוזרות
• במקרה של הפילוסופים הסועדים: הבטחת תכונות המניעה ההדדית וחוסר הרעבה גם אם אחד הסועדים &quot;תָּקוּל&quot;
• פילוסוף &quot;תָּקוּל&quot; נתקע במצב חשיבה לעד
• אפשר להוסיף חסינות ע&quot;י:
הפילוסוף ה 𝑖+1 יכול לקחת את המקל ה 𝑖+1 גם אם הפילוסוף 𝑖 חושב
• מוסיפים משתנה בוליאני 𝑥𝑖 המסמן לסועדים האחרים אם הפילוסוף 𝑖 חושב
</div>
</div>
<div class="ppt-text-layer" style="left:8.6029%;top:81.3287%;width:82.7941%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כדי להכניס את המשתנים,
עוברים ממודל של מערכות מעברים למודל של מערכת ערוצים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אלגוריתם בדיקה
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
<div class="ppt-text-layer" style="left:10.0000%;top:18.8889%;width:85.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
איך נבדוק שאין הרעבה
במערכת ערוצים 𝑃 𝐺 1 |⋯|𝑃 𝐺 𝑛
או בקוד פרומלה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-017.png" alt="" />
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
17
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:4.9256%;top:2.2222%;width:89.7688%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה רצה:
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
18
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
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:8.4382%;top:-1.9611%;width:86.9005%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
האם השגנו מניעה הדדית?
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
<div class="ppt-text-layer" style="left:41.9020%;top:21.8571%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑛2, 𝑦↦1
</div>
</div>
<div class="ppt-text-layer" style="left:29.3266%;top:39.4681%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑛2, 𝑦↦1
</div>
</div>
<div class="ppt-text-layer" style="left:54.4775%;top:39.4681%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑤2, 𝑦↦1
</div>
</div>
<div class="ppt-text-layer" style="left:41.5322%;top:58.0575%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑤2, 𝑦↦1
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:58.0575%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑛2, 𝑦↦0
</div>
</div>
<div class="ppt-text-layer" style="left:73.7105%;top:58.0575%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑛1, 𝑐2, 𝑦↦0
</div>
</div>
<div class="ppt-text-layer" style="left:24.8882%;top:77.6253%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑐1, 𝑤2, 𝑦↦0
</div>
</div>
<div class="ppt-text-layer" style="left:61.1351%;top:77.6253%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑤1, 𝑐2, 𝑦↦0
</div>
</div>
<div class="ppt-text-layer" style="left:19.0438%;top:64.0937%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:83.9037%;top:64.0937%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:71.0919%;top:83.5387%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:34.2578%;top:83.4957%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:55.0000%;top:27.7778%;width:4.2109%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
∅
</div>
</div>
<div class="ppt-text-layer" style="left:66.6667%;top:45.5556%;width:4.2109%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#7030a0;white-space:pre-wrap;width:100%;">
∅
</div>
</div>
<div class="ppt-text-layer" style="left:40.8333%;top:45.5555%;width:4.2109%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
∅
</div>
</div>
<div class="ppt-text-layer" style="left:52.5000%;top:64.4444%;width:4.2109%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
∅
</div>
</div>
<div class="ppt-text-layer" style="left:12.2662%;top:91.1111%;width:66.9005%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כן, מכיוון שאין מצב נגיש המכיל גם את𝑐𝑟𝑖𝑡1 וגם את 𝑐𝑟𝑖𝑡2
</div>
</div>
<div class="ppt-text-layer" style="left:3.3848%;top:15.8127%;width:17.7628%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆 𝑃 𝐺 1 ||𝑃 𝐺 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-020.png" alt="" />
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
<div class="ppt-text-layer" style="left:5.0000%;top:-1.1111%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: ריצות
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:25.5556%;width:98.3333%;height:65.9954%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:19.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• מקטע ריצה סופי של מערכת מעברים הוא רצף מתחלף של מצבים ופעולות המסתיים במצב:
• מקטע ריצה אינסופי של מערכת מעברים הוא רצף מתחלף אינסופי של מצבים ופעולות:
• ריצה של מערכת מצבים היא מקטע ריצה התחלתי ומקסימאלי
  • מקטע ריצה מקסימאלי הוא מקטע ריצה סופי המסיים במצב ללא עוקבים, או מקטע ריצה אינסופי
  • מקטע ריצה הוא התחלתי אם 𝑠 0 ∈𝐼
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סימונים לטיפול במקטעי מסלול
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
<div class="ppt-text-layer" style="left:5.0000%;top:24.4444%;width:89.1667%;height:67.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור מקטע מסלול 𝜋= 𝑠 0 𝑠 1 …:
  • 𝑓𝑖𝑟𝑠𝑡 𝜋 = 𝑠 0
  • אם 𝜋 סופי, באורך 𝑛, נסמן 𝑙𝑎𝑠𝑡(𝜋) = 𝑠 𝑛
  • עבור 𝑗≥0
    • האות ה 𝑗, 𝑠 𝑗 ,של 𝜋 תסומן 𝜋 𝑗
    • הרישא 𝑠 0 𝑠 1 … 𝑠 𝑗 תסומן 𝜋[..𝑗]
    • הסיפא 𝑠 𝑗 𝑠 𝑗+1 … תסומן 𝜋[𝑗..]
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
עֲקֵבוֹת (traces)
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
22
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:21.3700%;width:93.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:19.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תהי 𝑇𝑆 =〈𝑆, 𝐴𝑐𝑡, →, 𝐼, 𝐴𝑃, 𝐿〉 מערכת מעברים בלי מצבים סופניים (ללא קיפאון).
זה אומר שכל הריצות הן באורף אינסופי.
• העקבות של מקטע מסלול 𝜋= 𝑠 0 𝑠 1 …
  𝑡𝑟𝑎𝑐𝑒(𝜋)=𝐿(𝑠0)𝐿(𝑠1)…
• קבוצת העקבות של קבוצת מסלולים Π :
  𝑡𝑟𝑎𝑐𝑒(Π)={ 𝑡𝑟𝑎𝑐𝑒(𝜋) :𝜋∈Π}
  • סימונים:
    𝑇𝑟𝑎𝑐𝑒𝑠(𝑠)=𝑡𝑟𝑎𝑐𝑒(𝑃𝑎𝑡ℎ𝑠(𝑠))
  𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 = 𝑠∈𝐼 𝑇𝑟𝑎𝑐𝑒𝑠(𝑠)
</div>
</div>
<div class="ppt-text-layer" style="left:-0.8333%;top:71.1111%;width:57.5000%;height:23.5397%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
      𝑇𝑟𝑎𝑐𝑒𝑠𝑓𝑖𝑛 𝑠 =𝑡𝑟𝑎𝑐𝑒 𝑃𝑎𝑡ℎ 𝑠 𝑓𝑖𝑛 𝑠
      𝑇𝑟𝑎𝑐𝑒𝑠𝑓𝑖𝑛 𝑇𝑆 = 𝑠∈𝐼 𝑇𝑟𝑎𝑐𝑒 𝑠 𝑓𝑖𝑛 (𝑠)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: מסלול ועקבותיו
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
<div class="ppt-text-layer" style="left:2.5000%;top:26.6667%;width:95.8333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נניח 𝐴𝑃={𝑐𝑟𝑖𝑡1, 𝑐𝑟𝑖𝑡2}
• מצב מתויג ב-𝑐𝑟𝑖 𝑡 𝑖 אם יש
תהליך העומד במקום 𝑐𝑟𝑖 𝑡 𝑖
• דוגמה למסלול:
𝜋= 𝑛1, 𝑛2, 𝑦=1 → 𝑤1, 𝑛2, 𝑦=1 → 𝑐1, 𝑛2, 𝑦=0 → 𝑛1, 𝑛2, 𝑦=1
→ 𝑛1, 𝑤2, 𝑦=1 → 𝑛1, 𝑐2, 𝑦=0 →…
• עקבות המסלול:
𝑡𝑟𝑎𝑐𝑒 𝜋 =∅ ∅ {𝑐𝑟𝑖 𝑡 1 } ∅ ∅ {𝑐𝑟𝑖 𝑡 2 } ∅ ∅ {𝑐𝑟𝑖 𝑡 1 } ∅ ∅ {𝑐𝑟𝑖 𝑡 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:37.4352%;top:24.5117%;width:7.6651%;height:4.2714%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#0070c0;opacity:1.000;border:3.35px solid #002060;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
noncrit2
</div>
</div>
<div class="ppt-text-layer" style="left:37.4352%;top:43.1988%;width:7.6651%;height:4.2714%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#0070c0;opacity:1.000;border:3.35px solid #002060;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
crit2
</div>
</div>
<div class="ppt-text-layer" style="left:37.4352%;top:33.8552%;width:7.6651%;height:4.2714%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#0070c0;opacity:1.000;border:3.35px solid #002060;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
wait2
</div>
</div>
<div class="ppt-text-layer" style="left:39.4302%;top:38.7609%;width:19.0493%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦&gt;0 :𝑦 :=𝑦−1
</div>
</div>
<div class="ppt-text-layer" style="left:26.2379%;top:22.2620%;width:12.3590%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦 :=𝑦+1
</div>
</div>
<div class="ppt-text-layer" style="left:10.9200%;top:23.6465%;width:7.6651%;height:4.2714%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
noncrit1
</div>
</div>
<div class="ppt-text-layer" style="left:10.9200%;top:42.3337%;width:7.6651%;height:4.2714%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
crit1
</div>
</div>
<div class="ppt-text-layer" style="left:10.9200%;top:32.9901%;width:7.6651%;height:4.2714%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
wait1
</div>
</div>
<div class="ppt-text-layer" style="left:13.0128%;top:37.2964%;width:19.4872%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦&gt;0 : 𝑦 :=𝑦−1
</div>
</div>
<div class="ppt-text-layer" style="left:-0.3378%;top:21.4534%;width:12.3590%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑦 :=𝑦+1
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:6.6667%;width:85.0000%;height:13.3333%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות זמן ליניארי
Linear Time Properties
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
24
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:26.6667%;width:98.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: תכונת זמן-ליניארי 𝑃 היא תת קבוצה של המילים האינסופיות
מעל האלף-בית 2𝐴𝑃 ז&quot;א, 𝑃⊆ 2 𝐴𝑃 𝜔
אם מערכת מעברים 𝑇𝑆 מקיימת תכונת זמן לינארי 𝑃 נכתוב 𝑇𝑆⊨𝑃
הגדרה: 𝑇𝑆 ⊨ 𝑃 אם ורק אם 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑃
במילים: מערכת מעברים 𝑇𝑆 מקיימת תכונת זמן לינארי 𝑃 אם ורק אם כל רצפי העקבות האינסופיים שהתוכנית יכולה לייצר מקיימים את התכונה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:10.7720%;top:-2.8673%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מריצות לתכונות
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
<div class="ppt-text-layer" style="left:35.9793%;top:81.9905%;width:38.8123%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
קבוצה של מילים מעל הא&quot;ב 2𝐴𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:23.0438%;top:22.0743%;width:10.7498%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
ריצות
</div>
</div>
<div class="ppt-text-layer" style="left:19.0684%;top:40.4792%;width:15.5181%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
מסלולים
</div>
</div>
<div class="ppt-text-layer" style="left:14.3526%;top:58.8217%;width:20.5670%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
רִצְפֵי עֲקֵבוֹת
</div>
</div>
<div class="ppt-text-layer" style="left:22.8725%;top:81.0412%;width:11.6088%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
תכונה
</div>
</div>
<div class="ppt-text-layer" style="left:53.3114%;top:68.1153%;width:3.5798%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(90.00deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
⊆
</div>
</div>
<div class="ppt-text-layer" style="left:35.9793%;top:22.2182%;width:38.8123%;height:8.1398%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 0 𝛼 1 𝑠 1 𝛼 2 𝑠 2 𝛼 3 𝑠 3 ⋯
</div>
</div>
<div class="ppt-text-layer" style="left:35.9793%;top:41.1565%;width:38.8123%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑠 0 𝑠 1 𝑠 2 𝑠 3 ⋯
</div>
</div>
<div class="ppt-text-layer" style="left:35.9793%;top:59.0383%;width:38.8123%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐿 𝑠 0 𝐿 𝑠 1 𝐿 𝑠 2 𝐿 𝑠 3 ⋯
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:70.2344%;width:30.3971%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האם כל רִצְפֵי הָעֲקֵבוֹת
מקיימים את התכונה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:3.0590%;width:85.0000%;height:13.3333%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: תכונת זמן ליניארי, מערכת שמקיימת אותה ומערכת שאינה מקיימת אותה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Arial Rounded MT Bold','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
26
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:57.7778%;width:80.0000%;height:37.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c7bba6;opacity:0.231;border:0.75px solid #9b2d1f;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4f4b4b;white-space:pre-wrap;width:100%;">
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑝∈𝜎 𝑖 for infinitely many 𝑖′s
</div>
</div>
<div class="ppt-text-layer" style="left:27.5000%;top:60.0000%;width:26.0849%;height:12.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c7bba6;opacity:0.231;border:0.75px solid #9b2d1f;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4f4b4b;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠(𝑇 𝑆 1 )
</div>
</div>
<div class="ppt-text-layer" style="left:61.6667%;top:64.4444%;width:26.0849%;height:12.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#c7bba6;opacity:0.231;border:0.75px solid #9b2d1f;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4f4b4b;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠(𝑇 𝑆 2 )
</div>
</div>
<div class="ppt-text-layer" style="left:32.8447%;top:41.8365%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:12.5722%;top:41.8365%;width:5.9878%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞}
</div>
</div>
<div class="ppt-text-layer" style="left:22.8056%;top:29.3205%;width:3.7553%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:85.3456%;top:41.4167%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:64.8456%;top:36.6893%;width:5.9878%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞}
</div>
</div>
<div class="ppt-text-layer" style="left:75.7018%;top:30.3442%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:5.9263%;top:21.1131%;width:7.1469%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑇 𝑆 1 :
</div>
</div>
<div class="ppt-text-layer" style="left:53.6592%;top:23.7402%;width:7.7661%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑇 𝑆 2 :
</div>
</div>
<div class="ppt-text-layer" style="left:2.6004%;top:54.3385%;width:14.8807%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴𝑃={𝑝,𝑞}
</div>
</div>
<div class="ppt-text-layer" style="left:34.8783%;top:72.4136%;width:11.3283%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#248e16;white-space:pre-wrap;width:100%;">
𝑇 𝑆 1 ⊨𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:78.8804%;top:78.4207%;width:18.1583%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מילים כמו
𝑝 𝑞 {} 𝜔
מייצגות בָּאג במערכת
</div>
</div>
<div class="ppt-text-layer" style="left:78.1669%;top:60.0000%;width:11.1685%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 2 ⊭𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:18.6803%;top:85.9146%;width:52.1530%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0040c0;white-space:pre-wrap;width:100%;">
תכונת הזמן הלינארי – &quot;𝑝 מתקיים אינסוף פעמים&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:9.1684%;top:46.7367%;width:31.4184%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#00b050;white-space:pre-wrap;width:100%;">
מערכת המקיימת את התכונה
</div>
</div>
<div class="ppt-text-layer" style="left:58.6517%;top:46.8718%;width:35.0648%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מערכת שלא מקיימת את התכונה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: רמזורים מסונכרנים
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
<div class="ppt-text-layer" style="left:22.9046%;top:53.3333%;width:61.6588%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
&quot;הרמזור הראשון יהיה ירוק לעיתים תכופות (אינסוף פעמים)&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:3.7424%;top:66.6667%;width:93.3333%;height:32.3228%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל המילים האינסופיות מהצורה 𝐴 1 𝐴 2 𝐴 3 … מעל 2 𝐴𝑃 כך ש 𝑔𝑟𝑒𝑒 𝑛 1 ∈ 𝐴 𝑖 עבור אינסוף 𝑖-ים.
למשל, 𝑃 מכילה את המילים:
𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛2 𝑔𝑟𝑒𝑒𝑛1, 𝑟𝑒𝑑2 𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛2 𝑔𝑟𝑒𝑒𝑛1, 𝑟𝑒𝑑2 …
∅ 𝑔𝑟𝑒𝑒𝑛1 ∅ 𝑔𝑟𝑒𝑒𝑛1 ∅ 𝑔𝑟𝑒𝑒𝑛1 ∅ 𝑔𝑟𝑒𝑒𝑛1 …
{𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛1} {𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛1} {𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛1}…
{𝑔𝑟𝑒𝑒𝑛1, 𝑔𝑟𝑒𝑒𝑛2} {𝑔𝑟𝑒𝑒𝑛1, 𝑔𝑟𝑒𝑒𝑛2}{𝑔𝑟𝑒𝑒𝑛1, 𝑔𝑟𝑒𝑒𝑛2}…
</div>
</div>
<div class="ppt-text-layer" style="left:17.7271%;top:60.2158%;width:64.6362%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑃= 𝐴 1 𝐴 2 ⋯∈ 2 𝐴𝑃 𝜔 : ∀𝑗∈ℕ ∃𝑖&gt;𝑗 𝑔𝑟𝑒𝑒 𝑛 1 ∈ 𝐴 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:65.8643%;top:24.4444%;width:20.8024%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
〈𝑟𝑒𝑑, 𝑔𝑟𝑒𝑒𝑛〉
</div>
</div>
<div class="ppt-text-layer" style="left:65.8333%;top:38.8889%;width:20.8024%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
〈𝑔𝑟𝑒𝑒𝑛, 𝑟𝑒𝑑〉
</div>
</div>
<div class="ppt-text-layer" style="left:37.0669%;top:24.4444%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑔𝑟𝑒𝑒𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:37.0669%;top:38.8889%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:24.4444%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:38.8889%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑔𝑟𝑒𝑒𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:14.8269%;top:18.7586%;width:9.7470%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{𝑟𝑒 𝑑 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:45.2831%;width:12.4790%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑔𝑟𝑒𝑒𝑛 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:43.3262%;top:45.2831%;width:9.7498%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑟𝑒𝑑 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:43.3311%;top:18.2729%;width:12.5372%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑔𝑟𝑒𝑒𝑛 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:78.8832%;top:18.1563%;width:18.5467%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑟𝑒 𝑑 1 ,𝑔𝑟𝑒𝑒𝑛 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:78.5530%;top:45.1701%;width:18.5467%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑔𝑟𝑒𝑒𝑛 1 ,𝑟𝑒 𝑑 2 }
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: רמזורים מסונכרנים
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
<div class="ppt-text-layer" style="left:17.7271%;top:53.3333%;width:71.0644%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
&quot;אף פעם לא מדליקים אור ירוק בשני הרמזורים ביחד&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:2.1875%;top:67.7098%;width:97.0758%;height:28.9569%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל המילים האינסופיות מהצורה 𝐴 1 𝐴 2 𝐴 3 … מעל 2 𝐴𝑃 כך שלכל 𝑖, 𝑔𝑟𝑒𝑒 𝑛 1 ∉ 𝐴 𝑖 או 𝑔𝑟𝑒𝑒 𝑛 2 ∉ 𝐴 𝑖
למשל, 𝑃 מכילה את המילים:
𝑟𝑒 𝑑 1 , 𝑔𝑟𝑒𝑒 𝑛 2 𝑔𝑟𝑒𝑒 𝑛 1 , 𝑟𝑒 𝑑 2 𝑟𝑒 𝑑 1 , 𝑔𝑟𝑒𝑒 𝑛 2 𝑔𝑟𝑒𝑒 𝑛 1 , 𝑟𝑒 𝑑 2 . . .
∅ 𝑔𝑟𝑒𝑒𝑛1 ∅ 𝑔𝑟𝑒𝑒𝑛1 ∅ 𝑔𝑟𝑒𝑒𝑛1 ∅ 𝑔𝑟𝑒𝑒𝑛1 …
{𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛1} {𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛1} {𝑟𝑒𝑑1, 𝑔𝑟𝑒𝑒𝑛1}…
</div>
</div>
<div class="ppt-text-layer" style="left:17.7271%;top:60.0000%;width:68.2237%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃= 𝐴 1 𝐴 2 ⋯∈ 2 𝐴𝑃 𝜔 : ∀𝑖∈ℕ 𝑔𝑟𝑒𝑒 𝑛 1 ∉ 𝐴 𝑖 ∨𝑔𝑟𝑒𝑒 𝑛 2 ∉ 𝐴 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:65.8643%;top:24.4444%;width:20.8024%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
〈𝑟𝑒𝑑, 𝑔𝑟𝑒𝑒𝑛〉
</div>
</div>
<div class="ppt-text-layer" style="left:65.8333%;top:38.8889%;width:20.8024%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
〈𝑔𝑟𝑒𝑒𝑛, 𝑟𝑒𝑑〉
</div>
</div>
<div class="ppt-text-layer" style="left:37.0669%;top:24.4444%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑔𝑟𝑒𝑒𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:37.0669%;top:38.8889%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:24.4444%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑟𝑒𝑑
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:38.8889%;width:11.6667%;height:5.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑔𝑟𝑒𝑒𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:14.8269%;top:18.7586%;width:9.7470%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{𝑟𝑒 𝑑 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:45.2831%;width:12.4790%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑔𝑟𝑒𝑒𝑛 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:43.3262%;top:45.2831%;width:9.7498%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑟𝑒𝑑 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:43.3311%;top:18.2729%;width:12.5372%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑔𝑟𝑒𝑒𝑛 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:78.8832%;top:18.1563%;width:18.5467%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑟𝑒 𝑑 1 ,𝑔𝑟𝑒𝑒𝑛 2 }
</div>
</div>
<div class="ppt-text-layer" style="left:78.5530%;top:45.1701%;width:18.5467%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
{ 𝑔𝑟𝑒𝑒𝑛 1 ,𝑟𝑒 𝑑 2 }
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:0.0000%;top:28.9219%;width:100.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:17.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: המאפיין &quot;לכל מצב במערכת יש עוקב שתיוגו 𝑎 &quot; איננו תכונת זמן לינארי
הוכחה:
• נניח, בשלילה, שקיימת 𝑃 המתארת את המאפיין שהוגדר למעלה.
• ז&quot;א: 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆𝑃 אם ורק אם לכל מצב של 𝑇𝑆 יש עוקב שתיוגו {𝑎}
• נבחן שתי מערכות מעברים:
• על פי 2, מכיוון שב-𝑇 𝑆 1 לכל מצב יש עוקב שתיוגו {𝑎}, 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇 𝑆 1 ⊆𝑃
• בגלל ש- 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇 𝑆 2 ⊆𝑇𝑟𝑎𝑐𝑒𝑠 𝑇 𝑆 1 מקבלים גם: 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇 𝑆 2 ⊆𝑃
• בסתירה ל-2 (כי ל-𝑡1 אין עוקב שתיוגו {𝑎}).
</div>
</div>
<div class="ppt-text-layer" style="left:56.6582%;top:63.3284%;width:3.5370%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
s0
</div>
</div>
<div class="ppt-text-layer" style="left:60.5984%;top:67.6088%;width:4.3646%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{a}
</div>
</div>
<div class="ppt-text-layer" style="left:41.7611%;top:63.3284%;width:3.5370%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
s1
</div>
</div>
<div class="ppt-text-layer" style="left:45.6886%;top:67.6088%;width:4.4829%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{b}
</div>
</div>
<div class="ppt-text-layer" style="left:21.4953%;top:63.2505%;width:3.3005%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
t0
</div>
</div>
<div class="ppt-text-layer" style="left:25.3172%;top:67.5309%;width:4.3646%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{a}
</div>
</div>
<div class="ppt-text-layer" style="left:6.5982%;top:63.2505%;width:3.3005%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
t1
</div>
</div>
<div class="ppt-text-layer" style="left:10.4074%;top:67.5309%;width:4.4829%;height:3.9275%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Times','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{b}
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:7.8230%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
29
</div>
</div>
<div class="ppt-text-layer" style="left:21.9405%;top:2.2222%;width:56.1190%;height:12.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: תכונת זמן לינארי היא תת-קבוצה 𝑃⊆ 2 𝐴𝑃 𝜔
הגדרה: 𝑇𝑆 ⊨ 𝑃 אם ורק אם 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:14.1071%;top:56.6667%;width:4.7838%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.6260%;top:56.6667%;width:4.7480%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 1
</div>
</div>
<div class="ppt-text-layer" style="left:45.8333%;top:33.3333%;width:41.9551%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
∀𝑠∈𝑆 . 𝑎 ∈ 𝐿 𝑠 ′ : 𝑠′∈𝑝𝑜𝑠𝑡 𝑠
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
איך נגדיר מניעה הדדית?
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
30
</div>
</div>
<div class="ppt-text-layer" style="left:11.6667%;top:15.5556%;width:85.0000%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• &quot;לעולם לא יכנסו שני תהליכים ביחד לקטע הקריטי&quot;
• נניח 𝐴𝑃 = {𝑐𝑟𝑖𝑡1, 𝑐𝑟𝑖𝑡2}
  • הפסוקים האטומיים האחרים אינם רלוונטיים לתכונה הזאת
• תאור כתכונת זמן ליניארי:
𝑃mutex = 𝜎∈ 2 𝐴𝑃 𝜔 :∀𝑖 𝑐𝑟𝑖𝑡1, 𝑐𝑟𝑖𝑡2 ⊈𝜎 𝑖
• דוגמאות למילים אינסופיות ב- 𝑃 mutex :
  • 𝑐𝑟𝑖 𝑡 1 𝑐𝑟𝑖 𝑡 2 𝜔
  • 𝑐𝑟𝑖 𝑡 1 𝑐𝑟𝑖 𝑡 1 𝜔
• דוגמאות למילים אינסופיות שאינן ב- 𝑃 mutex :
  • 𝑐𝑟𝑖𝑡1 {} 𝑐𝑟𝑖𝑡1, 𝑐𝑟𝑖𝑡2 𝜔
  • 𝑐𝑟𝑖𝑡1, 𝑐𝑟𝑖𝑡2 {} 𝑐𝑟𝑖𝑡1, 𝑐𝑟𝑖𝑡2 {} 𝜔
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-031.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
איך נגדיר מניעת הרעבה?
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
<div class="ppt-text-layer" style="left:0.0000%;top:21.1111%;width:97.5000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• &quot;תהליך הרוצה להיכנס לקטע הקריטי ייכנס בסופו של דבר&quot;
• נגדיר 𝐴𝑃={𝑤𝑎𝑖𝑡1, 𝑐𝑟𝑖𝑡1, 𝑤𝑎𝑖𝑡2, 𝑐𝑟𝑖𝑡2}
• כתיבה כתכונת זמן ליניארי:
P nostarve = 𝜎∈ 2 𝐴𝑃 𝜔 : ∃ ∞ 𝑗 𝑤𝑎𝑖 𝑡 1 ∈𝜎 𝑗 ⇒ ∃ ∞ 𝑗 𝑐𝑟𝑖 𝑡 1 ∈𝜎 𝑗
∩
𝜎∈ 2 𝐴𝑃 𝜔 : ∃ ∞ 𝑗 𝑤𝑎𝑖 𝑡 2 ∈𝜎 𝑗 ⇒ ∃ ∞ 𝑗 𝑐𝑟𝑖 𝑡 2 ∈𝜎 𝑗
• סימון: &quot;קיימים אינסוף אינדקסים כך ש...&quot;
∃ ∞ 𝑗 ( ___)≡∀𝑘&gt;0 ∃𝑗&gt;𝑘 ___
</div>
</div>
<div class="ppt-text-layer" style="left:8.4557%;top:87.7778%;width:85.5356%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
האם האלגוריתם שראינו מקיים את התכונה 𝑃nostarve ?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-032.png" alt="" />
<div class="ppt-text-layer" style="left:13.3333%;top:-5.5556%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
האם האלגוריתם מבטיח חוסר הרעבה?
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
<div class="ppt-text-layer" style="left:41.9021%;top:16.3016%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:29.3266%;top:33.9126%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.4775%;top:33.9126%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:41.5322%;top:52.5020%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:10.8334%;top:52.5020%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:73.7105%;top:52.5020%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:24.8883%;top:72.0698%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:61.1351%;top:72.0698%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:19.0438%;top:58.5382%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:83.9037%;top:58.5382%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:64.9155%;top:77.9831%;width:14.9978%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖𝑡1, 𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:28.0814%;top:77.9401%;width:14.9978%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1, 𝑤𝑎𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:55.9129%;top:21.3619%;width:2.6331%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:65.9114%;top:39.7159%;width:9.6804%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:40.7786%;top:39.2267%;width:8.6987%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:42.6042%;top:57.6629%;width:15.8568%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑤𝑎𝑖𝑡1, 𝑤𝑎𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:10.5484%;top:87.5946%;width:83.3333%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לא: {} 𝑤𝑎𝑖 𝑡 2 𝑤𝑎𝑖 𝑡 1 , 𝑤𝑎𝑖 𝑡 2 𝑐𝑟𝑖 𝑡 1 , 𝑤𝑎𝑖 𝑡 2 𝜔 ∈ 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ∖ 𝑃nostarve
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-033.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
עִדּוּן דרישות ושקילות עקבות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
33
</div>
</div>
<div class="ppt-text-layer" style="left:5.8333%;top:21.1111%;width:89.1667%;height:74.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• כשבונים מערכת:
מתחילים בהגדרת דרישות כלליות ומפרטים את הדרישות במהלך הפיתוח
• מבחינה פורמאלית:
מתחילים במודל המגדיר ריצות ומעדנים אותו ככל שמבינים יותר איך המערכת צריכה לפעול – עד שמגיעים למימוש
• מתמטית: 𝑇𝑟𝑎𝑐𝑒𝑠 𝑇 𝑆 𝐿 ⊆𝑇𝑟𝑎𝑐𝑒𝑠(𝑇 𝑆 𝐻 )
מיתרונות הגישה הפורמאלית:
  • אפשר לבדוק תכונות בכל שלב של הפיתוח
  • אפשר לוודא שהמימוש הוא עִדּוּן של הדרישות
  • אפשר לוודא, מול הלקוח, כבר בשלב מוקדם, שהדרישות הובנו
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: אלגוריתם מניעה הדדית
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
<div class="ppt-text-layer" style="left:26.1365%;top:90.1701%;width:39.2371%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
האלגוריתם מקיים את התכונה 𝑃mutex
</div>
</div>
<div class="ppt-text-layer" style="left:41.9020%;top:21.8571%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:29.3266%;top:39.4681%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.4775%;top:39.4681%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:41.5322%;top:58.0575%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:58.0575%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:73.7105%;top:58.0575%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:24.8882%;top:77.6253%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:61.1351%;top:77.6253%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:19.0438%;top:64.0937%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:83.9037%;top:64.0937%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:71.0919%;top:83.5387%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:34.2578%;top:83.4957%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:42.2980%;top:45.3161%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:50.8310%;top:27.7631%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:67.0316%;top:45.0634%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:52.1975%;top:63.7961%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:68.9718%;top:89.3136%;width:29.8638%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
החלטנו שבמצב ששני התהליכים בהמתנה, נותנים עדיפות לתהליך הראשון
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: עידון אלגוריתם המניעה ההדדית
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
<div class="ppt-text-layer" style="left:11.3262%;top:91.4369%;width:75.9463%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לא צריך לבדוק: גם הגרסה הזאת (הורדנו קשת) מקיימת את התכונה 𝑃mutex
</div>
</div>
<div class="ppt-text-layer" style="left:41.9020%;top:21.8571%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:29.3266%;top:39.4681%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, n2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:54.4775%;top:39.4681%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:41.5322%;top:58.0575%;width:15.5344%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, w2, y=1
</div>
</div>
<div class="ppt-text-layer" style="left:10.8333%;top:58.0575%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, n2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:73.7105%;top:58.0575%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
n1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:24.8882%;top:77.6253%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
c1, w2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:61.1351%;top:77.6253%;width:14.7946%;height:5.8703%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
w1, c2, y=0
</div>
</div>
<div class="ppt-text-layer" style="left:19.0438%;top:64.0937%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:83.9037%;top:64.0937%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:71.0919%;top:83.5387%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡2}
</div>
</div>
<div class="ppt-text-layer" style="left:34.2578%;top:83.4957%;width:8.8214%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{𝑐𝑟𝑖𝑡1}
</div>
</div>
<div class="ppt-text-layer" style="left:42.2980%;top:45.3161%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:50.8310%;top:27.7631%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:67.0316%;top:45.0634%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:52.1975%;top:63.7961%;width:4.3862%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#7030a0;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:2.8982%;top:-1.1111%;width:92.1018%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שקילות עקבות ותכונות זמן ליניארי
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
36
</div>
</div>
<div class="ppt-text-layer" style="left:2.8982%;top:21.1111%;width:92.1018%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור מערכות מצבים 𝑇𝑆 ו 𝑇𝑆’ בלי מצבים סופניים:
</div>
</div>
<div class="ppt-text-layer" style="left:8.3951%;top:33.9939%;width:86.4583%;height:24.2344%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠 𝑇𝑆 ⊆ 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
אם ורק אם
לכל תכונת זמן ליניארי 𝑃 מתקיים: אם 𝑇𝑆’⊨ 𝑃 אז 𝑇𝑆⊨ 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:13.2485%;top:66.9970%;width:76.7515%;height:24.2344%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆) = 𝑇𝑟𝑎𝑐𝑒𝑠(𝑇𝑆’)
אם ורק אם
𝑇𝑆’ ו 𝑇𝑆 מקיימות את אותן תכונות זמן ליניארי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:-4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: שתי מכונות שתייה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
37
</div>
</div>
<div class="ppt-text-layer" style="left:4.2405%;top:49.6804%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
sprite
</div>
</div>
<div class="ppt-text-layer" style="left:30.0685%;top:49.6804%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
beer
</div>
</div>
<div class="ppt-text-layer" style="left:17.1545%;top:49.6804%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
select
</div>
</div>
<div class="ppt-text-layer" style="left:17.1545%;top:30.0113%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
pay
</div>
</div>
<div class="ppt-text-layer" style="left:62.0241%;top:49.8877%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
sprite
</div>
</div>
<div class="ppt-text-layer" style="left:74.8076%;top:49.8877%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
beer
</div>
</div>
<div class="ppt-text-layer" style="left:87.5912%;top:49.8877%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
select2
</div>
</div>
<div class="ppt-text-layer" style="left:49.2405%;top:49.8877%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
select1
</div>
</div>
<div class="ppt-text-layer" style="left:68.0245%;top:29.1833%;width:8.6093%;height:5.1761%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffff00;opacity:1.000;border:0.75px solid #000000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
pay
</div>
</div>
<div class="ppt-text-layer" style="left:33.0899%;top:67.7778%;width:34.6602%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴𝑃 = { 𝑝𝑎𝑦, 𝑠𝑝𝑟𝑖𝑡𝑒, 𝑏𝑒𝑒𝑟 }
</div>
</div>
<div class="ppt-text-layer" style="left:9.5412%;top:75.3463%;width:83.6247%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
אין תכונת זמן ליניארי שיכולה להבדיל בין שתי המכונות האלה
</div>
</div>
<div class="ppt-text-layer" style="left:41.6667%;top:41.1224%;width:4.6141%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
≡
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:23.3333%;width:9.3733%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑝𝑎𝑦}
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:54.1856%;width:11.9797%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑠𝑝𝑟𝑖𝑡𝑒}
</div>
</div>
<div class="ppt-text-layer" style="left:28.9268%;top:54.1271%;width:10.2092%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑏𝑒𝑒𝑟}
</div>
</div>
<div class="ppt-text-layer" style="left:19.1667%;top:54.1271%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:21.7405%;top:24.1998%;width:8.8123%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝𝑎𝑦}
</div>
</div>
<div class="ppt-text-layer" style="left:60.3558%;top:54.4693%;width:11.9797%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑠𝑝𝑟𝑖𝑡𝑒}
</div>
</div>
<div class="ppt-text-layer" style="left:74.3137%;top:54.4298%;width:10.2092%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑏𝑒𝑒𝑟}
</div>
</div>
<div class="ppt-text-layer" style="left:89.4589%;top:54.2435%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:50.8333%;top:54.2893%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:3.6795%;top:88.8454%;width:91.5093%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מסקנה: המאפיין &quot;יש ל-𝑇𝑆 ארבעה מצבים&quot; איננו תכונת זמן לינארי.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:12.1202%;top:5.8761%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: &quot;הַכֹּל צָפוּי וְהָרְשׁוּת נְתוּנָה&quot;
(משנה אבות ג&#x27; טו&#x27;)
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
<div class="ppt-text-layer" style="left:10.1692%;top:74.3793%;width:83.6247%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
אין תכונת זמן ליניארי שיכולה להבדיל בין שתי המכונות האלה
</div>
</div>
<div class="ppt-text-layer" style="left:48.7131%;top:49.9675%;width:4.6141%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
≡
</div>
</div>
<div class="ppt-text-layer" style="left:21.8381%;top:60.6726%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:3.6827%;top:84.5495%;width:94.1667%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מסקנה: המאפיין &quot;מכל מצב יש מסלול למצב המקיים את התכונה 𝑝&quot; איננה תכונת זמן לינארי.
</div>
</div>
<div class="ppt-text-layer" style="left:15.2061%;top:42.4279%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:36.0876%;top:42.2389%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:59.7554%;top:51.2351%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:81.4680%;top:51.2351%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#742217;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:24.1100%;top:23.5035%;width:55.7531%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;background:#ffffcc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
http://www.leibowitz.co.il/leibarticles.asp?id=62
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-039.png" alt="" />
<div class="ppt-text-layer" style="left:10.1692%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: תכונה הנוגעת לקיום ריצות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
39
</div>
</div>
<div class="ppt-text-layer" style="left:30.1732%;top:64.1789%;width:44.9921%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑇𝑟𝑎𝑐𝑒𝑠 𝑇 𝑆 2 ⊆𝑇𝑟𝑎𝑐𝑒𝑠(𝑇 𝑆 1 )
</div>
</div>
<div class="ppt-text-layer" style="left:14.1660%;top:37.4506%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:36.8615%;top:36.8100%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:59.7554%;top:45.8554%;width:4.5439%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:82.2420%;top:46.3395%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑝}
</div>
</div>
<div class="ppt-text-layer" style="left:36.7500%;top:53.2549%;width:5.9878%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞}
</div>
</div>
<div class="ppt-text-layer" style="left:17.2774%;top:19.8094%;width:6.4807%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 1
</div>
</div>
<div class="ppt-text-layer" style="left:53.2747%;top:18.8889%;width:6.5389%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑇 𝑆 2
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:82.3526%;width:96.5983%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
המאפיין &quot;יש ריצה המגיעה למצב המתויג ב- 𝑝 ויש ריצה המגיעה למצב המתויג ב- 𝑞 &quot; אינו תכונת זמן לינארי.
</div>
</div>
<div class="ppt-text-layer" style="left:18.5805%;top:71.8279%;width:67.6368%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל תכונת זמן לינארי ש-𝑇 𝑆 1 תקיים גם 𝑇 𝑆 2 תקיים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-040.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סוגים של תכונות
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-041.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות בטיחות (safety properties)
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
<div class="ppt-text-layer" style="left:4.1667%;top:17.7778%;width:90.8333%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונות בטיחות (safety properties) ≈ &quot;שום דבר רע לא יקרה&quot;
• תכונת בטיחות אופיינית: תכונת המניעה ההדדית
  • הדבר הרע (יותר מתהליך אחד בקטע הקריטי) לעולם לא קורה
• תוכנה זאת היא שמורה (invariant)
  • נתון תנאי 𝜙 למצבים
  • דורשים ש 𝜙 יתקיים לכל מצב נגיש
  • דוגמה: עבור תכונת המניעה ההדדית 𝜙=¬𝑐𝑟𝑖𝑡1∨¬𝑐𝑟𝑖𝑡2
  • דוגמה: תכונת הקִפָּאוֹן של הפילוסופים הסועדים
  𝜙=¬𝑤𝑎𝑖 𝑡 0 ∨¬𝑤𝑎𝑖 𝑡 1 ∨¬𝑤𝑎𝑖 𝑡 2 ∨¬𝑤𝑎𝑖 𝑡 3 ∨¬𝑤𝑎𝑖 𝑡 4
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-042.png" alt="" />
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
42
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-043.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
43
</div>
</div>
<div class="ppt-text-layer" style="left:4.9174%;top:16.6667%;width:88.3333%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת זמן ליניארי 𝑃inv היא שְׁמוּרָה אם יש תכונת מצב 𝜙 כך ש-
𝑃inv= 𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎 𝑖 ⊨𝜙 for all 𝑖∈ℕ
  • 𝜙 נקרא תנאי השמורה (invariant condition)
• קל להוכיח: 𝑇𝑆⊨ 𝑃inv אם ורק אם
  • 𝑡𝑟𝑎𝑐𝑒 𝜋 ∈𝑃inv לכל מסלול 𝜋 של 𝑇𝑆
  • 𝐿 𝑠 ⊨𝜙 לכל מצב 𝑠 השייך למסלול של 𝑇𝑆
  • 𝐿 𝑠 ⊨𝜙 לכל מצב 𝑠∈ 𝑅𝑒𝑎𝑐ℎ(𝑇𝑆)
• הוכחת קיום תכונת שמורה באינדוקציה:
  • 𝜙 חייב להתקיים בכל מצב התחלתי
  • נכונות 𝜙 נשמרת תחת כל מעבר (מספיק בתחום הנגיש)
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: שְׁמוּרוֹת (invariants)
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:34.4755%;width:23.6001%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מספיק שיהיה מצב נגיש אחד שלא מקיים את 𝜙 כדי לקבוע 𝑇𝑆 ⊭ 𝑃 𝑖𝑛𝑣
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-044.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
44
</div>
</div>
<div class="ppt-text-layer" style="left:4.9174%;top:16.6667%;width:88.3333%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת זמן ליניארי 𝑃inv היא שְׁמוּרָה אם יש תכונת מצב 𝜙 כך ש-
𝑃inv= 𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎 𝑖 ⊨𝜙 for all 𝑖∈ℕ
  • 𝜙 נקרא תנאי השמורה (invariant condition)
• קל להוכיח: 𝑇𝑆⊨ 𝑃inv אם ורק אם
  • 𝑡𝑟𝑎𝑐𝑒 𝜋 ∈𝑃inv לכל מסלול 𝜋 של 𝑇𝑆
  • 𝐿 𝑠 ⊨𝜙 לכל מצב 𝑠 השייך למסלול של 𝑇𝑆
  • 𝐿 𝑠 ⊨𝜙 לכל מצב 𝑠∈ 𝑅𝑒𝑎𝑐ℎ(𝑇𝑆)
• הוכחת קיום תכונת שמורה באינדוקציה:
  • 𝜙 חייב להתקיים בכל מצב התחלתי
  • נכונות 𝜙 נשמרת תחת כל מעבר (מספיק בתחום הנגיש)
</div>
</div>
<div class="ppt-text-layer" style="left:8.3333%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: שתנאי מצב
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:34.4755%;width:23.6001%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מספיק שיהיה מצב נגיש אחד שלא מקיים את 𝜙 כדי לקבוע 𝑇𝑆 ⊭ 𝑃 𝑖𝑛𝑣
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-045.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
45
</div>
</div>
<div class="ppt-text-layer" style="left:11.8621%;top:25.3447%;width:85.0000%;height:6.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מי מהתכונות הבאות הן שמורה? הוכיחו טענותיכם.
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:40.6808%;width:52.0710%;height:5.9053%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 1 = 𝜎∈ 2 𝐴𝑃 𝜔 : ∀𝑖. 𝜎 𝑖 ⊨ 𝑝→ 𝑞∨¬𝑟
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:67.7778%;width:50.3712%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 3 = 𝜎∈ 2 𝐴𝑃 𝜔 :𝑝∈𝜎 0 →∀𝑖. 𝑝∈𝜎 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:54.2293%;width:91.6734%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃 2 = 𝜎∈ 2 𝐴𝑃 𝜔 :𝜎 0 ⊨ 𝑝→𝑞 ∧ ∀𝑖. 𝑝∈𝜎 𝑖 ∨𝑞∉𝜎 𝑖 →𝜎 𝑖+1 ⊨ 𝑝∨¬𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:25.9218%;top:84.7502%;width:53.1565%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה אינה שמורה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-046.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
46
</div>
</div>
<div class="ppt-text-layer" style="left:7.0700%;top:27.7778%;width:87.6954%;height:63.5442%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: התכונה הבאה אינה תכונת שְׁמוּרָה
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 :𝑝∈𝜎 0 →∀𝑖. 𝑝∈𝜎 𝑖
הוכחה:
• נניח בשלילה שקיימת תכונת מצב 𝜙כך ש-
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎 𝑖 ⊨𝜙 for all 𝑖∈ℕ
• לפי הגדרת 𝑃, המילה 𝑝 𝜔 ∈𝑃 ולכן, ע&quot;פ הנחת השלילה, ⊨𝜙 וגם 𝑝 ⊨𝜙
• לכן, ע&quot;פ הנחת השלילה, המילה 𝑝 𝜔 ∈𝑃
• קיבלנו סתירה להגדרה של 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:25.0000%;top:14.4444%;width:53.1565%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה אינה שְׁמוּרָה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-047.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
47
</div>
</div>
<div class="ppt-text-layer" style="left:7.0700%;top:27.7778%;width:87.6954%;height:63.5442%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: התכונה הבאה אינה תכונת שְׁמוּרָה
𝑃={ 𝜎∈ 2 𝐴𝑃 𝜔 : 𝑝∈𝜎 2𝑖 for all 𝑖∈ℕ}
הוכחה:
• נניח בשלילה שקיימת תכונת מצב 𝜙 כך ש-
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : 𝜎 𝑖 ⊨𝜙 for all 𝑖∈ℕ
• לפי הגדרת 𝑃, המילה 𝑝 𝜔 ∈𝑃 ולכן, ע&quot;פ הנחת השלילה, ⊨𝜙
• לכן, ע&quot;פ הנחת השלילה, המילה 𝜔 ∈𝑃
• קיבלנו סתירה להגדרה של 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:25.0000%;top:14.4444%;width:53.1565%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#fad9cd;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
איך נוכיח שתכונה אינה שְׁמוּרָה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-048.png" alt="" />
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
48
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:17.3264%;width:97.4284%;height:21.6651%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
next 𝑑, 𝑚, 𝑦, ℎ, min, 𝑠 = (𝑑, 𝑚, 𝑦, ℎ, min, 𝑠 + 1) if s &lt; 59 (𝑑, 𝑚, 𝑦, ℎ, min⁡+ 1, 0) if 𝑠 = 59∧min&lt; 59 𝑑, 𝑚, 𝑦, ℎ + 1, 0, 0 if 𝑠 = 59∧𝑚𝑖𝑛&lt; 59∧ℎ &lt; 23 𝑑 + 1, 𝑚, 𝑦, 0, 0, 0 if 𝑠 = 59∧𝑚𝑖𝑛&lt; 59∧ℎ = 23∧𝑑 &lt;days 𝑚, 𝑦 (1, 𝑚 + 1, 𝑦, 0, 0, 0) if 𝑠 = 59∧𝑚𝑖𝑛&lt; 59∧ ℎ = 23∧𝑑 =days 𝑚, 𝑦 ∧𝑚 &lt; 12 1, 1, 𝑦 + 1, 0, 0, 0 if 𝑠 = 59∧𝑚𝑖𝑛&lt; 59∧ℎ = 23∧𝑑 =days 𝑚, 𝑦 ∧𝑚 = 12
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:43.2887%;width:40.3647%;height:12.9783%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
days 𝑑, 𝑦 = 31 if 𝑚∈ {1, 3, 5, 7, 8, 10, 12} 30 if 𝑚∈ 4, 6, 9, 11 28 if leap 𝑦 ∧𝑚=2
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:60.5643%;width:65.6004%;height:8.3540%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
leap 𝑦 = 𝑡𝑟𝑢𝑒 (𝑦 mod 4 = 0 ∧ y mod 100 ≠ 0) ∨ (y mod 400 = 0) 𝑓𝑎𝑙𝑠𝑒 otherwise
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:74.1833%;width:78.4237%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑇𝑆=⟨ ℕ 6 , 𝑠,𝑡𝑖𝑐𝑘,𝑛𝑒𝑥𝑡 𝑠 :𝑠∈ ℕ 6 , {tick}, 0,0,0,0,0,0 , ℕ 6 , 𝑠↦ 𝑠 ⟩
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:82.8983%;width:97.4284%;height:11.8367%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝜎∈ ℕ 6 :∀𝑖≥0 ∀ 𝑑, 𝑚, 𝑦, ℎ, min, 𝑠 ∈𝜎 𝑖 ¬ 𝑑+𝑚+ℎ+𝑚𝑖𝑛+𝑠=𝑦= 𝑑 2 = 𝑚 2 = min 2 = ℎ 2 = 𝑠 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-049.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
49
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:16.7252%;width:93.5256%;height:57.3459%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
קבוצת המצבים:
𝑆= 0,1 ∗
יחס המעברים:
𝑤 1 0 𝑤 2 1 𝑤 3 →1 𝑤 1 𝑤 2 𝑤 3 : 𝑤 1 , 𝑤 2 , 𝑤 3 ∈ 0,1 ∗
∪
𝑤 1 1 𝑤 2 0 𝑤 3 →1 𝑤 1 𝑤 2 𝑤 3 : 𝑤 1 , 𝑤 2 , 𝑤 3 ∈ 0,1 ∗
∪
𝑤 1 0 𝑤 2 0 𝑤 3 →0 𝑤 1 𝑤 2 𝑤 3 : 𝑤 1 , 𝑤 2 , 𝑤 3 ∈ 0,1 ∗
∪
𝑤 1 1 𝑤 2 1 𝑤 3 →0 𝑤 1 𝑤 2 𝑤 3 : 𝑤 1 , 𝑤 2 , 𝑤 3 ∈ 0,1 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:3.7581%;top:78.1964%;width:93.9952%;height:7.8640%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
חידה: לאיזה מצב סופי נגיע אם נתחיל במצב 0 2025 1 2025 ?
</div>
</div>
<div class="ppt-text-layer" style="left:17.1543%;top:89.0464%;width:65.8837%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תשובה: זוגיות מספר האחדות היא שמורה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-050.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת שמורות
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
<div class="ppt-text-layer" style="left:6.9792%;top:18.8889%;width:88.3333%;height:72.0834%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• בדיקה עבור פסוק 𝜙 = האם התכונה מתקיימת בכל מצב נגיש
  • שימוש בגרסה של אלגוריתם סריקת גרף (BFS או DFS)
  • בהנחה שמערכת המעברים סופית
• בדרך כלל, עדיף חיפוש DFS על BFS
  • רוב הַבָּאגִים המעניינים קורים לאחר רצף ארוך יחסית של פעולות
• ביצוע חיפוש DFS קדימה
  • אם מצאנו מצב 𝑠 כך ש 𝑠⊭𝜙 מסיקים ש 𝜙 אינו שמורה
• אפשרות אחרת: חיפוש אחורה
  • מתחילים מהמצבים בהם 𝜙 אינה מתקיימת (𝑠⊭𝜙)
  • מחשבים את המצבים הקודמים 𝑃𝑟 𝑒 ∗ (𝑠) באמצעות DFS או BFS
  • אם הגענו למצב התחלתי (𝐼∩𝑃𝑟 𝑒 ∗ 𝑠 ≠∅) מסיקים ש 𝜙 אינה שמורה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-051.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת שמורה באמצעות DFS
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
<div class="ppt-text-layer" style="left:21.1834%;top:26.1311%;width:64.9427%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
קלט: מערכת מעברים סופית 𝑇𝑆 ונוסחה 𝜙
פלט: true אם 𝑇𝑆 מקיימת את השמורה &quot;תמיד 𝜙&quot;, אחרת false
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-052.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקת שמורה באמצעות DFS
</div>
</div>
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-053.png" alt="" />
<div class="ppt-text-layer" style="left:6.9792%;top:0.0000%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיבוכיות זמן
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
53
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:22.2222%;width:96.6667%;height:61.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נניח שניתן לסרוק כל 𝑠’∈𝑃𝑜𝑠𝑡(𝑠) בזמן 𝜃(|𝑃𝑜𝑠𝑡(𝑠)|)
  • הנחה תקפה כאשר מייצגים את 𝑃𝑜𝑠𝑡(𝑠) ע&quot;י רשימות סמיכות
• סיבוכיות זמן בדיקת שמורה: 𝑂(𝑁⋅|𝜙|+𝑀)
  • 𝑁 מסמל את מספר המצבים הנגישים
  • 𝑀 =  𝑠 ∈ S |𝑃𝑜𝑠𝑡(𝑠)| הוא מספר המעברים (בחלק הנגיש) של 𝑇𝑆
• בדרך כלל לא מייצגים את רשימות הסמיכות באופן מפורש
  • למשל: ניתן להשתמש מעבר ישיר על גרפי התוכנית. במקרה זה,𝑃𝑜𝑠𝑡(𝑠) מתקבל מהכללים של יחס המעברים.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-054.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אלגוריתם שנותן גם דוגמה נגדית
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
54
</div>
</div>
<div class="ppt-table-layer" style="left:14.1667%;top:21.1111%;width:79.1667%;height:66.8259%;">
<table class="ppt-table">
<tr>
<td class="ppt-table-cell">
set of states 𝑅≔∅
</td>
<td class="ppt-table-cell">
(* קבוצת המצבים בהם ביקרנו *)
</td>
</tr>
<tr>
<td class="ppt-table-cell">
stack of states 𝑈 :=𝜖;
</td>
<td class="ppt-table-cell">
(* מחסנית מצבים &quot;לטיפול&quot; *)
</td>
</tr>
<tr>
<td class="ppt-table-cell">
boolean 𝑏 := true;
</td>
<td class="ppt-table-cell">
(* כל המצבים ב 𝑅 מקיימים את 𝜙*)
</td>
</tr>
<tr>
<td class="ppt-table-cell">
wile ((𝐼∖𝑅≠∅)∧𝑏) do
</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
take any 𝑠∈𝐼∖𝑅
visit(𝑠)
od
if 𝑏 then
</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
return “yes”
else
</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
return “no”, reverse(𝑈)
</td>
<td class="ppt-table-cell">

</td>
</tr>
<tr>
<td class="ppt-table-cell">
fi
</td>
<td class="ppt-table-cell">

</td>
</tr>
</table>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/11-linear-time-properties/slide-055.png" alt="" />
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
<div class="ppt-text-layer" style="left:5.8333%;top:2.1782%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה נגדית שימושית יותר מאשר הוכחת נכונות
כי דוגמה נגדית יכולה להצביע על באג אמיתי
</div>
</div>
<div class="ppt-text-layer" style="left:59.1667%;top:24.4444%;width:13.3333%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מערכת
</div>
</div>
<div class="ppt-text-layer" style="left:58.3333%;top:42.7778%;width:15.0000%;height:8.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מידול
</div>
</div>
<div class="ppt-text-layer" style="left:49.0000%;top:82.2222%;width:16.0000%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דוגמה נגדית
</div>
</div>
<div class="ppt-text-layer" style="left:30.4253%;top:57.7778%;width:22.9080%;height:13.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בדיקות מודל
(Model Cecking)
</div>
</div>
<div class="ppt-text-layer" style="left:10.4167%;top:24.4444%;width:13.3333%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
דרישות
</div>
</div>
<div class="ppt-text-layer" style="left:9.5833%;top:42.7778%;width:15.0000%;height:8.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
פירמול
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:58.8889%;width:19.1667%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות פורמליות
</div>
</div>
<div class="ppt-text-layer" style="left:57.5000%;top:58.8889%;width:16.6667%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מודל של המערכת
</div>
</div>
<div class="ppt-text-layer" style="left:72.5000%;top:83.7778%;width:15.0000%;height:8.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
סימולציה
</div>
</div>
<div class="ppt-text-layer" style="left:19.0000%;top:82.2222%;width:16.0000%;height:11.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#d34817;opacity:1.000;border:3.35px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
התכונות הוכחה
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
