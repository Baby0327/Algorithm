import sys
input = sys.stdin.readline

n = int(input())
num = [input().rstrip() for _ in range(n)]
i = 1

while 1:
    temp = set(list(map(lambda x : x[-i:], num)))
    
    if len(temp) == n:
        print(i)
        break
    else:
        i += 1