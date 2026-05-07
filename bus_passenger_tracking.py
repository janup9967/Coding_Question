'''
A Bus travels through serveral stations 
at each station
some passengers get off
some passengers get on

find the maximum number of passsenger in the bus at any time

Input Format
First Line : N Int (number of stations)
Next N Lines : 2 space separated Int (number of passengers get off and get on at each station)

Output Format
Maximum number of passsenger in the bus at any time

Sample Input
3
10 30
20 40
15 25

Sample Output
50

Explanation
At Station 1: 30-10 = 20 passenger
At Station 2: 20+40-20 = 40 passenger  
At Station 3: 40+25-15 = 50 passenger

So maximum passenger is 50

Sample Input 2
4
0 3
2 5
4 2
4 0

Sample Output 2
6 


Explanation 2
At Station 1: 3-0 = 3 passenger
At Station 2: 3+5-2 = 6 passenger
At Station 3: 6+2-4 = 4 passenger
At Station 4: 4+0-4 = 0 passenger

So maximum passenger is 6
'''

n = int(input())
max_pass = 0
current = 0
for i in range(n):
    off,on = map(int,input().split())
    current  += on - off
    max_pass = max(max_pass,current)
    
print(max_pass)
