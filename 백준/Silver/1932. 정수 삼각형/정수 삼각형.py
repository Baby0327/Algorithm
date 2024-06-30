import sys

n = int(sys.stdin.readline())

triangle = []
for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0 for i in range(j+1)] for j in range(n)]
result[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            result[i][j] = triangle[i][j] + result[i-1][j]
        elif j == i:
            result[i][j] = triangle[i][j] + result[i-1][j-1]
        else:
            result[i][j] = triangle[i][j] + max(result[i-1][j-1], result[i-1][j])

print(max(result[n-1]))