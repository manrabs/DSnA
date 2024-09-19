class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            j = i-1

            while j >= 0 and nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
        return nums

if __name__ == '__main__':
    nums = [5,2,3,1]
    sol = Solution()
    print(sol.sortArray(nums))