n, x = map(int, input().split())
people = list(map(int, input().split()))
i = 0

while 1:
    if people[i % n] < x:
        print(i % n + 1)
        break
    else:
        i += 1
        x += 1