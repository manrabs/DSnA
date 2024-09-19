# LEETCODE 20
#  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        closeMap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for c in s:
            if c in closeMap:
                if stack and stack[-1] == closeMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

if __name__ == '__main__':
    s = "()[]}"
    sol = Solution()
    print(sol.isValid(s))