---
theme: academic
dir: rtl
class: text-center
highlighter: shiki
lineNumbers: true
download: true
exportFilename: 04-channel-systems
htmlAttrs:
  dir: rtl
  lang: heb
drawings:
  enabled: true
info: |
  ## מערכות ערוצים (Channel Systems)
  מרצה: גרא וייס
---

# מערכות ערוצים <br> (Channel Systems)
## הרצאה בקורס מבוא לאימות תוכנה <br> בשיטות פורמאליות
הפקולטה למדעי המחשב והמידע | אוניברסיטת בן-גוריון

**גרא וייס**

<img src="/bgu-logo.png" class="bgu-logo" style="position: absolute; bottom: 20px; left: 450px; width: 80px; z-index: 100;" />

---

# מערכות ערוצים (Channel Systems)

מערכת מקבילית שבה תהליכים מתקשרים דרך **ערוצים (Channels)** — חוצצים מסוג FIFO שמכילים הודעות.

- מערכות ערוצים הן **סגורות**: תהליכים מתקשרים רק עם תהליכים אחרים במערכת, לא עם העולם החיצוני.
- מהוות את הבסיס לשפת **Promela** — שפת הקלט של מאמת המודלים **SPIN**.

<div class="mt-4">

**פעולות תקשורת (Communication Actions):**

$$Comm = \{c!v,\ c?x \mid c \in Chan,\ v \in dom(c),\ x \in Var \text{ with } dom(x) \supseteq dom(c)\}$$

</div>

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="bg-blue-50 p-3 rounded border border-blue-200">

**שליחה: $c!v$**  
שולח את הערך $v$ לסוף החוצץ של ערוץ $c$.

</div>
<div class="bg-green-50 p-3 rounded border border-green-200">

**קבלה: $c?x$**  
קורא הודעה מראש החוצץ של ערוץ $c$ <br>
ושם אותה במשתנה $x$.

</div>
</div>

- כל תהליך $P_i$ מוגדר ע"י **גרף תוכנית** $PG_i$ המורחב עם פעולות תקשורת.
- המעברים בגרף הם: מעברים מותנים רגילים (שמירות ופעולות), **או** פעולות תקשורת ($c!v$ / $c?x$).

---

# ערוצים: קיבולת וטיפוסים

לכל ערוץ $c$ שני מאפיינים:

- **תחום (Domain):** $dom(c)$ - טיפוס ההודעות שניתן לשדר.
  - לדוגמה: $dom(c) = \{0, 1\}$ לערוץ ביטים, או $dom(c) = \Sigma^{200}$ לטקסטים.

- **קיבולת (Capacity):** $cap(c) \in \mathbb{N} \cup \{\infty\}$ - מספר ההודעות המרבי שניתן לאחסן בחוצץ.

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="bg-orange-50 p-4 rounded border border-orange-200">

**$cap(c) = 0$ - סינכרוני**

אין חוצץ. התקשורת היא **Handshaking**: שליחה וקבלה מתרחשות **בו-זמנית**.

מקביל למנגנון ה-Handshaking שכבר ראינו!

</div>
<div class="bg-purple-50 p-2 rounded border border-purple-200">

**$cap(c) > 0$ - א-סינכרוני**

יש חוצץ. שליחה וקבלה מתרחשות **ברגעים שונים** - יש עיכוב בין שליחה לקריאה.

שליחה וקריאה של אותה הודעה <br>
 **לעולם אינן בו-זמניות**.

</div>
</div>


מערכות ערוצים מאפשרות מידול של **שני** סוגי התקשורת: סינכרונית וא-סינכרונית.

---

# מתי פעולות תקשורת בנות-ביצוע?

<div class="grid grid-cols-2 gap-4">
<div class="bg-orange-50 p-3 rounded border border-orange-200">

**Handshaking: $cap(c) = 0$**

תהליך $P_i$ יכול לשלוח $c!v$ **רק אם** תהליך אחר $P_j$ מציע פעולת קבלה משלימה $c?x$ **בו-זמנית**.

שני התהליכים מבצעים את הפעולה **יחד**, והאפקט הוא השמה מבוזרת:

$$x := v$$

</div>
<div class="bg-purple-50 p-3 rounded border border-purple-200">

**א-סינכרוני: $cap(c) > 0$**

- **שליחה** $c!v$: בר-ביצוע אם הערוץ **אינו מלא** (פחות מ-$cap(c)$ הודעות). הערך $v$ נכנס לסוף החוצץ.

- **קבלה** $c?x$: בר-ביצוע אם החוצץ **אינו ריק**. האיבר הראשון נשלף ומושם ב-$x$.

</div>
</div>

<div class="mt-4">

| | ...בר-ביצוע אם | אפקט |
|:---:|:---:|:---:|
| $c!v$ | הערוץ $c$ לא מלא | $Enqueue(c, v)$ |
| $c?x$ | הערוץ $c$ לא ריק | $x := Front(c);\ Dequeue(c)$ |

</div>


---

# הגדרה פורמלית: מערכת ערוצים 

**גרף תוכנית מעל $\langle Var, Chan \rangle$** הוא סדורה:

