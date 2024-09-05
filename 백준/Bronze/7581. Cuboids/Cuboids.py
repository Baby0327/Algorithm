"""
Cuboids
"""

while True:
    n = list(map(int, input().split()))

    if n.count(0) == 4:
        break
    elif n.index(0) in [0, 1, 2]:
        temp = n[-1]

        for i in range(3):
            if n[i] != 0:
                temp //= n[i]

        n[n.index(0)] = temp

        print(*n)
    else:
        temp = 1

        for i in range(3):
            temp *= n[i]

        n[-1] = temp

        print(*n)