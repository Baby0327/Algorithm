"""
점화식
"""

t = [1, 1]

n = int(input())

for i in range(n - 1):
    total = 0
    
    for j in range(len(t)):
        total += t[j] * t[len(t) - j - 1]
        
    t.append(total)

print(t[-1])