# Setup from Zero

This guide assumes that you have **never installed a programming tool and have never written code**. Read the whole section for your operating system before running commands. A command is not complete until its verification step succeeds.

## 1. Install Python

Download Python 3.11 or newer from [python.org/downloads](https://www.python.org/downloads/). Python 3.11–3.13 are supported by the course. On Windows, select **Add python.exe to PATH** in the installer. On macOS and Linux, use the official installer or your system package manager, but keep the course commands based on `python3` if `python` is not available.

Open a new terminal after installation and verify the runtime:

```text
# Windows PowerShell
py --version

# macOS or Linux
python3 --version
```

You should see Python 3.11, 3.12, or 3.13. If the command is not found, close every terminal window, open a new one, and try again. If it still fails, read the matching entry in [TROUBLESHOOTING.md](TROUBLESHOOTING.md); do not install several unrelated Python copies until you understand which one your terminal is using.

## 2. Install Git

Git records changes and lets you download the course. Install it from [git-scm.com/downloads](https://git-scm.com/downloads). Open a new terminal and verify:

```text
git --version
```

If you cannot install Git yet, download the repository as a ZIP from its GitHub page and extract it. That fallback gets you started, but return to Git before the first project so that you can practise reproducible collaboration.

## 3. Install Visual Studio Code

Download [Visual Studio Code](https://code.visualstudio.com/). Keep the default options. Launch it once so the application completes its first-run setup. The course uses VS Code because its editor, terminal, debugger, tests, and Markdown preview can be learned together; another editor is acceptable if it can run the same commands.

Install the extensions listed in [VS_CODE_SETUP.md](VS_CODE_SETUP.md) through the Extensions icon. The Python and Pylance extensions are required. The other extensions are conveniences that make code, Markdown, CSV, Git history, and SQLite fixtures easier to inspect.

## 4. Clone the course

Choose a folder where you keep projects. Replace the placeholder URL with the repository URL supplied by your course group:

```text
git clone <repository-url>
cd zero-to-hero-python-cybersecurity-
```

Open the repository folder in VS Code with **File > Open Folder**. Open **Terminal > New Terminal** inside VS Code. From now on, run course commands from the repository root, the folder containing `README.md` and `pyproject.toml`.

## 5. Create a project-local virtual environment

A virtual environment keeps this course's libraries separate from unrelated projects. On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

When activation succeeds, the terminal prompt normally begins with `(.venv)`. Verify that the active interpreter belongs to the course:

```text
python --version
python -c "import sys; print(sys.executable)"
```

If PowerShell refuses to activate a script, do not weaken security settings blindly. Use the troubleshooting guide, or run the course through `py -m` while you ask an instructor for help.

## 6. Install development tools

With the virtual environment active, install the pinned development dependencies:

```text
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The `-e` option installs the course package in editable mode so that your local changes are used immediately. The square-bracket `dev` group installs the test and quality tools used by the repository.

## 7. Select the interpreter in VS Code

Press `Ctrl+Shift+P` on Windows/Linux or `Command+Shift+P` on macOS. Choose **Python: Select Interpreter**, then select the interpreter whose path contains `.venv`. If the interpreter is not listed, choose **Enter interpreter path** and select `.venv/Scripts/python.exe` on Windows or `.venv/bin/python` on macOS/Linux.

Open a new VS Code terminal after selecting it. Run:

```text
python scripts/course_doctor.py
```

The doctor should report the Python version, repository root, virtual environment, required directories, and setup status. A failure is not a dead end; it is a checklist of the next fix.

## 8. Run your first program and first test

Run Day 1's starter:

```text
python -m course_days.day001
```

Run the repository tests:

```text
python -m pytest -q
```

Run the structural audit:

```text
python scripts/course_doctor.py --strict
```

The first time you run a command, read the output line by line. The purpose is not to memorise commands. It is to understand which program read which file and produced which result.

## 9. Daily update routine

At the beginning of a study session, activate `.venv`, run `git pull --ff-only`, and run the doctor. At the end, run the day's tests, inspect `git diff`, and write a short note about what you learned. Do not commit passwords, API keys, private evidence, or personal data. Use the synthetic fixtures supplied by the course.

## 10. The first recovery habits

When a command fails, copy the first error line, the command you ran, your operating system, and the output of `python --version`. Do not hide the error by repeatedly reinstalling tools. Most early failures come from being in the wrong directory, using the wrong interpreter, forgetting to activate `.venv`, or opening a terminal that existed before an installation changed PATH.
