import heapq

n, m = map(int, input().split())
lst = list(map(int, input().split()))
heap = []
for i in lst:
    heapq.heappush(heap, i)

for i in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    heapq.heappush(heap, a+b)

print(sum(heap))