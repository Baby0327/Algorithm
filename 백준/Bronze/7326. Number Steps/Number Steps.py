"""
Number Steps
"""

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    if y in (x, x-2):
        if x % 2 == 0:
            print(x + y)
        else:
            print(x + y - 1)
    else:
        print("No Number")