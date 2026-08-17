#!/usr/bin/env python3
"""Build book/book_map.yaml — the single build input for the Typst PDF and the
validation gate for the whole pipeline.

Derived, never hand-edited; book/*.md prose stays the source of truth. The output
file is gitignored (same policy as keyword_index.md) and regenerated on every PDF
build. Exits nonzero with a named failure if any validation check fails.

Parses the POST-period-piece-edit alphabet structure (the figure directive carries
the definition as its caption; the koan follows the figure):

    ## <L> is for <Title>

    ```{figure} images/facer/<l>_facer.<ext>
    :alt: ...
    :width: 100%

    **<L> is for <Title>** — <definition>
    ```

    > <koan>

Lineart paths are derived from the letter + whatever file is actually present in
book/images/lineart/ (extension-agnostic — the lineart pipeline may change formats).

Stdlib + PyYAML only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

BOOK = Path(__file__).resolve().parent.parent / "book"

ENTRY_RE = re.compile(
    r"## (?P<letter>[A-Z]) is for (?P<title>[^\n]+)\n\n"
    r"```\{figure\} (?P<facer>images/facer/[a-z]_facer\.[a-z]+)\n"
    r":alt: [^\n]*\n"
    r":width: 100%\n\n"
    r"\*\*[^\n]+\*\* — (?P<definition>[^\n]+)\n"
    r"```\n\n"
    r"> (?P<koan>[^\n]+)\n"
)

HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)


class MapError(SystemExit):
    """Named validation failure — always exits nonzero."""

    def __init__(self, name: str, detail: str):
        super().__init__(f"MAP VALIDATION FAILED [{name}]: {detail}")


def slugify(heading: str) -> str:
    s = heading.lower()
    s = re.sub(r"\*|_|`", "", s)  # markdown emphasis
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s


def section_ids(md_path: Path) -> list[str]:
    return [slugify(h) for h in HEADING_RE.findall(md_path.read_text())]


def parse_letters() -> list[dict]:
    src = (BOOK / "alphabet.md").read_text()
    letters = []
    for m in ENTRY_RE.finditer(src):
        letters.append(
            {
                "letter": m.group("letter"),
                "title": m.group("title").strip(),
                "koan": m.group("koan").strip(),
                "definition": m.group("definition").strip(),
                "facer": m.group("facer"),
                "lineart": derive_lineart(m.group("letter").lower()),
            }
        )
    return letters


def derive_lineart(letter: str) -> str:
    hits = sorted((BOOK / "images" / "lineart").glob(f"{letter}_lineart.*"))
    if not hits:
        raise MapError("lineart-missing", f"no lineart file for letter '{letter}'")
    if len(hits) > 1:
        raise MapError(
            "lineart-ambiguous",
            f"multiple lineart files for '{letter}': {[h.name for h in hits]}",
        )
    return str(hits[0].relative_to(BOOK))


def validate(letters: list[dict]) -> None:
    if len(letters) != 26:
        raise MapError("letter-count", f"expected 26 letter records, parsed {len(letters)}")

    seq = [rec["letter"] for rec in letters]
    expected = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    if seq != expected:
        raise MapError("letter-order", f"letters are not A–Z each-exactly-once: {seq}")

    paths = []
    for rec in letters:
        for field in ("title", "koan", "definition"):
            if not rec[field]:
                raise MapError("empty-field", f"letter {rec['letter']}: empty {field}")
        for field in ("facer", "lineart"):
            p = BOOK / rec[field]
            if not p.is_file():
                raise MapError("file-missing", f"letter {rec['letter']}: {rec[field]} not on disk")
            paths.append(rec[field])

    dupes = {p for p in paths if paths.count(p) > 1}
    if dupes:
        raise MapError("duplicate-paths", f"image paths used more than once: {sorted(dupes)}")


def main() -> None:
    myst = yaml.safe_load((BOOK / "myst.yml").read_text())
    project = myst["project"]
    toc = [entry["file"] for entry in project["toc"]]

    letters = parse_letters()
    validate(letters)

    book_map = {
        "meta": {
            "title": project["title"],
            "subtitle": project.get("subtitle", ""),
            "author": project["authors"][0]["name"],
            "copyright_year": 2025,
            "published_year": 2026,
            "license": project.get("license", "CC-BY-4.0"),
        },
        # section order = myst.yml toc order; ids from the actual headings
        "front": section_ids(BOOK / "front-matter.md"),
        "letters": letters,
        "back": section_ids(BOOK / "back-matter.md"),
    }

    # toc sanity: the files the map derives from must actually be in the toc
    for needed in ("front-matter.md", "alphabet.md", "back-matter.md", "coloring-pages.md"):
        if needed not in toc:
            raise MapError("toc-drift", f"{needed} missing from myst.yml toc")

    out = BOOK / "book_map.yaml"
    out.write_text(yaml.dump(book_map, sort_keys=False, allow_unicode=True, width=100))
    print(f"OK: wrote {out.relative_to(BOOK.parent)} — 26 letters, "
          f"{len(book_map['front'])} front sections, {len(book_map['back'])} back sections")


if __name__ == "__main__":
    main()
