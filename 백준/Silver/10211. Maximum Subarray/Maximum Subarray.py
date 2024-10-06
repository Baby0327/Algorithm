"""
Maximum Subarray
"""

import sys
input = sys.stdin.readline

def maximum(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]

    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])

    return max(dp)


t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(maximum(arr))