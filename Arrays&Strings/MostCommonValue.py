
from collections import Counter, deque

def find_most_common_word(word_dict):
    # Flatten the list of words from all dictionary values
    all_words = []
    for word_list in word_dict.values():
        for word in word_list:
            all_words.append(word)
    
    # Count the occurrences of each word
    word_counts = Counter(all_words)
    
    # Find the word with the highest count
    most_common_word = max(word_counts, key=word_counts.get)
    
    return most_common_word, word_counts[most_common_word]

# Example usage
word_dictionary = {
    'list1': ['apple', 'banana', 'cherry', 'date', 'apple'],
    'list2': ['apple', 'elderberry', 'fig', 'grape'],
    'list3': ['honeydew', 'apple', 'imbe', 'jackfruit']
}

most_common, count = find_most_common_word(word_dictionary)
# print(f"The most common word is '{most_common}' with {count} appearances.")

# multiline_str = 'Hi There\nHow are you?\nI am fine'
# multiline_str_split_list = multiline_str.split('\n')
# for s in multiline_str_split_list:
#     print(s)
nums = deque([2,4,6,8])
newnums = [1,3,5,7]
nums.extendleft(newnums)
print(nums)
print(list(reversed(nums)))
# ```

# This script does the following:

# 1. We define a function `find_most_common_word` that takes a dictionary as input.

# 2. Inside the function, we use a list comprehension to flatten all the word lists from the dictionary values into a single list `all_words`.

# 3. We use the `Counter` class from the `collections` module to count the occurrences of each word in `all_words`.

# 4. We use the `max` function with a key function to find the word with the highest count. The `key` function `word_counts.get` returns the count for each word, so `max` selects the word with the highest count.

# 5. The function returns both the most common word and its count.

# 6. In the example usage, we create a sample dictionary `word_dictionary` with lists of words as values.

# 7. We call the function with our dictionary and print the result.

# This script will work with any dictionary where the values are lists of words. It will find the word that appears most frequently across all the lists in the dictionary.

# If you run this script with the given example, it will output:
# ```
# The most common word is 'apple' with 4 appearances.
# ```

# You can modify the `word_dictionary` to test with different sets of words.​​​​​​​​​​​​​​​​