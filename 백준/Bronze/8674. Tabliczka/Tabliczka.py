a, b = list(map(int, input().split()))
print(0 if a % 2 == 0 or b % 2 == 0 else min(a, b))