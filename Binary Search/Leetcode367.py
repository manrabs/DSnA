# Given a positive integer 'num', write a function which returns True if num is a perfect square
# and False otherwise. Do NOT use any built-in library function such as sqrt

class Solution:
    def isPerfectSquare(self, num:int) -> bool:
    # Brute force solution, 0(sqrt(n)) complexity
    #    for i in range(1, num+1):
    #         if i*i == num:
    #             return True
    #         if i*i > num:
    #             return False
        l, r = 1, num
        while l <= r:
            mid = (l + (r - l) // 2)
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False


if __name__ == '__main__':
    num = 626
    sol = Solution()
    x = sol.isPerfectSquare(num)
    print(x)