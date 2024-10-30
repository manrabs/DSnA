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
        left = 1
        right = 1
        n = len(nums)
        left_arr = [0] * n
        right_arr = [0] * n
        res = []

        for i in range(n):
            j = -i -1 # cool way to go forwards and backwards on the array at the same time where i is at index zero and j is at index len-1
            
            # code below populates new left_arr and right_arr by assigning the values of left and right variables (i.e., the number 1, initially) to the
            # current index of left_arr and right_arr. Then it multiplies the left and right variables (i.e. 1, initially) by the respective current index of the original nums list.
            left_arr[i] = left
            right_arr[j] = right
            left *= nums[i]
            right *= nums[j]

        # zip function is used to iterate over the left_arr and right_arr lists simultaneously, pairing up the elements at the same index from the two lists and returns them as a tuple on each iteration.
        # The for loop then unpacks each tuple into the variables l and r, which represent the corresponding elements from the left_arr and right_arr lists, respectively
        # The overall effect is the main juice of the squeeze (i.e. the problem) because multiplication occurs on each pair of corresponding elements from the left_arr and right_arr lists, and collects the results in the res list.   
        for l, r in zip(left_arr, right_arr):
            res.append(l*r)
        
        return res

        # O(1) space complexity solution
        # n = len(nums)
        # res = [0] * n
        # left = 1
        # for i in range(n):
        #     res[i] = left
        #     left *= nums[i]
        # right = 1
        # for i in range(n-1, -1, -1):
        #     res[i] *= right
        #     right *= nums[i]
        # return res 

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))