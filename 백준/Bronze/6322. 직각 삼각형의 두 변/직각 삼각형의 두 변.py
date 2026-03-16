i = 1

while 1:
    n = list(map(int, input().split()))

    if n[0] == 0:
        break

    s = n.index(-1)
    print(f"Triangle #{i}")

    if s > 1:
        print(f"{chr(s + 97)} = {(n[0]**2 + n[1]**2)**0.5:.3f}")
    else:
        if n[0] >= n[2] or n[1] >= n[2]:
            print("Impossible.")
        else:
            print(f"{chr(s + 97)} = {(n[2]**2 - (n[0]**2 if n[0] > 0 else n[1]**2))**0.5:.3f}")

    print()
    i += 1