$$PG = \langle Loc,\ Act,\ Effect,\ \rightarrow,\ Loc_0,\ g_0 \rangle$$

כמו בהגדרה של גרף תוכנית רגיל, עם ההבדל שיחס המעברים מורחב לכלול פעולות תקשורת:

$$\rightarrow\ \subseteq\ Loc \times \big(Cond(Var) \times (Act \cup {\color{red} Comm})\big) \times Loc$$

<div class="mt-6 bg-blue-50 p-4 rounded border border-blue-200">

**מערכת ערוצים** $CS$ מעל $\langle Var, Chan \rangle$ מורכבת מגרפי תוכנית $PG_i$ מעל $\langle Var_i, Chan \rangle$ כאשר $Var = \bigcup_{1 \leq i \leq n} Var_i$:

$$CS = [PG_1 \mid \ldots \mid PG_n]$$

</div>

- הסימון $[\cdot | \cdot]$ מציין הרכבה מקבילית של תהליכים עם תקשורת דרך ערוצים.
- כל תהליך $PG_i$ יכול לבצע פעולות מקומיות **או** פעולות תקשורת ($c!v$ / $c?x$).

---

# הסמנטיקה הגלובלית: $TS(CS)$

כמו שמעבירים גרף תוכנית רגיל למערכת מעברים, כך גם למערכת ערוצים

$$CS = [PG_1 \mid \ldots \mid PG_n]$$

מתאימה מערכת המעברים $TS(CS)$ המתארת את ההתנהגות של **כל המערכת יחד**.

<div class="mt-5 bg-blue-50 p-4 rounded border border-blue-200">

המצבים הגלובליים של $TS(CS)$ הם מהצורה:

$$\langle l_1,\ldots,l_n,\eta,\xi \rangle$$

</div>

<div class="grid grid-cols-3 gap-4 mt-5 text-sm">
<div class="bg-slate-50 p-3 rounded border border-slate-200">

**$l_i$**  
המיקום הנוכחי של הרכיב $PG_i$

</div>
<div class="bg-green-50 p-3 rounded border border-green-200">

**$\eta \in Eval(Var)$**  
השמה נוכחית של כל המשתנים

</div>
<div class="bg-purple-50 p-3 rounded border border-purple-200">

**$\xi$**  
תוכן כל הערוצים במערכת

</div>
</div>

---

# הערכת ערוצים (Channel Evaluation)

הפונקציה $\xi$ מתארת עבור כל ערוץ מה נמצא כרגע בחוצץ שלו:

$$\xi \in Eval(Chan)$$
$$\xi : c \in Chan \mapsto \xi(c) \in dom(c)^*$$

- כלומר, לכל ערוץ $c$ מותאמת **סדרה סופית** של הודעות מתוך $dom(c)$.
- אורך הסדרה חייב לכבד את קיבולת הערוץ:

$$len(\xi(c)) \leq cap(c)$$

<div class="mt-5 bg-purple-50 p-4 rounded border border-purple-200">

אם

$$\xi(c) = v_1 v_2 \cdots v_k$$

אז $v_1$ נמצא **בראש התור** (front), ו-$v_k$ נמצא **בסוף התור** (rear).

</div>

---

# סימון שימושי לערוצים

כדי לעדכן את תוכן ערוץ יחיד נשתמש בסימון:

$$\xi[c := v_1,\ldots,v_k]$$

כלומר: אותה הערכת ערוצים כמו $\xi$, פרט לכך שהערוץ $c$ מקבל את הרצף החדש $v_1\ldots v_k$.

