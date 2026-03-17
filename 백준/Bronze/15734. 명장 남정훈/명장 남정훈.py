l, r, a = map(int, input().split())

if l == r:
    print((l + a // 2) * 2)
else:
    for i in range(a):
        if l < r:
            l += 1
        else:
            r += 1
    print(min(l, r) * 2)