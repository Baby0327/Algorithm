angle = []

for i in range(3):
    n = int(input())
    angle.append(n)

if angle[0] + angle[1] + angle[2] == 180:
    if angle[0] == angle[1] == angle[2] == 60:
        print("Equilateral")
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")