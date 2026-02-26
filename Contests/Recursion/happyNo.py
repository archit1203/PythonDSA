#User function Template for python3
def digSq(n):
    sm=0
    while(n):
        rem=n%10
        sm=sm+rem**2
        n//=10
    if sm==1:
        return 1
    elif sm==4:
        return 0
    else:
        return digSq(sm)

class Solution:
    def nextHappy (self, N):
        N+=1
        if digSq(N)==1:
            return N
        else:
            return self.nextHappy(N)
