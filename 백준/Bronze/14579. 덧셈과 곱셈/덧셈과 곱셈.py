result = 1
a, b = map(int, input().split())

for i in range(a, b + 1):
    result = (result * ((i * (i + 1)) // 2)) % 14579

print(result)