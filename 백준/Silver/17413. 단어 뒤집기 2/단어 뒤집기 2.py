s = list(input())

i = 0
test = []
while i < len(s):
    if s[i] == '<':
        while True:
            test.append(s[i])
            i += 1
            if s[i] == '>':
                test.append(s[i])
                print("".join(test), end="")
                test = []
                i += 1
                break
    else:
        test.append(s[i])
        i += 1
        if (i < len(s) and s[i] == '<') or i == len(s) or s[i] == " ":
            tmp = "".join(reversed(test))
            print(tmp, end="")
            test = []
            if i < len(s) and s[i] == ' ':
                print(" ", end="")
                i += 1