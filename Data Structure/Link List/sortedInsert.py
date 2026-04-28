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

def sortInsert(head,k):
    temp=Node(k)
    if head==None:
        return temp
    elif k<head.key:
        temp.next=head
        return head
    else:
        curr=head
        while curr.next!=None and curr.next.key<k:
            curr=curr.next
        temp.next=curr.next
        curr.next=temp
        return head

head=Node(0)
for i in range(1,5):
    head = insertEnd(head,i*10)

print("List: ",end='')
printList(head)

head=sortInsert(head,25)
print("Sort: ",end='')
printList(head)