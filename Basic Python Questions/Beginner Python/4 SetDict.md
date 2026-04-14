# Dictionaries and Sets in Python

## Dictionaries

### Definition
- A **dictionary** stores data in **key : value** pairs.
- Dictionaries are **unordered**, **mutable**, and **do not allow duplicate keys**.

```python
student = {
    "name": "Archit",
    "age": 23,
    "cgpa": 8.5
}
Adding / Updating Values
student["city"] = "Delhi"     # Add new key-value
student["age"] = 24           # Update value
Nested Dictionary
student = {
    "name": "Archit",
    "marks": {
        "math": 90,
        "science": 85
    }
}
Dictionary Methods
student.keys()      # Returns all keys
student.values()    # Returns all values
student.items()     # Returns (key, value) pairs
student.get("name") # Returns value of key
student.update({"age": 25})  # Update dictionary
```

##Sets

Definition

A set is a collection of unordered, unique elements.

Duplicate values are automatically removed.

```py
nums = {1, 2, 3, 3, 2}
# Result → {1, 2, 3}
Empty Set
empty_set = set()
Set Methods
s = {1, 2, 3}

s.add(4)                 # Add element
s.remove(2)              # Remove element
s.pop()                  # Remove random element
s.clear()                # Empty set

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.union(s2)             # Combine sets
s1.intersection(s2)      # Common elements
