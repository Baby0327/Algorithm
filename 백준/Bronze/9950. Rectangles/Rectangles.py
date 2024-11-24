while 1:
    n = list(map(int, input().split()))

    if sum(n) == 0:
        break

    i = n.index(0)

    if i < 2:
        n[i] = n[2] // n[1 - i]
    else:
        n[i] = n[0] * n[1]
        
    print(*n)