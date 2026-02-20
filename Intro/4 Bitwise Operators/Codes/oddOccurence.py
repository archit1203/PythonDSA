class Solution:
    def getOddOccurrence(self, arr):
        res=0
        for i in arr:
            res=res^i
        return res
