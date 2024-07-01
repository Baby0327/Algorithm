N = int(input())
result = []

for i in range(N):
    A, B = map(int, input().split())
    result.append(A+B)

j = 1
for i in result:

    print("Case #"+str(j)+": "+str(i))
    j += 1