$$
\xi[c := v_1 \ldots v_k](c') =
\begin{cases}
\xi(c') & c' \neq c \\
v_1 \ldots v_k & c' = c
\end{cases}
$$

<div class="mt-5 grid grid-cols-2 gap-4 text-sm">
<div class="bg-slate-50 p-3 rounded border border-slate-200">

כך אפשר לתאר פורמלית  
**enqueue** כעדכון של סוף הרצף

</div>
<div class="bg-slate-50 p-3 rounded border border-slate-200">

וכך אפשר לתאר פורמלית  
**dequeue** כהסרת האיבר הראשון

</div>
</div>

---

# מצבים התחלתיים ופעולות של $TS(CS)$

<div class="grid grid-cols-2 gap-6 mt-2 items-start">
<div>

מצב התחלתי של $TS(CS)$ חייב לקיים שלושה תנאים:

1. לכל רכיב $PG_i$ המיקום $l_i$ הוא מיקום התחלתי, כלומר $l_i \in Loc_{0,i}$.
2. השמת המשתנים $\eta$ מקיימת את תנאי ההתחלה $g_0$.
3. כל הערוצים ריקים בתחילת הריצה.

</div>
<div class="bg-orange-50 p-4 rounded border border-orange-200 text-[15px]">

הערכת הערוצים ההתחלתית היא $\xi_0$.

עבור כל $c \in Chan$ מתקיים:

$$\xi_0(c) = \varepsilon$$
$$len(\varepsilon) = 0$$

</div>
</div>

<div class="mt-5 bg-blue-50 p-4 rounded border border-blue-200">

קבוצת הפעולות של $TS(CS)$ כוללת:

- את כל הפעולות המקומיות $\alpha \in Act_i$ של הרכיבים.
- את הסימון המיוחד $\tau$ עבור **צעדי תקשורת**: שליחה, קבלה או handshaking דרך ערוצים.

</div>

---

# הגדרה פורמלית: $TS(CS)$

<div class="text-[13px] leading-snug">

<div class="bg-slate-50 px-4 py-3 rounded border border-slate-200 -mt-2">
$$
CS = [PG_1 \mid \ldots \mid PG_n], \qquad
PG_i = \langle Loc_i, Act_i, Effect_i, \to_i, Loc_{0,i}, g_{0,i} \rangle
$$
$$TS(CS) = \langle S, Act, \to, I, AP, L \rangle$$ 
</div>

<div class="grid grid-cols-2 gap-4 mt-2">
<div class="bg-blue-50 p-3 rounded border border-blue-200">

<div class="font-bold mb-1">מרחב המצבים והפעולות</div>

$$
S = (Loc_1 \times \ldots \times Loc_n) \times Eval(Var) \times Eval(Chan)
$$

$$
Act = \biguplus_{0 < i \leq n} Act_i \cup \{\tau\}
$$

<div class="mt-1">
היחס → מוגדר בשקף הבא ע"י כללי המעבר של interleaving, מסרים א־סינכרוניים ו־handshaking.
</div>

</div>
<div class="bg-orange-50 p-3 rounded border border-orange-200">

<div class="font-bold mb-1">מצבים התחלתיים ופסוקים אטומים</div>

$$
\begin{aligned}
I = \{ \langle l_1,\ldots,l_n,\eta,\xi_0 \rangle \mid
&\forall\, 0 < i \leq n.\\
&(l_i \in Loc_{0,i} \land \eta \models g_{0,i}) \}
\end{aligned}
$$

$$
AP = \biguplus_{0 < i \leq n} Loc_i \cup Cond(Var)
$$

</div>
</div>

<div class="mt-2 bg-purple-50 p-3 rounded border border-purple-200">

<div class="font-bold mb-1">פונקציית התיוג</div>

$$
L(\langle l_1,\ldots,l_n,\eta,\xi \rangle)
=
\{l_1,\ldots,l_n\} \cup \{g \in Cond(Var) \mid \eta \models g\}
$$

תיוג מצב גלובלי כולל גם את מיקומי הבקרה הנוכחיים וגם את כל התנאים שמתקיימים תחת $\eta$.

</div>

</div>

---

# יחס המעברים של $TS(CS)$

<div class="-mt-3 text-[12px] leading-[1.05]">

<div class="bg-blue-50 p-2 rounded border border-blue-200 mt-1">

<div class="font-bold mb-0">

1. שזירה (Interleaving) של פעולה מקומית $\alpha$
<!-- 1. שזירה (Interleaving) של פעולה מקומית α -->
</div>

<div class="-my-2">
$$
\frac{
l_i \xrightarrow{g:\alpha}_i l_i'
\qquad
\eta \models g
}{
\langle l_1,\ldots,l_i,\ldots,l_n,\eta,\xi\rangle
\xrightarrow{\alpha}
\langle l_1,\ldots,l_i',\ldots,l_n,\eta',\xi\rangle
}
$$
</div>

כאשר $\eta' = Effect(\alpha,\eta)$.

</div>

<div class="grid grid-cols-2 gap-2 mt-2">
<div class="bg-purple-50 p-2 rounded border border-purple-200">

<div class="font-bold mb-0">

2א. קבלה א-סינכרונית כאשר $c \in Chan$ ו-$cap(c)>0$ 
<!-- 2א. קבלה א־סינכרונית כאשר c ∈ Chan ו־cap(c) &gt; 0 -->
</div>

<div class="-my-2">
$$
\frac{
l_i \xrightarrow{g:c?x}_i l_i'
\quad
\eta \models g
\quad
len(\xi(c)) = k > 0
\quad
\xi(c) = v_1 \ldots v_k
}{
\langle l_1,\ldots,l_i,\ldots,l_n,\eta,\xi\rangle
\xrightarrow{\tau}
\langle l_1,\ldots,l_i',\ldots,l_n,\eta',\xi'\rangle
}
$$
</div>

כאשר $\eta' = \eta[x := v_1]$ ו־$\xi' = \xi[c := v_2 \ldots v_k]$.

</div>
<div class="bg-purple-50 p-2 rounded border border-purple-200">

<div class="font-bold mb-0">

2ב. שליחה א-סינכרונית כאשר $c \in Chan$ ו-$cap(c)>0$
<!-- 2ב. שליחה א־סינכרונית כאשר c ∈ Chan ו־cap(c) &gt; 0 -->
</div>

<div class="-my-2">
$$
\frac{
l_i \xrightarrow{g:c!v}_i l_i'
\quad
\eta \models g
\quad
len(\xi(c)) = k < cap(c)
\quad
\xi(c) = v_1 \ldots v_k
}{
\langle l_1,\ldots,l_i,\ldots,l_n,\eta,\xi\rangle
\xrightarrow{\tau}
\langle l_1,\ldots,l_i',\ldots,l_n,\eta,\xi'\rangle
}
$$
</div>

כאשר $\xi' = \xi[c := v_1 \ldots v_k v]$.

</div>
</div>

<div class="bg-orange-50 p-2 rounded border border-orange-200 mt-2">

<div class="font-bold mb-0">

3. תקשורת סינכרונית כאשר $c \in Chan$ ו-$cap(c) = 0$
<!-- 3. תקשורת סינכרונית כאשר c ∈ Chan ו־cap(c) = 0 -->
</div>

<div class="-my-2">
$$
\frac{
l_i \xrightarrow{g_1:c?x}_i l_i'
\qquad
\eta \models g_1
\qquad
\eta \models g_2
\qquad
l_j \xrightarrow{g_2:c!v}_j l_j'
\qquad
i \neq j
}{
\langle l_1,\ldots,l_i,\ldots,l_j,\ldots,l_n,\eta,\xi\rangle
\xrightarrow{\tau}
\langle l_1,\ldots,l_i',\ldots,l_j',\ldots,l_n,\eta',\xi\rangle
}
$$
</div>

כאשר $\eta' = \eta[x := v]$.

</div>

</div>


---

# דוגמה: שימוש בכללי הגזירה

<div class="-mt-2 text-[11px] leading-tight">

<div class="bg-slate-50 px-3 py-0 rounded border border-slate-200">

נבחן מערכת קטנה
$
CS = [P \mid S \mid R \mid T \mid U]
$
עם ערוץ  $a$ שעבורו $cap(a)=2$ וערוץ  $h$ שעבורו $cap(h)=0$.

$$
\begin{aligned}
P&: \ p_0 \xrightarrow{\texttt{true}:\alpha} p_1
\qquad Effect(\alpha,\eta)=\eta[z:=1] \\
S&: \ s_0 \xrightarrow{\texttt{true}:a!5} s_1
\qquad
R: \ r_0 \xrightarrow{\texttt{true}:a?x} r_1 \\
T&: \ t_0 \xrightarrow{\texttt{true}:h!7} t_1
\qquad
U: \ u_0 \xrightarrow{x=5:h?y} u_1
\end{aligned}
$$

<div class="mt-2 bg-white/80 rounded border border-slate-200 px-3 py-0">
<div class="font-bold mb-1">

מצב התחלתי ב־$TS(CS)$
</div>

$$
\sigma_0 =
\langle p_0,s_0,r_0,t_0,u_0,\eta,\xi_0\rangle
\qquad
\xi_0(a)=\varepsilon
$$
</div>

</div>

<div class="grid grid-cols-2 gap-0 mt-0">
<div v-click class="bg-blue-50 p-2 rounded border border-blue-200">
<div class="font-bold mb-1">1. הפעלת כלל השזירה</div>

$$
\sigma_0
\xrightarrow{\alpha}
\sigma_1
=
\langle p_1,s_0,r_0,t_0,u_0,\eta[z:=1],\xi_0\rangle
$$

רק הרכיב $P$ מתקדם, ולכן זהו צעד מסוג interleaving.
</div>

<div v-click class="bg-purple-50 p-2 rounded border border-purple-200">
<div class="font-bold mb-1">2. הפעלת כלל שליחה א־סינכרונית</div>

$$
\sigma_1
\xrightarrow{\tau}
\sigma_2
=
\langle p_1,s_1,r_0,t_0,u_0,\eta[z:=1],\xi_1\rangle
$$

כאשר $\xi_1=\xi_0[a:=5]$, כלומר ההודעה $5$ נכנסת לחוצץ של $a$.
</div>

<div v-click class="bg-purple-50 p-2 rounded border border-purple-200">
<div class="font-bold mb-1">3. הפעלת כלל קבלה א־סינכרונית</div>

$$
\sigma_2
\xrightarrow{\tau}
\sigma_3
=
\langle p_1,s_1,r_1,t_0,u_0,\eta[z:=1,x:=5],\xi_0\rangle
$$

הרכיב $R$ שולף את $5$ מראש התור, ולכן $a$ חוזר להיות ריק.
</div>

<div v-click class="bg-orange-50 p-2 rounded border border-orange-200">
<div class="font-bold mb-1">4. הפעלת כלל התקשורת הסינכרונית</div>

$$
\sigma_3
\xrightarrow{\tau}
\sigma_4
=
\langle p_1,s_1,r_1,t_1,u_1,\eta[z:=1,x:=5,y:=7],\xi_0\rangle
$$

כיוון ש־$cap(h)=0$, הרכיבים $T$ ו־$U$ חייבים לבצע handshaking יחד.
</div>
</div>

<div class="mt-2 bg-emerald-50 px-3 py-2 rounded border border-emerald-200">
<div class="font-bold mb-1">מסלול ריצה שמתפרש בהדרגה</div>

<div class="font-mono text-[10px] leading-snug">
<span>\(\sigma_0\)</span>
<span v-click>\(\xrightarrow{\alpha} \sigma_1\)</span>
<span v-click>\(\xrightarrow{\tau} \sigma_2\)</span>
<span v-click>\(\xrightarrow{\tau} \sigma_3\)</span>
<span v-click>\(\xrightarrow{\tau} \sigma_4\)</span>
</div>
</div>

</div>

---
clicks: 1
---

# אתגר 1: מה יהיה הערך של $x$?

> הערוץ מתחיל ריק, ו-$x$ אינו מאותחל מראש. עוצרים ברגע שמגיעים למצב ללא מוצא.

<div class="grid grid-cols-2 gap-8 items-start scale-[0.82] origin-top" dir="ltr">
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$P$
</div>
<TransitionSystemD3 :width="180" :height="140"
  :states="[
    { id: 'c1p0', text: '$p_0$', initial: true, initialDirection: 'top', x: 90, y: 30, width: 44 },
    { id: 'c1p1', text: '$p_1$', x: 90, y: 110, width: 44 }
  ]"
  :transitions="[
    { source: 'c1p0', target: 'c1p1', action: '$a!4$', actionX: 28 }
  ]"
