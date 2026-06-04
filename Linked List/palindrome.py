# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
        prev = None
        temp = slow
        while temp:
            front = temp.next
            temp.next = prev 
            prev = temp
            temp = front
        temp = head
        while prev:
            if temp.val != prev.val:
                return False
            temp = temp.next
            prev = prev.next
        return True
        
