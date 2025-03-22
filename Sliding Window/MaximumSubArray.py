# Maximum Subarray
# Given an array of integers nums, find the subarray with the largest sum and return the sum.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [2,-3,4,-2,2,1,-1,4]
# Output: 8
# Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

# Example 2:
# Input: nums = [-1]
# Output: -1

# Constraints:
# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000

class Solution():
    def maxSubArray(self, nums: list[int]) -> int:
        # l, r = 0, 1
        # n = len(nums)
        # maxSum = nums[0]
        # while r < n:
        #     if nums[l] > 0:
        #         nums[r] += nums[l]
        #     maxSum = max(maxSum, nums[r])
        #     l = r
        #     r += 1
        currSum = 0
        maxSum = nums[0]
        for num in nums:
            # if currSum < 0:
            #     currSum = 0
            # currSum += num
            # the lines above have the same outcome as line 36 (the line below is more concise and elegant)
            currSum = max(num, currSum + num) # Kadane's Algorithm
            maxSum = max(maxSum, currSum)
        return maxSum

if __name__ == "__main__":
    nums = [2,-3,4,-2,2,1,-1,4]
    sol = Solution()
    print(sol.maxSubArray(nums))