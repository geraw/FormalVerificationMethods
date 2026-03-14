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
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת
Liveness Properties
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
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-002.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:85.0000%;height:17.4020%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: תכונות בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.9608%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:3.6256%;top:21.2381%;width:94.1667%;height:51.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃 𝑠𝑎𝑓𝑒 היא תכונת בטיחות אם ורק אם
  לכל 𝜎∈ 2 𝐴𝑃 𝜔 ∖ 𝑃 𝑠𝑎𝑓𝑒 יש רֵישָׁא 𝜌 כך ש
  𝑃 𝑠𝑎𝑓𝑒 ∩ 𝜌𝜎 ′′ : 𝜎′′∈ 2 𝐴𝑃 𝜔 =∅
</div>
</div>
<div class="ppt-text-layer" style="left:4.0066%;top:70.0000%;width:90.5137%;height:19.6960%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
דוגמה: כל תכונת שמורה 𝑃 𝑖𝑛𝑣(𝜙) היא תכונת בטיחות כי בכל מילה 𝜎 שאינה מקיימת את התכונה יש אות שאינה מקיימת את 𝜙 ולכן אפשר לבחור את 𝜌 להיות תחילת המילה עד לאות הזאת (כולל). נקבל שכל המשך של 𝜌 למילה אינסופית ייתן מילה 𝜌𝜎′′ שלא תקיים את התכונה.
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: סְגוֹר (closure) של תכונה
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
<div class="ppt-text-layer" style="left:1.6667%;top:27.9084%;width:95.8333%;height:6.9697%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
קבוצת המילים שכל אחת מֵהָרֵישׁוֹת שלהן אפשר להמשיך למילה ב-𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:5.4167%;top:17.9604%;width:89.1667%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 = 𝜎∈ 2𝐴𝑃 𝜔 : 𝑝𝑟𝑒𝑓 𝜎 ⊆ 𝑝𝑟𝑒𝑓 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:37.7423%;width:92.5000%;height:46.3636%;padding:0.00pt 0.00pt 204.09pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:16.7143%;top:51.1111%;width:60.7857%;height:31.1111%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:25.8333%;top:61.2115%;width:45.0000%;height:16.9856%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:0.2871%;top:87.1527%;width:49.3197%;height:10.3220%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מילה שכל רישא שלה אפשר להמשיך למילה ב-𝑃 והיא עצמה איננה ב-𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-4.4444%;width:87.9167%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: שאלה מתוך בוחן
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
<div class="ppt-text-layer" style="left:2.9894%;top:14.7141%;width:95.4167%;height:51.1024%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לכל זוג תכונות זמן ליניארי 𝑃1 ו 𝑃2 :
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃1∪𝑃2 = 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃1 ∪𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃2)
רעיון ההוכחה:
כיוון אחד קל בגלל שברור שמילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 , למשל, היא גם מילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 ∪ 𝑃 2 .
בכיוון השני צריך להיזהר: איך אנחנו יודעים שכל מילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 ∪ 𝑃 2 , היא גם מילה שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 1 או שאת כל הרישות שלה אפשר להמשיך למילים ב- 𝑃 2 ?
</div>
</div>
<div class="ppt-text-layer" style="left:66.6667%;top:84.2190%;width:32.5874%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝜎∉𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 1 ∪𝑐𝑙𝑢𝑠𝑢𝑟𝑒( 𝑃 2 )
</div>
</div>
<div class="ppt-text-layer" style="left:35.0000%;top:92.0955%;width:10.7161%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#00b050;white-space:pre-wrap;width:100%;">
𝜌 𝜎 ′ ∈ 𝑃 1
</div>
</div>
<div class="ppt-text-layer" style="left:30.8333%;top:71.9958%;width:10.7680%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#00b050;white-space:pre-wrap;width:100%;">
𝜌 𝜎 ′ ∈ 𝑃 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.3109%;top:88.5475%;width:10.7161%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#00b050;white-space:pre-wrap;width:100%;">
𝜌 𝜎 ′ ∈ 𝑃 1
</div>
</div>
<div class="ppt-text-layer" style="left:60.0511%;top:68.8889%;width:10.7680%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#00b050;white-space:pre-wrap;width:100%;">
𝜌 𝜎 ′ ∈ 𝑃 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: משפט
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
<div class="ppt-text-layer" style="left:8.7500%;top:22.6064%;width:82.5000%;height:33.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונת זמן ליניארי 𝑃היא תכונת בטיחות
אם ורק אם
𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃) = 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:33.9932%;top:67.4886%;width:47.6428%;height:22.9097%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:40.8146%;top:76.3810%;width:35.2703%;height:12.5079%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:1.7347%;top:88.4287%;width:40.3060%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
אין מילה שכל רישא שלה אפשר להמשיך למילה ב-𝑃 והיא עצמה איננה ב-𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: משפט
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
<div class="ppt-text-layer" style="left:12.5000%;top:22.2222%;width:70.8333%;height:31.4167%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לכל תכונת זמן לינארי 𝑃 התכונה 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 היא תכונת בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:38.6333%;top:65.6390%;width:47.6428%;height:22.9097%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:45.4547%;top:74.5313%;width:35.2703%;height:12.5079%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:82.6349%;width:36.6667%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
קיימת רישא שלא ניתן להמשיך למילה ב-𝑃 ולכן גם לא למילה ב-𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הגדרה: תכונות חַיּוּת
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
<div class="ppt-text-layer" style="left:4.1667%;top:17.7778%;width:94.1667%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונת זמן ליניארי 𝑃 היא תכונת חַיּוּת (liveness property) אם
𝑝𝑟𝑒𝑓 𝑃 = 𝜌:𝜌⊑𝜎, 𝜎∈𝑃 = 2 𝐴𝑃 ∗
• תכונת חַיּוּת היא תכונת זמן ליניארי שאיננה פוסלת אף רישא
• תכונות חַיּוּת מופרות רק &quot;בזמן אינסופי&quot;
  • בניגוד לתכונות בטיחות המופרות תמיד בזמן סופי
  • אין אפשרות לקבוע קיום או אי-קיום התכונה ע&quot;פ רישא של הריצה
  • כל רישא סופית יכולה להמשך לריצה שתקיים את התכונה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
