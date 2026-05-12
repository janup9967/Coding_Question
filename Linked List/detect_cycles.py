'''
Detect Cycle in Linked List
Given the head of a singly linked list, determine whether the linked list contains a cycle.

✅ Input Format

First line: integer n (number of nodes)
Second line: n space-separated values
Third line: integer pos (index where tail connects, -1 if no cycle)


✅ Output
Print:
True
or
False


✅ Example 1
Input:
5
1 2 3 4 5
2

Output:
True


✅ Example 2
Input:
4
10 20 30 40
-1

Output:
False


✅ Constraints

1 ≤ n ≤ 10^5
-1 ≤ pos < n

'''
class Node:
    def __init__(self,value):
        self.data = value
        self.next =None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_end(self,value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    def connect_tails(self,pos):
        if pos <0:
            return 
        temp = self.head
        for _ in range(pos):
            temp =temp.next
        self.tail.next = temp
        
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
            if temp== self.tail.next:
                break
        # print(None)
        
    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if slow == fast:
                return True
        else:
            return  False
        
    
l1 = LinkedList()
n = int(input())
values = list(map(int,input().split()))
for i in values:
    l1.insert_at_end(i)
   
pos = int(input()) 
l1.connect_tails(pos)
print(l1.detect_cycle())
l1.display()

