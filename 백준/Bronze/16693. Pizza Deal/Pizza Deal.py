from math import pi

a, p1 = map(int, input().split())
r, p2 = map(int, input().split())
print("Slice of pizza" if a / p1 > r**2 * pi / p2 else "Whole pizza")