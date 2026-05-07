'''
Problem Statement
    You are given:
        An array of integers of size n
        An integer maxSum (maximum allowed sum)
        
    Find the maximum possible sum of elements from the array such that the sum is less than or equal to maxSum.
    You can choose any subset of elements.

Task
    Return the maximum sum ≤ maxSum.

Input
    Integer n (size of array)
    Array arr[n]
    Integer maxSum
    
Output Format
    Maximum possible sum ≤ maxSum
    
Test Cases
    Test Case 1
        Input:
        n = 4
        arr = [2, 3, 5, 7]
        maxSum = 10

        Output:
        10
        
    Explanation: subset {3, 7} gives sum 10.

    Test Case 2
        Input:
        n = 3
        arr = [4, 8, 6]
        maxSum = 9

        Output:
        8
        
    Explanation: best subset is {8}.
'''
'''
def solve(arr,index,cur,mx):
    if cur> mx:
        return 0
    if index == len(arr):
        return cur
    inc = solve(arr,index+1,cur+arr[index],mx)
    
    exc = solve(arr,index+1,cur,mx)
    
    return max(inc, exc )
'''

def solve(arr,index,cur,mx,dp):
    if cur> mx:
        return 0
    if index == len(arr):
        return cur
    key = (index,cur)
    if key in dp:
        return dp[key]
    inc = solve(arr,index+1,cur+arr[index],mx,dp)
    
    exc = solve(arr,index+1,cur,mx,dp)
    dp[key] = max(inc, exc)
    return dp[key]

n = int(input())
arr = list(map(int,input().split()))
maxSum = int(input())
dp = {}
print(solve(arr,0,0,maxSum,dp))