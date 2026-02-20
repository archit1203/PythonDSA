class Solution:
    def countDigits(self, n):
        count=0
        if n<10:
            return 1
        count+=1
        return count+self.countDigits(n//10)
