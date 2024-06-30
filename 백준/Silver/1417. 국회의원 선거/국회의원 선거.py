N = int(input())

DS = int(input())

num = []
for i in range(N-1):
    num.append(int(input()))

num.sort(reverse=True)

result = 0
while True:
    if len(num) == 0:
        break
    elif DS > num[0]:
        break
    else:
        num[0] -= 1
        DS += 1
        result += 1
        num.sort(reverse=True)

print(result)