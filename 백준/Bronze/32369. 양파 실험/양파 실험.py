n, a, b = map(int, input().split())
o1, o2 = 1, 1

for _ in range(n):
    o1 += a
    o2 += b

    if o1 < o2:
        o1, o2 = o2, o1
    elif o1 == o2:
        o2 -= 1

print(o1, o2)