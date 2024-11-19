for i in range(int(input())):
    n = int(input())
    s1 = sum(i for i in range(1, n + 1))
    s2 = sum(i for i in range(1, n*2 + 1, 2))
    s3 = sum(i for i in range(2, n*2 + 1, 2))
    print(s1, s2, s3)