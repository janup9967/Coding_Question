
''' 
Leaders in an array 
Given an array of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.
'''

n = int(input().strip())
arr = list(map(int,input().split()))


leaders = []
leader = arr[-1]
leaders.append(leader)
for i in range(n-2,-1,-1):
    if arr[i] > leader:
        leader = arr[i]
        leaders.append(leader)

print(*leaders[::-1])
        