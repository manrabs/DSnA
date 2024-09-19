# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l , r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + (r - l) // 2)
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
    
        # GPT Solution
        # left, right = 0, len(nums) - 1
    
        # while left < right:
        #     mid = (left + right) // 2
            
        #     # If mid element is greater than the rightmost element, min must be to the right of mid
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     # Otherwise, min must be to the left of mid or at mid
        #     else:
        #         right = mid
        
        # # When left == right, we have found the smallest element
        # return nums[left]

if __name__ == '__main__':
    nums = [7, 8, 9, 2, 3, 4]
    fm = Solution()
    print(fm.findMin(nums))
    a = "Hi"
    b = "hi"
    print(a == b)