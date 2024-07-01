N = int(input())
num = list(map(int, input().split()))

number = list(set(num))
number.sort()

dic = {}
for i in range(len(number)):
    dic[number[i]] = i

for i in num:
    print(dic[i], end=" ")