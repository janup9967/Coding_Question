'''
Given the head of a singly linked list and an integer val, remove all nodes that have value == val.
Return the updated linked list.

✅ Function Signature (LeetCode style)
def removeElements(head, val)

✅ Input
head = [1, 2, 6, 3, 4, 5, 6]
val = 6


✅ Output
1 -> 2 -> 3 -> 4 -> 5 -> None


✅ Example 2
Input:
head = [7,7,7,7]
val = 7

Output:
None


✅ Example 3
Input:
head = [1,2,3]
val = 4

Output:
1 -> 2 -> 3 -> None


✅ Constraints

0 ≤ number of nodes ≤ 10^5
-10^9 ≤ node value ≤ 10^9


🧪 Edge Cases (VERY IMPORTANT)
✅ Multiple deletions at start
✅ Multiple deletions in middle
✅ All nodes deleted
✅ No node matches
✅ Empty list

⚠️ Contest Thinking
👉 Only have:
head

👉 Cannot use:

tail
size


⏱️ Solve it carefully — this problem is tricky because:

Deleting head repeatedly
Maintaining connections correctly
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        # ✅ WRITE YOUR LOGIC HERE
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next

def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example
head = create_list([1, 2, 6, 3, 4, 5, 6])
val = 6

sol = Solution()
new_head = sol.removeElements(head, val)
print_list(new_head)

head = create_list([7,7,7,7])
val = 7
new_head = sol.removeElements(head, val)
print_list(new_head)

# head = create_list([1,2,3])
# val = 4
# new_head = sol.removeElements(head, val)
# print_list(new_head)