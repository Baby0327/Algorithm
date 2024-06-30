n = int(input())
num = [0, 1]

while len(num) <= n:
    num.append(num[-1] + num[-2])

print(num[n])