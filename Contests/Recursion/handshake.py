#User function Template for python3
def catalan(n):
    if n<=1:
        return 1
    res=0
    for i in range(n):
        res+=catalan(i)*catalan(n-1-i)
    return res

class Solution:
    def count(self, N):
        if N%2==1:
            return 0
        k=N//2
        return catalan(k)
        '''n=N
        count=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if j-i==1:
                    count+=1
        return count'''
