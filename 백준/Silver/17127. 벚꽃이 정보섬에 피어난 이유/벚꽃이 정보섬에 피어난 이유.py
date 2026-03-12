n = int(input())
a = list(map(int, input().split()))
m = n - 3
c = []

for i in range(4):
    mul = 1

    if i == 0:
        now =  sum(a[i+m:])
    else:
        now = sum(a[:i] + a[i+m:])

    for j in range(i, i + m):
        mul *= a[j]

    now += mul
    c.append(now)

print(max(c))