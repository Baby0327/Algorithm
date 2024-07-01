import sys

input = sys.stdin.readline

n, k = map(int, input().split())

test = [[0,0]]
for i in range(n):
    test.append(list(map(int, input().split())))

result = [[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = test[i][0]
        v = test[i][1]
        if j < w:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j-w]+v, result[i-1][j])

print(result[n][k])