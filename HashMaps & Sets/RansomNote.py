# LEETCODE 383
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = Counter(magazine)

        # for m in magazine:
        #     if m in magDict:
        #        magDict[m] += 1
        #     else:
        #        magDict[m] = 1

        for note in ransomNote:
            if note not in magDict:
                return False
            elif magDict[note] == 1:
                del magDict[note]
            else:
                magDict[note] -= 1
        return True

if __name__ == '__main__':
    ransomNote = "abb"
    magazine = "aab"
    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))