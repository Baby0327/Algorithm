H = []
for i in range(7):
    tmp = int(input())
    if tmp%2 == 1:
        H.append(tmp)

H.sort()

if len(H) == 0:
    print(-1)
else:
    print(sum(H))
    print(H[0])