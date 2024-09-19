# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1
        # res = []

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            # print(nums[right])
            # print(curr)
            ans += right - left + 1
            # res.append(nums[right])
            # print(res)

        return ans
    


if  __name__ == "__main__":
    sol = Solution()
    series = [10, 5, 2, 6]
    m = 100
    print(sol.numSubarrayProductLessThanK(series, m))