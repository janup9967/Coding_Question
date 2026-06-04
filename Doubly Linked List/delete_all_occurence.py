"""
Problem: Delete All Occurrences in a Doubly Linked List
🧩 Description
Given the head of a doubly linked list and a value x, delete all nodes in the list that have value equal to x.
After deletion, return the updated head of the list.

📥 Input

head → head of the doubly linked list
Integer x


📤 Output

Updated doubly linked list after removing all occurrences of x


✅ Example 1
Input:
DLL: 1 ⇄ 2 ⇄ 3 ⇄ 2 ⇄ 4
x = 2

Output:
1 ⇄ 3 ⇄ 4


✅ Example 2
Input:
DLL: 2 ⇄ 2 ⇄ 2
x = 2

Output:
None


✅ Example 3
Input:
DLL: 1 ⇄ 2 ⇄ 3
x = 5

Output:
1 ⇄ 2 ⇄ 3


🚀 Complexity

Time: O(n)
Space: O(1)


"""


# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List helper class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Display list
    def display(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        print("Forward:")
        while temp:
            print(temp.data, end=" <-> ")
            if temp.next is None:
                break
            temp = temp.next
        print("None")

        print("Backward:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# ✅ Solution class
class Solution:

    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        if not head.next and head.data == x:
            return None
        temp = head
        prev = None
        new_head = head
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                if temp.next:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
            prev = temp
            temp = temp.next
        return new_head


# ✅ ✅ Test Cases
dll = DoublyLinkedList()

# Example: 1 ⇄ 2 ⇄ 3 ⇄ 2 ⇄ 4
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(2)
dll.insert(4)

print("Original DLL:")
dll.display()

sol = Solution()

# Delete all occurrences of 2
dll.head = sol.deleteAllOccurOfX(dll.head, 2)

print("\nAfter deleting all occurrences of 2:")
dll.display()
