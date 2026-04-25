class Solution:
    def digitalRoot(self, n):
        if n<10:
            return n
        sum=n%10+self.digitalRoot(n//10)
        if sum<10:
            return sum
        else:
            return sum%10+self.digitalRoot(sum//10)

