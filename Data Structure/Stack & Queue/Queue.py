"""
QUEUE

FIFO Linear Data structure

Operations
1. enqueue()
2. dequeue()
3. isEmpty()
4. isFull()


Applications
Synchronisation
OS
Computer Network

Queue in Python
list
Collections.deque
queue.Queue -> multithreaded enviornment
Own implementation
"""


#Using List
q=[]

q.append(10)
q.append(20)
q.append(30)

print(q)
print(q.pop())

q.append(40)
print(q.pop())


