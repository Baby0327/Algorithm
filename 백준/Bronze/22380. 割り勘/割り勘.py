while 1:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    num = m // n
    a = list(map(int, input().split()))
    result = 0

    for i in a:
        if i >= num:
            result += num
        else:
            result += i

    print(result)