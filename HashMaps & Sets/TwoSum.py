# LEETCODE 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # numMap = {}
        # n = len(nums)

        # for i in range(n):
        #     numMap[nums[i]] = i

        # for i in range(n):
        #     y = target - nums[i]
        #     if y in numMap and numMap[y] != i:
        #         return [i, numMap[y]]
        # return [] 

        numMap = defaultdict(lambda: -1)
    
        for i, num in enumerate(nums):
            complement = target - num
            if numMap[complement] != -1:
                return [numMap[complement], i]
            numMap[num] = i
        
        return []

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))