a, b = map(int, input().split())

for i in range(-10000, 10001):
    if i * i + 2 * a * i + b == 0:
        print(i, end=' ')