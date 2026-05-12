'''

Design a singly linked list with the following features:
✅ Requirements:

Insert nodes at the end of the list
Maintain a variable size that tracks number of nodes
Implement:

insert_end(data)
get_size()
display()




✅ Example:
Input:
Insert: 10, 20, 30

Output:
10 -> 20 -> 30 -> None
Size: 3


🧠 Logic Explanation
✅ Key Idea:
We maintain an extra variable:
self.size = 0
👉 Every time we insert a node:
size += 1


🔍 Step-by-step Flow
Initially:
head = None
size = 0


Insert 10:
head → 10
size = 1


Insert 20:
10 → 20
size = 2


Insert 30:
10 → 20 → 30
size = 3

'''

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert_at_end(self,value):
        node = Node(value)
        if self.size == 0 and not self.head:
            self.head = self.tail = node
            self.size +=1
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size +=1
    
    def get_size(self):
        return self.size

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = "--> ")
            temp = temp.next
        print("None")
    
l1 = LinkedList()
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.insert_at_end(30)
print(l1.get_size())
l1.display()

