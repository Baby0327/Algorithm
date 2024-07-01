num = [0, 1]
n = int(input())

while len(num) <= n:
    num.append((num[-1] + num[-2])%1000000007)

print(num[n])