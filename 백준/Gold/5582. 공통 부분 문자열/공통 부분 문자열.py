import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
dp = [0] * (len(s1) + 1)
maxi = 0

for i in range(len(s2)):
    now = [0] * (len(s1) + 1)
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            now[j + 1] = dp[j] + 1
    maxi = max(maxi, *now)
    dp = now[:]

print(maxi)