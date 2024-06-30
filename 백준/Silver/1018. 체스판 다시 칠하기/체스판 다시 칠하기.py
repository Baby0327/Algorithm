import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

result = 0
for i in range(N-7):
    for j in range(M-7):
        test1 = 0
        test2 = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i+x][j+y] == 'W':
                        test1 += 1
                    else:
                        test2 += 1
                else:
                    if board[i+x][j+y] == 'B':
                        test1 += 1
                    else:
                        test2 += 1

        test = max(test1, test2)
        result = max(test,result)

print(64-result)