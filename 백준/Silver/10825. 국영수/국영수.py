import sys

N = int(sys.stdin.readline())


student = []
for i in range(N):
    tmp = list(sys.stdin.readline().rstrip().split())
    tmp[1], tmp[2], tmp[3] = int(tmp[1]), int(tmp[2]), int(tmp[3])
    student.append(tmp)

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in student:
    sys.stdout.write(i[0]+'\n')