"""
연속합
"""

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [0] * n
dp[0], result = num[0], num[0]

for i in range(1, n):
    dp[i] = num[i] if num[i] > dp[i - 1] + num[i] else  dp[i - 1] + num[i]
    
    if dp[i] > result:
        result = dp[i]

print(result)