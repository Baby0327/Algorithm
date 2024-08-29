"""
Vending Machine
"""

button = list(map(int, input().split()))
total = button.count(1) * 500 + button.count(2) * 800 + button.count(3) * 1000

print(5000 - total)