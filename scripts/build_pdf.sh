#!/usr/bin/env bash
# Build the PDF edition: regenerate the map -> validate -> pandoc the prose
# fragments -> typst compile.
#
# This is the ONE PDF path. The MyST typst export (myst build --typst) was
# removed from book/myst.yml deliberately: it flattened the book into a
# numbered-article template and could not express the real layout (mixed
# portrait/landscape, full-bleed posters, letter-grid navigation). The web
# edition remains MyST (`cd book && myst build --html`); the PDF is this script.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BOOK="$ROOT/book"
GEN="$BOOK/pdf/_generated"
OUT="$BOOK/exports/overresponsible-ai-handbook.pdf"

command -v pandoc >/dev/null || { echo "ERROR: pandoc is required (brew install pandoc)"; exit 2; }
command -v typst  >/dev/null || { echo "ERROR: typst is required (brew install typst)"; exit 2; }

# 1. Map: parse + validate (exits nonzero, named failure, on any drift).
python3 "$ROOT/scripts/build_map.py"

# 2. Prose fragments via pandoc (md -> typst), with metadata anchors injected
#    so the native typst TOC/grid can link to sections.
mkdir -p "$GEN"
python3 - "$BOOK" "$GEN" <<'PY'
import re
import subprocess
import sys
from pathlib import Path

book, gen = Path(sys.argv[1]), Path(sys.argv[2])

def slugify(heading: str) -> str:
    s = re.sub(r"\*|_|`", "", heading.lower())
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")

def sections(md_path: Path):
    """Split an H1-titled file into (id, title, body_md) H2 sections."""
    text = md_path.read_text()
    parts = re.split(r"^## ", text, flags=re.M)[1:]  # drop the H1 preamble
    out = []
    for part in parts:
        title, _, body = part.partition("\n")
        body = body.strip().strip("-").strip()  # trim the trailing --- rules
        out.append((slugify(title), title.strip(), body))
    return out

# Pandoc's typst writer references helpers its own template normally provides;
# these fragments are included bare, so define them here.
PRELUDE = (
    '#let horizontalrule = align(center, '
    'line(length: 26%, stroke: 0.5pt + luma(62%)))\n'
)

def to_typst(md: str) -> str:
    return subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "typst"],
        input=md, capture_output=True, text=True, check=True,
    ).stdout

def fragment(secs) -> str:
    chunks = [PRELUDE]
    for i, (sec_id, title, body) in enumerate(secs):
        if i > 0:
            chunks.append("#pagebreak(weak: true)")
        chunks.append(f'#place(metadata("sec-{sec_id}"))')
        chunks.append(to_typst(f"# {title}\n\n{body}"))
    return "\n".join(chunks)

front = sections(book / "front-matter.md")
toc_idx = next(i for i, (sec_id, _, _) in enumerate(front) if sec_id == "table_of_contents")
(gen / "front_pre_toc.typ").write_text(fragment(front[:toc_idx]))
(gen / "front_post_toc.typ").write_text(fragment(front[toc_idx + 1:]))  # TOC itself is rendered natively, linked

(gen / "back_all.typ").write_text(fragment(sections(book / "back-matter.md")))

# Coloring intro: the prose before the first per-letter section, heading dropped
# (main.typ provides the visible heading + anchor).
coloring = (book / "coloring-pages.md").read_text()
intro_md = coloring.split("---")[0]
intro_md = re.sub(r"^# .*\n", "", intro_md, flags=re.M).strip()
(gen / "coloring_intro.typ").write_text(to_typst(intro_md))

print(f"fragments: {[p.name for p in sorted(gen.glob('*.typ'))]}")
PY

# 3. Compile.
mkdir -p "$BOOK/exports"
typst compile --root "$BOOK" "$BOOK/pdf/main.typ" "$OUT"
ls -lh "$OUT" | awk '{print "PDF:", $9, "("$5")"}'
