class Solution:
    def josephus(self, n, k):
        li=[]
        for i in range(1,n+1):
            li.append(i)
        count=n
        i=0
        while len(li)>1:
            i=(i+k-1)%len(li)
            li.pop(i)
        return li[0]
