**How to recognize Josephus pattern problems in a coding exam**, since you won’t be explicitly told “this is Josephus.”

---

## 🧩 Clues That It’s Josephus
When reading the problem statement, look for these signals:

- **Circle setup**: People/items arranged in a circle or loop.
- **Step elimination**: Every *k‑th* person/item is removed.
- **Survivor asked**: The problem asks for the last remaining person/item (the “safe position”).
- **Repeated elimination**: The process continues until only one is left.
- **Indexing detail**: Sometimes the problem says “starting from 1” or “starting from 0” — this tells you whether the answer should be 1‑indexed or 0‑indexed.

---

## 🔑 Typical Wording in Exams
- “N people standing in a circle, every k‑th person is eliminated. Find the survivor.”  
- “Safe position in a circular elimination game.”  
- “Last person remaining after repeatedly removing every k‑th element.”  
- “Circular game problem.”  
- “Hot potato / musical chairs variant.”  

All of these are **Josephus problem disguises**.

---

## 🧠 How to Decide Quickly
- If you see **circle + elimination + survivor** → it’s Josephus.  
- If elimination is **every k‑th step** → use Josephus recurrence.  
- If they ask for **order of elimination** → simulate with a list.  
- If they ask for **final survivor only** → use the formula (recursive or iterative).

---

## 🚨 Common Mistakes in Exams
- Forgetting to update the index after elimination (like your earlier code).  
- Confusing 0‑index vs 1‑index answers.  
- Trying to simulate with lists for large `n` → too slow.  
- Not recognizing the problem as Josephus and wasting time on brute force.

---

## 📝 Quick Mental Notes
- Survivor position = **Josephus recurrence**.  
- Formula: \( J(n, k) = (J(n-1, k) + k) \mod n \).  
- Base case: \( J(1, k) = 0 \).  
- Add +1 at the end if answer must be 1‑indexed.  
- Iterative version is safest in exams (no recursion depth issues).

---

👉 So in an exam, as soon as you see **circle + elimination + survivor**, you should immediately think: *“This is Josephus — use the recurrence.”*  

Would you like me to also give you a **short checklist of exam problems that look different but secretly reduce to Josephus** (like hot potato, musical chairs, or circular linked list elimination)?
