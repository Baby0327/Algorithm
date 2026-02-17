m, d = map(int, input().split())
print(d // m + int(d % m > 0))