"""
Problem Statement: Reverse a Doubly Linked List

🧩 Problem
Given the head of a doubly linked list, reverse the list and return the new head.
In a doubly linked list, each node contains:

data
pointer to next node (next)
pointer to previous node (prev)

After reversing:

The next and prev pointers of all nodes should be swapped.
The head should point to the last node of the original list.


📥 Input

head → pointer to the first node of a doubly linked list


📤 Output

Return the new head of the reversed doubly linked list


✅ Example 1
Input:
DLL: 1 ⇄ 2 ⇄ 3 ⇄ 4

Output:
DLL: 4 ⇄ 3 ⇄ 2 ⇄ 1


✅ Example 2
Input:
DLL: 10 ⇄ 20 ⇄ 30

Output:
DLL: 30 ⇄ 20 ⇄ 10


✅ Example 3 (Single Node)
Input:
DLL: 5

Output:
DLL: 5

👉 No change because only one node exists

✅ Example 4 (Empty List)
Input:
DLL: None

Output:
None


🧠 Constraints

Number of nodes: 0 <= n <= 10^4
Values can be any integer

 Complexity

Time: O(n)
Space: O(1)

"""


# Node structure for DLL
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Display forward and backward
    def display(self):
        temp = self.head
        print("\nForward:")

        # Forward traversal
        while temp:
            print(temp.data, end=" <-> ")
            if temp.next is None:
                break
            temp = temp.next
        print("None")

        print("Backward:")
        # Backward traversal
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    # ✅ Reverse DLL
    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            # Swap next and prev
            curr.prev, curr.next = curr.next, curr.prev

            # Move forward (which is prev now)
            prev = curr
            curr = curr.prev

        # Update head
        if prev:
            self.head = prev


# ✅ Example Usage
dll = DoublyLinkedList()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)

print("Original DLL:")
dll.display()

dll.reverse()

print("\nReversed DLL:")
dll.display()

"""
# Case 1: Empty
dll = DoublyLinkedList()
dll.reverse()
dll.display()

# Case 2: Single node
dll = DoublyLinkedList()
dll.insert(10)
dll.reverse()
dll.display()

# Case 3: Two nodes
dll = DoublyLinkedList()
dll.insert(1)
dll.insert(2)
dll.reverse()
dll.display()
"""
