import sys
input = sys.stdin.readline

t, x = map(int, input().split())
a = {i for i in range(1, t + 1)}

for _ in range(int(input())):
    input()
    a = a.intersection(set(map(int, input().split())))

print("YES" if x in a else "NO")