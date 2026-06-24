"""
Problem Statement: Implement Stack Using List in Python
A stack is a linear data structure that follows the LIFO (Last In First Out) principle. You need to implement a stack using Python’s built-in list and support the following operations:
Operations to implement:

push(x) - Add an element x to the top of the stack
pop() - Remove and return the top element of the stack
peek() - Return the top element without removing it
is_empty() - Check if the stack is empty
size() - Return the number of elements in the stack


📥 Sample Input / Output
Example 1:
Input Operations:
push(10)
push(20)
push(30)
peek()
pop()
peek()
size()
is_empty()

Output:
Top element is: 30
Popped element: 30
Top element is: 20
Stack size: 2
Is stack empty: False


Example 2:
Input Operations:
pop()
is_empty()
push(5)
peek()

Output:
Stack is empty
Is stack empty: True
Top element is: 5

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            print("You cannot see the top of stack because Stack is Empty")
            return -1
        else:
            return self.items[-1]

    def pop(self):
        if self.is_empty():
            print("You cannot pop the item in stack because Stack is Empty")
            return None
        else:
            x = self.items.pop()
            return x


s = Stack()

while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Is Empty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to push: "))
        s.push(val)
        print(f"{val} pushed into stack")

    elif choice == 2:
        result = s.pop()
        if result is not None:
            print("Popped element:", result)

    elif choice == 3:
        result = s.peek()
        if result is not None:
            print("Top element:", result)

    elif choice == 4:
        print("Stack size:", s.size())

    elif choice == 5:
        print("Is stack empty:", s.is_empty())

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")


"""
# Quick Manual Test (Without Input)
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top element is:", s.peek())
print("Popped element:", s.pop())
print("Top element is:", s.peek())
print("Stack size:", s.size())
print("Is stack empty:", s.is_empty())

"""
