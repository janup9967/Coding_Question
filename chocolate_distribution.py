'''
N Packet of chocolate, each containing some chocolate 
We can select any M packets from N packets and distribute among M students.
Find the minimum difference between max and min chocolate recieved by students 

find the minimum possibe difference

Input Format
First Line : N Int
Second Line : N space separated Int (number of chocolate in each packet)
Third Line : M Int (Number of students)

Output Format
Minimum difference between max and min chocolate recieved by students

Sample Input
7
7 3 2 4 9 12 56
3

Sample Output
2

Explanation
We can select 3 packets with 3, 4 and 2 chocolates.
The difference between maximum and minimum is 4 - 2 = 2 which is minimum possible difference.

Sample Input 2
10
12 4 7 9 2 23 25 41 30 40
4

Sample Output 2
5

Explanation
We can select 4 packets with 7, 9, 12 and 4 chocolates.
The difference between maximum and minimum is 12 - 7 = 5 which is minimum possible difference.

Approach
Sort the array
select m consecutive element and find difference between first and last element

'''


n = int(input())
arr = list(map(int,input().split()))
m = int(input())

arr.sort()
min_packet =  float('inf')

for i in range(n-m+1):
    diff = arr[i+m-1]-arr[i]
    min_packet = min(min_packet,diff)
    
print(min_packet)