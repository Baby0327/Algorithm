from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = deque(list(map(int, input().split())))
multi = []
cnt = 0

while item:
    now = item.popleft()

    if now not in multi:
        if len(multi) < n :
            multi.append(now)
        else:
            temp = []

            for i in multi:
                if i in item:
                    temp.append([item.index(i), i])
                else:
                    temp.append([101, i])

            temp.sort(key=lambda x : (-x[0], x[1]))
            multi.remove(temp[0][1])
            multi.append(now)
            cnt += 1

print(cnt)