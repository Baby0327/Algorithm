import sys


N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
tmp = [0]

for i in range(N):
    tmp.append(tmp[i] + line[i])

M = int(sys.stdin.readline())

result = []
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    result.append(tmp[y]-tmp[x-1])

for i in result:
    print(i)