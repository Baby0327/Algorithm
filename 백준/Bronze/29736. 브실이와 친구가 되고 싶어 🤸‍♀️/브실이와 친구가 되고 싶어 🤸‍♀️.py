a, b = map(int, input().split())
k, x = map(int, input().split())
p = min(b, k + x) - max(a, k - x) + 1
print(p if p > 0 else "IMPOSSIBLE")