'''
Problem Statement
Create a singly linked list and implement the following operations:

Insert elements at the end of the list
Display all elements


✅ Input
    Insert elements: 5, 10, 15
✅ Output
    5 -> 10 -> 15 -> None


Your Task

    Create Node class
    Create LinkedList class
    Implement insert(data)
    Implement display()

'''

'''
Problem Statement
Create a singly linked list and implement the following operations:

Insert elements at the end of the list
Display all elements


✅ Input
    Insert elements: 5, 10, 15
✅ Output
    5 -> 10 -> 15 -> None


Your Task

    Create Node class
    Create LinkedList class
    Implement insert(data)
    Implement display()

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = "--> ")
            temp = temp.next
        print("None")
    
    def insert(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return 
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
        
l1 = LinkedList()
l1.insert(1)
l1.insert(3)
l1.insert(2)
l1.insert(4)
l1.insert(5)
l1.display()
        

        
        