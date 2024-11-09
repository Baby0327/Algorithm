import heapq
import sys
input = sys.stdin.readline

w = []
total = []

for i in range(int(input())):
    w.append(list(map(int, input().split())))

w.sort()

for i in w:
    heapq.heappush(total, i[1])
    if i[0] < len(total):
        heapq.heappop(total)

print(sum(total))