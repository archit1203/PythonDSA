class Solution:
    '''def isPalindrome(self, n):
		num=str(n)
		num2=num[::-1]
		if num==num2:
		    return True
		else:
		    return False'''
		    
		    
    def isPalindrome(self, n):
        original=n
        rev=0
        
        while n>0:
            temp=n%10
            rev=rev*10+temp
            n//=10
        
        return original==rev
