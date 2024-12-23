while 1:
    s = [i.lower()[0] for i in input().split()]

    if s == ["*"]:
        break

    print("Y" if s.count(s[0]) == len(s) else "N")