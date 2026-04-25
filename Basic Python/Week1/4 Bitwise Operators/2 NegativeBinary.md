# Representation of Negative Binary Numbers

## Why Do We Need Special Representation?
- Binary numbers use only **0 and 1**.
- We cannot directly use `+` or `-` signs.
- So, computers use a **sign bit (MSB)** to represent positive or negative numbers.

### Sign Bit
- `0` → Positive number  
- `1` → Negative number  

---

# Methods to Represent Negative Numbers

## 1️⃣ Signed Magnitude

### Concept
- MSB (Most Significant Bit) is the **sign bit**.
- Remaining bits represent the **magnitude**.

### Example (6-bit system)
- `0 01010` → +10  
- `1 01010` → -10  

### Range (n bits)
- Minimum: `-(2^(n-1) - 1)`
- Maximum: `+(2^(n-1) - 1)`

### Limitation
- Two representations of zero:
  - `+0` → `0 00000`
  - `-0` → `1 00000`

---

## 2️⃣ 1’s Complement

### Concept
- Positive numbers → Same as binary.
- Negative numbers → Take **1’s complement** (invert all bits).

### Example (5-bit system)
- +5 → `00101`
- -5 → `11010` (invert bits)

### Range (n bits)
- Minimum: `-(2^(n-1) - 1)`
- Maximum: `+(2^(n-1) - 1)`

### Limitation
- Two representations of zero:
  - `00000`
  - `11111`

---

## 3️⃣ 2’s Complement (Most Used)

### Concept
- Positive numbers → Same as binary.
- Negative numbers → Take **2’s complement**  
  (1’s complement + 1)

### Example
Find -5 (5-bit system):

Step 1: +5 → `00101`  
Step 2: 1’s complement → `11010`  
Step 3: Add 1 → `11011`  

So, -5 = `11011`

### Range (n bits)
- Minimum: `-(2^(n-1))`
- Maximum: `+(2^(n-1) - 1)`

### Advantages
- Only **one representation of zero**
- Simplifies arithmetic operations
- Used in modern computers

---

# Quick Python Demonstration

```python
# 2's complement of a number in n bits
def twos_complement(n, bits):
    if n >= 0:
        return format(n, f'0{bits}b')
    return format((1 << bits) + n, f'0{bits}b')

print(twos_complement(-5, 5))  # 11011
```
Conclusion

Signed Magnitude → Simple but has two zeros.

1’s Complement → Still has two zeros.

2’s Complement → Most efficient and widely used method.


- 2s Complement direct Formula: [2^n - x]
