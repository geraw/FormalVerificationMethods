from __future__ import annotations

import argparse
import posixpath
import re
import subprocess
import textwrap
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass
from pathlib import Path

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Lecture:
    number: int
    pptx: str
    pdf: str
    output: str
    fallback_title: str
    book_ref: str


LECTURES: list[Lecture] = [
    Lecture(10, "PowerPointSlides/l10.pptx", "PowerPointSlides/l10.pdf", "07-state-explosion.md", "State Explosion Problem", "Principles of Model Checking, Section 2.3"),
    Lecture(11, "PowerPointSlides/l11.pptx", "PowerPointSlides/l11.pdf", "11-linear-time-properties.md", "Linear-Time Properties", "Principles of Model Checking, Section 3.2"),
    Lecture(12, "PowerPointSlides/l12.pptx", "PowerPointSlides/l12.pdf", "12-invariant-properties.md", "Invariant Properties", "Principles of Model Checking, Section 3.3.1"),
    Lecture(13, "PowerPointSlides/l13.pptx", "PowerPointSlides/l13.pdf", "13-safety-properties.md", "Safety Properties", "Principles of Model Checking, Section 3.3.2"),
    Lecture(14, "PowerPointSlides/l14.pptx", "PowerPointSlides/l14.pdf", "14-property-closure.md", "Property Closure", "Principles of Model Checking, Sections 3.3.2 and 3.4.2"),
    Lecture(15, "PowerPointSlides/l15.pptx", "PowerPointSlides/l15.pdf", "15-liveness-properties.md", "Liveness Properties", "Principles of Model Checking, Section 3.4"),
    Lecture(16, "PowerPointSlides/l16.pptx", "PowerPointSlides/l16.pdf", "16-fairness.md", "Fairness", "Principles of Model Checking, Section 3.5"),
    Lecture(17, "PowerPointSlides/l17.pptx", "PowerPointSlides/l17.pdf", "17-automata-and-formal-languages-review.md", "Review of Automata and Formal Languages", "Principles of Model Checking, Section 4.1"),
    Lecture(18, "PowerPointSlides/l18.pptx", "PowerPointSlides/l18.pdf", "18-regular-safety-properties.md", "Model-Checking Regular Safety Properties", "Principles of Model Checking, Section 4.2"),
    Lecture(19, "PowerPointSlides/L19.pptx", "PowerPointSlides/L19.pdf", "19-omega-regular-languages.md", "Omega-Regular Languages", "Principles of Model Checking, Sections 4.3.1-4.3.2"),
    Lecture(20, "PowerPointSlides/l20.pptx", "PowerPointSlides/l20.pdf", "20-deterministic-and-generalized-buchi-automata.md", "Deterministic and Generalized Buchi Automata", "Principles of Model Checking, Sections 4.3.3-4.3.4"),
    Lecture(21, "PowerPointSlides/l21.pptx", "PowerPointSlides/l21.pdf", "21-verification-of-omega-regular-properties.md", "Model-Checking Omega-Regular Properties", "Principles of Model Checking, Section 4.4"),
    Lecture(22, "PowerPointSlides/l22.pptx", "PowerPointSlides/l22.pdf", "22-ltl.md", "Linear Temporal Logic", "Principles of Model Checking, Section 5.1"),
    Lecture(23, "PowerPointSlides/l23.pptx", "PowerPointSlides/l23.pdf", "23-ltl-model-checking.md", "Automata-Based LTL Model Checking", "Principles of Model Checking, Section 5.2"),
    Lecture(24, "PowerPointSlides/l24.pptx", "PowerPointSlides/l24.pdf", "24-ctl.md", "CTL", "Principles of Model Checking, Sections 6.1-6.2"),
]


