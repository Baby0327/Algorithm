C = int(input())
result = []

for i in range(C):
    num = list(map(int, input().split()))
    tmp = 0
    for j in range(1, num[0]+1):
        tmp += num[j]
    tmp = tmp//num[0]
    count = 0
    for j in range(1, num[0]+1):
        if num[j] > tmp:
            count += 1
    result.append(count/num[0]*100)

for i in result:
    print(format(i, ".3f")+"%")