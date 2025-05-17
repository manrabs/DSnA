# #Leetcode 56

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. 

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals:list[list[int]]):
        # sort interval list by first value in each pair
        intervals.sort(key = lambda interval: interval[0])
        merged = []
        for interval in intervals:
            # add next pair to merged list if empty or if the 2nd value in the last pair of merged list (merged[-1][1]) is less than the first value of current pair (interval[0]) in intervals list
            print(f"{interval} consists of: {interval[0]} and {interval[1]}")
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # otherwise update the last pair of the merged list to maintain it's current first value and change the 2nd value to the larger of the two end values (i.e. higher value between 2nd value of the current interval pair and 2nd value of the current last pair in merged list)
            # essentially we're handling overlapping intervals by taking the maximum of the two possible end values
            else:
                merged[-1] = [merged[-1][0], max(interval[1], merged[-1][1])]
        return merged
if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,4], [2,5], [5,7], [6,8]]
    print(sol.merge(intervals))