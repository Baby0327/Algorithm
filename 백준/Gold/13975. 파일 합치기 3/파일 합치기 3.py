import heapq
import sys
input = sys.stdin.readline

for i in range(int(input())):
    k = int(input())
    file = list(map(int, input().split()))
    heapq.heapify(file)
    cnt = 0

    while len(file) > 1:
        now = heapq.heappop(file) + heapq.heappop(file)
        heapq.heappush(file, now)
        cnt += now

    print(cnt)