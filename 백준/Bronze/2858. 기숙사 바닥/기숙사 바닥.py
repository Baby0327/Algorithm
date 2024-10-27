l, w = map(int, input().split())

for i in range(3, l + w + 1):
    if (l + w) % i == 0:
        j = (l + w) // i
        if (i - 2) * 2 + j * 2 == l:
            print(j, i)
            break