while 1:
    n = int(input())

    if n == 0:
        break

    k = list(map(int, input().split()))
    total = 0

    for i in k:
        if total + i <= 300:
            total += i

    print(total)