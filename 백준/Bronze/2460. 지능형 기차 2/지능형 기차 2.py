result = [0]

for i in range(10):
    a, b = map(int, input().split())
    result.append(result[-1] - a + b)

print(max(result))