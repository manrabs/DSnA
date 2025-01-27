class BubbleSort:
    def selection(arr):
        n = len(arr)
        # textbook approach
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

        # my intuitive approach, works but not efficient as it has more swaps.
        # for i in range(n):
        #     min_index = i
        #     for j in range(i+1, n):
        #         if arr[j] < arr[min_index]:
        #             min_index = j
        #             arr[j], arr[min_index] = arr[min_index], arr[j]
        # return arr
if __name__ == "__main__":
    arr = [50,2,-3,-1, 10]
    print(BubbleSort.selection(arr))