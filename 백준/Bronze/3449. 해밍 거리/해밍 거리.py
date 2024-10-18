"""
해밍 거리
"""

t = int(input())

for i in range(t):
    a = input()
    b = input()
    count = 0

    for j in range(len(a)):
        if a[j] != b[j]:
            count += 1

    print(f"Hamming distance is {count}.")