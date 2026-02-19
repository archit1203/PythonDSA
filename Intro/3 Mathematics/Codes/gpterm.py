import math
class Solution:
    def termOfGP(self, a, b, n):
        r=(b/a)
        power=math.pow(r,n-1)
        return a*power
