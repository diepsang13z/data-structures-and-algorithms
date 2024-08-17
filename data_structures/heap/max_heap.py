import heapq

numbers = [4, 1, 24, 2, 1]
invert_numbers = [-1 * n for n in numbers]
size = len(invert_numbers)

heapq.heapify(invert_numbers)

heap = []
for _ in range(size):
    heap.append(-1 * heapq.heappop(invert_numbers))

print(heap)
