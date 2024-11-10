import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
counter = []
result = []

for i in range(n):
    id, w = map(int, input().split())
    if len(counter) < k:
        heapq.heappush(counter, [w, i + 1, id])
    else:
        out = heapq.heappop(counter)
        heapq.heappush(counter, [w + out[0], out[1], id])
        heapq.heappush(result, [out[0], -out[1], out[2]])

while counter:
    out = heapq.heappop(counter)
    heapq.heappush(result, [out[0], -out[1], out[2]])

print(sum(heapq.heappop(result)[2] * (i + 1) for i in range(len(result))))