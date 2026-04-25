class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
    
def printList(head):
    #Traversal: TC = theta(n) ; SC = O(1)
    temp=head
    while temp!=None:
        print(temp.key,end=" -> ")
        temp=temp.next
    print("Null")
    
def insertBegin(head,k):
    #Insert @ Begin: TC = O(1) ; SC = O(1)
    temp=Node(k)
    temp.next=head
    return temp

def insertEnd(head,k):
    #Traversal: TC = theta(n) ; SC = O(1)
    if head==None:
        return Node(k) 
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=Node(k)
    return head
    
def insertAtPosition(head,key,pos):
    pass

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

head=insertBegin(head,5)
head=insertEnd(head,14)
printList(head)


