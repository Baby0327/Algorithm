n = int(input())
num = [1, 1, 1]

while len(num) <= n:
    num.append(num[-1] + num[-3])

print(num[n-1])