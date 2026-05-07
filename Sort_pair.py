'''
Problem Statement
You are given N pairs of integers. Each pair contains two values (a, b). Your task is to sort the pairs using Selection Sort based on the following rules:

Sorting Criteria
        Sort pairs in ascending order of the first element.
        If the first elements are equal, then sort based on the second element in ascending order.
        
Input Format
        First line contains an integer N — number of pairs.
        Next N lines each contain two integers a and b.

Output Format
        Print sorted pairs (one per line)

Example
    Input
        5
        10 4
        3 2
        5 2
        3 1
        10 5
        
    Output
        3 1
        3 2
        5 2
        10 4
        10 5
    
Explanation
First sort by first element → (3, 2) and (3, 1) come first.

Since the first elements are equal (3), compare the second → (3, 1) comes before (3, 2).

'''
n = int(input())
pairs =[]
for _ in range(n):
    a,b  = map(int,input().split())
    pairs.append((a,b))

pairs.sort(key= lambda x: (x[0],x[1]))
for i in pairs:
    print(i[0], i[1])