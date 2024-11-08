import heapq
import sys
input = sys.stdin.readline

w = []

for i in range(int(input())):
    d, s = map(int, input().split())
    heapq.heappush(w, [-s, d])

result = {}
while w:
    s, d = heapq.heappop(w)

    while 1:
        if d == 0:
            break

        if result.get(d, 0):
            d -= 1
        else:
            result[d] = -s
            break

print(sum(result.values()))