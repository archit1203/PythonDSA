class Solution:
    def RecursivePower(self, n, p):
        if p==0:
            return 1
        return n*self.RecursivePower(n, p-1)
        
