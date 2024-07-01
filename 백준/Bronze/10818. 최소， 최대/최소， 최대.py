N = int(input())
num = list(map(int, input().split()))

MIN = 1000000
MAX = -1000000

for i in num:
    if MIN > i:
        MIN = i
    if MAX < i:
        MAX = i

print(MIN, MAX)