/>
</div>
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$R$
</div>
<TransitionSystemD3 :width="180" :height="140"
  :states="[
    { id: 'c1r0', text: '$r_0$', initial: true, initialDirection: 'top', x: 90, y: 30, width: 44 },
    { id: 'c1r1', text: '$r_1$', x: 90, y: 110, width: 44 }
  ]"
  :transitions="[
    { source: 'c1r0', target: 'c1r1', action: '$a?x$', actionX: 28 }
  ]"
/>
</div>
</div>

<div class="-mt-4 text-center">

$cap(a)=1$
</div>

מה יהיה הערך של $x$ בסוף הריצה?

<v-click>

**תשובה:** בהכרח $x=4$.

יש רק הודעה אחת שנשלחת, ו-$R$ קורא בדיוק אותה לפני שמגיעים למצב ללא מוצא.

</v-click>

---
clicks: 1
---

# אתגר 2: יותר מאפשרות אחת

> הערוץ מתחיל ריק, ו-$x$ אינו מאותחל מראש. עוצרים ברגע שמגיעים למצב ללא מוצא.

<div class="grid grid-cols-3 gap-3 items-start scale-[0.74] origin-top" dir="ltr">
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$S_1$
</div>
<TransitionSystemD3 :width="160" :height="140"
  :states="[
    { id: 'c2s10', text: '$s_0$', initial: true, initialDirection: 'top', x: 80, y: 30, width: 44 },
    { id: 'c2s11', text: '$s_1$', x: 80, y: 110, width: 44 }
  ]"
  :transitions="[
    { source: 'c2s10', target: 'c2s11', action: '$a!1$', actionX: 28 }
  ]"
