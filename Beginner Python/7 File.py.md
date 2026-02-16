# File Handling in Python

## File Types
- **Text Files:** `.txt`, `.docx`
- **Binary Files:** `.mp4`, `.png`, `.jpeg`, `.mov`

---

## Opening a File
- Syntax:
```python
f = open("file_name", "mode")
File Modes
'r' → Read (default)

'w' → Write (overwrite)

'a' → Append

'x' → Create new file

'b' → Binary mode

't' → Text mode (default)

'+' → Read and write

Reading from a File
f = open("demo.txt", "r")

data = f.read()        # Read entire file
line = f.readline()    # Read one line

f.close()
Writing to a File
# Write (overwrite)
f = open("demo.txt", "w")
f.write("Hello Archit")
f.close()

# Append
f = open("demo.txt", "a")
f.write("\nNew line added")
f.close()
Using with Statement (Recommended)
Automatically closes the file.

with open("demo.txt", "a") as f:
    f.write("Hello Archit")
Deleting a File
import os
os.remove("demo.txt")