def normalize_text(text: str | None) -> str:
    if not text:
        return ""
    text = text.replace("\xa0", " ")
    text = re.sub(r"[\u200e\u200f\u202a-\u202e\u2066-\u2069]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_ignored_text(text: str) -> bool:
    text = normalize_text(text)
    if not text:
        return True
    if re.fullmatch(r"\d+", text):
        return True
    if re.fullmatch(r"[ivxlcdmIVXLCDM]+", text):
        return True
    if re.fullmatch(r"\d{1,2}\s+\S+\s+\d{2,4}", text):
        return True
    if re.fullmatch(r"\S+\s+\d{1,2},\s+\d{4}", text):
        return True
    if text.startswith("TeXPoint fonts used in EMF"):
        return True
    if text == "PowerPoint Presentation":
        return True
    return False


def is_metadata_line(text: str) -> bool:
    lowered = normalize_text(text).lower()
    if lowered in {
        "\u05d2\u05e8\u05d0 \u05d5\u05d9\u05d9\u05e1",
        "\u05d4\u05de\u05d7\u05dc\u05e7\u05d4 \u05dc\u05de\u05d3\u05e2\u05d9 \u05d4\u05de\u05d7\u05e9\u05d1",
        "\u05d0\u05d5\u05e0\u05d9\u05d1\u05e8\u05e1\u05d9\u05d8\u05ea \u05d1\u05df-\u05d2\u05d5\u05e8\u05d9\u05d5\u05df",
        "gra weiss",
    }:
        return True
    return any(token in lowered for token in ["department", "university", "faculty"])


def escape_markdown(text: str) -> str:
    text = normalize_text(text)
    if re.match(r"^(?:[#>*+-]|\d+\.)", text):
        text = "\\" + text
    text = text.replace("|", r"\|")
    text = text.replace("`", r"\`")
    return text


def comparison_key(text: str) -> str:
    text = normalize_text(text).lower()
    text = re.sub(r"[^0-9a-zA-Z\u0590-\u05ff]+", "", text)
    return text


def comparable_overlap(left: str, right: str, minimum: int = 5) -> bool:
    left_key = comparison_key(left)
    right_key = comparison_key(right)
    if len(left_key) < minimum or len(right_key) < minimum:
        return False
    return left_key in right_key or right_key in left_key


def run_command(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    return result.stdout


def get_pdf_page_count(pdf_path: Path) -> int | None:
    try:
        output = run_command(["pdfinfo", str(pdf_path)])
    except Exception:
        return None
    for line in output.splitlines():
        match = re.match(r"^Pages:\s+(\d+)$", line)
        if match:
            return int(match.group(1))
    return None


def get_first_pdf_lines(pdf_path: Path) -> list[str]:
    try:
        output = run_command(["pdftotext", "-f", "1", "-l", "1", "-layout", str(pdf_path), "-"])
    except Exception:
        return []
    lines: list[str] = []
    seen: set[str] = set()
    for raw_line in output.replace("\f", "\n").splitlines():
        line = normalize_text(raw_line)
        if is_ignored_text(line):
            continue
        if is_metadata_line(line):
            continue
        if line in seen:
            continue
        seen.add(line)
        lines.append(line)
    return lines[:5]


def get_cover_pdf_lines(pdf_path: Path) -> list[str]:
    try:
        output = run_command(["pdftotext", "-f", "1", "-l", "1", "-layout", str(pdf_path), "-"])
    except Exception:
        return []

    lines: list[str] = []
    seen: set[str] = set()
    for raw_line in output.replace("\f", "\n").splitlines():
        line = normalize_text(raw_line)
        if is_ignored_text(line):
            continue
        if line in seen:
            continue
        seen.add(line)
        lines.append(line)
    return lines


def get_pdf_pages(pdf_path: Path, mode: str = "layout") -> list[list[str]]:
    args = ["pdftotext"]
    if mode == "layout":
        args.append("-layout")
    elif mode == "raw":
        args.append("-raw")
    args.extend([str(pdf_path), "-"])
    try:
        output = run_command(args)
    except Exception:
        return []

    pages: list[list[str]] = []
    for page in output.split("\f"):
        lines: list[str] = []
        seen: set[str] = set()
        for raw_line in page.splitlines():
            line = normalize_text(raw_line)
            if is_ignored_text(line):
                continue
            if is_metadata_line(line):
                continue
            if line in seen:
                continue
            seen.add(line)
            lines.append(line)
        if lines:
            pages.append(lines)
    return pages


def relmap(zf: zipfile.ZipFile, rels_path: str) -> dict[str, str]:
    try:
        root = ET.fromstring(zf.read(rels_path))
    except KeyError:
        return {}
    return {rel.attrib["Id"]: rel.attrib["Target"] for rel in root}


def slide_paths(zf: zipfile.ZipFile) -> list[str]:
    pres = ET.fromstring(zf.read("ppt/presentation.xml"))
    pres_rels = relmap(zf, "ppt/_rels/presentation.xml.rels")
    result: list[str] = []
    for slide_id in pres.find("p:sldIdLst", NS):
        rid = slide_id.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
        result.append(posixpath.normpath(posixpath.join("ppt", pres_rels[rid])))
    return result


def get_rel_media_count(zf: zipfile.ZipFile, slide_path: str) -> int:
    rels_path = slide_path.replace("slides/slide", "slides/_rels/slide").replace(".xml", ".xml.rels")
    rels = relmap(zf, rels_path)
    return sum(1 for target in rels.values() if "/media/" in target or target.startswith("../media/"))


def parse_position(shape: ET.Element) -> tuple[int, int]:
    xfrm = shape.find("p:spPr/a:xfrm", NS)
    if xfrm is None:
        xfrm = shape.find("p:grpSpPr/a:xfrm", NS)
    if xfrm is None:
        return (10**12, 10**12)
    return (int(xfrm.attrib.get("y", "0")), int(xfrm.attrib.get("x", "0")))


def parse_shape_block(shape: ET.Element) -> dict | None:
    placeholder = shape.find("p:nvSpPr/p:nvPr/p:ph", NS)
    ph_type = placeholder.attrib.get("type", "") if placeholder is not None else ""
    top, left = parse_position(shape)
    paragraphs = []
    for paragraph in shape.findall("p:txBody/a:p", NS):
        ppr = paragraph.find("a:pPr", NS)
        level = int(ppr.attrib.get("lvl", "0")) + 1 if ppr is not None else 1
        text = normalize_text("".join(t.text or "" for t in paragraph.findall(".//a:t", NS)))
        if text and not is_ignored_text(text):
            paragraphs.append({"text": text, "level": max(level, 1)})
    if not paragraphs:
        return None
    block_text = " ".join(item["text"] for item in paragraphs).strip()
    return {
        "placeholder": ph_type,
        "top": top,
        "left": left,
        "paragraphs": paragraphs,
        "text": block_text,
        "char_count": len(block_text),
    }


def parse_slide(zf: zipfile.ZipFile, slide_path: str) -> dict:
    root = ET.fromstring(zf.read(slide_path))
    blocks = []
    title = ""
    for shape in root.findall(".//p:sp", NS):
        block = parse_shape_block(shape)
        if not block:
            continue
        if block["placeholder"] in {"title", "ctrTitle"} and not title:
            title = block["text"]
            continue
        blocks.append(block)

    blocks.sort(key=lambda item: (item["top"], item["left"]))
    if not title and blocks:
        first = blocks[0]
        if len(first["text"]) <= 90:
            title = first["text"]
            remainder = first["paragraphs"][1:]
            if remainder:
                first["paragraphs"] = remainder
                first["text"] = " ".join(item["text"] for item in remainder).strip()
                first["char_count"] = len(first["text"])
            else:
                blocks.pop(0)

    media_count = get_rel_media_count(zf, slide_path)
    total_chars = sum(block["char_count"] for block in blocks)
    paragraph_count = sum(len(block["paragraphs"]) for block in blocks)
    short_blocks = sum(1 for block in blocks if block["char_count"] <= 36)
    avg_block_chars = total_chars / len(blocks) if blocks else 0

    diagram_like = (len(blocks) >= 6 and avg_block_chars <= 30) or short_blocks >= 6
    figure_only = (diagram_like and len(blocks) >= 8) or (total_chars < 50 and media_count >= 2)
    use_figure = figure_only or (media_count >= 2 and total_chars <= 260) or diagram_like or (paragraph_count <= 2 and media_count >= 1)

    if not blocks:
        use_figure = True
        figure_only = True

    return {
        "title": title,
        "blocks": blocks,
        "media_count": media_count,
        "use_figure": use_figure,
        "figure_only": figure_only,
    }


def format_bullet_blocks(blocks: list[dict]) -> str:
    lines: list[str] = []
    for block in blocks:
        for paragraph in block["paragraphs"]:
            indent = "  " * max(paragraph["level"] - 1, 0)
            lines.append(f"{indent}- {escape_markdown(paragraph['text'])}")
        if len(block["paragraphs"]) > 1:
            lines.append("")
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def flatten_block_paragraphs(blocks: list[dict]) -> list[dict]:
    return [paragraph for block in blocks for paragraph in block["paragraphs"]]


def format_bullet_lines(lines: list[str], level: int = 1) -> str:
    items = []
    indent = "  " * max(level - 1, 0)
    for line in lines:
        items.append(f"{indent}- {escape_markdown(line)}")
    return "\n".join(items)


def line_looks_formal(line: str) -> bool:
    if "???" in line:
        return False
    has_latin = bool(re.search(r"[A-Za-z]", line))
    has_math = bool(re.search(r"[=<>∈∀∃∧∨¬→↔⇔⇕⊆⊂⊇∪∩ℒ𝒜𝜔𝛿𝜑𝜓𝑄𝐺𝐹𝐴𝑈𝑋{}()\[\]]", line))
    return has_latin or has_math


def extract_layout_supplement(lines: list[str], known_keys: set[str], title: str) -> list[str]:
    supplements: list[str] = []
    title_key = comparison_key(title)
    for line in lines:
        key = comparison_key(line)
        if not key or key in known_keys or key == title_key:
            continue
        if line_looks_formal(line):
            continue
        if len(line) < 3:
            continue
        supplements.append(line)
        known_keys.add(key)
    return supplements


def extract_formal_supplement(lines: list[str], known_keys: set[str]) -> list[str]:
    supplements: list[str] = []
    seen: set[str] = set()
    for line in lines:
        key = comparison_key(line)
        if not key or key in known_keys or key in seen:
            continue
        if not line_looks_formal(line):
            continue
        if len(line.split()) == 1 and not re.search(r"[=<>∈∀∃∧∨¬→↔⇔⊆⊂⊇∪∩]", line):
            continue
        seen.add(key)
        supplements.append(line)
    return supplements[:10]


def pdf_page_matches_slide(layout_lines: list[str], title: str, blocks: list[dict]) -> bool:
    if not layout_lines:
        return False

    references = [title] if title else []
    references.extend(paragraph["text"] for paragraph in flatten_block_paragraphs(blocks))
    references = [reference for reference in references if comparison_key(reference)]
    if not references:
        return True

    if title and any(comparable_overlap(title, line) for line in layout_lines):
        return True

    overlap_count = 0
    for reference in references[:6]:
        if any(comparable_overlap(reference, line) for line in layout_lines):
            overlap_count += 1

    return overlap_count >= 2


def add_text_block(parts: list[str], body: str, dimmed: bool = False) -> None:
    if not body:
        return
    opacity = " opacity-75" if dimmed else ""
    parts.append(f'<div class="text-right text-[15px] leading-snug{opacity}">')
    parts.append(body)
    parts.append("</div>")


def add_formal_block(parts: list[str], lines: list[str]) -> None:
    if not lines:
        return
    parts.append("```text")
    parts.extend(lines)
    parts.append("```")


def frontmatter(lecture: Lecture, cover_title: str) -> str:
    return textwrap.dedent(
        f"""\
        ---
        theme: academic
        dir: rtl
        class: text-center
        highlighter: shiki
        lineNumbers: true
        htmlAttrs:
          dir: rtl
          lang: heb
        drawings:
          enabled: true
        ---
        """
    ).rstrip()


def cover_slide(title: str, cover_lines: list[str]) -> str:
    lines = [f"# {title}"]
    if cover_lines:
        subtitle_lines: list[str] = []
        body_lines: list[str] = []
        metadata_started = False
        for line in cover_lines:
            if is_metadata_line(line):
                metadata_started = True
            if metadata_started:
                body_lines.append(line)
            else:
                subtitle_lines.append(line)

        if subtitle_lines:
            lines.append("")
            lines.extend(f"## {line}" for line in subtitle_lines)
        if body_lines:
            lines.append("")
            lines.extend(body_lines)
    return "\n".join(lines)


def deck_style() -> str:
    return textwrap.dedent(
        """\
        <style>
        </style>
        """
    ).rstrip()


def build_deck(lecture: Lecture) -> None:
    pptx_path = REPO_ROOT / lecture.pptx
    pdf_path = REPO_ROOT / lecture.pdf
    output_path = REPO_ROOT / lecture.output

    pdf_lines = get_first_pdf_lines(pdf_path)
    cover_lines = get_cover_pdf_lines(pdf_path)
    pdf_layout_pages = get_pdf_pages(pdf_path, "layout")
    pdf_raw_pages = get_pdf_pages(pdf_path, "raw")
    cover_title = cover_lines[0] if cover_lines else (pdf_lines[0] if pdf_lines else lecture.fallback_title)
    cover_rest = cover_lines[1:] if len(cover_lines) > 1 else []
    pdf_pages = get_pdf_page_count(pdf_path)

    parts: list[str] = [frontmatter(lecture, cover_title), "", cover_slide(cover_title, cover_rest)]

    with zipfile.ZipFile(pptx_path) as zf:
        ordered_paths = slide_paths(zf)
        if pdf_pages and pdf_pages != len(ordered_paths):
            print(f"warning: lecture {lecture.number} has {len(ordered_paths)} slides in PPTX but {pdf_pages} pages in PDF")

        for slide_number, slide_path in enumerate(ordered_paths[1:], start=2):
            slide = parse_slide(zf, slide_path)
            layout_lines = pdf_layout_pages[slide_number - 1] if slide_number - 1 < len(pdf_layout_pages) else []
            raw_lines = pdf_raw_pages[slide_number - 1] if slide_number - 1 < len(pdf_raw_pages) else []

            flattened = flatten_block_paragraphs(slide["blocks"])
            title = slide["title"]
            page_matches = pdf_page_matches_slide(layout_lines, title, slide["blocks"])
            if not page_matches:
                layout_lines = []
                raw_lines = []
            elif not title and layout_lines:
                title = layout_lines[0]
            body = format_bullet_blocks(slide["blocks"])
            known_keys = {comparison_key(title)}
            known_keys.update(comparison_key(paragraph["text"]) for paragraph in flattened)

            layout_supplement = extract_layout_supplement(layout_lines, known_keys, title)
            formal_supplement = extract_formal_supplement(raw_lines, known_keys)

            if not body and layout_supplement:
                body = format_bullet_lines(layout_supplement)
                layout_supplement = []

            parts.extend(["", "---", ""])

            if title:
                parts.extend([f"# {escape_markdown(title)}", ""])

            if layout_supplement:
                layout_body = format_bullet_lines(layout_supplement)
                body = f"{body}\n\n{layout_body}" if body else layout_body

            if body:
                add_text_block(parts, body)
            if formal_supplement:
                parts.append("")
                add_formal_block(parts, formal_supplement)
            if not title and not body and not formal_supplement:
                parts.append("<div></div>")

    parts.extend(["", deck_style()])
    output_path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lectures", nargs="*", type=int, help="Lecture numbers to generate")
    args = parser.parse_args()

    selected = LECTURES
    if args.lectures:
        wanted = set(args.lectures)
        selected = [lecture for lecture in LECTURES if lecture.number in wanted]

    for lecture in selected:
        print(f"Generating {lecture.output}...")
        build_deck(lecture)


if __name__ == "__main__":
    main()
