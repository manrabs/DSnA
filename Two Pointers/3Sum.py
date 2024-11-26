# LEETCODE 15
#  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]

# Explanation: The only possible triplet sums up to 0. 
# Constraints:
# 3 <= nums.length <= 3000
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0: break
            elif i > 0 and nums[i] == nums[i - 1]: continue

            low, high = i+1, n-1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total == 0:
                    answer.append([nums[i], nums[low], nums[high]])
                    # move low up and high down (two pointer process) to search for more possible totals that are equal to 0
                    low, high = low+1, high-1
                    # check to see if low is less than high AND current low is the same as previous low, if it is, move low up again by one position
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    # check to see if low is less than high AND current high is the same as previous high, if it is, move high down again by one position (opposite of above basically)
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                # if total is less than 0, move low up by one position. this works because numbers in list will be in ascending order so you're increasing in value as you move up through the list.
                elif total < 0:
                    low += 1
                # opposite of above
                else:
                    high -= 1
        
        return answer

if __name__ == "__main__":
    numbers = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(numbers))