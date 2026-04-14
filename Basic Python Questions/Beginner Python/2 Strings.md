# Strings and Conditional Statements (Python)

## Strings
- A **string** is a sequence of characters enclosed in quotes.
- Strings are **immutable** (cannot be modified after creation).

```python
s = "Hello"
Basic Operations

# Concatenation
result = "Hello" + " World"

# Length of string
length = len(s)
```

Indexing and Slicing
Indexing
Used to access individual characters.

```py
s = "Archit_Srivastava"
print(s[0])   # A
```
Strings cannot be modified using indexing (s[0] = 'B' not allowed).

Slicing
Used to extract a part of a string.

Syntax: str[start : end] (end not included)

```py
s = "Archit_Srivastava"

print(s[0:4])   # Arch
print(s[:4])    # Arch
print(s[1:])    # rchit_Srivastava
Negative Indexing
s = "Apple"
print(s[-3:-1])   # pl
```

Common String Functions
```py
s = "archit coder"
s.endswith("er")      # True if string ends with "er"
s.capitalize()        # Capitalizes first character
s.replace("coder", "developer")
s.find("co")          # Returns first index
s.count("e")          # Counts occurrences
```

Conditional Statements
```
Syntax
if condition:
    statement
elif condition:
    statement
else:
    statement
```
Example — Grading System

```py
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)
```
