import heapq

heap: heapq = []
numbers = [9, 2, 4, 1, 3, 11]

for number in numbers:
    heapq.heappush(heap, number)

print(heap)

heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)

print(heap)
