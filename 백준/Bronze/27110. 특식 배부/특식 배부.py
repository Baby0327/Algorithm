n = int(input())
people = list(map(int, input().split()))
result = 0

for i in people:
    if i >= n:
        result += n
    else:
        result += i

print(result)