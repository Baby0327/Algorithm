N = int(input())

num = list(map(int, input().split()))

if len(num) == 1:
    print(num[0]**2)
else:
    print(min(num)*max(num))