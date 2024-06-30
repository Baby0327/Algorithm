import sys

N, M = map(int, sys.stdin.readline().split())
num = []
for i in range(N):
    num.append(list(map(int, sys.stdin.readline().rstrip())))


result = 0
for i in range(N):
    for j in range(M-i):
        for k in range(N-i):
            if num[k][j] == num[k+i][j] == num[k][j+i] == num[k+i][j+i]:
                result = i+1

print(result**2)