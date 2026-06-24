"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = ["(", "{", "["]
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if (
                    (i == ")" and x != "(")
                    or (i == "]" and x != "[")
                    or (i == "}" and x != "{")
                ):
                    return False

        return len(stack) == 0


sol = Solution()

print(sol.isValid("()"))  # True
print(sol.isValid("()[]{}"))  # True
print(sol.isValid("(]"))  # False
print(sol.isValid("([])"))  # True
print(sol.isValid("([)]"))  # False


"""
# Alternative Solution using mapping (dictionary) 
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():  # opening brackets
                stack.append(char)
            else:  # closing brackets
                if not stack or stack.pop() != mapping[char]:
                    return False

        return len(stack) == 0
"""
