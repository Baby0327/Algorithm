import heapq
import sys
input = sys.stdin.readline

hq = []
cnt = 0

for i in range(int(input())):
    heapq.heappush(hq, int(input()))

while len(hq) > 1:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        heapq.heappush(hq, a + b)
        cnt += a + b

print(cnt)