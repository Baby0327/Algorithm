while 1:
    s = input()

    if s == "#":
        break

    total = 0

    for i in range(len(s)):
        if s[i] != " ":
            total += (i + 1) * (ord(s[i])-64)

    print(total)