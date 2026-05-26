# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head==None:
            return None
        if head.next==None:
            return head
        temp=head
        curr=None
        nex=None
        prev=None
        while temp!=None:
            curr=temp
            nex=curr.next
            curr.next=prev

            prev=curr
            temp=nex
        return prev