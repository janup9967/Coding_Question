# What will be the output of the following code?
funcs = []

for i in range(5):
    funcs.append(lambda: i)

print([f() for f in funcs])

'''
 Your Task:

Predict the output
Explain why it behaves that way
(Bonus) Fix it so the output becomes:
[0, 1, 2, 3, 4]

'''

'''
Predicted Output of above code is [4, 4, 4, 4, 4] not [0, 1, 2, 3, 4]

Why does this happen?
This is due to Python's late binding behavior in closures.

The lambda function does not capture the value of i at each iteration
Instead, it captures the variable i itself (by reference)

By the time the lambdas are called:
i = 4   # final value after loop ends
So every function returns:
lambda: i  → 4

'''
#  Fixed Code so that Output will be [0, 1, 2, 3, 4]
funcs = []

for i in range(5):
    funcs.append(lambda i=i: i)

print([f() for f in funcs])

#  Output = [0, 1, 2, 3, 4] 
'''
Why this works:

i=i creates a new local variable for each lambda
That value is frozen at definition time, not execution time
'''
