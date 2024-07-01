result = []
tmp = []
for i in range(3):
    tmp.append(int(input()))

result.append(min(tmp))

tmp = []
for i in range(2):
    tmp.append(int(input()))

result.append(min(tmp))

print(sum(result)-50)