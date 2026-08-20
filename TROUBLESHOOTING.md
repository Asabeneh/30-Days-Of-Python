# Troubleshooting

An error is a report about the current state of the machine or program. Read the command you ran, the first error line, the file path, and the line number before changing anything.

## `python` or `python3` is not found

Close and reopen the terminal after installing Python. On Windows, try `py --version`; on macOS or Linux, try `python3 --version`. If one command works and the other does not, use the working command to create `.venv`, then activate the environment and use `python` inside it.

## `git` is not found

Install Git from [git-scm.com](https://git-scm.com/downloads), close every terminal window, open a new one, and run `git --version`. If you used the ZIP fallback, continue with the setup but install Git before the first project checkpoint.

## VS Code uses the wrong interpreter

Run `python -c "import sys; print(sys.executable)"` in the terminal. If the path is not inside `.venv`, use **Python: Select Interpreter** and choose the project environment. Then open a new integrated terminal.

## Activation is blocked in PowerShell

Do not copy an unrestricted execution-policy command from an unknown website. Ask your instructor or administrator for the approved local policy, or use the course through the Python executable inside `.venv` while you resolve the environment safely.

## `No module named course_days`

The command was probably run outside the repository root. Use the VS Code Explorer to confirm that `README.md`, `pyproject.toml`, and `course_days` are visible. Then run `python -m course_days.day001` from that folder.

## A package is missing

Confirm that `.venv` is active. Run `python -m pip --version` and inspect its path. Then install the development group with `python -m pip install -e ".[dev]"`. Avoid `sudo pip` and avoid installing several global copies of the same tool.

## Tests are not discovered

Select the `.venv` interpreter, configure `pytest` in the Testing panel, and run the source-of-truth command:

```text
python -m pytest -q
```

If a single test fails, run it with its path and `-vv` so the assertion and values are visible.

## Markdown links or images do not open

Run the link checker when available and confirm that the path is relative to the Markdown file, not the repository root. Case differences matter on Linux. Do not “fix” a link by pointing it at a copied duplicate; correct the navigation structure instead.

## The course doctor reports a problem

Treat each line as a checklist. Missing root files usually mean setup is incomplete. Missing lesson files usually mean a day was created with the wrong name. A legacy marker means the active learner-facing course still contains inherited branding or clutter that must be rewritten or removed.

## Security lab uncertainty

Stop if the target, data, permission, or expected impact is unclear. Read `lab/scope.md`, restore the local fixture, and ask for clarification. Never continue against a public or third-party target because a command appears harmless.
