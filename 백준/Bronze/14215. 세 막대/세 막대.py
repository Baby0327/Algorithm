num = list(map(int, input().split(" ")))
num.sort()

if num[2] < num[0] + num[1]:
    print(sum(num))
else:
    num[2] = num[0] + num[1] - 1
    print(sum(num))