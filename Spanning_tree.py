'''
Problem Statement
You are given an undirected weighted graph representing cities and connections between them.

Your task is to:

1. Find the Minimum Spanning Tree (MST)
        A spanning tree that connects all vertices with minimum total weight.

2. Find the Second Minimum Spanning Tree
        A spanning tree whose total weight is:
        Strictly greater than MST
        Minimum among all such spanning trees

Input Format:
        The first line contains two integers:
        N → number of cities (vertices)
        M → number of connections (edges)
        Next M lines contain:
        u v w → connection between city u and v with weight w

Output Format
        Print two integers:
        MST weight
        Second MST weight

Constraints
        1 ≤ N ≤ 100
        1 ≤ M ≤ 1000
        Graph is connected
        
Example
    Input
        4 5                         
        1 2 1                      
        1 3 2
        2 3 1
        2 4 3
        3 4 4
        
                                1
                            1-------->2
                            |      /  |
                        2   |  1 /    | 3
                            |  /      |
                            3 ------->4
                                4
    Output
        5 6
        
Explanation
    MST edges:
        (1-2 → 1), (2-3 → 1), (2-4 → 3) → Total = 5

    Second MST:
        Replace one edge → total = 6
'''


