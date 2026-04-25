class Solution:
    def recursiveSum(self,n):
        if n==0:
            return 0
        return n+self.recursiveSum(n-1)
        
        
