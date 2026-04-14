import math

class Solution:
    def isPrime(self,n):
        if n==2 or n==3:
            return True
        if(n%2==0):
            return False
        #print(m)
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i==0:
                return False
        return True
