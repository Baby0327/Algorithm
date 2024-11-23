import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
question = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for s in range(n - i):
        e = s + i

        if s == e:
            dp[s][e] = 1
        elif num[s] == num[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s + 1][e - 1]:
                dp[s][e] = 1

for s, e in question:
    print(dp[s - 1][e - 1])