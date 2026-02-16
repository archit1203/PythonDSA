# Lists and Tuples in Python

## Lists

### Definition
- A **list** is a built-in data type that stores a **collection of values**.
- Elements can be of **different data types**.
- Lists are **mutable** (elements can be modified).

```python
student = ["Archit", 23, 8.5]
```
Properties
Elements can be modified:

```py
student[0] = "Arjun"
#Length of list:
len(student)
```

Slicing
Syntax: list[start : end] (end not included)

```py
marks = [87, 64, 33, 95, 76]

marks[1:4]     # [64, 33, 95]
marks[1:]      # [64, 33, 95, 76]
marks[-3:-1]   # [33, 95]
#Common List Methods
nums = [3, 1, 4]

nums.append(5)          # Add element at end
nums.sort()             # Sort ascending
nums.sort(reverse=True) # Sort descending
nums.reverse()          # Reverse list
nums.insert(1, 10)      # Insert at index
nums.remove(3)          # Remove element
nums.pop(2)             # Remove element at index
```

## Tuples

Definition:

A tuple is an ordered collection of values that is immutable (cannot be changed).

tup = (2, 1, 3, 1)
Properties
Elements cannot be modified:

***tup[0] = 10  ❌ Not allowed***
Tuple Methods

tup.index(1)   # Returns index of first occurrence

tup.count(1)   # Counts occurrences
