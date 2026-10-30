'''
function that takes in a number and returns the sum of numbers in that number e.g. 
input = 4719
output = 21
explanation => 4+7+1+9 = 21
'''
def digit_sum_str(n: int) -> int:
    s = str(n)
    total = 0
    for i in range(len(s)):
        total += int(s[i])
    return total

def digit_sum_modulo(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    number = 5280
    number2 = 4179
    print(digit_sum_str(number))
    print(digit_sum_modulo(number2))