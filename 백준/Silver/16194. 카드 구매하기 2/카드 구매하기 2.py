"""
카드 구매하기 2
"""

import sys
input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))
dp = card.copy()

for i in range(1, n + 1):
    dp[i] = min(dp[i], *[card[j] + dp[i - j] for j in range(1, i + 1)])

print(dp[-1])