n, k = map(int, input().split())

for i in list(map(int, input().split())):
    n -= i // 2
    if i % 2:
        n -= 1

print("YES" if n <= 0 else "NO")