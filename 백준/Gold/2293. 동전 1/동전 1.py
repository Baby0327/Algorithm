"""
동전 1
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
v = []
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    v.append(int(input()))

for i in v:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[-1])