now = list(map(int, input().split(":")))
na = list(map(int, input().split(":")))

if now >= na:
    na[0] += 24

now = sum(60 ** i * now[2 - i] for i in range(3))
na = sum(60 ** i * na[2 - i] for i in range(3))
s = na - now

print(f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}")