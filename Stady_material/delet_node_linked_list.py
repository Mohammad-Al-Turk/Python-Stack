class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
       
       
node1=Node("1")
node2=Node("2")
node3=Node("3")
node4=Node("4")
node5=Node("5")


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


head = node1


#delet head node
temp = head.next
head.next = None
head = temp



pointer1 = head
#to select behained last node then delet last node
while pointer1.next.next != None:
    pointer1 = pointer1.next
pointer1.next = None
    
    

pointer = head
while pointer != None:
    print(pointer.data)
    pointer=pointer.next


    