'''
Delete First Node (Head)
Given the head of a singly linked list, delete the first node and return the updated list.

✅ Function Signature (LeetCode style)
def deleteHead(head):

✅ Input
head = [10, 20, 30, 40]


✅ Output
20 -> 30 -> 40 -> None


✅ Example 2
Input:
head = [100]

Output:
None


✅ Constraints

0 ≤ number of nodes ≤ 10^5


🧪 Edge Cases

Empty list
Single node list

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
    
    def delete_at_beg(self):
        if not self.head:
            return
        # temp  = self.head
        self.head = self.head.next
        # temp.next =  None
        self.size -=1
        
        if self.head is None:
            self.tail = None



n = int(input())
arr = list(map(int, input().split()))
l1 = LinkedList()
for val in arr:
    l1.insert_at_end(val)
    
print("Inital LinkedList");
l1.display()
print("LinkedList After deletion at beg")
l1.delete_at_beg()
l1.display()

