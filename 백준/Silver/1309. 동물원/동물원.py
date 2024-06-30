n = int(input())

lion = [1, 3]

while len(lion) <= n:
    lion.append((lion[-1]*2+lion[-2])%9901)

print(lion[-1])