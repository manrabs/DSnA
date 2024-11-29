# LEETCODE 977
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n-1
        answer = []
        while l <= r:
            # the two pointer approach, combined with these conditionals comparing absolute values, enable us to create the answer list in decreasing order then we use the reverse function outside the loop to output the list in increasing order
            if abs(nums[l]) > abs(nums[r]):
                answer.append(nums[l] ** 2)
                l += 1
            else:
                answer.append(nums[r] ** 2)
                r -= 1
        answer.reverse()
        return answer
    
if __name__ == "__main__":
    numbers = [-7,-3,2,3,11]
    sol = Solution()
    print(sol.sortedSquares(numbers))