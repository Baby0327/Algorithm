n = int(input())
start = list(map(int, input().split()))
grow = list(map(int, input().split()))
consideration = [[] for i in range(len(start))]

for i in range(len(start)):
    consideration[i].append(start[i])
    consideration[i].append(grow[i])

consideration.sort(key=lambda x: x[1])

result = 0
for i in range(len(consideration)):
    result += (consideration[i][0] + consideration[i][1]*i)

print(result)