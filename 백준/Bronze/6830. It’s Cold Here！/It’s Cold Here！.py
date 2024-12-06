result = []

while 1:
    name, n = input().split()
    result.append([name, int(n)])

    if name == "Waterloo":
        break

print(sorted(result, key=lambda x : x[1])[0][0])