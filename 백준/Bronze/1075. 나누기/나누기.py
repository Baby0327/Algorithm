n = (int(input()) // 100) * 100
f = int(input())

while n % f:
    n += 1

print(f"{n % 100:02d}")