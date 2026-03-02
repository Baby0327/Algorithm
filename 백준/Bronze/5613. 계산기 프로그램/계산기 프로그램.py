s = input()

while 1:
    n = input()

    if n == "=":
        break
    else:
        s += n + input()
        s = str(int(eval(s)))

print(s)