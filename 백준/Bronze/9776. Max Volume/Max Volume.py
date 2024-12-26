pi = 3.14159
v = []

for _ in range(int(input())):
    info = input().split()

    if info[0] == "C":
        result = (1/3) * pi * float(info[1])**2 * float(info[2])
    elif info[0] == "L":
        result = pi * float(info[1])**2 * float(info[2])
    else:
        result = (4/3) * pi * float(info[1])**3

    v.append(result)

print(f"{max(v):.03f}")