n, m = map(int, input().split())
result = 0

for i in range(n):
    x = list(map(int, input().split()))
    result += int(x.count(0) == 0)

print(result)