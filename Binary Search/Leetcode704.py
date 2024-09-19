# Given an array of integers 'num' which is sorted in ascending order, and an integer 'target'
# write a function to search 'target' in 'nums'. 
# If target exists, then return its index. Otherwise return -1
class Solution:
    def binSearch (self, nums: list[int], target: int) -> int :
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + (r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    sol = Solution()
    x = sol.binSearch(nums, target)
    print(f"the index of the target is {x}")
