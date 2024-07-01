a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = 0
while a < b:
    if a < 0:
        count += c
    elif a == 0:
        count += e
        count += d
    else:
        count += e
    a += 1

print(count)