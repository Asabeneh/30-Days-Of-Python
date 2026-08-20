# Day 42: TCP Clients, Servers, and Framing

[← Day 41](../day_41_addresses__ports__and_sockets/day_41_addresses__ports__and_sockets.md) · [Day index](../DAY_INDEX.md) · [Day 43 →](../day_43_udp_and_framing/day_43_udp_and_framing.md)

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

TCP provides an ordered byte stream, not messages. A security engineer must understand connection lifecycle, partial reads, framing, and timeouts before writing a client or service.

## Prerequisites

Complete Day 41. Run the repository checks and use only the local fixtures and explicitly authorized loopback services.

## Outcomes

By the end of this lesson, you can:

- explain the protocol or security property in plain language
- run and modify every worked example
- test a normal, boundary, and failure case
- identify the trust boundary and residual risk
- connect the concept to the numbered cybersecurity exercises

## The problem

Build a local loopback echo exchange with a length or delimiter rule and a finite timeout.

## Security boundary

Use synthetic data, local fixtures, and loopback-only demonstrations. This lesson does not authorize scanning, interception, credential use, remote command execution, or changes to systems you do not own.

## Lesson

### Vocabulary

TCP is connection-oriented. A **stream** has no message boundaries. **Framing** tells the receiver where one message ends. `accept` creates a per-client socket.

## Worked examples

### Example 1: Bind a local server

Binding reserves an endpoint for a local process.

```python
import socket

server = socket.socket()
server.bind(("127.0.0.1", 0))
print(server.getsockname()[1])
server.close()
```

**What to observe:**

Port zero asks the OS for a temporary local port.

### Example 2: Listen and accept

A server creates a listening socket, then accepts a client socket.

```python
server.listen(1)
client, address = server.accept()
client.close()
```

**What to observe:**

`client` represents one connection; this call blocks until a client arrives.

### Example 3: Send bytes

Sockets send bytes, so text needs an encoding.

```python
payload = "hello".encode("utf-8")
print(payload)
```

**What to observe:**

`b'hello'`

### Example 4: Frame with a delimiter

A newline can separate small training messages.

```python
buffer = b"one\ntwo\n"
messages = buffer.split(b"\n")
print(messages[:2])
```

**What to observe:**

The first two frames are `one` and `two`.

### Example 5: Set a timeout

Blocking network calls need a finite wait.

```python
sock.settimeout(1.0)
print(sock.gettimeout())
```

**What to observe:**

The call will not wait forever.

## Execution trace

A TCP server binds and listens, accepts a connection, receives arbitrary-sized chunks, reconstructs frames, responds, and closes. A single `recv` is not guaranteed to return one complete message.

## Common mistakes

| Mistake | Symptom | Correction |
| --- | --- | --- |
| assume `recv` is one message | partial or combined frames | implement framing |
| forget close | sockets accumulate | use context managers and `finally` |
| no timeout | connection hangs | set a finite timeout |
| bind all interfaces | service is exposed unexpectedly | use loopback for practice |
| echo untrusted bytes | protocol confusion | define encoding and maximum frame size |

## Security application

Use only loopback and a disposable port. The exercise must include a maximum frame size and a test for a partial frame; it must not become a remote shell or scanner.

## Exercises

Complete the numbered questions in [practice/exercises.md](practice/exercises.md) in order. Run the requested local command, inspect its output, and record the limitation asked for by the exercise.

## Finish line

Run `python -m course_days.day042`, pass the relevant tests, complete the numbered exercises, and explain one edge case aloud or in writing.

## Mental model

> TCP is a stream with a lifecycle and no built-in message boundaries; framing and limits are application responsibilities.

## Limitations

TLS, authentication, access control, and operational hardening are not provided by a bare TCP socket.

[← Day 41](../day_41_addresses__ports__and_sockets/day_41_addresses__ports__and_sockets.md) · [Day index](../DAY_INDEX.md) · [Day 43 →](../day_43_udp_and_framing/day_43_udp_and_framing.md)
