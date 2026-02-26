In a coding exam, you won’t be told “use Catalan numbers.” You have to **recognize the pattern** from the way the problem is described. Let me show you how to spot it.

---

## 🧩 How the Problem is Usually Worded
> *N people are sitting around a circular table. Each person must shake hands with exactly one other person. Handshakes cannot cross. Find the number of possible ways to arrange the handshakes.*

---

## 🔑 How to Recognize It’s Catalan
1. **Circle + non‑crossing condition**  
   Whenever you see “arrangements without crossing” (chords in a circle, balanced parentheses, binary tree structures), it’s a strong hint that the problem is related to **Catalan numbers**.

2. **Pairing people**  
   Each handshake pairs two people. If there are `N` people, there must be `N/2` pairs.  
   - If `N` is odd → impossible (one person left out).  
   - If `N` is even → possible.

3. **Recursive structure**  
   Pick one person (say person 1). Whoever they shake hands with splits the circle into two smaller groups.  
   - The number of ways = sum of (ways to arrange left group × ways to arrange right group).  
   - This recursive splitting is exactly the Catalan recurrence.

---

## 🧠 The Connection
- Non‑crossing handshakes = **non‑crossing partitions of a circle**.  
- That’s one of the classic definitions of Catalan numbers.  
- So the answer is:
  - `0` if `N` is odd  
  - `Catalan(N/2)` if `N` is even  

---
## ✅ Takeaway for Exams
- If you see **non‑crossing pairings, balanced parentheses, binary trees, triangulations of polygons, or ways to nest structures** → think **Catalan numbers**.  
- That’s the mental shortcut: these problems all boil down to the same recursive structure.

---

Would you like me to give you a **list of common exam problems that secretly use Catalan numbers** (like balanced parentheses, binary search trees, polygon triangulations), so you can spot them faster?
