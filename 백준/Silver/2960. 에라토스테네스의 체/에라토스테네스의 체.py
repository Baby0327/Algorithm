n, k = map(int, input().split())

num = [True] * (n+1)
num[0] = False
num[1] = False
test = [0]

for i in range(2, n+1):
    if num[i] == True:
        test.append(i)
        for j in range(i+i, n+1, +i):
            if num[j] == True:
                test.append(j)
                num[j] = False

print(test[k])