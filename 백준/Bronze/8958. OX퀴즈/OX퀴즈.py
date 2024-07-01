N = int(input())

result = []

for i in range(N):
    test = input().split('X')
    tmp = 0
    for j in range(len(test)):
        tmp += (len(test[j])*(len(test[j])+1))//2
    result.append(tmp)

for i in result:
    print(i)
