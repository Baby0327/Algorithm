import sys

N, K = map(int, sys.stdin.readline().split())

coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline()))

count = 0
i = N-1
while K != 0:
    if K >= coin[i]:
        count += K//coin[i]
        K %= coin[i]
    i -= 1

print(count)