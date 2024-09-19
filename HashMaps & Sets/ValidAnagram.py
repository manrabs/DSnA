# LEETCODE 242
#  Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        sDict = Counter(s)
        tDict = Counter(t)
        return sDict == tDict
    
if __name__ == '__main__':
    s = "anagram"
    t = "granamad"
    sol = Solution()
    print(sol.isAnagram(s, t))