result = []

while True:
    N = list(map(int, input().split()))
    if N[0] == N[1] == N[2] == 0:
        break
    N.sort()
    if N[0]**2 + N[1]**2 == N[2]**2:
        result.append("right")
    else:
        result.append("wrong")

for i in result:
    print(i)