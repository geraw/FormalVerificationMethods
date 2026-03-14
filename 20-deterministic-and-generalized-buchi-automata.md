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
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-001.png" alt="" />
<div class="ppt-text-layer" style="left:14.1667%;top:46.6667%;width:70.0000%;height:23.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
גרא וייס
המחלקה למדעי המחשב
אוניברסיטת בן-גוריון
</div>
</div>
<div class="ppt-text-layer" style="left:5.0000%;top:21.9587%;width:90.0000%;height:21.4352%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
אוטומטי Büchi דטרמיניסטים ומוכללים
</div>
</div>
<div class="ppt-text-layer" style="left:76.4369%;top:-7.2793%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:87.3772%;top:-0.8058%;width:11.4335%;height:13.4635%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Aharoni','Segoe UI','Arial',sans-serif;font-size:54.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
597
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-002.png" alt="" />
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
2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-003.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: אוטומט Büchi
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
<div class="ppt-text-layer" style="left:7.5000%;top:23.3333%;width:88.3333%;height:70.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט Büchi לא דטרמיניסטי (NBA) הוא :〈𝑄, Σ, 𝛿, 𝑄 0 , 𝐹〉
• 𝑄 היא קבוצת מצבים סופית
• Σהוא האלפבית
• 𝛿: 𝑄×Σ→ 2 𝑄 היא פונקציית מעברים
• 𝑄 0 ⊆𝑄 היא קבוצת מצבים התחלתיים
• 𝐹⊆𝑄 היא קבוצת מצבים מקבלים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-004.png" alt="" />
<div class="ppt-text-layer" style="left:6.6667%;top:28.8273%;width:89.4792%;height:10.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מילים אינסופית &quot;המבקרות&quot; אינסוף פעמים במצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: שפה של NBA
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
<div class="ppt-text-layer" style="left:1.6667%;top:67.8394%;width:94.4792%;height:16.6050%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ריצה אינסופית 𝑞0𝑞1…היא מקבלת אם 𝑞 𝑖 ∈𝐹 עבור אינסוף 𝑖-ים
𝑤∈ Σ 𝜔 מתקבלת ע&quot;י 𝒜 אם יש ריצה אינסופית מקבלת של 𝑤 ב 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:29.6124%;top:90.9224%;width:43.3042%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#7030a0;white-space:pre-wrap;width:100%;">
אנחנו עובדים עם אוטומט לא דטרמיניסטי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-005.png" alt="" />
<div class="ppt-text-layer" style="left:9.6607%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: NBA ושפות 𝜔-רגולריות
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
<div class="ppt-text-layer" style="left:6.7221%;top:21.7917%;width:86.5558%;height:14.3611%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מחלקת השפות שאפשר להגדיר באמצעות NBAזהה
למחלקת השפות שאפשר להגדיר באמצעות ביטויים 𝜔-רגולריים
</div>
</div>
<div class="ppt-text-layer" style="left:9.4604%;top:70.4197%;width:83.8176%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
הוכחנו את שתי הטענות (באופן קוֹנְסְטְרוּקְטִיבִי) במצגת קודמת
</div>
</div>
<div class="ppt-text-layer" style="left:12.3237%;top:44.9837%;width:79.6740%;height:16.6050%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור כל אוטומט 𝒜, השפה ℒ 𝜔 (𝒜) היא 𝜔-רגולרית
לכל שפה 𝜔 -רגולרית 𝐿 קיים אוטומט 𝒜כך ש 𝐿=ℒ 𝜔 𝒜
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-006.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה: אוטומטים שקולים
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
<div class="ppt-text-layer" style="left:8.3333%;top:67.3120%;width:85.6562%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שני האוטומטים מגדירים: אינסוף פעמים 𝑎 וגם אינסוף פעמים 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:84.0764%;width:96.6043%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כדי להכריע אם שני אוטומטים שקולים צריך אלגוריתם לבדיקה אם השפה של האוטומט המתאר את ההפרש בין השפות שלהם היא ריקה
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:74.4844%;width:68.9067%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
always eventually 𝑎 ∧ always eventually 𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:32.7881%;top:61.8193%;width:4.7569%;height:4.7222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:26.7638%;top:53.3471%;width:2.5521%;height:4.7222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:16.7985%;top:62.0739%;width:4.6875%;height:4.7222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:20.0971%;top:35.8239%;width:2.4826%;height:4.7222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:32.5944%;top:35.0660%;width:5.6477%;height:4.0391%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:67.8819%;top:55.2662%;width:2.4826%;height:4.7222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:67.1441%;top:23.4491%;width:2.5521%;height:4.7222%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:21.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:56.1238%;top:16.9647%;width:5.6477%;height:4.0391%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:53.0406%;top:38.1046%;width:5.6477%;height:4.0391%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:74.8324%;top:61.3757%;width:5.6477%;height:4.0391%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:78.2639%;top:39.1053%;width:5.6477%;height:4.0391%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:43.1720%;top:36.8433%;width:6.7528%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
∼
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-007.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תנאי שקול לאי-רֵיקוּת השפה
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
<div class="ppt-text-layer" style="left:21.6667%;top:23.3333%;width:57.5000%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
אם ורק אם
</div>
</div>
<div class="ppt-text-layer" style="left:21.6667%;top:17.7778%;width:57.5000%;height:5.3854%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
ℒ 𝜔 𝒜 ≠∅
</div>
</div>
<div class="ppt-text-layer" style="left:20.8333%;top:32.2222%;width:60.0000%;height:18.8490%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
∃ 𝑞 0 ∈ 𝑄 0 , 𝑞∈𝐹, 𝑤∈ Σ ∗ ,𝑣∈ Σ + .
𝑞∈ 𝛿 ∗ 𝑞 0 ,𝑤 ∧𝑞∈ 𝛿 ∗ (𝑞,𝑣)
</div>
</div>
<div class="ppt-text-layer" style="left:48.6602%;top:64.4885%;width:2.8638%;height:6.6767%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞
</div>
</div>
<div class="ppt-text-layer" style="left:33.5137%;top:55.2836%;width:2.4822%;height:6.5579%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:35.3545%;top:69.8936%;width:1.6617%;height:6.6767%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑤
</div>
</div>
<div class="ppt-text-layer" style="left:65.4216%;top:59.3682%;width:1.6617%;height:6.6767%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑣
</div>
</div>
<div class="ppt-text-layer" style="left:2.5000%;top:81.1111%;width:95.0000%;height:15.7477%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffcc;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝛿 ∗ 𝑞, 𝑤 הוא סימון לקבוצת המצבים שהאוטומט יכול להגיע מ-𝑞 בקריאת המילה 𝑤:
𝛿 ∗ 𝑞, 𝜖 = 𝑞 , 𝛿 ∗ 𝑞, 𝐴 =𝛿 𝑞, 𝐴 , 𝛿 ∗ 𝑞, 𝜎 = 𝑝∈𝛿 𝑞,𝜎 0 𝛿 ∗ (𝑝,𝜎 1.. )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-008.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:-2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בדיקה אם שפת ה-𝜔 של אוטומט ריקה
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
<div class="ppt-text-layer" style="left:0.0000%;top:17.7778%;width:100.0000%;height:76.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• אם מתעלמים מהאותיות על המעברים אפשר להתייחס לאוטומט 𝒜 כגרף 𝐺 𝒜 =〈 𝑉 𝒜 , 𝐸 𝒜 〉באשר 𝑉 𝒜 =𝑆 ו 𝑠, 𝑠 ′ ∈ 𝐸 𝒜 אם ורק אם קיימת 𝛼 כך ש 𝑠,𝛼, 𝑠 ′ ∈𝛿
• קבוצת צמתים 𝑋 בגרף נקראת רכיב קשירות חזק אם בין כל זוג 𝑣, 𝑣 ′ ∈𝑋 מחבר מסלול בגרף
  • רכיב קשירות חזק אינו טריוויאלי אם הוא מכיל לפחות קשת אחת.
  • הוא מקסימאלי אם אין רכיב קשירות חזק המכיל אותו.
• כל מעגל נמצא ברכיב קשירות חזק לא טריוויאלי
וכל רכיב קשירות לא טריוויאלי מכיל מעגל
• מקבלים: ℒ 𝜔 (𝒜) אינה ריקה אם ורק אם קיים רכיב קשירות חזק לא טריוויאלי ב- 𝐺 𝒜 הנגיש ממצב התחלתי ומכיל מצב מקבל. מספיק לבדוק רכיבי קשירות חזקים מקסימאליים.
• מציאת רכיבי הקשירות המקסימאליים ובדיקת נגישות לוקחות, כל אחת, 𝒪 𝒜 צעדים
</div>
</div>
<div class="ppt-text-layer" style="left:11.6667%;top:88.6102%;width:73.5474%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
מסקנה: ניתן לבדוק אם שפת ה 𝜔 של 𝒜 היא ריקה בזמן 𝒪 𝒜
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-009.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט שאינו חוסם
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
<div class="ppt-text-layer" style="left:10.0000%;top:33.3333%;width:80.8333%;height:24.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט 𝒜 אינו חוסם אם
𝛿(𝑞,𝐴)  ∅ לכל 𝑞∈𝑆 ולכל 𝐴∈Σ
</div>
</div>
<div class="ppt-text-layer" style="left:18.8915%;top:77.9262%;width:58.6085%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#840900;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
  לכל מילת קלט יש ריצה אינסופית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-010.png" alt="" />
<div class="ppt-text-layer" style="left:11.8230%;top:2.2432%;width:71.6667%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בלי הגבלת הכלליות:
נניח אוטומט שאינו חוסם
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
<div class="ppt-text-layer" style="left:4.1667%;top:23.3124%;width:91.6667%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• לכל אוטומט NBA, 𝒜, קיים אוטומט לא חוסם 𝑡𝑟𝑎𝑝(𝒜) כך ש:
  • |𝑡𝑟𝑎𝑝 𝒜 | =𝒪(|𝒜|)
  • וגם ℒ 𝜔 𝒜 = ℒ 𝜔 𝑡𝑟𝑎𝑝 𝒜
