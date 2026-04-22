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
    temp=Node(k)
    temp.next=head
    return temp


head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

head=insertBegin(head,5)

printList(head)


