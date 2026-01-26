"""
paper_figures.py

Skill: 从 arXiv PDF 自动提取“论文主图”（通常 Figure 1/首页最大图），并可选择性地把图片块嵌入到
`world_model_interactive_guide/07_paper_tracker.html` 的论文卡片中（方式 A：本地资源）。

核心目标：
- 可重复运行（幂等）
- 生成本地 webp（体积小，适合静态站）
- 产出 manifest（便于审计/追踪）

依赖：
- PyMuPDF (pymupdf)  用于读取 PDF / 提取内嵌图片 / 渲染页面
- Pillow (PIL)        用于转码到 webp
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Literal


ARXIV_ABS_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{5})")


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


def parse_arxiv_ids_from_html(html_text: str) -> list[str]:
    return sorted(set(ARXIV_ABS_RE.findall(html_text)))


def download(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, out_path)


@dataclass(frozen=True)
class ExtractResult:
    arxiv_id: str
    image_file: str
    mode: str
    page: int


def _extract_main_image_from_pdf(
    pdf_path: Path,
    out_webp: Path,
    *,
    try_pages: tuple[int, ...] = (0, 1),
    render_scale: float = 2.0,
    webp_quality: int = 92,
) -> tuple[str, int]:
    """
    策略：
    - 优先：扫描前 try_pages 页的所有内嵌图片，选择面积最大的一张（width*height 最大）
    - 兜底：若找不到可解码图片，则渲染 PDF 首页（整页）为图片
    """
    import fitz  # PyMuPDF
    from PIL import Image

    doc = fitz.open(pdf_path)
    best_bytes: bytes | None = None
    best_area = 0
    best_ext = "unknown"
    best_page = 0

    for page_index in try_pages:
        if page_index >= doc.page_count:
            continue
        page = doc.load_page(page_index)
        for img in page.get_images(full=True):
            xref = img[0]
            info = doc.extract_image(xref)
            if not info or not info.get("image"):
                continue
            w = int(info.get("width") or 0)
            h = int(info.get("height") or 0)
            area = w * h
            if area > best_area:
                best_area = area
                best_bytes = info["image"]
                best_ext = str(info.get("ext") or "unknown")
                best_page = page_index
        if best_bytes is not None:
            break

    out_webp.parent.mkdir(parents=True, exist_ok=True)
    if best_bytes is None:
        page = doc.load_page(0)
        pix = page.get_pixmap(matrix=fitz.Matrix(render_scale, render_scale), alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(out_webp, format="WEBP", quality=webp_quality, method=6)
        return ("page-render", 0)

    try:
        img = Image.open(io.BytesIO(best_bytes)).convert("RGB")
        img.save(out_webp, format="WEBP", quality=webp_quality, method=6)
        return (f"image-{best_ext}-area{best_area}", best_page)
    except Exception:
        page = doc.load_page(0)
        pix = page.get_pixmap(matrix=fitz.Matrix(render_scale, render_scale), alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(out_webp, format="WEBP", quality=webp_quality, method=6)
        return ("page-render", 0)


def extract_figures(
    *,
    html_path: Path,
    out_dir: Path,
    overwrite: bool,
    keep_pdfs: bool,
) -> list[ExtractResult]:
    html_text = html_path.read_text(encoding="utf-8", errors="ignore")
    ids = parse_arxiv_ids_from_html(html_text)
    eprint(f"[extract] found {len(ids)} arXiv ids")

    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[ExtractResult] = []

    for aid in ids:
        pdf_path = out_dir / f"arxiv-{aid}.pdf"
        img_path = out_dir / f"arxiv-{aid}-fig1.webp"

        if img_path.exists() and not overwrite:
            results.append(ExtractResult(aid, img_path.name, "skip-exists", -1))
            continue

        url = f"https://arxiv.org/pdf/{aid}.pdf"
        download(url, pdf_path)

        mode, page_idx = _extract_main_image_from_pdf(pdf_path, img_path)
        results.append(ExtractResult(aid, img_path.name, mode, page_idx))
        eprint(f"[extract] {aid} -> {img_path.name} ({mode}, page={page_idx})")

        if not keep_pdfs:
            try:
                pdf_path.unlink()
            except Exception:
                pass

    # manifest
    manifest = {
        r.arxiv_id: {"file": r.image_file, "mode": r.mode, "page": r.page}
        for r in results
        if r.mode != "skip-exists"
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return results


FIGURE_BLOCK_RE = re.compile(
    r"""<figure\s+class="paper-figure">[\s\S]*?</figure>\s*""",
    re.IGNORECASE,
)


def embed_figures_into_html(*, html_path: Path, out_dir: Path) -> int:
    """
    幂等嵌入策略：
    - 找到每个 paper-card 内的 arXiv id
    - 如果该 card 内已存在 <figure class="paper-figure"> 则跳过
    - 否则把 figure block 插入到 paper-header 之后
    """
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    cards = html.split('<div class="paper-card">')
    if len(cards) <= 1:
        eprint("[embed] no paper-card blocks found")
        return 0

    changed = 0
    new_parts = [cards[0]]

    for card in cards[1:]:
        m = ARXIV_ABS_RE.search(card)
        if not m:
            new_parts.append('<div class="paper-card">' + card)
            continue
        aid = m.group(1)
        if 'class="paper-figure"' in card:
            new_parts.append('<div class="paper-card">' + card)
            continue

        img_path = out_dir / f"arxiv-{aid}-fig1.webp"
        if not img_path.exists():
            new_parts.append('<div class="paper-card">' + card)
            continue

        fig = (
            f'\n                <figure class="paper-figure">\n'
            f'                    <img src="assets/papers/{img_path.name}" alt="arXiv:{aid} Figure 1" loading="lazy">\n'
            f'                    <figcaption><strong>论文主图</strong>：Figure 1（来源：论文 Fig.1）</figcaption>\n'
            f"                </figure>\n"
        )

        # insert right after the first closing paper-header block
        marker = "</div>\n                </div>\n"
        idx = card.find(marker)
        if idx == -1:
            new_parts.append('<div class="paper-card">' + card)
            continue

        insert_at = idx + len(marker)
        new_card = card[:insert_at] + fig + card[insert_at:]
        new_parts.append('<div class="paper-card">' + new_card)
        changed += 1

    if changed:
        html_path.write_text("".join(new_parts), encoding="utf-8")
    eprint(f"[embed] inserted figures into {changed} cards")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--html",
        default="world_model_interactive_guide/07_paper_tracker.html",
        help="paper tracker HTML path",
    )
    parser.add_argument(
        "--out-dir",
        default="world_model_interactive_guide/assets/papers",
        help="output directory for images",
    )
    parser.add_argument("--overwrite", action="store_true", help="overwrite existing images")
    parser.add_argument("--keep-pdfs", action="store_true", help="keep downloaded PDFs")
    parser.add_argument(
        "--embed",
        action="store_true",
        help="also embed <figure> blocks into the HTML for each arXiv paper card",
    )
    args = parser.parse_args()

    html_path = Path(args.html)
    out_dir = Path(args.out_dir)
    if not html_path.exists():
        eprint(f"HTML not found: {html_path}")
        return 2

    extract_figures(
        html_path=html_path,
        out_dir=out_dir,
        overwrite=bool(args.overwrite),
        keep_pdfs=bool(args.keep_pdfs),
    )

    if args.embed:
        embed_figures_into_html(html_path=html_path, out_dir=out_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

