# Big-O Notation

### What is Big-O?
- **Big-O notation** describes the **upper bound ( worst-case )** time or space complexity of an algorithm.
- It represents the **asymptotic growth rate**, not the exact running time.
- Helps compare the efficiency of different algorithms independent of hardware.

**Definition:**  
\(f(n) = O(g(n))\) if there exist constants **c > 0** and **n₀** such that  
\(f(n) \le c \cdot g(n)\) for all \(n \ge n₀\)

---

#### Quick Method to Find Big-O
- Ignore **lower-order terms**
- Ignore **constant factors**
- Keep only the **dominant (highest-growth) term**

**Examples**
- \(3n^2 + 2n + 1000\log n + 5000 \rightarrow O(n^2)\)
- \(3n^3 + 2n^2 + 5n + 1 \rightarrow O(n^3)\)

---

#### Important Properties
- **Reflexive:** \(f(n) = O(f(n))\)
- **Transitive:** If \(f(n)=O(g(n))\) and \(g(n)=O(h(n))\), then \(f(n)=O(h(n))\)
- **Constant factor:** If \(f(n)=O(g(n))\), then \(c f(n)=O(g(n))\)
- **Sum rule:** \(f(n)+h(n)=O(\max(g(n),k(n)))\)
- **Product rule:** \(f(n) \cdot h(n)=O(g(n)\cdot k(n))\)

---

#### Common Big-O Complexities (Small → Large)
- **O(1)** — Constant
- **O(log n)** — Logarithmic (Binary Search)
- **O(n)** — Linear (Linear Search)
- **O(n log n)** — Efficient sorting (Merge Sort, Heap Sort)
- **O(n²)** — Quadratic (Bubble Sort)
- **O(n³)** — Cubic (Naive Matrix Multiplication)
- **O(2ⁿ)** — Exponential (Subset generation)
- **O(n!)** — Factorial (Permutations)

---

#### Relation with Other Notations
- **Big-O (O)** → Upper bound (worst case)
- **Omega (Ω)** → Lower bound (best case)
- **Theta (Θ)** → Exact bound (tight bound)

If  
\(f(n)=O(g(n))\) **and** \(f(n)=Ω(g(n))\)  
then  
\(f(n)=Θ(g(n))\)


# Big-Omega Notation (Ω)

#### What is Big-Omega?
- **Big-Omega (Ω)** represents the **lower bound** of an algorithm’s time or space complexity.
- It describes the **best-case performance** or the **minimum time** an algorithm will take.
- Used to guarantee that an algorithm will take **at least a certain amount of time**.

**Definition:**  
\(f(n) = Ω(g(n))\) if there exist constants **c > 0** and **n₀** such that  
\(f(n) \ge c \cdot g(n)\) for all \(n \ge n₀\)

---

#### Key Points
- Shows how fast a function grows **from below**.
- Every algorithm has a trivial lower bound of **Ω(1)**, but tighter bounds are preferred.
- Determined by analyzing the **minimum number of operations** performed by the algorithm.

---

#### Example
- Nested loops printing all pairs of an array execute about **n²** operations.  
- Hence, the running time is at least **Ω(n²)**.

---

#### Big-Omega vs Little-Omega
- **Ω(g(n))** → Function grows **at least as fast** as \(g(n)\) (lower bound)
- **ω(g(n))** → Function grows **strictly faster** than \(g(n)\)

# Big-Theta Notation (Θ)

#### What is Big-Theta?
- **Big-Theta (Θ)** represents the **exact bound** of an algorithm’s complexity.
- It provides **both upper and lower bounds**, giving the **tight (precise) growth rate**.
- Commonly associated with the **average-case complexity** when input distribution is known.

**Definition:**  
\(f(n) = Θ(g(n))\) if there exist constants **c₁, c₂ > 0** and **n₀** such that  
\[
c_1 g(n) \le f(n) \le c_2 g(n) \quad \text{for all } n \ge n_0
\]

---

#### Key Points
- Describes the **exact asymptotic growth** of an algorithm.
- Indicates the algorithm runs **at the same order of growth** as \(g(n)\).
- More precise than **O (upper bound)** and **Ω (lower bound)**.

---

#### Example
- **Linear Search (average case):**  
  When all positions are equally likely, average comparisons ≈ **n/2**  
  After ignoring constants → **Θ(n)**

---

#### When to Use Θ Notation
- When both **upper and lower bounds** are known.
- When the **average-case performance** of the algorithm needs to be represented precisely.

# Understanding Time Complexity

#### Key Idea
- **Time complexity** measures how the **number of operations grows** with input size, not the actual execution time.
- Actual running time depends on **machine, compiler, and system load**, but time complexity remains the same.

---

#### Simple Intuition (Pen Search Example)
- **O(n²)** → Asking each person and also asking them about everyone else
- **O(n)** → Asking each person one by one
- **O(log n)** → Repeatedly dividing the group into halves (binary search approach)

---

#### Basic Examples

- **Constant Time — O(1)**  
  Executing a statement once (e.g., print once)

- **Linear Time — O(n)**  
  Loop running **n** times (e.g., printing a message n times, summing array elements)

- **Quadratic Time — O(n²)**  
  Nested loops (e.g., iterating through an n × n matrix)

---

#### How to Determine Time Complexity
- Count how many times key operations execute.
- Express the number of operations as a function of **n**.
- Keep the **dominant term** and ignore constants.

**Examples**
- Sum of array elements → **O(n)**
- Sum of matrix elements (n × m) → **O(n·m)**

---

#### Conclusion
- Time complexity focuses on **growth rate of operations**, not actual runtime.
- As input size increases, algorithms with **lower complexity scale better**.
