'''
Problem Statement
    A king wants to arrange his army in a line following strict rules.

Given
        N → total number of soldiers in the arrangement
        R → soldiers numbered from 1 to R
        end → the last soldier in the arrangement must be this number

Rules
        The arrangement must start with soldier 1
        The arrangement must end with the soldier end
        No two adjacent soldiers can have the same number
        You can use any soldier number from 1 to R multiple times

Task
        Find the total number of valid arrangements of length N that satisfy all the above conditions.

Input Format
        Three integers:
        N R end

Output Format
        A single integer → number of valid arrangements

Sample Test Cases
    Test Case 1
        Input:
        4 4 3

        Output:
        7
        
    Test Case 2
        Input:
        3 3 2

        Output:
        1
    
Explanation
        Valid sequences:

        1 2 2 (invalid, same adjacent)
        1 3 2
        1 2 3 (wrong end)
        1 2 1 (wrong end)
        So answer = 1
'''

n, r ,end = map(int,input().split())
dp = [0]*(r+1)
dp[1] = 1
for i in range(2,n+1):
    total = sum(dp)
    new = [0]*(r+1)
    for j in range(1,r+1):
        new[j] = total -dp[j]
    dp = new
print(dp[end])
