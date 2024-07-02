n = int(input())
time = list(map(int, input().split()))
result = sum(time) + 8 * (n-1)
print(result // 24, result % 24)