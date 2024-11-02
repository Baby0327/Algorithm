while True:
    n = list(map(int, input().split()))

    if n == [0]:
        break

    result = [n[1]]

    for i in range(2, n[0] + 1):
        if result and result[-1] != n[i]:
            result.append(n[i])

    result.append("$")
    print(*result)