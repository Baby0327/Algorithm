import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
input()
case = set()

for i in w:
    now = set([i])

    for j in case:
        now.add(i + j)
        now.add(abs(i - j))

    case |= now

print(*["Y" if i in case else "N" for i in list(map(int, input().split()))])