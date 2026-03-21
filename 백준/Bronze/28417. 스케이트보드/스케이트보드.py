n = 0

for _ in range(int(input())):
    a, b, c, d, e, f, g = map(int, input().split())
    n = max(n, (max(a, b) + sum(sorted([c, d, e, f, g])[-2:])))

print(n)