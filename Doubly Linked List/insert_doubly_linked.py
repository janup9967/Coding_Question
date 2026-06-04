'''
Problem Statement: Insert at Any Position in DLL
📌 Problem
Given a doubly linked list, insert a new node with a given value at a specific position pos.

📥 Input

Head of DLL
Integer data
Integer pos (0-based index)


📤 Output

Updated doubly linked list after insertion


✅ Example
Input:
DLL: 1 ⇄ 2 ⇄ 4 ⇄ 5  
Insert: 3 at position 2

Output:
1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5


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
        
    def insert_at_end(self,value):
        node = Node(value)
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
    
    def insert_at_beg(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size +=1
    
    def insert(self,value,pos):
        if pos < 0 or pos > self.size:
            print("Invalid Postion") 
            return 
        if pos == 0:
            self.insert_at_beg(value)
        elif pos == self.size:
            self.insert_at_end(value)
        else:
            temp = self.head
            node = Node(value)
            for _ in range(pos-1):
                temp = temp.next
            node.next = temp.next
            temp.next.prev = node
            node.prev = temp
            temp.next = node
            self.size +=1
         

l1 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(4)
l1.insert_at_end(5)
l1.display()
print("After insertion after 2 pos of value 3")
l1.insert(3,2)
l1.display()
        
# ✅ Edge Case Testing

print("\n--- Empty List Insert ---")
l = LinkedList()
l.insert(10, 0)
l.display()

print("\n--- Insert at Beginning ---")
l = LinkedList()
l.insert(1, 0)
l.insert(2, 0)
l.insert(3, 0)
l.display()

print("\n--- Insert at End ---")
l = LinkedList()
l.insert(1, 0)
l.insert(2, 1)
l.insert(3, 2)
l.display()

print("\n--- Insert in Middle ---")
l = LinkedList()
l.insert_at_end(1)
l.insert_at_end(2)
l.insert_at_end(4)
l.insert_at_end(5)
l.insert(3, 2)
l.display()

print("\n--- Invalid Position (-1) ---")
l.insert(100, -1)

print("\n--- Invalid Position (Out of Range) ---")
l.insert(100, 10)