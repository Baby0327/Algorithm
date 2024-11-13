import heapq
import sys
input = sys.stdin.readline

n = int(input())

info = []
for _ in range(n):
    i, s, e = map(int, input().split())
    info.append([s, e, i])

info.sort()
h = []
room = [0] * n
cnt = 0

for s, e, i in info:
    if h and h[0][0] <= s:
        end, start, index = heapq.heappop(h)
        room[i - 1] = room[index - 1]
    else:
        cnt += 1
        room[i - 1] = cnt

    heapq.heappush(h, [e, s, i])

print(cnt)
print("\n".join(map(str, room)))