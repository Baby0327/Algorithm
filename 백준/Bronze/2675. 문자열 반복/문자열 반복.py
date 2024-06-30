T = int(input())

result = []
for i in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)
    S_list = list(S)
    tmp = ""
    x = 0
    for j in range(len(S)):
        tmp += str(S_list[x]*R)
        x += 1
    result.append(tmp)

for i in result:
    print(i)