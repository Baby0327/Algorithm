"""
파스칼의 삼각형
"""

num = [[1], [1, 1]]
n, k = map(int, input().split())

for i in range(n-2):
    temp = [1]

    for j in range(len(num[-1]) - 1):
        temp.append(num[-1][j] + num[-1][j+1])

    temp.append(1)
    num.append(temp)

print(num[n - 1][k - 1])