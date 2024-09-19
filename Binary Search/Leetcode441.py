# You have n coins and you want to build a staircase with these coins. 
# The staircase consists of k rows where the ith row has exactly i coins. 
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of COMPLETE rows of the staircase you will build.
# i.e. with a limited number of coins, output the number of COMPLETE rows you will build

class Solution:
    def arrangingCoins(self, num: int) -> int:
        l, r = 1, num
        result = 0
        while l <= r:
            mid = (l + (r - l) // 2)
            coins = (mid / 2) * (mid + 1)
            if coins > num:
                r = mid - 1
            else:
                l = mid + 1
                result = max(mid, result)
        return result


if __name__ == '__main__':
    n = 80
    sol = Solution()
    rows = sol.arrangingCoins(n)
    print(rows)
