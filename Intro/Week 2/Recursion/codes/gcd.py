class Solution:
    def GCD(self,a,b):
        rem=a%b
        if rem==0:
            return b
        return self.GCD(b,a%b)
