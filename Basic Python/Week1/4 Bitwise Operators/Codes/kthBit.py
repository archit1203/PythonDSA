def b(n):
    if n==0:
        return ""
    return b(n//2)+str(n%2)
    
class Solution:
    def checkKthBit(self, n, k):
        num=b(n)
        for i in range(len(num)):
            if i==k:
                if int(num[-(i+1)])==1:
                    return True
        return False
