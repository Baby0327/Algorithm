num = []

for i in range(9):
    n = int(input())
    num.append(n)

result = 0
count = 0
for i in range(9):
    if result < num[count]:
        result = num[count]
        index = count+1
    count += 1

print(result)
print(index)