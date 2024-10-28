result = 1000

for i in range(int(input())):
    a, b = map(int, input().split())
    if a < b and b < result:
        result = b

print(result if result != 1000 else -1)