"""
Bank Transfer
"""

k = 25 + int(input()) * 0.01

if k < 100:
    k = 100
elif k > 2000:
    k = 2000

print(f"{k:.2f}")