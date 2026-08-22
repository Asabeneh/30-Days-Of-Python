# VS Code Setup and Learner Workflow

VS Code is optional software, not a substitute for learning the terminal. The course explains every essential command so that you can continue even if an extension is unavailable. The extensions below make the feedback loop faster and make the dense lessons easier to navigate.

## Install extensions through the Extensions panel

Open VS Code, select the four-square **Extensions** icon, search for each name, verify the publisher, and select **Install**. Do not install an extension merely because its name contains “security.” Read its publisher, permissions, update history, and reviews first.

| Extension | Marketplace page | Status | Use |
| --- | --- | --- | --- |
| Python | [Microsoft Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | Required | Interpreter selection, running files, environments, testing, and Python commands |
| Pylance | [Microsoft Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) | Required | Completion, navigation, diagnostics, and readable type information |
| Python Debugger | [Microsoft Debugpy](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) | Required | Breakpoints, stepping, variables, and call-stack inspection |
| Ruff | [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) | Required | Formatting and lint feedback; the Marketplace page is the source of truth for its current publisher and setup |
| Markdown All in One | [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) | Required | Table of contents, navigation, and readable lesson editing |
| Markdownlint | [Markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) | Recommended | Consistent Markdown style |
| GitLens | [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) | Recommended | Visual history, branches, and line-level change context |
| Rainbow CSV | [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) | Recommended | Read CSV, TSV, and pipe-delimited security fixtures more comfortably |
| SQLite Viewer | [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) | Recommended | Inspect local case databases without another application |

The required group is intentionally small. Install recommended extensions one at a time and keep only those that make your workflow clearer. If a course instruction works only after an optional extension is installed, it is a documentation bug.

## Select the Python interpreter

After creating `.venv`, press `Ctrl+Shift+P` or `Command+Shift+P`, choose **Python: Select Interpreter**, and select the interpreter whose path contains `.venv`. Confirm the selection in the bottom status bar. Open a new integrated terminal and run:

```text
python -c "import sys; print(sys.executable)"
```

The printed path should point into this repository's `.venv` directory. A correct-looking editor with the wrong interpreter is one of the most common beginner traps.

## Run and debug a file

Open a starter file and press the play button in the upper-right corner, or run the explicit terminal command documented by that day. To understand execution rather than watch output flash past, click to the left of a line number to add a breakpoint. Start **Run and Debug**, inspect the Variables panel, then use **Step Over** to move one statement at a time.

When debugging a parser or detection rule, ask three questions at every stop: what values entered this function, what decision is being made, and what evidence will be returned to the caller? Remove breakpoints after the experiment so that the next learner can run the starter normally.

## Run tests from the editor

The Python extension discovers `test_*.py` files after the interpreter is selected. Open the Testing beaker icon, select **Configure Python Tests**, choose `pytest`, and choose the repository `tests` directory. You can run one test, one file, or the complete suite. The terminal remains the source of truth:

```text
python -m pytest -q
```

A green test is evidence for the behavior the test describes. It is not proof that the entire design is secure. Security reasoning still requires a threat model, review, and negative tests.

## Read the lessons efficiently

Use the Markdown outline view to jump between prerequisites, outcomes, traces, common mistakes, practice, and the finish line. Keep the lesson open beside the starter using **Split Right**. Use the preview only to inspect formatting; execute code from the terminal so that the runtime and the editor agree about what happened.

The course uses diagrams and code blocks as explanatory tools. If a diagram is unclear, redraw it on paper or in a text file. A learner who can sketch the data flow and trust boundary is learning more than a learner who can only reproduce a command.

## Recommended workspace habits

Keep one VS Code window open at the repository root. Keep one terminal for the active virtual environment and a second terminal for Git commands when necessary. Save your work before running tests. Use `git diff` to inspect changes, and do not commit generated caches, virtual environments, credentials, private evidence, or downloaded challenge data.

## Extension safety

Extensions execute code with access to your development environment. Install from the official Marketplace page, verify the publisher, keep extensions updated, and remove extensions that you no longer use. Never paste private incident data, tokens, passwords, or proprietary source code into an extension's chat panel or an online service without explicit permission and an approved data-handling policy.
