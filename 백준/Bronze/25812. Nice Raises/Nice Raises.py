n, r = map(int, input().split())
result = [0, 0]

for i in range(n):
    num = int(input())
    if num > r:
        result[1] += 1
    elif num < r:
        result[0] += 1

if result[0] == result[1]:
    print(0)
elif result[0] > result[1]:
    print(1)
else:
    print(2)