while True:
    num = list(map(int, input().split()))
    cnt = 0

    if num[0] == num[1] == num[2] == num[3] == 0:
        break

    while num.count(num[0]) != 4:
        temp = []
        for i in range(-4, 0):
            temp.append(abs(num[i] - num[i + 1]))
        num = temp
        cnt += 1

    print(cnt)