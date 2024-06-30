import sys

grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
         'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
         'F': 0.0}

N = int(sys.stdin.readline())

total = 0
score_X_num = 0
for i in range(N):
    tmp = sys.stdin.readline().rstrip().split()
    score = grade[tmp[2]]
    score_X_num += score * int(tmp[1])
    total += int(tmp[1])

tmp = list(str(score_X_num/total))
if len(tmp) >= 5:
    if int(tmp[4]) >= 5:
        tmp[3] = int(tmp[3])
        tmp[3] += 1
        tmp[3] = str(tmp[3])
        tmp[4] = '1'
    else:
        tmp[4] = '1'

    result = float("".join(tmp))
    print(round(result, 2))

else:
    print('{:.2f}'.format(score_X_num / total))