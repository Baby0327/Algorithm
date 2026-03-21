d1, d2, d3 = map(int, input().split())
n = (d1 + d2 - d3) / 2

if n > 0 and d1 - n > 0 and d2 - n > 0:
    print(1)
    print(f"{n:.1f} {d1 - n:.1f} {d2 - n:.1f}")
else:
    print(-1)