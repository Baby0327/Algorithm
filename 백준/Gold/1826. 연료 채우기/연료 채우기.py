import heapq
import sys
input = sys.stdin.readline

info = []

for i in range(int(input())):
    info.append(list(map(int, input().split())))

info.sort()
l, p = map(int, input().split())
cnt = 0
now = p
result = []

while now < l :
    while info and info[0][0] <= now :
        a, b = heapq.heappop(info)
        heapq.heappush(result, [-b, a])

    if not result :
        cnt = -1
        break

    b, a = heapq.heappop(result)
    now -= b
    cnt += 1

print(cnt)