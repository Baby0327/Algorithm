result = []

while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        break
    result.append(A+B)

for i in result:
    print(i)