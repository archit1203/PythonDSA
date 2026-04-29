import math

class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self,k):
        temp=Node(k)
        temp.next=self.head
        self.head=temp
        self.size=self.size+1

    def size(self):
        return self.size

    def peek(self):
        if self.head==None:
            return math.inf
        return self.head.key
    
    def pop(self):
        if self.head==None:
            return math.inf
        res=self.head.key
        self.head=self.head.next
        self.size=self.size-1
        return res
    


s=stack()
s.push(10)
s.push(20)
print(s.pop())