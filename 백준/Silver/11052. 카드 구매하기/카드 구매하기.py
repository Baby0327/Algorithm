"""
카드 구매하기
"""

import sys
input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i], * [card[j] + dp[i - j] for j in range(1, i + 1)])

print(dp[-1])