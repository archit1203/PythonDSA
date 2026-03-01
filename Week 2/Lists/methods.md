# List ethods
**append(x)**  
Inserts `x` at the end of the list.

**insert(i, x)**  
Inserts `x` at index `i` and shifts subsequent elements to the right.

**remove(x)**  
Removes `x` from list and shifts subsequent elements to the left.

**pop(x)**  
Removes `x` from list and shifts subsequent elements to the left and return the value of `x`.

**del l[1] or del l[0:2]**
Removes the item of particular index from list.

=> Max, min etc kind of functions wont work if hetrogenous list.
**max(l)**

**min(l)**

**sum(l)**

**l.reverse()**

**l.sort()**

# Working of Lists in Python:

1. Adv: Random access , Cache Friendly
2. Dis: Insert, Delete, Search is Slow for unsorted
3. Dynamic memory allocation is done.
4. It preallocates some extra space, if it becomes full:
      a. Allocate new space of larger size
      b. Copy old space to new and free old space. 

# Slicing
> L [ start : stop : step ]

# Comprehension
```
l1 = [x for x in range(11) if x%2==0] #evenno
l2 = [x for x in range(11) if x%2!=0] #odd
```
