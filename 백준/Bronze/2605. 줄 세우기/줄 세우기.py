"""
줄 세우기
"""

n = int(input())
order = list(map(int, input().split()))
student = []

for i in range(n):
    student.insert(order[i], i+1)

print(*reversed(student))