tmp = list(input().split("."))

result = ""
test = True
for i in range(len(tmp)):
    if len(tmp[i]) == 0:
        result += "."
    elif len(tmp[i]) % 2 == 1:
        test = False
        break
    else:
        result += "AAAA"*(len(tmp[i])//4)
        result += "BB"*(len(tmp[i])%4//2)
        result += "."

if test:
    print(result[:len(result)-1])
else:
    print(-1)