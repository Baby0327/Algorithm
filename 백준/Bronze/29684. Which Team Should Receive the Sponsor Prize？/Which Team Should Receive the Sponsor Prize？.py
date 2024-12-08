while 1:
    n = int(input())

    if n == 0:
        break

    a = list(map(int, input().split()))
    result = sorted((abs(2023 - num), i) for i, num in enumerate(a))
    print(result[0][1] + 1)