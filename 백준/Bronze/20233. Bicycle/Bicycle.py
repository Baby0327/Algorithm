"""
Bicycle
"""

a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

A = a if t <= 30 else a + ((t - 30) * x) * 21
B = b if t <= 45  else b + ((t - 45) * y) * 21

print(A, B)