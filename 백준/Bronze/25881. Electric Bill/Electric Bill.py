a, b = map(int, input().split())

for _ in range(int(input())):
    n = int(input())
    print(n, a * 1000 + b * (n - 1000) if n >= 1000 else a * n)