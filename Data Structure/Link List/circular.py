#Circular Linked List



class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printList(head):
    #Traversal: TC = theta(n) ; SC = O(1)
    temp=head
    while temp!=None:
        print(temp.key,end=" -> ")
        temp=temp.next
    print("Null")        



head=Node(10)
t1=Node(20)
t2=Node(30)

head.next=t1
t1.next=t2
t2.next=head

print("CLL: ",end="")
printList(head)