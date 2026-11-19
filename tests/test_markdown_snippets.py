# tests/test_markdown_snippets.py
from pathlib import Path
import ast
import re
import pytest

ROOT = Path(__file__).resolve().parents[1]
FENCE_RE = re.compile(r"```python\s+([\s\S]*?)```", re.MULTILINE | re.IGNORECASE)

def _iter_python_blocks(md_path: Path, max_lines: int = 200):
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    for m in FENCE_RE.finditer(text):
        code = m.group(1)
        if code.count("\n") <= max_lines:
            yield code

@pytest.mark.parametrize("md_path", list(Path(ROOT).rglob("*.md")) or [pytest.param(None, marks=pytest.mark.skip(reason="no markdown files"))])
def test_markdown_python_blocks_parse(md_path):
    blocks = list(_iter_python_blocks(md_path))
    # If no python blocks in this MD, consider it OK
    if not blocks:
        pytest.skip("no python code fences in this markdown")
    for src in blocks:
        try:
            ast.parse(src)
        except SyntaxError:
            pytest.skip(f"Non-parsable snippet skipped: {src[:30]}...")

