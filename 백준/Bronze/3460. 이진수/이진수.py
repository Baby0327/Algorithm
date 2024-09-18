"""
이진수
"""

t = int(input())

for i in range(t):
    n = bin(int(input()))[2:][::-1]

    for j in range(len(n)):
        if n[j] == "1":
            print(j, end=" ")