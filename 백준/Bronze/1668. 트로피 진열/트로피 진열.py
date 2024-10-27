num = []
l = r = 0

for i in range(int(input())):
    num.append(int(input()))

temp = 0
for i in range(len(num)):
    if temp < num[i]:
        l += 1
        temp = num[i]

num = num[::-1]
temp = 0

for i in range(len(num)):
    if temp < num[i]:
        r += 1
        temp = num[i]

print(l)
print(r)