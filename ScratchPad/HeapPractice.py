import heapq 
# A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
# n = len(A)

# for i in range(n):
#     A[i] *= -1
# heapq.heapify(A)
# print(A)

class Nodes:
    def find_missing_children(heap):
        n = len(heap)
        missing_nodes = []

        for i in range(n):
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            missing = []
            if left_child >= n:
                missing.append("left")
            if right_child >= n:
                missing.append("right")

            if missing:
                missing_nodes.append({
                    "node": heap[i],
                    "missing_children": missing
                })

        return missing_nodes
    
    def insert_last(heap, val):
        # heapq.heappush(heap, val)
        heap.append(val)
        n = len(heap)
        i = n - 1
        while i > 0 and heap[i] < heap[(i-1)//2]:
            heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
            i = (i-1)//2
    
    def insert_first(heap, val):
        heap.insert(0, val)
        n = len(heap)
        i = 0

        while True:
            smallest = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < n and heap[left_child] < heap[smallest]:
                smallest = left_child
            if right_child < n and heap[right_child] < heap[smallest]:
                smallest = right_child
            if smallest != i:
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
            else:
                break
# # Example usage
if __name__ == "__main__":
    heap = [1, 3, 6, 5, 9, 8]
    result = Nodes.find_missing_children(heap)
    print(result)
    result2 = Nodes.insert_last(heap, 4)
    print(heap)
    Nodes.insert_first(heap, 7)
    print(heap)
