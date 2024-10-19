"""
Triangles
"""

for i in range(int(input())):
    n, x = input().split()

    for j in range(int(n)):
        print(chr(ord(x) + j if ord(x) + j < 91 else ord(x) + j - 26) * (j + 1))

    print()