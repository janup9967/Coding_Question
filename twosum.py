'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

✅ Conditions:

Each input has exactly one solution
You cannot use the same element twice
Return the answer in any order


📌 Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
⚠️ Twist (Important 🔥):

You must solve it in O(n) time
Nested loops (O(n²)) are NOT allowed


✅ Function Signature:
def two_sum(nums: list[int], target: int) -> list[int]:    

💡 Hint (if needed):
Think about:

How to store previously seen numbers
How to instantly check if the required number exists
'''

def two_sum(nums: list[int],target:int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        a = target -nums[i]
        if a in seen:
            return [seen[a],i]
        else:
            seen[nums[i]] = i
    else:
        return []

print(two_sum([2, 7, 11, 15],9))
print(two_sum([-3, 4, 3, 90],0))
print(two_sum([3, 3],6))
print(two_sum([1, 2, 3, 4, 5],10))