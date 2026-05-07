'''
Input 10 20 30 40 

Code
arr = list(map(int,input().split()))
print(arr)

'''

'''
Input   10,20,30,50

Code
arr = list(map(int,input().split(",")))
print(arr)
'''

'''
input : 2 3

Code

a, b = map(int,input().split())
print(f"{a} & {b}")
'''

'''

my_list = [1, 2, 3, 4]
print(my_list)
print("different way to print list ")
print(*my_list, sep=", ")

names = ["Anup", "Kailas", "Mahak"]
print(" ".join(names))
'''

'''
n = int(input().strip())
arr = list(map(int,input().split()))
rank_map = {}
rank = 1
for i in sorted(arr):
    if i not in rank_map:
        rank_map[i] = rank
        rank +=1

result = [rank_map[x] for x in arr]
print(*result) 

Input 
5
20 30 8 2 5

Output
4 5 3 1 2
'''

'''
Remove characters from first string which are present in second string

Input :
abcdef
cefz

output :  
abd

str1 = input().strip()
str2 = input().strip()
# result = ''.join([c for c in str1 if c not in str2])  time complexity = O(m*n)
result_list = []
remove_set = set(str2)  
for letter in str1:
    if letter not in remove_set:
        result_list.append(letter)

result = "".join(result_list)
# time complexity = O(m+n)

print(result)
'''

'''
Not Repeating Elements

Input :
6
1 2 -1 1 3 1 

output :  
2 -1 3 

'''

n = int(input().strip())
arr = list(map(int,input().split()))
count_map = {}
for num in arr:
    count_map[num] = count_map.get(num,0)+1
    
result = []

for num in arr:
    if count_map[num] == 1:
        result.append(num)
        
print(" ".join(map(str,result))) if result else print(-1)

print(*result) if result else print(-1)
 