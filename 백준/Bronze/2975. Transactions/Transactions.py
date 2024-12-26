while 1:
    s = input().split()

    if s == ["0", "W", "0"]:
        break

    if s[1] == "D":
        result = int(s[0]) + int(s[2])
    else:
        result = int(s[0]) - int(s[2])

    print(result if result >= -200 else "Not allowed")