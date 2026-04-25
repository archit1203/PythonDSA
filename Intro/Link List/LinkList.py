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
    #Insert $ End: TC = theta(n) ; SC = O(1)
    if head==None:
        return Node(k) 
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=Node(k)
    return head
    
def insertAtPosition(head,k,pos):
    #Insert @ Position: TC= theta(min(pos,n))
    temp=Node(k)
    if pos==1:
        temp.next=head
        return temp
    curr=head
    for i in range(pos-2):
        curr=curr.next
        if curr==None:
            return head
    temp.next=curr.next
    curr.next=temp
    return head


def delFirst(head):
    head=head.next
    return head



head=Node(0)
head.next=Node(1)
head.next.next=Node(2)

head=insertBegin(head,3)
head=insertEnd(head,4)
head=insertAtPosition(head,'Mid',4)
printList(head)

head=delFirst(head)
printList(head)


