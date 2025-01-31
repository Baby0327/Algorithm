a, b = map(int, input().split())
d = int(input())
print((a * b // 12 + int(a * b % 12 > 0)) * d)