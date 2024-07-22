"""
Gnome Sequencing
"""

n = int(input())

print("Gnomes:")

for i in range(n):
    line = list(map(int, input().split()))
    asc = sorted(line)
    desc = sorted(line, reverse=True)

    if line == asc or line == desc:
        print("Ordered")
    else:
        print("Unordered")