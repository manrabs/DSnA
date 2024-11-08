# LEETCODE 169
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
from collections import defaultdict, Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        # Linear time and O(n) Solution
        # returns first answer to get to max value if there is more than one answer
        counter = Counter(nums)
        answer = -1
        maxCount = 0
        for key, val in counter.items():
            if val > maxCount:
                maxCount = val
                answer = key
        return answer
    
        # Linear time and O(1) Space solution
        # returns last answer to get to max value if there is more than one answer
        # count = 0
        # answer = -1
        # for num in nums:
        #     if count == 0:
        #         answer = num
            
        #     if num == answer:
        #         count += 1
        #     else:
        #         count -= 1
        # return answer

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,3,3,3,2,3]
    sol = Solution()
    print(sol.majorityElement(nums))