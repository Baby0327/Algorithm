import sys

input = sys.stdin.readline

n, k = map(int, input().split())

subject = [[0,0]]
for i in range(k):
    subject.append(list(map(int, input().split())))

result = [[0 for i in range(n+1)] for j in range(k+1)]
for x in range(1, k+1):
    for y in range(1, n+1):
        i = subject[x][0]
        t = subject[x][1]
        if y < t:
            result[x][y] = result[x-1][y]
        else:
            result[x][y] = max(result[x-1][y], result[x-1][y-t]+i)

print(result[k][n])