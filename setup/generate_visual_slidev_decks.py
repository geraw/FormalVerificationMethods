from __future__ import annotations

import argparse
import gc
import html
import re
import shutil
import tempfile
import time
from pathlib import Path

import pythoncom
import pywintypes
import win32com.client

from generate_slidev_decks import LECTURES, REPO_ROOT, normalize_text

POWERPOINT_GROUP = 6
POWERPOINT_TABLE = 19
EXPORT_SCALE = 2
TEXPOINT_PREFIX = "TexPoint fonts used in EMF."
PUBLIC_ROOT = REPO_ROOT / "public"
BACKGROUND_ROOT = PUBLIC_ROOT / "slide-backgrounds"
REFERENCE_ROOT = PUBLIC_ROOT / "slide-reference"


def sanitize_lines(text: str) -> str:
    text = text.replace("\x0b", "\n").replace("\r", "\n")
    text = re.sub(r"\n+", "\n", text)
    lines = [normalize_text(line) for line in text.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def keep_text_shape(text: str) -> bool:
    clean = sanitize_lines(text)
    if not clean:
        return False
    if clean.startswith(TEXPOINT_PREFIX):
        return False
    return True


def has_hebrew(text: str) -> bool:
    return bool(re.search(r"[\u0590-\u05ff]", text))


def rgb_to_hex(rgb_value: int | float | None) -> str | None:
    if rgb_value in (None, -2147483648):
        return None
    value = int(rgb_value) & 0xFFFFFF
    red = value & 0xFF
    green = (value >> 8) & 0xFF
    blue = (value >> 16) & 0xFF
    return f"#{red:02x}{green:02x}{blue:02x}"


def to_percent(value: float, total: float) -> str:
    if not total:
        return "0%"
    return f"{(value / total) * 100:.4f}%"


def font_weight(value) -> str:
    return "700" if value in (-1, True) else "400"


def font_style(value) -> str:
    return "italic" if value in (-1, True) else "normal"


def alignment_to_css(value) -> str:
    mapping = {
        1: "left",
        2: "center",
        3: "right",
        4: "justify",
        5: "distribute",
    }
    return mapping.get(value, "right")


def vertical_alignment(shape_name: str, anchor_value) -> str:
    if "Title" in shape_name or "Subtitle" in shape_name:
        return "center"
    mapping = {
        1: "flex-start",
        2: "center",
        3: "center",
        4: "flex-end",
    }
    return mapping.get(anchor_value, "flex-start")


def border_radius(shape_name: str) -> str | None:
    if "Oval" in shape_name:
        return "9999px"
    if "Rounded" in shape_name:
        return "16px"
    return None


def render_text_content(shape) -> str:
    paragraphs = shape.TextFrame.TextRange.Paragraphs()
    lines: list[str] = []
    for index in range(1, paragraphs.Count + 1):
        paragraph = shape.TextFrame.TextRange.Paragraphs(index, 1)
        paragraph_text = sanitize_lines(paragraph.Text)
        if not paragraph_text:
            continue
        try:
            indent_level = max(int(paragraph.IndentLevel) - 1, 0)
        except Exception:
            indent_level = 0
        bullet_prefix = ""
        try:
            if paragraph.ParagraphFormat.Bullet.Visible != 0:
                bullet_prefix = "• "
        except Exception:
            bullet_prefix = ""
        prefix = "  " * indent_level + bullet_prefix
        for offset, line in enumerate(paragraph_text.splitlines()):
            line_prefix = prefix if offset == 0 else "  " * indent_level
            lines.append(f"{line_prefix}{line}")
    return "\n".join(lines)


def shape_fill_style(shape) -> str | None:
    try:
        if shape.Fill.Visible == 0:
            return None
        color = rgb_to_hex(shape.Fill.ForeColor.RGB)
        if not color:
            return None
        transparency = 0.0
        try:
            transparency = float(shape.Fill.Transparency)
        except Exception:
            transparency = 0.0
        opacity = max(0.0, min(1.0, 1.0 - transparency))
        return f"background:{color};opacity:{opacity:.3f};"
    except Exception:
        return None


def shape_line_style(shape) -> str | None:
    try:
        if shape.Line.Visible == 0:
            return None
        color = rgb_to_hex(shape.Line.ForeColor.RGB)
        if not color:
            return None
        weight = 1.0
        try:
            weight = float(shape.Line.Weight)
        except Exception:
            weight = 1.0
        return f"border:{weight:.2f}px solid {color};"
    except Exception:
        return None


def render_text_shape(shape, slide_width: float, slide_height: float) -> str:
    raw_text = shape.TextFrame.TextRange.Text
    text = render_text_content(shape)
    if not keep_text_shape(raw_text) or not text:
        return ""

    try:
        font = shape.TextFrame.TextRange.Font
    except Exception:
        font = None

    font_name = ""
    font_size = 20.0
    font_color = "#222222"
    bold = False
    italic = False
    if font is not None:
        try:
            font_name = font.Name or ""
        except Exception:
            font_name = ""
        try:
            font_size = float(font.Size or 20.0)
        except Exception:
            font_size = 20.0
        try:
            font_color = rgb_to_hex(font.Color.RGB) or font_color
        except Exception:
            pass
        try:
            bold = font.Bold in (-1, True)
        except Exception:
            bold = False
        try:
            italic = font.Italic in (-1, True)
        except Exception:
            italic = False

    try:
        alignment = alignment_to_css(shape.TextFrame.TextRange.ParagraphFormat.Alignment)
    except Exception:
        alignment = "right" if has_hebrew(text) else "left"
    direction = "rtl" if has_hebrew(text) else "ltr"
    justify = vertical_alignment(shape.Name, getattr(shape.TextFrame, "VerticalAnchor", None))
    fill_style = shape_fill_style(shape) or ""
    line_style = shape_line_style(shape) or ""
    radius = border_radius(shape.Name)
    radius_style = f"border-radius:{radius};" if radius else ""
    rotation = ""
    try:
        if abs(float(shape.Rotation)) > 0.1:
            rotation = f"transform:rotate({float(shape.Rotation):.2f}deg);transform-origin:center;"
    except Exception:
        rotation = ""

    outer_style = (
        f"left:{to_percent(shape.Left, slide_width)};"
        f"top:{to_percent(shape.Top, slide_height)};"
        f"width:{to_percent(shape.Width, slide_width)};"
        f"height:{to_percent(shape.Height, slide_height)};"
        f"padding:{shape.TextFrame.MarginTop:.2f}pt {shape.TextFrame.MarginRight:.2f}pt "
        f"{shape.TextFrame.MarginBottom:.2f}pt {shape.TextFrame.MarginLeft:.2f}pt;"
        f"justify-content:{justify};"
        f"text-align:{alignment};"
        f"direction:{direction};"
        f"{fill_style}{line_style}{radius_style}{rotation}"
    )
    inner_style = (
        f"font-family:'{font_name or 'Gisha'}','Segoe UI','Arial',sans-serif;"
        f"font-size:{font_size:.2f}pt;"
        f"line-height:1.15;"
        f"font-weight:{font_weight(bold)};"
        f"font-style:{font_style(italic)};"
        f"color:{font_color};"
        "white-space:pre-wrap;"
        "width:100%;"
    )
    escaped_text = html.escape(text)
    return "\n".join(
        [
            f'<div class="ppt-text-layer" style="{outer_style}">',
            f'<div class="ppt-text-inner" style="{inner_style}">',
            escaped_text,
            "</div>",
            "</div>",
        ]
    )


def render_table_shape(shape, slide_width: float, slide_height: float) -> str:
    try:
        table = shape.Table
    except Exception:
        return ""

    rows = table.Rows.Count
    cols = table.Columns.Count
    if rows <= 0 or cols <= 0:
        return ""

    left = to_percent(shape.Left, slide_width)
    top = to_percent(shape.Top, slide_height)
    width = to_percent(shape.Width, slide_width)
    height = to_percent(shape.Height, slide_height)

    row_html: list[str] = []
    for row_index in range(1, rows + 1):
        cell_html: list[str] = []
        for col_index in range(1, cols + 1):
            cell = table.Cell(row_index, col_index)
            text = sanitize_lines(cell.Shape.TextFrame.TextRange.Text)
            cell_html.extend(
                [
                    '<td class="ppt-table-cell">',
                    html.escape(text),
                    "</td>",
                ]
            )
        row_html.append("<tr>")
        row_html.extend(cell_html)
        row_html.append("</tr>")

    return "\n".join(
        [
            f'<div class="ppt-table-layer" style="left:{left};top:{top};width:{width};height:{height};">',
            '<table class="ppt-table">',
            *row_html,
            "</table>",
            "</div>",
        ]
    )


def collect_rendered_layers(container, slide_width: float, slide_height: float) -> list[str]:
    layers: list[str] = []
    count = container.Count
    for index in range(1, count + 1):
        shape = container(index)
        if shape.Type == POWERPOINT_GROUP:
            layers.extend(collect_rendered_layers(shape.GroupItems, slide_width, slide_height))
            continue
        if shape.Type == POWERPOINT_TABLE:
            table_html = render_table_shape(shape, slide_width, slide_height)
            if table_html:
                layers.append(table_html)
            continue
        try:
            if shape.HasTextFrame and shape.TextFrame.HasText != 0:
                html_block = render_text_shape(shape, slide_width, slide_height)
                if html_block:
                    layers.append(html_block)
        except Exception:
            continue
    return layers


def delete_text_shapes(container) -> None:
    for index in range(container.Count, 0, -1):
        shape = container(index)
        if shape.Type == POWERPOINT_GROUP:
            delete_text_shapes(shape.GroupItems)
            continue
        if shape.Type == POWERPOINT_TABLE:
            shape.Delete()
            continue
        try:
            if shape.HasTextFrame and shape.TextFrame.HasText != 0 and keep_text_shape(shape.TextFrame.TextRange.Text):
                shape.Delete()
        except Exception:
            continue


def export_slide_images(slide, background_slide, reference_path: Path, background_path: Path, width_px: int, height_px: int) -> None:
    slide.Export(str(reference_path), "PNG", width_px, height_px)
    delete_text_shapes(background_slide.Shapes)
    background_slide.Export(str(background_path), "PNG", width_px, height_px)


def deck_frontmatter() -> str:
    return "\n".join(
        [
            "---",
            "theme: default",
            "defaults:",
            "  layout: full",
            "lineNumbers: false",
            "htmlAttrs:",
            "  dir: rtl",
            "  lang: heb",
            "---",
        ]
    )


def deck_style() -> str:
    return "\n".join(
        [
            "<style>",
            ".slidev-layout.full {",
            "  padding: 0;",
            "}",
            ".ppt-slide-canvas {",
            "  position: relative;",
            "  width: 100%;",
            "  height: 100%;",
            "  overflow: hidden;",
            "  background: white;",
            "}",
            ".ppt-slide-bg {",
            "  position: absolute;",
            "  inset: 0;",
            "  width: 100%;",
            "  height: 100%;",
            "  object-fit: fill;",
            "}",
            ".ppt-text-layer, .ppt-table-layer {",
            "  position: absolute;",
            "  box-sizing: border-box;",
            "  overflow: hidden;",
            "  display: flex;",
            "  flex-direction: column;",
            "}",
            ".ppt-table {",
            "  width: 100%;",
            "  height: 100%;",
            "  border-collapse: collapse;",
            "  table-layout: fixed;",
            "  background: transparent;",
            "}",
            ".ppt-table-cell {",
            "  border: 1px solid #444;",
            "  padding: 4px 6px;",
            "  font-family: 'Gisha','Segoe UI','Arial',sans-serif;",
            "  font-size: 16pt;",
            "  white-space: pre-wrap;",
            "  text-align: right;",
            "  vertical-align: top;",
            "}",
            "</style>",
        ]
    )


def build_slide_markdown(background_src: str, rendered_layers: list[str]) -> str:
    lines = [
        '<div class="ppt-slide-canvas">',
        f'<img class="ppt-slide-bg" src="{background_src}" alt="" />',
    ]
    lines.extend(rendered_layers)
    lines.append("</div>")
    return "\n".join(lines)


def open_powerpoint_application():
    last_error = None
    for _ in range(5):
        try:
            app = win32com.client.gencache.EnsureDispatch("PowerPoint.Application")
            app.DisplayAlerts = 0
            return app
        except Exception as exc:
            last_error = exc
            time.sleep(2)
    raise last_error


def open_presentation(powerpoint, pptx_path: Path):
    last_error = None
    for _ in range(5):
        try:
            return powerpoint.Presentations.Open(
                FileName=str(pptx_path),
                ReadOnly=False,
                Untitled=False,
                WithWindow=False,
            )
        except pywintypes.com_error as exc:
            last_error = exc
            time.sleep(2)
    raise last_error


def build_visual_deck(lecture, powerpoint) -> None:
    pptx_path = REPO_ROOT / lecture.pptx
    output_path = REPO_ROOT / lecture.output
    deck_stem = Path(lecture.output).stem
    background_dir = BACKGROUND_ROOT / deck_stem
    reference_dir = REFERENCE_ROOT / deck_stem

    shutil.rmtree(background_dir, ignore_errors=True)
    shutil.rmtree(reference_dir, ignore_errors=True)
    background_dir.mkdir(parents=True, exist_ok=True)
    reference_dir.mkdir(parents=True, exist_ok=True)

    temp_root = REPO_ROOT / "tmp-slide-export"
    temp_root.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(prefix=f"{deck_stem}-", dir=str(temp_root)))
    temp_pptx = temp_dir / pptx_path.name
    shutil.copy2(pptx_path, temp_pptx)

    presentation = None
    try:
        presentation = open_presentation(powerpoint, temp_pptx)
        slide_width = float(presentation.PageSetup.SlideWidth)
        slide_height = float(presentation.PageSetup.SlideHeight)
        width_px = int(slide_width * EXPORT_SCALE)
        height_px = int(slide_height * EXPORT_SCALE)

        slides: list[str] = []
        for slide_index in range(1, presentation.Slides.Count + 1):
            slide = presentation.Slides(slide_index)
            rendered_layers = collect_rendered_layers(slide.Shapes, slide_width, slide_height)
            reference_path = reference_dir / f"slide-{slide_index:03d}.png"
            background_path = background_dir / f"slide-{slide_index:03d}.png"
            export_slide_images(slide, slide, reference_path, background_path, width_px, height_px)
            background_src = f"/slide-backgrounds/{deck_stem}/slide-{slide_index:03d}.png"
            slides.append(build_slide_markdown(background_src, rendered_layers))

        if slides:
            slides[-1] = slides[-1] + "\n\n" + deck_style()
        output = deck_frontmatter() + "\n\n" + "\n\n---\n\n".join(slides)
        output_path.write_text(output.strip() + "\n", encoding="utf-8")
    finally:
        if presentation is not None:
            presentation.Close()
            presentation = None
        gc.collect()
        time.sleep(1)
        shutil.rmtree(temp_dir, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lectures", nargs="*", type=int, help="Lecture numbers to generate")
    args = parser.parse_args()

    selected = LECTURES
    if args.lectures:
        wanted = set(args.lectures)
        selected = [lecture for lecture in LECTURES if lecture.number in wanted]

    pythoncom.CoInitialize()
    powerpoint = open_powerpoint_application()
    try:
        for lecture in selected:
            print(f"Generating visual deck for {lecture.output}...")
            build_visual_deck(lecture, powerpoint)
    finally:
        gc.collect()
        time.sleep(1)
        try:
            powerpoint.Quit()
        except Exception:
            try:
                powerpoint.Presentations.Application.Quit()
            except Exception:
                pass
        powerpoint = None
        gc.collect()
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    main()
