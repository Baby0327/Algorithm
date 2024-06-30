n = int(input())
num = list(map(int, input().split()))
sorted_num = sorted(num)
for i in range(n):
    tmp = sorted_num.index(num[i])
    print(tmp, end=" ")
    sorted_num[tmp] = False
