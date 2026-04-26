#Doubly Linked List
#Each node has refrence to both next and previous node

#Advantages
#Can be traversed in both directions
#Insert/Delete before given node
#Insert/Delete from both end using tail

#Disadvantages
#Extra Space for Prev
#Code becomes complex



class Node:
    def __init__(self,key):
        self.key=key
        self.prev=None
        self.next=None

def printList(head):
    #Traversal: TC = theta(n) ; SC = O(1)
    temp=head
    while temp!=None:
        print(temp.key,end=" <=> ")
        temp=temp.next
    print("Null")

def insertBegin(head,k):
    #TC = O(1)
    temp=Node(k)
    if head==None:
        return temp
    head.prev=temp
    temp.next=head
    return temp

def insertEnd(head,k):
    temp=Node(k)
    if head==None:
        return temp
    curr=head
    while curr.next!=None:
        curr=curr.next
    temp.prev=curr
    curr.next=temp
    return head
    
def reverse(head):
    if head==None:
        return None
    if head.next==None:
        return head
    temp=head
    pre=None
    
    curr=None
    nex=None

    while temp!=None:
        curr=temp
        nex=temp.next
        temp.next=pre
        temp.prev=nex
        pre=temp
        temp=nex
    return pre

'''
def reverse(head):
    if head==None:
        return None
    if head.next==None:
        return head
    temp=head
    pre=None

    curr=None
    nex=None

    while temp.next!=None:
        pre=temp
        temp.next,temp.prev=temp.prev,temp.next
        temp=temp.prev
    return prev
'''

head=Node(10)
t1=Node(20)
t2=Node(30)

head.next=t1
t1.prev=head 
t1.next=t2
t2.prev=t1
print("List 1: ",end='')
printList(head)

head = insertBegin(head,5)
print("Insert Begin: ",end='')
printList(head)

head = insertEnd(head,100)
print("Insert End: ",end='')
printList(head)


head=reverse(head)
print("Reverse List: ",end='')
printList(head)
