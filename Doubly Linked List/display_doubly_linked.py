'''
Problem Statement: Display Doubly Linked List
📌 Problem
Given the head of a doubly linked list, display all elements of the list in:

Forward direction (from head to tail)
Backward direction (from tail to head)

📥 Input

Head of a doubly linked list

Each node contains:
prev ← data → next

📤 Output

Print elements:

Forward traversal
Backward traversal

📌 Constraints

Number of nodes: [0, 10^4]
-10^5 ≤ Node.data ≤ 10^5

✅ Example
Input:
DLL:
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5


Output:
Forward:
1 → 2 → 3 → 4 → 5

Backward:
5 → 4 → 3 → 2 → 1
'''

class Node:
    def __init__(self,value):
        self.data = value
        self.prev = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def display(self):
        temp = self.head
        print("\nForward:")
        while temp:
            print(temp.data,end = " ->")
            if temp.next is None:
                break
            temp = temp.next
        print("None")
        print("\nBackward:")
        while temp:
            print(temp.data,end = " ->")
            temp = temp.prev
        print("None")
    
    def insert_at_end(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.size +=1
        else: 
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp
            self.size +=1
        
l1 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_end(4)
l1.display()
        
