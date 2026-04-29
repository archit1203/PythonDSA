#Flloyd's Cycle Detection Algo

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Space = O(1)
#Time = O(n)

class Solution:
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
            
        return False

        
        