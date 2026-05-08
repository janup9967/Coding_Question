'''
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:
i ≠ j, i ≠ k, j ≠ k
nums[i] + nums[j] + nums[k] == 0


✅ Requirements:

Do not return duplicate triplets
Return result in any order


📌 Example:
Input: nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2],
 [-1, 0, 1]]

⚠️ Constraints (Important 🔥):

Must be better than O(n³)
Expected solution: O(n²)

Function Signature:
def three_sum(nums: list[int]) -> list[list[int]]:
    pass


Hint (Don't skip this):

Sort the array
Fix one element
Use two pointers (left + right)
Carefully skip duplicates

'''
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    if not nums:
        return result
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if ((nums[i] + nums[j] + nums[k]) == 0):
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
    return result
    
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0, 0]))
print(three_sum([1, 2, 3, 4]))
print(three_sum([-5, -4, -3, -2, -1]))
print(three_sum([-2, 0, 1, 1, 2]))
print(three_sum([-1, 0, 1, 2, -1, -4, 2, -2]))
print(three_sum([]))

