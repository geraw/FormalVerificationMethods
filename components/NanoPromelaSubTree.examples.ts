export type ExampleKey = 'if-basic' | 'do-basic' | 'nested-if-do'

export type SubBox = {
  x: number
  y: number
  width: number
  lines: string[]
  placement?: 'absolute' | 'above-node'
}

export type TreeNode = {
  id: string
  lines: string[]
  x: number
  y: number
  width: number
  step: number
  sub?: SubBox
}

export type TreeEdge = {
  from: string
  to: string
  label: string
  labelX: number
  labelY: number
}

export type StepRule = {
  title: string
  lines: string[]
}

export type Example = {
  program: string[]
  width: number
  height: number
  maxSteps: number
  notes: Record<number, string>
  rules: Record<number, StepRule>
  nodes: TreeNode[]
  edges: TreeEdge[]
}

export const examples: Record<ExampleKey, Example> = {
  'if-basic': {
    program: [
      'if',
      ':: x > 1 -> y := x + y',
      ':: true  -> x := 0; y := x',
      'fi',
    ],
    width: 700,
    height: 285,
    maxSteps: 5,
    notes: {
      0: 'מתחילים מן העלים. בכל צעד נחשף ה-sub של צומת אחד, והוא נשאר ליד הצומת גם בהמשך.',
      1: 'לעלה y := x + y מפעילים את מקרה הבסיס, ולכן ה-sub שלו הוא רק הוא עצמו יחד עם exit.',
      2: 'כעת גם לעלה x := 0 יש sub משלו, ועדיין ההרכבה מעליו טרם חושבה.',
      3: 'הבן השני של ההרכבה, y := x, מצטרף גם הוא עם sub בסיסי משלו.',
      4: 'עכשיו אפשר לטפס להורה עם כלל ההרכבה הסדרתית: sub של שני הבנים משולב ל-sub של x := 0 ; y := x.',
      5: 'לבסוף מפעילים את ההגדרה של if: מאחדים את שני הענפים ומוסיפים cond_cmd.',
    },
    rules: {
      0: {
        title: 'כיוון העבודה',
        lines: ['מתקדמים מן העלים כלפי מעלה.'],
      },
      1: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      2: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      3: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      4: {
        title: 'הרכבה סדרתית',
        lines: ['sub(stmt1 ; stmt2) = { stmt1 ; stmt2 } ∪ (sub(stmt1) \\ {exit}) ∪ sub(stmt2)'],
      },
      5: {
        title: 'כלל if',
        lines: ['sub(if ... fi) = { cond_cmd } ∪ ⋃_i sub(stmt_i)'],
      },
    },
    nodes: [
      {
        id: 'if-root',
        lines: ['if ... fi'],
        x: 350,
        y: 58,
        width: 148,
        step: 5,
        sub: {
          x: 224,
          y: 58,
          width: 100,
          placement: 'absolute',
          lines: [
            'sub = {',
            '  cond_cmd,',
            '  y := x + y,',
            '  x := 0 ; y := x,',
            '  y := x, exit',
            '}',
          ],
        },
      },
      {
        id: 'if-left',
        lines: ['y := x + y'],
        x: 180,
        y: 188,
        width: 138,
        step: 1,
        sub: {
          x: 104,
          y: 132,
          width: 170,
          lines: ['sub = {', '  y := x + y,', '  exit', '}'],
        },
      },
      {
        id: 'if-seq',
        lines: ['x := 0 ; y := x'],
        x: 520,
        y: 166,
        width: 172,
        step: 4,
        sub: {
          x: 590,
          y: 94,
          width: 190,
          lines: ['sub = {', '  x := 0 ; y := x,', '  y := x, exit', '}'],
        },
      },
      {
        id: 'if-x0',
        lines: ['x := 0'],
        x: 405,
        y: 258,
        width: 108,
        step: 2,
        sub: {
          x: 315,
          y: 236,
          width: 150,
          lines: ['sub = {', '  x := 0,', '  exit', '}'],
        },
      },
      {
        id: 'if-yx',
        lines: ['y := x'],
        x: 540,
        y: 258,
        width: 108,
        step: 3,
        sub: {
          x: 654,
          y: 236,
          width: 142,
          lines: ['sub = {', '  y := x,', '  exit', '}'],
        },
      },
    ],
    edges: [
      { from: 'if-root', to: 'if-left', label: 'x > 1', labelX: 246, labelY: 116 },
      { from: 'if-root', to: 'if-seq', label: 'true', labelX: 452, labelY: 104 },
      { from: 'if-seq', to: 'if-x0', label: 'stmt1', labelX: 445, labelY: 214 },
      { from: 'if-seq', to: 'if-yx', label: 'stmt2', labelX: 566, labelY: 214 },
    ],
  },
  'do-basic': {
    program: [
      'do',
      ':: x > 1 -> y := x + y',
      ':: y < x -> x := 0; y := x',
      'od',
    ],
    width: 700,
    height: 295,
    maxSteps: 5,
    notes: {
      0: 'עד שלב 4 העץ דומה לדוגמת if, אבל בצעד האחרון נראה שהאופרטור do מייצר sub שונה לגמרי.',
      1: 'העלה y := x + y תורם sub בסיסי משלו.',
      2: 'גם ל-x := 0 יש sub בסיסי, שעדיין לא הומר ל-loop.',
      3: 'גם ל-y := x יש sub בסיסי. שלושת ה-sub-ים של העלים נשארים גלויים על המסך.',
      4: 'כמו קודם, קודם בונים את sub של x := 0 ; y := x לפי כלל ההרכבה הסדרתית.',
      5: 'רק בשורש do מחברים לכל תת-פקודה לא-סופית את ; loop_cmd ומוסיפים loop_cmd, exit.',
    },
    rules: {
      0: {
        title: 'כיוון העבודה',
        lines: ['מתקדמים מן העלים כלפי מעלה.'],
      },
      1: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      2: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      3: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      4: {
        title: 'הרכבה סדרתית',
        lines: ['sub(stmt1 ; stmt2) = { stmt1 ; stmt2 } ∪ (sub(stmt1) \\ {exit}) ∪ sub(stmt2)'],
      },
      5: {
        title: 'כלל do',
        lines: [
          'sub(do ... od) = { loop_cmd, exit }',
          '                 ∪ ⋃_i { stmt ; loop_cmd | stmt ∈ sub(stmt_i) \\ {exit} }',
        ],
      },
    },
    nodes: [
      {
        id: 'do-root',
        lines: ['do ... od'],
        x: 350,
        y: 58,
        width: 148,
        step: 5,
        sub: {
          x: 176,
          y: 66,
          width: 224,
          placement: 'absolute',
          lines: [
            'sub = {',
            '  loop_cmd, exit,',
            '  y := x + y ; loop_cmd,',
            '  x := 0 ; y := x ; loop_cmd,',
            '  y := x ; loop_cmd',
            '}',
          ],
        },
      },
      {
        id: 'do-left',
        lines: ['y := x + y'],
        x: 180,
        y: 192,
        width: 138,
        step: 1,
        sub: {
          x: 102,
          y: 136,
          width: 170,
          lines: ['sub = {', '  y := x + y,', '  exit', '}'],
        },
      },
      {
        id: 'do-seq',
        lines: ['x := 0 ; y := x'],
        x: 520,
        y: 170,
        width: 172,
        step: 4,
        sub: {
          x: 592,
          y: 96,
          width: 190,
          lines: ['sub = {', '  x := 0 ; y := x,', '  y := x, exit', '}'],
        },
      },
      {
        id: 'do-x0',
        lines: ['x := 0'],
        x: 405,
        y: 266,
        width: 108,
        step: 2,
        sub: {
          x: 316,
          y: 242,
          width: 148,
          lines: ['sub = {', '  x := 0,', '  exit', '}'],
        },
      },
      {
        id: 'do-yx',
        lines: ['y := x'],
        x: 590,
        y: 266,
        width: 108,
        step: 3,
        sub: {
          x: 654,
          y: 242,
          width: 142,
          lines: ['sub = {', '  y := x,', '  exit', '}'],
        },
      },
    ],
    edges: [
      { from: 'do-root', to: 'do-left', label: 'x > 1', labelX: 246, labelY: 118 },
      { from: 'do-root', to: 'do-seq', label: 'y < x', labelX: 454, labelY: 108 },
      { from: 'do-seq', to: 'do-x0', label: 'stmt1', labelX: 446, labelY: 220 },
      { from: 'do-seq', to: 'do-yx', label: 'stmt2', labelX: 568, labelY: 220 },
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
    width: 700,
    height: 265,
    maxSteps: 4,
    notes: {
      0: 'בקינון, ה-sub של הילד do נבנה קודם ורק אחר כך עובר להורה if.',
      1: 'העלה x := x + 1 מקבל sub בסיסי, כמו כל פקודה אטומית.',
      2: 'כעת do בונה sub חדש מן הילד שלו: הוא מוסיף loop_cmd ויוצר x := x + 1 ; loop_cmd.',
      3: 'גם לענף השני של if, כלומר skip, יש sub בסיסי משלו.',
      4: 'לבסוף if מאחד את sub של do עם sub של skip, ומוסיף cond_cmd.',
    },
    rules: {
      0: {
        title: 'כיוון העבודה',
        lines: ['קודם מחשבים את sub של do, ורק אחר כך של if.'],
      },
      1: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      2: {
        title: 'כלל do',
        lines: [
          'sub(do ... od) = { loop_cmd, exit }',
          '                 ∪ ⋃_i { stmt ; loop_cmd | stmt ∈ sub(stmt_i) \\ {exit} }',
        ],
      },
      3: {
        title: 'מקרה בסיס',
        lines: ['sub(cmd) = { cmd, exit }'],
      },
      4: {
        title: 'כלל if',
        lines: ['sub(if ... fi) = { cond_cmd } ∪ ⋃_i sub(stmt_i)'],
      },
    },
    nodes: [
      {
        id: 'nested-root',
        lines: ['if ... fi'],
        x: 350,
        y: 54,
        width: 146,
        step: 4,
        sub: {
          x: 520,
          y: 60,
          width: 190,
          placement: 'absolute',
          lines: [
            'sub = {',
            '  cond_cmd,',
            '  loop_cmd,',
            '  x := x + 1 ; loop_cmd,',
            '  skip, exit',
            '}',
          ],
        },
      },
      {
        id: 'nested-do',
        lines: ['do ... od'],
        x: 220,
        y: 160,
        width: 146,
        step: 2,
        sub: {
          x: 96,
          y: 162,
          width: 162,
          lines: ['sub = { loop_cmd, exit,', '        x := x + 1 ; loop_cmd }'],
        },
      },
      {
        id: 'nested-assign',
        lines: ['x := x + 1'],
        x: 220,
        y: 248,
        width: 136,
        step: 1,
        sub: {
          x: 96,
          y: 244,
          width: 150,
          lines: ['sub = { x := x + 1, exit }'],
        },
      },
      {
        id: 'nested-skip',
        lines: ['skip'],
        x: 488,
        y: 192,
        width: 102,
        step: 3,
        sub: {
          x: 608,
          y: 190,
          width: 128,
          lines: ['sub = { skip, exit }'],
        },
      },
    ],
    edges: [
      { from: 'nested-root', to: 'nested-do', label: 'y = 0', labelX: 260, labelY: 98 },
      { from: 'nested-root', to: 'nested-skip', label: 'true', labelX: 444, labelY: 118 },
      { from: 'nested-do', to: 'nested-assign', label: 'x < 3', labelX: 266, labelY: 208 },
    ],
  },
}
