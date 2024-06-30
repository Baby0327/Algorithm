N = int(input())
i = 0
test = 1

while True:
    tmp = test
    test += 6*i
    if (tmp <= N) and (N <= test):
        break
    i += 1

print(i+1)