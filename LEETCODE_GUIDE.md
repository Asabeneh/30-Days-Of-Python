# LeetCode and Problem-Solving Guide

Algorithms are useful because they help you reason about data, time, memory, and trade-offs. They are not a replacement for authorization, threat modeling, evidence handling, secure design, or professional judgment. This guide adds a small, deliberate LeetCode strand to the course so that a beginner develops general problem-solving fluency without losing the cybersecurity focus.

## Weekly routine

Complete two **core** problems and one **stretch** problem each week after the relevant Python concepts have been taught. Before coding, write the input, output, constraints, and one example. After coding, add tests, explain the invariant or decision rule, and record time and space complexity. If you are stuck, write a simpler correct solution before trying to optimize it.

Use the official problem page for the statement. This repository provides original prompts, hints, and security bridges; it does not reproduce copyrighted problem statements or hidden platform solutions.

## Progressive problem map

| Course days | Patterns | Core problems | Security bridge |
| ---: | --- | --- | --- |
| 11–20 | Arrays, strings, sets, hash maps, stacks | [Two Sum](https://leetcode.com/problems/two-sum/), [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/), [Valid Anagram](https://leetcode.com/problems/valid-anagram/), [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Deduplicate indicators, count event frequencies, and track parser state |
| 21–30 | Sorting, two pointers, windows, binary search | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [Binary Search](https://leetcode.com/problems/binary-search/), [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/), [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Scan thresholds, reason about time windows, and search ordered events |
| 31–40 | Queues, linked lists, recursion, heaps | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/), [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Model work queues, detect cycles, and prioritize triage |
| 41–50 | Intervals, trees, graph traversal | [Merge Intervals](https://leetcode.com/problems/merge-intervals/), [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/), [Number of Islands](https://leetcode.com/problems/number-of-islands/), [Course Schedule](https://leetcode.com/problems/course-schedule/) | Merge asset ranges, traverse dependencies, and reason about reachability in fixtures |
| 51–70 | Backtracking, dynamic programming, bit operations | [Subsets](https://leetcode.com/problems/subsets/), [Combination Sum](https://leetcode.com/problems/combination-sum/), [House Robber](https://leetcode.com/problems/house-robber/), [Counting Bits](https://leetcode.com/problems/counting-bits/) | Bound search spaces, plan resources, and interpret permission flags |
| 71–90 | Mixed practical review | Revisit one weak pattern each week and implement a course parser or detector using it | Translate generic patterns into explainable security logic |
| 91–120 | Communication and design | One timed core problem every two weeks plus a project-specific complexity explanation | Defend choices, failure handling, and scalability in the capstone |

## The solution note template

For every problem, write a short note with these headings:

```text
Pattern:
Input and output:
Simplest correct idea:
Invariant or decision rule:
Why the implementation works:
Time complexity:
Space complexity:
Edge case:
Security bridge:
What I would test next:
```

The security bridge is not an excuse to claim that a LeetCode problem is a real security control. It is a prompt to ask where the pattern appears in a bounded utility: a frequency counter in log triage, a queue in an alert pipeline, an interval merge in an asset inventory, or a graph traversal in a dependency fixture.

## What not to optimise

Do not spend an entire study session chasing a clever one-line solution while your tests are missing. Do not copy a solution before attempting the problem. Do not treat a green online judge as proof that code is secure. Real security software must also handle untrusted input, permissions, logging, privacy, dependencies, failure, and authorization.
