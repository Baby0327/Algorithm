n, k, p = map(int, input().split())
c = list(map(int, input().split()))
print(sum(1 for i in range(0, n*k, k) if c[i:i+k].count(0) < p))