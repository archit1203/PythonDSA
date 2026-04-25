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
    #Del @ Head: TC: O(1)
    if head==None:
        return None
    else:
        return head.next

def delLast(head):
    if head==None:
        return None
    if head.next==None:
        return None
    temp=head
    while temp.next.next!=None: #2nd Last Node
        temp=temp.next
    temp.next=None
    return head

def search(head,k):
    #TC = O(n) SC = O(1)
    temp=head
    pos=1
    while temp!=None:
        if temp.key==k:
            return pos
        pos=pos+1
        temp=temp.next
    return -1
    



head=Node(0)
head.next=Node(10)
head.next.next=Node(20)

head=insertBegin(head,30)
head=insertEnd(head,40)
head=insertAtPosition(head,'Mid',4)
printList(head)

head=delFirst(head)
printList(head)

head=delLast(head)
printList(head)

pos=search(head,30)
print(pos)
pos=search(None,20)
print(pos)

