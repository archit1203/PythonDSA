# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        if list1==None:
            if list2==None:
                return None
            else:
                return list2
        elif list2==None:
                return list1

        l1=list1
        l2=list2
        l3=head
        
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                l3.next=l1
                l1=l1.next
            else:
                l3.next=l2
                l2=l2.next
            l3=l3.next
        
        if l1 is not None:
            l3.next=l1
        if l2 is not None:
            l3.next=l2
        
        return head.next