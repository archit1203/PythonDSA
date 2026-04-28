'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

"""
Brute Force => O(n^2)
n=[1]
key=10
for i in range(len(n)):
    temp=key-n[i]
    for j in range(i+1,len(n)):
        if temp==n[j]:
            print(i,j)
            break
"""

"""
Better => Sorting & Binary Seach nlogn

Optimal => 
"""
def twoSum(self, nums, target):
        d=dict()
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            need=target-nums[i]
            if (need in d.keys()) and d[need]!=i:
                return [i,d[need]]
