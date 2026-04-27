#Circular Linked List



class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printList(head):
    #Traversal: TC = theta(n) ; SC = O(1)
    if head==None:
        return
    print(head.key,end=" -> ")
    curr=head.next
    while curr!=head:
        print(curr.key,end=" -> ")
        curr=curr.next
    print("Null")      

def insertBegin(head,k):
    #TC = theta(n)
    temp=Node(k)
    if head==None:
        temp.next=temp
        return temp
    curr=head.next
    while curr.next!=head:
        curr=curr.next  
    curr.next=temp
    temp.next=head
    return temp

def insertBeginOptimal(head,k):
    #TC = O(1)
    temp=Node(k)
    if head==None:
        temp.next=temp
        return temp
    temp.next=head.next
    head.next=temp
    head.key,temp.key=temp.key,head.key
    return head

def insertEnd(head,k):
    #TC = theta(n)
    temp=Node(k)
    if head==None:
        temp.next=temp
        return temp
    curr=head.next
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return head

def insertEndOptimal(head,k):
    #TC = theta(n)
    temp=Node(k)
    if head==None:
        temp.next=temp
        return temp
    temp.next=head.next
    head.next=temp   
    head.key,temp.key=temp.key,head.key
    return temp

def delHead(head):
    if head==None:
        return None
    if head.next==head:
        return None
    head.key=head.next.key
    head.next=head.next.next
    return head


head=Node(10)
t1=Node(20)
t2=Node(30)

head.next=t1
t1.next=t2
t2.next=head

print("CLL: ",end="")
printList(head)

head=insertBegin(head,0)
print("Insert Begin: ",end="")
printList(head)

#head=insertBeginOptimal(head,-10)
#print("Insert Begin 2: ",end="")
#printList(head)

#head=insertEnd(head,100)
#print("Insert End: ",end="")
#printList(head)

head=insertEndOptimal(head,100)
print("Insert End: ",end="")
printList(head)

head=delHead(head)
print("Delete Head: ",end="")
printList(head)