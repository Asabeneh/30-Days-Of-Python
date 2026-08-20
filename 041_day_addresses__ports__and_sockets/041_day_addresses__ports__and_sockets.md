# Day 41: Addresses, Ports, and Sockets

[← Day 40](../040_day_project__host_baseline_auditor/040_day_project__host_baseline_auditor.md) · [Day index](../DAY_INDEX.md) · [Day 42 →](../042_day_tcp_clients_and_servers/042_day_tcp_clients_and_servers.md)

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

Network programs begin with names and endpoints. A learner must understand what an address identifies, what a port represents, and why a socket operation is not automatically authorized.

## Prerequisites

Complete Day 40. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Describe a local service endpoint and create a socket object without scanning or connecting to an unknown host.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

An IP address identifies an interface in a network context. A port identifies a transport endpoint. A socket is a program object representing communication settings.

## Worked examples

### Example 1: Represent an endpoint

Keep host and port as separate typed values.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int


print(Endpoint("127.0.0.1", 8000))
```

**What to observe:**

`Endpoint(host='127.0.0.1', port=8000)`

### Example 2: Validate a port

Conversion and range policy are separate steps.

```python
def port(value: str) -> int:
    number = int(value)
    if not 1 <= number <= 65535:
        raise ValueError("port outside TCP/UDP range")
    return number
```

**What to observe:**

`port('8000')` returns 8000; 0 and 65536 are rejected.

### Example 3: Create a socket

Creating a socket does not send traffic.

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock.family, sock.type)
sock.close()
```

**What to observe:**

The object is IPv4/TCP and is closed without connecting.

### Example 4: Use a context manager

Cleanup should happen even when later code fails.

```python
with socket.socket() as sock:
    sock.settimeout(1.0)
    print(sock.gettimeout())
```

**What to observe:**

`1.0` seconds.

### Example 5: State scope

A network operation should carry its authorization boundary.

```python
scope = {"host": "127.0.0.1", "purpose": "course fixture", "remote": False}
print(scope)
```

**What to observe:**

The scope is local and explicit.

## Execution trace

The endpoint is validated, the socket is created, options are set, and cleanup happens. No network operation occurs until a connect, bind, send, or receive call is made.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| port as a string everywhere | comparisons behave unexpectedly | convert at the boundary |
| socket never closed | resources remain open | use `with` |
| localhost equals harmless | a local service may contain private data | define authorization and fixture |
| address equals identity | IP data is overinterpreted | record source and confidence |
| connect in a test | external side effect | use a fake or local controlled service |

## Security application

Use loopback or a fake socket in tests. Do not enumerate ports or connect to systems not explicitly supplied by the course.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day041`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> An endpoint is data; a socket is a capability; authorization must exist before the capability is used.

## Limitations

Addresses and ports change, can be spoofed, and do not identify a person or authorize access.

[← Day 40](../040_day_project__host_baseline_auditor/040_day_project__host_baseline_auditor.md) · [Day index](../DAY_INDEX.md) · [Day 42 →](../042_day_tcp_clients_and_servers/042_day_tcp_clients_and_servers.md)
