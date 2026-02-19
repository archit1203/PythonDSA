import math
class Solution:
    def vowelCount(self, s):
        vow="aeiou"
        li={}
        count=[]
        count=0
        for i in range(len(s)):
            if s[i] in vow:
                count+=1
                if s[i] not in li:
                    li[s[i]]=1
                else:
                    li[s[i]]+=1
         
        if count==0:
            return 0
        res=1
        l2=[]
        for i in li.values():
            l2.append(i)
        
        for i in range(1,len(l2)+1):
            res=res*i
        

        for i in range(1,len(l2)+1):
            if l2[i-1]>1:
                res = res * ((l2[i-1]))
        
        
        return res
