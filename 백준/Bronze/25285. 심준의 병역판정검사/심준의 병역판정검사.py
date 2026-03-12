for _ in range(int(input())):
    h, w = map(int, input().split())
    bmi = w / (h*0.01)**2

    if h < 140.1:
        n = 6
    elif h < 146:
        n = 5
    elif h < 159:
        n = 4
    elif h < 161:
        if 16 <= bmi < 35:
            n = 3
        else:
            n = 4
    elif h < 204:
        if 20 <= bmi < 25:
            n = 1
        elif 18.5 <= bmi < 30:
            n = 2
        elif 16 <= bmi < 35:
            n = 3
        else:
            n = 4
    else:
        n = 4

    print(n)