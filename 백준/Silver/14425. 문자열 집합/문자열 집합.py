import sys

N, M = map(int, sys.stdin.readline().split())

S = set()
for i in range(N):
    S.add(sys.stdin.readline().rstrip())

result = 0
for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp in S:
        result += 1

print(result)