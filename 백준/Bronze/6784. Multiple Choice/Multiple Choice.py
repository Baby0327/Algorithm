import sys
input = sys.stdin.readline

n = int(input())
answer = [input().rstrip() for _ in range(n)]
print(sum(1 for i in range(n) if input().rstrip() == answer[i]))