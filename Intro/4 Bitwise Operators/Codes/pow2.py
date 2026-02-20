class Solution:
    def isPowerofTwo(self, n):
        x=n.bit_count()
        if x==1:
            return True
        return False
