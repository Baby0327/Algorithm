for _ in range(int(input())):
    n = int(input())
    pairs = []

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i < j and i + j == n:
                pairs.append(str(i) + " " + str(j))

    print(f"Pairs for {n}: {', '.join(pairs)}")