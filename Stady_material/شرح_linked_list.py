#شرح بطريقه ثانية مشان فحم طريقة كتابة الكود
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
   


head=Node("5")   
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")

# end_new_node=Node("6")
# mid_new_node=Node("7")




head.next=node1
node1.next = node2
node2.next = node3
node3.next = node4




#head = starter_new_node
# pointer = head



# while pointer != None:
#     print(pointer.data)
#     pointer=pointer.next

# pointer.next = end_new_node

pointer = head
postion = 3
# للوصول الى نود معينة

while ( postion-1 > 0):
    pointer = pointer.next
    postion -= 1
    
#for k in range(0,postion ,1):
#    #print(pointer.data)
#    pointer = pointer.next


mid_new_node=Node("7")
print("This is the third node",pointer.data)
temp = pointer.next
pointer.next = mid_new_node
mid_new_node.next = temp





# node1.next = node4
# node2.next = node3
# node3.next = node1
# node4.next = node2


# print(node3.data)
# print(node1.next.data)
# print(node1.next.next.next.data)



# pointer = head
# طباعة محتويات اللينك لست وعدد محتوياتها
# count = 0
# while pointer != None:
#     print(pointer.data)
#     pointer=pointer.next
#     count=count+1
# print("numberd of element: ",count)






#pointer = head
# count = 0
# while pointer != None:
#     print(pointer.data)
#     pointer=pointer.next
#     count=count+1
# zzprint("numberd of element: ",count)


#غلط استخدم الي معلمه ب * لانه مش معروف وين انا وباي نود
# *node2.next = mid_new_node
# *mid_new_node.next = node 
# pointer.next = mid_new_node

# mid_new_node.next = pointer.next.next



new_pointer = head
# pointer = head
# طباعة محتويات اللينك لست وعدد محتوياتها
count = 0
while new_pointer != None:
    print(new_pointer.data)
    new_pointer=new_pointer.next
    count=count+1
print("numberd of element: ",count)