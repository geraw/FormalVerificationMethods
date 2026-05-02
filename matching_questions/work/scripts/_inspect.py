from pathlib import Path
from docx import Document
from docx.oxml.ns import qn

ROOT = Path(r"C:\Users\geraw\courses\FormalVerificationMethods\matching_questions\work")
doc = Document(ROOT / "source.docx")

# Find Q6 area - look for PG paragraphs and question starts
for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if "PG" in text or text.startswith("6.") or text.startswith("7.") or text.startswith("1.") or text.startswith("2."):
        runs_info = [(r.text, r.font.size, r.font.name, r.font.bold) for r in para.runs]
        style = para.style.name if para.style else "?"
        print(f"[{i}] '{text[:60]}' style={style} runs={runs_info}")
