
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


str1 = input().strip()

# Sliding Window methods
char_set = set()
left = 0
maxLength = 0
for right in range(len(str1)):
    while str1[right] in char_set:
        char_set.remove(s[left])
        left +=1
    char_set.add(str1[right])
    maxlength = max(maxLength, right-left+1)
    
print(maxLength)