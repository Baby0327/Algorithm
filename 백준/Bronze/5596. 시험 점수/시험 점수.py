a, b, c, d = map(int, input().split())
A, B, C, D = map(int, input().split())

S = a+b+c+d
T = A+B+C+D

if S < T:
    print(T)
else:
    print(S)