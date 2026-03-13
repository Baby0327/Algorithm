n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    s = 0

    for i in range(l, r):
        s += abs(a[i - 1] - a[i])

    print(s)