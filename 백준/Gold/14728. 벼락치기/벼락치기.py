import sys

input = sys.stdin.readline

n, t = map(int, input().split())
test = [[0,0]]
for i in range(n):
    test.append(list(map(int, input().split())))

result = [[0 for i in range(t+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, t+1):
        k = test[i][0]
        s = test[i][1]
        if j < k:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-k]+s)

print(result[n][t])