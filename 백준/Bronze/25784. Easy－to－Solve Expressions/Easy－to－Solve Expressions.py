n = sorted(list(map(int, input().split())))

if n[0] + n[1] == n[2]:
    print(1)
elif n[0] * n[1] == n[2]:
    print(2)
else:
    print(3)