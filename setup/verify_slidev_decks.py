from __future__ import annotations

import re
import sys
import unicodedata
import zipfile
from pathlib import Path

from generate_slidev_decks import (
    LECTURES,
    REPO_ROOT,
    get_first_pdf_lines,
    get_pdf_pages,
    get_pdf_page_count,
    normalize_text,
    parse_slide,
    slide_paths,
)


def normalize_compare(text: str) -> str:
    text = normalize_text(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*]\([^)]+\)", " ", text)
    text = re.sub(r"^[#>\-\+\*\s\\]+", "", text)
    text = re.sub(r"[`*_#>\[\]\(\)\{\}|\\]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def title_fragments(text: str) -> list[str]:
    text = normalize_text(text)
    parts = re.findall(r"[\u0590-\u05ff][\u0590-\u05ff\s\"'.,:;!?()\-/]*|[A-Za-z][A-Za-z0-9\s\"'.,:;!?()\-/]*", text)
    fragments = [normalize_loose(part) for part in parts]
    return [fragment for fragment in fragments if len(fragment) >= 3]


def normalize_loose(text: str) -> str:
    text = normalize_text(text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    text = re.sub(r"[^0-9A-Za-z\u0590-\u05ff\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def extract_markdown_slides(markdown_path: Path) -> list[str]:
    text = markdown_path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end == -1:
            raise ValueError(f"frontmatter not terminated in {markdown_path}")
        text = text[end + 5 :]
    slides = [part.strip() for part in re.split(r"(?m)^\s*---\s*$", text) if part.strip()]
    return slides


def extract_slide_blob(slide_markdown: str) -> str:
    lines = []
    for raw_line in slide_markdown.splitlines():
        line = normalize_text(raw_line)
        if not line:
            continue
        if line.startswith("<") and line.endswith(">"):
            continue
        if "Source slide from the lecture PDF." in line:
            continue
        lines.append(line)
    return normalize_compare(" ".join(lines))


def extract_image_pages(slide_markdown: str) -> list[int]:
    return [int(match.group(1)) for match in re.finditer(r"page-(\d+)\.jpg", slide_markdown)]


def verify_lecture(lecture) -> list[str]:
    issues: list[str] = []
    markdown_path = REPO_ROOT / lecture.output
    pdf_path = REPO_ROOT / lecture.pdf
    pptx_path = REPO_ROOT / lecture.pptx

    slides_md = extract_markdown_slides(markdown_path)
    pdf_lines = get_first_pdf_lines(pdf_path)
    pdf_pages = get_pdf_page_count(pdf_path)
    pdf_layout_pages = get_pdf_pages(pdf_path, "layout")

    with zipfile.ZipFile(pptx_path) as zf:
        ordered_paths = slide_paths(zf)
        if len(slides_md) != len(ordered_paths):
            issues.append(
                f"slide-count mismatch: markdown has {len(slides_md)} slides, pptx has {len(ordered_paths)}"
            )

        cover_md = extract_slide_blob(slides_md[0])
        cover_slide = parse_slide(zf, ordered_paths[0])
        cover_md_loose = normalize_loose(cover_md)
        for fragment in title_fragments(cover_slide["title"]):
            if fragment not in cover_md_loose:
                issues.append(f"cover slide is missing the PPT title fragment '{fragment}'")
        if pdf_lines:
            if normalize_compare(pdf_lines[0]) not in cover_md:
                issues.append("cover slide is missing the first PDF title line")
            if len(pdf_lines) > 1 and normalize_compare(pdf_lines[1]) not in cover_md:
                issues.append("cover slide is missing the second PDF title line")

        for slide_number, slide_path in enumerate(ordered_paths[1:], start=2):
            if slide_number - 1 >= len(slides_md):
                issues.append(f"slide {slide_number}: missing from markdown deck")
                continue

            ppt_slide = parse_slide(zf, slide_path)
            md_slide = slides_md[slide_number - 1]
            md_blob = extract_slide_blob(md_slide)
            image_pages = extract_image_pages(md_slide)
            pdf_layout_lines = pdf_layout_pages[slide_number - 1] if slide_number - 1 < len(pdf_layout_pages) else []

            if ppt_slide["title"] and normalize_compare(ppt_slide["title"]) not in md_blob:
                issues.append(f"slide {slide_number}: title mismatch")

            if image_pages:
                issues.append(f"slide {slide_number}: still contains embedded source slide image")
                continue

            missing_paragraphs = []
            for block in ppt_slide["blocks"]:
                for paragraph in block["paragraphs"]:
                    normalized = normalize_compare(paragraph["text"])
                    if normalized and normalized not in md_blob:
                        missing_paragraphs.append(paragraph["text"])
            if missing_paragraphs:
                sample = "; ".join(missing_paragraphs[:3])
                issues.append(f"slide {slide_number}: missing PPT text -> {sample}")

            if "לא אותר בשקף טקסט עריך" in md_slide:
                issues.append(f"slide {slide_number}: still contains generic non-editable placeholder text")

            if not ppt_slide["title"] and not ppt_slide["blocks"] and pdf_layout_lines and len(md_blob) < 20:
                issues.append(f"slide {slide_number}: expected textual content from the PDF but slide is almost empty")

    return issues


def main() -> int:
    failed = False
    for lecture in LECTURES:
        issues = verify_lecture(lecture)
        if issues:
            failed = True
            print(f"[FAIL] lecture {lecture.number}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"[OK] lecture {lecture.number}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
