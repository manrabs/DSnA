def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

if __name__ == '__main__':
    print(findDuplicate([3,1,3,4,2]))
    letters = set([3,2,1,34,4,2,4,4,1,3])
    print (letters)
    letters.add(2)
    print (letters)
