b, c, d = map(int, input().split())
burger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
drink = sorted(list(map(int, input().split())), reverse=True)
total = sum(burger) + sum(side) + sum(drink)

print(total)

for i in range(min(b, c, d)):
    total -= (burger[i] + side[i] + drink[i]) * 0.1

print(int(total))