/>
</div>
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$S_2$
</div>
<TransitionSystemD3 :width="160" :height="140"
  :states="[
    { id: 'c2s20', text: '$t_0$', initial: true, initialDirection: 'top', x: 80, y: 30, width: 44 },
    { id: 'c2s21', text: '$t_1$', x: 80, y: 110, width: 44 }
  ]"
  :transitions="[
    { source: 'c2s20', target: 'c2s21', action: '$a!2$', actionX: 28 }
  ]"
/>
</div>
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$R$
</div>
<TransitionSystemD3 :width="160" :height="140"
  :states="[
    { id: 'c2r0', text: '$r_0$', initial: true, initialDirection: 'top', x: 80, y: 30, width: 44 },
    { id: 'c2r1', text: '$r_1$', x: 80, y: 110, width: 44 }
  ]"
  :transitions="[
    { source: 'c2r0', target: 'c2r1', action: '$a?x$', actionX: 28 }
  ]"
/>
</div>
</div>

<div class="-mt-6 text-center">

$cap(a)=1$
</div>

אילו ערכים יכולים להיות ל-$x$ בסוף הריצה?

<v-click>

**תשובה:** $x \in \{1,2\}$.

השולח שמצליח ראשון להכניס הודעה לערוץ קובע מה $R$ יקרא,
ואחר כך השולח השני עוד יכול להיתקע עם הודעה שלא תיקרא.

</v-click>

---
clicks: 1
---

# אתגר 3: שלושה תהליכים

> הערוצים מתחילים ריקים, ו-$x$ אינו מאותחל מראש. עוצרים ברגע שמגיעים למצב ללא מוצא.

<div class="grid grid-cols-3 gap-3 items-start scale-[0.72] origin-top" dir="ltr">
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$P$
</div>
<TransitionSystemD3 :width="250" :height="110"
  :states="[
    { id: 'c3p0', text: '$p_0$', initial: true, initialDirection: 'top', x: 40, y: 45, width: 44 },
    { id: 'c3p1', text: '$p_1$', x: 40+1*95, y: 45, width: 44 },
    { id: 'c3p2', text: '$p_2$', x: 40+2*95, y: 45, width: 44 }
  ]"
  :transitions="[
    { source: 'c3p0', target: 'c3p1', action: '$a!1$', actionY: -12 },
    { source: 'c3p1', target: 'c3p2', action: '$b!2$', actionY: -12 }
  ]"
/>
</div>
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$Q$
</div>
<TransitionSystemD3 :width="170" :height="110"
  :states="[
    { id: 'c3q0', text: '$q_0$', initial: true, initialDirection: 'top', x: 45, y: 45, width: 44 },
    { id: 'c3q1', text: '$q_1$', x: 45+1*95, y: 45, width: 44 }
  ]"
  :transitions="[
    { source: 'c3q0', target: 'c3q1', action: '$b!3$', actionY: -12 }
  ]"
