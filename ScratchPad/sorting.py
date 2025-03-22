class InsertionSort:
    def insert(self, arr):
        n = len(arr)
        for i in range(n):
            j = i
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
        return arr

class MergeSort: # sorting algorithm that uses the divide and conquer paradigm, works for already sorted arrays 
    def merge(self, a, b):
        n, m = len(a), len(b)
        i = j = 0
        res = []
        # while i < n or j < m:
        #     if j == m or (i < n and a[i] < b[j]):
        #         res.append(a[i])
        #         i += 1
        #     else:
        #         res.append(b[j])
        #         j += 1
        # return res
        while i < n and j < m:
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        return res + a[i:] + b[j:]

if __name__ == "__main__":
    # arr = [2,-3,4,-2,2,1,-1,4]
    # ins = InsertionSort()
    # print(ins.insert(arr)) # [-3, -2, -1, 1, 2, 2, 4, 4]
    a, b = [1, 3, 5, 7, 15], [2, 4, 6, 8, 10, 28, 30]
    merger = MergeSort()
    print(merger.merge(a, b)) # [1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 28, 30]