import sys
input = sys.stdin.readline

k = int(input())
s = 0

for _ in range(int(input())):
    t, z = input().split()
    s += int(t)

    if s >= 210:
        print(k)
        break
    elif z == "T":
        k += 1
        k -= 8 if k == 9 else 0