/>
</div>
<div class="flex flex-col items-center">
<div class="font-bold text-slate-500 -mb-4">

$R$
</div>
<TransitionSystemD3 :width="250" :height="110"
  :states="[
    { id: 'c3r0', text: '$r_0$', initial: true, initialDirection: 'top', x: 40, y: 45, width: 44 },
    { id: 'c3r1', text: '$r_1$', x: 40+1*95, y: 45, width: 44 },
    { id: 'c3r2', text: '$r_2$', x: 40+2*95, y: 45, width: 44 }
  ]"
  :transitions="[
    { source: 'c3r0', target: 'c3r1', action: '$a?x$', actionY: -12 },
    { source: 'c3r1', target: 'c3r2', action: '$b?x$', actionY: -12 }
  ]"
/>
</div>
</div>

<div class="-mt-6 text-center">

$cap(a)=cap(b)=1$
</div>

אילו ערכים יכולים להיות ל-$x$ בסוף הריצה?

<v-click>

**תשובה:** $x \in \{2,3\}$.

אמנם הקריאה הראשונה של $R$ קובעת זמנית $x=1$, אבל הקריאה השנייה מ-$b$ דורסת את הערך הזה.
לכן $1$ אינו יכול להיות הערך הסופי, וההכרעה היא מי יכניס ראשון ל-$b$: הרכיב $P$ עם $2$ או הרכיב $Q$ עם $3$.

</v-click>

---
clicks: 1
---

# אתגר 4: שאלה קומבינטורית

> הערוץ מתחיל ריק. המשתנים $x,z$ מתחילים ב-$0$. עוצרים ברגע שמגיעים למצב ללא מוצא.

<div class="grid grid-cols-2 gap-4 items-start scale-[0.74] origin-top" dir="ltr">
<div class="flex flex-col gap-2">
<div class="flex flex-col items-center">
<!-- <div class="font-bold text-slate-500 -mb-4">

$S_0$ 
</div> -->
<TransitionSystemD3 :width="260" :height="90"
  :states="[
    { id: 'c4s00', text: '$s_0$', initial: true, initialDirection: 'top', x: 30, y: 40, width: 44 },
    { id: 'c4s01', text: '$s_1$', x: 30+1*95, y: 40, width: 44 },
    { id: 'c4s02', text: '$s_2$', x: 30+2*95, y: 40, width: 44 },
    { id: 'c4s03', text: '$s_3$', x: 30+3*95, y: 40, width: 44 }
  ]"
  :transitions="[
    { source: 'c4s00', target: 'c4s01', action: '$a!0$', actionY: -12 },
    { source: 'c4s01', target: 'c4s02', action: '$a!0$', actionY: -12 },
    { source: 'c4s02', target: 'c4s03', action: '$a!0$', actionY: -12 }
  ]"
/>
</div>
<div class="flex flex-col items-center">
<!-- <div class="font-bold text-slate-500 -mb-4">

$S_1$
</div> -->
<TransitionSystemD3 :width="260" :height="90"
  :states="[
    { id: 'c4s10', text: '$t_0$', initial: true, initialDirection: 'top', x: 30, y: 40, width: 44 },
    { id: 'c4s11', text: '$t_1$', x: 30+1*95, y: 40, width: 44 },
    { id: 'c4s12', text: '$t_2$', x: 30+2*95, y: 40, width: 44 },
    { id: 'c4s13', text: '$t_3$', x: 30+3*95, y: 40, width: 44 }
  ]"
  :transitions="[
    { source: 'c4s10', target: 'c4s11', action: '$a!1$', actionY: -12 },
    { source: 'c4s11', target: 'c4s12', action: '$a!1$', actionY: -12 },
    { source: 'c4s12', target: 'c4s13', action: '$a!1$', actionY: -12 }
  ]"
/>
</div>
</div>
<div class="flex flex-col items-center">
<!-- <div class="font-bold text-slate-500 -mb-10">

$R$
</div> -->
<TransitionSystemD3 :width="360" :height="190"
  :states="[
    { id: 'c4r0', text: '$r_0$', initial: true, initialDirection: 'top', x: 80, y: 95, width: 44, initialText: '$x =0 \\land z=0$' },
    { id: 'c4r1', text: '$r_1$', x: 370, y: 95, width: 44 }
  ]"
  :transitions="[
    { source: 'c4r0', target: 'c4r1', action: '$a?y$', actionY: -12 },
    { source: 'c4r1', target: 'c4r0', action: '$y=0 : z:=z+1$', curve: -0.35, actionY: 25, actionWidth: 130, actionFontSize: 13 },
    { source: 'c4r1', target: 'c4r0', action: '$y=1 : x:=x+z$', curve: 0.35, actionY: -25, actionWidth: 130, actionFontSize: 13 }
  ]"
/>
</div>
</div>

<div class="-mt-20 text-center">

$cap(a)=1$
</div>

אילו ערכים יכולים להיות ל-$x$ בסוף הריצה?

<v-click>

