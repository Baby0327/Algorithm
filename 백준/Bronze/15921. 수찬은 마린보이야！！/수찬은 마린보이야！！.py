n = int(input())

if n > 0:
    p = list(map(int, input().split()))
    s = set(p)
    e = sum(p.count(i) / n * i for i in s)
    print(f"{sum(p) / n / e:.2f}")
else:
    print("divide by zero")
