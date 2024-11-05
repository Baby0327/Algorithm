a, b = map(int, input().split())
result = [i for i in range(min(a, b) + 1, max(a, b))]
print(len(result))
print(*result)