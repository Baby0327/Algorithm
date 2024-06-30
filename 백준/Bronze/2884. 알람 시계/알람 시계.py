H, M = map(int, input().split())

if H == 0 and M <45:
    print(23, ((M+60)-45)%60)
elif M<45 :
    print(H-1, ((M+60)-45)%60)
else :
    print(H, M-45)