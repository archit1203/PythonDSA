class Solution:
    def powerSet(self, s):
        if not s:
            return [""]
        sub=[""]
        for ch in s:
            sub+=[sb+ch for sb in sub]
        return sub
