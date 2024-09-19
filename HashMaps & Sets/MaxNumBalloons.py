# LEETCODE 1189
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible. You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0
 
# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import Counter, defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = defaultdict(int)
        balloon = 'balloon'
        count = 0
        for t in text:
            if t in balloon:
                balloonCounter[t] += 1
        
        if any(t not in balloonCounter for t in balloon):
            return 0
        else:
            return min(balloonCounter['b'], balloonCounter['a'], balloonCounter['l']//2, balloonCounter['o']//2, balloonCounter['n'])
    

if __name__ == '__main__':
     text = "loonbalxballpoon"
     sol = Solution()
     print(sol.maxNumberOfBalloons(text))
    #  board = [["8","3","5"],
    #           ["6","4","1"],
    #           ["7","9","2"]]
    #  for i in range(3):
    #         s = set()
    #         for j in range(3):
    #             item = board[j][i]
    #             print(item)