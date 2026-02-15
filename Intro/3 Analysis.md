  # Analysis of Loops in Algorithms

## Steps to Analyze a Loop
- Determine the **number of iterations**
- Count **operations per iteration**
- Express total operations as a function of **n**
- Keep the **dominant term** to determine complexity

---

## Common Loop Time Complexities (Python Examples)

### O(1) — Constant Time
```python
for i in range(10):
    print("Hello")
```
### O(n) — Linear Time
```python
for i in range(n):
    print(i)
O(n²) — Quadratic Time (Nested Loops)
for i in range(n):
    for j in range(n):
        print(i, j)
```
### O(log n) — Logarithmic Time
```python
i = 1
while i < n:
    print(i)
    i *= 2
```
O(log log n) — Log-Log Time
```python
i = 2
while i < n:
    print(i)
    i = i ** 2
```
### Combining Loop Complexities
#### Consecutive Loops → Add
```python 
for i in range(n):
    print(i)
    
for j in range(n):
    print(j)
```
Time Complexity → O(n)

### Nested Loops → Multiply
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
Time Complexity → O(n²)

# Time Complexity Analysis of Recursive Functions

## Recurrence Relations
- Recursive algorithms often lead to a **recurrence relation**.
- A recurrence expresses running time **T(n)** in terms of smaller inputs.
- Goal: find the **asymptotic growth** (Big-O) by solving the recurrence.

**Example (Divide and Conquer):**
- Merge Sort recurrence:  
  \(T(n) = 2T(n/2) + cn\)

---

## Example (Python)
```python
def fun(n):
    if n <= 1:
        return
    fun(n // 2)
    fun(n // 2)

    for i in range(n):
        print("Archit", end=" ")
```
Recurrence:

𝑇(𝑛)=2𝑇(𝑛/2)+𝑂(𝑛)

T(n)=2T(n/2)+O(n)

### Why Solve Recurrences?

Determines running time of recursive algorithms

Helps compare algorithm efficiency

Identifies performance bottlenecks

Useful for designing optimized algorithms

Methods to Solve Recurrence Relations
1. Substitution Method – Guess the solution and prove using induction
2. Recurrence Tree Method – Expand recurrence into a tree and sum costs
3. Master Theorem – Direct formula for recurrences of form
    𝑇(𝑛)=𝑎𝑇(𝑛/𝑏)+𝑓(𝑛)
    T(n)=aT(n/b)+f(n)


# Recursion Tree Method

## Idea
- The **recursion tree method** analyzes recursive algorithms by expanding the recurrence into a tree.
- Each **node** represents work done in one recursive call.
- Each **level** represents one stage of recursion.
- Total time = **sum of costs across all levels**.

---

## Steps to Use Recursion Tree Method
- Draw the recursion tree for the recurrence.
- Compute **cost at each level**.
- Determine the **number of levels (tree height)**.
- Sum the cost of all levels to get total complexity.

---

## Example 1: Equal Subproblems
```python
def fun(n):
    if n <= 1:
        return
    fun(n // 2)
    fun(n // 2)
    for i in range(n):
        print("Archit", end=" ")
```
Recurrence:
𝑇(𝑛)=2𝑇(𝑛/2)+𝑂(𝑛)T(n)=2T(n/2)+O(n)

Cost at each level = cn

Number of levels = log n

Total cost = cn × log n

Result:
𝑇(𝑛)=𝑂(𝑛log⁡𝑛)T(n)=O(nlogn)

Example 2: Unequal Subproblems
```python
def fun(n):
    if n <= 1:
        return
    fun(n // 4)
    fun(n // 2)

    for i in range(n):
        for j in range(n):
            print("Archit", end=" ")
```
Recurrence:

𝑇(𝑛)=𝑇(𝑛/4)+𝑇(𝑛/2)+𝑂(𝑛2)

T(n)=T(n/4)+T(n/2)+O(n^2)
Result:

𝑇(𝑛)=𝑂(𝑛2)

T(n)=O(n^2)
Key Note:
-For equal splits, each level often has the same cost.
-For unequal splits, assume the deepest possible tree to obtain a valid upper bound.

# Time and Space Complexity

## Overview
- Used to compare different algorithms based on **efficiency**.
- Measured in terms of **input size (n)** and independent of machine configuration.
- Focuses on **order of growth**, not exact execution time.

---

## Time Complexity
- Measures how the **number of operations** grows with input size.
- Estimated by counting how many times key instructions execute.

### Example 1 — Constant Time O(1)
```python
def add(a, b):
    return a + b
```
Example 2 — Quadratic Time O(n²)
```py
def find_pair(arr, z):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] + arr[j] == z:
                return True
    return False
```
Example 3 — Tricky Case (Geometric Reduction → O(n))
```py
count = 0
i = n
while i > 0:
    for j in range(i):
        count += 1
    i //= 2
```
Total operations → n+n/2+n/4+...≈2n → O(n)

Space Complexity
Measures memory used by the algorithm as input size grows.

Consists of:

Fixed part: variables, constants, instructions

Variable part: recursion stack, dynamic data structures

Example — Linear Space O(n)
```py
def count_freq(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq
```
Auxiliary Space
Extra memory used excluding input storage.

Example: freq dictionary above uses O(n) auxiliary space.

Key Idea
Time Complexity → speed growth

Space Complexity → memory growth

Efficient algorithms aim for lower time and space growth as input size increases.