**תשובה:** $x \in \{0,1,\dots,9\}$.

בסוף הריצה $x$ סופר בדיוק את מספר הזוגות מסוג "0 לפני 1" במילה שהתקבלה:
כל פעם שנקלטת $1$, מוסיפים ל-$x$ את מספר האפסים שכבר נקלטו.

כל שזירה של שלושה אפסים ושלוש יחידות אפשרית כאן, ולכן אפשר לקבל כל מספר
בין $0$ לבין $3 \cdot 3 = 9$.

</v-click>

---

# דוגמה: פרוטוקול הביט המתהפך (ABP)

<img src="/images/abp_channels_comic.png" class="absolute bottom-0 left-0 w-70" />

מערכת תקשורת בין שולח $S$ ומקבל $R$ דרך שני ערוצים:

- **ערוץ $c$** (שולח $\to$ מקבל): לא אמין - הודעות עלולות **ללכת לאיבוד**.
  - $cap(c) = \infty$ (חוצץ אינסופי)
- **ערוץ $d$** (מקבל $\to$ שולח): אמין לחלוטין.
  - $cap(d) = \infty$

**עיקרון Send-and-Wait:** $S$ שולח הודעה ומחכה לאישור (ACK) לפני שליחת ההודעה הבאה.

**ביט בקרה מתחלף:** ההודעות נשלחות כזוגות $\langle m, b \rangle$ כאשר $b \in \{0,1\}$:

$$\langle m_0, 0 \rangle,\ \langle m_1, 1 \rangle,\ \langle m_2, 0 \rangle,\ \langle m_3, 1 \rangle,\ \ldots$$

- $R$ מקבל $\langle m, b \rangle$ ושולח ACK עם ביט $b$ חזרה דרך $d$.
- $S$ מקבל ACK עם $b$ ושולח הודעה חדשה עם ביט $\neg b$.
- אם $S$ מחכה זמן רב מדי - מתרחש **timeout** והוא שולח מחדש.


---

# ABP: גרפי התוכנית

<div class="relative h-[400px] w-full" dir="ltr">

<!-- Sender S -->
<div class="absolute -top-10 -left-10 scale-[0.6] origin-top-left">
  <h4 class="font-bold mb-15 text-center">שולח (Sender S)</h4>
  <TransitionSystemD3 :width="900" :height="250"
    :states="[
      { id: 'snd0', text: 'snd_msg(0)', initial: true, initialDirection: 'top', x: 80, y: 50, width: 130, rx: 20 },
      { id: 'st0', text: 'st_tmr(0)', x: 310, y: 50, width: 110, rx: 20 },
      { id: 'wait0', text: 'wait(0)', x: 540, y: 50, width: 90, rx: 20 },
      { id: 'chk0', text: 'chk_ack(0)', x: 770, y: 50, width: 130, rx: 20 },
      { id: 'chk1', text: 'chk_ack(1)', x: 80, y: 230, width: 130, rx: 20 },
      { id: 'wait1', text: 'wait(1)', x: 310, y: 230, width: 90, rx: 20 },
      { id: 'st1', text: 'st_tmr(1)', x: 540, y: 230, width: 110, rx: 20 },
      { id: 'snd1', text: 'snd_msg(1)', x: 770, y: 230, width: 130, rx: 20 }
    ]"
    :transitions="[
      { source: 'snd0', target: 'st0', action: 'c!⟨m,0⟩' },
      { source: 'snd0', target: 'st0', action: 'lost', curve: 0.2, actionY: 8 },
      { source: 'st0', target: 'wait0', action: 'tmr_on!' },
      { source: 'wait0', target: 'chk0', action: 'd?x' },
      { source: 'chk0', target: 'snd1', action: 'x=0: tmr_off!' },
      { source: 'chk0', target: 'snd0', action: 'x=1', curve: 0.2, actionY: -10 },
      { source: 'wait0', target: 'snd0', action: 'timeout?', curve: 0.2, actionY: -5, actionX: 40 },
      { source: 'snd1', target: 'st1', action: 'c!⟨m,1⟩' },
      { source: 'snd1', target: 'st1', action: 'lost', curve: 0.2, actionY: -8 },
      { source: 'st1', target: 'wait1', action: 'tmr_on!' },
      { source: 'wait1', target: 'chk1', action: 'd?x' },
      { source: 'chk1', target: 'snd0', action: 'x=1 : tmr_off!' },
      { source: 'chk1', target: 'snd1', action: 'x=0', curve: 0.2, actionY: 10 },
      { source: 'wait1', target: 'snd1', action: 'timeout?', curve: 0.2, actionY: 5, actionX: -40 }
    ]"
  />
</div>