המחשה
</div>
</div>
<div class="ppt-text-layer" style="left:67.9559%;top:100.0000%;width:35.3775%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
8
</div>
</div>
<div class="ppt-text-layer" style="left:46.6667%;top:62.8313%;width:46.9000%;height:33.6589%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת
&quot;משהו טוב יקרה בסופו של דבר&quot;
תמיד יכול להיות
ש &quot;הדבר הטוב&quot; יקרה
</div>
</div>
<div class="ppt-text-layer" style="left:6.6000%;top:62.6823%;width:41.3780%;height:33.6589%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תכונות בְּטִיחוּת
&quot;משהו רע לא יקרה&quot;
לא ניתן לתקן
את הדבר הרע
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-009.png" alt="" />
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
<div class="ppt-text-layer" style="left:11.1955%;top:5.0484%;width:36.8137%;height:15.1287%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑝𝑟𝑒𝑓: 2 𝐴𝑃 𝜔 → 2 2 𝐴𝑃 ∗
𝑝𝑟𝑒𝑓 𝜎 = 𝜌∈ 2 𝐴𝑃 ∗ : 𝜌⊏𝜎
</div>
</div>
<div class="ppt-text-layer" style="left:56.6667%;top:5.9824%;width:33.6820%;height:14.7398%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑒𝑥𝑡: 2 2 𝐴𝑃 ∗ → 2 2 𝐴𝑃 𝜔
𝑒𝑥𝑡 𝑆 = 𝜎: ∀𝑖 . 𝜎 ..𝑖 ∈𝑆
</div>
</div>
<div class="ppt-text-layer" style="left:23.1576%;top:27.3414%;width:10.3515%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:70.2283%;top:31.1111%;width:9.7148%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:23.7502%;top:50.6094%;width:4.2024%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:70.5691%;top:50.4167%;width:12.7643%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#002060;white-space:pre-wrap;width:100%;">
𝑝𝑟𝑒𝑓 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:19.5812%;top:43.3333%;width:14.7237%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#4e1610;white-space:pre-wrap;width:100%;">
𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃)
</div>
</div>
<div class="ppt-text-layer" style="left:48.1464%;top:47.7778%;width:6.6432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑝𝑟𝑒𝑓
</div>
</div>
<div class="ppt-text-layer" style="left:27.8771%;top:34.9777%;width:50.1000%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑒𝑥𝑡
</div>
</div>
<div class="ppt-text-layer" style="left:66.1938%;top:23.2942%;width:19.6729%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
מילים באורך סופי
</div>
</div>
<div class="ppt-text-layer" style="left:16.4628%;top:91.4514%;width:22.8284%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9e3611;white-space:pre-wrap;width:100%;">
מילים באורך אינסופי
</div>
</div>
<div class="ppt-text-layer" style="left:18.2727%;top:66.3812%;width:17.2415%;height:17.4562%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#df6c5d;opacity:1.000;border:1.00px solid #9b320e;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#4e1610;white-space:pre-wrap;width:100%;">
תכונת חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:49.3704%;top:70.0000%;width:6.6432%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑝𝑟𝑒𝑓
</div>
</div>
<div class="ppt-text-layer" style="left:12.8197%;top:52.9861%;width:9.5753%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
בטיחות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
איך נוכיח ש-𝑃 היא תכונות חַיּוּת?
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
<div class="ppt-text-layer" style="left:13.7570%;top:54.0108%;width:6.4539%;height:2.6230%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(11.10deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝜌∈ 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:13.6089%;top:66.0022%;width:10.1181%;height:2.6189%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;transform:rotate(348.81deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
𝜎 ′ ∈𝑃 כך ש-𝜌⊏𝜎′
</div>
</div>
<div class="ppt-text-layer" style="left:20.8868%;top:32.2222%;width:9.2476%;height:3.9284%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מתמתטיקאי המוכיח
ש-𝑃 היא תכונת חיות
</div>
</div>
<div class="ppt-text-layer" style="left:6.4667%;top:32.2222%;width:9.8729%;height:3.9284%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מתמתטיקאי המוכיח
ש-𝑃 איננה תכונת חיות
</div>
</div>
<div class="ppt-text-layer" style="left:3.5417%;top:21.3673%;width:93.9583%;height:13.9937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃= 𝜎 : ∃𝑖≥0 ∀𝑗&gt;𝑖 𝜎 𝑗 ⊨ 𝑝⇒𝜎 𝑗+1 ⊨𝑞 היא תכונת חַיּוּת
הוכחה: 𝜌 .{} 𝜔 ∈𝑃 עבור כל 𝜌∈ 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:3.9000%;top:48.2788%;width:93.9583%;height:13.9937%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃= 𝜎: ∀𝑖≥0 ∃𝑗&gt;𝑖 𝜎 𝑗 ⊨𝑝 היא תכונת חַיּוּת
הוכחה: 𝜌 .{𝑝} 𝜔 ∈𝑃 עבור כל 𝜌∈ 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:4.0191%;top:75.5556%;width:93.9583%;height:13.7618%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃= 𝜎: ∃𝑗&gt;0 𝜎 𝑗 =𝜎 0 היא תכונת חַיּוּת
הוכחה: 𝜌.(𝜌 0 ) 𝜔 ∈𝑃 עבור כל 𝜌∈ 2 𝐴𝑃 + ו- 𝜌 .{} 𝜔 ∈𝑃 עבור 𝜌=𝜖
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-011.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
איך נוכיח ש-𝑃 אינה תכונות חַיּוּת?
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
<div class="ppt-text-layer" style="left:10.8262%;top:51.5071%;width:6.4539%;height:2.6230%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(11.10deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝜌∈ 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:10.6781%;top:63.4985%;width:10.1181%;height:2.6189%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;transform:rotate(348.81deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
𝜎 ′ ∈𝑃 כך ש-𝜌⊏𝜎′
</div>
</div>
<div class="ppt-text-layer" style="left:17.9560%;top:29.7185%;width:9.2476%;height:3.9284%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מתמתטיקאי המוכיח
ש-𝑃 היא תכונת חיות
</div>
</div>
<div class="ppt-text-layer" style="left:0.3667%;top:29.7185%;width:13.0421%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מתמתטיקאי המוכיח
ש-𝑃 אינה תכונת חיות
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:21.3673%;width:93.9583%;height:13.9666%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃= 𝜎: ∀𝑖≤0 ∃𝑗≤𝑖 𝑝∈𝜎 𝑗 היא לא תכונת חַיּוּת
הוכחה: כל מילה אינסופית המתחילה ב-𝜌={} איננה ב-𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:81.9887%;width:93.9583%;height:13.4841%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃= 𝜎: ∀𝑖&gt;0 𝜎 2𝑖 ⊨𝑝 היא לא תכונת חַיּוּת
הוכחה: כל מילה אינסופית המתחילה ב-𝜌={}{} 𝑝 איננה ב-𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:53.0268%;width:93.9583%;height:13.9666%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃= 𝜎: ∃0&lt;𝑗&lt;10 𝜎 𝑗 =𝜎 0 היא לא תכונת חַיּוּת
הוכחה: כל מילה אינסופית המתחילה ב-𝜌={𝑝}{ } 9 איננה ב-𝑃
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:7.3299%;top:-5.0000%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משמעות תכונות חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
12
</div>
</div>
<div class="ppt-text-layer" style="left:34.1667%;top:14.5708%;width:63.0401%;height:81.6100%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• The question of whether a real system satisfies a liveness property is meaningless
• it can be answered only by observing the system for an infinite length of time, and real systems don’t run forever
• Liveness is always an approximation to the property we really care about
• We want a program to terminate within 100 years, but proving that it does would require addition of distracting timing assumptions
• So, we prove the weaker condition that the program eventually terminates
• This doesn’t prove that the program will terminate within our lifetimes, but it does demonstrate the absence of infinite loops
</div>
</div>
<div class="ppt-text-layer" style="left:7.8952%;top:65.5556%;width:22.0823%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
LESLIE LAMPORT
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת לדוגמה
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
<div class="ppt-text-layer" style="left:4.5833%;top:18.8889%;width:90.8333%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• &quot;אם המיכל ריק, ברז היציאה ייסגר לבסוף&quot;
• &quot;אם ברז היציאה פתוח ואות הבקשה כבוי, הברז ייסגר לבסוף&quot;
• &quot;אם המיכל מלא ויש אות בקשה, ברז היציאה יפתח לבסוף&quot;
• &quot;התוכנית תסתיים בתוך 50 צעדי חישוב&quot;
  • יש רישא סופית שסותרת את הדרישה =&gt; זאת תכונת בטיחות
