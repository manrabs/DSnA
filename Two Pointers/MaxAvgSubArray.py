# LEETCODE 643
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000
 
# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

class Solution:
    def findMaxAverage(self, nums: list[int], k:int) -> float:
        n = len(nums)
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i] - nums[i-k]
            max_avg = max(max_avg, cur_sum / k)
        
        return max_avg
    
# Time Complexity: O(n)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
    print(sol.findMaxAverage([5], 1))
    print(sol.findMaxAverage([1,12,-5,-6,50,3], 2))