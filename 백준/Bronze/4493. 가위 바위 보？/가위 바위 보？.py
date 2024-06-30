list = ["P", "S", "R"]

t = int(input())
for i in range(t):
    n = int(input())
    person1, person2 = 0, 0
    for _ in range(n):
        a, b = input().split()
        if a == list[list.index(b) - 1]:
            person2 += 1
        elif b == list[list.index(a) - 1]:
            person1 += 1
    if person1 > person2:
        print("Player 1")
    elif person1 < person2:
        print("Player 2")
    else:
        print("TIE")