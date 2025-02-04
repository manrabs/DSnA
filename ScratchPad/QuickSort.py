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
    
if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = myQuickSort(arr)
    print(sorted_arr)