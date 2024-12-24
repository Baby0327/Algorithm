x, l , r = map(int, input().split())
result = [abs(i - x) for i in range(l, r + 1)]
print(l + result.index(min(result)))