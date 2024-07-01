n = int(input())
num = [0, 1]

while len(num) <= n:
    num.append(num[-2] + num[-1])

print(num[n])