N = int(input())

if N != 1:
    print(" "*(N-1)+"*")

for i in range(2, N):
    print(" "*(N-i)+"*"+" "*(2*i-3)+"*")

print("*"*(2*N-1))