for _ in range(int(input())):
    n, m = map(int, input().split())
    num = [list(map(int, input().split())) for i in range(m)]
    result = [0] * n

    for i in range(n):
        for j in range(m):
            result[i] += num[j][i]

    print(sorted([[i + 1, v] for i, v in enumerate(result)], key=lambda x : -x[1])[0][0])