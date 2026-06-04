"""
roblem Statement: Delete Node at Any Position in DLL
📥 Input

Head of a doubly linked list
Integer pos (0-based index)

📤 Output

Delete the node at position pos
Return updated DLL


✅ Example
Input:
DLL: 1 ⇄ 2 ⇄ 3 ⇄ 4 ⇄ 5
Delete position = 2

Output:
1 ⇄ 2 ⇄ 4 ⇄ 5
"""


class Node:
    def __init__(self, value):
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
            print(temp.data, end=" ->")
            if temp.next is None:
                break
            temp = temp.next
        print("None")
        print("\nBackward:")
        while temp:
            print(temp.data, end=" ->")
            temp = temp.prev
        print("None")

    def insert_at_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.size += 1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp
            self.size += 1

    def insert_at_beg(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert(self, value, pos):
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
            for _ in range(pos - 1):
                temp = temp.next
            node.next = temp.next
            temp.next.prev = node
            node.prev = temp
            temp.next = node
            self.size += 1

    def delete_at_beg(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            prev = temp.prev
            prev.next = None
        self.size -= 1

    def delete(self, pos):
        if pos < 0 or pos >= self.size:
            print("Invalid Position")
            return
        elif pos == 0:
            self.delete_at_beg()
        elif pos == self.size - 1:
            self.delete_at_end()
        else:
            temp = self.head
            for _ in range(pos - 1):
                temp = temp.next
            node = temp.next
            temp.next = temp.next.next
            if node.next:
                node.next.prev = temp

            node.prev = None
            node.next = None
            self.size -= 1


l1 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_end(4)
l1.insert_at_end(5)

l1.display()

print("\nAfter deleting position 2:")
l1.delete(2)

l1.display()



# ✅ Testing all edge cases

l = LinkedList()

print("\n--- Empty list delete ---")
l.delete(0)  # should not crash

print("\n--- Single node delete ---")
l.insert_at_end(10)
l.display()
l.delete(0)
l.display()

print("\n--- Multiple nodes ---")
for i in range(1, 6):
    l.insert_at_end(i)

l.display()

print("\nDelete head:")
l.delete(0)
l.display()

print("\nDelete last:")
l.delete(l.size - 1)
l.display()

print("\nDelete middle:")
l.delete(1)
l.display()

print("\nInvalid position:")
l.delete(10)
