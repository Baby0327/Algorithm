import sys
input = sys.stdin.readline

y = input().rstrip()
maxi = 0
win = "ZZZZZZZZZZZZZZZZZZZZ"
first = ""

for i in range(int(input())):
    name = input().rstrip()
    first = min(first, name)
    n = y + name
    l = n.count("L")
    o = n.count("O")
    v = n.count("V")
    e = n.count("E")
    mod = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
    if mod > maxi:
        maxi = mod
        win = name
    elif mod == maxi:
        win = min(win, name)

print(win if win else first)