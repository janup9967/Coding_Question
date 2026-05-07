

def max_product_subarray(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    zero = [x for x in arr if x == 0]
    pos = [x for x in arr if x > 0]
    neg = sorted([x for x in arr if x < 0])
    
    if not neg and not pos:
        return 0
    
    if not pos and len(neg) == 1:
        return 0 if zero else neg[0]
    
    if len(neg)%2 != 0:
        neg = neg[:-1]
    
    subset = neg + pos  
    if not subset:
        return 0
    
    result = 1
    for x in subset:
        result *=x
    
    return result

# -------- Test Cases --------
tests = [
    ([-1, 2, 3, 4],       24),
    ([-1, -2, 3, 4],      24),
    ([2, 3, 4],           24),
    ([-1, -2, -3, -4],    24),
    ([-1, -2, -3],         6),
    ([0, 2, 3, 4],        24),
    ([-1, -2, 0],          2),
    ([-1, 0],              0),
    ([-5],                -5),
    ([5],                  5),
    ([-1, -3, 2, 3, 4],   72),
]

for arr, expected in tests:
    result = max_product_subarray(arr)  # ✅ fixed function name
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] Input: {arr} => Got: {result}, Expected: {expected}")