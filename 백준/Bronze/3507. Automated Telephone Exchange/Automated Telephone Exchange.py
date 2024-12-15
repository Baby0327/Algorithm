n = int(input())
result = 0

for i in range(100):
    if n - i < 100:
        result += 1

print(result)