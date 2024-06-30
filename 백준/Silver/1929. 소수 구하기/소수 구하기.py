import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

result = [1 for i in range(N+1)]
result[0] = 0
result[1] = 0

for i in range(2, int(N**(1/2))+1):
    if result[i] == 1:
        for j in range(i*2, N+1, +i):
            result[j] = 0

for i in range(M, N+1):
    if result[i] == 1:
        print(i)