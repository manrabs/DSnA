def reverse_num(n: int) -> int:
    sign = -1 if n < 0 else 1
    # int() strips the leading zeros the reversal creates: 1200 -> "0021" -> 21
    return sign * int(str(abs(n))[::-1])


def reverse_num_math(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reverse = 0
    while n > 0:
        remainder = n % 10       # peel the rightmost digit off n
        reverse = reverse * 10 + remainder   # shift rev left one place, drop digit in
        n //= 10             # chop that digit off n
    return sign * reverse


if __name__ == "__main__":
    number = 4321
    print(reverse_num_math(number))