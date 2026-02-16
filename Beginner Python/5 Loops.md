# Loops in Python

## While Loop
- Executes a block of code **as long as the condition is True**.

```python
# Print "hello" five times
i = 1
while i <= 5:
    print("hello")
    i += 1
# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
For Loop
Used for sequential traversal of lists, strings, tuples, etc.

nums = [1, 2, 3, 4]
for el in nums:
    print(el)
for-else
The else block runs when the loop completes normally (not when break is used).

for i in range(5):
    print(i)
else:
    print("Loop finished")
Break and Continue
Break
Terminates the loop immediately.

for i in range(10):
    if i == 5:
        break
    print(i)
Continue
Skips the current iteration and moves to the next.

for i in range(6):
    if i == 3:
        continue
    print(i)
range() Function
Generates a sequence of numbers.

Syntax: range(start, stop, step)

for i in range(1, 6):
    print(i)   # 1 to 5
pass Statement
A null statement that does nothing.

Used as a placeholder.

for i in range(5):
    pass
