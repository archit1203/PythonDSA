 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Solution 1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersect=None
        if headA is None or headB is None:
            return intersect
        
        if headA==headB:
            return headA

        t1=headA
        t2=headB
        l1=dict()

        while t1:
            l1[t1]=1
            t1=t1.next
        
        #{100:1, 200:1, 300:1, 400:1, 500:1}

        while t2:
            if t2 in l1:
                return t2
            t2=t2.next
        
        return intersect
"""

"""
Solution 2
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersect=None
        if headA is None or headB is None:
            return intersect
        
        if headA==headB:
            return headA

        t1=headA
        t2=headB

        n1,n2=0,0
        while t1:
            n1+=1
            t1=t1.next
        while t2:
            n2+=1
            t2=t2.next

        t1=headA
        t2=headB
        
        diff=n1-n2

        if diff>0:
            for i in range(diff):
                t1=t1.next
        elif diff<0:
            diff=0-diff
            for i in range(diff):
                t2=t2.next
        
        while t1 or t2:
            if t1!=t2:
                t1=t1.next
                t2=t2.next
            else:
                return t1
        
        return intersect

"""