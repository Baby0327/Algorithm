num = [100]

for i in range(int(input())):
    num.append(num[-1] + int(input()))

print(max(num))