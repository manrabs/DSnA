def reverse_string(s: str) -> str:
    # O(n-squared) complexity
    newString = ''
    for ch in s:
        newString = ch + newString #prepend not append. 'abc' becomes, 'a', then 'ba', then 'cba'
    return newString

def reverse_string_range(s: str) -> str:
    # O(n-squared) complexity generally, O(n) in this exact shape
    newString = ''
    for i in range(len(s) -1, -1, -1):
        newString += s[i]
    return newString

def reverse_string_slice(s: str) -> str:
    # O(n) complexity guaranteed
    return s[::-1]

def reverse_string_join(s: str) -> str:
     # O(n) complexity guaranteed
    stringList = []
    for i in range(len(s) - 1, -1, -1):
        stringList.append(s[i])
    return ''.join(stringList)

if __name__ == '__main__':
    testString = 'programming'
    print(reverse_string_join(testString))