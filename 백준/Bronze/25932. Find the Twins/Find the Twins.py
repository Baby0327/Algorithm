import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = list(map(int, input().split()))
    print(*num)

    if 18 in num:
        print("both" if 17 in num else "mack")
    else:
        print("zack" if 17 in num else "none")

    print()