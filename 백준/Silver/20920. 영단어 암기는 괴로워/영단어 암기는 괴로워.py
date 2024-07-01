import sys

n, m = map(int, sys.stdin.readline().split())
word = {}
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    if len(tmp) >= m:
        if tmp in word:
            word[tmp] += 1
        else:
            word[tmp] = 1

word = sorted(word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(word)):
    sys.stdout.write(word[i][0]+'\n')