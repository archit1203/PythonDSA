# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k) :
        if head is None or head.next is None or k==0:
            return head

        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next

        k=k%count
        if k==0:
            return head

        temp=head
        for i in range(count-k-1):
            temp=temp.next
        
        temp2=temp.next
        temp.next=None

        temp3=temp2

        while temp3.next:
            temp3=temp3.next
        
        temp3.next=head

        return temp2

