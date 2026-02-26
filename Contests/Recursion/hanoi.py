class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n==1:
            return 1
        #move n-1 disk from source to aux
        mov=self.towerOfHanoi(n-1,fromm,aux,to)
        #move largest disk from src to destn
        mov+=1
        #move n-1 disks from aux to destn
        mov+=self.towerOfHanoi(n-1,aux,to,fromm)
        return mov
