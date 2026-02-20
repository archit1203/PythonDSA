# Common Built-in Binary Functions in Python

These built-in functions help in **binary representation and bit manipulation**.

---

## 1️⃣ `bin()`
- Converts an integer to binary string.
- Adds prefix `0b`.

```python
bin(10)      # '0b1010'
```
2️⃣ format()

Converts number into formatted binary (no 0b prefix).
```
format(10, 'b')     # '1010'
format(10, '08b')   # '00001010' (8-bit format)
```
3️⃣ int()

Converts binary string to integer.
```
int('1010', 2)   # 10
```
4️⃣ bit_length()

Returns number of bits required to represent the number in binary.

```
n = 10
n.bit_length()   # 4
```
5️⃣ bit_count() (Python 3.8+)

Counts number of set bits (1s).
```
n = 10
n.bit_count()   # 2
```
6️⃣ oct()

Converts number to octal.

```oct(10)   # '0o12' ```

7️⃣ hex()

Converts number to hexadecimal.

```hex(10)   # '0xa' ```

8️⃣ ord() and chr()

Useful for ASCII / Unicode conversions.
```
ord('A')   # 65
chr(65)    # 'A'
```
