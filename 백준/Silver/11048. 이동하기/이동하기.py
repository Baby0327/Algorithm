"""
이동하기
"""

n, m = map(int, input().split())
candy = []

for i in range(n):
    candy.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            candy[i][j] += candy[i][j-1]
        elif j == 0:
            candy[i][j] += candy[i-1][j]
        else:
            candy[i][j] += max([candy[i-1][j-1], candy[i-1][j], candy[i][j-1]])

print(candy[-1][-1])