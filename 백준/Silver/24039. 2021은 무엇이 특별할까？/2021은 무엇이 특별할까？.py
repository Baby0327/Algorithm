num = [True]*201
num[0] = False
num[1] = False

for i in range(201):
    if num[i]:
        for j in range(i+i, 201, +i):
            num[j] = False

prime = []
for i in range(len(num)):
    if num[i]:
        prime.append(i)


n = int(input())
i = 0
while True:
    result = prime[i] * prime[i+1]
    if result > n:
        print(result)
        break
    else:
        i += 1