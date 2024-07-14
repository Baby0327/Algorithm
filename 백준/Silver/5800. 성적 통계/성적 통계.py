"""
성적 통계
"""

import sys

K = int(sys.stdin.readline())

for i in range(K):
    score = sorted(list(map(int, sys.stdin.readline().split()))[1:], reverse=True)
    maxi = score[0]
    mini = score[-1]
    gap = max([score[i] - score[i+1] for i in range(len(score) - 1)])
    sys.stdout.write(f"Class {i + 1}\n")
    sys.stdout.write(f"Max {maxi}, Min {mini}, Largest gap {gap}\n")