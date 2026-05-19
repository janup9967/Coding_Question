'''
Here is a **complete LeetCode-style problem statement + template code** for **Remove Nth Node From End of List** 👇

***

# ✅ Problem Statement: Remove Nth Node From End of List

### 📌 Problem

Given the head of a **singly linked list**, remove the **nth node from the end of the list** and return its head.

***

# 📥 Input

* The head of a singly linked list
* An integer `n`

***

# 📤 Output

* Return the head of the modified linked list after removing the nth node from the end

***

# 📌 Constraints

* The number of nodes in the list is `sz`
* `1 ≤ sz ≤ 10^4`
* `0 ≤ Node.val ≤ 100`
* `1 ≤ n ≤ sz`

***

# ✅ Example 1

```
Input:
head = [1,2,3,4,5], n = 2

Output:
[1,2,3,5]
```

***

# ✅ Explanation

```
Original:
1 → 2 → 3 → 4 → 5

Remove 2nd node from end → removes 4

Result:
1 → 2 → 3 → 5
```

***

# ✅ Example 2

```
Input:
head = [1], n = 1

Output:
[]
```

***

# ✅ Example 3

```
Input:
head = [1,2], n = 1

Output:
[1]
```

***

# ✅ Follow-Up

👉 Can you solve it in **one pass**?

***

# ✅ Function Signature (Python)

```python
def removeNthFromEnd(self, head, n):
```

***
'''

# ✅ ✅ VS Code Template (No Implementation)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        # Brute Force approach
        if not head:
            return None
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length +=1
        if length == n:
            return head.next
        temp = head
        for _ in range(length-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
        '''
        
        # Optimized Code
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next =slow.next.next
        return head
            


# ✅ Helper functions for testing

def create_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


# ✅ Test Input
if __name__ == "__main__":
    head = create_list([1, 2, 3, 4, 5])
    n = 2

    sol = Solution()
    result = sol.removeNthFromEnd(head, n)

    print_list(result)