• עבור 𝒜=〈𝑄,Σ,𝛿, 𝑄 0 ,𝐹〉 נגדיר 𝑡𝑟𝑎𝑝(𝒜)=〈 𝑄 ′ ,Σ,𝛿′, 𝑄0, 𝐹〉
  𝑄’=𝑄∪ 𝑞𝑡𝑟𝑎𝑝 (בהנחה ש- 𝑞 𝑡𝑟𝑎𝑝 איננו איבר ב-𝑄)
</div>
</div>
<div class="ppt-text-layer" style="left:20.0000%;top:79.2996%;width:67.5975%;height:15.3335%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
𝛿 ′ 𝑞,𝑎 = 𝛿 𝑞,𝐴 if 𝑞∈𝑄 and 𝛿 𝑞,𝐴 ≠∅ &amp; 𝑞 trap , otherwise
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-011.png" alt="" />
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
11
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-012.png" alt="" />
<div class="ppt-text-layer" style="left:6.3962%;top:-2.7778%;width:90.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תזכורת: אוטומט דֶּטֶרְמִינִיסְטִי ואוטומט שלם
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
<div class="ppt-text-layer" style="left:8.3333%;top:21.1111%;width:86.6667%;height:57.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט 𝒜 נקרא דֶּטֶרְמִינִיסְטִי (deterministic) אם
| 𝑄 0 |=1 וגם 𝛿 𝑞,𝐴 ≤1 לכל 𝑞∈𝑄 ולכל 𝐴∈Σ
אוטומט 𝒜 נקרא שלם (total) אם
𝛿 𝑞,𝐴 ≥1 לכל 𝑞∈𝑄 ולכל 𝐴∈Σ
</div>
</div>
<div class="ppt-text-layer" style="left:8.9185%;top:79.8957%;width:82.7482%;height:13.9123%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
באוטומט דֶּטֶרְמִינִיסְטִי יש ריצה יחידה לכל מילת קלט
אפשר להפוך כל אוטומט לאוטומט שלם שקול (איך?)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-013.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה של DBA לתכונת זמן ליניארי
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
<div class="ppt-text-layer" style="left:4.8236%;top:68.1670%;width:88.0502%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שני האוטומטים מייצגים את תכונת הזמן הליניארי: &quot;תמיד 𝑏 ואינסוף פעמים 𝑎&quot;
</div>
</div>
<div class="ppt-text-layer" style="left:68.0018%;top:53.5035%;width:6.9982%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
NBA
</div>
</div>
<div class="ppt-text-layer" style="left:23.9546%;top:54.1379%;width:6.8755%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
DBA
</div>
</div>
<div class="ppt-text-layer" style="left:32.2335%;top:80.3622%;width:33.2304%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
always 𝑏∧eventually 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:11.8856%;top:30.1313%;width:9.9728%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:23.9546%;top:33.1425%;width:9.9728%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:37.1332%;top:29.8099%;width:8.0795%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:24.4025%;top:45.5994%;width:8.0795%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:69.7599%;top:33.7344%;width:8.0795%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:81.4984%;top:30.1572%;width:8.0795%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.8721%;top:29.8966%;width:4.0033%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:70.8333%;top:45.7257%;width:4.0033%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:5.2051%;top:90.1753%;width:13.6073%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו טענה זאת
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-014.png" alt="" />
<div class="ppt-text-layer" style="left:7.5000%;top:3.3246%;width:85.0000%;height:12.3458%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תזכורת: שקילות אומגה ⇍ שקילות סופית
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
<div class="ppt-text-layer" style="left:0.8289%;top:82.5278%;width:98.3420%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ℒ 𝜔 𝒜 1 = ℒ 𝜔 ( 𝒜 2 ) אבל ℒ 𝒜 1  ℒ 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:0.8289%;top:19.9899%;width:29.1667%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל המילים הסופיות בהן כל האותיות מכילות את הפסוק האטומי 𝑎 ואורכן אי-זוגי
</div>
</div>
<div class="ppt-text-layer" style="left:77.8124%;top:45.6172%;width:17.2190%;height:19.2977%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כל המילים האינסופיות בהן כל האותיות מכילות את הפסוק האטומי 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:11.9390%;top:45.7474%;width:20.9320%;height:15.7075%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל המילים הסופיות בהן כל האותיות מכילות את הפסוק האטומי 𝑎 ואורכן זוגי
</div>
</div>
<div class="ppt-text-layer" style="left:50.3125%;top:23.7269%;width:3.3681%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:50.0000%;top:35.1621%;width:3.3681%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:49.2708%;top:52.7546%;width:3.3681%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:49.1667%;top:63.8889%;width:3.3681%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-015.png" alt="" />
<div class="ppt-text-layer" style="left:8.8902%;top:3.3333%;width:85.0000%;height:14.5247%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
תזכורת: שקילות סופית ⇍שקילות 𝜔
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
<div class="ppt-text-layer" style="left:0.6687%;top:86.1311%;width:97.8666%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
ℒ 𝒜 1 =ℒ 𝒜 2 אבל ℒ 𝜔 𝒜 1 ≠ ℒ 𝜔 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:8.8902%;top:61.2219%;width:23.8813%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
שפה ריקה
</div>
</div>
<div class="ppt-text-layer" style="left:2.5629%;top:24.0267%;width:23.1475%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל המילים האינסופיות בהן כל האותיות מכילות את הפסוק האטומי 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.3358%;top:49.3186%;width:17.8637%;height:22.8880%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כל המילים הסופיות באורך גדול מ-1 בהן כל האותיות מכילות את הפסוק האטומי 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:50.0000%;top:65.9491%;width:3.3681%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:40.2778%;top:54.8380%;width:3.3681%;height:6.2732%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:49.1667%;top:35.5556%;width:3.3681%;height:6.2731%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:61.3194%;top:23.7269%;width:3.3681%;height:6.2731%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:43.6500%;top:52.0230%;width:34.4904%;height:10.8451%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;background:#b81e00;opacity:1.000;transform:rotate(159.11deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בחירה לא דֶּטֶרְמִינִיסְטִית
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-016.png" alt="" />
<div class="ppt-text-layer" style="left:1.1756%;top:18.7294%;width:88.3333%;height:68.2975%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אם 𝒜 1 ו 𝒜 2 דטרמיניסטים אז:
ℒ(𝒜 1 )=ℒ 𝒜 2 גורר שגם ℒ 𝜔 (𝒜 1 )= ℒ 𝜔 𝒜 2
הוכחה: אם ℒ(𝒜 1 )=ℒ 𝒜 2 מקבלים:
  𝑤∈ ℒ 𝜔 𝒜 1
  ⇕
  ∃ ∞ 𝑖 . 𝑤 0..𝑖 ∈ℒ 𝒜 1
  ⇕
  ∃ ∞ 𝑖 . 𝑤 0..𝑖 ∈ℒ 𝒜 2
  ⇕
  𝑤∈ ℒ 𝜔 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שקילות אוטומטים דטרמיניסטיים
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
<div class="ppt-text-layer" style="left:35.7121%;top:53.5121%;width:5.0173%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
???
</div>
</div>
<div class="ppt-text-layer" style="left:36.1311%;top:75.5553%;width:5.0173%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
???
</div>
</div>
<div class="ppt-text-layer" style="left:35.7121%;top:64.3093%;width:10.8725%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מההנחה
</div>
</div>
<div class="ppt-text-layer" style="left:62.4173%;top:56.2531%;width:14.5224%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0..𝑖 ∈ℒ( 𝒜 1 )
</div>
</div>
<div class="ppt-text-layer" style="left:66.9812%;top:60.9135%;width:14.5224%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0..𝑖 ∈ℒ( 𝒜 1 )
</div>
</div>
<div class="ppt-text-layer" style="left:72.7762%;top:65.7078%;width:14.5224%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0..𝑖 ∈ℒ( 𝒜 1 )
</div>
</div>
<div class="ppt-text-layer" style="left:64.6768%;top:49.6215%;width:3.0924%;height:3.5341%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:76.6924%;top:49.6215%;width:3.0924%;height:3.5341%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:88.7080%;top:49.6215%;width:3.0924%;height:3.5341%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:60.4169%;top:46.8240%;width:5.8062%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0
</div>
</div>
<div class="ppt-text-layer" style="left:66.2230%;top:46.8240%;width:5.4562%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:72.5993%;top:46.8240%;width:7.5943%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 𝑖+1
</div>
</div>
<div class="ppt-text-layer" style="left:89.2190%;top:52.6147%;width:5.9773%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:60.3775%;top:70.2027%;width:14.8141%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0..𝑖 ∈ℒ( 𝒜 2 )
</div>
</div>
<div class="ppt-text-layer" style="left:65.3820%;top:74.7128%;width:14.8141%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0..𝑖 ∈ℒ( 𝒜 2 )
</div>
</div>
<div class="ppt-text-layer" style="left:71.6128%;top:79.5172%;width:14.8141%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0..𝑖 ∈ℒ( 𝒜 2 )
</div>
</div>
<div class="ppt-text-layer" style="left:64.2251%;top:89.2158%;width:3.0924%;height:3.5341%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:76.2406%;top:89.2158%;width:3.0924%;height:3.5341%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:88.2562%;top:89.2158%;width:3.0924%;height:3.5341%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:59.9651%;top:86.4183%;width:5.8062%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 0
</div>
</div>
<div class="ppt-text-layer" style="left:65.7712%;top:86.4183%;width:5.4562%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:72.1475%;top:86.4183%;width:7.5943%;height:4.0391%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#c00000;white-space:pre-wrap;width:100%;">
𝑤 𝑖+1
</div>
</div>
<div class="ppt-text-layer" style="left:90.1319%;top:92.3935%;width:6.0355%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#c00000;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:0.8165%;top:65.0582%;width:15.4952%;height:13.9123%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#34b2cf;white-space:pre-wrap;width:100%;">
איפה השתמשנו בעובדה שהאוטומטים דטרמיניסטיים?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-017.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
שקילות אוטומטים דטרמיניסטיים
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
<div class="ppt-text-layer" style="left:5.8333%;top:16.6667%;width:88.3333%;height:27.2263%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אם 𝒜 1 ו 𝒜 2 דטרמיניסטים אז:
ℒ(𝒜 1 )=ℒ 𝒜 2 גורר שגם ℒ 𝜔 (𝒜 1 )= ℒ 𝜔 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:14.1667%;top:47.2120%;width:76.6667%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffff00;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
המשפט ההפוך לא נכון, גם אם האוטומטים דטרמיניסטיים
</div>
</div>
<div class="ppt-text-layer" style="left:37.4841%;top:86.6667%;width:22.6005%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דוגמה נגדית?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-018.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
NBA יותר עשירים מ-DBA
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
<div class="ppt-text-layer" style="left:6.6667%;top:18.8889%;width:84.1667%;height:75.5556%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
למדנו בקורס מודלים חישוביים:
NFA ו DFA מתארים את אותה משפחת שפות
זה לא נכון למילים אינסופיות:
NBA ו-DBA אינם מתארים את אותה משפחת השפות
הוכחה:
  לא קיים DBA המקבל את השפה
  𝐴+𝐵 ∗ 𝐵 𝜔
  אבל קיים אוטומט NBA המקבל אותה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-019.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:2.2222%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אוטומט לא דטרמיניסטי שלא ניתן לחקות באמצעות אוטומט דטרמיניסטי
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
<div class="ppt-text-layer" style="left:-1.0802%;top:79.1641%;width:102.6280%;height:13.0148%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:25.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
האוטומט &quot;מנחש&quot; באופן אי-דטרמיניסטי מתי מתחיל רצף ה-𝐵-ים
טענה: לא ניתן לחקות את הניחוש הזה באמצעות אוטומט דטרמיניסטי!
</div>
</div>
<div class="ppt-text-layer" style="left:27.5000%;top:65.4905%;width:41.6667%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴+𝐵 ∗ 𝐵 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:33.2858%;top:27.3953%;width:5.1204%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:46.4942%;top:38.5470%;width:5.2480%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:32.9452%;top:54.9136%;width:5.2480%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:59.7762%;top:54.8101%;width:5.2480%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-020.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:87.2368%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
הוכחת הטענה מהשקף הקודם
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.7961%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.1316%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
20
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:18.8889%;width:97.5000%;height:78.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:19.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נניח בשלילה שקיים אוטומט דטרמיניסטי המקבל את השפה 𝐴+𝐵 ∗ 𝐵 𝜔
• נזין אותו במילה 𝐴𝐵𝐵𝐵𝐵… עם מספיק 𝐵-ים עד שנגיע למצב מקבל
• נמשיך ב-𝐴 ואחריו מספיק 𝐵-ים עד שנגיע שוב למצב מקבל
• נחזור על התהליך עד שנבקר באותו המצב המקבל פעמיים (שובך היונים ) )
• קיבלנו את התמונה הבאה:
• זה אומר שיש מילה עם אינסוף 𝐴-ים שהאוטומט מקבל, בסתירה להגדרת השפה
𝐴𝐵…𝐵𝐴𝐵…𝐵𝐴𝐵…𝐵 𝐴𝐵…𝐵𝐴𝐵…𝐵𝐴𝐵…𝐵 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:27.1508%;top:68.8072%;width:11.9020%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט
במצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:66.3269%;top:68.8072%;width:20.6032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט במצב
מקבל שכבר היה קודם
</div>
</div>
<div class="ppt-text-layer" style="left:17.4553%;top:68.8072%;width:14.2521%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט
במצב התחלתי
</div>
</div>
<div class="ppt-text-layer" style="left:23.2047%;top:62.2223%;width:44.7428%;height:4.6311%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴𝐵…𝐵𝐴𝐵…𝐵𝐴𝐵…𝐵𝐴𝐵…𝐵𝐴𝐵…𝐵𝐴𝐵…𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:35.3401%;top:68.8072%;width:11.9020%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט
במצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:43.1044%;top:68.8072%;width:11.9020%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט
במצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:52.0321%;top:68.8072%;width:11.9020%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט
במצב מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:60.8435%;top:68.8072%;width:11.9020%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:9.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
האוטומט
במצב מקבל
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-021.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-5.5556%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אותה ההוכחה במילים יותר פורמליות
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
21
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:62.5450%;width:94.5408%;height:30.1518%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• נסמן ב- 𝑞 𝑖 = 𝛿 ∗ 𝑞 0 , 𝑤 𝑖 1.. 𝑛 𝑖 את המצב אליו מגיע האוטומט אחרי קריאת המילה 𝑤 𝑖 1.. 𝑛 𝑖
• בגלל שכל המילים בשפה, קיימים 0&lt; 𝑛 1 &lt;𝑛2&lt;𝑛3&lt; עבורם 𝑞 𝑖 ∈𝐹 לכל 𝑖
• ע&quot;פ עקרון שובך היונים, בגלל ש-𝐹 קבוצה סופית, חייבים להיות 𝑖,𝑗, כך ש- 𝑖&lt;𝑗 וגם 𝑞 𝑖 = 𝑞 𝑗
• מקבלים שהריצה של המילה 𝑤 𝑖 1.. 𝑛 𝑖 𝑤 𝑗 𝑛 𝑖 +1 .. 𝑛 𝑗 𝜔 עוברת אינסוף פעמים במצב מקבל
• זאת סתירה, מכיוון שזה אומר שהאוטומט מקבל מילה המכילה אינסוף 𝐴-ים (ולכן איננה בשפה)
</div>
</div>
<div class="ppt-text-layer" style="left:8.8020%;top:11.1111%;width:89.1974%;height:10.7708%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נניח בשלילה שקיים אוטומט Büchi דטרמיניסטי 𝒜=〈𝑄, Σ, 𝛿, 𝑞 0 ,𝐹〉 המקבל את השפה 𝐴+𝐵 ∗ 𝐵 𝜔
• עבור כל סדרת מספרים טבעיים 0&lt;𝑛1&lt;𝑛2&lt;𝑛3&lt; נגדיר את המילים האינסופיות:
</div>
</div>
<div class="ppt-text-layer" style="left:32.0833%;top:25.5556%;width:37.0833%;height:34.2170%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑤 1 = 𝐴𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝑤 1 [1.. 𝑛 1 ] 𝐵𝐵…
𝑤 2 = 𝑤 1 1.. 𝑛 1 𝐴𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝐵𝐵… 𝑤 2 [1.. 𝑛 2 ]
⋮
𝑤 𝑖+1 = 𝑤 𝑖 1.. 𝑛 𝑖 𝐴𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝐵𝐵… 𝑤 𝑖+1 [1.. 𝑛 𝑖+1 ]
⋮
</div>
</div>
<div class="ppt-text-layer" style="left:1.2783%;top:22.6200%;width:13.6351%;height:11.4514%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#840900;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:10.50pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מילים עם מספר סופי של 𝐴-ים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-022.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה בניית אוטומט הַחֶזְקָה לא עובדת?
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
<div class="ppt-text-layer" style="left:1.6667%;top:22.2222%;width:93.3333%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• עבור אוטומטים לשפות מעל מילים סופיות: מתרגמים אוטומט לא דטרמיניסטי לדטרמיניסטי שמצביו הן קבוצות מצבים
• אוטומט הַחֶזְקָה מאפשר לעקוב לאיזה מצבים יכול האוטומט
האי-דטרמיניסטי להגיע לאחר קריאת רישא של המילה
• עבור מילים באורך סופי: מקבלים את המילה אם אחד המצבים שהאוטומט האי-דטרמיניסטי יכול היה להגיע אליהם הוא מקבל
• למה זה לא עובד עבור שפות אינסופיות?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-023.png" alt="" />
<div class="ppt-text-layer" style="left:48.2460%;top:79.0590%;width:4.8222%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה בניית אוטומט הַחֶזְקָה לא עובדת?
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
<div class="ppt-text-layer" style="left:74.4475%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:86.7712%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:78.1651%;top:33.8111%;width:10.7243%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:87.2085%;top:45.9828%;width:11.5206%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:70.4563%;top:46.1719%;width:7.5803%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:10.5748%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 }
</div>
</div>
<div class="ppt-text-layer" style="left:36.3874%;top:69.6152%;width:10.2674%;height:13.6899%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:37.3901%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 , 𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:10.1401%;top:70.1858%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:25.3271%;top:33.2376%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:6.8138%;top:61.1778%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:2.1652%;top:53.1632%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:42.7608%;top:36.1102%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:24.0320%;top:42.4533%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:41.5134%;top:60.0499%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:20.5849%;top:57.7959%;width:13.0843%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(323.98deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.6841%;top:71.0822%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:59.6076%;top:20.9694%;width:37.8438%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט לא-דטרמיניסטי 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:12.7442%;top:23.7123%;width:34.0480%;height:6.8271%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט דטרמיניסטי 2 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:59.2837%;top:59.3831%;width:23.9865%;height:5.9240%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בניית אוטומט הַחֶזְקָה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-024.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה בניית אוטומט הַחֶזְקָה לא עובדת?
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
<div class="ppt-text-layer" style="left:74.4475%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:86.7712%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:78.1651%;top:33.8111%;width:10.7243%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:87.2085%;top:45.9828%;width:11.5206%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:70.4563%;top:46.1719%;width:7.5803%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:10.5748%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 }
</div>
</div>
<div class="ppt-text-layer" style="left:36.3874%;top:69.6152%;width:10.2674%;height:13.6899%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:37.3901%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 , 𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:10.1401%;top:70.1858%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:25.3271%;top:33.2376%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:6.8138%;top:61.1778%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:2.1652%;top:53.1632%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:42.7608%;top:36.1102%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:24.0320%;top:42.4533%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:41.5134%;top:60.0499%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:20.5849%;top:57.7959%;width:13.0843%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(323.98deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:48.2460%;top:79.0590%;width:4.8222%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:22.6841%;top:71.0822%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:54.0338%;top:72.0428%;width:37.7130%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#c3c1c1;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
האם האוטומטים האלה שקולים?
</div>
</div>
<div class="ppt-text-layer" style="left:59.6076%;top:20.9694%;width:37.8438%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט לא-דטרמיניסטי 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:12.7442%;top:23.7123%;width:34.0480%;height:6.8271%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט דטרמיניסטי 2 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:59.2837%;top:59.3831%;width:23.9865%;height:5.9240%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בניית אוטומט הַחֶזְקָה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-025.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה בניית אוטומט הַחֶזְקָה לא עובדת?
</div>
</div>
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
<div class="ppt-text-layer" style="left:74.4475%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:86.7712%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:78.1651%;top:33.8111%;width:10.7243%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:87.2085%;top:45.9828%;width:11.5206%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:70.4563%;top:46.1719%;width:7.5803%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:10.5748%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 }
</div>
</div>
<div class="ppt-text-layer" style="left:36.3874%;top:69.6152%;width:10.2674%;height:13.6899%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:37.3901%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 , 𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:10.1401%;top:70.1858%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:25.3271%;top:33.2376%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:6.8138%;top:61.1778%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:2.1652%;top:53.1632%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:42.7608%;top:36.1102%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:24.0320%;top:42.4533%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:41.5134%;top:60.0499%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:20.5849%;top:57.7959%;width:13.0843%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(323.98deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:48.2460%;top:79.0590%;width:4.8222%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:22.6841%;top:71.0822%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:59.2837%;top:59.3831%;width:23.9865%;height:5.9240%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בניית אוטומט הַחֶזְקָה
</div>
</div>
<div class="ppt-text-layer" style="left:54.0601%;top:80.4313%;width:37.7131%;height:5.0012%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#00b050;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בקורס קודם הוכחנו ℒ 𝒜 =ℒ( 2 𝒜 )
</div>
</div>
<div class="ppt-text-layer" style="left:54.0338%;top:72.0428%;width:37.7130%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#c3c1c1;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
האם האוטומטים האלה שקולים?
</div>
</div>
<div class="ppt-text-layer" style="left:59.6076%;top:20.9694%;width:37.8438%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט לא-דטרמיניסטי 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:12.7442%;top:23.7123%;width:34.0480%;height:6.8271%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט דטרמיניסטי 2 𝒜
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-026.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה בניית אוטומט הַחֶזְקָה לא עובדת?
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
<div class="ppt-text-layer" style="left:74.4475%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:86.7712%;top:36.0212%;width:5.6878%;height:7.1698%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-end;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:78.1651%;top:33.8111%;width:10.7243%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:87.2085%;top:45.9828%;width:11.5206%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:70.4563%;top:46.1719%;width:7.5803%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:10.5748%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 }
</div>
</div>
<div class="ppt-text-layer" style="left:36.3874%;top:69.6152%;width:10.2674%;height:13.6899%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:37.3901%;top:41.6454%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{ 𝑞 0 , 𝑞 1 }
</div>
</div>
<div class="ppt-text-layer" style="left:10.1401%;top:70.1858%;width:9.2900%;height:12.3866%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
{}
</div>
</div>
<div class="ppt-text-layer" style="left:25.3271%;top:33.2376%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:6.8138%;top:61.1778%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:2.1652%;top:53.1632%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:42.7608%;top:36.1102%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:24.0320%;top:42.4533%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏∧¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:41.5134%;top:60.0499%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:20.5849%;top:57.7959%;width:13.0843%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(323.98deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:48.2460%;top:79.0590%;width:4.8222%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:22.6841%;top:71.0822%;width:10.2430%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:59.6076%;top:20.9694%;width:37.8438%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט לא-דטרמיניסטי 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:12.7442%;top:23.7123%;width:34.0480%;height:6.8271%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אוטומט דטרמיניסטי 2 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:54.0338%;top:88.8843%;width:37.7393%;height:5.3994%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ff0000;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
אבל 𝑎,𝑏 𝑏 𝜔 ∈ ℒ 𝜔 2 𝒜 ∖ ℒ 𝜔 𝒜
</div>
</div>
<div class="ppt-text-layer" style="left:54.0601%;top:80.4313%;width:37.7131%;height:5.0012%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#00b050;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בקורס קודם הוכחנו ℒ 𝒜 =ℒ( 2 𝒜 )
</div>
</div>
<div class="ppt-text-layer" style="left:54.0338%;top:72.0428%;width:37.7130%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#c3c1c1;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
האם האוטומטים האלה שקולים?
</div>
</div>
<div class="ppt-text-layer" style="left:17.6445%;top:84.2350%;width:22.7232%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
מה רע בריצה הזאת?
</div>
</div>
<div class="ppt-text-layer" style="left:59.2837%;top:59.3831%;width:23.9865%;height:5.9240%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
בניית אוטומט הַחֶזְקָה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-027.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
למה בניית אוטומט הַחֶזְקָה לא עובדת?
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
<div class="ppt-text-layer" style="left:4.1667%;top:18.2597%;width:94.1667%;height:68.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:justify;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• הבעיה היא תנאי הקבלה:
  • תנאי הקבלה למילים אינסופיות הוא שיש ריצה אחת שעוברת אינסוף פעמים במצב מקבל
  • אוטומט הַחֶזְקָה יקבל גם אם יש אינסוף רישות שלכל אחת מהן יש ריצה שונה המגיעה למצב מקבל
  • זה המקרה עבור האוטומט למטה והמילה {𝑏𝑙𝑖𝑛𝑘} 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:32.6309%;top:80.5622%;width:4.9645%;height:6.3097%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:2.25px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:57.5355%;top:80.6662%;width:4.9645%;height:6.3097%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffcc;opacity:1.000;border:4.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:31.2796%;top:70.4317%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:43.6659%;top:78.2464%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:54.2913%;top:70.4584%;width:10.4903%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑏𝑙𝑖𝑛𝑘
