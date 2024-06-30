N = int(input())
r = list(map(int, input().split()))

for i in range(1, len(r)):
    if r[0] % r[i] == 0:
        print(str(r[0] // r[i]) + "/" + "1")
    else:
        a = max(r[0], r[i])
        b = min(r[0], r[i])
        while True:
            tmp = a%b
            if tmp == 0:
                break
            a = b
            b = tmp
        print(str(r[0]//b)+"/"+str(r[i]//b))