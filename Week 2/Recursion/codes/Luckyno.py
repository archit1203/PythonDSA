class Solution:
    def isLucky(self, n): 
        step=2
        while step<=n:
            if n%step==0:
                return 0
            n-=n//step
            step+=1
        return 1
        
