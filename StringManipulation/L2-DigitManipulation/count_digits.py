"""
tally up the total amount of digits in a number
"""
def count_digits(n: int) -> int:
    total = 0
    s = str(n)
    for ch in s:
        total += 1
    return total

def count_digits_div(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
if __name__ == "__main__":
    number = 0
    print(count_digits_div(number))