<!-- Receiver R -->
<div class="absolute top-20 right-0 scale-[0.6] origin-top-right">
  <h4 class="font-bold mb-4 text-center">מקבל (Receiver R)</h4>
  <TransitionSystemD3 :width="550" :height="150"
    :states="[
      { id: 'w0', text: 'wait(0)', initial: true, initialDirection: 'top', x: 70, y: 50, width: 90, rx: 20 },
      { id: 'pr0', text: 'pr_msg(0)', x: 270, y: 50, width: 120, rx: 20 },
      { id: 'sa0', text: 'snd_ack(0)', x: 470, y: 50, width: 120, rx: 20 },
      { id: 'sa1', text: 'snd_ack(1)', x: 70, y: 220, width: 120, rx: 20 },
      { id: 'pr1', text: 'pr_msg(1)', x: 270, y: 220, width: 120, rx: 20 },
      { id: 'w1', text: 'wait(1)', x: 470, y: 220, width: 90, rx: 20 }
    ]"
    :transitions="[
      { source: 'w0', target: 'pr0', action: 'c?⟨m,y⟩' },
      { source: 'pr0', target: 'sa0', action: 'y=0', actionY: -20 },
      { source: 'pr0', target: 'w0', action: 'y=1', curve: 0.3, actionY: -10 },
      { source: 'sa0', target: 'w1', action: 'd!0' },
      { source: 'w1', target: 'pr1', action: 'c?⟨m,y⟩' },
      { source: 'pr1', target: 'sa1', action: 'y=1', actionY: 5 },
      { source: 'pr1', target: 'w1', action: 'y=0', curve: 0.3, actionY: 10 },
      { source: 'sa1', target: 'w0', action: 'd!1' }
    ]"
  />
</div>

<!-- Timer -->
<div class="absolute bottom-10 left-0 scale-[0.6] origin-bottom-right">
  <h4 class="font-bold -mb-4 text-center">טיימר (Timer)</h4>
  <TransitionSystemD3 :width="200" :height="150"
    :states="[
      { id: 'off', text: 'off', initial: true, initialDirection: 'top', x: 100, y: 50, rx: 20 },
      { id: 'on', text: 'on', x: 100, y: 140, rx: 20 }
    ]"
    :transitions="[
      { source: 'off', target: 'on', action: 'tmr_on?', curve: 1, actionX: -20 },
      { source: 'on', target: 'off', action: 'tmr_off?'  },
      { source: 'on', target: 'off', action: 'timeout!', curve: 1, actionX: 20 }
    ]"
  />
</div>

<!-- Formal Definition -->
<div class="absolute -bottom-15 left-0 w-full text-center">

$$ABP = [S \mid Timer \mid R]$$
$$Chan = \{c, d, tmr\_on, tmr\_off, timeout\}, Var = \{x, y, m_i\}$$

</div>

</div>

---

# ABP: ריצה עם שידור חוזר לא צפוי

<div class="-mt-2 text-[11px] leading-tight">

<div class="mb-0">
קטע הריצה הבא מראה מדוע המקבל `R` חייב לדעת להתמודד גם עם קבלה חוזרת של
`⟨m,0⟩` אחרי שכבר עבר למצב `wait(1)`.
</div>

<table class="w-full text-[9px] border-collapse" dir="ltr">
  <thead>
    <tr class="bg-slate-100">
      <th class="border border-slate-300 px-1 py-0.5 text-center align-middle">sender S</th>
      <th class="border border-slate-300 px-1 py-0.5 text-center align-middle">timer</th>
      <th class="border border-slate-300 px-1 py-0.5 text-center align-middle">receiver R</th>
      <th class="border border-slate-300 px-1 py-0.5 text-center align-middle">channel c</th>
      <th class="border border-slate-300 px-1 py-0.5 text-center align-middle">channel d</th>
      <th class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">אירוע</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>snd_msg(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl"></td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>st_tmr(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">⟨m,0⟩</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">הודעה עם סיבית 0 נשלחת</td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>on</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">⟨m,0⟩</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl"></td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>snd_msg(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">⟨m,0⟩</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">timeout</td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>st_tmr(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">⟨m,0⟩,⟨m,0⟩</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">שידור חוזר</td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>st_tmr(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>pr_msg(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">⟨m,0⟩</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">המקבל קורא את ההודעה הראשונה</td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>st_tmr(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>wait(1)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">⟨m,0⟩</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">0</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">המקבל עובר למצב 1</td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>st_tmr(0)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>off</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle"><i>pr_msg(1)</i></td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">&empty;</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">0</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">המקבל מתעלם מהשידור החוזר</td>
    </tr>
    <tr>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">...</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">...</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">...</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">...</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle">...</td>
      <td class="border border-slate-300 px-1 py-0.5 text-center align-middle" dir="rtl">...</td>
    </tr>
  </tbody>
</table>

<div class="grid grid-cols-2 gap-2 mt-2">
  <div class="bg-red-50 p-2 rounded border border-red-200 text-[10px]">
    <b>למה זה חיוני?</b><br>
    בלי ההתנהגות הזו בגרף של `R`, המערכת הייתה נתקעת כאשר שידור חוזר ישן היה מגיע
    אחרי שהמקבל כבר עבר למצב `wait(1)`.
  </div>
  <div class="bg-green-50 p-2 rounded border border-green-200 text-[10px]">
    <b>פישוט אפשרי של `S`:</b><br>
    אם הערוץ `d` אמין, אפשר להשמיט את המצבים <i>chk_ack(0)</i> ו־<i>chk_ack(1)</i>.
    אם `d` אינו אמין, המצבים הללו נשארים הכרחיים.
  </div>
</div>

</div>



