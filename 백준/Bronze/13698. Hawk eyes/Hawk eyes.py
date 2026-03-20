m = input()
b = [0, 1, 0, 0, 2]

for i in m:
    if i == "A":
        b[1], b[2] = b[2], b[1]
    elif i == "B":
        b[1], b[3] = b[3], b[1]
    elif i == "C":
        b[1], b[4] = b[4], b[1]
    elif i == "D":
        b[2], b[3] = b[3], b[2]
    elif i == "E":
        b[2], b[4] = b[4], b[2]
    else:
        b[3], b[4] = b[4], b[3]

print(b.index(1))
print(b.index(2))