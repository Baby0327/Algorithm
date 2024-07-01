N = int(input())
num = []
result = []

for i in range(N):
    A, B = map(int, input().split())
    result.append(A+B)
    num.append([])
    num[i].append(A)
    num[i].append(B)

j = 1
for i in result:
        print("Case #"+str(j)+": "+str(num[j-1][0])+" + "+str(num[j-1][1])+" = "+str(i))
        j += 1