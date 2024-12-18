for _ in range(int(input())):
    s = input().split()
    result = float(s[0])

    for i in s[1:]:
        if i == "@":
            result *= 3
        elif i == "%":
            result += 5
        elif i == "#":
            result -= 7

    print(f"{result:.2f}")