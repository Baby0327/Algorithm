result = []

while True:
    A, B, C = map(int, input().split())
    if A==0 and B==0 and C==0:
        break
    tmp = []
    tmp.append(A)
    tmp.append(B)
    tmp.append(C)
    tmp.sort()
    if tmp[0] + tmp[1] <= tmp[2]:
        result.append("Invalid")
    else:
        if tmp[0] == tmp[1] or tmp[1] == tmp[2]:
            if tmp[0] == tmp[2]:
                result.append("Equilateral")
            else:
                result.append("Isosceles")
        else:
            result.append("Scalene")

for i in result:
    print(i)