import sys
input = sys.stdin.readline

n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]
result = []

for i in range(3):
    dp = [[10e6] * 3 for _ in range(n)]
    dp[0][i] = color[0][i]

    for j in range(1, n):
        dp[j][0] = color[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = color[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = color[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    dp[-1][i] = 10e6
    result.append(min(dp[-1]))

print(min(result))