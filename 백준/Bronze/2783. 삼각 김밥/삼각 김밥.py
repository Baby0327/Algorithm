x, y = map(int, input().split())
price = [x/y]

for _ in range(int(input())):
    x, y = map(int, input().split())
    price.append(x/y)

print(min(price) * 1000)