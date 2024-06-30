import sys

while True:
    tmp = list(sys.stdin.readline().rstrip())
    if tmp == ["."]:
        break
    test = []
    for i in tmp:
        if i == "(" or i == ")" or i == "[" or i == "]":
            test.append(i)
    result = []
    final = True
    for i in test:
        if len(result) != 0:
            if i == ")" and result[-1] == "(":
                result.pop()
            elif i == "]" and result[-1] == "[":
                result.pop()
            else:
                result.append(i)
        else:
            result.append(i)

    if len(result) != 0:
        final = False

    if final:
        print("yes")
    else:
        print("no")