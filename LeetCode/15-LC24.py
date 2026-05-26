# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        curr=head.next.next
        prev=head
        head=head.next
        head.next=prev
        
        while curr and curr.next:
            prev.next=curr.next
            prev=curr
            next=curr.next.next
            curr.next.next=curr
            curr=next
        prev.next=curr
        return head