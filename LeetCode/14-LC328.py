   # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd=head
        even=head.next

        curr=odd
        temp=even

        while temp and temp.next:
            curr.next=temp.next
            curr=curr.next
            
            temp.next=curr.next
            temp=temp.next
            
        curr.next=even

        return head


