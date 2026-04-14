class Solution:
    def possibleWords(self, arr):
        mapping = {
            2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"
        }
        
        res=[""]
        
        for i in arr:
            if i not in mapping:
                continue
            temp=[]
            for j in res:
                for ch in mapping[i]:
                    temp.append(j+ch)
            res=temp
        return res
        
