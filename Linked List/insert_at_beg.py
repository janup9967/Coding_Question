'''
 Problem: Insert at Beginning of Linked List
You are given a sequence of integers. Create a singly linked list by inserting each element at the beginning of the list.
After all insert operations, print the final linked list.

✅ Input Format

First line: integer n (number of elements)
Second line: n space-separated integers


✅ Output Format
Print the linked list elements

✅ Example 1
Input:
5
10 20 30 40 50

Output:
50 -> 40 -> 30 -> 20 -> 10 -> None


✅ Example 2
Input:
3
1 2 3

Output:
3 -> 2 -> 1 -> None


✅ Constraints

1 ≤ n ≤ 10^5
Values can be any integer

'''
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end = "--> ")
            temp = temp.next
        print(None)
        
    def insert_at_beg(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        
l1 = LinkedList()
n = int(input())
arr = list(map(int,input().split()))
for val in arr:
    l1.insert_at_beg(val)

l1.display()
        
