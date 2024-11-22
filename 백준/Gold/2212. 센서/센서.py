import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))
result = sorted([sensor[i + 1] - sensor[i] for i in range(n - 1)])
print(sum(result[:n - k]))