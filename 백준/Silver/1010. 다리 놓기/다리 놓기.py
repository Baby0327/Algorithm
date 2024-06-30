import sys

T = int(sys.stdin.readline())
result = []

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    num = 1
    for j in range(M, M-N, -1):
        num *= j
    tmp = 1
    for j in range(1, N+1):
        tmp *= j
    result.append(num//tmp)

for i in result:
    print(i)