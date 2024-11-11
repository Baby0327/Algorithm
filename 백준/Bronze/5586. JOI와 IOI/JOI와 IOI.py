s = input()
j = 0
i = 0

for k in range(len(s) - 2):
    w = s[k:k+3]
    if w == "JOI":
        j += 1
    elif w == "IOI":
        i += 1

print(j, i, sep="\n")