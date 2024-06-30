t = int(input())

for i in range(t):
    n = int(input())
    tmp = str(n**2)
    test = tmp[len(tmp)-len(str(n)):]
    if str(n) == test:
        print("YES")
    else:
        print("NO")