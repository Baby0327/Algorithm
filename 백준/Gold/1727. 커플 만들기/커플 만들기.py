import sys
input = sys.stdin.readline

n, m = map(int, input().split())
man = sorted(list(map(int, input().split())))
woman = sorted(list(map(int, input().split())))
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        now = dp[i - 1][j - 1] + abs(woman[i - 1] - man[j - 1])
        
        if i < j:
            dp[i][j] = min(now, dp[i][j - 1])
        elif i > j:
            dp[i][j] = min(now, dp[i - 1][j])
        else:
            dp[i][j] = now

print(dp[m][n])