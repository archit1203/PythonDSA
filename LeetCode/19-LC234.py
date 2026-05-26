# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        temp=head
        stack=[]

        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        
        temp=head

        while temp is not None:
            if temp.val!=stack.pop():
                return False
            temp=temp.next
        
        return True


"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
               
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        
        stx=[]
        temp=head

        c=count//2


        while c:
            stx.append(temp.val)
            temp=temp.next
            c-=1
        
        if count%2!=0:
            temp=temp.next
        
        i=1
        while temp:
            t1=stx[-i]
            if temp.val!=t1:
                return False

            temp=temp.next
            i+=1
        
        return True
"""
        