import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

limit = max(cost, key=lambda x : x[1])[1]
dp = [10e5] * (c + limit)
dp[0] = 0

for i, j in cost:
    for k in range(1, c + limit):
        if j <= k:
            dp[k] = dp[k] if dp[k] <= dp[k - j] + i else dp[k - j] + i

print(min(dp[c:]))