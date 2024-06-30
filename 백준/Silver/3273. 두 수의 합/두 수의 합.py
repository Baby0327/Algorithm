n = int(input())
num = list(map(int, input().split()))
num.sort()
x = int(input())

start = 0
end = n-1
result = 0
while end - start > 0:
    sum = num[start] + num[end]
    if sum > x:
        end -= 1
    elif sum == x:
        result += 1
        start += 1
        end -= 1
    else:
        start += 1

print(result)