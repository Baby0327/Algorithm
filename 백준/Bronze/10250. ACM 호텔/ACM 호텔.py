N = int(input())

result = []

for i in range(N):
    H, W, N = map(int, input().split())
    room_H = N%H
    room_W = N//H + 1
    if room_H == 0:
        room_H = H
        room_W -= 1
    result.append(room_H*100 + room_W)

for i in result:
    print(i)