</div>
</div>
<div class="ppt-text-layer" style="left:29.1667%;top:88.2054%;width:34.4877%;height:5.9053%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
eventually always ¬𝑏𝑙𝑖𝑛𝑘
</div>
</div>
<div class="ppt-text-layer" style="left:7.2442%;top:86.4229%;width:15.8687%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
בנו אוטומט חזקה
והראו שהוא לא עובד
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-028.png" alt="" />
<div class="ppt-text-layer" style="left:8.7255%;top:5.3578%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לצורך אמיתי באוטומט לא דטרמיניסטי: הגדרת תכונה סבירה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
28
</div>
</div>
<div class="ppt-text-layer" style="left:0.0000%;top:62.2825%;width:96.6667%;height:28.6007%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
התרגום מהאוטומט בצד שמאל לאוטומט בצד ימין:
𝐴= 𝑏𝑙𝑖𝑛𝑘 , 𝐵={}
&quot;בסופו של דבר, 𝐵 יתקיים כל הזמן&quot; שקול לביטוי &quot;מספר סופי שלblink –ים&quot;
𝐴+𝐵 ∗ 𝐵 𝜔 = {}+ 𝑏𝑙𝑖𝑛𝑘 ∗ {} 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:18.1401%;top:23.4053%;width:5.1204%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:30.1944%;top:32.4227%;width:5.2480%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:17.8308%;top:47.4005%;width:5.2480%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:42.2018%;top:47.3103%;width:5.2480%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:59.3500%;top:24.0824%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:71.7364%;top:33.2982%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:82.8430%;top:23.9406%;width:10.4903%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑏𝑙𝑖𝑛𝑘
</div>
</div>
<div class="ppt-text-layer" style="left:56.4711%;top:46.3512%;width:38.8166%;height:5.9053%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
eventually always ¬𝑏𝑙𝑖𝑛𝑘
</div>
</div>
<div class="ppt-text-layer" style="left:65.7550%;top:52.1899%;width:16.5349%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
תכונת התמדה
</div>
</div>
<div class="ppt-text-layer" style="left:8.8175%;top:52.1899%;width:43.4620%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
אוטומט שאין לו אוטומט דטרמניסטי שקול
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-029.png" alt="" />
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
29
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-030.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומטי Büchi מוכללים
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
<div class="ppt-text-layer" style="left:0.3125%;top:20.0000%;width:98.3333%;height:71.1111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• קיימים סוגים שונים של אוטומטים לתיאור שפות של מילים אינסופיות:
  • אוטומטי Müller , Rabin ו-Street – עליהם לא נדבר בקורס
  • אנחנו נשתמש ב Generalized Büchi Automata (GNBA)