• &quot;התוכנית תסתיים בסופו של דבר&quot;
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת למניעה הדדית
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
<div class="ppt-text-layer" style="left:4.5833%;top:21.1111%;width:90.8333%;height:63.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• בסופו של דבר:
  • כל תהליך יכנס בסופו של דבר לקטע הקריטי שלו
• באופן תדיר (infinitely often) :
  • כל תהליך יכנס לקטע הקריטי שלו אינסוף פעמים
• מניעת הרעבה:
  • כל תהליך שממתין לקטע הקריטי, יכנס בסופו של דבר
</div>
</div>
<div class="ppt-text-layer" style="left:28.4180%;top:85.5556%;width:37.7821%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
איך ננסח תכונות אלה?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונות חַיּוּת למניעה הדדית
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
<div class="ppt-text-layer" style="left:4.1667%;top:14.4444%;width:90.8333%;height:83.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝐴𝑃={𝑤𝑎𝑖𝑡1, 𝑐𝑟𝑖𝑡1, 𝑤𝑎𝑖𝑡2, 𝑐𝑟𝑖𝑡2}
𝑃 ={𝐴0 𝐴1 𝐴2 ∈ 2 𝐴𝑃 𝜔 : … }
• בסופו של דבר:
  ∃𝑗≥0. 𝑐𝑟𝑖𝑡1∈ 𝐴𝑗 ∧(∃𝑗≥0. 𝑐𝑟𝑖𝑡2∈ 𝐴𝑗)
