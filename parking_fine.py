'''
Problem Statement
A parking system calculates fines based on the number of hours a vehicle is parked.

Given an integer hours representing parking duration:

    If parking time ≤ 2 hours, fine = 100
    If parking time > 2 and ≤ 5 hours, fine = 50
    If parking time > 5 hours, fine = 20
    
Task
    Write a program to calculate and print the parking fine.

Input
    An integer hours

Output
    An integer representing the fine
    
Test Cases
    Input: 2
    Output: 100

    Input: 4
    Output: 50

    Input: 6
    Output: 20
    
'''
n = int(input())
if n<=2:
    print(100)
elif n <=5:
    print(50)
else:
    print(20)
    
