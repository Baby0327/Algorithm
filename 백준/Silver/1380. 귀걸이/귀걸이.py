import sys

result = []
num = 0

while True:
    num += 1
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    student = []
    for i in range(n):
        student.append(sys.stdin.readline().rstrip())
    test = []
    for i in range(2*n-1):
        a, b = sys.stdin.readline().rstrip().split()
        test.append(int(a))
    for i in test:
        if test.count(i) == 1:
            result.append([num, student[i-1]])

for i in result:
    print(i[0], i[1])