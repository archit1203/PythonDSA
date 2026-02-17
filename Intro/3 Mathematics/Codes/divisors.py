#User function Template for python3
import math
class Solution:
    def print_divisors(self, N):
        n=N
        li=[]

        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                if n//i==i:
                    li.append(i)
                else:
                    li.append(i)
                    li.append(n//i)

        li.sort()
        
        for d in li:
            print(d, end=" ")
