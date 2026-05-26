"""

class Solution:
   def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

#Without Stack

        n1=len(nums1)
        n2=len(nums2)

        ans=[]

        for i in range(n1):
            for j in range(n2):
                if nums1[i]!=nums2[j]:
                    continue
                else:
                    flag=0
                    for k in range(j+1,n2):
                        if nums2[k]>nums2[j]:
                            ans.append(nums2[k])
                            flag=1
                            break
                    if flag!=1:
                        ans.append(-1)
        return ans
"""