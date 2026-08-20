# Day 33: Paths, File Metadata, and Symlinks

[← Day 32](../032_day_linux_command_line/032_day_linux_command_line.md) · [Day index](../DAY_INDEX.md) · [Day 34 →](../034_day_safe_subprocesses/034_day_safe_subprocesses.md)

## Table of Contents

- [Why this lesson exists](#why-this-lesson-exists)
- [Prerequisites](#prerequisites)
- [Outcomes](#outcomes)
- [The problem](#the-problem)
- [Security boundary](#security-boundary)
- [Lesson](#lesson)
- [Vocabulary](#vocabulary)
- [Worked examples](#worked-examples)
- [Execution trace](#execution-trace)
- [Common mistakes](#common-mistakes)
- [Security application](#security-application)
- [Exercises](#exercises)
- [Finish line](#finish-line)

## Why this lesson exists

A file’s content is not its only property. Size, mode, owner, modification time, and link status affect how a security tool should handle it.

## Prerequisites

Complete Day 32 and run the phase checks. The lesson assumes you can read a traceback, use a virtual environment, and work only with the supplied repository fixtures.

## Outcomes

By the end of this lesson, you can:

- explain the concept in plain language and precise Python terms
- run and modify each worked example
- test a normal case, boundary case, and failure case
- apply the idea to the safe local context described by Day 33

## The problem

Inspect metadata of local fixture files without following an unexpected link or assuming that a name identifies one object.

## Security boundary

Use only local synthetic fixtures and explicitly authorized course files. The lesson does not authorize public scanning, credential use, remote command execution, or changes to operating-system state.

## Lesson

### Vocabulary

Metadata describes a file object. A **symlink** points to another path. A **mode** describes permission bits. `stat` reports file metadata.

## Worked examples

### Example 1: Read basic metadata

`Path.stat` returns size and timestamps.

```python
from pathlib import Path

path = Path("shared/fixtures/events.log")
info = path.stat()
print(info.st_size)
```

**What to observe:**

A non-negative byte count.

### Example 2: Check a regular file

A tool should decide whether directories, devices, and links are allowed.

```python
print(path.is_file(), path.is_dir())
```

**What to observe:**

The fixture is a regular file and not a directory.

### Example 3: Inspect without following

`lstat` describes the link itself when the path is a symlink.

```python
info = path.lstat()
print(info.st_mode)
```

**What to observe:**

The mode can be inspected before opening.

### Example 4: Hash a fixture

A digest identifies content changes but is not secrecy or authenticity.

```python
import hashlib

digest = hashlib.sha256(path.read_bytes()).hexdigest()
print(digest[:12])
```

**What to observe:**

A short display prefix for a synthetic file.

### Example 5: Compare before and after

Metadata and hashes can support a local baseline.

```python
before = path.stat().st_size
# change a local fixture deliberately, then measure again
after = path.stat().st_size
print(before, after)
```

**What to observe:**

A change is observable and should be explained.

## Execution trace

A path lookup returns an object whose metadata can be inspected; a link may redirect the lookup, so the tool must choose follow or no-follow behavior before reading.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| name equals object | symlink or replacement is missed | inspect link and resolved target |
| hash proves integrity | digest is treated as authenticity | compare against a trusted reference |
| timestamps equal causation | order is overclaimed | state clock limitations |
| read everything for metadata | unnecessary data exposure | inspect metadata first |
| assume POSIX permissions | Windows behavior differs | document platform scope |

## Security application

Inspect only local fixture metadata. Do not change permissions or follow links outside the repository. Record what the baseline can and cannot show.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run every requested command, create the requested artifact, and record the limitation the exercise asks you to name.

## Finish line

Run `python -m course_days.day033`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> File metadata is context for a decision, not a verdict; inspect the object, the path resolution, and the source of the baseline.

## Limitations

Metadata can be changed, clocks can be wrong, and a hash without trusted provenance is only a fingerprint.

[← Day 32](../032_day_linux_command_line/032_day_linux_command_line.md) · [Day index](../DAY_INDEX.md) · [Day 34 →](../034_day_safe_subprocesses/034_day_safe_subprocesses.md)
