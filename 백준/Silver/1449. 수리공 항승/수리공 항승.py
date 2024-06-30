N, L = map(int, input().split())

point = list(map(int, input().split()))
point.sort()

start = 0
count = 0
result = False

while True:
    for i in range(start+1, len(point)+1):
        if i == len(point):
            count += 1
            result = True
            break
        elif point[i] - point[start] > L-1:
            start = i
            count += 1
            break

    if result:
        break

print(count)