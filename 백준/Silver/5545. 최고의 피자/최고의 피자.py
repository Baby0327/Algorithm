import sys

N = int(sys.stdin.readline())

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

calorie = []
for i in range(N):
    calorie.append(int(sys.stdin.readline()))

calorie.sort(reverse=True)

i = 0
tmp_calorie = C
tmp_cost = A
while True:
    test = (tmp_calorie + calorie[i])/(tmp_cost+B)
    if test >= tmp_calorie/tmp_cost:
        tmp_calorie = tmp_calorie + calorie[i]
        tmp_cost = tmp_cost+B
        i += 1
        if i == len(calorie):
            print(tmp_calorie//tmp_cost)
            break
    else:
        print(tmp_calorie//tmp_cost)
        break