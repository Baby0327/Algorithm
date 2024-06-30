A, B = map(int, input().split())
quotient = []

i = 2
while i <= A and i <= B:
    if A%i==0 and B%i==0:
        A //= i
        B //= i
        quotient.append(i)
    else:
        i += 1

GCD = 1
for i in quotient:
    GCD *= i

print(GCD)
print(GCD*A*B)