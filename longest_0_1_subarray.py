
'''
Given an array of 0s and 1s, find the length of the longest contiguous subarray with an equal number of 0s and 1s.
'''


arr = list(map(int,input().split()))

# Brute Force Code
maxLength = 0
for i in range(len(arr)):
    count0 = 0
    count1 = 0
    for j in range(i,len(arr)):
        if arr[j] == 0:
            count0 +=1
        else :
            count1 +=1
            
        if count0 == count1:
            maxLength =max(maxLength,j-i+1)
            
print(maxLength)
        