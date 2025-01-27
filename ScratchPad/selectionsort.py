class BubbleSort:
    def selection(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    arr[j], arr[min_index] = arr[min_index], arr[j]
        return arr
if __name__ == "__main__":
    arr = [50,2,-3,4,-2,2,5,1,-1,4,10]
    print(BubbleSort.selection(arr))