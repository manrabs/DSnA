# LEETCODE 49
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
from collections import defaultdict
class SortedSolution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # sort the word and use it as a key in the hashmap
            sortedWord = ''.join(sorted(word))
            # if sortedword is in the hashmap, append the word as a value of the key (because it is possible for multiple words to have the same sorted word)
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            # otherwise the sorted word is not in the hashmap. in that case you just add it as a key and then the word becomes the value (possibly the first value of many)
            else:
                anagrams[sortedWord] = [word]
        print(anagrams)
        return list(anagrams.values())

class OptimalSolution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # create a tuple of character counts
            charCount = [0] * 26
            for char in word:
                # increment the count of the character in the character count array by using the ascii value of the character as the index
                charCount[ord(char) - ord('a')] += 1
            # convert the character count array to a tuple so it can be used as a key in the hashmap
            key = tuple(charCount)
            anagrams[key].append(word)
        return list(anagrams.values())

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = OptimalSolution()
    print(sol.groupAnagrams(strs))