first = [1, 0, 1]
second = [0, 1, 1]

d, k = map(int, input().split())
for i in range(d-3):
    first.append(first[-2] + first[-1])
    second.append(second[-2] + second[-1])

count1 = first[-1]
count2 = second[-1]

num1 = 1
while True:
    test = (k - num1 * count1)
    if test % count2 == 0:
        print(num1)
        print(test//count2)
        break
    else:
        num1 += 1