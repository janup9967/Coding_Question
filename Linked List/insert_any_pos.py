"""
 Problem Statement
You are given a singly linked list with n elements.
You need to perform multiple insert operations at any given position (0-based index).
After all operations, print the final linked list.

✅ Input Format
First line: Integer n (number of nodes)
Second line: n space-separated integers

Third line: Integer q (number of insert operations)

Next q lines:
Each line contains 2 integers → index value


✅ Output Format
Print the final linked list:
value -> value -> ... -> None


✅ Rules

If index = 0 → insert at beginning
If index = size → insert at end
If index > size → ignore insertion
Index is 0-based


✅ Example 1
Input:
4
10 20 30 40
3
2 25
0 5
5 50

Explanation:
Initial: 10 -> 20 -> 30 -> 40

Insert 25 at index 2:
10 -> 20 -> 25 -> 30 -> 40

Insert 5 at index 0:
5 -> 10 -> 20 -> 25 -> 30 -> 40

Insert 50 at index 5:
(valid → insert at end)
5 -> 10 -> 20 -> 25 -> 30 -> 50 -> 40


✅ Output:
5 -> 10 -> 20 -> 25 -> 30 -> 50 -> 40 -> None


✅ Example 2
Input:
3
1 2 3
2
1 10
10 99

Output:
1 -> 10 -> 2 -> 3 -> None


✅ Constraints

1 ≤ n ≤ 10^5
1 ≤ q ≤ 10^5
-10^9 ≤ value ≤ 10^9


⏱️ Solve like contest:

Handle edge cases carefully
Make sure links are correct
Avoid breaking the list
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
            for _ in range(pos-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.size += 1


n = int(input())
arr = list(map(int, input().split()))
q = int(input())
l1 = LinkedList()
for val in arr:
    l1.insert_at_end(val)

# print("Initial Linked List\n")
# l1.display()
for _ in range(q):
    pos, value = map(int, input().split())
    # print(f"Inserting {value} at position {pos}")
    l1.insert(value, pos)
    # l1.display()

# print("\nFinal Linked List")
l1.display()
