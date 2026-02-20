class Solution:
    def sumOfDigits(self, n):
        if n==0:
            return 0
        temp=n%10
        return temp+self.sumOfDigits(n//10)
