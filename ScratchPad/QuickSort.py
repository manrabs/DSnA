import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def myQuickSort(arr):
    if len(arr) <= 1: return
    def qSort(l, r):
        if l >= r: return
        pivot = arr[r-1]
        m = l
        for i in range(l, r):
            if arr[i] < pivot:
                arr[i], arr[m] = arr[m], arr[i]
                m += 1
        arr[m], arr[r-1] = arr[r-1], arr[m]
        qSort(l, m - 1)
        qSort(m + 1, r)
    qSort(0, len(arr))
    return arr

# Given an unsorted array arr and an integer k, return the element at index k as if the array were sorted. \
# HINT: The array doesn't need to be fully sorted; instead, you can use an efficient algorithm to find the element at the specified index.
# Example 1: 
# Input: arr = [7, 10, 4, 3, 20, 15], k = 2
# Output: 4
# Explanation: The sorted array is [3, 4, 7, 10, 15, 20], and the element at index 2 is 4.

def quickselect(arr, k):
    def select(left, right, k):
        if left == right:  # If the list contains only one element
            return arr[left]
        
        # Select a random pivotIndex between left and right
        pivot_index = random.randint(left, right)
                
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        middle = left
        
        # Move all smaller elements to the left
        for i in range(left, right):
            if arr[i] < arr[pivot_index]:
                arr[middle], arr[i] = arr[i], arr[middle]
                middle += 1
        
        # Move pivot to its final place
        arr[right], arr[middle] = arr[middle], arr[right]
        
        # The pivot is in its final sorted position
        if k == middle:
            return arr[k]
        elif k < middle:
            return select(left, middle - 1, k)
        else:
            return select(middle + 1, right, k)
    return select(0, len(arr) - 1, k)

# The Quickselect algorithm efficiently finds the element at a specific index K in an array as if the array were sorted, without actually sorting the entire array. This is achieved by recursively partitioning the array around a randomly chosen pivot until the pivot is at the desired index K. The algorithm is similar to the Quicksort algorithm, but instead of recursively sorting both sides of the partition, it only recurses on the side of the partition that contains the desired index K.
if __name__ == '__main__':
    arr = [3,4,5,6,17,845,2432,5,1,6,8,8,9,34, 6, 8, 10, 1, 2, 1]
    print(quick_sort(arr))
    sorted_arr = myQuickSort(arr)
    print(sorted_arr)
    k = len(arr) - 2
    print(quickselect(arr, k))