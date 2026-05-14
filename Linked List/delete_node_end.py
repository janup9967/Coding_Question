'''
Delete Last Node
📌 Problem Statement
Given the head of a singly linked list, delete the last node of the list and return the updated list.

✅ Function Signature
Pythondef deleteTail(head):Show more lines

✅ Input
head = [10, 20, 30, 40]


✅ Output
10 -> 20 -> 30 -> None


✅ Example 2
Input:
head = [100]

Output:
None


✅ Example 3
Input:
head = [5, 10]

Output:
5 -> None


✅ Constraints

0 ≤ number of nodes ≤ 10^5


🧪 Edge Cases
✅ Empty list → return None
✅ Single node → return None
✅ Two nodes → remove second

⚠️ Important (Contest Thinking)
👉 You ONLY have:
head

👉 You DO NOT have:

tail
size


'''
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
    
    def delete_end(self):
        if self.head is None:
            return 
        temp = self.head
        if temp.next is None:
            self.head =self.tail =  None
            self.size -=1
            return
        pre = None
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.size -=1
        self.tail = pre


n = int(input())
arr = list(map(int, input().split()))
l1 = LinkedList()
for val in arr:
    l1.insert_at_end(val)
    
print("Inital LinkedList");
l1.display()
print("LinkedList After deletion at End")
l1.delete_end()
l1.display()