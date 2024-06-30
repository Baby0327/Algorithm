N, M = map(int, input().split())

A = []
B = []
# result = [[0 for i in range(N)] for j in range(M)]

for i in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp)

for i in range(N):
    tmp = list(map(int, input().split()))
    B.append(tmp)

for i in range(0, N):
    for j in range(0, M):
        print(A[i][j] + B[i][j], end=" ")
    print()