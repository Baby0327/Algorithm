import sys
input = sys.stdin.readline

for n in range(int(input())):
    g = sum(i * j for i, j in zip(list(map(int, input().split())), [1, 2, 3, 3, 4, 10]))
    s = sum(i * j for i, j in zip(list(map(int, input().split())), [1, 2, 2, 2, 3, 5, 10]))
    a = "No victor on this battle field"

    if g > s:
        a = "Good triumphs over Evil"
    elif g < s:
        a = "Evil eradicates all trace of Good"

    print(f"Battle {n + 1}: {a}")