'''

Insert at End + Find Middle Element

Insert nodes at the end (O(1) using tail)
Implement:
find_middle()


Return the middle node value


✅ Example
Input:
Insert: 10, 20, 30, 40, 50

Output:
Middle: 30


🧠 Core Logic (Very Important)
👉 Use Two Pointers (Slow & Fast)
✅ Idea:

slow moves 1 step
fast moves 2 steps


🔍 Visualization
List: 10 -> 20 -> 30 -> 40 -> 50
        ↑
      slow, fast

Step 1:
slow = 20
fast = 30

Step 2:
slow = 30
fast = 50

Step 3:
fast reaches end → STOP

✅ slow is at middle → 30
'''

class Node:
    def __init__(self,value):
        self.data = value
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_end(self,value):
        node = Node(value)
        if not self.head:
            self.head =self.tail =  node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end= "--> ")
            temp = temp.next
        print("None")

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
l1 = LinkedList()
l1.insert_at_end(10)
l1.insert_at_end(20)
l1.insert_at_end(30)
l1.insert_at_end(40)
l1.insert_at_end(50)
l1.display()
middle_node = l1.find_middle()
print("Middle Node:", middle_node.data)