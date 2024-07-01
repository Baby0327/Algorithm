n, m = map(int, input().split())

tmp = list(map(int, input().split()))
pay = [0]
for i in range(len(tmp)):
    pay.append(pay[-1]+tmp[i])

result = 0
for i in range(m, len(pay)):
    test = pay[i]-pay[i-m]
    result = max(result, test)

print(result)