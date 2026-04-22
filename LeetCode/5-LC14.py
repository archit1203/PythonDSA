class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=""

        min_len=len(strs[0])
        mi=strs[0]
        for i in range(len(strs)):
            if min_len>len(strs[i]):
                min_len=len(strs[i])
                mi=strs[i]
        for i in range(min_len):
            ch=mi[i]
            for j in range(len(strs)):
                if strs[j][i] != ch:
                    return mi[:i]
                    
        return mi
"""        sh=min(strs,key=len)
        for i in range(len(sh)):
            char=sh[i]
            for s in strs:
                if s[i]!=char:
                    return sh[:i]
        return sh"""




        