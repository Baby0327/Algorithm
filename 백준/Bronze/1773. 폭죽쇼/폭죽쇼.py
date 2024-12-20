n, c = map(int, input().split())
result = [0] * c

for _ in range(n):
    num = int(input())
    result[num - 1::num] = [1] * (c // num)

print(result.count(1))