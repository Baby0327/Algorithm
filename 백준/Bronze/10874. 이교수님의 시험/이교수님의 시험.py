answer = [divmod(i - 1, 5)[1] + 1 for i in range(1, 11)]

for i in range(int(input())):
    if list(map(int, input().split())) == answer:
        print(i + 1)