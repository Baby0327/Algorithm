import sys

n = int(sys.stdin.readline())

student = []
for i in range(n):
    student.append(list(input().split())[::-1])

student.sort(key=lambda x:(-int(x[0]), -int(x[1]), -int(x[2])))
print(student[0][3])
student.sort(key=lambda x:(int(x[0]), int(x[1]), int(x[2])))
print(student[0][3])