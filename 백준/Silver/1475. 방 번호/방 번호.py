N = list(map(int, input()))

num = [0 for i in range(10)]

for i in N:
    num[i] += 1

tmp = num[6] + num[9]
if tmp%2==0:
    tmp = tmp//2
else:
    tmp = tmp//2+1

del num[6]
del num[8]

num.append(tmp)

print(max(num))