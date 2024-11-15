import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
box = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x : x[1])
truck = [c] * (n + 1)
maxi = 0

for send, receive, count in box:
    now = min(count, min(truck[send - 1 : receive - 1]))

    if now:
        for i in range(send - 1, receive - 1):
            truck[i] -= now
        maxi += now

print(maxi)