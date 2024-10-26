import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []

for i in range(n):
    num.append(int(input()))

num.sort()

s = e = 0
result = 2000000000

while s <= e and e < n :
    now = num[e] - num[s]
    if now < m:
        e += 1
    elif now >= m:
        result = min(now, result)
        s += 1

print(result)