L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

result = []
if A%C == 0:
    result.append(A//C)
else:
    result.append(A//C+1)
if B%D == 0:
    result.append(B//D)
else:
    result.append(B//D+1)

print(L-max(result))