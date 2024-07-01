N = int(input())
time = list(map(int, input().split()))

time.sort()

result = []
tmp = 0
for i in range(len(time)):
    tmp += time[i]
    result.append(tmp)

print(sum(result))