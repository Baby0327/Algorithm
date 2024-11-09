import heapq
import sys
input = sys.stdin.readline

c = []

for i in range(int(input())):
    p, d = map(int, input().split())
    heapq.heappush(c, [-p, d])

result = {}
while c:
    p, d = heapq.heappop(c)

    while 1:
        if d == 0:
            break

        if result.get(d, 0):
            d -= 1
        else:
            result[d] = -p
            break

print(sum(result.values()))