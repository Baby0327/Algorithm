import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
dp = [0] * len(s2)

for i in range(len(s1)):
    temp = 0
    for j in range(len(s2)):
        if temp < dp[j]:
            temp = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = temp + 1

print(max(dp))