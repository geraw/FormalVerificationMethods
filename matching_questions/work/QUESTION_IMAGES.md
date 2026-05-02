# Question Image Workflow

Edit question text only in `source.docx`. Do not regenerate or rewrite Word text
from scripts after manual edits in Word.

Edit diagrams only in `tex/*.tex`, using the `qNN_...tex` naming convention.
Then run:

```powershell
python .\scripts\update_question_images.py
```

`update_question_images.py` only refreshes diagram images. It should not change
question wording or answer labels. The helper scripts that used to rewrite Word
text are intentionally disabled.

Common TeX files such as `q09_option_common.tex` and `q10_option_common.tex`
compile directly as preview sheets with all answer options together. The
individual `qNN_option_*.tex` files still control the exact answer-option images
embedded in Word.

The script compiles every TeX file to PDF, converts the PDF to vector SVG, and
also creates high-resolution PNG files. The Word document embeds PNG files for
Tomax/Word compatibility; the SVG/PDF files remain available as vector source
artifacts. LaTeX build products are kept in `build/`.

Image map:

- `q01_transition_systems_vs_program_graphs.tex` -> question 1 diagram
- `q02_interleaving_with_handshake.tex` -> question 2 diagram
- `q03_logic_circuits_transition_systems.tex` -> question 3 diagram
- `q04_nanopromela_unfolding.tex` -> question 4 shared option source
- `q04_option_a.tex` -> question 4 answer option A
- `q04_option_b.tex` -> question 4 answer option B
- `q04_option_c.tex` -> question 4 answer option C
- `q04_option_d.tex` -> question 4 answer option D
- `q04_option_e.tex` -> question 4 answer option E
- `q04_option_f.tex` -> question 4 answer option F
- `q05_async_channel_system.tex` -> question 5 diagram
- `q06_alt_nanopromela_rules.tex` -> question 6 rules
- `q06_alt_nanopromela_program_graphs.tex` -> question 6 shared overview source
- `q06_option_a.tex` -> question 6 answer option A
- `q06_option_b.tex` -> question 6 answer option B
- `q06_option_c.tex` -> question 6 answer option C
- `q06_option_d.tex` -> question 6 answer option D
- `q06_option_e.tex` -> question 6 answer option E
- `q06_option_f.tex` -> question 6 answer option F
- `q07_traffic_controller_safety.tex` -> question 7 controller
- `q08_traffic_controller_neither.tex` -> question 8 controller
- `q09_rules.tex` -> question 9 derivation rules
- `q09_ts_input.tex` -> question 9 input transition systems
- `q09_option_a.tex` -> question 9 answer option A
- `q09_option_b.tex` -> question 9 answer option B
- `q09_option_c.tex` -> question 9 answer option C
- `q09_option_d.tex` -> question 9 answer option D
- `q09_option_e.tex` -> question 9 answer option E
- `q09_option_f.tex` -> question 9 answer option F
- `q10_rules.tex` -> question 10 derivation rules
- `q10_ts_input.tex` -> question 10 input transition systems
- `q10_option_a.tex` -> question 10 answer option A
- `q10_option_b.tex` -> question 10 answer option B
- `q10_option_c.tex` -> question 10 answer option C
- `q10_option_d.tex` -> question 10 answer option D
- `q10_option_e.tex` -> question 10 answer option E
- `q10_option_f.tex` -> question 10 answer option F
