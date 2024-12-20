n = int(input())
b = list(map(int, input().split()))
result = [b[0]]

for i in range(1, n):
    result.append(b[i] * (i + 1) - sum(result))

print(*result)