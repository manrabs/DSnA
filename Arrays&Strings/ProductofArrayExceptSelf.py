# LEETCODE 238
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # O(n) space complexity solution
        prefix = 1
        postfix = 1
        n = len(nums)
        pre_arr = [0] * n
        post_arr = [0] * n
        res = []

        for i in range(n):
            j = -i -1
            pre_arr[i] = prefix
            post_arr[j] = postfix
            prefix *= nums[i]
            postfix *= nums[j]
        
        for pre, post in zip(pre_arr, post_arr):
            res.append(pre*post)
        
        return res

        # O(1) space complexity solution
        # n = len(nums)
        # res = [0] * n
        # prefix = 1
        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(n-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res 

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))