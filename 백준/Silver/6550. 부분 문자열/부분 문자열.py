while 1:
    try:
        s, t = input().split()
        n = 0

        for i in t:
            if n < len(s) and s[n] == i:
                n += 1

        if n == len(s):
            print("Yes")
        else:
            print("No")

    except:
        break