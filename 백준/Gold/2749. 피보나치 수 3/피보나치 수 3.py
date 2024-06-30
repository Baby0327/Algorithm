mod = 1000000
period = int(mod * 1.5)
num = [0, 1]

for i in range(period):
    num.append((num[-1] + num[-2])%mod)

n = int(input())
print(num[n%period])