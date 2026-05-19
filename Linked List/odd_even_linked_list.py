"""
***

# ✅ Problem Statement: Odd Even Linked List

### 📌 Problem

Given the head of a **singly linked list**, group all the nodes with **odd indices** together followed by the nodes with **even indices**, and return the reordered list.

👉 Note:

* The indexing is **1-based**
* You must preserve the **relative order** of both odd and even nodes

***

# 📥 Input

* The head of a singly linked list

***

# 📤 Output

* The linked list rearranged such that:
  ```
  All odd position nodes come first, followed by even position nodes
  ```

***

# 📌 Constraints

* The number of nodes in the list is in the range `[0, 10^4]`
* `-10^6 ≤ Node.val ≤ 10^6`
* The relative order of odd and even indexed nodes must remain the same
* Time Complexity: **O(n)**
* Space Complexity: **O(1)**

***

# ✅ Example 1

```
Input:
head = [1,2,3,4,5]

Output:
[1,3,5,2,4]
```

***

# ✅ Explanation

```
Original:
1 → 2 → 3 → 4 → 5

Odd index nodes:  1 → 3 → 5
Even index nodes: 2 → 4

Result:
1 → 3 → 5 → 2 → 4
```

***

# ✅ Example 2

```
Input:
head = [2,1,3,5,6,4,7]

Output:
[2,3,6,7,1,5,4]
```

***

# ✅ Explanation

```
Odd index nodes:  2 → 3 → 6 → 7
Even index nodes: 1 → 5 → 4

Result:
2 → 3 → 6 → 7 → 1 → 5 → 4
```

***

# ✅ Example 3

```
Input:
head = []

Output:
[]
```

***

# ✅ Function Signature (Python)

```python
def oddEvenList(self, head):
```


```
odd list tail → even list head
```
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        even_node = head.next
        even_head = even_node
        odd_node = head  
        while even_node and even_node.next:
            odd_node.next = odd_node.next.next
            odd_node = odd_node.next
            even_node.next   = even_node.next.next
            even_node = even_node.next
        odd_node.next = even_head
        return head


# ✅ Helper functions for local testing


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

    sol = Solution()
    result = sol.oddEvenList(head)

    print_list(result)
