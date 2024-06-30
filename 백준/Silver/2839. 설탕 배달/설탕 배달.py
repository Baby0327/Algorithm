N = int(input())
N_5 = N//5
N_3 = N%5//3

if N >= 10:
    if (N%5) % 3 == 0:
        print(N_5 + N_3)
    elif (N%5) % 3 == 1:
        print(N_5 + N_3 + 1)
    elif (N%5) % 3 == 2:
        print(N_5 + N_3 + 2)
    else:
        print(-1)
else:
    if N%3 == 0:
        print(N//3)
    elif N%5 == 0:
        print(N//5)
    elif N%5%3 == 0:
        print(N_5 + N_3)
    else :
        print(-1)