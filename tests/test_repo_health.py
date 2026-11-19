# tests/test_repo_health.py
from pathlib import Path
import py_compile

ROOT = Path(__file__).resolve().parents[1]

def test_readme_exists():
    names = [p.name.lower() for p in ROOT.iterdir() if p.is_file()]
    assert "readme.md" in names

def test_python_files_compile():
    """Compile all tracked .py files; fail on syntax errors."""
    py_files = [p for p in ROOT.rglob("*.py")]
    for p in py_files:
        py_compile.compile(str(p), doraise=True)