• GNBA הם כמו NBA רק שמרשים מספר קבוצות של מצבים מקבלים:
  • ב-GNBA דורשים לבקר כל אחת מהקבוצות 𝐹 1 ,…, 𝐹 𝑘 אינסוף פעמים
  • כאשר 𝑘=1 מקבלים NBA
• עם GNBA קל יותר לבנות את החיתוך (תנאי &quot;וגם&quot;) בין שתי שפות
  • בעלי יכולת תיאור זהה ל-NBA - לא מוסיפים כוח ביטוי, רק מבנה נתונים לחישוב
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-031.png" alt="" />
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-032.png" alt="" />
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-033.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
33
</div>
</div>
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.4684%;top:89.3014%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.5010%;top:59.5328%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6877%;top:85.5627%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:40.0597%;top:77.7579%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:93.3689%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.5792%;top:72.5512%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.1300%;top:92.4135%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:62.0534%;top:46.4557%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:17.2971%;top:65.8849%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:45.2530%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.1219%;top:58.6086%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.1326%;top:61.9346%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-034.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.4684%;top:89.3014%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.5010%;top:59.5328%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6877%;top:85.5627%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:40.0597%;top:77.7579%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:93.3689%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.5792%;top:72.5512%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.1326%;top:61.9346%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.1300%;top:92.4135%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:62.0534%;top:46.4557%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:17.2971%;top:65.8849%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:45.2530%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.1219%;top:58.6086%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-035.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.4684%;top:89.3014%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.5010%;top:59.5328%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6877%;top:85.5627%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:40.0597%;top:77.7579%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:93.3689%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.5792%;top:72.5512%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.1326%;top:61.9346%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.1300%;top:92.4135%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:62.0534%;top:46.4557%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:17.2971%;top:65.8849%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:45.2530%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.1219%;top:58.6086%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.6308%;top:46.2684%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:61.7082%;top:46.3045%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:34.9378%;top:71.8109%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:40.0152%;top:71.8470%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-036.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.4684%;top:89.3014%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.5010%;top:59.5328%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6877%;top:85.5627%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:40.0597%;top:77.7579%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:93.3689%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.5792%;top:72.5512%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.1326%;top:61.9346%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.1300%;top:92.4135%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:62.0534%;top:46.4557%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:17.2971%;top:65.8849%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:45.2530%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.1219%;top:58.6086%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.6308%;top:46.2684%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:61.7082%;top:46.3045%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:34.9378%;top:71.8109%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:40.0152%;top:71.8470%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:71.6376%;top:37.3949%;width:26.6312%;height:23.4577%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:right;direction:rtl;border:0.75px solid #353232;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם נבחר את ⟨ 𝑞 1 , 𝑞 2 ⟩ להיות מקבל. תתקבל המילה 𝑏 𝜔 שאינה בשפת החיתוך בין האוטומטים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-037.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.4684%;top:89.3014%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.5010%;top:59.5328%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6877%;top:85.5627%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:40.0597%;top:77.7579%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:93.3689%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.5792%;top:72.5512%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.1326%;top:61.9346%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.1300%;top:92.4135%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:62.0534%;top:46.4557%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:17.3172%;top:66.3879%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:45.2530%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.1219%;top:58.6086%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.6308%;top:46.2684%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:61.7082%;top:46.3045%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:34.9378%;top:71.8109%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:40.0152%;top:71.8470%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:-0.3789%;top:42.8376%;width:26.6312%;height:23.4577%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:right;direction:rtl;border:0.75px solid #353232;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם נבחר את ⟨ 𝑞 2 , 𝑞 1 ⟩להיות מקבל. תתקבל המילה 𝑎 𝜔 שאינה בשפת החיתוך בין האוטומטים
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-038.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
מוטיבציה: אוטומט לחיתוך שפות
בעיה עם אוטומטי מַכְפֵּלָה
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
<div class="ppt-text-layer" style="left:17.9249%;top:26.4683%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:29.6011%;top:27.2866%;width:5.8143%;height:7.2522%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #ff0000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:13.9542%;top:20.4703%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:24.7786%;top:18.0478%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:37.6080%;top:22.8672%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:25.5923%;top:37.5794%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
¬𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:5.8285%;top:26.5608%;width:6.1175%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝒜 1
</div>
</div>
<div class="ppt-text-layer" style="left:61.2821%;top:26.7756%;width:6.6667%;height:8.8889%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:73.0034%;top:27.6835%;width:5.7362%;height:7.1548%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #0000ff;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:57.2115%;top:20.5422%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.0359%;top:18.1197%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:80.8654%;top:22.9391%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:68.8497%;top:37.6513%;width:2.7208%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:84.6110%;top:27.6835%;width:6.1757%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:71.0953%;top:37.3949%;width:27.1736%;height:26.2729%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:right;direction:rtl;border:0.75px solid #353232;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אם נבחר את ⟨ 𝑞 1 , 𝑞 2 ⟩ואת ⟨ 𝑞 2 , 𝑞 1 ⟩ לא מקבלים. לא תתקבל המילה ( 𝑎 𝑏 ) 𝜔 שבשפת החיתוך בין אוטומטים
</div>
</div>
<div class="ppt-text-layer" style="left:6.9224%;top:50.9596%;width:12.4419%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝒜 1 × 𝒜 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:53.4204%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 1, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:32.8934%;top:79.8491%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6267%;top:80.0125%;width:7.9748%;height:10.3765%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#ffffff;opacity:1.000;border:1.50px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝑞 2, 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:43.7839%;top:54.2974%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.4684%;top:89.3014%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:49.8224%;top:78.6272%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:22.5835%;top:47.8580%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.5010%;top:59.5328%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:27.9818%;top:73.3076%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6877%;top:85.5627%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:40.0597%;top:77.7579%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:93.3689%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:59.5792%;top:72.5512%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.1326%;top:61.9346%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.1300%;top:92.4135%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:62.0534%;top:46.4557%;width:11.4394%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:17.2971%;top:65.8849%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:43.6728%;top:45.2530%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:38.1219%;top:58.6086%;width:14.0353%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
¬𝑎∧¬𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.6308%;top:46.2684%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:61.7082%;top:46.3045%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:34.9378%;top:71.8109%;width:2.8945%;height:1.8587%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(10.51deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מקבל
</div>
</div>
<div class="ppt-text-layer" style="left:40.0152%;top:71.8470%;width:2.9822%;height:1.7510%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:rtl;background:#fbca03;opacity:1.000;transform:rotate(349.49deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:6.00pt;line-height:1.15;font-weight:700;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
לא מקבל
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-039.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: אוטומט Büchi מוכללים
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
<div class="ppt-text-layer" style="left:0.0000%;top:21.1111%;width:95.0000%;height:73.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
אוטומט Büchi מוכלל (GNBA) הוא חמישייה 𝒢=〈𝑄,Σ,𝛿, 𝑄 0 ,ℱ〉
• 𝑄 קבוצה סופית של מצבים המכילה קבוצת מצבים התחלתיים 𝑄0
• Σ הוא האלפבית
• 𝛿: 𝑄×Σ→ 2 𝑄 היא פונקצית המעברים
• ℱ={ 𝐹 0 ,…, 𝐹 𝑘−1 } הן תת-קבוצות של 𝑄 המייצגות את תנאי הקבלה
</div>
</div>
<div class="ppt-text-layer" style="left:12.5000%;top:44.9285%;width:25.8333%;height:6.7111%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ddc49e;opacity:1.000;border:0.75px solid #b0925c;border-radius:16px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#644646;white-space:pre-wrap;width:100%;">
ה-&quot;צבעים&quot; השונים
</div>
</div>
<div class="ppt-text-layer" style="left:75.6317%;top:79.0056%;width:4.1049%;height:5.4987%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:59.7672%;top:79.0056%;width:4.1144%;height:5.4987%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:91.4866%;top:79.0056%;width:4.1144%;height:5.4987%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:82.9437%;top:75.4908%;width:6.6224%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖 𝑡 2
</div>
</div>
<div class="ppt-text-layer" style="left:82.7098%;top:83.3335%;width:6.3054%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:74.4932%;top:87.0303%;width:6.3054%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:66.7617%;top:83.7751%;width:6.5768%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖 𝑡 1
</div>
</div>
<div class="ppt-text-layer" style="left:66.9807%;top:75.4046%;width:6.3054%;height:4.4879%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:2.2934%;top:66.5069%;width:51.4742%;height:27.9219%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
𝑄= 𝑞 0 , 𝑞 1 , 𝑞 2
Σ= 2 𝑐𝑟𝑖 𝑡 1 ,𝑐𝑟𝑖 𝑡 2 = {}, 𝑐𝑟𝑖 𝑡 1 , 𝑐𝑟𝑖 𝑡 2 , 𝑐𝑟𝑖 𝑡 1 ,𝑐𝑟𝑖 𝑡 2
𝛿 𝑞,A = 𝑞 0 ∪ 𝑞 1 if 𝑞= 𝑞 0 and 𝑐𝑟𝑖 𝑡 1 ∈𝐴 𝑞 2 if 𝑞= 𝑞 0 and 𝑐𝑟𝑖 𝑡 2 ∈𝐴 ∅ otherwise
ℱ={ 𝑞 1 ,{ 𝑞 2 }}
</div>
</div>
<div class="ppt-text-layer" style="left:85.2045%;top:65.5455%;width:12.2224%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
דוגמה:
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-040.png" alt="" />
<div class="ppt-text-layer" style="left:10.5208%;top:23.3333%;width:78.9583%;height:34.4444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מילים אינסופית &quot;המבקרות&quot; אינסוף פעמים
בכל אחת מהקבוצות המקבלות
</div>
</div>
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
שפה של GNBA
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
<div class="ppt-text-layer" style="left:45.5460%;top:65.5556%;width:47.0060%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
ריצה 𝑞 0 , 𝑞 1 , 𝑞 2 ,… היא מקבלת אם:
</div>
</div>
<div class="ppt-text-layer" style="left:25.0000%;top:74.4444%;width:36.7772%;height:18.7667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝐹∈ ℱ ( ∃ ∞ 𝑗 . 𝑞 𝑗 ∈𝐹 )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-041.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: שפה של GNBA
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
<div class="ppt-text-layer" style="left:1.6667%;top:15.5556%;width:95.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• עבור אוטומט מוכלל 𝒢=〈𝑄,Σ,𝛿, 𝑄 0 ,ℱ〉 ומילה 𝑤= 𝐴 1 𝐴 2 ⋯∈ Σ 𝜔
• ריצה של 𝑤 ב 𝒢 היא רצף מצבים 𝑞0 𝑞1 …∈ 𝑄 𝜔 אינסופי כך ש:
𝑞 0 ∈ 𝑄 0 ו- 𝑞 𝑖 𝐴 𝑖+1 𝑞 𝑖+1 לכל 𝑖≥0
• ריצה 𝑞0 𝑞1…מקבלת אם, לכל 𝐹∈ℱ, 𝑞𝑖∈𝐹 עבור אינסוף 𝑖-ים
• מילה 𝑤∈ Σ 𝜔 מתקבלת ע&quot;י 𝒢 אם יש ריצה מקבלת של 𝑤 ב 𝒢
• השפה המתקבלת ע&quot;י 𝒢 :
ℒ 𝜔 𝒢 = 𝑤∈ Σ 𝜔 :𝒢 ב 𝑤 יש ריצה מקבלת של
• 𝒢 ו 𝒢 ′ הם שקולים אם ℒ 𝜔 𝒢 = ℒ 𝜔 ( 𝒢 ′ )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-042.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
הגדרה: שפה של GNBA
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
<div class="ppt-text-layer" style="left:1.6667%;top:15.5556%;width:95.0000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• עבור אוטומט מוכלל 𝒢=〈𝑄,Σ,𝛿, 𝑄 0 ,ℱ〉 ומילה 𝑤= 𝐴 1 𝐴 2 ⋯∈ Σ 𝜔
• ריצה של 𝑤 ב 𝒢 היא רצף מצבים 𝑞0 𝑞1 …∈ 𝑄 𝜔 אינסופי כך ש:
𝑞 0 ∈ 𝑄 0 ו- 𝑞 𝑖 𝐴 𝑖+1 𝑞 𝑖+1 לכל 𝑖≥0
• ריצה 𝑞0 𝑞1…מקבלת אם, לכל 𝐹∈ℱ, 𝑞𝑖∈𝐹 עבור אינסוף 𝑖-ים
• מילה 𝑤∈ Σ 𝜔 מתקבלת ע&quot;י 𝒢 אם יש ריצה מקבלת של 𝑤 ב 𝒢
• השפה המתקבלת ע&quot;י 𝒢 :
ℒ 𝜔 𝒢 = 𝑤∈ Σ 𝜔 :𝒢 ב w יש ריצה מקבלת של
• 𝒢 ו 𝒢 ′ הם שקולים אם ℒ 𝜔 𝒢 = ℒ 𝜔 ( 𝒢 ′ )
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-043.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-3.9985%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
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
43
</div>
</div>
<div class="ppt-text-layer" style="left:0.1851%;top:77.6767%;width:98.9816%;height:16.7677%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:22.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
GNBA עבור הדרישה &quot;כל אחד מהתהליכים מבקר בקטע הקריטי אינסוף פעמים&quot;
ℱ= 𝑞 1 , 𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:17.6851%;top:31.0101%;width:67.3310%;height:9.6797%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#222222;white-space:pre-wrap;width:100%;">
𝐴 0 𝐴 1 ⋅⋅⋅ : ∃ ∞ 𝑖 . 𝑐𝑟𝑖 𝑡 1 ∈ 𝐴 𝑖 ∧ ∃ ∞ 𝑖 . 𝑐𝑟𝑖 𝑡 2 ∈ 𝐴 𝑖
</div>
</div>
<div class="ppt-text-layer" style="left:11.8249%;top:19.3120%;width:79.0513%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
alwyas eventually 𝑐𝑟𝑖 𝑡 1 ∧ always eventually 𝑐𝑟𝑖 𝑡 2
</div>
</div>
<div class="ppt-text-layer" style="left:47.6736%;top:51.8056%;width:7.4479%;height:9.9769%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0
</div>
</div>
<div class="ppt-text-layer" style="left:18.8889%;top:51.8056%;width:7.4653%;height:9.9769%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1
</div>
</div>
<div class="ppt-text-layer" style="left:76.4410%;top:51.8056%;width:7.4653%;height:9.9769%;padding:0.00pt 0.00pt 7.20pt 0.00pt;justify-content:center;text-align:right;direction:ltr;background:#fffacc;opacity:1.000;border:0.00px solid #fffacc;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 2
</div>
</div>
<div class="ppt-text-layer" style="left:62.9338%;top:46.8707%;width:7.9519%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖 𝑡 2
</div>
</div>
<div class="ppt-text-layer" style="left:62.6508%;top:61.3195%;width:7.5270%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:47.4557%;top:67.5691%;width:7.5270%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:32.1262%;top:61.4377%;width:7.8937%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑐𝑟𝑖 𝑡 1
</div>
</div>
<div class="ppt-text-layer" style="left:32.8514%;top:46.9526%;width:7.5270%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-044.png" alt="" />
<div class="ppt-text-layer" style="left:4.1667%;top:2.2763%;width:89.7959%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
בנייה: אוטומט Büchi מוכלל לחיתוך בין שפות של אוטומטי Büchi מוכללים
</div>
</div>
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
<div class="ppt-text-layer" style="left:4.1667%;top:22.2222%;width:86.0525%;height:67.1681%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור האוטומטים 𝒢 1 =〈 𝑄 1 ,Σ, 𝛿 1 , 𝑄 01 , ℱ 1 〉 ו 𝒢 2 =〈 𝑄 2 ,Σ, 𝛿 2 , 𝑄 02 , ℱ 2 〉
נגדיר:
𝒢= 𝒢 1 × 𝒢 2 =〈 𝑄 1 × 𝑄 2 ,Σ,𝛿, 𝑄 01 × 𝑄 02 ,ℱ〉
באשר יחס המעברים 𝛿מוגדר ע&quot;י כלל ההיסק:
ותנאי הקבלה מוגדר ע&quot;י:
</div>
</div>
<div class="ppt-text-layer" style="left:20.6511%;top:42.0706%;width:19.0769%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
אוטומט המכפלה
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-045.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
דוגמה לחיתוך
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
<div class="ppt-text-layer" style="left:12.6142%;top:36.6667%;width:14.4663%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אינסוף A-ים
</div>
</div>
<div class="ppt-text-layer" style="left:73.6228%;top:36.6667%;width:14.2910%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
אינסוף B-ים
</div>
</div>
<div class="ppt-text-layer" style="left:16.9518%;top:91.5111%;width:22.2149%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
GNBA עבור החיתוך
</div>
</div>
<div class="ppt-text-layer" style="left:62.7207%;top:91.8667%;width:20.4793%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
NBA עבור החיתוך
</div>
</div>
<div class="ppt-text-layer" style="left:55.0000%;top:53.3333%;width:10.8333%;height:14.4444%;padding:3.60pt 0.00pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:6.00px solid #4f4b4b;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0 , 𝑞 2 ,1
</div>
</div>
<div class="ppt-text-layer" style="left:77.7833%;top:53.3333%;width:10.8333%;height:14.4444%;padding:3.60pt 0.00pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.75px solid #4f4b4b;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 , 𝑞 3 ,1
</div>
</div>
<div class="ppt-text-layer" style="left:55.0000%;top:74.4444%;width:10.8333%;height:14.4444%;padding:3.60pt 0.00pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.75px solid #4f4b4b;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 0 , 𝑞 2 ,2
</div>
</div>
<div class="ppt-text-layer" style="left:77.7833%;top:74.4444%;width:10.8333%;height:14.4444%;padding:3.60pt 0.00pt 3.60pt 0.00pt;justify-content:center;text-align:left;direction:ltr;background:#fffacc;opacity:1.000;border:0.75px solid #4f4b4b;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑞 1 , 𝑞 3 ,2
</div>
</div>
<div class="ppt-text-layer" style="left:70.6301%;top:55.5556%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:91.4634%;top:52.2222%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:56.4294%;top:67.9479%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:73.1301%;top:64.4444%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:68.3239%;top:72.3924%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:49.1667%;top:83.5035%;width:4.4367%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐵
</div>
</div>
<div class="ppt-text-layer" style="left:69.9906%;top:81.1111%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:83.9634%;top:67.9479%;width:2.7032%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-046.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
מ-GNBA ל-NBA
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
<div class="ppt-text-layer" style="left:12.5000%;top:22.8520%;width:75.0000%;height:54.0741%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
משפט: עבור כל GNBA 𝒢 קיים NBA 𝒜 כך ש-
ℒ 𝜔 𝒢 = ℒ 𝜔 𝒜
𝒜 =𝒪 𝒢 ⋅ ℱ
באשר ℱ היא קבוצת הקבוצות המקבלות ב-𝒢
</div>
</div>
<div class="ppt-text-layer" style="left:13.3333%;top:85.6298%;width:78.3333%;height:7.6293%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#743c29;opacity:1.000;border:0.75px solid #a65a40;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
מסקנה: GNBA ו NBA בעלי אותה יכולת ביטוי
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-047.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.0531%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
לֶמָה מרכזית בהוכחה
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
<div class="ppt-text-layer" style="left:9.4792%;top:62.2222%;width:79.7980%;height:33.4426%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור ריצה 𝑞 0 𝑞 1 …∈ 𝑄 𝜔 וקבוצה ℱ= 𝐹 0 ,…, 𝐹 𝑛−1 ⊆ 2 𝑄 :
לכל 𝐹∈ℱ מתקיים ∃ ∞ 𝑖 . 𝑞 𝑖 ∈𝐹
אם ורק אם
קיימים 𝑖 0 &lt; 𝑖 1 &lt; ⋅⋅⋅ כך ש- 𝑞 𝑖 𝑗 ∈ 𝐹 𝑗 mod 𝑛
</div>
</div>
<div class="ppt-text-layer" style="left:10.0457%;top:16.0836%;width:79.9495%;height:14.3611%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
כל איברי קבוצה 𝑎 1 ,…, 𝑎 𝑛 מופיעים לעיתים תכופות בסדרה אינסופית
אם ורק אם
הסדרה היא מהצורה Σ ∗ 𝑎 1 Σ ∗ 𝑎 2 Σ ∗ … Σ ∗ 𝑎 𝑛 𝜔
</div>
</div>
<div class="ppt-text-layer" style="left:53.1154%;top:42.0271%;width:33.4674%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
Σ ∗ Σ ∗ Σ ∗ Σ ∗ 𝜔
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-048.png" alt="" />
<div class="ppt-text-layer" style="left:9.1667%;top:-4.0531%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
חידה?
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
<div class="ppt-text-layer" style="left:1.6667%;top:18.6030%;width:97.5000%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
• נתונות לנו 10 פרוצדורות, אחת לכל ספרה, כל אחת מהן קוראת ספרות מהקלט וחוזרת אלינו כשהיא מוצאת את הסיפרה שהיא מכירה.
• יש לנו גם פרוצדורה הגורמת להבהוב נורה.
• המשימה שלנו היא לכתוב פרוצדורה שמהבהבת את הנורה אינסוף פעמים אם ורק אם יש בקלט אינסוף מכל אחת מהספרות.
• כלומר, אם ורק אם אין ספרה שמופיעה רק מספר סופי של פעמים.
• איך נממש את הפרוצדורה הזו?
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-049.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:3.3333%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:36.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תרגום אוטומט GNBA לאוטומט NBA
רעיון הבנייה
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
<div class="ppt-text-layer" style="left:13.3333%;top:35.5556%;width:8.3333%;height:10.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝐹0
</div>
</div>
<div class="ppt-text-layer" style="left:45.8333%;top:26.6667%;width:8.3333%;height:10.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝐹1
</div>
</div>
<div class="ppt-text-layer" style="left:83.7791%;top:32.8695%;width:8.5066%;height:10.0000%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
𝐹𝑘−1
</div>
</div>
<div class="ppt-text-layer" style="left:18.3333%;top:25.5556%;width:8.3333%;height:7.7778%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;border:3.00px solid #ffffff;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ffffff;white-space:pre-wrap;width:100%;">
𝑄0
</div>
</div>
<div class="ppt-text-layer" style="left:63.5745%;top:31.2500%;width:5.8237%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:24.00pt;line-height:1.15;font-weight:700;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
⋯
</div>
</div>
<div class="ppt-text-layer" style="left:1.4873%;top:60.2411%;width:97.5000%;height:12.1172%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
בונים 𝑘 עותקים של ה-GNBA ועוברים מהעותק ה-𝑖 לעותק ה-(𝑖+1) ביציאה מ- 𝐹 𝑖 .
המצבים המקבלים ב-NBA הם 𝐹 1 בעותק הראשון. ההתחלתיים הם 𝑄 0 בעותק הראשון.
</div>
</div>
<div class="ppt-text-layer" style="left:3.2631%;top:78.1432%;width:94.0576%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;background:#c6b7b8;opacity:1.000;border:0.75px solid #948182;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מבקרים בכל 𝐹 𝑖 אינסוף פעמים⇔ מבקרים ב- 𝐹 0 אח&quot;כ ב- 𝐹 1 עד 𝐹 𝑘−1 ושוב ב- 𝐹 0 וחוזר חלילה
</div>
</div>
<div class="ppt-text-layer" style="left:19.1667%;top:87.5026%;width:42.5000%;height:9.4245%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
ייתכן שבין הביקורים האלה ב- 𝐹 0 וב- 𝐹 1 נבקר גם בקבוצות אחרות
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-050.png" alt="" />
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
50
</div>
</div>
<div class="ppt-text-layer" style="left:19.6000%;top:85.5556%;width:57.1885%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
מהי השפה של הGNBA- הזה? איך נמיר אותו ל-NBA ?
</div>
</div>
<div class="ppt-text-layer" style="left:18.3333%;top:91.8115%;width:63.5297%;height:5.9053%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
eventually 𝑏∧next 𝑏 ∧eventually always 𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-051.png" alt="" />
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
51
</div>
</div>
<div class="ppt-text-layer" style="left:30.0000%;top:58.8889%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:10.5707%;width:4.5751%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:38.1411%;top:25.8090%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:45.8333%;top:26.6667%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:37.6438%;top:45.7895%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:32.1740%;top:35.3996%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:21.9165%;top:50.6896%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:18.2509%;top:35.3996%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:11.2894%;top:26.6082%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.7921%;top:40.9942%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:3.8306%;top:25.0098%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:69.2180%;top:41.4620%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:60.0000%;top:35.5556%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.1411%;top:50.2534%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:90.8333%;top:51.1111%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:77.1740%;top:59.8440%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.8123%;top:75.0000%;width:8.2198%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.2509%;top:59.8440%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.2894%;top:51.0526%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:55.7921%;top:65.4386%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:48.5181%;top:49.1764%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:75.0000%;top:83.3333%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:23.1040%;top:15.8768%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:82.6438%;top:70.2339%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:0.1407%;top:90.9401%;width:96.2468%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
שכפלנו, צבענו מצבים מקבלים מתאימים בכל עותק, השארנו רק מצבי ההתחלה בעותק הראשון
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-052.png" alt="" />
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
52
</div>
</div>
<div class="ppt-text-layer" style="left:23.1040%;top:15.8768%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:10.5707%;width:4.5751%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:18.2509%;top:35.3996%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:11.2894%;top:26.6082%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.7921%;top:40.9942%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:3.8306%;top:25.0098%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:69.2180%;top:41.4620%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:60.0000%;top:35.5556%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.1411%;top:50.2534%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:90.8333%;top:51.1111%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:82.6438%;top:70.2339%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:77.1740%;top:59.8441%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:66.8123%;top:75.0000%;width:8.2198%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.2509%;top:59.8441%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.2894%;top:51.0526%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:55.7921%;top:65.4386%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:48.5181%;top:49.1764%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.2179%;top:79.2105%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:38.1392%;top:78.4242%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.5957%;top:88.5694%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:9.2569%;top:77.4390%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:75.8637%;top:10.6898%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.2550%;top:20.7077%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:41.8230%;top:66.0446%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-053.png" alt="" />
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
53
</div>
</div>
<div class="ppt-text-layer" style="left:23.1040%;top:15.8768%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:10.5707%;width:4.5751%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:18.2509%;top:35.3996%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:11.2894%;top:26.6082%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.7921%;top:40.9942%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:3.8306%;top:25.0098%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:69.2180%;top:41.4620%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:60.0000%;top:35.5556%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.1411%;top:50.2534%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:90.8333%;top:51.1111%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:82.6438%;top:70.2339%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:77.1740%;top:59.8441%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.2509%;top:59.8441%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.2894%;top:51.0526%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.2179%;top:79.2105%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:38.1392%;top:78.4242%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.5957%;top:88.5694%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:9.2569%;top:77.4390%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:75.8637%;top:10.6898%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:31.9147%;top:35.3900%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:27.6889%;top:43.7475%;width:8.2198%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:47.3361%;top:75.7315%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:50.4983%;top:65.6242%;width:8.2198%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-054.png" alt="" />
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
54
</div>
</div>
<div class="ppt-text-layer" style="left:23.1040%;top:15.8768%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:15.8333%;top:10.5707%;width:4.5751%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:18.2509%;top:35.3996%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:11.2894%;top:26.6082%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:10.7921%;top:40.9942%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:3.8306%;top:25.0098%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:69.2180%;top:41.4620%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:60.0000%;top:35.5556%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:83.1411%;top:50.2534%;width:2.4725%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:90.8333%;top:51.1111%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:82.6438%;top:70.2339%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:77.1740%;top:59.8441%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:63.2509%;top:59.8441%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:56.2894%;top:51.0526%;width:2.4972%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:80.2179%;top:79.2105%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:38.1392%;top:78.4242%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:46.5957%;top:88.5694%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:9.2569%;top:77.4390%;width:4.9048%;height:3.8737%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:75.8637%;top:10.6898%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:31.9147%;top:35.3900%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:27.6889%;top:43.7475%;width:8.2198%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:47.3361%;top:75.7315%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:50.4983%;top:65.6242%;width:8.2198%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎∧𝑏
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-055.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
אפשרות אחרת
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
55
</div>
</div>
<div class="ppt-text-layer" style="left:19.6129%;top:31.9567%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:50.4553%;top:40.6428%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:58.4145%;top:31.8492%;width:7.6672%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑡𝑟𝑢𝑒
</div>
</div>
<div class="ppt-text-layer" style="left:31.0683%;top:40.6428%;width:4.1435%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑏
</div>
</div>
<div class="ppt-text-layer" style="left:69.8423%;top:40.6428%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:79.5565%;top:31.3870%;width:4.1849%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:20.1627%;top:69.5354%;width:62.2303%;height:5.9053%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
eventually 𝑏∧next 𝑏 ∧eventually always 𝑎
</div>
</div>
<div class="ppt-text-layer" style="left:6.4010%;top:86.3318%;width:11.7841%;height:6.7318%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:12.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
הוכיחו שזאת
שפת האוטומט
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-056.png" alt="" />
<div class="ppt-text-layer" style="left:8.3333%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
תיאור מתמטי של הבניה
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
<div class="ppt-text-layer" style="left:4.1667%;top:20.0000%;width:90.0000%;height:73.3333%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
נניח ℱ={ 𝐹 1 , 𝐹 2 ,…, 𝐹 𝑘 } עבור 𝑘&gt;1 ונגדיר את 𝒜 :
• 𝑄 𝒜 = 𝑄 𝒢 ×{1,2,…,𝑘}
• 𝑄 0𝒜 = Q 0𝒢 × 1
• 𝑠,𝑖 ,𝑎, 𝑠 ′ ,𝑗 ∈ 𝛿 𝒜 iff 𝑠,𝑎, 𝑠 ′ ∈ 𝛿 𝒢 and
𝑠∉ 𝐹 𝑖 ∧𝑗=𝑖 ∨ 𝑠∈ 𝐹 𝑖 ∧ 𝑗= 𝑖 mod 𝑘 +1
• 𝐹 𝒜 = 𝐹 1 × 1
</div>
</div>
<div class="ppt-text-layer" style="left:69.1667%;top:30.6189%;width:24.2262%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9b2d1f;white-space:pre-wrap;width:100%;">
𝑘 עותקים של האוטומט
</div>
</div>
<div class="ppt-text-layer" style="left:60.2679%;top:40.8749%;width:33.8988%;height:5.3751%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9b2d1f;white-space:pre-wrap;width:100%;">
מתחילים ב 𝑄 0 של העותק הראשון
</div>
</div>
<div class="ppt-text-layer" style="left:50.5357%;top:86.7503%;width:43.6309%;height:4.9366%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#9b2d1f;white-space:pre-wrap;width:100%;">
עוברים אינסוף פעמים ב 𝐹 1 של העותק הראשון
</div>
</div>
<div class="ppt-text-layer" style="left:74.4345%;top:70.3893%;width:19.7321%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ff0000;white-space:pre-wrap;width:100%;">
כשמגיעים ל 𝐹 𝑖
עוברים לעותק הבא
</div>
</div>
<div class="ppt-text-layer" style="left:4.1667%;top:70.0000%;width:24.1667%;height:8.5269%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#0000ff;white-space:pre-wrap;width:100%;">
כל עוד לא הגענו ל 𝐹 𝑖
ממשיכים באותו העותק
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-057.png" alt="" />
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
57
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-058.png" alt="" />
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
58
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-059.png" alt="" />
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
59
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-060.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
חיתוך
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
60
</div>
</div>
<div class="ppt-text-layer" style="left:12.5000%;top:16.6667%;width:75.6944%;height:72.2222%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:center;direction:rtl;background:#ffffff;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:28.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
עבור אוטומטי GNBA G1 ו G2
קיים אוטומט GNBA G
כך ש:
L!(G) = L!(G1) Å L!(G2)
jGj = O(jG1j⋅jG2j)
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-061.png" alt="" />
<div class="ppt-text-layer" style="left:56.6319%;top:53.9352%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
q
</div>
</div>
<div class="ppt-text-layer" style="left:57.6042%;top:55.0926%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6285%;top:53.9352%;width:1.8403%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
;
</div>
</div>
<div class="ppt-text-layer" style="left:59.6181%;top:53.9352%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
r
</div>
</div>
<div class="ppt-text-layer" style="left:60.6250%;top:55.0926%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:78.4549%;top:53.9352%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
q
</div>
</div>
<div class="ppt-text-layer" style="left:79.4444%;top:55.0926%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:80.4688%;top:53.9352%;width:1.8403%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
;
</div>
</div>
<div class="ppt-text-layer" style="left:81.4583%;top:53.9352%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
r
</div>
</div>
<div class="ppt-text-layer" style="left:82.4653%;top:55.0926%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:78.4549%;top:83.0787%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
q
</div>
</div>
<div class="ppt-text-layer" style="left:79.4444%;top:84.2361%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:80.4688%;top:83.0787%;width:1.8403%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
;
</div>
</div>
<div class="ppt-text-layer" style="left:81.4583%;top:83.0787%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
r
</div>
</div>
<div class="ppt-text-layer" style="left:82.4653%;top:84.2361%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:56.6319%;top:83.1713%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
q
</div>
</div>
<div class="ppt-text-layer" style="left:57.6042%;top:84.3287%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
1
</div>
</div>
<div class="ppt-text-layer" style="left:58.6285%;top:83.1713%;width:1.8403%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
;
</div>
</div>
<div class="ppt-text-layer" style="left:59.6181%;top:83.1713%;width:2.2396%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
r
</div>
</div>
<div class="ppt-text-layer" style="left:60.6250%;top:84.3287%;width:1.8576%;height:2.7778%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmr7','Segoe UI','Arial',sans-serif;font-size:11.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
2
</div>
</div>
<div class="ppt-text-layer" style="left:73.2292%;top:65.2083%;width:2.9514%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
A
</div>
</div>
<div class="ppt-text-layer" style="left:65.1736%;top:72.3611%;width:2.9514%;height:3.9120%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:flex-start;text-align:left;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'cmmi10','Segoe UI','Arial',sans-serif;font-size:16.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
A
</div>
</div>
<div class="ppt-text-layer" style="left:1.8173%;top:-5.7137%;width:96.6667%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:32.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
עוד דוגמה
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Perpetua','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Franklin Gothic Book','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
61
</div>
</div>
<div class="ppt-text-layer" style="left:13.8240%;top:51.9639%;width:7.3387%;height:10.0688%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:4.50px solid #000000;border-radius:9999px;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 1 , 𝑟 1
</div>
</div>
<div class="ppt-text-layer" style="left:26.1453%;top:65.1650%;width:7.3387%;height:10.0688%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:1.50px solid #000000;border-radius:9999px;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#ff0000;white-space:pre-wrap;width:100%;">
𝑞 2 , 𝑟 2
</div>
</div>
<div class="ppt-text-layer" style="left:23.5354%;top:59.3538%;width:2.9404%;height:3.7540%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:5.2154%;top:65.9847%;width:7.3387%;height:10.0688%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:1.50px solid #000000;border-radius:9999px;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 1 , 𝑟 1
</div>
</div>
<div class="ppt-text-layer" style="left:21.0907%;top:68.1376%;width:2.9404%;height:3.7540%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:14.3898%;top:73.7257%;width:2.9404%;height:3.7540%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:14.6577%;top:66.8746%;width:2.9404%;height:3.7540%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:8.5423%;top:91.4968%;width:20.4793%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
NBA עבור החיתוך
</div>
</div>
<div class="ppt-text-layer" style="left:56.4506%;top:92.4119%;width:22.2149%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#000000;white-space:pre-wrap;width:100%;">
GNBA עבור החיתוך
</div>
</div>
<div class="ppt-text-layer" style="left:51.8588%;top:31.8761%;width:5.7501%;height:7.5716%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟 2
</div>
</div>
<div class="ppt-text-layer" style="left:52.2110%;top:19.4384%;width:5.0385%;height:6.6345%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#fffacc;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟 1
</div>
</div>
<div class="ppt-text-layer" style="left:52.2152%;top:32.4089%;width:5.0385%;height:6.6345%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:center;direction:ltr;background:#fffacc;opacity:1.000;border:0.75px solid #000000;border-radius:9999px;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝑟 2
</div>
</div>
<div class="ppt-text-layer" style="left:58.4334%;top:26.0711%;width:2.6506%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:47.5000%;top:26.7363%;width:2.6506%;height:5.8342%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:20.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
𝐴
</div>
</div>
<div class="ppt-text-layer" style="left:43.5277%;top:23.8917%;width:2.5805%;height:5.3854%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:ltr;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#000000;white-space:pre-wrap;width:100%;">
×
</div>
</div>
<div class="ppt-text-layer" style="left:17.2528%;top:79.4402%;width:7.3387%;height:10.0688%;padding:0.00pt 0.00pt 0.00pt 7.20pt;justify-content:center;text-align:center;direction:ltr;border:1.50px solid #000000;border-radius:9999px;transform:rotate(38.78deg);transform-origin:center;">
<div class="ppt-text-inner" style="font-family:'Cambria Math','Segoe UI','Arial',sans-serif;font-size:18.00pt;line-height:1.15;font-weight:400;font-style:italic;color:#0000ff;white-space:pre-wrap;width:100%;">
𝑞 2 , 𝑟 2
</div>
</div>
</div>

---

<div class="ppt-slide-canvas">
<img class="ppt-slide-bg" src="/slide-backgrounds/20-deterministic-and-generalized-buchi-automata/slide-062.png" alt="" />
<div class="ppt-text-layer" style="left:10.0000%;top:-1.1111%;width:85.0000%;height:16.6667%;padding:3.60pt 7.20pt 7.20pt 7.20pt;justify-content:center;text-align:center;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:40.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
סיכום עובדות לגבי אוטומטי Büchi
</div>
</div>
<div class="ppt-text-layer" style="left:72.9167%;top:100.0000%;width:27.0833%;height:6.9444%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:center;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#696464;white-space:pre-wrap;width:100%;">
13 מרץ 26
</div>
</div>
<div class="ppt-text-layer" style="left:1.6667%;top:2.2222%;width:5.0000%;height:6.6667%;padding:0.00pt 0.00pt 0.00pt 0.00pt;justify-content:center;text-align:center;direction:ltr;background:#d34817;opacity:1.000;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:14.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#ffffff;white-space:pre-wrap;width:100%;">
62
</div>
</div>
<div class="ppt-text-layer" style="left:3.3333%;top:24.1176%;width:94.4444%;height:66.6667%;padding:3.60pt 7.20pt 3.60pt 7.20pt;justify-content:flex-start;text-align:right;direction:rtl;">
<div class="ppt-text-inner" style="font-family:'Gisha','Segoe UI','Arial',sans-serif;font-size:26.00pt;line-height:1.15;font-weight:400;font-style:normal;color:#222222;white-space:pre-wrap;width:100%;">
• בעלי יכולת ביטוי כמו ביטויים 𝜔-רגולריים = שפות 𝜔-רגולריות
• סגורים תחת הפעולות: איחוד, השלמה, חיתוך
• אוטומטי Büchi לא דטרמיניסטים יכולים לבטא יותר מאשר אוטומטי Büchi דטרמיניסטים
• בדיקת רֵיקוּת = בדיקה אם קיים מצב נגיש מקבל שניתן לחזרה
  • אפשר לחשב בזמן 𝒪(|𝒜|)
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
