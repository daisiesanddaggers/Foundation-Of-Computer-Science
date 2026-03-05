# 🪑 Classroom Seating Arrangement Problem

> **ST4015CMD – Foundation of Computer Science**
> Softwarica College of IT and E-Commerce (in collaboration with Coventry University)
> **Author:** Aayush Kadel (Student ID: 250573) | **Submitted to:** Rupak Rajbanshi | **Date:** 04 March 2026

---

## 📌 Overview

This project explores the **Classroom Seating Arrangement Problem** through the lens of computational complexity theory. Given a set of students with constraints (no friends sitting adjacent, no same-hometown neighbours), we implement and compare two algorithmic approaches:

| Approach | Strategy | Time Complexity |
|---|---|---|
| **Brute Force** | Try every permutation | O(n!) |
| **Heuristic** | Most-constrained student first + early pruning | O(n²) approx. |

The problem illustrates core **P vs NP** concepts — a valid arrangement is easy to *verify* but hard to *find* as class size grows.

---

## 🗂️ Project Structure

```
📦 classroom-seating/
├── brute_force.py       # Exhaustive search using itertools.permutations
├── heuristic.py         # Smart placement: most constrained first + pruning
└── README.md
```

---

## 🧠 Problem Definition

**Constraints:**
- Two students who are **friends** must NOT sit next to each other
- Two students from the **same hometown** must NOT sit next to each other

**Demo setup (5 students):**

| Student | Home City | Friend Pairs |
|---|---|---|
| Friend1 | Kathmandu | Friend3, Friend5 |
| Friend2 | Chitwan | Friend4 |
| Friend3 | Kathmandu | Friend1 |
| Friend4 | Pokhara | Friend2 |
| Friend5 | Lalitpur | Friend1 |

---

## ⚙️ How to Run

```bash
# Brute Force – tries all 120 permutations
python brute_force.py

# Heuristic – places most constrained students first
python heuristic.py
```

No external libraries required beyond Python's standard `itertools`.

---

## 🔨 Approach 1: Brute Force

Generates all `n!` permutations and validates each one against the constraints.

```python
from itertools import permutations

for one_arrangement in permutations(my_classmates):
    if check_if_arrangement_is_ok(one_arrangement):
        good_arrangements.append(one_arrangement)
```

**Result for 5 students:** 28 valid arrangements found out of 120 total.

**Why it fails at scale:**

| Students (n) | Permutations (n!) | Feasibility |
|---|---|---|
| 5 | 120 | Instant |
| 10 | 3,628,800 | Under 1 second |
| 15 | 1,307,674,368,000 | Several minutes |
| 20 | 2,432,902,008,176,640,000 | Billions of years |
| 30 | 265 undecillion+ | Exceeds age of universe |

---

## 💡 Approach 2: Heuristic (Smart)

Two strategies are combined:

**Strategy 1 – Most Constrained First**
Rank students by total constraints (friend pairs + same-city classmates). Place the hardest-to-seat students first to avoid dead ends.

**Strategy 2 – Early Pruning**
Before placing each student, check if they conflict with the *last seated person*. Skip immediately if they do — no need to explore further.

```python
def how_many_rules_apply(one_student):
    number_of_friends = sum(1 for a, b in friend_pairs if a == one_student or b == one_student)
    number_from_same_city = sum(1 for s in my_classmates if s != one_student and home_city[s] == home_city[one_student])
    return number_of_friends + number_from_same_city
```

**Execution trace (5 students):**

| Step | Student Tried | Decision | Row After Step |
|---|---|---|---|
| 1 | Friend1 | Placed (row empty) | Friend1 |
| 2 | Friend3 | Skipped — friends with Friend1 | Friend1 |
| 3 | Friend2 | Placed | Friend1 → Friend2 |
| 4 | Friend3 | Placed | Friend1 → Friend2 → Friend3 |
| 5 | Friend4 | Placed | Friend1 → Friend2 → Friend3 → Friend4 |
| 6 | Friend5 | Placed | Friend1 → Friend2 → Friend3 → Friend4 → Friend5 |

**Result:** Valid arrangement found in **6 steps** vs **120 steps** for brute force — a **95% reduction** in effort.

---

## 📊 P vs NP Connection

| Class | Solvable Efficiently? | Verifiable Efficiently? | Example |
|---|---|---|---|
| P | ✅ Yes (polynomial) | ✅ Yes | Sorting, searching |
| NP | ❓ Not necessarily | ✅ Yes (polynomial) | Seating arrangement, scheduling |
| NP-Complete | ❌ No known poly solution | ✅ Yes | Boolean satisfiability |

The seating arrangement problem behaves as an **NP problem** — checking a given layout is O(n), but finding one grows exponentially with class size.

---

## 📚 References

1. Cormen, T. H. et al. (2022) *Introduction to Algorithms*
2. Garey, M. R. and Johnson, D. S. (1979) *Computers and Intractability: A Guide to the Theory of NP-Completeness*
3. Russell, S. and Norvig, P. (2021) *Artificial Intelligence: A Modern Approach* — https://aima.cs.berkeley.edu/
4. MIT OpenCourseWare — Introduction to Algorithms: https://ocw.mit.edu
5. Stanford Encyclopedia of Philosophy — Computational Complexity Theory: https://plato.stanford.edu/entries/computational-complexity/
