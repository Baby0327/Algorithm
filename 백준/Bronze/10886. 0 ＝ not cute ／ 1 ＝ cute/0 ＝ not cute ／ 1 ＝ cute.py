"""
0 = not cute / 1 = cute
"""

n = int(input())
vote = []

for i in range(n):
    vote.append(int(input()))

print( "Junhee is cute!" if vote.count(1) > (n//2) else "Junhee is not cute!")