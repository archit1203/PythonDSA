import math

class Node:
    def __init__(self,k):
        self.key=k
        self.next=None

class twostack:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=self.size
    
    def push1(self,k):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=k
            return True
        return False

    def push2(self,k):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=k
            return True
        return False

    def size1(self):
        return self.top1+1

    def size2(self):
        return self.size-self.top2
    
    def peek(self):
        if self.head==None:
            return math.inf
        return self.head.key
    
    def pop1(self):
        if self.top1>=0:
            x=self.arr[self.top1]
            self.top1=self.top1-1
            return x
        return None
    
    def pop2(self):
        if self.top2<self.size:
            x=self.arr[self.top2]
            self.top2=self.top2+1
            return x
        return None


s=twostack(5)
s.push1(10)
s.push2(70)
print(s.pop1())