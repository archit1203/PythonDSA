# Tuple Slicing in Python

## What is Tuple Slicing?
Tuple slicing allows you to extract a **sub-part of a tuple** using index ranges.

> Tuples are **immutable**, but slicing creates a **new tuple**.

---

## Syntax

#####tuple[start : stop : step]

start → starting index (inclusive), default = 0

stop → ending index (exclusive)

step → increment value, default = 1

Basic Examples
```
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tup[2:6])   # (2, 3, 4, 5)
print(tup[:4])    # (0, 1, 2, 3)
print(tup[5:])    # (5, 6, 7, 8, 9)
print(tup[:])     # Entire tuple

#Using Negative Indices
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tup[-3:])     # (7, 8, 9)
print(tup[:-3])     # (0, 1, 2, 3, 4, 5, 6)
print(tup[-3:-1])   # (7, 8)
```

Negative indexing starts from the end (-1 is last element).

Using Step
```
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tup[1:8:2])   # (1, 3, 5, 7)
print(tup[::-1])    # Reverse tuple
```
Key Points

Slicing does not modify the original tuple.

stop index is not included.

Step can be negative to reverse.

Works same as string slicing.


# Python List Slicing

## 🔹 Syntax

python
list_name[start : end : step]

start → inclusive (default = 0)

end → exclusive (default = len(list))

step → interval (default = 1)

🔹 Basic Example
```
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])   # [2, 3, 4]
```
🔹 Get All Elements
```
print(a[:])     # Entire list
print(a[::])    # Same as above
```
🔹 Before / After Specific Index
```
print(a[2:])    # From index 2 to end
print(a[:3])    # From start to index 3 (exclusive)
```
🔹 Between Two Positions
```
print(a[1:4])   # [2, 3, 4]
```
🔹 Using Step
```
print(a[::2])       # Every 2nd element
print(a[1:8:3])     # Step of 3
```
🔹 Negative Indexing
```
print(a[-2:])       # Last 2 elements
print(a[:-3])       # All except last 3
print(a[-4:-1])     # From -4 to -1 (exclusive)
print(a[-8:-1:2])   # Step with negative indices
```
🔹 Out-of-Bound Slicing
```
print(a[7:15])   # No error, returns available elements
```
Python safely adjusts out-of-range indices.

🔹 Reverse List
print(a[::-1])   # Reverse list
🔹 Key Points

end index is not included

Works on lists, strings, tuples

Negative step reverses direction

Does not modify original list (creates new list)


# String Slicing in Python

## 🔹 Syntax

```python
substring = s[start : end : step]
```
start → inclusive (default = 0)

end → exclusive (default = len(s))

step → interval (default = 1)

Always returns a new string

🔹 Basic Example
```
s = "Hello, Python!"
print(s[0:5])   # Hello
```
🔹 Get Entire String
```
s = "Hello, World!"

print(s[:])
print(s[::])
```
🔹 Before / After Specific Index
```
s = "Hello, World!"

print(s[7:])   # From index 7 to end
print(s[:5])   # From start to index 5 (exclusive)
```
🔹 Between Two Positions
```
s = "Hello, World!"
print(s[1:5])   # ello
```
🔹 Using Step
```
s = "abcdefghi"

print(s[::2])      # acegi
print(s[1:8:3])    # beh
```
🔹 Negative Indexing
```
s = "abcdefghijklmno"

print(s[-4:])       # lmno
print(s[:-3])       # abcdefghijkl
print(s[-5:-2])     # klm
print(s[-8:-1:2])   # hjln

#-1 represents last character.
```
🔹 Reverse a String
```
s = "Python"

print(s[::-1])   # nohtyP
```
🔹 Key Points

end index is not included

Works same as list & tuple slicing

Negative step reverses direction

Strings are immutable (original string unchanged)

# List Comprehension in Python

## 🔹 What is List Comprehension?

A concise way to create a new list by applying an expression to each item in an iterable.

It combines:
- Looping
- Transformation
- Optional filtering  
in a single line.

---

## 🔹 Syntax

```python
[expression for item in iterable if condition]
```

expression → operation to perform

item → current element

iterable → list, tuple, range, etc.

if condition → optional filter

🔹 Basic Example
```
a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)
# [4, 9, 16, 25]
```
🔹 For Loop vs List Comprehension
Using For Loop
```
a = [1, 2, 3]
res = []
for val in a:
    res.append(val * 2)
print(res)
```
Using List Comprehension
```
a = [1, 2, 3]
res = [val * 2 for val in a]
print(res)
```
🔹 With Condition (Filtering)
```
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)
# [2, 4]
```
🔹 Create List from Range
```
nums = [i for i in range(10)]
print(nums)
```
🔹 Nested Loops
```
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)
```
🔹 Flatten a Nested List
```
mat = [[1, 2], [3, 4], [5, 6]]
res = [val for row in mat for val in row]
print(res)
```
🔹 Why Use It?

Cleaner code

More readable

Often faster than loops

Reduces temporary variables

🔹 Key Points

Returns a new list

Does not modify original iterable

Can include conditions and nested loops

Improves code conciseness
