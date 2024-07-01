import sys

N, M = map(int, sys.stdin.readline().split())

memo = {}
for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    memo[tmp] = 0

for i in range(M):
    tmp = list(sys.stdin.readline().rstrip().split(","))
    for j in range(len(tmp)):
        if tmp[j] in memo:
            del memo[tmp[j]]
    print(len(memo))