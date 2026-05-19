'''
Here is your **proper interview-ready problem statement** based on the code and example you shared 👇

***

# ✅ Problem Statement: Reverse Linked List II (Partial Reverse)

### 📌 Problem

Given the head of a **singly linked list** and two integers `left` and `right`, reverse the nodes of the list from position **left to right** (1-based index), and return the modified list.

***

# 📥 Input

* A singly linked list
* Two integers `left` and `right` such that:
  ```
  1 ≤ left ≤ right ≤ length of list
  ```

### Example:

```
head = [1,2,3,4,5], left = 2, right = 4
```

***

# 📤 Output

* The linked list after reversing nodes between positions `left` and `right`

### Output:

```
[1,4,3,2,5]
```

***

# 📌 Explanation

* Original list:
  ```
  1 → 2 → 3 → 4 → 5
  ```
* Sublist from position 2 to 4:
  ```
  2 → 3 → 4
  ```
* After reversing:
  ```
  4 → 3 → 2
  ```
* Final list:
  ```
  1 → 4 → 3 → 2 → 5
  ```

***

# 📌 Constraints

* The number of nodes in the list is in the range `[1, 500]`
* `-500 ≤ Node.val ≤ 500`
* `1 ≤ left ≤ right ≤ n`

***

# ✅ Function Signature (Python)

```python
def reverseBetween(self, head, left, right):
```

***

# ✅ Example Cases

### Example 1

```
Input:  head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

***

### Example 2

```
Input:  head = [5], left = 1, right = 1
Output: [5]
```
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
            
        cur = prev.next
        for _ in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
        



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
head = create_list([1,2,3,4,5])
left = 2
right = 4

# Solution call
sol = Solution()
result = sol.reverseBetween(head, left, right)

# Output
print_list(result)
