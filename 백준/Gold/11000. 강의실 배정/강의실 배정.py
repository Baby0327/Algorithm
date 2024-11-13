import heapq
import sys
input = sys.stdin.readline

n = int(input())
info = sorted([list(map(int, input().split())) for _ in range(n)])
h = []
cnt = 0

for start, end in info:
    while h and h[0] <= start:
        heapq.heappop(h)

    heapq.heappush(h, end)

    if len(h) > cnt:
        cnt = len(h)

print(cnt)