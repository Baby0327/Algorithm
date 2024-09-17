"""
키 큰 사람
"""

while True:
    n = int(input())

    if not n:
        break

    h = 0.0
    name = []
    
    for i in range(n):
        student, height = input().split()
        
        if float(height) > h:
            h = float(height)
            name = [student]
        elif float(height) == h:
            name.append(student)

    print(*name)