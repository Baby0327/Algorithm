num = list(map(int, input().split()))
test = sorted(num)

while num != test:
    for i in range(4):
        if num[i] > num[i + 1]:
            tmp = num[i]
            num[i] = num[i + 1]
            num[i + 1] = tmp
            for j in range(4):
                print(num[j], end=" ")
            print(num[4])