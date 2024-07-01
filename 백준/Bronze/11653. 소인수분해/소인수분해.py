N = int(input())
num = []

i = 2
while True:
    if N % i == 0:
        num.append(i)
        N = N//i
    else:
        i += 1
    if N == 1:
        break

for i in num:
    print(i)