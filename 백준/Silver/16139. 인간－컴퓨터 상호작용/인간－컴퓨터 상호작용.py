import sys

S = list(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline())

result = [[0 for i in range(26)] for j in range(len(S)+1)]

for i in range(1, len(S)+1):
    tmp = ord(S[i - 1]) - 97
    for j in range(26):
        if tmp == j:
            result[i][j] = result[i-1][j] + 1
            continue
        result[i][j] = result[i-1][j]

for i in range(q):
    x, start, end = sys.stdin.readline().rstrip().split()
    x = ord(x) - 97
    start = int(start)
    end = int(end)

    sys.stdout.write(str(result[end+1][x] - result[start][x])+'\n')