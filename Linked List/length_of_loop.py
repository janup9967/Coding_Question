"""
Here is the **LeetCode-style problem statement** for *Find Length of Loop in Linked List* 👇

***

# ✅ Problem Statement: Find Length of Loop in Linked List

### 📌 Problem

Given the head of a **singly linked list**, determine if the linked list contains a cycle (loop).
If a cycle exists, return the **length of the loop**. Otherwise, return `0`.

***

# 📥 Input

* The head of a singly linked list.
* The linked list may or may not contain a cycle.

***

# 📤 Output

* Return an integer representing the **length of the cycle**.
* If no cycle exists, return `0`.

***

# 📌 Constraints

* The number of nodes in the list is in the range `[0, 10^4]`
* `-10^5 ≤ Node.val ≤ 10^5`
* The cycle can be at any position in the list

***

# ✅ Example 1

```
Input:
head = [1,2,3,4,5]
pos = 1   (tail connects to node at index 1)

Output:
4
```

### Explanation:

```
Cycle: 2 → 3 → 4 → 5 → back to 2
Length of loop = 4
```

***

# ✅ Example 2

```
Input:
head = [1,2]
pos = 0

Output:
2
```

### Explanation:

```
Cycle: 1 → 2 → back to 1
Length = 2
```

***

# ✅ Example 3

```
Input:
head = [1]
pos = -1

Output:
0
```

### Explanation:

```
No cycle present
```


# ✅ Function Signature (Python)

```python
def findLoopLength(self, head):
```
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findLoopLength(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        '''
        # brute force approach
        # time complexity is O(n) and space complexity is O(n)
        if not head or not head.next:
            return 0
        my_dict = {}
        travel = 0
        temp = head
        while temp:
            if temp in my_dict:
                return travel - my_dict[temp]
            else:
                my_dict[temp] = travel
            travel += 1
            temp = temp.next

        return 0
        '''
        # optimal approach
        # time complexity is O(n) and space complexity is O(1)
        if not head or not head.next:
            return 0
        # Floyd's Cycle Detection Algorithm
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                break
        else:
            return 0
        count = 1
        slow = slow.next
        while slow != fast:
            count +=1
            slow = slow.next
        return count
    


# Helper function to create linked list
def create_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# Helper to print list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Input
head = create_list([1, 2, 3, 4, 5])

# Create cycle at position 1
tail = head
cycle_node = None
index = 0
pos = 1

while tail.next:
    if index == pos:
        cycle_node = tail
    tail = tail.next
    index += 1

tail.next = cycle_node  # create loop

# Solution call
sol = Solution()
result = sol.findLoopLength(head)

# Output
print(result)
