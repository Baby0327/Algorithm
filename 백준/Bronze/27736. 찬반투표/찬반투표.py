"""
찬반투표
"""

n = int(input())
vote = list(map(int, input().split()))

if vote.count(0) >= n / 2:
    print("INVALID")
else:
    if vote.count(1) > vote.count(-1):
        print("APPROVED")
    else:
        print("REJECTED")