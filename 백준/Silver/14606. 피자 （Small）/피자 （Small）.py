N = [int(input())]

result = 0
while N:
    a = N[0]//2
    b = N[0]-a
    result += a*b
    if a > 1:
        N.append(a)
    if b > 1:
        N.append(b)
    N.remove(N[0])

print(result)