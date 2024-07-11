"""
고급 수학
"""

n = int(input())

for i in range(1, n+1):
    a, b, c = sorted(list(map(int, input().split())))
    print(f"Scenario #{i}:")
    
    if a**2 + b**2 == c**2:
        print("yes\n")
    else:
        print("no\n")