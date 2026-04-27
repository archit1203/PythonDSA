class Node:
    def __init__(self,key):
        self.key=key
        self.prev=None
        self.next=None

def printList(head):
    #Traversal: TC = theta(n) ; SC = O(1)
    temp=head
    while temp!=None:
        print(temp.key,end=" -> ")
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


def deleteKth(head,k):
    if k<=0:
        print("Invalid")
        return head
    if head==None:
        return None
    if head.next==None:
        return None
    if k==1:
        return head.next
    curr=head
    for i in range(k-2):
        if curr.next.next!=None:
            curr=curr.next
        else:
            print("Out of Range")
            return(head)
    curr.next=curr.next.next
    return head


head=Node(0)
for i in range(1,5):
    head = insertEnd(head,i*10)

print("List: ",end='')
printList(head)

head=deleteKth(head,20)
print("Kth Node: ",end='')
printList(head)