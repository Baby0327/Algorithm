N, M = map(int, input().split())

result = [0 for i in range (N)]

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i-1,j):
        result[y] = k

for x in result:
    print(x, end=" ")