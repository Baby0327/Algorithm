result = []

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    elif A % B == 0:
        result.append("multiple")
    elif B % A == 0:
        result.append("factor")
    else:
        result.append("neither")

for i in result:
    print(i)