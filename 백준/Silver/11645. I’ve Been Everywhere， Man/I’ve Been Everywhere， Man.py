"""
I've Been Everywhere, Man
"""

t = int(input())

for i in range(t):
    n = int(input())
    city = set()

    for i in range(n):
        city.add(input())

    print(len(city))