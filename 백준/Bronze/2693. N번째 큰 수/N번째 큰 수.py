T = int(input())

result = []
for i in range(T):
    tmp = list(map(int, input().split()))
    tmp.sort()
    result.append(tmp[len(tmp)-3])

for i in result:
    print(i)