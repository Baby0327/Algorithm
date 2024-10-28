result = 1000
check = 0

for i in range(int(input())):
    a, b = map(int, input().split())
    if a <= b:
        result = min(result, b)
        check = 1

print(result if check else -1)