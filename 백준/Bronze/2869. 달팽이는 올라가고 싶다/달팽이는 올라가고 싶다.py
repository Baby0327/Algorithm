A, B, V = map(int, input().split())

tmp = (V-A)//(A-B)

if tmp*(A-B)+A >= V:
    print(tmp+1)
else :
    print(tmp+2)