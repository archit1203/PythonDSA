class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
    
def printList(head):
    temp=head
    while temp!=None:
        print(temp.key,end=" -> ")
        temp=temp.next
    print("Null")
    

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

printList(head)


