while 1:
    try:
        s = input()
        num = [0] * 4

        for i in s:
            if i.islower():
                num[0] += 1
            elif i.isupper():
                num[1] += 1
            elif i.isdigit():
                num[2] += 1
            else:
                num[3] += 1

        print(*num)
    except EOFError:
        break