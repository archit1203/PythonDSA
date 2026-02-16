# Object-Oriented Programming (OOP) in Python

## Object-Oriented Programming
- **OOP** uses **objects** to model real-world entities in code.
- Helps achieve **modularity, reusability, and better organization**.

---

## Class and Object
- **Class:** Blueprint for creating objects.
- **Object (Instance):** A specific instance created from a class.

```python
class Student:
    pass

s1 = Student()   # Object creation
Attributes
Class Attributes: Shared by all objects.

Instance Attributes: Unique to each object.

class Student:
    school = "ABC School"   # Class attribute

    def __init__(self, name):
        self.name = name    # Instance attribute
Constructor (__init__)
Automatically called when an object is created.

Used to initialize object attributes.

self refers to the current object.

class Student:
    def __init__(self, name):
        self.name = name
Methods
Functions defined inside a class.

class Student:
    def greet(self):
        print("Hello", self.name)
Static Methods
Methods that do not use self.

Declared using @staticmethod.

class Student:
    @staticmethod
    def info():
        print("This is a static method")
Important OOP Concepts
Abstraction
Hiding internal implementation details and showing only essential features.

Encapsulation
Wrapping data and methods into a single unit (object).
