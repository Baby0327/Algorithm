n, s = map(int, input().split())
now = 0

for i in range(n):
    now += int(input())
    if now > s and i < n - 1:
        now -= 1

print(now)