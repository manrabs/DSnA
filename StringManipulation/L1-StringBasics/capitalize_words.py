def capitalize(s: str) -> str:
    newList = []
    for i in range(len(s)):
        if i == 0 or s[i - 1] == ' ':
            newList.append(s[i].upper())
            continue
        newList.append(s[i])

    return ''.join(newList)

if __name__ == "__main__":
    testString = "the quick brown fox jumped over the dog"
    print(capitalize(testString))