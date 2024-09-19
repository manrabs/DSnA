import heapq 
A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(A)

for i in range(n):
    A[i] *= -1
heapq.heapify(A)
print(A)