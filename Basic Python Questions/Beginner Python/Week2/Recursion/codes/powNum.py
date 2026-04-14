def rev(n,r=0):
    if n==0:
        return r
    return rev(n//10,r*10+n%10)
    

class Solution:
    def reverseexponentiation(self, n):
        r=rev(n)
        return pow(n,r)
        
        
        """num=n
        rev=0
        while(num>0):
            rev=rev*10+num%10
            num//=10
        return pow(n,rev)"""
