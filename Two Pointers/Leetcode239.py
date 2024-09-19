# Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max value in each sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque() # will contain indices and not values
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: 
                # while deque is non empty and right most value of deque is less than value of r (i.e. while values smaller than value of r exist in queue), keep popping values (remember popping values using .pop() function only begins from the top/right hand side of the deque)
                q.pop()
            q.append(r)

            # if left value is out of bounds (i.e greater than left value of the deque), pop from the left
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
        

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))