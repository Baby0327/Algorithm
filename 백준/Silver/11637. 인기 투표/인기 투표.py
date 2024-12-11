import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num = [int(input()) for _ in range(n)]
    maxi = max(num)

    if num.count(maxi) > 1:
        print("no winner")
    elif maxi > sum(num) / 2:
        print(f"majority winner {num.index(maxi) + 1}")
    else:
        print(f"minority winner {num.index(maxi) + 1}")