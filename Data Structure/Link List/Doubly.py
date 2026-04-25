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
    if head==None:
        return Node(k)
    temp=Node(k)
    head.prev=temp
    temp.next=head

    return temp


head=Node(10)
t1=Node(20)
t2=Node(30)

head.next=t1
t1.prev=head 
t1.next=t2
t2.prev=t1
printList(head)

head = insertBegin(head,5)
printList(head)
