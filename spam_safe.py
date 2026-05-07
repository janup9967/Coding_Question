'''
A Chat platform want to detect spam, if message contains three consecutive identical characters, 
it it considered spam
Given a message string determine whether it is spam or safe 

Example 1:
Input: message = "hellooo"
Output: spam

Example 2:
Input: message = "hey"
Output: safe
'''


str1 = input().strip()
count = 1
for i in range(1,len(str1)):
    if str1[i] == str1[i-1]:
        count +=1
        if count >=3:
            print("spam")
            break
    else:
        count =1 
else:
    print("Safe")
    
        