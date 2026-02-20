# Introduction to Bitwise Algorithms

## What are Bitwise Operators?
- Operate directly on **binary bits (0 and 1)**.
- Used for **optimization, masking, toggling bits, encryption, compression**, etc.
- Faster for low-level manipulation.

---

## Main Bitwise Operators

| Operator | Symbol | Description |
|----------|--------|------------|
| AND      | `&`    | Sets bit if both bits are 1 |
| OR       | `|`    | Sets bit if at least one bit is 1 |
| XOR      | `^`    | Sets bit if bits are different |
| NOT      | `~`    | Inverts all bits |
| Left Shift  | `<<` | Shifts bits left (×2 per shift) |
| Right Shift | `>>` | Shifts bits right (÷2 per shift) |

---

## Basic Bitwise Examples

### AND (`&`)
``` 
a = 7   # 111
b = 4   # 100
print(a & b)   # 4
```
OR (|)
```
a = 12
b = 25
print(a | b)   # 29
XOR (^)
a = 12
b = 25
print(a ^ b)   # 21
NOT (~)
a = 0
print(~a)   # -1
```
#Shift Operators
Left Shift (<<)

Multiply by 2 for each shift.
```
num = 5
print(num << 1)   # 10
print(num << 2)   # 20
Right Shift (>>)
```
Divide by 2 for each shift.
```
num = 5
print(num >> 1)   # 2
print(num >> 2)   # 1
```
Common Bit Manipulation Problems
1. Set a Bit
```
def set_bit(num, pos):
    return num | (1 << pos)

print(set_bit(4, 1))   # 6
```
2. Unset (Clear) a Bit
```
def unset_bit(num, pos):
    return num & (~(1 << pos))

print(unset_bit(7, 1))   # 5
```
3. Toggle a Bit
```
def toggle_bit(num, pos):
    return num ^ (1 << pos)

print(toggle_bit(4, 1))   # 6
```
4. Check if Bit is Set
```
def is_set(num, pos):
    return (num & (1 << pos)) != 0

print(is_set(5, 0))   # True
```
5. Multiply by 2
```
num = 12
print(num << 1)   # 24
```
6. Divide by 2
```
num = 12
print(num >> 1)   # 6
```      
7. XOR from 1 to n
```
def xor_1_to_n(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

print(xor_1_to_n(5))
```
8. Check if Number is Power of 2
```
def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0

print(is_power_of_two(8))   # True
```
9. Count Set Bits
```
def count_bits(n):
    count = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count

print(count_bits(5))   # 2
```
10. Position of Rightmost Set Bit

```
def rightmost_set_bit(n):
    if n == 0:
        return 0
    pos = 1
    while (n & 1) == 0:
        n >>= 1
        pos += 1
    return pos

print(rightmost_set_bit(18))   # 2
```
Key Takeaways
-Bitwise operations are fast and memory-efficient.
-Frequently used in competitive programming and system-level code.
-Many bit tricks run in O(1) time and O(1) space.
