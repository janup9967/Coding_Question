''''
Remove Duplicate Characters from a String
Input: "programming"
Output: "progamin"


str1 = input()
seen = set()
result = []
for i in str1:
    if i in seen:
        continue
    else:
        result.append(i)
        seen.add(i)
    
print("".join(result))
'''

'''
Problem:
Find the first character that does not repeat.
Test Cases
A)
Input: "swiss"
Output: 'w'
B)
Input: "aabbcc"
Output: -1 (or null)
C)
Input: "geeksforgeeks"
Output: 'f'

'''

str1 = input()
char_dict = {}
for i in str1:
    char_dict[i] = char_dict.get(i,0) +1
    
for i in str1:
    
    if char_dict[i] ==1:
        print(i)
        break
    
else:
    print(-1)