num = list(map(int, input().split()))

num[0] = 1 - num[0]
num[1] = 1 - num[1]
num[2] = 2 - num[2]
num[3] = 2 - num[3]
num[4] = 2 - num[4]
num[5] = 8 - num[5]

for i in num:
    print(i, end=" ")