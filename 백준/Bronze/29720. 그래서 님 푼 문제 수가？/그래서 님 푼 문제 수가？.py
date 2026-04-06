n, m, k = map(int, input().split())

if n < m:
    print(0, n - 1)
else:
    print(max(n - (m * k), 0), n - (m * (k - 1) + 1))