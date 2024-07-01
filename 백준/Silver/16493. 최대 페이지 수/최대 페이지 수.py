import sys

input = sys.stdin.readline

n, m = map(int, input().split())

test = [[0, 0]]
for i in range(m):
    test.append(list(map(int, input().split())))

result = [[0 for i in range(n+1)] for j in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        day = test[i][0]
        page = test[i][1]
        if day > j:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-day]+page)

print(result[m][n])