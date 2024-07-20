"""
와글와글 숭고한
"""

s, k, h = map(int, input().split())

if sum([s, k, h]) >= 100:
    print("OK")
else:
    univ = min([s, k, h])
    if univ == s:
        print("Soongsil")
    elif univ == k:
        print("Korea")
    else:
        print("Hanyang")