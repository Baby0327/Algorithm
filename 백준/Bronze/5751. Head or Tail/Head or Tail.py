"""
Head or Tail
"""

while int(input()):
    r = list(map(int, input().split()))
    print(f"Mary won {r.count(0)} times and John won {r.count(1)} times")