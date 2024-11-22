w, n, p = map(int, input().split())
h = list(map(int, input().split()))
print(sum(1 for i in range(p) if w <= h[i] <= n))