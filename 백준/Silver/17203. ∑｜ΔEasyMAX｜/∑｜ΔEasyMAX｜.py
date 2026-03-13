n, q = map(int, input().split())
a = list(map(int, input().split()))
s = [0]

for i in range(n - 1):
    s.append(s[-1] + abs(a[i + 1] - a[i]))

for _ in range(q):
    l, r = map(int, input().split())
    print(s[r - 1] - s[l - 1])