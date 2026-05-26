"""
NAIVE

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stx=[]
        n=len(heights)
        
        for i in range(n):
            #left
            count=1
            for j in range(i-1,-1,-1):
                if heights[j]>=heights[i]:
                    count+=1
                else:
                    break
            
            #right
            c2=1
            temp=0

            for j in range(i+1,n):
                if heights[j]>=heights[i]:
                    count+=1
                else:
                    break
            
            stx.append(heights[i]*count)
        return max(stx)
"""