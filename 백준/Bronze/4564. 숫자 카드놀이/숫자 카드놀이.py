while True:
    s = input()

    if s == "0":
        break

    result = [s]

    while len(s) > 1:
        temp = 1
        for i in s:
            temp *= int(i)
        s = str(temp)
        result.append(s)

    print(*result)