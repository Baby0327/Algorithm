num = []

for i in range(5):
    tmp = int(input())
    num.append(tmp)

num.sort()

total = 0
for i in num:
    total += i

print(total//5)
print(num[2])
