for i in range(int(input())):
    x = int(input())
    total = 0

    for j in range(x):
        name, count, cost = input().split()
        total += int(count) * float(cost)

    print(f"${total:.2f}")