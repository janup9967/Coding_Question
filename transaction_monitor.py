'''
you are bulding a transaction monitoring system 
Procss N Transactions, each 4 fields sender, receiver timestamp, amount 

r rules in order for each transactios print exactly one output and terminate when a rule fires

Rules:
1. Duplicate Transactions Check
if any transaction have same sender & receiver as any previous transaction

2. Fraud Detection
if the diff betn timestamp of any two consecutive transaction is > 60 sec

3. All Transaction Valid
If the entire loop complete without trigging rule 1 or 2
print "All Transaction Valid"

'''

n = int(input())
transactions = []
for i in range(n):
    sender,receiver,timestamp, amount = input().strip().split()
    transactions.append([sender,receiver,int(timestamp),int(amount)])
    
seen = set()
prevtime = -1
for i in range(n):
    sender,receiver,timestamp, amount = transactions[i]
    if (sender,receiver) in seen:
        print("Duplicate Transaction")
        break
    seend.add((sender,receiver))
    if prevtime != -1 and timestamp-prevtime > 60:
        print("Fraud Detected")
        break
    prevtime= timestamp 
else:
    print("All Transaction Valid")


