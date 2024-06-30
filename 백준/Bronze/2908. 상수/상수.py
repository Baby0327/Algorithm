A, B = input().split()

A = list(map(int, str(A)))
tmp = A[0]
A[0] = A[2]
A[2] = tmp

B = list(map(int, str(B)))
tmp = B[0]
B[0] = B[2]
B[2] = tmp

a = 100*A[0]+10*A[1]+A[2]
b = 100*B[0]+10*B[1]+B[2]

if a > b:
    print(a)
else:
    print(b)