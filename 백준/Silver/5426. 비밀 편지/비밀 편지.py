T = int(input())
result = []

for i in range(T):
    line = list(input())
    size = int(len(line) ** (1 / 2))
    test = [[0 for a in range(size)] for b in range(size)]
    count = 0
    X = 0
    for x in range(size):
        for y in range(size):
            test[x][y] = line[count]
            if count == len(line)-1:
                X = 'stop'
                break
            else:
                count += 1
        if X == 'stop':
            break

    tmp = ""
    for y in range(size-1, -1, -1):
        for x in range(size):
            tmp += test[x][y]

    result.append(tmp)

for i in result:
    print(i)
