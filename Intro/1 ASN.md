# Introduction to Analysis of Algorithms
## What is Algorithm Analysis?
- **Algorithm analysis** is the process of evaluating the performance of an algorithm.
- It helps us understand how efficiently an algorithm uses **time** and **memory**.
- The goal is to compare different algorithms and choose the **most efficient solution** for a problem.
## Why Do We Analyze Algorithms?
- To predict **performance before implementation**
- To select the **best approach** among multiple solutions
- To design **scalable programs** that work efficiently even for large inputs
## Key Focus Areas
- **Time Complexity** – How execution time grows with input size
- **Space Complexity** – How memory usage grows with input size
## Order of Growth
- Let **f(n)** and **g(n)** be running times of two algorithms.
- **f(n)** grows faster than **g(n)** if:
\[ \lim_{n \to \infty} \frac{g(n)}{f(n)} = 0 \]
---
### Quick Method to Find Order of Growth
- Ignore **lower-order terms**
- Ignore **constant factors**
**Examples**
- \(4n^2 + 3n + 100 \rightarrow n^2\)
- \(100n\log n + 3n + 100\log n + 2 \rightarrow n\log n\)
---
### Standard Growth Order (Small → Large)
\[ c < \log\log n < \log n < n^{1/2} < n < n\log n < n^2 < n^3 < 2^n < n^n \]
# Asymptotic Notations
## Overview
- **Asymptotic analysis** measures algorithm efficiency **independent of machine-specific constants**.
- It evaluates how **time and space complexity grow as input size (n) increases**.
- Used to compare algorithms without implementing them.
---
## Main Asymptotic Notations
### 1. Theta Notation — Θ(g(n))
- Represents the **exact bound** (both upper and lower bound).
- Used when the growth rate of the algorithm is known precisely.
- Example: \(3n^3 + 6n^2 + 6000 = Θ(n^3)\)
--- 
### 2. Big-O Notation — O(g(n))
- Represents the **upper bound** (worst-case complexity).
- Most commonly used notation.
- Example: Insertion Sort worst case → **O(n²)**
---
### 3. Omega Notation — Ω(g(n))
- Represents the **lower bound** (best-case complexity).
- Example: Insertion Sort best case → **Ω(n)**
---
## Key Relationships
- If **f(n) = O(g(n))** and **f(n) = Ω(g(n))**, then **f(n) = Θ(g(n))**
- If **f(n) = O(g(n))**, then  **g(n) = Ω(f(n))**
---
## Important Properties (Quick View)
- **Constant factor rule:**  
  If \(f(n) = O(g(n))\), then \(a·f(n) = O(g(n))\)
- **Transitive rule:**  
  If \(f(n)=O(g(n))\) and \(g(n)=O(h(n))\), then \(f(n)=O(h(n))\)
- **Reflexive rule:**  
  \(f(n)=O(f(n))\), \(Θ(f(n))\), \(Ω(f(n))\)
- **Symmetry (Θ only):**  
  If \(f(n)=Θ(g(n))\), then \(g(n)=Θ(f(n))\)
