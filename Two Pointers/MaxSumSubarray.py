# Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

class Solution:
    def find_best_subarray(self, nums: list[int], k: int) -> int:
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr
        for j in range(k, len(nums)):
            curr += nums[j] - nums[j-k]
            print(nums[j])
            ans = max(curr, ans)
        return ans

if  __name__ == "__main__":
    sol = Solution()
    nums = [3, -1, 4, 12, -8, 5, 6]
    k = 4
    print(sol.find_best_subarray(nums, k))