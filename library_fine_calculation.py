'''
A Library keeps track of books borrowed by students. each elements in the arrays represents the no of days 
students kept a book
if book is kept more than k days, the student must pay 1 unit fine for each extra day
Calculate the total fine collected by the library
Input Format
First Line : N Int (number of students)
Second Line : N space separated Int (number of days students kept the book)
Third Line : K Int (number of days allowed to keep the book)

Output Format
Total fine collected by the library

Sample Input
5
12 3 5 7 9
5

Sample Output
13

Explanation
Student 1 kept book for 12 days, fine = 12 - 5 = 7
Student 2 kept book for 3 days, fine = 0 (as 3 < 5)
Student 3 kept book for 5 days, fine = 0 (as 5 == 5)
Student 4 kept book for 7 days, fine = 7 - 5 = 2
Student 5 kept book for 9 days, fine = 9 - 5 = 4
Total Fine = 7 + 0 + 0 + 2 + 4 = 13

Sample Input 2
4
15 20 10 5
10

Sample Output 2
15

Explanation
Student 1 kept book for 15 days, fine = 15 - 10 = 5
Student 2 kept book for 20 days, fine = 20 - 10 = 10
Student 3 kept book for 10 days, fine = 0 (as 10 == 10)
Student 4 kept book for 5 days, fine = 0 (as 5 < 10)
Total Fine = 5 + 10 + 0 + 0 = 15

Approach
Traverse the array and check if element > k, then fine = element - k
else fine = 0
return sum of all fines
'''


n = int(input())
arr = list(map(int,input().split()))
k = int(input())

fine = 0
for i in arr:
    if i >k:
        fine += i-k
    
print(fine)