• באופן תדיר:
  ∃ ∞ 𝑗≥0 . 𝑐𝑟𝑖𝑡1∈ 𝐴𝑗 ∧( ∃ ∞ 𝑗≥0 . 𝑐𝑟𝑖𝑡2∈𝐴𝑗)
• מניעת הרעבה:
∀𝑗≥0. 𝑤𝑎𝑖𝑡1∈𝐴𝑗 ⟹(∃𝑘&gt;𝑗. 𝑐𝑟𝑖𝑡1∈𝐴𝑘))
∧
∀𝑗≥0. 𝑤𝑎𝑖𝑡2∈𝐴𝑗 ⟹(∃𝑘&gt;𝑗. 𝑐𝑟𝑖𝑡2∈𝐴𝑘))
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:7.7083%;top:4.4444%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונה שהיא גם חַיּוּת וגם בטיחות
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
<div class="ppt-text-layer" style="left:1.4333%;top:21.1556%;width:97.0833%;height:68.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
משפט:
  אם 𝑃 היא גם תכונת בטיחות וגם תכונת חַיּוּת מעל 𝐴𝑃 אז 𝑃= 2 𝐴𝑃 𝜔
הוכחה:
  • אם 𝑃 היא תכונת חַיּוּת אז כל מילה סופית היא רישא של מילה ב 𝑃.
  • לכן כל רישא של כל מילה אינסופית היא רישא של מילה ב-𝑃.
  • לכן כל מילה אינסופית נמצאת בסגור של 𝑃 ⇐ 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 = (2 𝐴𝑃 ) 𝜔
  • מכיוון ש 𝑃 תכונת בטיחות, 𝑃=𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ומקבלים 𝑃= 2 𝐴𝑃 𝜔 .
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:5.8333%;top:34.4444%;width:45.4989%;height:35.3967%;padding:3.60pt 302.40pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:15.9945%;top:41.5872%;width:35.8333%;height:21.1111%;padding:3.60pt 64.80pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בטיחות רגולרית
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
<div class="ppt-text-layer" style="left:38.6320%;top:47.6984%;width:12.8109%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
שמורה
</div>
</div>
<div class="ppt-text-layer" style="left:51.3322%;top:34.8428%;width:45.4989%;height:35.3967%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:1.4279%;top:15.8170%;width:40.1320%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
קיימת 𝐵𝑎𝑑𝑃𝑟𝑒𝑓 כך ש-
𝑃= 𝜎: 𝑝𝑟𝑒𝑓 𝜎 ∩𝐵𝑎𝑑𝑃𝑟𝑒𝑓=∅
</div>
</div>
<div class="ppt-text-layer" style="left:31.8490%;top:74.9604%;width:26.3535%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
קיימת 𝜙 כך ש-
𝑃= 𝜎: ∀𝑖. 𝜎 𝑖 ⊨𝜙
</div>
</div>
<div class="ppt-text-layer" style="left:30.4413%;top:26.8039%;width:20.3601%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
𝐵𝑎𝑑𝑃𝑟𝑒𝑓 רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:43.9861%;top:66.5685%;width:15.2692%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#353232;white-space:pre-wrap;width:100%;">
𝑃= 2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:64.8416%;top:25.7154%;width:22.0255%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#353232;white-space:pre-wrap;width:100%;">
𝑝𝑟𝑒𝑓 𝑃 = 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:26.4213%;top:5.2579%;width:49.1945%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עולם תכונות הזמן הלינארי
</div>
</div>
<div class="ppt-text-layer" style="left:1.6130%;top:78.5893%;width:19.9884%;height:18.7190%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
2 2 𝐴𝑃 𝜔
כל נקודה כאן היא
תכונת זמן לינארי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תכונה שאיננה בטיחות ולא חַיּוּת
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
<div class="ppt-text-layer" style="left:1.6667%;top:18.8889%;width:97.5000%;height:73.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
&quot;מכונת המשקאות נותנת ספרייט אינסוף פעמים
לאחר שבהתחלה נתנה קולה שלוש פעמים ברצף&quot;
• לתכונה זאת שני חלקים:
  • דורשים שניתן ספרייט אינסוף פעמים
    • כיוון שלא ניתן להכריע נכונות ע&quot;פ רישא סופית, זאת תכונת חַיּוּת
  • שלושת המשקאות הראשונים צריכים להיות קולה
    • יש רישות רעות (אחד משלושת המשקאות הראשונים הוא ספרייט)
    לכן זאת תכונת בטיחות
