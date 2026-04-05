export type PgExampleKey = 'if-basic' | 'do-basic' | 'nested-if-do'

export type PgState = {
  id: string
  shortLabel: string
  locationText: string
  reachableFromStart: boolean
  x: number
  y: number
  width: number
  initial?: boolean
  initialDirection?: 'left' | 'right' | 'top' | 'bottom'
}

export type PgEdge = {
  id: string
  source: string
  target: string
  graphLabel: string
  previewLabel: string
  actionWidth?: number
  actionHeight?: number
  actionX?: number
  actionY?: number
  loopDirection?: string
  loopRadius?: number
  loopLabelRadius?: number
  curve?: number
}

export type PgStep = {
  id: string
  edgeId: string
  source: string
  target: string
  note: string
  ruleTitle: string
  ruleLines: string[]
  ruleLatex?: string
  instanceLines: string[]
  instanceLatex?: string
}

export type PgExample = {
  program: string[]
  width: number
  height: number
  introNote: string
  introRuleLines: string[]
  states: PgState[]
  edges: PgEdge[]
  steps: PgStep[]
}

const ASSIGN_RULE_LATEX = String.raw`\frac{}{\texttt{x := expr} \xrightarrow{\mathrm{true} : \texttt{x := expr}} \texttt{exit}}`

const SKIP_RULE_LATEX = String.raw`\frac{}{\texttt{skip} \xrightarrow{\mathrm{true} : \texttt{skip}} \texttt{exit}}`

const SEQ_RULE_LATEX = String.raw`\frac{stmt_1 \xrightarrow{g : \alpha} \texttt{exit}}{stmt_1 ; stmt_2 \xrightarrow{g : \alpha} stmt_2}`

const IF_RULE_LATEX = String.raw`\frac{stmt_i \xrightarrow{h : \alpha} stmt_i'}{\texttt{cond\_cmd} \xrightarrow{(g_i \land h) : \alpha} stmt_i'}`

const DO_FINISH_RULE_LATEX = String.raw`\frac{stmt_i \xrightarrow{h : \alpha} \texttt{exit}}{\texttt{loop\_cmd} \xrightarrow{(g_i \land h) : \alpha} \texttt{loop\_cmd}}`

const DO_CONTINUE_RULE_LATEX = String.raw`\frac{stmt_i \xrightarrow{h : \alpha} stmt_i' \quad stmt_i' \neq \texttt{exit}}{\texttt{loop\_cmd} \xrightarrow{(g_i \land h) : \alpha} stmt_i' ; \texttt{loop\_cmd}}`

const DO_EXIT_RULE_LATEX = String.raw`\frac{}{\texttt{loop\_cmd} \xrightarrow{(\neg g_1 \land \cdots \land \neg g_n) : \texttt{skip}} \texttt{exit}}`

