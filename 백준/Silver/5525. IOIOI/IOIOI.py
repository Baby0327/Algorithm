N = int(input())
M = int(input())
S = input()
test = list("I" + "OI"*N)

i = 0
P1 = 0
result = 0
while i <= M-1:
    if S[i:i+3] == "IOI":
        i += 2
        P1 += 1
        if P1 == N:
            result += 1
            P1 -= 1
    else:
        i += 1
        P1 = 0

print(result)