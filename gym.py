"""
A gym offers membership plans based on the number of months a customer wants to enroll. The cost of the membership is determined as follows:

Duration (Months)	Cost (₹)
≤ 0	                Invalid Input
1	                2000
2 to 3	            5000
4 to 6	            9000
> 6	                15000

Task
Write a program that: Takes an integer input for months

Prints:
    "Invalid Input" if months <= 0
    Otherwise prints: Cost: <amount>
Input Format
    A single integer months
Output Format
    Print "Invalid Input" OR
    Print:Cost: <amount>

Sample Test Cases
    Test Case 1
        Input:
            1
        Output:
            Cost: 2000
            
    Test Case 2
        Input:
            3
        Output:
            Cost: 5000

    Test Case 3
        Input:
            5
        Output:
            Cost: 9000

    Test Case 4
        Input:
            7
        Output:
            Cost: 15000

    Test Case 5
        Input:
            0
        Output:
            Invalid Input
"""

def gym_membership_fees(month):
    if month > 6: 
        return 15000
    elif  month <= 6 :
        return 9000
    elif  month <= 3:
        return 5000
    elif month == 1:
        return 2000
    else:
        return "Invalid Input"
    
    
    
n = int(input())
if n >0:
    print(f"Cost: {gym_membership_fees(n)}")
else:
    print(gym_membership_fees(n))
    

""" months = int(input())

if months <= 0:
    print("Invalid Input")
elif months == 1:
    print("Cost: 2000")
elif months <= 3:
    print("Cost: 5000")
elif months <= 6:
    print("Cost: 9000")
else:
    print("Cost: 15000")
    
"""