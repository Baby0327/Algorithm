N = int(input())

for i in range(1, N):
    print(str("*"*(2*i-1)).rjust((2*N-1)//2+i))

print("*"*(2*N-1))

x = N-1
for i in range(N-1):
    print(str("*"*(2*x-1)).rjust((2*N-1)//2+x))
    x -= 1