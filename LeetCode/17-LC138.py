 """
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head) :
        if not head:
            return None
        
        temp=head
        while temp:
            t2=Node(temp.val)
            t2.next=temp.next
            temp.next=t2
            temp=t2.next
        

        temp=head
        while temp:
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next

        temp=head
        head2=head.next

        while temp:
            t2=temp.next
            temp.next=t2.next

            if t2.next:
                t2.next=t2.next.next
            
            temp=temp.next

        return head2
        