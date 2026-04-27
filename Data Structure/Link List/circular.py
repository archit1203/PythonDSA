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
    temp=Node(k)
    if head==None:
        return temp
    temp.next=head
    curr=head.next
    while curr.next!=head:
        curr=curr.next  
    curr.next=temp
    return temp


head=Node(10)
t1=Node(20)
t2=Node(30)

head.next=t1
t1.next=t2
t2.next=head

print("CLL: ",end="")
printList(head)

head=insertBegin(head,-1)
print("CLL: ",end="")
printList(head)
