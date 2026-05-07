'''
1. Right Half Pyramid Star Pattern
Input: N = 3
Output: 
*
**
***

'''

n = int(input())

print("Right Half Pyramid Star Pattern\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end = "")
    print()
    

'''
2. Inverted Right Half Pyramid Star Pattern
Input: N = 3
Output:
***
**
*
'''


print("\nInverted Right Half Pyramid Pattern\n")

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*", end = "")
    print()
    
    
'''
Another ways 
output = []
for i in range(n,0,-1):
    output.append("*"*i)
    # print("*"*i)

print("\n".join(output))

'''

'''
3. Left Half Pyramid Star Pattern
Input: N = 3
Output:
  *
 **
 ***

'''

print("\nLeft Half Pyramid Star Pattern\n")

for i in range(1,n+1):
    for _ in range(n-i+1):
        print(" ", end = "")
    
    for j in range(1,i+1):
        print("*",end = "")
    print()
    
'''
4. Inverted Left Half Pyramid Star Pattern
Input: N = 3
Output:
***
 **
  *

'''
print("\nInverted Left Half Pyramid Star Pattern\n")

for i in range(n,0,-1):
    for _ in range(n-i+1):
        print(" ", end = "")
    for j in range(1,i+1):
        print("*", end = "")
    print()
    
    
'''
5. Full Pyramid Star Pattern
Input: N = 3
Output:
  *
 ***
*****

'''

print("\nFull Pyramid Star Pattern\n")
for i in range(1,n+1):
    for _ in range(n-i+1):
        print(" ", end = "")
    for j in range(1, 2*i):
        print("*", end = "")
    print()
    
'''
6. Inverted Full Pyramid Star Pattern
Input: N = 3
Output:
*****
 ***
  *

'''
print("\nInverted Full Pyramid Star Pattern\n")

for i in range(n,0,-1):
    for _ in range(n-i+1):
        print(" ", end = "")
    for j in range(1,2*i):
        print("*", end = "")
    print()
    
'''
7. Half Diamond Star Pattern
Input: N = 3
Output:
*
**
***
**
*

'''
print("\n Half Diamond Star Pattern\n")

for i in range(1,2*n+1):
    if i <=n:
        for j in range(1,i+1):
            print("*", end = "")
    else:
        for j in range(2*n-i+1,0,-1):
            print("*", end = "")
    print()
    
'''
8. Diamond Star Pattern
Input: N = 3
Output:
  *
 ***
*****
 ***
  *
'''

print("\nDiamond Star Pattern\n")

# for i in range(1,2*n+1):
    