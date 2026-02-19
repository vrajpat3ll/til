import asyncio
from math import ceil
from pathlib import Path
import subprocess as sp

from elements import HTMLElement

DOCS_DIR = Path("docs")

AVOID_DIRS = {
    ".git",
    ".obsidian",
    ".venv",
    "__pycache__",
    "images",
    "site",
    "work-in-progress",
}

res = sp.run(
    ["git", "ls-files", "--others", "--exclude-standard"],
    capture_output=True,
    text=True,
)

untracked_files = res.stdout.splitlines() if res.stdout else []
AVOID_TILS = {str((DOCS_DIR / "index.md").resolve()), *untracked_files}


def get_categories(base_path: Path) -> list[str]:
    """Return sorted list of category directories."""
    return sorted(
        d.name for d in base_path.iterdir() if d.is_dir() and d.name not in AVOID_DIRS
    )


def get_tils(category: str) -> list[Path]:
    """Return all markdown TIL files in a category."""
    category_path = DOCS_DIR / category
    return [p for p in category_path.glob("*.md") if str(p) not in AVOID_TILS]


def get_title(file_path: Path) -> str:
    """Extract first markdown heading as title."""
    try:
        with file_path.open(encoding="utf-8") as f:
            for line in f:
                if line.startswith("#"):
                    return line.lstrip("#").strip()
    except Exception as e:
        print(e)

    return "Find Out Yourself!"


def count_total_tils() -> int:
    return sum(len(get_tils(cat)) for cat in get_categories(DOCS_DIR))


def sanitize_topic(topic: str) -> str:
    """Convert directory name to readable title."""
    topic = topic.replace("_", " ").replace("-", " ")
    return " ".join(word.capitalize() for word in topic.split())


def format_link(path: Path, for_docs_site: bool) -> str:
    """
    Format link depending on output location.

    for_docs_site=True  -> index.md (inside docs/)
    for_docs_site=False -> README.md (repo root)
    """
    path_str = path.as_posix()

    if for_docs_site:
        return path_str.removeprefix("docs/").removesuffix('.md')  # remove docs/ prefix
    return path_str  # keep docs/ prefix


def build_categories_table() -> tuple[str, list[str]]:
    categories = get_categories(DOCS_DIR)
    categories = [c for c in categories if get_tils(c)]

    cols = 3
    rows = ceil(len(categories) / cols)

    content = "## Categories\n\n" + HTMLElement.table_start

    for r in range(rows):
        content += HTMLElement.row_start
        for c in range(cols):
            idx = r * cols + c
            if idx >= len(categories):
                break

            cat = categories[idx]
            count = len(get_tils(cat))

            link = HTMLElement.href(f"#{cat}", sanitize_topic(cat))
            badge = HTMLElement.superscript(f"[{count}]")

            content += HTMLElement.data_start + link + badge + HTMLElement.data_end
        content += HTMLElement.row_end

    content += HTMLElement.table_end + "\n"
    return content, categories


def build_recent_tils(n: int = 5) -> str:
    all_tils = [til for cat in get_categories(DOCS_DIR) for til in get_tils(cat)]

    recent = sorted(all_tils, key=lambda p: p.stat().st_mtime, reverse=True)[:n]

    content = "## Recent TILs 🆕\n\n" + HTMLElement.table_start

    for til in recent:
        content += (
            HTMLElement.row_start
            + HTMLElement.data_start
            + HTMLElement.href(format_link(til, True), get_title(til))
            + HTMLElement.data_end
            + HTMLElement.row_end
        )

    content += HTMLElement.table_end + "\n"
    return content


def build_til_sections(categories: list[str], for_docs_site: bool) -> str:
    sections = []

    for cat in categories:
        tils = get_tils(cat)
        if not tils:
            continue

        section = f"## {sanitize_topic(cat)}\n\n"
        for til in tils:
            link = format_link(til, for_docs_site)
            section += f"- {HTMLElement.link(get_title(til), link)}\n"

        sections.append(section)

    return "\n".join(sections)


def write_index():
    content, categories = build_categories_table()

    with (DOCS_DIR / "index.md").open("w", encoding="utf-8") as f:
        f.write(HTMLElement.HEADER)
        f.write(f"_{count_total_tils()} TILs_ and counting...\n\n")
        f.write(content)
        f.write(build_recent_tils())
        f.write(build_til_sections(categories, True))
        f.write("\n---\n\n" + HTMLElement.FOOTER)


def write_readme():
    content, categories = build_categories_table()

    with Path("README.md").open("w", encoding="utf-8") as f:
        f.write(HTMLElement.HEADER)
        f.write(f"_{count_total_tils()} TILs_ and counting...\n\n")
        f.write(content)
        f.write(build_til_sections(categories, False))
        f.write("\n---\n\n" + HTMLElement.FOOTER)


async def main():
    """TIL build script algorithm:

    1. Create an index.md file for the index of the website
    2. Create readme file for github repo
    """

    await asyncio.gather(
        asyncio.to_thread(write_index),
        asyncio.to_thread(write_readme),
    )


if __name__ == "__main__":
    asyncio.run(main())
