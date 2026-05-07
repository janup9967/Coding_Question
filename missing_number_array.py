
'''
Missing Number in Array 
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.   
Example 1:
Input:
N = 3
A[] = [3,0,1]
Output: 2
'''

n = int(input().strip())
arr = list(map(int,input().split()))

expected_total = n*(n+1)/2
actual_total = sum(arr)

missing_number = expected_total - actual_total
print(int(missing_number))
