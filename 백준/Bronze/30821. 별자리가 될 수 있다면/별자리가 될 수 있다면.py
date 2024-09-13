"""
별자리가 될 수 있다면
"""

n = int(input())

top = 1
bottom = 1

for i in range(5):
    top *= n - i
    bottom *= i+1

print(top // bottom)