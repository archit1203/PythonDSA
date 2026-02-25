#User function Template for python3
import math

class Solution:
    def findPermutation(self, s):
        if len(s)==1:
            return [s]
        res=set()
        for i in range(len(s)):
            rem=s[:i]+s[i+1:]
            for p in self.findPermutation(rem):
                res.add(s[i]+p)
        return list(res)
