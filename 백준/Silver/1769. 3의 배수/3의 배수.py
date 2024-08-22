"""
3의 배수
"""

x = input()
count = 0

while int(x) >= 10:
    total = 0
    
    for i in x:
        total += int(i)
        
    x = str(total)
    count += 1

print(count)
print("YES" if int(x) % 3 == 0 else "NO")