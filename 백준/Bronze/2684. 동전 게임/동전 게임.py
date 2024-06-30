P = int(input())

result = []
for i in range(P):
    coin = list(input())
    tmp = [0 for i in range(8)]
    for j in range(38):
        if coin[j]+coin[j+1]+coin[j+2] == 'TTT':
            tmp[0] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'TTH':
            tmp[1] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'THT':
            tmp[2] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'THH':
            tmp[3] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'HTT':
            tmp[4] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'HTH':
            tmp[5] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'HHT':
            tmp[6] += 1
        elif coin[j]+coin[j+1]+coin[j+2] == 'HHH':
            tmp[7] += 1
    result.append(tmp)

for i in result:
    for j in range(7):
        print(i[j], end=" ")
    print(i[7])