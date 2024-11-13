import heapq
import sys
input = sys.stdin.readline

n = int(input())
info = sorted([list(map(int, input().split())) for _ in range(n)])
h = []
heapq.heappush(h, info[0][1])

for i in range(1, n):
    if info[i][0] >= h[0]:
        heapq.heappop(h)
    heapq.heappush(h, info[i][1])

print(len(h))