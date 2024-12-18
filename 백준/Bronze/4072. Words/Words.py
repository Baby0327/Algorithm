while 1:
    s = input().split()

    if s == ["#"]:
        break

    print(" ".join([i[::-1] for i in s]))