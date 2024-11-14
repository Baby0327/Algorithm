import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = sorted(list(map(int, input().split())), reverse=True)
result = []

for i in t:
    if len(result) < m:
        heapq.heappush(result, i)
    else:
        heapq.heappush(result, i + heapq.heappop(result))

print(max(result))