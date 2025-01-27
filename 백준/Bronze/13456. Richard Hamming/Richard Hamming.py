for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    u = list(map(int, input().split()))

    print(sum(1 for i in range(n) if v[i] != u[i]))