import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = sorted([list(map(int, input().split())) for _ in range(n)])
bag = sorted([int(input()) for _ in range(k)])
possible = []
result = 0

for i in bag:
    while jewel and jewel[0][0] <= i:
        m, v = heapq.heappop(jewel)
        heapq.heappush(possible, [-v])

    if possible:
        result -= heapq.heappop(possible)[0]

print(result)