export const pgExamples: Record<PgExampleKey, PgExample> = {
  'if-basic': {
    program: [
      'if',
      ':: x > 1 -> y := x + y',
      ':: true  -> x := 0; y := x',
      'fi',
    ],
    width: 560,
    height: 330,
    introNote: 'בונים את כל המעברים מעל Loc = sub(stmt). בדוגמה הזאת כל המקומות אכן נגישים מהמקום ההתחלתי.',
    introRuleLines: [
      'מתחילים מן המעברים הבסיסיים של תתי-הפקודות.',
      'אחר כך מרכיבים מהם מעברים עבור sequence ועבור if.',
    ],
    states: [
      {
        id: 'if-l0',
        shortLabel: 'l_0',
        locationText: 'if :: x > 1 -> y := x + y :: true -> x := 0; y := x fi',
        reachableFromStart: true,
        x: 286,
        y: 56,
        width: 74,
        initial: true,
        initialDirection: 'top',
      },
      {
        id: 'if-l1',
        shortLabel: 'l_1',
        locationText: 'x := 0; y := x',
        reachableFromStart: true,
        x: 504,
        y: 122,
        width: 74,
      },
      {
        id: 'if-l2',
        shortLabel: 'l_2',
        locationText: 'y := x',
        reachableFromStart: true,
        x: 504,
        y: 286,
        width: 74,
      },
      {
        id: 'if-l3',
        shortLabel: 'l_3',
        locationText: 'y := x + y',
        reachableFromStart: true,
        x: 118,
        y: 162,
        width: 74,
      },
      {
        id: 'if-exit',
        shortLabel: 'exit',
        locationText: 'exit',
        reachableFromStart: true,
        x: 286,
        y: 286,
        width: 74,
      },
    ],
    edges: [
      {
        id: 'if-e1',
        source: 'if-l3',
        target: 'if-exit',
        graphLabel: '$true : y := x + y$',
        previewLabel: '-- true : y := x + y -->',
        actionWidth: 144,
        curve: 0.16,
        actionY: -4,
      },
      {
        id: 'if-e2',
        source: 'if-l2',
        target: 'if-exit',
        graphLabel: '$true : y := x$',
        previewLabel: '-- true : y := x -->',
        actionWidth: 118,
        curve: -0.16,
        actionY: -4,
      },
      {
        id: 'if-e3',
        source: 'if-l1',
        target: 'if-l2',
        graphLabel: '$true : x := 0$',
        previewLabel: '-- true : x := 0 -->',
        actionWidth: 120,
        actionX: 8,
      },
      {
        id: 'if-e4',
        source: 'if-l0',
        target: 'if-exit',
        graphLabel: '$x > 1 : y := x + y$',
        previewLabel: '-- x > 1 : y := x + y -->',
        actionWidth: 166,
        actionX: -32,
        actionY: -2,
      },
      {
        id: 'if-e5',
        source: 'if-l0',
        target: 'if-l2',
        graphLabel: '$true : x := 0$',
        previewLabel: '-- true : x := 0 -->',
        actionWidth: 122,
        actionX: 30,
      },
    ],
    steps: [
      {
        id: 'if-step-1',
        edgeId: 'if-e1',
        source: 'if-l3',
        target: 'if-exit',
        note: 'הפקודה y := x + y היא אטומית, ולכן אקסיומת ההשמה נותנת לה מעבר ישיר ל-exit.',
        ruleTitle: 'אקסיומת השמה',
        ruleLines: [
          'x := expr -- true : x := expr --> exit',
        ],
        ruleLatex: ASSIGN_RULE_LATEX,
        instanceLines: [
          'y := x + y -- true : y := x + y --> exit',
        ],
      },
      {
        id: 'if-step-2',
        edgeId: 'if-e2',
        source: 'if-l2',
        target: 'if-exit',
        note: 'אותו כלל בסיסי פועל גם על y := x, ולכן גם l_2 יוצא ל-exit בצעד אחד.',
        ruleTitle: 'אקסיומת השמה',
        ruleLines: [
          'x := expr -- true : x := expr --> exit',
        ],
        ruleLatex: ASSIGN_RULE_LATEX,
        instanceLines: [
          'y := x -- true : y := x --> exit',
        ],
      },
      {
        id: 'if-step-3',
        edgeId: 'if-e3',
        source: 'if-l1',
        target: 'if-l2',
        note: 'כאן מפעילים את כלל ההרכבה הסדרתית: הצעד הראשון של x := 0 מסיים את stmt_1, ולכן עוברים ל-y := x.',
        ruleTitle: 'הרכבה סדרתית',
        ruleLines: [
          'אם stmt_1 -- g : alpha --> exit',
          'אז stmt_1 ; stmt_2 -- g : alpha --> stmt_2',
        ],
        ruleLatex: SEQ_RULE_LATEX,
        instanceLines: [
          'x := 0 -- true : x := 0 --> exit',
          'x := 0 ; y := x -- true : x := 0 --> y := x',
        ],
      },
      {
        id: 'if-step-4',
        edgeId: 'if-e4',
        source: 'if-l0',
        target: 'if-exit',
        note: 'מעל הענף הראשון של if מצרפים את guard x > 1 למעבר שכבר נגזר עבור y := x + y.',
        ruleTitle: 'כלל if',
        ruleLines: [
          'אם stmt_i -- h : alpha --> stmt_i\'',
          'אז cond_cmd -- (g_i && h) : alpha --> stmt_i\'',
        ],
        ruleLatex: IF_RULE_LATEX,
        instanceLines: [
          'y := x + y -- true : y := x + y --> exit',
          'l_0 -- x > 1 : y := x + y --> exit',
        ],
        instanceLatex: String.raw`\frac{\frac{}{\texttt{y := x + y} \xrightarrow{\mathrm{true} : \texttt{y := x + y}} \texttt{exit}}}{\ell_0 \xrightarrow{x > 1 : \texttt{y := x + y}} \texttt{exit}}`,
      },
      {
        id: 'if-step-5',
        edgeId: 'if-e5',
        source: 'if-l0',
        target: 'if-l2',
        note: 'באותו אופן, על הענף השני של if יושבים guard = true והמעבר הסדרתי של x := 0 ; y := x.',
        ruleTitle: 'כלל if',
        ruleLines: [
          'אם stmt_i -- h : alpha --> stmt_i\'',
          'אז cond_cmd -- (g_i && h) : alpha --> stmt_i\'',
        ],
        ruleLatex: IF_RULE_LATEX,
        instanceLines: [
          'x := 0 ; y := x -- true : x := 0 --> y := x',
          'l_0 -- true : x := 0 --> l_2',
        ],
        instanceLatex: String.raw`\frac{\frac{\frac{}{\texttt{x := 0} \xrightarrow{\mathrm{true} : \texttt{x := 0}} \texttt{exit}}}{\texttt{x := 0 ; y := x} \xrightarrow{\mathrm{true} : \texttt{x := 0}} \texttt{y := x}}}{\ell_0 \xrightarrow{\mathrm{true} : \texttt{x := 0}} \ell_2}`,
      },
    ],
  },
  'do-basic': {
    program: [
      'do',
      ':: x > 1 -> y := x + y',
      ':: y < x -> x := 0; y := x',
      'od',
    ],
    width: 560,
    height: 360,
    introNote: 'הגרף כולל גם מקומות שאינם נגישים מהמקום ההתחלתי. כאן l_2 שייך ל-Loc, אבל אין מסלול שמוביל אליו מן ההתחלה.',
    introRuleLines: [
      'ב-do מחשבים מעברים גם מן הלולאה עצמה וגם מן המקומות שנוצרו בצורה stmt ; loop_cmd.',
      'מקומות שאינם נגישים עדיין נשארים חלק מן הגרף.',
    ],
    states: [
      {
        id: 'do-l0',
        shortLabel: 'l_0',
        locationText: 'do :: x > 1 -> y := x + y :: y < x -> x := 0; y := x od',
        reachableFromStart: true,
        x: 276,
        y: 66,
        width: 74,
        initial: true,
        initialDirection: 'left',
      },
      {
        id: 'do-l1',
        shortLabel: 'l_1',
        locationText: 'x := 0; y := x; loop_cmd',
        reachableFromStart: true,
        x: 458,
        y: 258,
        width: 82,
      },
      {
        id: 'do-l2',
        shortLabel: 'l_2',
        locationText: 'y := x + y; loop_cmd',
        reachableFromStart: false,
        x: 112,
        y: 236,
        width: 82,
      },
      {
        id: 'do-l3',
        shortLabel: 'l_3',
        locationText: 'y := x; loop_cmd',
        reachableFromStart: true,
        x: 276,
        y: 322,
        width: 82,
      },
      {
        id: 'do-exit',
        shortLabel: 'exit',
        locationText: 'exit',
        reachableFromStart: true,
        x: 506,
        y: 72,
        width: 74,
      },
    ],
    edges: [
      {
        id: 'do-e1',
        source: 'do-l2',
        target: 'do-l0',
        graphLabel: '$true : y := x + y$',
        previewLabel: '-- true : y := x + y -->',
        actionWidth: 146,
        curve: -0.12,
        actionX: -10,
      },
      {
        id: 'do-e2',
        source: 'do-l3',
        target: 'do-l0',
        graphLabel: '$true : y := x$',
        previewLabel: '-- true : y := x -->',
        actionWidth: 118,
        curve: 0.12,
        actionX: 34,
        actionY: -18,
      },
      {
        id: 'do-e3',
        source: 'do-l1',
        target: 'do-l3',
        graphLabel: '$true : x := 0$',
        previewLabel: '-- true : x := 0 -->',
        actionWidth: 120,
        actionX: 6,
      },
      {
        id: 'do-e4',
        source: 'do-l0',
        target: 'do-l0',
        graphLabel: '$x > 1 : y := x + y$',
        previewLabel: '-- x > 1 : y := x + y -->',
        actionWidth: 164,
        loopDirection: '-95deg',
        loopRadius: 92,
        loopLabelRadius: 80,
        actionY: -4,
      },
      {
        id: 'do-e5',
        source: 'do-l0',
        target: 'do-l3',
        graphLabel: '$y < x : x := 0$',
        previewLabel: '-- y < x : x := 0 -->',
        actionWidth: 134,
        actionX: -10,
        actionY: 16,
        curve: 0.1,
      },
      {
        id: 'do-e6',
        source: 'do-l0',
        target: 'do-exit',
        graphLabel: '$\\neg(x > 1) \\land \\neg(y < x) : skip$',
        previewLabel: '-- !(x > 1) && !(y < x) : skip -->',
        actionWidth: 220,
        actionX: 14,
        actionY: 6,
      },
    ],
    steps: [
      {
        id: 'do-step-1',
        edgeId: 'do-e1',
        source: 'do-l2',
        target: 'do-l0',
        note: 'גוזרים קודם מעבר גם מ-l_2, אף על פי שהוא לא נגיש מההתחלה. הוא שייך ל-Loc ולכן חייב לקבל מעברים לפי הכללים.',
        ruleTitle: 'הרכבה סדרתית',
        ruleLines: [
          'אם stmt_1 -- g : alpha --> exit',
          'אז stmt_1 ; stmt_2 -- g : alpha --> stmt_2',
        ],
        ruleLatex: SEQ_RULE_LATEX,
        instanceLines: [
          'y := x + y -- true : y := x + y --> exit',
          'y := x + y ; loop_cmd -- true : y := x + y --> loop_cmd',
        ],
        instanceLatex: String.raw`\frac{\frac{}{\texttt{y := x + y} \xrightarrow{\mathrm{true} : \texttt{y := x + y}} \texttt{exit}}}{\texttt{y := x + y ; loop\_cmd} \xrightarrow{\mathrm{true} : \texttt{y := x + y}} \texttt{loop\_cmd}}`,
      },
      {
        id: 'do-step-2',
        edgeId: 'do-e2',
        source: 'do-l3',
        target: 'do-l0',
        note: 'אותו כלל סדרתי מחזיר גם את y := x ; loop_cmd אל הלולאה עצמה.',
        ruleTitle: 'הרכבה סדרתית',
        ruleLines: [
          'אם stmt_1 -- g : alpha --> exit',
          'אז stmt_1 ; stmt_2 -- g : alpha --> stmt_2',
        ],
        ruleLatex: SEQ_RULE_LATEX,
        instanceLines: [
          'y := x -- true : y := x --> exit',
          'y := x ; loop_cmd -- true : y := x --> loop_cmd',
        ],
        instanceLatex: String.raw`\frac{\frac{}{\texttt{y := x} \xrightarrow{\mathrm{true} : \texttt{y := x}} \texttt{exit}}}{\texttt{y := x ; loop\_cmd} \xrightarrow{\mathrm{true} : \texttt{y := x}} \texttt{loop\_cmd}}`,
      },
      {
        id: 'do-step-3',
        edgeId: 'do-e3',
        source: 'do-l1',
        target: 'do-l3',
        note: 'כעת מפעילים את כלל ההרכבה על x := 0 ; y := x ; loop_cmd: הצעד הראשון מסיים את x := 0 ולכן עוברים ל-y := x ; loop_cmd.',
        ruleTitle: 'הרכבה סדרתית',
        ruleLines: [
          'אם stmt_1 -- g : alpha --> exit',
          'אז stmt_1 ; stmt_2 -- g : alpha --> stmt_2',
        ],
        ruleLatex: SEQ_RULE_LATEX,
        instanceLines: [
          'x := 0 -- true : x := 0 --> exit',
          'x := 0 ; y := x ; loop_cmd -- true : x := 0 --> y := x ; loop_cmd',
        ],
        instanceLatex: String.raw`\frac{\frac{}{\texttt{x := 0} \xrightarrow{\mathrm{true} : \texttt{x := 0}} \texttt{exit}}}{\texttt{x := 0 ; y := x ; loop\_cmd} \xrightarrow{\mathrm{true} : \texttt{x := 0}} \texttt{y := x ; loop\_cmd}}`,
      },
      {
        id: 'do-step-4',
        edgeId: 'do-e4',
        source: 'do-l0',
        target: 'do-l0',
        note: 'בענף הראשון של do הגוף מסיים מייד, ולכן כלל do מחזיר את הלולאה אל עצמה עם guard = x > 1.',
        ruleTitle: 'כלל do: גוף שמסתיים',
        ruleLines: [
          'אם stmt_i -- h : alpha --> exit',
          'אז loop_cmd -- (g_i && h) : alpha --> loop_cmd',
        ],
        ruleLatex: DO_FINISH_RULE_LATEX,
        instanceLines: [
          'y := x + y -- true : y := x + y --> exit',
          'l_0 -- x > 1 : y := x + y --> l_0',
        ],
        instanceLatex: String.raw`\frac{\frac{}{\texttt{y := x + y} \xrightarrow{\mathrm{true} : \texttt{y := x + y}} \texttt{exit}}}{\ell_0 \xrightarrow{x > 1 : \texttt{y := x + y}} \ell_0}`,
      },
      {
        id: 'do-step-5',
        edgeId: 'do-e5',
        source: 'do-l0',
        target: 'do-l3',
        note: 'בענף השני הגוף לא מסיים בצעד הראשון, ולכן כלל do שולח אותנו אל y := x ; loop_cmd.',
        ruleTitle: 'כלל do: גוף שלא הסתיים',
        ruleLines: [
          'אם stmt_i -- h : alpha --> stmt_i\' ו-stmt_i\' != exit',
          'אז loop_cmd -- (g_i && h) : alpha --> stmt_i\' ; loop_cmd',
        ],
        ruleLatex: DO_CONTINUE_RULE_LATEX,
        instanceLines: [
          'x := 0 ; y := x -- true : x := 0 --> y := x',
          'l_0 -- y < x : x := 0 --> l_3',
        ],
        instanceLatex: String.raw`\frac{\frac{\frac{}{\texttt{x := 0} \xrightarrow{\mathrm{true} : \texttt{x := 0}} \texttt{exit}}}{\texttt{x := 0 ; y := x} \xrightarrow{\mathrm{true} : \texttt{x := 0}} \texttt{y := x}}}{\ell_0 \xrightarrow{y < x : \texttt{x := 0}} \ell_3}`,
      },
      {
        id: 'do-step-6',
        edgeId: 'do-e6',
        source: 'do-l0',
        target: 'do-exit',
        note: 'לבסוף מוסיפים את כלל היציאה של do: אם אף guard לא מאופשר, יוצאים ל-exit.',
        ruleTitle: 'כלל יציאה מן do',
        ruleLines: [
          'loop_cmd -- (!(g_1) && ... && !(g_n)) : skip --> exit',
        ],
        ruleLatex: DO_EXIT_RULE_LATEX,
        instanceLines: [
          'l_0 -- !(x > 1) && !(y < x) : skip --> exit',
        ],
      },
    ],
  },
  'nested-if-do': {
    program: [
      'if',
      ':: y = 0 -> do',
      '             :: x < 3 -> x := x + 1',
      '           od',
      ':: true  -> skip',
      'fi',
    ],
    width: 560,
    height: 360,
    introNote: 'כאן יש שני מקומות שאינם נגישים מהמקום ההתחלתי: l_2 = skip ו-l_3 = x := x + 1 ; loop_cmd. למרות זאת, שניהם עדיין ב-Loc = sub(stmt).',
    introRuleLines: [
      'קודם גוזרים מעברים מתוך ה-do ומן ה-skip.',
      'רק אחר כך מפעילים את כלל if ומקבלים את המעברים מן המקום ההתחלתי.',
    ],
    states: [
      {
        id: 'nested-l0',
        shortLabel: 'l_0',
        locationText: 'if :: y = 0 -> do :: x < 3 -> x := x + 1 od :: true -> skip fi',
        reachableFromStart: true,
        x: 270,
        y: 58,
        width: 74,
        initial: true,
        initialDirection: 'top',
      },
      {
        id: 'nested-l1',
        shortLabel: 'l_1',
        locationText: 'do :: x < 3 -> x := x + 1 od',
        reachableFromStart: true,
        x: 116,
        y: 172,
        width: 74,
      },
      {
        id: 'nested-l2',
        shortLabel: 'l_2',
        locationText: 'skip',
        reachableFromStart: false,
        x: 476,
        y: 130,
        width: 74,
      },
      {
        id: 'nested-l3',
        shortLabel: 'l_3',
        locationText: 'x := x + 1 ; loop_cmd',
        reachableFromStart: false,
        x: 118,
        y: 318,
        width: 82,
      },
      {
        id: 'nested-exit',
        shortLabel: 'exit',
        locationText: 'exit',
        reachableFromStart: true,
        x: 388,
        y: 312,
        width: 74,
      },
    ],
    edges: [
      {
        id: 'nested-e1',
        source: 'nested-l2',
        target: 'nested-exit',
        graphLabel: '$true : skip$',
        previewLabel: '-- true : skip -->',
        actionWidth: 110,
        curve: 0.08,
        actionX: 10,
        actionY: -20,
      },
      {
        id: 'nested-e2',
        source: 'nested-l3',
        target: 'nested-l1',
        graphLabel: '$true : x := x + 1$',
        previewLabel: '-- true : x := x + 1 -->',
        actionWidth: 146,
        actionX: -36,
      },
      {
        id: 'nested-e3',
        source: 'nested-l1',
        target: 'nested-l1',
        graphLabel: '$x < 3 : x := x + 1$',
        previewLabel: '-- x < 3 : x := x + 1 -->',
        actionWidth: 162,
        loopDirection: '-150deg',
        loopRadius: 90,
        loopLabelRadius: 80,
        actionX: 20,
        actionY: -20,
      },
      {
        id: 'nested-e4',
        source: 'nested-l1',
        target: 'nested-exit',
        graphLabel: '$\\neg(x < 3) : skip$',
        previewLabel: '-- !(x < 3) : skip -->',
        actionWidth: 156,
        curve: 0.06,
        actionX: 0,
        actionY: 22,
      },
      {
        id: 'nested-e5',
        source: 'nested-l0',
        target: 'nested-exit',
        graphLabel: '$true : skip$',
        previewLabel: '-- true : skip -->',
        actionWidth: 116,
        curve: -0.28,
        actionX: 0,
        actionY: -12,
      },
      {
        id: 'nested-e6',
        source: 'nested-l0',
        target: 'nested-l1',
        graphLabel: '$x < 3 \\land y = 0 : \\\\ \\quad x := x + 1$',
        previewLabel: '-- x < 3 && y = 0 : x := x + 1 -->',
        actionWidth: 208,
        actionX: 8,
        actionY: -10,
      },
      {
        id: 'nested-e7',
        source: 'nested-l0',
        target: 'nested-exit',
        graphLabel: '$\\neg(x < 3) \\land y = 0 : skip$',
        previewLabel: '-- !(x < 3) && y = 0 : skip -->',
        actionWidth: 204,
        curve: 0.24,
        actionX: -10,
        actionY: 10,
      },
    ],
    steps: [
      {
        id: 'nested-step-1',
        edgeId: 'nested-e1',
        source: 'nested-l2',
        target: 'nested-exit',
        note: 'גם skip הוא מקום ב-Loc, אף על פי שלא נגיע אליו ישירות מן if. לכן גוזרים לו אקסיומה רגילה.',
        ruleTitle: 'אקסיומת skip',
        ruleLines: [
          'skip -- true : skip --> exit',
        ],
        ruleLatex: SKIP_RULE_LATEX,
        instanceLines: [
          'l_2 -- true : skip --> exit',
        ],
      },
      {
        id: 'nested-step-2',
        edgeId: 'nested-e2',
        source: 'nested-l3',
        target: 'nested-l1',
        note: 'המקום x := x + 1 ; loop_cmd אינו נגיש מן ההתחלה, אבל בכלל ההרכבה הסדרתית הוא עדיין מוליד מעבר ל-loop_cmd.',
        ruleTitle: 'הרכבה סדרתית',
        ruleLines: [
          'אם stmt_1 -- g : alpha --> exit',
          'אז stmt_1 ; stmt_2 -- g : alpha --> stmt_2',
        ],
        ruleLatex: SEQ_RULE_LATEX,
        instanceLines: [
          'x := x + 1 -- true : x := x + 1 --> exit',
          'x := x + 1 ; loop_cmd -- true : x := x + 1 --> loop_cmd',
        ],
      },
      {
        id: 'nested-step-3',
        edgeId: 'nested-e3',
        source: 'nested-l1',
        target: 'nested-l1',
        note: 'כאשר גוף ה-do מסיים בצעד הראשון, כלל do מחזיר אותנו ללולאה עצמה.',
        ruleTitle: 'כלל do: גוף שמסתיים',
        ruleLines: [
          'אם stmt_i -- h : alpha --> exit',
          'אז loop_cmd -- (g_i && h) : alpha --> loop_cmd',
        ],
        ruleLatex: DO_FINISH_RULE_LATEX,
        instanceLines: [
          'x := x + 1 -- true : x := x + 1 --> exit',
          'l_1 -- x < 3 : x := x + 1 --> l_1',
        ],
      },
      {
        id: 'nested-step-4',
        edgeId: 'nested-e4',
        source: 'nested-l1',
        target: 'nested-exit',
        note: 'מוסיפים גם את כלל היציאה מן do: כשה-guard היחיד שקרי, הלולאה מסתיימת.',
        ruleTitle: 'כלל יציאה מן do',
        ruleLines: [
          'loop_cmd -- (!(g_1) && ... && !(g_n)) : skip --> exit',
        ],
        ruleLatex: DO_EXIT_RULE_LATEX,
        instanceLines: [
          'l_1 -- !(x < 3) : skip --> exit',
        ],
      },
      {
        id: 'nested-step-5',
        edgeId: 'nested-e5',
        source: 'nested-l0',
        target: 'nested-exit',
        note: 'עכשיו if מרכיב את ענף skip: ה-guard של הענף הוא true, ולכן מתקבל מעבר ישיר מ-l_0 אל exit.',
        ruleTitle: 'כלל if',
        ruleLines: [
          'אם stmt_i -- h : alpha --> stmt_i\'',
          'אז cond_cmd -- (g_i && h) : alpha --> stmt_i\'',
        ],
        ruleLatex: IF_RULE_LATEX,
        instanceLines: [
          'skip -- true : skip --> exit',
          'l_0 -- true : skip --> exit',
        ],
      },
      {
        id: 'nested-step-6',
        edgeId: 'nested-e6',
        source: 'nested-l0',
        target: 'nested-l1',
        note: 'על הענף הראשון של if מחברים את guard y = 0 אל המעבר החוזר של do.',
        ruleTitle: 'כלל if',
        ruleLines: [
          'אם stmt_i -- h : alpha --> stmt_i\'',
          'אז cond_cmd -- (g_i && h) : alpha --> stmt_i\'',
        ],
        ruleLatex: IF_RULE_LATEX,
        instanceLines: [
          'l_1 -- x < 3 : x := x + 1 --> l_1',
          'l_0 -- x < 3 && y = 0 : x := x + 1 --> l_1',
        ],
      },
      {
        id: 'nested-step-7',
        edgeId: 'nested-e7',
        source: 'nested-l0',
        target: 'nested-exit',
        note: 'לבסוף, אותו ענף ראשון של if תורם גם מעבר יציאה כאשר ה-do מסתיים, ולכן מתקבלים שני מעברים שונים מ-l_0 אל exit.',
        ruleTitle: 'כלל if',
        ruleLines: [
          'אם stmt_i -- h : alpha --> stmt_i\'',
          'אז cond_cmd -- (g_i && h) : alpha --> stmt_i\'',
        ],
        ruleLatex: IF_RULE_LATEX,
        instanceLines: [
          'l_1 -- !(x < 3) : skip --> exit',
          'l_0 -- !(x < 3) && y = 0 : skip --> exit',
        ],
      },
    ],
  },
}
