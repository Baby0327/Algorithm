num = [int(input()) for _ in range(int(input()))]

if num[1] / num[0] == num[2] / num[1]:
    print(num[-1] * (num[1] // num[0]))
else:
    print(num[-1] + (num[1] - num[0]))