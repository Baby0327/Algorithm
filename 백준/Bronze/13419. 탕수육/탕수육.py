for _ in range(int(input())):
    s = input()
    if len(s) % 2:
        s *= 2
    print(s[::2])
    print(s[1::2])