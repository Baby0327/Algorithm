import sys

A_N, A_M = map(int, sys.stdin.readline().split())
A = []

for i in range(A_N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

B_N, B_M = map(int, sys.stdin.readline().split())
B = []

for i in range(B_N):
    B.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0 for i in range(B_M)] for j in range(A_N)]
for i in range(A_N):
    for j in range(B_M):
        for k in range(A_M):
            result[i][j] += A[i][k]*B[k][j]

for i in range(A_N):
    for j in range(B_M):
        print(result[i][j], end=" ")
    print()