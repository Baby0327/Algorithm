result = [[ 0 for i in range(2)] for j in range(20)]

for i in range(20):
    grade = input()
    tmp = grade.split()
    if tmp[2] == 'A+':
        tmp[2] = 4.5
    elif tmp[2] == 'A0':
        tmp[2] = 4.0
    elif tmp[2] == 'B+':
        tmp[2] = 3.5
    elif tmp[2] == 'B0':
        tmp[2] = 3.0
    elif tmp[2] == 'C+':
        tmp[2] = 2.5
    elif tmp[2] == 'C0':
        tmp[2] = 2.0
    elif tmp[2] == 'D+':
        tmp[2] = 1.5
    elif tmp[2] == 'D0':
        tmp[2] = 1.0
    elif tmp[2] == 'F':
        tmp[2] = 0
    elif tmp[2] == 'P':
        tmp[2] = 'no'

    result[i][0] = float(tmp[1])
    result[i][1] = tmp[2]

score = 0
total = 0
for i in range(20):
    if result[i][1] != 'no':
        score += result[i][0]*result[i][1]
        total += result[i][0]
    else:
        result[i][0] = 0

print(score/total)