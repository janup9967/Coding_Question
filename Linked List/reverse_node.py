"""
Problem Statement: Reverse a Linked List
📌 Problem
Given the head of a singly linked list, reverse the list and return the new head.

📥 Input

A singly linked list:

1 → 2 → 3 → 4 → 5 → NULL


📤 Output

The reversed linked list:

5 → 4 → 3 → 2 → 1 → NULL


📌 Constraints

The number of nodes in the list is in the range [0, 5000]
-5000 <= Node.val <= 5000

✅ Example 1
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]


✅ Example 2
Input:  head = [1,2]
Output: [2,1]


✅ Example 3
Input:  head = []
Output: []
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

    # Reverse a linked list using stack
    # time complexity = O(n) and space complexity = O(n)
    def reverse_node(self):
        if self.head is None:
            return
        stack = []
        temp = self.head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        temp = self.head
        while temp is not None:
            e = stack.pop()
            temp.data = e
            temp = temp.next

    # Reverse a linked list by changing the links between nodes
    # time complexity = O(n) and space complexity = O(1)
    def reverse_links(self):
        if self.head is None:
            return
        prev = None
        temp = self.head
        self.tail = self.head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev


n = int(input())
arr = list(map(int, input().split()))
l1 = LinkedList()
for val in arr:
    l1.insert_at_end(val)
print("Original List: ")
l1.display()
l1.reverse_links()
print("Reversed List: ")
l1.display()
