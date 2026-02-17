class Solution:
    def primeFac(self, n):
        li=[]
        if n%2==0:
            li.append(2)
            while n%2==0:
                n//=2
                
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i==0:
                li.append(i)
                while(n%i==0):
                    n//=i
        if n>2:
            li.append(n)
            
        return li
