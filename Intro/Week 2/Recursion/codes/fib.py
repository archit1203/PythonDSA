class Solution:
    def nthFibonacci(self, n):
        n1=0
        n2=1
        if n<=1:
            return n
        return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
