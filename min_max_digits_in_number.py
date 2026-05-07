
'''
You are given a positive integer n. Your task is to find the minimum and maximum digits in the number n and print them as a space-separated pair.
'''

n = int(input().strip())
max_digit = 0
min_digit = 9

while n>0 :
    digit = n%10 
    min_digit = min(min_digit,digit)
    max_digit = max(max_digit,digit)
    n //=10

print(min_digit,max_digit)