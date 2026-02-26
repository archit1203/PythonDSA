#User function Template for python3

class Solution:
    def safePos(self, n, k):
        li=[]
        for i in range(1,n+1):
            li.append(i)
        i=0
        while(len(li)!=1):
            kill=(i+k-1)%len(li)
            li=li[:kill]+li[kill+1:]
            i=kill
        return li[0]
