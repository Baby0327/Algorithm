while 1:
    n = int(input())

    if n == 0:
        break

    num = list(map(int, input().split()))
    print(max(sum(num[i:i + 3]) for i in range(n - 2)))