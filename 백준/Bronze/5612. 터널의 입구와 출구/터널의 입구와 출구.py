n = int(input())
now = int(input())
maxi = [now]

for i in range(n):
    s, e = map(int, input().split())
    now += s - e

    if now < 0:
        maxi = [0]
        break

    maxi.append(now)

print(max(maxi))