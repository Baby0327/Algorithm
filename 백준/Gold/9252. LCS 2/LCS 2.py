import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
dp = [""] * len(s2)

for i in s1:
    temp = []
    for index, j in enumerate(s2):
        if i == j:
            temp.append(dp[index - 1] + i if index else i)
        else:
            now = temp[-1] if index else ""
            temp.append(dp[index] if len(dp[index]) > len(now) else now)
    dp = temp[:]

print(len(dp[-1]))
if len(dp[-1]):
    print(dp[-1])