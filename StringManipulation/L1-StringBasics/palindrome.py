def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i].lower() != s[n-1-i].lower():
            return False
    return True

def is_palindrome_slicing(s: str) -> bool:
    return s.lower() == s[::-1].lower()

def is_palindrome_binary(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    testString = 'racecaR'
    print(is_palindrome_binary(testString))