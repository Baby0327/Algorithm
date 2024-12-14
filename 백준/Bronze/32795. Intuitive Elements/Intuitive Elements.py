for _ in range(int(input())):
    a = input()
    b = list(input())
    print("YES" if len(list(filter(lambda x : x in a, b))) == len(b) else "NO")