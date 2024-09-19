# from collections import Counter, defaultdict
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)

# print(hash(42))            # Output: Hash value for integer 42
# print(hash("Hello"))       # Output: Hash value for string "Hello"
# print(hash((1, 2, 3)))     # Output: Hash value for tuple (1, 2, 3)
# print(globals())
# def foo(x: int) -> int:
#     print(locals())
# foo(1)
# def add(x, y):
#     return x+y
# m = [2, 4, 6]
# n = [3, 5, 7]
# result = map(add, m, n)
# print(list(result))

def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func() # 1
        return ret + 1
    return inner
def foo():
    return 1

namisan = outer(foo)
print(namisan())
