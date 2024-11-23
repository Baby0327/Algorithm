import sys
input = sys.stdin.readline

n = int(input())
v = []

for i in range(n):
    r, c = map(int, input().split())
    v.append(r)

v.append(c)
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    for j in range(1, n - i + 1):
        now = i + j
        dp[j][now] = 2 ** 32

        for k in range(j, now):
            dp[j][now] = min(dp[j][now], dp[j][k] + dp[k + 1][now] + v[j - 1] * v[k] * v[now])

print(dp[1][-1])