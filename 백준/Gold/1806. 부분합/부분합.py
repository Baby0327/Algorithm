import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
l = r = 0
now = num[0]
result = 100000

while l <= r:
    if now < s:
        r += 1
        if r >= n: break
        now += num[r]
    else:
        result = min(r - l + 1, result)
        now -= num[l]
        l += 1

print(result if result < 100000 else 0)