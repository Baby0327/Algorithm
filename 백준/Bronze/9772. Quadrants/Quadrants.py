while 1:
    x, y = map(float, input().split())

    if x == 0 or y == 0:
        print("AXIS")
    elif x > 0:
        print("Q1" if y > 0 else "Q4")
    else:
        print("Q2" if y > 0 else "Q3")

    if x == y == 0:
        break