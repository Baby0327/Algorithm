n, m = map(int, input().split())
num = list(map(int, input().split()))
result = 1

for i in num:
    result *= i % m

print(result % m)