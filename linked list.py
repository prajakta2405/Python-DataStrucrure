#concept of linked list
'''head={'value':11,
      'next':{
          'value':12,
          'next':{
              'value':13,
              'next':None,
              }}}
print(head['next']['next']['value'])'''

# initalizing a linkedlist 
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.lenght=1
    # print linkedList

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next
    
    #empty the linkedList

    def empty_list(self):
        if self.head is not None:
            self.head=None
            self.tail=None
        self.lenght=0
    
    # append node in linked list

    
    def append(self,value):
        new_node=Node(value)
        if self.lenght==0:
            self.head= new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.lenght =+1
            
    #pop node from linked list
    def pop(self):
        if self.lenght==0:
            return None
        temp=self.head
        pre= self.head
        while temp.next:
            pre =temp
            temp=temp.next

        self.tail=pre
        self.tail.next=None
        self.lenght -=1
        if self.lenght==0:
            self.head=0
            self.tail=0
        return temp

    def prepend(self,value):
        new_node=Node(value)
        if self.lenght==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next= self.head
            self.head= new_node
        self.lenght +=1
        return True


my_linkedList= LinkedList(3)
my_linkedList.empty_list()
my_linkedList.append(1)
my_linkedList.append(2)
my_linkedList.prepend(3)


#print(my_linkedList.pop())

#print(my_linkedList.pop())

#print(my_linkedList.pop())

my_linkedList.printList()


#print(my_linkedList.lenght)print(my_linkedList.head.value)