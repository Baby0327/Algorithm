for i in range(int(input())):
    g = int(input())
    c = list(map(int, input().split()))
    for j in c:
        if c.count(j) % 2:
            print(f"Case #{i + 1}: {j}")
            break