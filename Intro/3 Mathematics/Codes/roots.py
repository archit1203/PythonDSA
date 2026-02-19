import math
class Solution:
	def quadraticRoots(self, a : int, b : int , c:int ) -> list[int]:
        D=math.pow(b,2) - 4*a*c
        if D<0:
            return [-1]
        D=math.sqrt(D)
        a1=(-b)+D
        a1=math.floor(a1/(2*a))
        
        a2=(-b)-D
        a2=math.floor(a2/(2*a))
        
        li=[]
        if a1>a2:
            li.append(a1)
            li.append(a2)
        else:
            li.append(a2)
            li.append(a1)
        
        return li
