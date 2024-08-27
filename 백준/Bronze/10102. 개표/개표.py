"""
개표
"""

v = int(input())
result = input()
a = result.count("A")
b = result.count("B")

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")