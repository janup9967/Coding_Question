"""
Given the head of a singly linked list and an integer index, delete the node at that position (0-based index) and return the updated head.

✅ Function Signature
Pythondef deleteAtPosition(head, index):Show more lines

✅ Input
head = [10, 20, 30, 40, 50]
index = 2


✅ Output
10 -> 20 -> 40 -> 50 -> None


✅ Example 2
Input:
head = [1, 2, 3, 4]
index = 0

Output:
2 -> 3 -> 4 -> None


✅ Example 3
Input:
head = [5]
index = 0

Output:
None


✅ Example 4
Input:
head = [10, 20, 30]
index = 5

Output:
10 -> 20 -> 30 -> None

👉 (Invalid index → no change)

✅ Constraints

0 ≤ number of nodes ≤ 10^5
0 ≤ index ≤ 10^5


🧪 Edge Cases (Very Important)
✅ Delete head (index = 0)
✅ Delete last node
✅ Single node
✅ Invalid index
✅ Empty list

⏱️ Solve it like a real interview:

Only head is given ❗
No tail, no size
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

    def insert_at_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.size += 1

    def insert_at_beg(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert(self, value, pos):
        if pos < 0 or pos > self.size:
            return
        elif pos == 0:
            self.insert_at_beg(value)
            return
        elif pos == self.size:
            self.insert_at_end(value)
            return
        else:
            temp = self.head
            node = Node(value)
            for _ in range(pos - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.size += 1

    def delete_at_beg(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1
        
        if self.head is None:
            self.tail = None


    def delete_at_end(self):
        if not self.head:
            return
        elif self.head.next is None:
            self.head =self.tail= None
            self.size -= 1
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.size -= 1

    def delete_at_pos(self, pos):
        if pos < 0 or pos >= self.size:
            return
        elif pos == 0:
            self.delete_at_beg()
            return
        elif pos == self.size-1:
            self.delete_at_end()
            return
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        temp.next = temp.next.next
        self.size -= 1
        # temp.next = None


n = int(input())
arr = list(map(int, input().split()))
l1 = LinkedList()
for val in arr:
    l1.insert_at_end(val)

print("Inital LinkedList")
l1.display()
q = int(input())
for i in range(q):
    print("\nEnter the position to delete")
    pos = int(input())
    print("\nLinkedList After deletion at pos")
    l1.delete_at_pos(pos)
    l1.display()
