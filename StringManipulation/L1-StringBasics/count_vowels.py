# count vowels, ignore case
def count_vowels (s: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    s = s.lower()
    for ch in s:
        if ch in vowels:
            count += 1
    return count

def count_vowels_set(s: str) -> int:
    vowels = frozenset('aeiou')
    return sum(ch in vowels for ch in s.lower())

if __name__ == '__main__':
    testString = 'OnomatoPeIa'
    print(count_vowels_set(testString))
