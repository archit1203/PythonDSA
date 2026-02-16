# Functions and Recursion in Python

## Functions in Python
- A **function** is a block of code that performs a specific task.
- Improves **code reuse** and **modularity**.

### Function Structure
```python
def func_name(param1, param2):
    # some work
    return value
Function Call
func_name(arg1, arg2)
Example
def add(a, b):
    return a + b

print(add(2, 3))
Types of Functions
Built-in Functions: print(), range(), len()

User-defined Functions: Created using def

Default Parameters
A parameter can have a default value, used when no argument is passed.

def greet(name="Archit"):
    print("Hello", name)

greet()        # Hello Archit
greet("Ravi")  # Hello Ravi
Recursion
Recursion occurs when a function calls itself.

Must include a base condition to stop recursion.

Example — Print Numbers from n to 1
def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)
Example — Factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
