for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    result = [0] * n

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] <= a[j]:
                result[j] += 1

    print(sum(result))