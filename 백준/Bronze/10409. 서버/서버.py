n, t = map(int, input().split())
num = list(map(int, input().split()))
i = 0

while i < n:
    t -= num[i]

    if t < 0:
        break

    i += 1

print(i)