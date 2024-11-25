for i in range(int(input())):
    n = list(map(int, list(input())))
    result = sum(n) + int("".join(map(str, n[-3:]))) * 10
    print(result + 1000 if result < 1000 else str(result)[-4:])