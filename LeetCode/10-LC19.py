# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
        count=0
        while fast:
            count+=1
            fast=fast.next
        p=count-n

        if p==0:
            return head.next
        
        i=1
        while slow!=None and i<p:
            slow=slow.next
            i+=1

        slow.next=slow.next.next
        return head       