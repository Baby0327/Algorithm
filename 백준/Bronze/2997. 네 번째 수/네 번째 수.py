n = sorted(list(map(int, input().split())))

if n[1] - n[0] == n[2] - n[1]:
    print(n[2] + (n[1] - n[0]))
elif (n[1] - n[0]) * 2 == n[2] - n[1]:
    print(n[1] + (n[1] - n[0]))
else:
    print(n[0] + (n[2] - n[1]))