• התכונה היא חיתוך (וגם) של תכונת בטיחות ותכונת חַיּוּת
נראה שניתן לפרק כך כל תכונת זמן ליניארי?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בטיחות מול חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
19
</div>
</div>
<div class="ppt-text-layer" style="left:0.8333%;top:21.1111%;width:97.5000%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• האם תכונות בטיחות שונות מתכונות חַיּוּת?
• האם כל תכונה היא תכונת בטיחות או תכונת חַיּוּת?
• אבל ( ע&quot;פ משפט הפירוק שננסח בשקפים הבאים):
  כל תכונה ניתן לתאר כ &quot;וְגַם&quot; של תכונת בטיחות ותכונת חַיּוּת
• מסקנה: תכונות חַיּוּת ובטיחות (ופעולת &quot;וְגַם&quot;) מאפשרות הגדרת כל התכונות
</div>
</div>
<div class="ppt-text-layer" style="left:5.7152%;top:22.1571%;width:5.1181%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#00b050;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
כן
</div>
</div>
<div class="ppt-text-layer" style="left:5.0622%;top:35.5556%;width:5.7711%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ff0000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
לא
</div>
</div>
<div class="ppt-text-layer" style="left:6.5333%;top:67.7778%;width:37.5000%;height:10.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
למשל: האות הראשונה מקיימת 𝑝 וגם יש אות המקיימת 𝑞
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:5.8333%;top:34.4444%;width:45.4989%;height:35.3967%;padding:3.60pt 302.40pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בטיחות
</div>
</div>
<div class="ppt-text-layer" style="left:15.9945%;top:41.5872%;width:35.8333%;height:21.1111%;padding:3.60pt 64.80pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בטיחות רגולרית
</div>
</div>
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
<div class="ppt-text-layer" style="left:38.6320%;top:47.6984%;width:12.8109%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
שמורה
</div>
</div>
<div class="ppt-text-layer" style="left:51.3322%;top:34.8428%;width:45.4989%;height:35.3967%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#675859;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:1.4279%;top:15.8170%;width:40.1320%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
קיימת 𝐵𝑎𝑑𝑃𝑟𝑒𝑓 כך ש-
𝑃= 𝜎: 𝑝𝑟𝑒𝑓 𝜎 ∩𝐵𝑎𝑑𝑃𝑟𝑒𝑓=∅
</div>
</div>
<div class="ppt-text-layer" style="left:31.8490%;top:74.9604%;width:26.3535%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
קיימת 𝜙 כך ש-
𝑃= 𝜎: ∀𝑖. 𝜎 𝑖 ⊨𝜙
</div>
</div>
<div class="ppt-text-layer" style="left:30.4413%;top:26.8039%;width:20.3601%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#353232;white-space:pre-wrap;width:100%;">
𝐵𝑎𝑑𝑃𝑟𝑒𝑓 רגולרית
</div>
</div>
<div class="ppt-text-layer" style="left:43.9861%;top:66.5685%;width:15.2692%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#353232;white-space:pre-wrap;width:100%;">
𝑃= 2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:64.8416%;top:25.7154%;width:22.0255%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#353232;white-space:pre-wrap;width:100%;">
𝑝𝑟𝑒𝑓 𝑃 = 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:54.8594%;top:84.2050%;width:20.7212%;height:5.7099%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝑃 𝑠𝑎𝑓𝑒 ∩ 𝑃 𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:26.4213%;top:5.2579%;width:49.1945%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
עולם תכונות הזמן הלינארי
</div>
</div>
<div class="ppt-text-layer" style="left:1.6130%;top:78.5893%;width:19.9884%;height:18.7190%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
2 2 𝐴𝑃 𝜔
כל נקודה כאן היא
תכונת זמן לינארי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משפט הפירוק
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
<div class="ppt-text-layer" style="left:16.6667%;top:20.0000%;width:71.6667%;height:36.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לכל תכונת זמן ליניארי 𝑃 מעל הפסוקים האטומיים 𝐴𝑃 קיימות תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 ותכונת חַיּוּת 𝑃 𝑙𝑖𝑣𝑒 (שתיהן מעל 𝐴𝑃) כך ש:
𝑃=𝑃𝑠𝑎𝑓𝑒∩𝑃𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:64.1667%;top:87.7628%;width:7.1413%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑃𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:87.7778%;width:7.8074%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑃𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.9684%;top:67.9479%;width:9.3649%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה:
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:76.6667%;width:63.5541%;height:8.0632%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃=𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ∩ 𝑃∪ 2 𝐴𝑃 𝜔 ∖closure P
</div>
</div>
<div class="ppt-text-layer" style="left:9.0231%;top:56.8262%;width:10.7463%;height:3.1415%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒄𝒍𝒐𝒔𝒖𝒓𝒆(𝑷)
</div>
</div>
<div class="ppt-text-layer" style="left:10.5333%;top:47.6439%;width:9.1667%;height:3.6006%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:14.1366%;top:65.2164%;width:2.3730%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑷
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משפט הפירוק
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
<div class="ppt-text-layer" style="left:16.6667%;top:20.0000%;width:71.6667%;height:36.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לכל תכונת זמן ליניארי 𝑃 מעל הפסוקים האטומיים 𝐴𝑃 קיימות תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 ותכונת חַיּוּת 𝑃 𝑙𝑖𝑣𝑒 (שתיהן מעל 𝐴𝑃) כך ש:
𝑃=𝑃𝑠𝑎𝑓𝑒∩𝑃𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:64.1667%;top:87.7628%;width:7.1413%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑃𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:87.7778%;width:7.8074%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑃𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.9684%;top:67.9479%;width:9.3649%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה:
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:76.6667%;width:63.5541%;height:8.0632%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃=𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ∩ 𝑃∪ 2 𝐴𝑃 𝜔 ∖closure P
</div>
</div>
<div class="ppt-text-layer" style="left:9.0231%;top:56.8262%;width:10.7463%;height:3.1415%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒄𝒍𝒐𝒔𝒖𝒓𝒆(𝑷)
</div>
</div>
<div class="ppt-text-layer" style="left:10.5333%;top:47.6439%;width:9.1667%;height:3.6006%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:14.1366%;top:65.2164%;width:2.3730%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑷
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משפט הפירוק
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
<div class="ppt-text-layer" style="left:16.6667%;top:20.0000%;width:71.6667%;height:36.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
לכל תכונת זמן ליניארי 𝑃 מעל הפסוקים האטומיים 𝐴𝑃 קיימות תכונת בטיחות 𝑃 𝑠𝑎𝑓𝑒 ותכונת חַיּוּת 𝑃 𝑙𝑖𝑣𝑒 (שתיהן מעל 𝐴𝑃) כך ש:
𝑃=𝑃𝑠𝑎𝑓𝑒∩𝑃𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:64.1667%;top:87.7628%;width:7.1413%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑃𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:32.5000%;top:87.7778%;width:7.8074%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑃𝑠𝑎𝑓𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.9684%;top:67.9479%;width:9.3649%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה:
</div>
</div>
<div class="ppt-text-layer" style="left:22.5000%;top:76.6667%;width:63.5541%;height:8.0632%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃=𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ∩ 𝑃∪ 2 𝐴𝑃 𝜔 ∖closure P
</div>
</div>
<div class="ppt-text-layer" style="left:9.0231%;top:56.8262%;width:10.7463%;height:3.1415%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒄𝒍𝒐𝒔𝒖𝒓𝒆(𝑷)
</div>
</div>
<div class="ppt-text-layer" style="left:10.5333%;top:47.6439%;width:9.1667%;height:3.6006%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:14.1366%;top:65.2164%;width:2.3730%;height:3.5903%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:center;direction:ltr;background:#e9e5dc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑷
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-024.png" alt="" />
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
<div class="ppt-text-layer" style="left:69.1593%;top:55.1598%;width:11.5380%;height:4.4953%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(11.10deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝜌∈ 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:84.1207%;top:62.3920%;width:13.3198%;height:10.7783%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
אם יש
𝜎 ′ ∈ 2 𝐴𝑃 𝜔
כך ש-𝜌 𝜎 ′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:66.8981%;top:71.9901%;width:18.1127%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;transform:rotate(348.81deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
נבחר את ה-𝜎′ הזאת
</div>
</div>
<div class="ppt-text-layer" style="left:55.8333%;top:74.4444%;width:9.5121%;height:20.1953%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
הצלחנו למצוא 𝜎′ כך ש-𝜌 𝜎 ′
שייכת ל- 𝑃 𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:22.6104%;top:55.1277%;width:11.5380%;height:4.4953%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;transform:rotate(11.10deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#69240c;white-space:pre-wrap;width:100%;">
𝜌∈ 2 𝐴𝑃 ∗
</div>
</div>
<div class="ppt-text-layer" style="left:35.8333%;top:62.2222%;width:15.0000%;height:10.7783%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
אם אין
𝜎 ′ ∈ 2 𝐴𝑃 𝜔
כך ש-𝜌 𝜎 ′ ∈𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:20.6509%;top:71.7043%;width:15.0799%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;transform:rotate(348.81deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
נבחר 𝜎′ כלשהיא
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:68.8889%;width:17.0121%;height:29.6198%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
למילה 𝜌𝜎′ יש את הרישא 𝜌 שכל המשך שלה לא יקיים את 𝑃 מקבלים ש-
𝜌 𝜎 ′ ∉𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃
לכן
𝜌 𝜎 ′ ∈ 𝑃 𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:5.3988%;top:4.4444%;width:85.0545%;height:7.4246%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
התכונה 𝑃 𝑙𝑖𝑣𝑒 =𝑃∪ 2 𝐴𝑃 𝜔 ∖closure P היא תכונת חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:23.3262%;top:13.3333%;width:73.1975%;height:5.3957%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה: נוכיח שלכל 𝜌∈ 2 𝐴𝑃 ∗ קיימת 𝜎 ′ ∈ 2 𝐴𝑃 𝜔 כך ש-𝜌 𝜎 ′ ∈ 𝑃 𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:66.2050%;top:21.1111%;width:11.3984%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
מקרה א&#x27;
</div>
</div>
<div class="ppt-text-layer" style="left:19.2354%;top:21.1111%;width:11.1881%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#69240c;white-space:pre-wrap;width:100%;">
מקרה ב&#x27;
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
25
</div>
</div>
<div class="ppt-text-layer" style="left:1.4075%;top:11.8434%;width:96.1178%;height:8.4381%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
טענה: 𝑃 𝑙𝑖𝑣𝑒 =𝑃∪ 2 𝐴𝑃 𝜔 ∖closure P היא תכונת חַיּוּת
</div>
</div>
<div class="ppt-text-layer" style="left:83.2517%;top:22.8852%;width:14.5189%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכחה:
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:31.1111%;width:56.1991%;height:8.7513%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜌∈pref 𝑃 ⇒𝜌∈pref( 𝑃 𝑙𝑖𝑣𝑒 )
</div>
</div>
<div class="ppt-text-layer" style="left:7.8843%;top:45.4331%;width:82.1157%;height:34.0431%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝜌∉pref 𝑃 ⇒𝜌. {} 𝜔 ∉closure 𝑃
⇒𝜌. {} 𝜔 ∈ 2 𝐴𝑃 𝜔 ∖closure 𝑃
⇒𝜌∈pref 2 𝐴𝑃 𝜔 ∖closure 𝑃
⇒𝜌∈pref 𝑃 𝑙𝑖𝑣𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:4.1775%;top:88.4105%;width:90.9771%;height:7.6462%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מסקנה: כל 𝜌 שייך ל-pref 𝑃 𝑙𝑖𝑣𝑒 ⇐ pref 𝑃 𝑙𝑖𝑣𝑒 = 2 𝐴𝑃 ∗
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
26
</div>
</div>
<div class="ppt-text-layer" style="left:7.5000%;top:17.7778%;width:85.2845%;height:10.5493%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝑎 𝑖 𝑎,𝑏 . 𝜎: 𝑖∈ℕ, 𝜎∈ 2 𝐴𝑃 𝜔 such that ∃ ∞ 𝑗. 𝑏∈𝜎 𝑗
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:31.7964%;width:92.1537%;height:11.3028%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
{𝑎} {𝑎} {𝑎} {𝑎} 𝑎 ⋯ 𝑎 𝑎,𝑏 𝑖+1 ⋯ …,𝑏,… ⋯ …,𝑏,… ⋯{…,𝑏,…}
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:49.8082%;width:79.1667%;height:12.5491%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
קל להוכיח שזאת איננה תכונת בטיחות וגם לא תכונת חַיּוֹת
אבל מתקיים 𝑃= 𝑃 𝑠𝑎𝑓𝑒 ∩ 𝑃 𝑙𝑖𝑣𝑒 עבור
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:69.0893%;width:92.1537%;height:9.0243%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃 𝑠𝑎𝑓𝑒 =closure 𝑃 = 𝑎 𝜔 ∪ 𝑎 𝑖 𝑎,𝑏 .𝜎: 𝑖∈ℕ, 𝜎∈ 2 𝐴𝑃 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:4.0206%;top:82.2222%;width:50.0000%;height:7.1721%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃 𝑙𝑖𝑣𝑒 =𝑃∪ 2 𝐴𝑃 𝜔 ∖closure 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:85.1643%;top:63.7959%;width:13.3619%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו טענות אלה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
27
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:20.2012%;width:91.4560%;height:6.5214%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝑃= 𝜎∈ 2 𝐴𝑃 𝜔 : ∃𝑖≥0 𝜎 𝑖 ⊨ Φ 2 ∧ ∀0≤𝑗≤𝑖.𝜎 𝑗 ⊨ Φ 1
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:45.0998%;width:87.5000%;height:12.5491%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
קל להוכיח שזאת איננה תכונת בטיחות וגם לא תכונת חַיּוֹת
אבל מתקיים 𝑃= 𝑃 𝑠𝑎𝑓𝑒 ∩ 𝑃 𝑙𝑖𝑣𝑒 עבור
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:69.0893%;width:92.1537%;height:7.0543%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃 𝑠𝑎𝑓𝑒 =closure 𝑃 =𝑃∪ 𝜎∈ 2 𝐴𝑃 𝜔 :∀𝑖≥0 𝜎 𝑖 ⊨ Φ 1
</div>
</div>
<div class="ppt-text-layer" style="left:4.5080%;top:82.2222%;width:50.0000%;height:7.1721%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:23.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑃 𝑙𝑖𝑣𝑒 =𝑃∪ 2 𝐴𝑃 𝜔 ∖closure 𝑃
</div>
</div>
<div class="ppt-text-layer" style="left:37.3845%;top:29.5636%;width:55.4614%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
באשר Φ 1 ו- Φ 2 הם פסוקי מצב כלשהם.
</div>
</div>
<div class="ppt-text-layer" style="left:4.5080%;top:33.0766%;width:15.8647%;height:5.9583%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffc5;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
Φ 1 until Φ 2
</div>
</div>
<div class="ppt-text-layer" style="left:85.1885%;top:61.3590%;width:13.3619%;height:3.8147%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו טענות אלה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
משפט הפירוק &quot;החזק&quot;
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
<div class="ppt-text-layer" style="left:12.9921%;top:23.3950%;width:74.0157%;height:38.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם 𝑃 תכונת זמן ליניארי כך ש 𝑃 = 𝑃𝑠𝑎𝑓𝑒 ∩ 𝑃𝑙𝑖𝑣𝑒
כש 𝑃𝑠𝑎𝑓𝑒תכונת בטיחות ו 𝑃𝑙𝑖𝑣𝑒 תכונת חַיּוּת אז:
• 𝑐𝑙𝑜𝑠𝑢𝑟𝑒 𝑃 ⊆ 𝑃𝑠𝑎𝑓𝑒
• 𝑃𝑙𝑖𝑣𝑒⊆ 𝑃∪ ( 2𝐴𝑃 𝜔 ∖𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃))
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:73.1061%;width:93.3333%;height:16.6050%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• 𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃) היא תכונת הבטיחות החזקה ביותר
• 𝑃∪( 2𝐴𝑃 𝜔 ∖𝑐𝑙𝑜𝑠𝑢𝑟𝑒(𝑃))היא תכונת החַיּוּת החלשה ביותר
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-029.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיווג תכונות זמן ליניארי
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
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/15-liveness-properties/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיכום תכונות זמן ליניארי
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
<div class="ppt-text-layer" style="left:0.0000%;top:17.7778%;width:99.1667%;height:77.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• תכונות זמן ליניארי:
קבוצות של מילים באורך אינסופי מעל האלף-בית 2𝐴𝑃 (עקבות)
• שמורה: דורשים שתנאי מצב 𝜙 מתקיים בכל אות במילה
• לכל סדרת עקבות המפרה תכונת בטיחות יש רישא הגורמת לכך:
  • תכונת בטיחות היא רגולרית אם קבוצת הרישות הרעות היא שפה רגולרית
  • שמורות הן תכונות בטיחות רגולריות עם רישא רעה מינימלית 𝜙 ∗ ¬𝜙
  • תכונות בטיחות מגבילות את הרישות של ההתנהגות
• תכונות חַיּוּת אינן פוסלות אף התנהגות סופית
  • תכונות חַיּוּת מגבילות את הזנבות של ההתנהגות
• כל תכונת זמן ליניארית היא חיתוך תכונת בטיחות ותכונת חַיּוּת
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
