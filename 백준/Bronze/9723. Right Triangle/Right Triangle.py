for i in range(int(input())):
    l = sorted(list(map(int, input().split())))
    result = "YES" if l[0]**2 + l[1]**2 == l[2]**2 else "NO"
    print(f"Case #{i + 1}: {result}")