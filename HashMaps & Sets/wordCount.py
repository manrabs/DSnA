from collections import Counter

def find_most_common_word(word_dict):
    # Flatten the list of words from all dictionary values
    # all_words = [word for word_list in word_dict.values() for word in word_list]
    all_words = []
    for word_list in word_dict.values():
        for word in word_list:
            all_words.append(word)
    print(all_words)
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
print(f"The most common word is '{most_common}' with {count} appearances.")