import heapq
import sys
input = sys.stdin.readline

n = int(input())
info = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : x[1])
h = []
cnt = 0

for num, start, end in info:
    while h and h[0] <= start:
        heapq.heappop(h)

    heapq.heappush(h, end)

    if len(h) > cnt:
        cnt = len(h)

print(cnt)