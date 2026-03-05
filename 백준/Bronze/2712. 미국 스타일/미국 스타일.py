for _ in range(int(input())):
    n, s = input().split()
    n = float(n)

    if s == "kg":
        print(f"{n * 2.2046:.4f} lb")
    elif s == "lb":
        print(f"{n * 0.4536:.4f} kg")
    elif s == "l":
        print(f"{n * 0.2642:.4f} g")
    else:
        print(f"{n * 3.7854:.4f} l")