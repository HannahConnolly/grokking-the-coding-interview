# Grokking the Coding Interview — Solutions & Notes 📘

This repository holds my solutions, implementations, and learning notes for the **Grokking the Coding Interview: Patterns for Coding Questions** course by DesignGurus. ([Design Gurus][1])

---

## Table of Contents

* [About the Course](#about-the-course)
* [Timeline & Milestones](#timeline--milestones)
* [Repo Structure & Layout](#repo-structure--layout)
* [How to Use / Run Solutions](#how-to-use--run-solutions)
* [Progress Tracker](#progress-tracker)
* [Learning Notes & Reflections](#learning-notes--reflections)
* [Future Plans](#future-plans)
* [Credits & Resources](#credits--resources)

---

## About the Course

* **Title**: Grokking the Coding Interview: Patterns for Coding Questions ([Design Gurus][1])
* **Estimated Study Time**: ~ 90 hours ([Design Gurus][1])
* **Lessons**: 543 lessons + 609 playgrounds / exercises ([Design Gurus][1])
* **Content Focus**: 33 (or so) coding patterns which can map to many algorithmic problems ([Design Gurus][1])
* **Why Patterns?**
  The core idea is: once you internalize a pattern, you can often map new problems to that pattern rather than starting from scratch. ([Design Gurus][1])

---

## Timeline & Milestones

Here’s a sample roadmap I’m using (you can adjust it):

---

### 📅 **Timeline & Milestones**

| Phase                                   | Patterns / Topics                                                            | Planned Duration | Calendar Weeks (2025) |
| --------------------------------------- | ---------------------------------------------------------------------------- | ---------------- | --------------------- |
| **Phase 0: Warm-up / Basics**           | Warmup, Two Pointers, Fast & Slow Pointers                                   | **1 week**       | **Oct 13 – Oct 19**   |
| **Phase 1: Core Sliding / Interval**    | Sliding Window, Merge Intervals, Cyclic Sort                                 | **1 week**       | **Oct 20 – Oct 26**   |
| **Phase 2: Linked Lists & Stacks**      | In-place Reversal, Stacks, Monotonic Stack, Hash Maps                        | **1½ weeks**     | **Oct 27 – Nov 6**    |
| **Phase 3: Tree & Graph Patterns**      | BFS, DFS, Level-order, Graph Traversal                                       | **2 weeks**      | **Nov 7 – Nov 20**    |
| **Phase 4: Subsets & Search Variants**  | Subsets, Modified Binary Search, Bitwise XOR, Top-K / K-way Merge            | **2 weeks**      | **Nov 21 – Dec 4**    |
| **Phase 5: Greedy / DP / Backtracking** | Greedy, DP (Knapsack, 0-1), Backtracking, Trie, Topological Sort, Union-Find | **2½ weeks**     | **Dec 5 – Dec 21**    |
| **Phase 6: Review & Hard Challenges**   | Re-solve tough problems, timed practice, mixed sets                          | **1 week**       | **Dec 22 – Dec 28**   |

> 🗒️ *Tip:* Commit each solution as you finish it — your Git history becomes an automatic detailed timeline.

---
> ⏱ These are rough estimates. I may pause, revisit, or slow down depending on difficulty or other commitments.

I’ll update as I progress, marking which pattern or module I’m working on and when.

---

## Repo Structure & Layout

This is how I plan to organize the code and notes:

```
grokking-solutions/
├── warmup/
│   ├── contains_duplicate.py
│   ├── valid_palindrome.py
│   └── …
├── two_pointers/
├── fast_slow_pointers/
├── sliding_window/
├── merge_intervals/
├── cyclic_sort/
├── linked_list_reversal/
├── stack/
├── monotonic_stack/
├── hash_maps/
├── tree_bfs/
├── tree_dfs/
├── graph_patterns/
├── subsets/
├── binary_search_variants/
├── bitwise/
├── top_k_merges/
├── greedy/
├── dp_knapsack/
├── backtracking/
├── trie/
├── topo_sort_union_find/
├── hard_challenges/
├── README.md
└── NOTES.md
```

* Each folder corresponds to a pattern or topic.
* File names reflect the problem (e.g., `merge_intervals.py`, `top_k_frequent.py`).
* `NOTES.md` captures insights, tricky cases, improvements, and pattern mapping thoughts.
* If I implement the same problem in multiple languages (say Python + Java), I may use subfolders (e.g. `python/`, `java/`) or suffix naming conventions.

---

## How to Use / Run Solutions

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/grokking-solutions.git
   cd grokking-solutions
   ```

2. Find the topic folder you want (e.g. `sliding_window/`), then the file.

3. Run it (if language supports it). For example, in Python:

   ```bash
   python sliding_window/longest_substring_k_distinct.py
   ```

4. Most solution files include a `main()` or test harness for sample/test cases.

---

## Progress Tracker

I’ll maintain a section like this to show where I stand:

* ✅ Warmup
* 🔄 Two Pointers
* ❌ Fast & Slow Pointers (in progress)
* ❌ Sliding Window
* ❌ Merge Intervals
* ❌ Cyclic Sort
* …
* 🧩 Hard Challenges (not started)

Additionally, commit history gives fine-grained timestamps of when each problem was solved.

---

## Learning Notes & Reflections

In `NOTES.md` I’ll reflect on:

* How I recognized a pattern in a new problem
* Key insights or “aha” moments
* Alternative approaches, optimizations, and trade-offs
* Common pitfalls and edge cases
* How often I revisit or re-solve problems to reinforce pattern recognition

Sample entry:

> **Pattern:** Sliding Window — Longest Substring with K Distinct
> **Initial approach:** Expand / contract window, maintain char counts
> **Challenges:** handling when window contracts, off-by-one indexing
> **Optimizations / reflection:** using a sliding window with hashmap and count management simplified the logic
> **Takeaway:** mapping substring / window problems to this pattern helps me quickly structure approach

---

## Future Plans

* Add versions of solutions in multiple languages (Python, Java, C++).
* Develop a “spaced repetition” script that picks problems I should re-solve periodically.
* Time myself on old problems to gauge improvement.
* Add tags or metadata (difficulty, time taken, notes) to each solution file or a tracking spreadsheet.
* Write mini-blog posts or deep dives for particularly challenging patterns.

---

 
[1]: https://www.designgurus.io/course/grokking-the-coding-interview "Grokking the Coding Interview: Patterns for Coding Questions | #1 Interview Prep Course"

