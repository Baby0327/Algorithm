num = []

for i in range(28):
    n = int(input())
    num.append(n)

result = []
x = 1
for i in range(30):
    if x not in num:
        result.append(x)
    x += 1

for i in result:
    print(i)