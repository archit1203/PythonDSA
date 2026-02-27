# Python Lists – Quick Notes

## What is a List?
A **list** is a built-in data structure that stores an **ordered collection of items**.

### Properties
- Ordered (maintains insertion order)
- Mutable (can modify elements)
- Allows duplicates
- Index-based (starts from 0)
- Can store mixed data types

---

## Creating Lists

### 1️⃣ Using Square Brackets
```python
a = [1, 2, 3]
b = ["apple", "banana"]
c = [1, "hello", 3.14, True]
```
2️⃣ Using list() Constructor
```
a = list((1, 2, 3))
b = list("ABC")
```
3️⃣ Repeated Elements
```
a = [2] * 5
#Accessing Elements
a = [10, 20, 30, 40, 50]

print(a[0])     # First element
print(a[-1])    # Last element
print(a[1:4])   # Slicing
Adding Elements
a = []

a.append(10)        # Add single element
a.insert(0, 5)      # Insert at index
a.extend([15, 20])  # Add multiple elements
a.clear()           # Remove all elements
#Updating Elements
a = [10, 20, 30]
a[1] = 25
#Removing Elements
a = [10, 20, 30, 40]

a.remove(30)   # Remove by value
a.pop(1)       # Remove by index
del a[0]       # Delete by index
```
Iterating Over List
```
a = ["apple", "banana"]

for item in a:
    print(item)
Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])
List Comprehension
squares = [x**2 for x in range(1, 6)]
```
Memory Note

-Lists store references to objects, not actual values.

-Mutable objects inside lists can change original data.

Lists are:

-Flexible

-Dynamic

-Most commonly used data structure in Python
