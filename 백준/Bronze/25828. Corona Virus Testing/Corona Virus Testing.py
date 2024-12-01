g, p, t = map(int, input().split())
result1 = g * p
result2 = g + p * t
print(int(result1 != result2) + int(result1 > result2))