for _ in range(int(input())):
    n = int(input())
    room = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if room[j]:
                room[j] = 0
            else:
                room[j] = 1

    print(room.count(1))