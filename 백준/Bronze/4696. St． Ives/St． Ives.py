while 1:
    n = float(input())

    if n == 0:
        break
    elif n == 1:
        print(f"{n * 5:.2f}")
    else:
        print(f"{(n**5 - 1) / (n - 1):.2f}")