A, B, C = map(int, input().split())
D = int(input())

A1 = D//3600
B1 = (D-3600*A1)//60
C1 = D%60

A += A1
B += B1
C += C1

if C >= 60:
    B += C//60
    C %= 60
if B >= 60:
    A += B//60
    B %= 60
if A >= 24:
    A %= 24

print(A, B, C)