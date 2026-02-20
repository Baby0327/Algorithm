n = input()

if "0" in n:
    i = n.index("0")
    if i == len(n) - 1:
        print(int(n[:i-1]) + int(n[i-1:]))
    else:
        print(int(n[:i+1]) + int(n[i+1:]))
else:
    print(int(n[0]) + int(n[1]))