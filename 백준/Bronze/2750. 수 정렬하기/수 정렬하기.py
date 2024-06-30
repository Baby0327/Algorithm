N = int(input())
num = []

for i in range(N):
    tmp = int(input())
    num.append(tmp)

num.sort()

for i in num:
    print(i)